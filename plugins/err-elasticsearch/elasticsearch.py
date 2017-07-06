from errbot import BotPlugin, botcmd
import os
import requests
import json
import subprocess

class Elasticsearch(BotPlugin):

    ELASTIC_USERNAME = ""
    ELASTIC_PASSWORD = ""

    @botcmd(admin_only=True)
    def elasticsearch(self, mess, args):
        """ Example: !elasticsearch 
        """
        
        if not args:
            return 'Please give me a valid endpoint'
            
        endpoint = args
        ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL', "https://elasticsearch-elk.service.local:9200")
        es_url = ELASTICSEARCH_URL + endpoint
        r = requests.post(es_url)
        result = r.json()
        return "```\n" + str(result).strip() + "\n```"


    @arg_botcmd('--username', dest='Username', type=str)
    @arg_botcmd('--password', dest='Password', type=str)
    def escredentials(self, mess, Username=None, Password=None):
        """ Example: !escredentials --username esuser --password changeme
        """
        print("----------------------------------")
        print(Username)
        print(Password)
        if not Username:
            return 'Please give me a username'
        if not Password:
            return 'Please give me a password'

        return "```\n Credentials set successfully \n```"


