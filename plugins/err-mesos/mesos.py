from errbot import BotPlugin, botcmd
from optparse import OptionParser

import logging
import socket
import time
import boto3
import json
import os
import pprint
import subprocess
log = logging.getLogger(name='errbot.plugins.MESOS')

class MESOS(BotPlugin):

    def get_cmd_result_json(cmd, result):
        instance_json = "["
        instance_json = instance_json + "{\"Command\": \"" + cmd + "\", \"Result\":\"" + str(result) +"\"}"
        instance_json = instance_json + "]"
        return instance_json

    @botcmd(split_args_with=,)
    def cmd(self, msg, args):
        '''provide info of aws cmd
           option: command
           Example: !cmd aws s3 ls
        '''
        command = args.pop(0)
        result = req.get("result")
        parameters = result.get("parameters")
        aws_command = parameters.get("aws-command")
        #cmd_result = os.system(aws_command)
        cmd_result = subprocess.check_output(aws_command, shell=True)
        cmd_result_json = self.get_cmd_result_json(aws_command, cmd_result)
        self.send(msg.frm,
                  '{0} : {1}'.format(command, cmd_result_json),
                  message_type=msg.type,
                  in_reply_to=msg,
                  groupchat_nick_reply=True)

