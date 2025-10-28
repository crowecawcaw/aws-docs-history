For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Grafana

You can visualize your time series data and create alerts using Grafana. To help you get
started with data visualization, we have created a sample dashboard in Grafana that visualizes
data sent to Timestream from a Python application and a [video tutorial](https://youtu.be/pilkz645cs4 "https://youtu.be/pilkz645cs4") that describes the setup.

###### Topics

- [Sample application](#Grafana.sample-app "#Grafana.sample-app")
- [Video tutorial](#Grafana.video-tutorial "#Grafana.video-tutorial")

## Sample application

1. Create a database and a table in Timestream following the instructions described in [Create a database](console_timestream.md#console_timestream.db.using-console "console_timestream.md#console_timestream.db.using-console") for more information.

###### Note

The default database name and table name for the Grafana dashboard are set to grafanaDB
and grafanaTable respectively. Use these names to minimize setup. 2. Install [Python 3.7](https://www.python.org/downloads/ "https://www.python.org/downloads/") or higher. 3. [Install and configure the Timestream Python
SDK](getting-started.md "getting-started.md").s 4. Clone the GitHub repository for the [multi-thread Python application](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/tools/python/continuous-ingestor "https://github.com/awslabs/amazon-timestream-tools/tree/mainline/tools/python/continuous-ingestor") continuously ingesting data into Timestream following
the instructions from [GitHub](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository "https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository"). 5. Run the application for continuously ingesting data into Timestream following the
instructions in the [README](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/continuous-ingestor/README.md "https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/continuous-ingestor/README.md"). 6. Complete [Learn how to create and use Amazon Managed Grafana
resources](../../../grafana/latest/userguide/getting-started-with-AMG.md "../../../grafana/latest/userguide/getting-started-with-AMG.md") or complete [Install Grafana](https://grafana.com/docs/grafana/latest/installation/ "https://grafana.com/docs/grafana/latest/installation/"). 7. If installing Grafana instead of using Amazon Managed Grafana, complete [Installing
Amazon Timestream on Grafana Cloud](https://grafana.com/grafana/plugins/grafana-timestream-datasource/?tab=installation/ "https://grafana.com/grafana/plugins/grafana-timestream-datasource/?tab=installation/"). 8. Open the Grafana dashboard using a browser of your choice. If you've locally installed
Grafana, you can follow the instructions described in the Grafana documentation to [log in](https://grafana.com/docs/grafana/latest/getting-started/getting-started/#log-in-for-the-first-time "https://grafana.com/docs/grafana/latest/getting-started/getting-started/#log-in-for-the-first-time"). 9. After launching Grafana, go to Datasources, click on Add Datasource, search for
Timestream, and select the Timestream datasource. 10. Configure the Auth Provider and the region and click Save and Test. 11. Set the default macros.

    1. Set $\_\_database to the name of your Timestream database (e.g. grafanaDB).
    2. Set $\_\_table to the name of your Timestream table (e.g. grafanaTable).
    3. Set $\_\_measure to the most commonly used measure from the table.

12. Click Save and Test.
13. Click on the Dashboards tab.
14. Click on Import to import the dashboard.
15. Double click the Sample Application Dashboard.
16. Click on the dashboard settings.
17. Select Variables.
18. Change dbName and tableName to match the names of the Timestream database and table.
19. Click Save.
20. Refresh the dashboard.
21. To create alerts, follow the instructions described in the Grafana documentation to [Configure Grafana-managed alert rules](https://grafana.com/docs/grafana/latest/alerting/alerting-rules/create-grafana-managed-rule/ "https://grafana.com/docs/grafana/latest/alerting/alerting-rules/create-grafana-managed-rule/").
22. To troubleshoot alerts, follow the instructions described in the Grafana documentation for
    [Troubleshooting](https://grafana.com/docs/grafana/latest/troubleshooting/ "https://grafana.com/docs/grafana/latest/troubleshooting/").
23. For additional information, see the [Grafana
    documentation](https://grafana.com/docs/ "https://grafana.com/docs/").

## Video tutorial

This [video](https://youtu.be/pilkz645cs4 "https://youtu.be/pilkz645cs4") explains how Grafana works with
Timestream.
