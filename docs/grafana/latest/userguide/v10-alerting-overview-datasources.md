# Data sources and Grafana

alerting

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

There are a number of data sources that are compatible with Grafana Alerting.
Each data source is supported by a plugin. Grafana alerting requires that data
source plugins be _backend_ plugins, in order to evaluate rules
using the data source, because the evaluation engine runs on the backend. Plugins
must also specify that they are compatible with Grafana alerting.

Data sources are added and updated over time. The following data sources are
known to be compatible with Grafana alerting.

- [Connect to an Amazon CloudWatch
  data source](using-amazon-cloudwatch-in-AMG.md "using-amazon-cloudwatch-in-AMG.md")
- [Connect to an Azure Monitor data
  source](using-azure-monitor-in-AMG.md "using-azure-monitor-in-AMG.md")
- [Connect to an Amazon OpenSearch Service data
  source](using-Amazon-OpenSearch-in-AMG.md "using-Amazon-OpenSearch-in-AMG.md")
- [Connect to a Google Cloud
  Monitoring data source](using-google-cloud-monitoring-in-grafana.md "using-google-cloud-monitoring-in-grafana.md")
- [Connect to a Graphite data source](using-graphite-in-AMG.md "using-graphite-in-AMG.md")
- [Connect to an InfluxDB data source](using-influxdb-in-AMG.md "using-influxdb-in-AMG.md")
- [Connect to a Loki data source](using-loki-in-AMG.md "using-loki-in-AMG.md")
- [Connect to a Microsoft SQL
  Server data source](using-microsoft-sql-server-in-AMG.md "using-microsoft-sql-server-in-AMG.md")
- [Connect to a MySQL data source](using-mysql-in-AMG.md "using-mysql-in-AMG.md")
- [Connect to an OpenTSDB data source](using-opentsdb-in-AMG.md "using-opentsdb-in-AMG.md")
- [Connect to a PostgreSQL data
  source](using-postgresql-in-AMG.md "using-postgresql-in-AMG.md")
- [Connect to Amazon Managed Service for Prometheus and open-source Prometheus
  data sources](prometheus-data-source.md "prometheus-data-source.md")
- [Connect to a Jaeger data source](jaeger-data-source.md "jaeger-data-source.md")
- [Connect to a Zipkin data source](zipkin-data-source.md "zipkin-data-source.md")
- [Connect to a Tempo data source](tempo-data-source.md "tempo-data-source.md")
- [Configure a TestData data source for
  testing](testdata-data-source.md "testdata-data-source.md")
  For more detailed information about data sources and data source plugins in
  Amazon Managed Grafana, see [Connect to data sources](AMG-data-sources.md "AMG-data-sources.md").
