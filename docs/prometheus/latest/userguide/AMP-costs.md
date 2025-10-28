# Understand and optimize costs in Amazon Managed Service for Prometheus

The following frequently asked questions and their answers may be helpful in understanding
and optimizing costs associated with Amazon Managed Service for Prometheus.

## What contributes to my costs?

For most customers, metric _ingestion_ contributes the majority of
costs. Customers with high query usage will also see some cost based on _query
samples processed_, with _metrics storage_ being a
small driver of overall costs. For more information about the prices for each of these,
see [Pricing](https://aws.amazon.com/prometheus/pricing#Pricing "https://aws.amazon.com/prometheus/pricing#Pricing") in the
_Amazon Managed Service for Prometheus product page_.

## What is the best way to lower my costs? How do

I lower ingestion costs?

Ingestion rates (not storage of the metrics) is the majority of costs for most
customers. You can reduce ingestion rates by reducing the collection frequency
(increasing the collection interval) or by reducing the number of active series
ingested.

You can increase the collection (scraping) interval from your collection agent: Both
the Prometheus server (running in Agent mode) and the AWS Distro for OpenTelemetry
(ADOT) collector support the `scrape_interval` configuration. For example,
increasing the collection interval from 30 seconds to 60 seconds will reduce your
ingestion usage by half.

You can also filter the metrics sent to Amazon Managed Service for Prometheus by using the
`<relabel_config>`. For more information about relabeling in the
Prometheus agent configuration, see [https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config "https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config")
in the Prometheus documentation.

## What is the best way to lower my query

costs?

Query costs are based on the number of samples processed. You can reduce the frequency
of queries to reduce your query costs.

To get more visibility into the queries that are contributing the most to your query
costs, you can reach out to file a ticket with your support contact. The Amazon Managed Service for Prometheus team
can help you understand the queries that are contributing the most to your costs.

## If I decrease the retention period of my

metrics, will that help reduce my total bill?

You can reduce your retention period, however, this is unlikely to substantially
reduce your costs.

For information about how to configure the retention period of a workspace, see [Configure your workspace](AMP-workspace-configuration.md "AMP-workspace-configuration.md").

## How can I keep my alert query costs

low?

Alerting creates queries against your data, which add to your query costs. Here are
some strategies that you can use to optimize your alert queries, and keep your costs
lower.

- **Use Amazon Managed Service for Prometheus alerting** – Alerting
  systems external to Amazon Managed Service for Prometheus may require additional queries to add resiliency
  or high availability, as the external service queries the metrics from multiple
  availability zones or regions. This includes alerting in Grafana for high
  availability. This can multiply your cost by three times or more. The alerting
  in Amazon Managed Service for Prometheus is optimized and will give you high availability and resiliency
  with the fewest number of queries.

We recommend using the native alerting in Amazon Managed Service for Prometheus rather than external
alerting systems.

- **Optimize your alert interval** – One
  quick way to optimize your alert queries is to increase the auto-refresh
  interval. If you have an alert that queries every minute, but is only needed
  every five minutes, increasing the auto-refresh interval could save you five
  times your query costs for that alert.
- **Use an optimal lookback** – A larger
  lookback window in your query increases the costs of the query, as it pulls more
  data. Ensure that the lookback window in your PromQL query is reasonably sized
  for the data you need to alert. For example, in the following rule, the
  expression includes a ten minute lookback window:

```
    - alert: metric:alerting_rule
      expr: avg(rate(container_cpu_usage_seconds_total[10m])) > 0
      for: 2m
```

Changing the `expr` to
`avg(rate(container_cpu_usage_seconds_total[`5m`]))

> 0` can help to reduce your query costs.

In general, look at your alerting rules and make sure that you are alerting on the
best metrics for your service. It's easy to create overlapping alerts on the same
metrics or multiple alerts that give you the same information, especially as you add
alerts over time. If you find that you often see groups of alerts happening at the same
time, it's possible that you can optimize your alerts and not include all of
them.

These suggestions can help you to reduce costs. Ultimately, you must balance the costs
with creating the right set of alerts for understanding the state of your system.

For more information about alerting in Amazon Managed Service for Prometheus, see [Managing and forwarding alerts in Amazon Managed Service for Prometheus with alert
manager](AMP-alert-manager.md "AMP-alert-manager.md").

## What metrics can I use to monitor my

costs?

Monitor `IngestionRate` in Amazon CloudWatch to track your ingestion costs.

###### Note

`IngestionRate` provides an estimated value and might not exactly match
your final billing charges.

For more information about monitoring Amazon Managed Service for Prometheus metrics in CloudWatch, see [Use CloudWatch metrics to monitor Amazon Managed Service for Prometheus
resources](AMP-CW-usage-metrics.md "AMP-CW-usage-metrics.md").

## Can I check my bill at any time?

The AWS Cost and Usage Report tracks your AWS usage and provides estimated charges associated with
your account within a billing period. For more information, see [What are AWS Cost
and Usage Reports?](../../../cur/latest/userguide/what-is-cur.md "../../../cur/latest/userguide/what-is-cur.md") in the _AWS Cost and Usage Reports User
Guide_

## Why is my bill higher at the beginning of the

month than at the end of the month?

Amazon Managed Service for Prometheus has a tiered pricing model for ingestion, which results in costs in your
initial usage being higher. As your usage reaches higher ingest tiers, with lower costs,
your costs are lower. For more information about pricing, including ingest tiers, see
[Pricing](https://aws.amazon.com/prometheus/pricing#Pricing "https://aws.amazon.com/prometheus/pricing#Pricing") in the
_Amazon Managed Service for Prometheus product page_.

###### Note

- Tiers are for usage _within a region_, not across
  regions. Usage within a region must reach the next tier to use the lower
  rate.
- In an organization in AWS Organizations, tier usage is tallied _per payer
  account_, not per account (the payer account is always the
  organization management account). When the total ingested metrics (within a
  region) for _all accounts in an organization_ reaches the
  next tier, all accounts are charged the lower rate.

## I deleted all my Amazon Managed Service for Prometheus workspaces, but I

still seem to be getting charged. What might be happening?

One possibility in this case is that you still have AWS managed scrapers that are
setup to send metrics to your deleted workspaces. Follow the instructions to [Find and delete scrapers](AMP-collector-how-to.md#AMP-collector-list-delete "AMP-collector-how-to.md#AMP-collector-list-delete").
