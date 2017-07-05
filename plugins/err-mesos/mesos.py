from errbot import BotPlugin, botcmd
import os
import requests
import json
import subprocess

class Mesos(BotPlugin):

    @botcmd(admin_only=True)
    def mesos(self, mess, args):
        """ Example: !mesos /health
        """
        
        if not args:
            return 'Please give me a valid endpoint'
            
        endpoint = args
        mesos_url = "http://10.0.10.10:5050" + endpoint
        r = requests.post(mesos_url)
        result = r.json()
        return "```\n" + str(result).strip() + "\n```"

