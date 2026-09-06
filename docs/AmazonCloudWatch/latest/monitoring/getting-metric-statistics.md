

# Get statistics for a metric (GetMetricStatistics)
<a name="getting-metric-statistics"></a>

`GetMetricStatistics` is the legacy single-metric API. For new code, use [Retrieve metric data (GetMetricData)](metrics-classic-getdata.md) instead — it supports batch queries and math expressions.

## Usage
<a name="getting-metric-statistics-usage"></a>

```
aws cloudwatch get-metric-statistics \
  --namespace "AWS/EC2" \
  --metric-name "CPUUtilization" \
  --dimensions Name=InstanceId,Value={{i-1234567890abcdef0}} \
  --start-time $(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --period 300 \
  --statistics Average Maximum
```

## When to use this API
<a name="getting-metric-statistics-when-to-use"></a>
+ Legacy applications that already depend on it
+ Simple single-metric retrievals where batch isn't needed

For everything else, use [Retrieve metric data (GetMetricData)](metrics-classic-getdata.md).