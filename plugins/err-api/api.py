from errbot import BotPlugin, botcmd
from configuration_manager import configuration_manager
import os
import requests
import json
import subprocess
import yaml

class Api(BotPlugin):

    @botcmd(admin_only=True)
    def get(self, mess, args):
        """ Example: !get mesosmaster stats
        """ 
        if not args:
            return 'Please give me a valid a parameters. Try running !get help'

        arguments = args.split()
        service = arguments[0]
        if len(arguments) > 1:
           endpoint = arguments[1]
        with open("/app/api_conf.yml", 'r') as stream:
          try:
             config = yaml.load(stream)
             api_manager = configuration_manager.get_instance(config)
             if service == "help" or endpoint == "help":
                print("Inside if")
                response = api_manager.get_help("get", service)
             else:
                print("Inside else")
                response = api_manager.get_response("get", service, endpoint)
          except yaml.YAMLError as exc:
             print(exc)

        return "```\n" + str(response).strip() + "\n```"


    @botcmd(admin_only=True)
    def post(self, mess, args):
        """ Example: !mesosagent /version
        """

        if not args:
            return 'Please give me a valid endpoint'

        endpoint = args
        return "```\n" + str(result).strip() + "\n```"
