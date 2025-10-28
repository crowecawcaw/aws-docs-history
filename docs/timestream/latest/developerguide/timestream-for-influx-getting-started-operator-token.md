For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Creating a new operator

token for your InfluxDB instance

If you need to get the Operator Token for your new InfluxDB instance, perform the following
steps:

1. To change your operator token, we recommend using the Influx CLI. For instructions,
   please see: [Install and
   use the Influx CLI](https://docs.influxdata.com/influxdb/v2/tools/influx-cli/ "https://docs.influxdata.com/influxdb/v2/tools/influx-cli/").
2. Configure your CLI to use `--username-password` to be able to create the
   operator:

```
influx config create --config-name CONFIG_NAME1  --host-url "https://yourinstanceid.eu-central-1.timestream-influxdb.amazonaws.com:8086" --org [YOURORG]  --username-password [YOURUSERNAME] --active
```

3. Create your new operator token. You will be asked for your password to confirm this
   step.

```
influx auth create --org [YOURORG] --operator

```

###### Important

Once a new operator token has been created, you will need to update any client that is
currently using the old one.
