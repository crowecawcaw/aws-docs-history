# Publish custom metrics with OpenTelemetry

You can publish custom metrics to CloudWatch using the OpenTelemetry Protocol (OTLP). You can use
OTel SDKs (Java, Python, Go, .NET, Node.js), the OTel Collector, or any OTLP-compatible
client.

## CloudWatch OTLP endpoint

Send metrics to the CloudWatch OTLP endpoint in your Region:

```
https://monitoring.`region`.amazonaws.com/v1/metrics
```

Authentication uses standard AWS SigV4 signing. The service name is
`monitoring`. For more information about the endpoint, authentication options, and
limits, see [OTLP Endpoints](CloudWatch-OTLPEndpoint.md "CloudWatch-OTLPEndpoint.md").

## Quick start: publish your first metric

### Option 1: OTel Collector (recommended for production)

Configure an OTel Collector with the OTLP HTTP exporter and SigV4 authentication:

```
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:
    send_batch_size: 200
    timeout: 10s

exporters:
  otlphttp:
    tls:
      insecure: false
    metrics_endpoint: "https://monitoring.`us-east-1`.amazonaws.com/v1/metrics"
    auth:
      authenticator: sigv4auth

extensions:
  sigv4auth:
    service: "monitoring"
    region: "`us-east-1`"

service:
  extensions: [sigv4auth]
  pipelines:
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp]
```

For detailed setup instructions, see
[Getting started](CloudWatch-OTLPGettingStarted.md "CloudWatch-OTLPGettingStarted.md").

### Option 2: OTel SDK (Python example)

```
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter

# Point at the CloudWatch OTLP endpoint
exporter = OTLPMetricExporter(
    endpoint="https://monitoring.`us-east-1`.amazonaws.com:443/v1/metrics"
)
reader = PeriodicExportingMetricReader(exporter, export_interval_millis=60000)
provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(provider)

# Create and record a metric
meter = metrics.get_meter("my-app")
counter = meter.create_counter("http_requests_total", description="Total HTTP requests")
counter.add(1, {"method": "GET", "path": "/api/users", "status": "200"})
```

### Option 3: OTel SDK (Java example)

```
import io.opentelemetry.api.metrics.Meter;
import io.opentelemetry.api.metrics.LongCounter;

Meter meter = GlobalOpenTelemetry.getMeter("my-app");
LongCounter counter = meter.counterBuilder("http_requests_total")
    .setDescription("Total HTTP requests")
    .build();

counter.add(1, Attributes.of(
    AttributeKey.stringKey("method"), "GET",
    AttributeKey.stringKey("path"), "/api/users",
    AttributeKey.stringKey("status"), "200"
));
```

## IAM permissions required

The identity sending metrics needs the `cloudwatch:PutMetricData` permission.
For SigV4 authentication, attach the following policy:

```
{
  "Effect": "Allow",
  "Action": [
    "cloudwatch:PutMetricData"
  ],
  "Resource": "*"
}
```

For bearer token authentication, see
[Setting up bearer token authentication for Metrics](CloudWatch-OTLP-MetricsBearerTokenAuth.md "CloudWatch-OTLP-MetricsBearerTokenAuth.md").

## Verify metrics are arriving

Open the CloudWatch console, navigate to **Query Studio**, and
run:

```
http_requests_total
```

Metrics typically appear within 1–2 minutes of the first data point being
sent.

## Supported metric types

The following table describes the OTel metric types that CloudWatch supports and how to query
them with PromQL.

| OTel metric type | PromQL behavior                            |
| ---------------- | ------------------------------------------ |
| Counter          | Use `rate()` or `increase()` to query      |
| Gauge            | Query directly (current value)             |
| Histogram        | Use `histogram_quantile()` for percentiles |

## Best practices

Follow these recommendations when sending metrics through OTLP:

- **Use meaningful metric names** — Follow OTel
  naming conventions (for example, `http.server.request.duration` or
  `http_request_duration_seconds`).
- **Keep label cardinality reasonable** — Avoid
  request IDs or UUIDs as label values.
- **Set an appropriate export interval** —
  60 seconds is standard. Shorter intervals increase cost.
- **Use resource attributes** — Use resource
  attributes for static metadata (service name, version, environment) rather than
  per-data-point labels.
