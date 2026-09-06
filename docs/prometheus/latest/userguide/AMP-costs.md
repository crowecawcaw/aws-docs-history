

# Understand and optimize costs in Amazon Managed Service for Prometheus
<a name="AMP-costs"></a>

The following frequently asked questions and their answers may be helpful in understanding and optimizing costs associated with Amazon Managed Service for Prometheus.

## What contributes to my costs?
<a name="AMP-costs-FAQ-contributors"></a>

For most customers, metric *ingestion* contributes the majority of costs. Customers with high query usage will also see some cost based on *query samples processed*, with *metrics storage* being a small driver of overall costs. For more information about the prices for each of these, see [Pricing](https://aws.amazon.com/prometheus/pricing#Pricing) in the *Amazon Managed Service for Prometheus product page*.

## What is the best way to lower my costs? How do I lower ingestion costs?
<a name="AMP-costs-FAQ-ingestion"></a>

Ingestion rates (not storage of the metrics) is the majority of costs for most customers. You can reduce ingestion rates by reducing the collection frequency (increasing the collection interval) or by reducing the number of active series ingested.

You can increase the collection (scraping) interval from your collection agent: Both the Prometheus server (running in Agent mode) and the AWS Distro for OpenTelemetry (ADOT) collector support the `scrape_interval` configuration. For example, increasing the collection interval from 30 seconds to 60 seconds will reduce your ingestion usage by half.

You can also filter the metrics sent to Amazon Managed Service for Prometheus by using the `<relabel_config>`. For more information about relabeling in the Prometheus agent configuration, see [https://prometheus.io/docs/prometheus/latest/configuration/configuration/\#relabel\_config](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config) in the Prometheus documentation.

## What is the best way to lower my query costs?
<a name="AMP-costs-FAQ-query"></a>

Query costs are based on the number of samples processed. You can reduce the frequency of queries to reduce your query costs.

To get more visibility into the queries that are contributing the most to your query costs, see [Managing the query cost in Amazon Managed Service for Prometheus](query-insights-control.md).

## If I decrease the retention period of my metrics, will that help reduce my total bill?
<a name="AMP-costs-FAQ-dataretention"></a>

You can reduce your retention period, however, this is unlikely to substantially reduce your costs.

For information about how to configure the retention period of a workspace, see [Configure your workspace](AMP-workspace-configuration.md).

## How can I keep my alert query costs low?
<a name="AMP-costs-FAQ-alertquery"></a>

Alerting creates queries against your data, which add to your query costs. Here are some strategies that you can use to optimize your alert queries, and keep your costs lower.
+ **Use Amazon Managed Service for Prometheus alerting** – Alerting systems external to Amazon Managed Service for Prometheus may require additional queries to add resiliency or high availability, as the external service queries the metrics from multiple availability zones or regions. This includes alerting in Grafana for high availability. This can multiply your cost by three times or more. The alerting in Amazon Managed Service for Prometheus is optimized and will give you high availability and resiliency with the fewest number of queries.

  We recommend using the native alerting in Amazon Managed Service for Prometheus rather than external alerting systems.
+ **Optimize your alert interval** – One quick way to optimize your alert queries is to increase the auto-refresh interval. If you have an alert that queries every minute, but is only needed every five minutes, increasing the auto-refresh interval could save you five times your query costs for that alert.
+ **Use an optimal lookback** – A larger lookback window in your query increases the costs of the query, as it pulls more data. Ensure that the lookback window in your PromQL query is reasonably sized for the data you need to alert. For example, in the following rule, the expression includes a ten minute lookback window:

  ```
      - alert: metric:alerting_rule
        expr: avg(rate(container_cpu_usage_seconds_total[10m])) > 0
        for: 2m
  ```

  Changing the `expr` to `avg(rate(container_cpu_usage_seconds_total[{{5m}}])) > 0` can help to reduce your query costs.

In general, look at your alerting rules and make sure that you are alerting on the best metrics for your service. It's easy to create overlapping alerts on the same metrics or multiple alerts that give you the same information, especially as you add alerts over time. If you find that you often see groups of alerts happening at the same time, it's possible that you can optimize your alerts and not include all of them.

These suggestions can help you to reduce costs. Ultimately, you must balance the costs with creating the right set of alerts for understanding the state of your system.

For more information about alerting in Amazon Managed Service for Prometheus, see [Managing and forwarding alerts in Amazon Managed Service for Prometheus with alert manager](AMP-alert-manager.md).

## Can I check my bill at any time?
<a name="AMP-costs-FAQ-bill"></a>

The AWS Cost and Usage Report tracks your AWS usage and provides estimated charges associated with your account within a billing period. For more information, see [What are AWS Cost and Usage Reports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) in the *AWS Cost and Usage Reports User Guide*

## What metrics can I use to monitor my costs?
<a name="AMP-costs-FAQ-monitor"></a>

Metric samples you ingest are the primary cost driver for Amazon Managed Service for Prometheus. The number of samples ingested directly determines your monthly charges, making it essential to monitor and understand your ingestion patterns.

[AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) is the source of truth for monitoring your Amazon Managed Service for Prometheus costs. You can monitor Cost Explorer for historical and day-by-day trends for cost on Amazon Managed Service for Prometheus across multiple dimensions including ingested samples. [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html) can also provide you the ability to monitor unexpected changes in your spending patterns.

Using `IngestionRate` metrics provides an auxiliary method to monitor trends in ingestion that are directly correlated to cost. The advantages of using `IngestionRate` as an additional metric include:
+ **Workspace-level tracking** – Monitor ingestion on a per-workspace basis rather than only at the account level.
+ **Granular visibility** – Track ingestion patterns on an hourly or even minute-by-minute basis for real-time insights.
+ **Proactive monitoring** – Set CloudWatch alarms to detect usage spikes before they appear in billing.

**Note**  
`IngestionRate` can be used to estimate costs and trends or attribute cost per workspace, but it is not 100% accurate. Because `IngestionRate` reports an average rate sampled at 1-minute intervals, multiplying this rate by time provides an approximation rather than an exact count of samples ingested. Additionally, Amazon CloudWatch's data retention policy affects the granularity available for historical queries, with data older than 63 days limited to 1-hour intervals.

For more information about monitoring Amazon Managed Service for Prometheus metrics in CloudWatch, see [Use CloudWatch metrics to monitor Amazon Managed Service for Prometheus resources](AMP-CW-usage-metrics.md).

**Monitoring native histogram costs** – Native histograms are metered based on populated buckets: each populated bucket (a bucket with non-zero observations) counts as 0.25 of a metric sample, and empty buckets are not metered. For example, a native histogram with 10 populated buckets is metered as 2.5 metric samples. To monitor your native histogram cost drivers, you can use the `NativeHistogramIngestedBucketsRate` metric to monitor the rate of populated buckets being ingested. You can also use `NativeHistogramIngestionRate` to track the overall native histogram sample ingestion rate and `NativeHistogramActiveSeries` to monitor the number of active native histogram series in your workspace.

## How do I view my costs in AWS Cost Explorer?
<a name="AMP-costs-FAQ-costexplorer"></a>

As your source of truth for Amazon Managed Service for Prometheus costs, AWS Cost Explorer provides your actual billed usage and charges for Amazon Managed Service for Prometheus samples ingested, including historical billing data by month and region. Use Cost Explorer for your final billed amounts and day-by-day cost trends.

To view your Amazon Managed Service for Prometheus costs:

**Access AWS Cost Explorer**

1. Sign in to the AWS Management Console.

1. Navigate to the Billing and Cost Management dashboard.

1. Select **Cost Explorer** from the left navigation menu.

1. Choose **Launch Cost Explorer** (if this is your first time using it).

**Configure the report**

1. Set your time range to the desired billing period (for example, March 2025 - February 2026).

1. Under **Filters**, select:
   + **Service**: Choose "Amazon Managed Service for Prometheus".
   + **Usage Type**: Filter for "MetricSampleCount" to isolate sample ingestion charges.

**Group and view data**

1. Under **Group by**, select **Region** to view cost and usage data per region.

1. Choose your preferred visualization (bar chart, line chart, or table).

1. Choose **Apply** to generate the report.

**Export data (optional)**

1. Choose **Download CSV** in the top right corner to export the data.

1. The CSV file will contain: billing period, region, usage type, billed amount, and usage quantity (number of samples billed).

**Note**  
Cost Explorer data typically has a 24-hour delay. For the most current billing period, data may not be available until the following day.

## How do I calculate the number of samples ingested in a month?
<a name="AMP-costs-FAQ-calculate"></a>

You can calculate the approximate number of samples ingested using Amazon CloudWatch's `IngestionRate` metrics with the AWS Command Line Interface. This is useful for reviewing monthly bills and understanding usage patterns across workspaces.

To retrieve ingestion data:

```
aws cloudwatch get-metric-data \
    --region {{your-region}} \
    --start-time {{start-timestamp}} \
    --end-time {{end-timestamp}} \
    --metric-data-queries '[
        {
            "Id": "e1",
            "Expression": "SUM(METRICS())",
            "Period": 3600
        },
        {
            "Id": "ws1",
            "MetricStat": {
                "Metric": {
                    "Namespace": "AWS/Usage",
                    "MetricName": "ResourceCount",
                    "Dimensions": [
                        {"Name": "Service",    "Value": "Prometheus"},
                        {"Name": "Resource",   "Value": "IngestionRate"},
                        {"Name": "Type",       "Value": "Resource"},
                        {"Name": "Class",      "Value": "None"},
                        {"Name": "ResourceId", "Value": "{{YOUR_AMP_WORKSPACE_ID}}"}
                    ]
                },
                "Period": 3600,
                "Stat": "Average"
            }
        }
    ]'
```

The command returns hourly average `IngestionRate` values, measured in samples per second. To calculate the approximate number of samples ingested in a month, multiply each hourly data point by 3600 (seconds per hour) to get the samples ingested in that hour, then sum all hourly totals across the month:

```
Monthly samples ≈ Σ (hourly IngestionRate average × 3600)
```

For example, if a single hour returns an average `IngestionRate` of 500 samples per second, that hour contributed approximately 500 × 3600 = 1,800,000 samples. Repeat this for every hour in the month and sum the results to get your approximate monthly ingestion count.

Key parameters:
+ `Period`: 3600 (1 hour in seconds)
+ `StartTime`: Beginning of your month (for example, `2026-02-01T00:00:00Z`)
+ `EndTime`: End of your month (for example, `2026-03-01T00:00:00Z`)
+ `Stat`: Average

To find your workspace IDs:

```
aws amp list-workspaces --region {{your-region}}
```

Use the workspace ID to filter the metrics to show data only for the specified workspace, rather than aggregating across all Prometheus resources in the region.

## What data granularity is available for historical cost analysis?
<a name="AMP-costs-FAQ-granularity"></a>

Amazon CloudWatch's data retention policy affects the granularity available for historical queries:
+ **Data less than 15 days old**: Query at 1-minute intervals (`Period`: 60)
+ **Data 15–63 days old**: Query at 5-minute intervals (`Period`: 300)
+ **Data older than 63 days**: Limited to 1-hour intervals (`Period`: 3600)

For historical analysis beyond 63 days, CloudWatch automatically downsamples data to a minimum 1-hour period. When reviewing billing for months older than 63 days, you must use hourly aggregated data. The monthly sample calculation uses these hourly-averaged data points, summing each value multiplied by 3600 across the entire month.

This reduced granularity further contributes to why `IngestionRate` provides estimates rather than exact counts for older data—always refer to Cost Explorer for your authoritative billed amounts.

For more details on CloudWatch metric retention, see [Metrics retention](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Metric) in the *Amazon CloudWatch User Guide*.

## What are best practices for monitoring Amazon Managed Service for Prometheus costs?
<a name="AMP-costs-FAQ-bestpractices"></a>

To effectively manage and optimize your Amazon Managed Service for Prometheus spending, consider implementing the following monitoring practices:
+ Monitor Cost Explorer regularly to track actual spending trends and identify cost anomalies across multiple dimensions including ingested samples.
+ Enable AWS Cost Anomaly Detection to receive alerts for unexpected cost increases in your Amazon Managed Service for Prometheus spending.
+ Set up CloudWatch alarms on `IngestionRate` for workspace-level monitoring and early detection of ingestion spikes.
+ Export Cost Explorer data regularly for long-term cost analysis and reporting.

## Why is my bill higher at the beginning of the month than at the end of the month?
<a name="AMP-costs-FAQ-tiers"></a>

Amazon Managed Service for Prometheus has a tiered pricing model for ingestion, which results in costs in your initial usage being higher. As your usage reaches higher ingest tiers, with lower costs, your costs are lower. For more information about pricing, including ingest tiers, see [Pricing](https://aws.amazon.com/prometheus/pricing#Pricing) in the *Amazon Managed Service for Prometheus product page*.

**Note**  
Tiers are for usage *within a region*, not across regions. Usage within a region must reach the next tier to use the lower rate.
In an organization in AWS Organizations, tier usage is tallied *per payer account*, not per account (the payer account is always the organization management account). When the total ingested metrics (within a region) for *all accounts in an organization* reaches the next tier, all accounts are charged the lower rate.

## I deleted all my Amazon Managed Service for Prometheus workspaces, but I still seem to be getting charged. What might be happening?
<a name="AMP-costs-FAQ-scrapers"></a>

One possibility in this case is that you still have AWS managed scrapers that are setup to send metrics to your deleted workspaces. Follow the instructions to [Find and delete scrapers](AMP-collector-how-to.md#AMP-collector-list-delete).