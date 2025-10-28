# Configure Node-RED flows for AWS IoT SiteWise data

integration

With Node-RED®, you can implement two flows to manage data between your devices and
AWS IoT SiteWise. These flows work together to create a comprehensive data management solution that
addresses both local and cloud data flow.

- **Data publish flow** – Publishes to the cloud.
  The data publish flow sends data to AWS IoT SiteWise. This flow simulates a turbine device by
  generating sensor data, translating it to AWS IoT SiteWise format, and publishing to the SiteWise Edge
  MQTT broker. This enables you to leverage AWS IoT SiteWise's cloud capabilities for storage,
  analytics, and integration with other AWS services.

For more information, see [Configure the data publish
flow](windows-nodered-data-publish-flow.md "windows-nodered-data-publish-flow.md").

- **Data retention flow** – Stores data at the
  edge. The data retention flow subscribes to the SiteWise Edge MQTT broker to receive data,
  translate it into InfluxDB® format, and stores it locally for monitoring. This
  local storage provides immediate access to operational data, reduces latency for
  time-critical applications, and ensures continuity during network disruptions.

For more information, see [Configure the data retention
flow](windows-nodered-data-retention-flow.md "windows-nodered-data-retention-flow.md").
These two flows work together to ensure data is both sent to AWS IoT SiteWise and stored locally
for immediate access.

To access your Node-RED console, go to [http://127.0.0.1:1880](http://127.0.0.1:1880 "http://127.0.0.1:1880"). For information about enabling TLS, see [Enable TLS
encryption](https://docs.influxdata.com/influxdb/v2/admin/security/enable-tls/ "https://docs.influxdata.com/influxdb/v2/admin/security/enable-tls/").
