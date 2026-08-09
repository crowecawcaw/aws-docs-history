# Amazon CloudWatch solution: Amazon OpenSearch Service insights

This solution helps you monitor your Amazon OpenSearch Service domains in CloudWatch without
running or scaling your own collection infrastructure. A Amazon CloudWatch managed Prometheus collector
connects to your VPC, collects cluster, node, and index metrics from the domain, and delivers
them to CloudWatch. For general information about all CloudWatch observability solutions, see [CloudWatch observability solutions](Monitoring-Solutions.md "Monitoring-Solutions.md"). For the complete
collector setup walkthrough, including scraper creation and the example scrape configuration,
see [Integrate Amazon OpenSearch Service](managed-prometheus-collectors-opensearch-setup.md "managed-prometheus-collectors-opensearch-setup.md").

###### Topics

- [Requirements](#Solution-Prometheus-On-OpenSearch-Requirements "#Solution-Prometheus-On-OpenSearch-Requirements")
- [Enable the managed collector](#Solution-Prometheus-On-OpenSearch-Enable-Collector "#Solution-Prometheus-On-OpenSearch-Enable-Collector")
- [Validate metrics collection](#Solution-Prometheus-On-OpenSearch-Validate "#Solution-Prometheus-On-OpenSearch-Validate")
- [Build a custom dashboard](#Solution-Prometheus-On-OpenSearch-Dashboards "#Solution-Prometheus-On-OpenSearch-Dashboards")
- [Costs](#Solution-Prometheus-On-OpenSearch-Costs "#Solution-Prometheus-On-OpenSearch-Costs")

## Requirements

This solution is relevant for the following conditions:

- An Amazon OpenSearch Service domain with VPC access. Managed collectors support only
  domains that have VPC access. Domains with public access are not supported.
- Amazon VPC with DNS enabled, and at least two subnets in different Availability
  Zones for the collector.
- A security group that allows the collector to reach your domain endpoint over HTTPS
  (port 443).

## Enable the managed collector

To collect Amazon OpenSearch Service metrics with a managed collector, you create a
VPC-connected collector that connects to your domain and delivers metrics to your CloudWatch
dataset. You specify the domain to collect from in the `exporters` field of the
request, and provide the networking in the `source` field. For step-by-step
instructions, see [Integrate Amazon OpenSearch Service](managed-prometheus-collectors-opensearch-setup.md "managed-prometheus-collectors-opensearch-setup.md").

## Validate metrics collection

Within minutes, metrics begin flowing to your CloudWatch dataset. To confirm that your metrics
arrive, run an ad-hoc query in CloudWatch using [Query
Studio](CloudWatch-PromQL-QueryStudio.md "CloudWatch-PromQL-QueryStudio.md"). For example, the following query returns the cluster health status for your
domain:

```
opensearch_cluster_health_status
```

## Build a custom dashboard

After the collector begins delivering your Amazon OpenSearch Service metrics to CloudWatch, you
can build a custom CloudWatch dashboard to visualize them. With custom dashboards, you can combine
the collected metrics into widgets, add PromQL-based queries, and organize the widgets to fit
your monitoring needs. For more information, see [Using CloudWatch
dashboards](CloudWatch_Dashboards.md "CloudWatch_Dashboards.md").

## Costs

We charge for Prometheus collectors by the hour, and CloudWatch OpenTelemetry metric ingestion pricing applies. For more information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
