import requests, json, pprint, time
import hashlib
import base64

URL_SEARCH = "https://affiliate-api.flipkart.net/affiliate/1.0/search.json"

headers = { 'Fk-Affiliate-Id' : 'sujithejg',
            'Fk-Affiliate-Token' : '1e3c864a20654c95ab56a300906e1d69',
            'Content-Type' : 'application/json',
            }

def query(query_str):
    params = {
                'query' : query_str,
                'resultCount' : 5
             }
    response = requests.get(URL_SEARCH, headers=headers, params=params)
    res = response.json()
    print(res)
    product_id = res['products'][0]['productBaseInfoV1']
    print('\n')
    print(product_id)
    print('\n')
    #for k, v in product_id.items():
    print('\n')
    print(product_id.get("productId"))
    print('\n')
    #return jsonData

if __name__=="__main__":
    query('sony mobile');
    print("\n\n\n\n QUERYING IPOD \n\n\n\n");
    query('ipod')
