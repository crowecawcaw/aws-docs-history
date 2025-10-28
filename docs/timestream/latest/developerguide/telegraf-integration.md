For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Telegraf integration with Timestream for InfluxDB 3

Telegraf is a plugin-based data collection agent with over 300 input plugins for collecting
metrics from various sources and output plugins for writing data to different destinations. Its
"plug-and-play" architecture makes it ideal for quickly collecting and reporting
metrics to InfluxDB 3.

## Requirements

- Telegraf 1.9.2 or greater – For installation instructions, see the [Telegraf Installation
  documentation.](https://docs.influxdata.com/telegraf/latest/install/ "https://docs.influxdata.com/telegraf/latest/install/")
- InfluxDB 3 cluster endpoint and credentials.
- Network connectivity to your InfluxDB 3 cluster.

## Telegraf configuration options

Telegraf provides two output plugins compatible with InfluxDB 3:

1. `outputs.influxdb_v2` - Recommended for new deployments.
2. `outputs.influxdb` (v1) - For existing v1 configurations.

### Using the v2 output plugin

We recommend that you use the `outputs.influxdb_v2` plugin to connect to the
InfluxDB v2 compatibility API:

```
[[outputs.influxdb_v2]]
  urls = ["https://your-cluster-endpoint:8086"]
  token = "${INFLUX_TOKEN}"  # Use environment variable for security
  organization = ""           # Can be left empty for InfluxDB 3
  bucket = "DATABASE_NAME"

  ## Optional: Enable gzip compression
  content_encoding = "gzip"

  ## Optional: Increase timeout for high-latency networks
  timeout = "10s"

  ## Optional: Configure batching
  metric_batch_size = 5000
  metric_buffer_limit = 50000

```

### Using the legacy v1 output

plugin

For existing Telegraf configurations using the v1 plugin:

```
[[outputs.influxdb]]
  urls = ["https://your-cluster-endpoint:8086"]
  database = "DATABASE_NAME"
  skip_database_creation = true
  username = "ignored"           # Required but ignored
  password = "${INFLUX_TOKEN}"   # Use environment variable
  content_encoding = "gzip"

  ## Optional: Configure write parameters
  timeout = "10s"
  metric_batch_size = 5000
  metric_buffer_limit = 50000

```

## Basic Telegraf configuration

Example

The following is a complete example that collects system metrics and writes them to
InfluxDB 3:

```
# Global Agent Configuration
[agent]
  interval = "10s"
  round_interval = true
  metric_batch_size = 5000
  metric_buffer_limit = 50000
  collection_jitter = "0s"
  flush_interval = "10s"
  flush_jitter = "0s"
  precision = "s"
  hostname = ""
  omit_hostname = false

# Input Plugins - Collect system metrics
[[inputs.cpu]]
  percpu = true
  totalcpu = true
  collect_cpu_time = false
  report_active = false

[[inputs.disk]]
  ignore_fs = ["tmpfs", "devtmpfs", "devfs", "iso9660", "overlay", "aufs", "squashfs"]

[[inputs.mem]]

[[inputs.net]]
  interfaces = ["eth*", "en*"]

[[inputs.system]]

# Output Plugin - Write to InfluxDB 3
[[outputs.influxdb_v2]]
  urls = ["https://your-cluster-endpoint:8086"]
  token = "${INFLUX_TOKEN}"
  organization = ""
  bucket = "telegraf_metrics"
  content_encoding = "gzip"

```

## Best practices for Telegraf with

InfluxDB 3

- **Security**
  - Store tokens in environment variables or secret stores.
  - Never hardcode tokens in configuration files.
  - Use HTTPS endpoints for production deployments.

- **Performance optimization**
  - Enable gzip compression with content_encoding = "gzip".
  - Configure appropriate batch sizes (5000-10000 metrics).
  - Set buffer limits based on available memory.
  - Use precision appropriate for your use case (seconds often sufficient).

- **Network configuration**
  - For private clusters, run Telegraf within the same VPC.
  - Configure appropriate timeouts for your network latency.
  - Use the writer/reader endpoint for write operations.

- **Monitoring**
  - Enable Telegraf's internal metrics plugin to monitor agent performance.
  - Monitor write errors and retries.
  - Set up alerts for buffer overflow conditions.

- **Data organization**
  - Use consistent tag naming across input plugins.
  - Leverage Telegraf's processor plugins to normalize data.
  - Apply tag filtering to control cardinality.

## Running Telegraf

To start Telegraf with your configuration, do the following:

```
# Test configuration
telegraf --config telegraf.conf --test

# Run Telegraf
telegraf --config telegraf.conf

# Run as a service (systemd)
sudo systemctl start telegraf

```

### Common Telegraf plugins for time

series data

**Popular input plugins:**

- `inputs.cpu`, `inputs.mem`, `inputs.disk` - System metrics.
- `inputs.docker`, `inputs.kubernetes` - Container metrics.
- `inputs.prometheus` - Scrape Prometheus endpoints.
- `inputs.snmp` - Network device monitoring.
- `inputs.mqtt_consumer` - IoT data collection.
- `inputs.http_listener_v2` - HTTP webhook receiver.

**Useful processor plugins:**

- `processors.regex` - Transform tag/field names.
- `processors.converter` - Change field data types.
- `processors.aggregator` - Aggregate metrics.
- `processors.filter` - Filter metrics based on conditions.

By leveraging Telegraf's extensive plugin ecosystem with InfluxDB 3, you can build
comprehensive monitoring solutions that collect data from diverse sources and efficiently write
it to your time-series database.
