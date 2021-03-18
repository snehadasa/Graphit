import requests, json
import hashlib
import base64
from models.product import Product
from os import getenv

URL_SEARCH = "https://affiliate-api.flipkart.net/affiliate/1.0/search.json"
URL_PRODUCT = "https://affiliate-api.flipkart.net/affiliate/1.0/product.json"

headers = { 'Fk-Affiliate-Id' : getenv('FK_AFFILATE_ID'),
            'Fk-Affiliate-Token' : getenv('FK_AFFILIATE_TOKEN'),
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
    result['product_url'] = product['productUrl']
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
    result['prices'] = Product.get_prices(product.product_id)
    result['price_range'] = Product.prices_range(product.product_id)
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
    if response.ok:
        return extract_product(response.json()['productBaseInfoV1'])
    else:
        return None



