# Get statistics for a metric (GetMetricStatistics)

`GetMetricStatistics` is the legacy single-metric API. For new code, use
[Retrieve metric data (GetMetricData)](metrics-classic-getdata.md "metrics-classic-getdata.md") instead
— it supports batch queries and math expressions.

## Usage

```
aws cloudwatch get-metric-statistics \
  --namespace "AWS/EC2" \
  --metric-name "CPUUtilization" \
  --dimensions Name=InstanceId,Value=`i-1234567890abcdef0` \
  --start-time $(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --period 300 \
  --statistics Average Maximum
```

## When to use this API

- Legacy applications that already depend on it
- Simple single-metric retrievals where batch isn't needed

For everything else, use [Retrieve metric data (GetMetricData)](metrics-classic-getdata.md "metrics-classic-getdata.md").
