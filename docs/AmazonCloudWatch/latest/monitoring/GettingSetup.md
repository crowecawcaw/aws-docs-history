

# Quickstart: Send metrics, logs, and traces to CloudWatch with OpenTelemetry
<a name="GettingSetup"></a>

In about 20 minutes, you send three signals from one application to CloudWatch: a metric, a log record, and a trace. You see the metric in Query Studio, the log in CloudWatch Logs, and the trace in Transaction Search.

This is the recommended path for new telemetry. You use the OpenTelemetry SDK, then the OpenTelemetry Collector, then the CloudWatch OpenTelemetry Protocol (OTLP) endpoints, and finally Query Studio, CloudWatch Logs, and Transaction Search. This path works the same way on Amazon EKS, Amazon ECS, Amazon EC2, and on-premises servers. The instrumentation that you write here doesn't change when you deploy.

When you finish, you have the following:
+ A counter metric and a histogram metric, a log record, and a trace with a span, all emitted by a sample application
+ A Collector that signs and forwards all three signals to CloudWatch
+ A PromQL query and an alarm for the metric, the log record in CloudWatch Logs, and the trace in Transaction Search

The resources that you create in this quickstart might incur charges to your AWS account. Ingesting metrics, logs, and traces can each incur charges. For more information, see [OTel metrics pricing and storage](metrics-otel-pricing.md).

## Choosing the right path
<a name="GettingSetup-RightPath"></a>

Use this quickstart for any new custom metric. Use a different approach only if one of the following applies to you.


| If you | Use instead | 
| --- | --- | 
| Run in an AWS Region where OTLP metrics ingestion isn't available. For more information about supported Regions, see [Supported AWS Regions](CloudWatch-PromQL.md#CloudWatch-PromQL-Regions). | `PutMetricData` or the embedded metric format. For more information, see [Publish custom metrics (PutMetricData / EMF)](publishingMetrics.md). | 
| Already have alarms and dashboards on an existing custom namespace that you must keep | Keep publishing with `PutMetricData`, and migrate later. For more information, see [Migrate from Classic to OTel metrics](metrics-otel-migrate.md). | 
| Need a metric from existing log events without changing code | A metric filter on the log group. For more information, see [Creating metrics from log events using filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) in the *Amazon CloudWatch Logs User Guide*. | 
| Want request rate, errors, and latency without writing code | Application Signals. Add custom metrics only for business events. For more information, see [Application Signals](CloudWatch-Application-Monitoring-Sections.md). | 

## Prerequisites
<a name="GettingSetup-Prerequisites"></a>

Before you begin this quickstart, make sure that you have the following:
+ <a name="ConsoleSignIn"></a>An AWS account and access to [Query Studio in the CloudWatch console](https://console.aws.amazon.com/cloudwatch/home#query:) in a supported AWS Region. This quickstart uses `aa-example-1`. Replace it with your Region everywhere that it appears.
+ <a name="SetupCLI"></a>AWS credentials that the Collector can find. On AWS compute, use an AWS Identity and Access Management (IAM) role. For example, use an instance profile on Amazon EC2, use IAM roles for service accounts or Amazon EKS Pod Identity on Amazon EKS, or use a task role on Amazon ECS. When you test locally, use environment variables. To get credentials for the AWS CLI, see [Getting set up with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html) in the *AWS Command Line Interface User Guide*.
+ CloudWatch Transaction Search enabled in your Region. You can send traces to the OTLP traces endpoint only after you enable Transaction Search. For more information, see [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html).
+ Docker, to run the Collector.
+ Python 3.9 or later, for the sample application. The Java, Go, .NET, and Node.js SDKs work the same way.

**Important**  
Traces that you send to the X-Ray OTLP endpoint require Transaction Search to be enabled. This is a one-time, account-wide setting. It switches all X-Ray span ingestion into CloudWatch Logs collection mode, billed under CloudWatch pricing, with 1 percent of spans indexed for free. Metrics and logs don't require this setting.  
To enable Transaction Search, run the following command.  

```
aws xray update-trace-segment-destination --destination CloudWatchLogs --region aa-example-1
```
To verify, run the following command. The destination is ready when `Status` is `ACTIVE` and `Destination` is `CloudWatchLogs`.  

```
aws xray get-trace-segment-destination --region aa-example-1
```

**IAM policy for the Collector's role** — The Collector needs permissions to send metrics, logs, and traces. Attach the AWS managed policy `CloudWatchAgentServerPolicy` to the Collector's role. This is the simplest option, and it grants everything that the Collector needs for all three signals.

**Note**  
Sending metrics over OTLP uses the `cloudwatch:PutMetricData` permission, even though you never call that API. CloudWatch metrics don't support resource-level permissions, so policies that allow this action set `Resource` to `"*"`. The `CloudWatchAgentServerPolicy` managed policy already includes this permission, along with the permissions for logs and traces.

People who query metrics or create alarms also need the `cloudwatch:GetMetricData` and `cloudwatch:ListMetrics` permissions. For more information, see [IAM permissions for PromQL](CloudWatch-PromQL.md#CloudWatch-PromQL-IAM).

Workloads outside AWS can use a bearer token instead of SigV4 for metrics and logs. The traces endpoint doesn't support bearer tokens; traces require SigV4. For more information, see [Setting up bearer token authentication for Metrics](CloudWatch-OTLP-MetricsBearerTokenAuth.md).

## Step 1: Instrumenting your application
<a name="GettingSetup-Instrument"></a>

Your application sends telemetry to a local Collector, not directly to CloudWatch. The SDK's OTLP exporter doesn't sign requests with SigV4, so CloudWatch rejects direct calls to the endpoints. The Collector handles signing, batching, and retries.

The following command installs the SDK and the OTLP HTTP exporter. The HTTP exporter package provides the metric, span, and log exporters that this quickstart uses.

```
pip install opentelemetry-sdk opentelemetry-exporter-otlp-proto-http
```

Create `app.py`. It records one counter (orders placed) and one histogram (checkout latency), wraps each checkout in a trace span, and writes a log record for each order. All three signals go to the local Collector.

```
import logging, random, time
from opentelemetry import metrics, trace
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter

# Static metadata goes on the resource, not on every data point
resource = Resource.create({
    "service.name": "checkout",
    "service.version": "1.4.0",
    "deployment.environment": "dev",
})

# Metrics: local Collector; exports every 60 seconds
metric_exporter = OTLPMetricExporter(endpoint="http://localhost:4318/v1/metrics")
reader = PeriodicExportingMetricReader(metric_exporter, export_interval_millis=60000)
metrics.set_meter_provider(MeterProvider(resource=resource, metric_readers=[reader]))

# Traces: local Collector
trace.set_tracer_provider(TracerProvider(resource=resource))
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces"))
)

# Logs: local Collector, bridged from the Python logging module
logger_provider = LoggerProvider(resource=resource)
logger_provider.add_log_record_processor(
    BatchLogRecordProcessor(OTLPLogExporter(endpoint="http://localhost:4318/v1/logs"))
)
set_logger_provider(logger_provider)
logging.getLogger().addHandler(LoggingHandler(logger_provider=logger_provider))
logging.getLogger().setLevel(logging.INFO)

meter = metrics.get_meter("checkout")
orders = meter.create_counter("orders_placed", unit="1", description="Orders placed")
latency = meter.create_histogram("checkout_duration", unit="s", description="Checkout latency")
tracer = trace.get_tracer("checkout")
log = logging.getLogger("checkout")

while True:
    try:
        payment = random.choice(["card", "wallet"])
        with tracer.start_as_current_span("checkout") as span:
            span.set_attribute("payment_method", payment)
            orders.add(1, {"payment_method": payment})
            duration = random.uniform(0.05, 1.2)
            latency.record(duration, {"payment_method": payment})
            log.info("Order placed using %s in %.3fs", payment, duration)
            time.sleep(1)
    except Exception as error:
        print(f"Error recording telemetry: {error}")
```

**Important**  
Use attributes whose values come from a small, fixed set, such as `payment_method`. Never use order IDs, user IDs, or URLs that contain IDs as attribute values.

## Step 2: Running the Collector
<a name="GettingSetup-Collector"></a>

In this quickstart, you run the Collector locally and give it credentials through environment variables. In production, the Collector runs on your compute platform and uses an IAM role instead, as shown in [Next steps](#GettingSetup-NextSteps).

**Important**  
Sending metrics, logs, and traces to CloudWatch incurs charges. For more information, see [OTel metrics pricing and storage](metrics-otel-pricing.md).

The Collector receives all three signals from your application and exports each one to its CloudWatch OTLP endpoint. Use a distribution that includes the `sigv4auth` extension, such as the OpenTelemetry Collector Contrib distribution or the AWS Distro for OpenTelemetry (ADOT) Collector.

**Note**  
The CloudWatch agent is an alternative. It can receive OpenTelemetry Protocol (OTLP) data and send it to CloudWatch, so you can use it instead of running a separate OpenTelemetry Collector. For more information, see [Collect metrics and traces with OpenTelemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-OpenTelemetry-metrics.html).

The logs exporter sends to the log group and log stream that you set in the `x-aws-log-group` and `x-aws-log-stream` headers. This example uses a `/otel/quickstart` log group and a `default` stream. Create them in CloudWatch Logs first, or change the values to a log group and stream that already exist.

Create `collector.yaml`. In the following example, replace `aa-example-1` with your Region.

```
extensions:
  sigv4auth/metrics:
    service: monitoring        # always "monitoring" for metrics
    region: aa-example-1
  sigv4auth/logs:
    service: logs              # always "logs" for logs
    region: aa-example-1
  sigv4auth/traces:
    service: xray              # always "xray" for traces
    region: aa-example-1

receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  memory_limiter:
    check_interval: 1s
    limit_percentage: 80         # Valid range: 1-100
    spike_limit_percentage: 20   # Valid range: 1-100
  batch:
    send_batch_size: 200         # Number of records to buffer before sending
    send_batch_max_size: 1000    # Maximum batch size; CloudWatch accepts at most 1,000 metric data points for each request
    timeout: 10s                 # Maximum time to wait before sending a batch

exporters:
  otlphttp/metrics:            # the endpoints support HTTP only, not gRPC
    metrics_endpoint: https://monitoring.aa-example-1.amazonaws.com/v1/metrics
    compression: gzip
    auth:
      authenticator: sigv4auth/metrics
  otlphttp/logs:               # the endpoints support HTTP only, not gRPC
    logs_endpoint: https://logs.aa-example-1.amazonaws.com/v1/logs
    compression: gzip
    headers:
      x-aws-log-group: /otel/quickstart   # create this log group, or use an existing one
      x-aws-log-stream: default           # create this stream, or use an existing one
    auth:
      authenticator: sigv4auth/logs
  otlphttp/traces:             # the endpoints support HTTP only, not gRPC
    traces_endpoint: https://xray.aa-example-1.amazonaws.com/v1/traces
    compression: gzip
    auth:
      authenticator: sigv4auth/traces

service:
  extensions: [sigv4auth/metrics, sigv4auth/logs, sigv4auth/traces]
  pipelines:
    metrics:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters: [otlphttp/metrics]
    logs:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters: [otlphttp/logs]
    traces:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters: [otlphttp/traces]
```

The logs endpoint writes to an existing log group and log stream. Before you start the Collector, create the log group and stream named in the `x-aws-log-group` and `x-aws-log-stream` headers of your `collector.yaml` logs exporter. Otherwise, CloudWatch rejects your logs with `The specified log group does not exist`.

```
aws logs create-log-group --log-group-name /otel/quickstart --region aa-example-1
aws logs create-log-stream --log-group-name /otel/quickstart --log-stream-name default --region aa-example-1
```

Run the Collector locally with your credentials, and then start the application:

```
docker run --rm -p 4317:4317 -p 4318:4318 \
  -v "$PWD/collector.yaml:/etc/otelcol-contrib/config.yaml" \
  -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_SESSION_TOKEN \
  otel/opentelemetry-collector-contrib:latest

python app.py
```

In production, pin a Collector version instead of using `latest`. On AWS compute, omit the `-e` flags. The Collector uses the role's credentials.

## Step 3: Checking that your telemetry arrived
<a name="GettingSetup-Verify"></a>

Data usually appears 1–2 minutes after the first export. Verify each signal in turn.

**Metrics** — In the CloudWatch console, open Query Studio and run each of the following queries. For more information, see [Running a PromQL query in Query Studio](CloudWatch-PromQL-QueryStudio.md#CloudWatch-PromQL-QueryStudio-RunQuery).


| To | PromQL | 
| --- | --- | 
| Confirm that the series exists | `orders_placed` | 
| Show orders per second, by payment method | `sum by (payment_method) (rate(orders_placed[5m]))` | 
| Show 95th percentile checkout latency | `histogram_quantile(0.95, sum(rate(checkout_duration[5m])))` | 

The raw `orders_placed` query returns one series for each payment method. Because a counter only increases, each series shows a cumulative total, as in the following example.

```
orders_placed{payment_method="card"}    512
orders_placed{payment_method="wallet"}  488
```

The `sum by (payment_method) (rate(orders_placed[5m]))` query converts those totals to a per-second rate. With the sample application, each series is near 0.5 per second, as in the following example.

```
{payment_method="card"}    0.51
{payment_method="wallet"}  0.49
```

Counters need `rate()` or `increase()`, because a raw counter only increases. You can query gauges directly. CloudWatch stores histograms as native histograms, so you query the metric name directly, without `_bucket` series or an `le` label. For more information, see [Querying histogram metrics](CloudWatch-PromQL-Querying.md#CloudWatch-PromQL-Querying-Histograms).

**Logs** — In the CloudWatch console, open CloudWatch Logs and open the `/otel/quickstart` log group (or the log group that you set in the `x-aws-log-group` header). Each order writes one log record. To search the records, use CloudWatch Logs Insights. For more information, see [Analyze log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) in the *Amazon CloudWatch Logs User Guide*.

In Logs Insights, select the `/otel/quickstart` log group and run the following query to find your records:

```
fields @timestamp, severityText, body, traceId, spanId
| filter @message like /checkout/
| sort @timestamp desc
| limit 50
```

CloudWatch stores the OpenTelemetry log record as JSON, with resource attributes nested under `resource.attributes` (for example, `resource.attributes.service.name`), and the span's `payment_method` attribute is not a field on the log record — it appears in the span and in the log body. If you need to filter by a nested field, run a bare `fields @timestamp, @message | limit 50` query first to see the exact field paths.

**Traces** — In the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home), open Transaction Search and open the Traces view. Each checkout produces one trace with a `checkout` span. If you don't see traces, confirm that Transaction Search is enabled in your Region.

Transaction Search stores spans in the `aws/spans` log group. You can search them in the CloudWatch Transaction Search console, filtered by the `checkout` service, or with a Logs Insights query on `aws/spans`. In Logs Insights, select the `aws/spans` log group and run the following query. This query filters on the top-level span name to avoid nested-field-path issues.

```
fields @timestamp, name, durationNano, attributes.payment_method, status.code, traceId
| filter name = "checkout"
| sort @timestamp desc
| limit 20
```

Each span carries the trace and span IDs that also appear on your log records, so you can pivot between a log line and its trace. CloudWatch enriches spans with Application Signals attributes such as `aws.local.service`.

If you don't see data after 5 minutes, see [Troubleshooting telemetry export](#GettingSetup-Troubleshooting).

## Step 4: Creating an alarm and a dashboard widget
<a name="GettingSetup-Alarm"></a>

Turn the latency query into an alarm and a dashboard widget, both from Query Studio.

**To create an alarm and a dashboard widget**

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home), and then open Query Studio.

1. In Query Studio, run the 95th percentile latency query from [Step 3: Checking that your telemetry arrived](#GettingSetup-Verify).

1. From the actions menu, choose **Create alarm**. For more information, see [Creating alarms from Query Studio](CloudWatch-PromQL-QueryStudio.md#CloudWatch-PromQL-QueryStudio-Alarms).
**Note**  
If you receive an `AccessDenied` error, verify that the `CloudWatchAgentServerPolicy` managed policy is attached, or that your IAM policy includes the `cloudwatch:GetMetricData` and `cloudwatch:ListMetrics` permissions. For the required permissions, see [Prerequisites](#GettingSetup-Prerequisites).

1. Set the condition to greater than **0.8** seconds for 3 out of 3 periods.

1. Choose an Amazon SNS topic for notifications.

1. Return to Query Studio, choose **Add to dashboard**, and choose or create a dashboard for the checkout service. For more information, see [Adding visualizations to dashboards](CloudWatch-PromQL-QueryStudio.md#CloudWatch-PromQL-QueryStudio-Dashboards).

1. (Optional) Add `sum(rate(orders_placed[5m]))` to the same dashboard.

1. (Optional) Turn on anomaly detection for the orders metric, so that a drop in orders alerts you without a fixed threshold. For more information, see [Anomaly detection using PromQL](anomaly_detection_promql.md).

## Troubleshooting telemetry export
<a name="GettingSetup-Troubleshooting"></a>

Check the Collector logs first. Export errors include the HTTP status code from CloudWatch.


| Symptom | Likely cause | Fix | 
| --- | --- | --- | 
| 403 on metrics in the Collector logs | The role lacks `cloudwatch:PutMetricData`, or the `sigv4auth` service isn't `monitoring`. | Attach `CloudWatchAgentServerPolicy`, or fix the `service` value. | 
| 403 on logs in the Collector logs | The role lacks the logs permissions, or the `sigv4auth` service isn't `logs`. | Attach `CloudWatchAgentServerPolicy`, and set the logs `service` to `logs`. | 
| 4xx on logs, missing header | The logs exporter doesn't set the `x-aws-log-group` or `x-aws-log-stream` header. | Set both headers on the `otlphttp/logs` exporter to the target log group and stream. | 
| A log event is truncated or rejected | A single request to the logs endpoint is larger than 1 MB. | Reduce the batch size or the size of each log record so that each request stays under 1 MB. | 
| Traces rejected | Transaction Search isn't enabled in the Region. | Enable CloudWatch Transaction Search, and then resend the traces. | 
| 403 on traces in the Collector logs | A bearer token was used for traces. The traces endpoint doesn't support bearer tokens. | Use SigV4 for traces. Configure the `sigv4auth` extension with the `xray` service. | 
| Connection errors to CloudWatch | The exporter is gRPC (`otlp`) instead of `otlphttp`, or the Region in the URL is wrong. | Use `otlphttp`, and use the same Region in the URL and in `sigv4auth`. | 
| The application logs `connection refused` | The Collector isn't running, or port 4318 isn't published. | Start the Collector, and check `-p 4318:4318`. | 
| 400, too many data points | A batch has more than 1,000 data points. | Set `send_batch_max_size: 1000`. | 
| 400 on some series | A data point has more than 150 labels, or a label value is longer than 1,024 characters. | Drop or shorten attributes in a `transform` processor. | 
| 429 | More than 500 requests per second for the account, or too many new series. | Send larger batches, and reduce the number of attribute values. | 
| Accepted, but not visible | The data point timestamp is more than 14 days in the past or more than 2 hours in the future. | Check the host clock. | 

For all limits, see [Endpoint limits and restrictions](CloudWatch-OTLPEndpoint.md#CloudWatch-LimitsandRestrictions).

## Clean up resources
<a name="GettingSetup-Cleanup"></a>

To avoid ongoing charges, delete the resources that you created in this quickstart when you no longer need them:
+ Delete the alarm that you created.
+ Remove the dashboard widget that you added.
+ Delete the `/otel/quickstart` log group and its `default` log stream (or the log group and stream that you used) in CloudWatch Logs.
+ Stop the Collector container and the sample application.
+ Detach `CloudWatchAgentServerPolicy` from the Collector's role if you attached it only for this quickstart.

## Keeping costs predictable
<a name="GettingSetup-Cost"></a>

CloudWatch bills OTLP metrics per GB ingested, with 15 months of storage included. Logs and traces are also billed by the volume that you ingest, and Transaction Search has its own charges. Volume grows with the number of data points per series, the number of series, the number of log records, and the number of traces. For more information, see [OTel metrics pricing and storage](metrics-otel-pricing.md).

To keep costs predictable, keep the following practices in mind:
+ **Export every 60 seconds.** Halving the interval roughly doubles the volume.
+ **Count your series before you ship.** The number of series for a metric is the product of the number of distinct values of each attribute. For example, 2 payment methods, 3 Regions, and 5 status codes produce 30 series. Adding a user ID makes the number unbounded.
+ **Put static metadata on the resource.** As shown in [Step 1: Instrumenting your application](#GettingSetup-Instrument), service name, version, and environment belong on the resource, not on each data point.
+ **Use histograms where you need distributions.** A histogram data point carries more data than a counter or gauge data point. Use histograms for latency and sizes, not for everything.
+ **Drop what you don't query.** With a `filter` processor in the Collector, you can remove unused metrics, log records, spans, or attributes before you're billed for them.

## Next steps
<a name="GettingSetup-NextSteps"></a>

Your instrumentation stays the same in production. Only where the Collector runs changes.

The following table shows where the Collector runs and which credentials to use in each environment.


| Environment | Where the Collector runs | Credentials | 
| --- | --- | --- | 
| Amazon EKS | A DaemonSet or Deployment. Applications send to its Service. | IAM roles for service accounts or Amazon EKS Pod Identity | 
| Amazon ECS | A sidecar container in the task | Task role | 
| Amazon EC2 | A service on each instance | Instance profile | 
| On-premises | A service on each host, or a central gateway | IAM Roles Anywhere, or a bearer token for metrics and logs | 

Before you go to production, also plan for the following:
+ Configure the sending queue and retry settings on each exporter.
+ Set up Collector health checks.
+ Set up cross-account observability if telemetry from many accounts goes to one monitoring account. For more information, see [CloudWatch cross-account observability](CloudWatch-Unified-Cross-Account.md).

For more ways to send telemetry, see [Collect and send telemetry](collect-send-telemetry.md).