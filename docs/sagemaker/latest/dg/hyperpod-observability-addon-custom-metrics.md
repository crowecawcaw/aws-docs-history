# Creating custom

SageMaker HyperPod cluster metrics

The Amazon SageMaker HyperPod (SageMaker HyperPod) observability add-on provides hundreds of
health, performance, and efficiency metrics out-of-the-box. In addition to those
metrics, you might need to monitor custom metrics specific to your applications
or business needs that aren't captured by default metrics, such as
model-specific performance indicators, data processing statistics, or
application-specific measurements. To address this need, you can implement
custom metrics collection using OpenTelemetry by integrating a Python code
snippet into your application.

To create custom metrics, first run the following shell command to install the
core OpenTelemetry components needed to instrument Python applications for
observability. This installation makes it possible for Python applications that
run on SageMaker HyperPod clusters to emit custom telemetry data. That data gets
collected by the OpenTelemetry collector and forwarded to the observability
infrastructure.

```
pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp-proto-grpc
```

The following example script configures an OpenTelemetry metrics pipeline that
automatically tags metrics with pod and node information, ensuring proper
attribution within your cluster, and sends these metrics to the SageMaker HyperPod
built-in observability stack every second. The script establishes a connection
to the SageMaker HyperPod metrics collector, sets up appropriate resource attributes
for identification, and provides a meter interface through which you can create
various types of metrics (counters, gauges, or histograms) to track any aspect
of your application's performance. Custom metrics integrate with the
SageMaker HyperPod monitoring dashboards alongside system metrics. This integration
allows for comprehensive observability through a single interface where you can
create custom alerts, visualizations, and reports to monitor your workload's
complete performance profile.

```
import os
from opentelemetry import metrics
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource

# Get hostname/pod name
hostname = os.uname()[1]
node_name = os.getenv('NODE_NAME', 'unknown')

collector_endpoint = "hyperpod-otel-collector.hyperpod-observability:4317"

# Configure the OTLP exporter
exporter = OTLPMetricExporter(
    endpoint=collector_endpoint,
    insecure=True,
    timeout=5000  # 5 seconds timeout
)

reader = PeriodicExportingMetricReader(
    exporter,
    export_interval_millis=1000
)

resource = Resource.create({
    "service.name": "metric-test",
    "pod.name": hostname,
    "node.name": node_name
})

meter_provider = MeterProvider(
    metric_readers=[reader],
    resource=resource
)
metrics.set_meter_provider(meter_provider)

# Create a meter
meter = metrics.get_meter("test-meter")

# Create a counter
counter = meter.create_counter(
    name="test.counter",
    description="A test counter"
)

counter.add(1, {"pod": hostname, "node": node_name})
```
