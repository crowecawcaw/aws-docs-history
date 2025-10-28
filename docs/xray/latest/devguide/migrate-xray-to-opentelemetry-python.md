# Migrate to OpenTelemetry Python

This guide helps you migrate Python applications from X-Ray SDK to OpenTelemetry instrumentation. It covers both automatic and manual instrumentation approaches, with code examples for common scenarios.

###### Sections

- [Zero code automatic instrumentation solutions](#zero-code-python "#zero-code-python")
- [Manually instrument your applications](#manual-instrumentation-python "#manual-instrumentation-python")
- [Tracing setup initialization](#manual-instrumentation-python-tracing "#manual-instrumentation-python-tracing")
- [Tracing incoming requests](#tracing-incoming-requests-python "#tracing-incoming-requests-python")
- [AWS SDK instrumentation](#aws-sdk-instrumentation-python "#aws-sdk-instrumentation-python")
- [Instrumenting outgoing HTTP calls through requests](#http-instrumentation-python "#http-instrumentation-python")
- [Instrumentation support for other libraries](#xray-migration-libraries-python "#xray-migration-libraries-python")
- [Manually creating trace data](#manual-trace-creation-python "#manual-trace-creation-python")
- [Lambda instrumentation](#lambda-instrumentation-python "#lambda-instrumentation-python")

## Zero code automatic instrumentation solutions

With X-Ray SDK, you had to modify your application code to trace requests. OpenTelemetry offers zero-code auto-instrumentation solutions to trace requests. With OpenTelemetry, you have the option of using zero-code auto-instrumentation solutions to trace requests.

**Zero code with OpenTelemetry-based automatic instrumentations**

1. Using the AWS Distro for OpenTelemetry (ADOT) auto-Instrumentation for Python – For automatic instrumentation for Python applications, see [Tracing and Metrics with the AWS Distro for OpenTelemetry Python Auto-Instrumentation](https://aws-otel.github.io/docs/getting-started/python-sdk/auto-instr "https://aws-otel.github.io/docs/getting-started/python-sdk/auto-instr").

(Optional) You can also enable CloudWatch Application Signals when automatically instrumenting your applications on AWS with the ADOT Python auto-instrumentation to monitor current application
health and track long-term application performance against your business objectives. Application Signals provides you with a unified, application-centric view of your applications, services, and dependencies, and helps you monitor and triage application health. 2. Using the OpenTelemetry Python zero-code automatic instrumentation – For automatic instrumentation with the OpenTelemetry Python, see [Python zero-code instrumentation](https://opentelemetry.io/docs/zero-code/python/ "https://opentelemetry.io/docs/zero-code/python/").

## Manually instrument your applications

You can manually instrument your applications using the `pip` command.

With X-Ray SDK

```

pip install aws-xray-sdk

```

With OpenTelemetry SDK

```

pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp opentelemetry-propagator-aws-xray

```

## Tracing setup initialization

With X-Ray SDK
In X-Ray, the global `xray_recorder` is initialized and used it to generate segments and sub-segments.

With OpenTelemetry SDK###### Note

X-Ray Remote Sampling is currently not available to be configured for OpenTelemetry Python. However, support for X-Ray Remote Sampling is currently available
through the ADOT Auto-Instrumentation for Python.

In OpenTelemetry, you need to initialize a global `TracerProvider`. Using this `TracerProvider`, you can acquire a [Tracer](https://opentelemetry.io/docs/concepts/signals/traces/#tracer "https://opentelemetry.io/docs/concepts/signals/traces/#tracer") that you can use to generate spans anywhere in your application. It is recommend that you configure the following components:

- `OTLPSpanExporter` – Required for exporting traces to the CloudWatch Agent/OpenTelemetry Collector
- An AWS X-Ray Propagator
  – Required for propagating the Trace Context to AWS Services that are integrated with X-Ray

```

from opentelemetry import (
    trace,
    propagate
)
from opentelemetry.sdk.trace import TracerProvider

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.propagators.aws import AwsXRayPropagator

# Sends generated traces in the OTLP format to an OTel Collector running on port 4318
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces")
# Processes traces in batches as opposed to immediately one after the other
span_processor = BatchSpanProcessor(otlp_exporter)
# More configurations can be done here. We will visit them later.

# Sets the global default tracer provider
provider = TracerProvider(active_span_processor=span_processor)
trace.set_tracer_provider(provider)

# Configures the global propagator to use the X-Ray Propagator
propagate.set_global_textmap(AwsXRayPropagator())

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer("my.tracer.name")
# Use this tracer to create Spans

```

**With ADOT auto-Instrumentation for Python**

You can use the ADOT auto-instrumentation for Python to automatically configure OpenTelemetry for your Python applications. By using ADOT auto-instrumentation, you do not need to make manual code changes to trace incoming requests,
or to trace libraries such as the AWS SDK or HTTP clients. For more information, see [Tracing and Metrics with the AWS Distro for OpenTelemetry Python Auto-Instrumentation](https://aws-otel.github.io/docs/getting-started/python-sdk/auto-instr "https://aws-otel.github.io/docs/getting-started/python-sdk/auto-instr").

ADOT auto-instrumentation for Python supports:

- X-Ray remote sampling through the environment variable `export OTEL_TRACES_SAMPLER=xray`
- X-Ray trace context propagation (enabled by default)
- Resource detection (resource detection for Amazon EC2, Amazon ECS, and Amazon EKS environments are enabled by default)
- Automatic library instrumentations for all supported OpenTelemetry instrumentations are enabled by default. You can disable selectively through the `OTEL_PYTHON_DISABLED_INSTRUMENTATIONS` environment variable. (all are enabled by default)
- Manual creation of Spans
  **From X-Ray service plug-ins to OpenTelemetry AWS resource providers**

The X-Ray SDK provides plug-ins that you could add to the `xray_recorder` to capture the platform specific information from the hosted service like Amazon EC2, Amazon ECS, and Elastic Beanstalk.
It's similar to the Resource Providers in OpenTelemetry that captures the information as Resource attributes. There are multiple Resource Providers available for different AWS platforms.

- Start by installing the AWS extension package, `pip install opentelemetry-sdk-extension-aws`
- Configure the desired resource detector. The following example shows how to configure the Amazon EC2 resource provider in OpenTelemetry SDK

```

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.extension.aws.resource.ec2 import (
    AwsEc2ResourceDetector,
)
from opentelemetry.sdk.resources import get_aggregated_resources

provider = TracerProvider(
    active_span_processor=span_processor,
    resource=get_aggregated_resources([
        AwsEc2ResourceDetector(),
    ]))

trace.set_tracer_provider(provider)

```

## Tracing incoming requests

With X-Ray SDK
The X-Ray Python SDK supports application frameworks like Django, Flask, and Bottle in tracing the incoming requests for Python applications running on them. This is done by adding `XRayMiddleware` to the application for each framework.

With OpenTelemetry SDKOpenTelemetry provides instrumentations for [Django](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/django/django.html "https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/django/django.html") and [Flask](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/flask/flask.html "https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/flask/flask.html") through the specific instrumentation libraries.
There is no instrumentation for Bottle available in OpenTelemetry, applications can still be traced by using the
[OpenTelemetry WSGI Instrumentation](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/wsgi/wsgi.html "https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/wsgi/wsgi.html") .

For the following code example, you need the following dependency:

```

pip install opentelemetry-instrumentation-flask

```

You must initialize the OpenTelemetry SDK and register the global TracerProvider before adding instrumentations for your application framework. Without it, the trace operations will be `no-ops`.
Once you have configured the global `TracerProvider`, you can use the instrumentor for your application framework. The following example demonstrates a Flask application.

```

from flask import Flask
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.extension.aws.resource import AwsEc2ResourceDetector
from opentelemetry.sdk.resources import get_aggregated_resources
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

provider = TracerProvider(resource=get_aggregated_resources(
    [
        AwsEc2ResourceDetector(),
    ]))

processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer("my.tracer.name")

app = Flask(__name__)

# Instrument the Flask app
FlaskInstrumentor().instrument_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

```

## AWS SDK instrumentation

With X-Ray SDK
The X-Ray Python SDK traces the AWS SDK client request by patching the `botocore` library. For more information, see [Tracing AWS SDK calls with the X-Ray SDK for Python](xray-sdk-python-awssdkclients.md "xray-sdk-python-awssdkclients.md") . In your application, the `patch_all()` method is used to instrument all the libraries or patch selectively using the `botocore` or `boto3`libraries using `patch((['botocore']))`.
Any of the chosen method instruments all the Boto3 clients in your application and generates a sub-segment for any call made using these clients.

With OpenTelemetry SDKFor the following code example, you will need the following dependency:

```

pip install opentelemetry-instrumentation-botocore

```

Use the [OpenTelemetry Botocore Instrumentation](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/botocore/botocore.html "https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/botocore/botocore.html") programmatically to instrument all the Boto3 clients in your application. The following example demonstrates the `botocore` instrumentation.

```

import boto3
import opentelemetry.trace as trace
from botocore.exceptions import ClientError
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import get_aggregated_resources
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.instrumentation.botocore import BotocoreInstrumentor

provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer("my.tracer.name")

# Instrument BotoCore
BotocoreInstrumentor().instrument()

# Initialize S3 client
s3 = boto3.client("s3", region_name="us-east-1")

# Your bucket name
bucket_name = "my-example-bucket"

# Get bucket location (as an example of describing it)
try:
    response = s3.get_bucket_location(Bucket=bucket_name)
    region = response.get("LocationConstraint") or "us-east-1"
    print(f"Bucket '{bucket_name}' is in region: {region}")

    # Optionally, get bucket's creation date via list_buckets
    buckets = s3.list_buckets()
    for bucket in buckets["Buckets"]:
        if bucket["Name"] == bucket_name:
            print(f"Bucket created on: {bucket['CreationDate']}")
            break
except ClientError as e:
    print(f"Failed to describe bucket: {e}")

```

## Instrumenting outgoing HTTP calls through requests

With X-Ray SDK
The X-Ray Python SDK traces outgoing HTTP calls through requests by patching the requests library. For more information, see [Tracing calls to downstream HTTP web services using the X-Ray SDK for Python](xray-sdk-python-httpclients.md "xray-sdk-python-httpclients.md"). In your application, you can use the `patch_all()` method to instrument all the libraries or by selectively patching the requests libraries by using `patch((['requests']))`.
Any of the option instruments the `requests` library, generating a sub-segment for any call made through `requests`.

With OpenTelemetry SDKFor the following code example, you will need the following dependency:

```

pip install opentelemetry-instrumentation-requests

```

Use the OpenTelemetry Requests Instrumentation programmatically to instrument the requests library to generate traces for HTTP requests made by it in your application. For more information,
see [OpenTelemetry requests Instrumentation](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/requests/requests.html "https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/requests/requests.html") . The following example demonstrates the `requests` library instrumentation.

```

from opentelemetry.instrumentation.requests import RequestsInstrumentor

# Instrument Requests
RequestsInstrumentor().instrument()

...

    example_session = requests.Session()
    example_session.get(url="https://example.com")

```

Alternatively, you can also instrument the underlying `urllib3` library to trace HTTP requests:

```

# pip install opentelemetry-instrumentation-urllib3
from opentelemetry.instrumentation.urllib3 import URLLib3Instrumentor

# Instrument urllib3
URLLib3Instrumentor().instrument()

...

    example_session = requests.Session()
    example_session.get(url="https://example.com")

```

## Instrumentation support for other libraries

You can find the full list of supported Library instrumentations for OpenTelemetry Python under [Supported libraries, frameworks, application servers, and JVMs](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md "https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md") .

Alternatively, you can search the OpenTelemetry Registry to find out if OpenTelemetry supports instrumentation. See the [Registry](https://opentelemetry.io/ecosystem/registry/ "https://opentelemetry.io/ecosystem/registry/") to start searching.

## Manually creating trace data

You can create segments and sub-segments using the `xray_recorder` in your Python application. For more information, see [Instrumenting Python code manually](xray-sdk-python-middleware.md#xray-sdk-python-middleware-manual "xray-sdk-python-middleware.md#xray-sdk-python-middleware-manual") . You can also manually add annotations and metadata to the trace data.

**Creating spans With OpenTelemetry SDK**

Use the `start_as_current_span` API to start a span and set it for creating spans. For examples on creating spans, see [Creating spans](https://opentelemetry.io/docs/languages/python/instrumentation/#creating-spans "https://opentelemetry.io/docs/languages/python/instrumentation/#creating-spans").
Once a span is started and is in the current scope, you can add more information to it by adding attributes, events, exceptions, links, and so on. Like how we have segments and sub-segments in X-Ray,
there are different kinds of spans in OpenTelemetry. Only the `SERVER` kind spans are converted to X-Ray segments while others are converted to X-Ray sub-segments.

```

from opentelemetry import trace
from opentelemetry.trace import SpanKind

import time

tracer = trace.get_tracer("my.tracer.name")

# Create a new span to track some work
with tracer.start_as_current_span("parent", kind=SpanKind.SERVER) as parent_span:
    time.sleep(1)

    # Create a nested span to track nested work
    with tracer.start_as_current_span("child", kind=SpanKind.CLIENT) as child_span:
        time.sleep(2)
        # the nested span is closed when it's out of scope

    # Now the parent span is the current span again
    time.sleep(1)

    # This span is also closed when it goes out of scope

```

**Adding annotations and metadata to traces with OpenTelemetry SDK**

The X-Ray Python SDK provides separate APIs, `put_annotation` and `put_metadata` for adding annotations and metadata to a trace. In OpenTelemetry SDK, the annotations and metadata are simply attributes on a span,
added through the `set_attribute` API.

Span attributes that you want them to be annotations on a trace are added under the reserved key `aws.xray.annotations` whose value is a list of key-value pairs of annotations. All the other span attributes become metadata
on the converted segment or sub-segment.

Additionally, if you are using the ADOT collector you can configure which span attributes should be converted to X-Ray annotations by specifying the `indexed_attributes` in the collector configuration.

The below example demonstrates how to add annotations and metadata to a trace using OpenTelemetry SDK.

```

with tracer.start_as_current_span("parent", kind=SpanKind.SERVER) as parent_span:
    parent_span.set_attribute("TransactionId", "qwerty12345")
    parent_span.set_attribute("AccountId", "1234567890")

    # This will convert the TransactionId and AccountId to be searchable X-Ray annotations
    parent_span.set_attribute("aws.xray.annotations", ["TransactionId", "AccountId"])

    with tracer.start_as_current_span("child", kind=SpanKind.CLIENT) as child_span:

        # The MicroTransactionId will be converted to X-Ray metadata for the child subsegment
        child_span.set_attribute("MicroTransactionId", "micro12345")

```

## Lambda instrumentation

To monitor your lambda functions on X-Ray, you enable X-Ray and added appropriate permissions to the function invocation role. Additionally, if you are tracing downstream requests from your function, you would be instrumenting the
code with X-Ray Python SDK.

With OpenTelemetry for X-Ray, it is recommended to use the CloudWatch Application Signals lambda layer with [Application Signals](../../../lambda/latest/dg/monitoring-application-signals.md "../../../lambda/latest/dg/monitoring-application-signals.md") turned off.
This will auto-instrument your function and will generate spans for the function invocation and any downstream request from your function. Besides tracing, if you are interested in using Application Signals to monitor the health of your function,
see [Enable your applications on Lambda](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-LambdaMain.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-LambdaMain.md") .

- Find the required Lambda layer ARN for your function from [AWS Lambda Layer for OpenTelemetry ARNs](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-LambdaMain.md#Enable-Lambda-Layers "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-LambdaMain.md#Enable-Lambda-Layers") and add it.
- Set the following environment variables for your function.
  - `AWS_LAMBDA_EXEC_WRAPPER=/opt/otel-instrument` – This loads the auto-instrumentation for the function
  - `OTEL_AWS_APPLICATION_SIGNALS_ENABLED=false` – This will disable Application Signals monitoring

**Manually creating spans with Lambda instrumentation**

Additionally, you can generate custom spans within your function to track work. You can do by using only the `opentelemetry-api` package in conjunction with the Application Signals lambda layer auto-instrumentation.

1. Include the `opentelemetry-api` as a dependency in your function
2. The following code snippet is a sample to generate custom spans

```

from opentelemetry import trace

# Get the tracer (auto‑configured by the Application Signals layer)
tracer = trace.get_tracer(__name__)

def handler(event, context):
    # This span is a child of the layer's root span
    with tracer.start_as_current_span("my-custom-span") as span:
        span.set_attribute("key1", "value1")
        span.add_event("custom-event", {"detail": "something happened"})

        # Any logic you want to trace
        result = some_internal_logic()

    return {
        "statusCode": 200,
        "body": result
    }

```
