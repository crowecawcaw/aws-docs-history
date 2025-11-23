# Monitor an MSK Provisioned cluster with

Prometheus

You can monitor your MSK Provisioned cluster with Prometheus, an open-source
monitoring system for time-series metric data. You can publish this data to Amazon
Managed Service for Prometheus using Prometheus's remote write feature. You can also use
tools that are compatible with Prometheus-formatted metrics or tools that integrate with
Amazon MSK Open Monitoring, such as [Datadog](https://docs.datadoghq.com/integrations/amazon_msk/ "https://docs.datadoghq.com/integrations/amazon_msk/"), [Lenses](https://docs.lenses.io/latest/deployment/configuration/agent/automation/kafka/aws-msk "https://docs.lenses.io/latest/deployment/configuration/agent/automation/kafka/aws-msk"), [New Relic](https://docs.newrelic.com/docs/integrations/amazon-integrations/aws-integrations-list/aws-managed-kafka-msk-integration "https://docs.newrelic.com/docs/integrations/amazon-integrations/aws-integrations-list/aws-managed-kafka-msk-integration"), and [Sumo logic](https://help.sumologic.com/03Send-Data/Collect-from-Other-Data-Sources/Amazon_MSK_Prometheus_metrics_collection "https://help.sumologic.com/03Send-Data/Collect-from-Other-Data-Sources/Amazon_MSK_Prometheus_metrics_collection"). Open monitoring is available for free but charges apply for the
transfer of data across Availability Zones.

For information about Prometheus, see the [Prometheus documentation](https://prometheus.io/docs "https://prometheus.io/docs").

For information about using Prometheus, see [Enhance operational insights for Amazon MSK using Amazon Managed Service for Prometheus and Amazon Managed Grafana](https://aws.amazon.com/blogs//big-data/enhance-operational-insights-for-amazon-msk-using-amazon-managed-service-for-prometheus-and-amazon-managed-grafana/ "https://aws.amazon.com/blogs//big-data/enhance-operational-insights-for-amazon-msk-using-amazon-managed-service-for-prometheus-and-amazon-managed-grafana/").

###### Note

KRaft metadata mode and MSK Express brokers can't have open monitoring and public
access both enabled.
