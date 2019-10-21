import requests, json
import hashlib
import base64

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
    result['image_url'] = product['imageUrls']['400x400']
    result['description'] = product['productDescription']
    if product['flipkartSpecialPrice']:
        result['price'] = product['flipkartSpecialPrice']['amount']
    else:
        result['price'] = product['flipkartSellingPrice']['amount']
    return result;

def query(query_str):
    params = {
                'query' : query_str,
                'resultCount' : 5
             }
    response = requests.get(URL_SEARCH, headers=headers, params=params)
    #jsonData = json.loads(response)
    return transform_query_response(response.json())

def query_product(product_id):
    params = {
        'id': product_id
    }
    response = requests.get(URL_PRODUCT, headers=headers, params=params)
    return extract_product(response.json()['productBaseInfoV1']);

if __name__=="__main__":
    print(query('iphone'))
    print(query_product('MOBEJB94H7G2FGRW'))



