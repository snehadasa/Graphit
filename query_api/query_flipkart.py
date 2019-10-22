import requests, json
import hashlib
import base64
from models.product import Product

URL_SEARCH = "https://affiliate-api.flipkart.net/affiliate/1.0/search.json"
URL_PRODUCT = "https://affiliate-api.flipkart.net/affiliate/1.0/product.json"

headers = { 'Fk-Affiliate-Id' : 'sujithejg',
            'Fk-Affiliate-Token' : '1e3c864a20654c95ab56a300906e1d69',
            'Content-Type' : 'application/json',
            }

def transform_query_response(json):
    results = []
    for product_info in json['products']:
        product = product_info['productBaseInfoV1']
        result = extract_product(product)
        results.append(result)
    return results

def extract_product(product):
    result = {}
    result['product_id'] = product['productId']
    result['title'] = product['title']
    result['image_url'] = product['imageUrls']['200x200']
    result['description'] = product['productDescription']
    if product['flipkartSpecialPrice']:
        result['price'] = product['flipkartSpecialPrice']['amount']
    else:
        result['price'] = product['flipkartSellingPrice']['amount']

    product = Product.get_product(result['product_id'])
    if not product:
        args = {'product_id': result['product_id'], 'price': result['price']}
        product = Product(**args)
    else:
        product.price = result['price']
    product.save()
    result['price'] = Product.get_prices(product.product_id)
    return result

def query(query_str):
    params = {
                'query' : query_str,
                'resultCount' : 5
             }
    response = requests.get(URL_SEARCH, headers=headers, params=params)

    # jsonData = json.loads(response)
    json_response = response.json()
    return transform_query_response(json_response)

def query_product(product_id):
    params = {
        'id': product_id
    }
    response = requests.get(URL_PRODUCT, headers=headers, params=params)
    return extract_product(response.json()['productBaseInfoV1'])

if __name__=="__main__":
    Product.get_product('MOBEMK6289R7UFQH')



