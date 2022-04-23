import os
from os.path import exists

from grafanaInterface import GrafanaManager

# Grafana Host
DEFAULT_GRAFANA_HOST = 'localhost'
# File location for Grafana admin username and password
DEFAULT_ADMIN_INFO_LOCATION = ''
# Default configuration file path
DEFAULT_CONFIG_FILE_PATH = '/home/mfuser/services/grafana_dashboard/grafanaConfig.txt'
# Default configuration file delimiter
DEFAULT_CONFIG_FILE_DELIMITER = '-'
# Default user information file path
DEFAULT_USER_INFORMATION_PATH = '/home/mfuser/services/grafana_dashboard/userInfo.txt'
# Default user information file delimiter
DEFAULT_USER_INFORMATION_DELIMITER = '='

def getAdminInformation(infoFile):
    """
    Reads in Grafana Username and Password information

    :param infoFile: Path to info file containing Grafana Admin information
    :type infoFile: str
    :return: Grafana admin username
    :rtype: str
    :return: Grafana admin password
    :rtype: str
    """
    username = 'admin'
    password = 'admin'
    
    return username, password

def main():
    response = {
        "success": False,
        "msg": None
    }

    grafanaAdminUsername, grafanaAdminPassword = getAdminInformation(DEFAULT_ADMIN_INFO_LOCATION)

    # Create new Grafana Manager object
    interface = GrafanaManager(
        DEFAULT_GRAFANA_HOST, 
        grafanaAdminUsername, 
        grafanaAdminPassword, 
        DEFAULT_USER_INFORMATION_PATH, 
        DEFAULT_USER_INFORMATION_DELIMITER
    )

    # Create new API token
    tokenCreationStatus = interface.createAdminToken()

    # Check if new API token creation was successful
    if tokenCreationStatus['success']:

        # Create Config File
        configFileCreationStatus = interface.createConfigFile(
            DEFAULT_CONFIG_FILE_PATH, 
            DEFAULT_CONFIG_FILE_DELIMITER
        )

        if configFileCreationStatus['success']:
            response['success'] =  True
            response['msg'] = configFileCreationStatus['msg']
        else:
            response['msg'] = "Failed to create configuration file."

    else:
        response['msg'] = tokenCreationStatus['msg']
        response['data'] = tokenCreationStatus['data']

    return response

if __name__ == "__main__":
    main()