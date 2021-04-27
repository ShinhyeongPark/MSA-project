from elasticsearch import Elasticsearch, RequestsHttpConnection, helpers
import requests
import json


url = '127.0.0.1'
port = '9200'
es = Elasticsearch(f'{url}:{port}')


def search_category(category, search_keyword):
    index = [category]
    body = {
        "query": {
            "bool": {
            "must": [
                {
                "match": {
                    "item_title.jaso": {
                    "query": search_keyword,
                    "analyzer": "suggest_search_analyzer"
                    }
                }
                }
            ],
            "should": [
                {
                "match": {
                    "item_title.ngram": {
                    "query": search_keyword,
                    "analyzer": "my_ngram_analyzer"
                    }
                },
                }   
            ]
            }
        },
        "highlight":{
            "fields":{
            "item_title.ngram":{}
            }   
        }
    }
    result=es.search(index=index,body=body)
    
    result_list=[]
    for data in result['hits']['hits']:
        result_list.append(data['_source'])
    return result_list

