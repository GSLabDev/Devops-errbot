from errbot import BotPlugin, botcmd
import os
import subprocess

class Aws(BotPlugin):

    @botcmd(admin_only=True )
    def cmd(self, mess, args):
        """ Example: !cmd aws s3 ls
        """
        
        if not args:
            return 'Please give me a command'
            
        command = args

        p = subprocess.check_output(command, shell=True)
        return "```\n" + str(p).strip() + "\n```"
