from GrafanaManager.grafanaInterface import GrafanaManager

# Default location for uploaded JSON dashboards
DEFAULT_DASHBOARD_DIRECTORY = '/home/mfuser/services/grafana_dashboard/files'
# Default configuration file name
DEFAULT_CONFIG_FILE_PATH = '/home/mfuser/services/grafana_dashboard/grafanaConfig.txt'
# Default configuration file delimiter
DEFAULT_CONFIG_FILE_DELIMITER = '-'

def main():
    interface = GrafanaManager()

    # Read from config file
    interface.parseConfigFile(DEFAULT_CONFIG_FILE_PATH, DEFAULT_CONFIG_FILE_DELIMITER)

    # Upload each dashboard to Grafana
    result = interface.uploadDashboards(DEFAULT_DASHBOARD_DIRECTORY)

    return result
    
if __name__ == "__main__":
    main()