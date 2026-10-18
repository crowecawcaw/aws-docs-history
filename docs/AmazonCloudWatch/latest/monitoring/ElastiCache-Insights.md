

# ElastiCache Insights
<a name="ElastiCache-Insights"></a>

With ElastiCache Insights, you can monitor and troubleshoot your node‐based Amazon ElastiCache for Valkey clusters. ElastiCache Insights is a prebuilt dashboard in the CloudWatch console. It shows the OpenTelemetry metrics from your cache engine and from the host that each node runs on.

For complete information about ElastiCache OpenTelemetry metrics, including supported configurations, metric attributes, example PromQL queries, and the metrics reference, see [Monitoring ElastiCache with OpenTelemetry metrics](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/otel-metrics.html) in the *Amazon ElastiCache User Guide*.

## Key capabilities
<a name="ElastiCache-Insights-capabilities"></a>
+ **Vended metrics at no additional cost.** ElastiCache emits a core set of metrics automatically, at 60‐second granularity, as soon as the cluster is running. You don't need to configure anything.
+ **Detailed monitoring.** Select any metric with a resource metrics configuration to emit it at 15‐second granularity. For more information, see [CloudWatch detailed monitoring for OpenTelemetry metrics](resource-metrics-configuration.md).
+ **Rich attributes.** Every datapoint carries attributes that identify the account, Region, Availability Zone, replication group, shard, and node, so that you can filter and aggregate at query time.
+ **PromQL query support.** Query metrics in Query Studio, create alarms from PromQL queries, add queries to dashboards, or query from Amazon Managed Grafana. For more information, see [Query metrics with PromQL](CloudWatch-PromQL.md).
+ **Customizable dashboard.** Use the prebuilt dashboard as is, or save a copy as a custom dashboard to add or remove widgets, or to combine ElastiCache metrics with metrics from other sources. Changes to a copy don't affect the prebuilt dashboard.

## Supported configurations
<a name="ElastiCache-Insights-supported"></a>

All node‐based Valkey clusters emit OpenTelemetry metrics, on any Valkey version, except clusters on AWS Outposts. Serverless caches, Redis OSS, and Memcached don't emit OpenTelemetry metrics.

## How to access
<a name="ElastiCache-Insights-access"></a>

**To open the ElastiCache Insights dashboard**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Infrastructure monitoring**, **ElastiCache Insights**.

You can also open the dashboard from the **Metrics** tab of a cluster in the ElastiCache console.

## Pricing
<a name="ElastiCache-Insights-pricing"></a>

ElastiCache Insights is priced on CloudWatch OpenTelemetry metrics ingestion. The dashboard and the core set of vended metrics are free. When you select metrics for detailed monitoring, you pay the standard CloudWatch OpenTelemetry metrics ingestion price for the additional datapoints emitted. PromQL queries that run in the CloudWatch console are free. Queries through the CloudWatch API, including from Amazon Managed Grafana, and PromQL alarms are charged separately. If you save a copy of the dashboard, the copy is billed as a custom dashboard. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).