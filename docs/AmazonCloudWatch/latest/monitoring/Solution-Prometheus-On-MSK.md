# Amazon CloudWatch solution: Amazon MSK insights

This solution helps you monitor your Amazon MSK clusters in CloudWatch without running or
scaling your own collection infrastructure. When you enable Open Monitoring on an Amazon MSK
cluster, the cluster exposes Prometheus metrics through the JMX Exporter and Node
Exporter, and an
Amazon CloudWatch managed Prometheus collector scrapes those metrics and delivers them to CloudWatch. For
general information about all CloudWatch observability solutions, see [CloudWatch observability solutions](Monitoring-Solutions.md "Monitoring-Solutions.md"). For the complete
collector setup walkthrough, including scraper creation and the example scrape configuration,
see [Integrate Amazon MSK](managed-prometheus-collectors-msk-setup.md "managed-prometheus-collectors-msk-setup.md").

###### Topics

- [Requirements](#Solution-Prometheus-On-MSK-Requirements "#Solution-Prometheus-On-MSK-Requirements")
- [Enable the managed collector](#Solution-Prometheus-On-MSK-Enable-Collector "#Solution-Prometheus-On-MSK-Enable-Collector")
- [Amazon MSK detailed monitoring levels](#Solution-Prometheus-On-MSK-Detailed-Monitoring "#Solution-Prometheus-On-MSK-Detailed-Monitoring")
- [View the automatic dashboard](#Solution-Prometheus-On-MSK-Dashboards "#Solution-Prometheus-On-MSK-Dashboards")
- [Costs](#Solution-Prometheus-On-MSK-Costs "#Solution-Prometheus-On-MSK-Costs")

## Requirements

This solution is relevant for the following conditions:

- An Amazon MSK cluster in provisioned mode, with standard or express brokers. Managed
  collectors do not support Amazon MSK Serverless clusters.
- Open Monitoring enabled on the cluster, which exposes the JMX Exporter (port 11001)
  and Node Exporter (port 11002).
- Amazon VPC with DNS enabled, and at least two subnets in different Availability
  Zones for the collector.
- A security group that allows the collector to reach broker ports 11001 and

11002.

## Enable the managed collector

To collect Amazon MSK metrics with a managed collector, you enable Open Monitoring on your
cluster and then create a VPC-connected collector that scrapes the broker endpoints and
delivers metrics to your CloudWatch dataset. The collector connects to your VPC and scrapes all
brokers using DNS-based service discovery, so your monitoring stays resilient to broker
replacements and cluster scaling. For step-by-step instructions, see [Integrate Amazon MSK](managed-prometheus-collectors-msk-setup.md "managed-prometheus-collectors-msk-setup.md").

###### Note

The `--open-monitoring` parameter alone exposes the Prometheus
endpoints on ports 11001 and 11002. Enhanced monitoring tiers such as
`PER_TOPIC_PER_PARTITION` are separate from Open Monitoring and can incur
additional charges, so set them only if you need that level of Amazon MSK metrics.

## Amazon MSK detailed monitoring levels

Separately from the Prometheus metrics that the collector scrapes, Amazon MSK
publishes its own metrics to CloudWatch at several monitoring levels. Each level builds on the
previous one and provides more granular operational visibility. You choose a monitoring
level when you create or update the cluster. The following list summarizes the levels. For
the complete list of metrics at each level, see [Amazon MSK metrics for monitoring
with CloudWatch](../../../msk/latest/developerguide/metrics-details.md "../../../msk/latest/developerguide/metrics-details.md") in the _Amazon MSK Developer Guide_.

- **Basic monitoring** (`DEFAULT`) —
  The default level, available at no additional cost. Includes cluster-level and
  broker-level metrics such as the number of brokers, number of partitions,
  bytes and messages in and out, CPU utilization, and network I/O.
- **Enhanced broker-level monitoring**
  (`PER_BROKER`) — Includes basic monitoring plus more granular
  per-broker metrics, at an additional cost.
- **Enhanced topic-level monitoring**
  (`PER_TOPIC_PER_BROKER`) — Includes enhanced broker-level monitoring
  plus per-topic metrics for a more granular view of topic performance across brokers, at
  an additional cost.
- **Enhanced partition-level monitoring**
  (`PER_TOPIC_PER_PARTITION`) — The most detailed level. Includes
  enhanced topic-level monitoring plus fine-grained per-partition metrics such as offset
  lag, at an additional cost.

###### Note

Amazon MSK publishes detailed monitoring metrics to classic CloudWatch metrics, which you
can query with the `GetMetricData` API. To make detailed monitoring metrics
available alongside the Open Monitoring Prometheus metrics, you need to
enable OpenTelemetry enrichment. For more information, see [OpenTelemetry
metric enrichment](CloudWatch-OTelEnrichment.md "CloudWatch-OTelEnrichment.md").

## View the automatic dashboard

After the collector begins delivering your Amazon MSK metrics to CloudWatch, the CloudWatch console
provides an automatic dashboard named **MSK OTel**. To open it,
see [MSK OTel](https://console.aws.amazon.com/cloudwatch/home?#dashboards/templates/msk-otel "https://console.aws.amazon.com/cloudwatch/home?#dashboards/templates/msk-otel"), or sign in to the AWS Management Console, open the CloudWatch console, choose
**Dashboards** in the navigation pane, choose
**Automatic dashboards**, and then choose
**MSK OTel**. You can start monitoring your clusters without
building any widgets or dashboards yourself. If the automatic dashboard meets your needs, you
can use it as is. To build a tailored monitoring experience, you can add any of its widgets
to a custom dashboard. For more information about custom dashboards, see [Using
CloudWatch dashboards](CloudWatch_Dashboards.md "CloudWatch_Dashboards.md").

## Costs

We charge for Prometheus collectors by the hour, and CloudWatch OpenTelemetry
metric ingestion pricing applies. Higher Amazon MSK monitoring levels also incur additional
monthly costs. For more information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
