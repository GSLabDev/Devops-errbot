from errbot import BotPlugin, botcmd
import os
import requests
import json
import subprocess

class Mesos(BotPlugin):

    @botcmd(admin_only=True)
    def mesosmaster(self, mess, args):
        """ Example: !mesosmaster /version
        """
        
        if not args:
            return 'Please give me a valid endpoint'
            
        endpoint = args
        mesos_url = "http://mesos_master.service.local:5050" + endpoint
        r = requests.post(mesos_url)
        result = r.json()
        return "```\n" + str(result).strip() + "\n```"


    @botcmd(admin_only=True)
    def mesosagent(self, mess, args):
        """ Example: !mesosagent /version
        """

        if not args:
            return 'Please give me a valid endpoint'

        endpoint = args
        mesos_url = "http://mesos_worker.service.local:5051" + endpoint
        r = requests.post(mesos_url)
        result = r.json()
        return "```\n" + str(result).strip() + "\n```"
