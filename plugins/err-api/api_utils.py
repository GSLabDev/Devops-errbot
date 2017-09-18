import yaml
import json
import requests
import os

def get_help(config):
    response = ""
    print(config)
    for webservice in config:
        response = response + " \n" + str(webservice["service"]) + " : " + str(webservice["help"])
        for endpoints in webservice["endpoints"]:
            response = response + " \n " + str(endpoints["name"]) + " : " + str(endpoints["help"])
    return response


def get_service_help(config, service):
    response = ""
    print(config)
    for webservice in config:
        if webservice["service"] == str(service):
           response = response + " \n" + str(webservice["service"]) + " : " + str(webservice["help"])
           for endpoints in webservice["endpoints"]:
               response = response + " \n " + str(endpoints["name"]) + " : " + str(endpoints["help"])
    return response

def call_webservice(config, method, url):
    api_url = str(url) + str(config["path"])
    result = ""
    if str(method) == "get":
       result = requests.get(api_url)
    elif str(method) == "post":
       result = requests.post(api_url)
    return result.json()


def get_response(config, result):
    response = ""
    for item in config["response_fields"]:
        for i in item:
	        response = response + " \n " + i + " : " + result[i]
    return response
