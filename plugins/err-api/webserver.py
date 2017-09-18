#!/bin/python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from json2html import *

import pprint
import subprocess

import boto.ec2
import boto.ec2.cloudwatch
import boto.s3.connection
import datetime

from flask import Flask
from flask import request
from flask import make_response
from configuration_manager import configuration_manager
import os
import requests
import json
import subprocess
import yaml


# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    result = "No result found"
    intent = req.get("result").get("metadata").get("intentName")
    action = req.get("result").get("action")
    if intent.startswith('api-'):
       result = api_call(req, action)
    elif intent == "command":
       result = run_aws_command(req)
    result_json = json.dumps(result)
    data = json.loads(result_json)
    res = makeWebhookResult(req, result_json)
    return res

def api_call(req, endpoint):

    result = req.get("result")
    api_name = result.get("parameters").get("api_name")
    method = result.get("parameters").get("method")
    return get_response(api_name, endpoint, method)

def get_response(api_name, endpoint, method):
    response = ""
#    with open("/app/api_conf.yml", 'r') as stream:
    with open("api_conf.yml", 'r') as stream:
          try:
             config = yaml.load(stream)
             api_manager = configuration_manager.get_instance(config)
             if endpoint == "help":
                response = api_manager.get_help(method, api_name)
             else:
                response = api_manager.get_response(method, api_name, endpoint)
          except yaml.YAMLError as exc:
             print(exc)
    return str(response).strip()

def makeWebhookResult(req, data):
    result = req.get("result")
    print(data)
    text_message = data
    display = "Below are the details"
    slack_message = {
        "text": display,
        "attachments": [
            {
                "title": "Metrics Details",
                "color": "#36a64f",
                "text": text_message
            }
        ]
    }

    speech = " Details : " + text_message

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        "data": {"slack": slack_message},
        # "data": data,
        # "contextOut": [],
        "source": "aws-metrics-apis"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 6000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')


