# GraphIt ~ *Shopping Made Easier*

![logo](https://datavizcatalogue.com/methods/images/top_images/area_graph.png)

# Introduction

## The Project

**GraphIt** is a price comparision site for an Indian ecommerce website [Flipkart](https://www.flipkart.com/). This website is open for all users. Users can search for desired products and it redirects to the search page where they can click on track button and the product price gets tracked. Users can view the tracked items in their customer product mapper page.

## The Context
This project is my Portfolio Project. This project is a part of Foundations Year at [Holberton School](https://www.holbertonschool.com/).

## The Team

This is my solo project. I got this idea when i was searching ideas about my portfolio project and thought to do a price trackr tool and also thought why not do it for an Indian website.

**Sneha Dasa Lakshminath** [@snehadasa](https://twitter.com/DasaSneha) - Former junior architect. Passionate Software Engineer in progress.

Follow me on twitter.

## Deployment
Deployment of the project was done using DigitalOcean

## Overview
**GraphIt** is coded mainly in python. I used mysql for the database, Flask for the web framework, jinja as a wrapper for html. For the frontend, i used HTML, CSS and JavaScript for a dynamic designing of my webpage. I used Flipkart ecommerce api to get the data about the products. I set up a chronjob which automatically schedules a job to update prices everyday at midnight.

### Flipkart API
For this project i used flipkart ecommerce api to get data about the products. I was limited to get only 5 products at a time. 

```

def transform_query_response(json):
    results = []
    for product_info in json['products']:
        product = product_info['productBaseInfoV1']
        result = extract_product(product)
        results.append(result)
    return results

def query(query_str):
    params = {
                'query' : query_str,
                'resultCount' : 5
             }
    response = requests.get(URL_SEARCH, headers=headers, params=params)

    # jsonData = json.loads(response)
    json_response = response.json()
    return transform_query_response(json_response)
```

### Chronjob
A cron job is a Linux command for scheduling a task. This is normally used to schedule a job that is executed periodically i.e., i set up a chronjob to update prices for the tracking at midnight.

```
 def update_prices():
        """Update prices of all customer"""
        customer_product_mappings = models.storage.get_session().query(CustomerProductMapping).all()
        product_ids = {}
        for customer_product_mapping in customer_product_mappings:
            product_id = customer_product_mapping.product_id
            if product_id not in product_ids.keys():
                print(product_id)
                product_ids[product_id] = True
                product = Product.get_product(product_id)
                if not product:
                    query_product(product_id)
```

# Acknowledgments

I would like to thank holberton School staff for constant support through out the project, my peers for their invaluable support, and my dearest husband Sujith for his regardless amount of help in the material.

#Resources

These are some of the links to the material which was helpful during this project,

* [chronjob](https://www.taniarascia.com/setting-up-a-basic-cron-job-in-linux/)
* [camelcamelcamel](https://camelcamelcamel.com/)
* [Flask](https://realpython.com/tutorials/flask/)
* [API](https://www.dataquest.io/blog/python-api-tutorial/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
