import requests, json, pprint, time
import hashlib
import base64

URL_SEARCH = "https://affiliate-api.flipkart.net/affiliate/1.0/search.json"

headers = { 'Fk-Affiliate-Id' : 'sujithejg',
            'Fk-Affiliate-Token' : '1e3c864a20654c95ab56a300906e1d69',
            'Content-Type' : 'application/json',
            }

#def query(query_str):
#params = {
            #'query' : query_str,
         #}
response = requests.get(URL_SEARCH, headers=headers)
print(response)
res_text = response.text
print(type(res_text))
print(res_text)

res = response.json()
print(type(res))
print(res)
res["products"] = [dict(productId = pr["productId"], title = pr["title"], attributes = pr["attributes"]) for pr in res["products"]]
jsonProducts = json.dump(res)
#product_id = res['products'][0]['productBaseInfoV1']
with open("products.json", mode='w') as file:
    json.dump(json_f, file)

#if __name__ == "__main__":
    #query("ipod")
