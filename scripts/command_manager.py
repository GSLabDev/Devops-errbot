from function_manager import function_manager
from function_manager import function_config
import command_utils
import logging

log = logging.getLogger(__name__)

class command_config( function_config ):
	def __init__(self, command_config):
           config = command_config


class command_manager( function_manager ):
    def __init__(self, command_config):
        self.config = command_config["api"]


    def get_help(self, method, service):
        response = ""
        if service == "help":
           response = command_utils.get_help(self.config[method])
        else:
           response = command_utils.get_service_help(self.config[method], service)
        return response

    def get_response(self, method, service, endpoint):
        url = ""
        for webservice in self.config[method]:
            if webservice["service"] == str(service):
               url = webservice["url"]
               for endpoints in webservice["endpoints"]:
                   if endpoints["name"] == str(endpoint):
                      print(endpoints)
                      print(url)
                      result = command_utils.call_webservice(endpoints, method, url)
                      print(result)
                      response = command_utils.get_response(endpoints, result)
                      return response
        
        
