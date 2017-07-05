from errbot import BotPlugin, botcmd
import os
import subprocess

class Logs(BotPlugin):

    @botcmd(admin_only=True)
    def logs(self, mess, args):
        """ Example: !logs /home/pi/errbot/errbot.log
        """
        
        if not args:
            return 'Please give me a path to a log-file'
            
        LOGS_PATH = os.environ.get('LOGS_PATH', args)

        if not os.path.exists(LOGS_PATH):
            return ('ERROR: the file does not exist')

        p = subprocess.Popen(['/usr/bin/tail', '-n10', args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "```\n" + p.stdout.read().decode().strip() + "\n```"
