
from api_manager import api_manager
from command_manager import command_manager

class configuration_manager( object ):
    @staticmethod
    def get_instance(config):
        if config.get("api") != None:
            return api_manager(config)
        elif config.get("command") != None:
            return command_manager(config)

        raise("Unsupported api type")
