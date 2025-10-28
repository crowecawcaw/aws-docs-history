# Process data for open source

integrations

The data can be processed (such as transformation or aggregation), at different stages
using various tools, each serving different monitoring requirements.

## Process data with Node-RED nodes

Transform your data in real time using Node-RED® built-in processing nodes.
Configure these nodes through the Node-RED console to create your data pipeline.

### Data transformation nodes

Transform individual data points, similar to Transforms in AWS IoT SiteWise, using these
nodes:

- **change node** - Performs simple value modifications
  on your data.
- **function node** - Enables custom JavaScript
  transformations for complex data processing.

### Metrics calculation nodes

Combine multiple data points into a single output, similar to Metrics in AWS IoT SiteWise, using
these nodes:

- **batch node** - Groups multiple messages for batch
  processing.
- **join node** - Combines multiple data streams into a
  single output.
- **aggregator node** - Calculates aggregate metrics
  from multiple data points.

For additional node options, see the [Node-RED
Library](https://flows.nodered.org/ "https://flows.nodered.org/").

## Create InfluxDB tasks

While Node-RED excels at basic data processing with quick setup, complex metric
calculations may become challenging in flow-based programming. InfluxDB® Tasks provide
an alternative through scheduled Flux scripts for advanced processing needs.

Use InfluxDB Tasks for:

- Statistical aggregations across large datasets
- Mathematical operations on multiple properties
- Derived measurements from multiple sources

### Task features

- **Scheduled Execution** - Run tasks based on cron
  expressions
- **Batch Processing** - Optimize operations for
  time-series data
- **Error Recovery** - Automatically retry failed
  operations
- **Monitoring** - Track execution through detailed
  logs

Manage tasks through the InfluxDB UI, API, or CLI. For more information, see [Process data with
InfluxDB tasks](https://docs.influxdata.com/influxdb/cloud/process-data/ "https://docs.influxdata.com/influxdb/cloud/process-data/").

## Use Grafana transformations

Transform data visualization in Grafana® without modifying the source data in
InfluxDB. Grafana transformations apply only to the visualization layer.

- **Visual Builder** - Create transformations without
  writing code
- **Live Preview** - View transformation results in real
  time
- **Multi-Source** - Process data from multiple database
  sources
- **Storage Efficient** - Transform data at visualization
  time without storing intermediary results

For more information, see [Transform
data](https://grafana.com/docs/grafana/latest/panels/transform-data/ "https://grafana.com/docs/grafana/latest/panels/transform-data/").
