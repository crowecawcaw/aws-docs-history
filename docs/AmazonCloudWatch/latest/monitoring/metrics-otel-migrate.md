

# Migrate from Classic to OTel metrics
<a name="metrics-otel-migrate"></a>

Customers currently publishing custom metrics through PutMetricData or EMF can migrate incrementally to the OTel path. There is no flag day — migration happens workload by workload at your own pace.

## Migration approach
<a name="metrics-otel-migrate-approach"></a>

The migration follows four phases:

1. **Dual-write** — Publish metrics through both Classic and OTel paths simultaneously.

1. **Validate** — Confirm OTel metrics appear in Query Studio through PromQL.

1. **Recreate consumers** — Update alarms and dashboards to use PromQL and OTel metric names.

1. **Cut over** — Stop Classic publishing after you validate OTel consumers.

## Step 1: Instrument with OTel SDK (dual-write)
<a name="metrics-otel-migrate-step1"></a>

Add the OTel SDK alongside your existing PutMetricData calls. Both paths can publish simultaneously — you don't lose data.

```
# Existing Classic publishing (keep running during migration)
cloudwatch.put_metric_data(
    Namespace='MyApp',
    MetricData=[{'MetricName': 'RequestLatency', 'Value': 42.5, 'Unit': 'Milliseconds'}]
)

# New OTel publishing (add this)
from opentelemetry import metrics
meter = metrics.get_meter("my-app")
histogram = meter.create_histogram("http_request_duration_seconds")
histogram.record(0.0425, {"method": "GET", "path": "/api/users"})
```

## Step 2: Verify in Query Studio
<a name="metrics-otel-migrate-step2"></a>

To verify that your OTel metrics are arriving, open the CloudWatch console and navigate to Query Studio. Search for your metric:

```
http_request_duration_seconds
```

Confirm that data appears with the labels you expect.

## Step 3: Recreate alarms on OTel metrics
<a name="metrics-otel-migrate-step3"></a>

Create new alarms that query OTel metrics using PromQL expressions. The following example shows a Classic alarm and its OTel equivalent.

**Classic alarm:**

```
aws cloudwatch put-metric-alarm \
  --alarm-name "high-latency" \
  --namespace "MyApp" \
  --metric-name "RequestLatency" \
  --statistic Average --threshold 100 ...
```

**OTel equivalent (PromQL alarm):**

```
aws cloudwatch put-metric-alarm \
  --alarm-name "high-latency-otel" \
  --metrics '[{"Id":"q1","Expression":"avg(http_request_duration_seconds{path=\"/api/users\"}) * 1000","Period":300,"ReturnData":true}]' \
  --threshold 100 ...
```

Run both alarms in parallel until you are confident the OTel version fires correctly.

## Step 4: Stop Classic publishing
<a name="metrics-otel-migrate-step4"></a>

After you validate your OTel alarms and dashboards, remove the PutMetricData calls from your application code. Classic metrics stop incurring charges immediately.

## Metric name mapping
<a name="metrics-otel-migrate-name-mapping"></a>

The following table shows common Classic metric names and their suggested OTel equivalents.


| Classic name | Suggested OTel name | Notes | 
| --- | --- | --- | 
| RequestLatency (ms) | http\_request\_duration\_seconds | Convert to seconds (OTel convention) | 
| RequestCount | http\_requests\_total | Use `_total` suffix for counters | 
| ErrorCount | http\_server\_errors\_total | Use `_total` suffix | 
| QueueDepth | queue\_depth | Gauge — no suffix needed | 

## What about AWS vended metrics?
<a name="metrics-otel-migrate-vended-metrics"></a>

You don't need to migrate AWS vended metrics (Amazon EC2 CPU, Amazon RDS connections, and so on) manually. Enable OTel Vended Metric Enrichment to make them queryable through PromQL automatically. For more information, see [AWS vended metrics in OpenTelemetry format](CloudWatch-OTelEnrichment.md).