# Set up local storage with InfluxDB

With InfluxDB®, you can store time series data from your devices locally. The
purpose of local storage capability is to maintain operational visibility during network
disruptions and reduce latency for time-critical applications. You can perform analysis and
visualization at the edge while still having the option to selectively forward data to the
cloud.

In this section, you create a time series bucket for turbine wind speed data and
generate an API token for Grafana® and Node-RED® connectivity. The InfluxDB
bucket serves as a dedicated storage container for your time series data, similar to a
database in traditional systems. The API token enables secure programmatic access to your
data.

###### To set up InfluxDB

1. After completing the prerequisite steps and ensuring all tools are running on the
   same host, open your web browser and go to [http://127.0.0.1:8086](http://127.0.0.1:8086 "http://127.0.0.1:8086").
2. (Optional) Enable TLS encryption for enhanced security. For more information, see
   [Enable
   TLS encryption](https://docs.influxdata.com/influxdb/v2/admin/security/enable-tls/ "https://docs.influxdata.com/influxdb/v2/admin/security/enable-tls/") in the _InfluxData Documentation_.
3. Create a time series InfluxDB bucket to store data from Node-RED. The bucket will
   serve as a dedicated container for your wind farm data, allowing you to organize and
   manage retention policies specific to this dataset. For more information, see [Manage buckets](https://docs.influxdata.com/influxdb/v2/admin/buckets/ "https://docs.influxdata.com/influxdb/v2/admin/buckets/") in
   the _InfluxData Documentation_.
4. (Optional) Configure the data retention period for your edge location. Setting
   appropriate retention periods helps manage storage resources efficiently by
   automatically removing older data that's no longer needed for local operations.

For information about data retention, see [Data
retention in InfluxDB](https://docs.influxdata.com/influxdb/v2/reference/internals/data-retention/ "https://docs.influxdata.com/influxdb/v2/reference/internals/data-retention/") in the _InfluxData Documentation_. 5. Generate an API token for the bucket. This token will enable secure communication
between InfluxDB and other components like Node-RED and Grafana. This way, only
authorized services can read from or write to your data store. For more information, see
[Create a token](https://docs.influxdata.com/influxdb/cloud/admin/tokens/create-token/ "https://docs.influxdata.com/influxdb/cloud/admin/tokens/create-token/") in the _InfluxData Documentation_.
After you complete these steps, you can store time series data in your InfluxDB
instance, providing a foundation for local data persistence and analysis in your edge
environment.
