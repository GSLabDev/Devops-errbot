from function_manager import function_manager
from function_manager import function_config
import api_utils

class api_config( function_config ):
	def __init__(self, api_config):
           config = api_config


class api_manager( function_manager ):
    def __init__(self, api_config):
        self.config = api_config["api"]


    def get_help(self, method, service):
        response = ""
        if service == "help":
           response = api_utils.get_help(self.config[method])
        else:
           response = api_utils.get_service_help(self.config[method], service)
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
                      result = api_utils.call_webservice(endpoints, method, url)
                      response = api_utils.get_response(endpoints, result)
                      return response
        
        
