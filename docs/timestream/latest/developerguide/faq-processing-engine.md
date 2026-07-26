For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Processing engine FAQ for Amazon Timestream for InfluxDB 3

Questions about extending Amazon Timestream for InfluxDB 3 with the built-in processing engine and Python plugins. For the complete guide, see [Extend Timestream for InfluxDB with processing engine plugins](processing-engine.md "processing-engine.md").

**What is the processing engine?**

The processing engine lets you run custom Python plugins directly inside your InfluxDB 3 cluster. Plugins can respond to data writes, run on a schedule, or be triggered by HTTP requests. This enables real-time data transformation, alerting, and automation without external infrastructure. For getting started with plugins, see the [InfluxDB 3 Enterprise processing engine documentation](https://docs.influxdata.com/influxdb3/enterprise/plugins/ "https://docs.influxdata.com/influxdb3/enterprise/plugins/").

**What types of plugins are supported?**

InfluxDB 3 supports three plugin trigger types: write triggers (execute when data is written), schedule triggers (execute on a cron-like schedule), and request triggers (execute in response to HTTP requests). InfluxData also provides certified plugins for common use cases such as downsampling, anomaly detection, and forecasting. For the full plugin catalog, see the [InfluxDB 3 plugin library](https://docs.influxdata.com/influxdb3/enterprise/plugins/library/ "https://docs.influxdata.com/influxdb3/enterprise/plugins/library/").

**Can I run my own custom plugins?**

Yes. In addition to the InfluxData certified plugins, you can run your own Python plugins hosted in a plugin repository that you control—public or private. You configure the repository on a DB parameter group, apply it to your cluster, and reference plugins in triggers with the `gh:` prefix. Custom plugins run on both Core and Enterprise editions. For details, see [Use custom plugins with the processing engine](influxdb3-custom-plugins.md "influxdb3-custom-plugins.md").
