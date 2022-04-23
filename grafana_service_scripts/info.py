from grafanaInterface import GrafanaManager

# Default user information file path
DEFAULT_USER_INFORMATION_PATH = '/home/mfuser/services/grafana_dashboard/userInfo.txt'
# Default user information file delimiter
DEFAULT_USER_INFORMATION_DELIMITER = '='

def main():
    interface = GrafanaManager()

    # Assign user information file to new instance of Grafana Manager
    interface.setUserInfoFile(DEFAULT_USER_INFORMATION_PATH, DEFAULT_USER_INFORMATION_DELIMITER)

    # Read all user information from user information file
    userInformationData = interface.getAllUserInfo()

    return userInformationData

if __name__ == "__main__":
    main()