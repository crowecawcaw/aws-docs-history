

# Retrieve metric data (GetMetricData)
<a name="metrics-classic-getdata"></a>

`GetMetricData` is the primary API for retrieving Classic metric data points programmatically. It supports batch queries, math expressions, and queries in a single call.

## Basic usage
<a name="metrics-classic-getdata-basic"></a>

Retrieve a single metric:

```
aws cloudwatch get-metric-data \
  --metric-data-queries '[
    {
      "Id": "cpu",
      "MetricStat": {
        "Metric": {
          "Namespace": "AWS/EC2",
          "MetricName": "CPUUtilization",
          "Dimensions": [{"Name": "InstanceId", "Value": "{{i-1234567890abcdef0}}"}]
        },
        "Period": 300,
        "Stat": "Average"
      }
    }
  ]' \
  --start-time $(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --output json
```

## Batch queries
<a name="metrics-classic-getdata-batch"></a>

Retrieve multiple metrics in a single call (up to 500 queries):

```
aws cloudwatch get-metric-data \
  --metric-data-queries '[
    {"Id": "cpu", "MetricStat": {"Metric": {"Namespace": "AWS/EC2", "MetricName": "CPUUtilization", "Dimensions": [{"Name": "InstanceId", "Value": "{{i-abc}}"}]}, "Period": 300, "Stat": "Average"}},
    {"Id": "mem", "MetricStat": {"Metric": {"Namespace": "CWAgent", "MetricName": "mem_used_percent", "Dimensions": [{"Name": "InstanceId", "Value": "{{i-abc}}"}]}, "Period": 300, "Stat": "Average"}}
  ]' \
  --start-time 2024-01-01T00:00:00 \
  --end-time 2024-01-01T01:00:00
```

## Math expressions
<a name="metrics-classic-getdata-math"></a>

Combine metrics using arithmetic:

```
[
  {"Id": "rx", "MetricStat": {"Metric": {"Namespace": "AWS/EC2", "MetricName": "NetworkIn", "Dimensions": [{"Name": "InstanceId", "Value": "{{i-abc}}"}]}, "Period": 300, "Stat": "Sum"}},
  {"Id": "tx", "MetricStat": {"Metric": {"Namespace": "AWS/EC2", "MetricName": "NetworkOut", "Dimensions": [{"Name": "InstanceId", "Value": "{{i-abc}}"}]}, "Period": 300, "Stat": "Sum"}},
  {"Id": "total", "Expression": "rx + tx", "Label": "TotalNetwork"}
]
```

## GetMetricData vs GetMetricStatistics
<a name="metrics-classic-getdata-comparison"></a>


|  | **GetMetricData** | **GetMetricStatistics** | 
| --- | --- | --- | 
| Batch support | Up to 500 queries per call | Single metric per call | 
| Math expressions | Yes | No | 
|  queries | Yes | No | 
| Pagination | Yes (NextToken) | No | 
| Recommended | Yes — primary API | Legacy — use GetMetricData instead | 

## Pricing
<a name="metrics-classic-getdata-pricing"></a>

$0.01 per 1,000 metrics requested through `GetMetricData`.

**Note**  
For OTel metrics, use the Prometheus-compatible query API or CloudWatch Query Studio with PromQL. `GetMetricData` does not query OTel metrics.