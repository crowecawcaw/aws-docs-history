# Query your Prometheus metrics

Now that metrics are being ingested to the workspace, you can query them.

To create dashboards with visual representations of your metrics, you can use a service
such as Amazon Managed Grafana. Amazon Managed Grafana (or a standalone instance of Grafana) can build a graphical
interface that shows your metrics in a wide variety of display presentation styles. For more
information about Amazon Managed Grafana see the [Amazon Managed Grafana User Guide](../../../grafana/latest/userguide.md "../../../grafana/latest/userguide.md").

You can also create one-off queries, explore your data, or write your own applications
that use your metrics by using direct queries. Direct queries use the Amazon Managed Service for Prometheus API and the
standard Prometheus query language, PromQL, to get data from your Prometheus workspace. For
more information about PromQL and its syntax, see [Querying
Prometheus](https://prometheus.io/docs/prometheus/latest/querying/basics/ "https://prometheus.io/docs/prometheus/latest/querying/basics/") in the Prometheus documentation.

###### Topics

- [PromQL cheat sheet](#promql-cheat-sheet "#promql-cheat-sheet")
- [Basic selectors](#promql-basic-selectors "#promql-basic-selectors")
- [Range vector selectors](#promql-range-selectors "#promql-range-selectors")
- [Aggregation operators](#promql-aggregation-operators "#promql-aggregation-operators")
- [Common functions](#promql-functions "#promql-functions")
- [Binary operators](#promql-operators "#promql-operators")
- [Practical query examples](#promql-practical-examples "#promql-practical-examples")
- [Secure your metric queries](AMP-secure-querying.md "AMP-secure-querying.md")
- [Set up Amazon Managed Grafana for use with Amazon Managed Service for Prometheus](AMP-amg.md "AMP-amg.md")
- [Set up Grafana open source or
  Grafana Enterprise for use with Amazon Managed Service for Prometheus](AMP-onboard-query-standalone-grafana.md "AMP-onboard-query-standalone-grafana.md")
- [Query using Grafana running in an Amazon EKS
  cluster](AMP-onboard-query-grafana-7.md "AMP-onboard-query-grafana-7.md")
- [Query using Prometheus-compatible APIs](AMP-onboard-query-APIs.md "AMP-onboard-query-APIs.md")
- [Get statistics about your query usage for each query](AMP-stats.md "AMP-stats.md")

## PromQL cheat sheet

Use this PromQL (Prometheus Query Language) cheat sheet as a quick reference when
querying metrics in your Amazon Managed Service for Prometheus workspace. With PromQL, you can select and aggregate
time series data in real time through its functional query language.

For more details about PromQL, see [PromQL Cheat Sheet](https://promlabs.com/promql-cheat-sheet/ "https://promlabs.com/promql-cheat-sheet/") on the
_PromLabs_ website.

## Basic selectors

Select time series by metric name and label matchers:

```

# Select all time series with the metric name http_requests_total
http_requests_total

# Select time series with specific label values
http_requests_total{job="prometheus", method="GET"}

# Use label matchers
http_requests_total{status_code!="200"}          # Not equal
http_requests_total{status_code=~"2.."}          # Regex match
http_requests_total{status_code!~"4.."}          # Negative regex match

```

## Range vector selectors

Select a range of samples over time:

```

# Select 5 minutes of data
http_requests_total[5m]

# Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks), y (years)
cpu_usage[1h]
memory_usage[30s]

```

## Aggregation operators

Aggregate data across multiple time series:

```

# Sum all values
sum(http_requests_total)

# Sum by specific labels
sum by (job) (http_requests_total)
sum without (instance) (http_requests_total)

# Other aggregation operators
avg(cpu_usage)                    # Average
min(response_time)               # Minimum
max(response_time)               # Maximum
count(up)                        # Count of series
stddev(cpu_usage)               # Standard deviation

```

## Common functions

Apply functions to transform your data:

```

# Rate of increase per second (for counters)
rate(http_requests_total[5m])

# Increase over time range
increase(http_requests_total[1h])

# Derivative (for gauges)
deriv(cpu_temperature[5m])

# Mathematical functions
abs(cpu_usage - 50)              # Absolute value
round(cpu_usage, 0.1)           # Round to nearest 0.1
sqrt(memory_usage)              # Square root

# Time functions
time()                          # Current Unix timestamp
hour()                          # Hour of day (0-23)
day_of_week()                   # Day of week (0-6, Sunday=0)

```

## Binary operators

Perform arithmetic and logical operations:

```

# Arithmetic operators
cpu_usage + 10
memory_total - memory_available
disk_usage / disk_total * 100

# Comparison operators (return 0 or 1)
cpu_usage > 80
memory_usage < 1000
response_time >= 0.5

# Logical operators
(cpu_usage > 80) and (memory_usage > 1000)
(status_code == 200) or (status_code == 201)

```

## Practical query examples

Common monitoring queries you can use in your Amazon Managed Service for Prometheus workspace:

```

# CPU usage percentage
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Memory usage percentage
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100

# Request rate per second
sum(rate(http_requests_total[5m])) by (job)

# Error rate percentage
sum(rate(http_requests_total{status_code=~"5.."}[5m])) /
sum(rate(http_requests_total[5m])) * 100

# 95th percentile response time
histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))

# Top 5 instances by CPU usage
topk(5, avg by (instance) (cpu_usage))

```
