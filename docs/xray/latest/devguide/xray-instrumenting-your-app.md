# Instrumenting your application

for AWS X-Ray

###### Important

End of support notice – On February 25th, 2027, AWS X-Ray will discontinue support for AWS X-Ray SDKs and daemon. After February 25th, 2027, you will no longer receive updates or releases. For more information on the timeline, see
[X-Ray SDK and daemon end of support timeline](xray-daemon-eos.md "xray-daemon-eos.md") and for information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

Instrumenting your application involves sending trace data for incoming and outbound requests and other events
within your application, along with metadata about each request. There are several different instrumentation options
you can choose from or combine, based on your particular requirements:

- _Auto instrumentation_ – instrument your application with zero code changes,
  typically via configuration changes, adding an auto-instrumentation agent, or other mechanisms.
- _Library instrumentation_ – make minimal application code changes to add pre-built
  instrumentation targeting specific libraries or frameworks, such as the AWS SDK, Apache HTTP clients, or SQL
  clients.
- _Manual instrumentation_ – add instrumentation code to your application at each
  location where you want to send trace information.

There are several SDKs, agents, and tools that can be used to instrument your application for X-Ray tracing.

###### Topics

- [Instrumenting your application with the AWS Distro for OpenTelemetry](#xray-instrumenting-opentel "#xray-instrumenting-opentel")
- [Instrumenting your application with AWS X-Ray SDKs](#xray-instrumenting-xray-sdk "#xray-instrumenting-xray-sdk")
- [Choosing between the AWS Distro for OpenTelemetry and X-Ray SDKs](#xray-instrumenting-choosing "#xray-instrumenting-choosing")

## Instrumenting your application with the AWS Distro for OpenTelemetry

The AWS Distro for OpenTelemetry (ADOT) is an AWS distribution based on the Cloud Native Computing Foundation (CNCF) OpenTelemetry
project. OpenTelemetry provides a single set of open source APIs, libraries, and agents to collect distributed
traces and metrics. This toolkit is a distribution of upstream OpenTelemetry components including SDKs,
auto-instrumentation agents, and collectors that are tested, optimized, secured, and supported by AWS.

With ADOT, engineers can instrument their applications once and send correlated metrics and traces to multiple
AWS monitoring solutions including Amazon CloudWatch, AWS X-Ray, and Amazon OpenSearch Service.

Using X-Ray with ADOT requires two components: an _OpenTelemetry SDK_ enabled for
use with X-Ray, and the _AWS Distro for OpenTelemetry Collector_ enabled for use with
X-Ray. For more information about using the AWS Distro for OpenTelemetry with AWS X-Ray and other AWS services,
see the [AWS Distro for OpenTelemetry Documentation](https://aws-otel.github.io/docs/introduction "https://aws-otel.github.io/docs/introduction").

For more information about language support and usage, see [AWS Observability on GitHub](https://github.com/aws-observability "https://github.com/aws-observability").

###### Note

You can now use the CloudWatch agent to collect metrics, logs and traces from Amazon EC2 instances and on-premise
servers. CloudWatch agent version 1.300025.0 and later can collect traces from
OpenTelemetry
or [X-Ray](#xray-instrumenting-xray-sdk "#xray-instrumenting-xray-sdk") client SDKs, and send them to X-Ray. Using the CloudWatch agent instead of
the AWS Distro for OpenTelemetry (ADOT) Collector or X-Ray daemon to collect traces can help you reduce the number of agents that you manage.
See the [CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md")
topic in the CloudWatch User Guide for more information.

ADOT includes the following:

- [AWS Distro for OpenTelemetry Go](https://aws-otel.github.io/docs/getting-started/go-sdk "https://aws-otel.github.io/docs/getting-started/go-sdk")
- [AWS Distro for OpenTelemetry Java](https://aws-otel.github.io/docs/getting-started/java-sdk "https://aws-otel.github.io/docs/getting-started/java-sdk")
- [AWS Distro for OpenTelemetry JavaScript](https://aws-otel.github.io/docs/getting-started/javascript-sdk "https://aws-otel.github.io/docs/getting-started/javascript-sdk")
- [AWS Distro for OpenTelemetry Python](https://aws-otel.github.io/docs/getting-started/python-sdk "https://aws-otel.github.io/docs/getting-started/python-sdk")
- [AWS Distro for OpenTelemetry .NET](https://aws-otel.github.io/docs/getting-started/dotnet-sdk "https://aws-otel.github.io/docs/getting-started/dotnet-sdk")

ADOT currently includes auto-instrumentation support for [Java](https://aws-otel.github.io/docs/getting-started/java-sdk/auto-instr "https://aws-otel.github.io/docs/getting-started/java-sdk/auto-instr") and [Python](https://aws-otel.github.io/docs/getting-started/python-sdk/auto-instr "https://aws-otel.github.io/docs/getting-started/python-sdk/auto-instr"). In addition, ADOT enables
auto-instrumentation of AWS Lambda functions and their downstream requests using Java, Node.js, and Python
runtimes, via [ADOT Managed Lambda Layers](https://aws-otel.github.io/docs/getting-started/lambda "https://aws-otel.github.io/docs/getting-started/lambda").

ADOT SDKs for Java and Go support X-Ray centralized sampling rules. If you need support for X-Ray sampling
rules in other languages, consider using an AWS X-Ray SDK.

###### Note

You can send now send W3C trace IDs to X-Ray. By default, traces that are created with OpenTelemetry have a
trace ID format that's based on the [W3C Trace Context
specification](https://www.w3.org/TR/trace-context/ "https://www.w3.org/TR/trace-context/"). This is different from the format for trace IDs that are created using an X-Ray SDK or
by AWS services that are integrated with X-Ray. To ensure that trace IDs in W3C format are accepted by
X-Ray, you must use [AWS X-Ray
Exporter](https://aws-otel.github.io/docs/getting-started/x-ray "https://aws-otel.github.io/docs/getting-started/x-ray") version 0.86.0 or later, which is included with [ADOT Collector](https://aws-otel.github.io/download "https://aws-otel.github.io/download") version 0.34.0 and later. Previous versions
of the exporter validate trace ID timestamps, which might cause W3C trace IDs to be rejected.

## Instrumenting your application with AWS X-Ray SDKs

AWS X-Ray includes a set of language-specific SDKs for instrumenting your application to send traces to
X-Ray. Each X-Ray SDK provides the following:

- _Interceptors_ to add to your code to trace incoming HTTP
  requests
- _Client handlers_ to instrument AWS SDK clients that your
  application uses to call other AWS services
- An _HTTP client_ to instrument calls to other internal and external HTTP web
  services

X-Ray SDKs also support instrumenting calls to SQL databases, automatic AWS SDK client
instrumentation, and other features. Instead of sending trace data directly to X-Ray, the SDK
sends JSON segment documents to a daemon process listening for UDP traffic. The [X-Ray daemon](xray-daemon.md "xray-daemon.md") buffers segments in a queue and uploads them to X-Ray in
batches.

The following language-specific SDKs are provided:

- [AWS X-Ray SDK for Go](xray-sdk-go.md "xray-sdk-go.md")
- [AWS X-Ray SDK for Java](xray-sdk-java.md "xray-sdk-java.md")
- [AWS X-Ray SDK for Node.js](xray-sdk-nodejs.md "xray-sdk-nodejs.md")
- [AWS X-Ray SDK for Python](xray-sdk-python.md "xray-sdk-python.md")
- [AWS X-Ray SDK for .NET](xray-sdk-dotnet.md "xray-sdk-dotnet.md")
- [AWS X-Ray SDK for Ruby](xray-sdk-ruby.md "xray-sdk-ruby.md")

X-Ray currently includes auto-instrumentation support for [Java](aws-x-ray-auto-instrumentation-agent-for-java.md "aws-x-ray-auto-instrumentation-agent-for-java.md").

## Choosing between the AWS Distro for OpenTelemetry and X-Ray SDKs

The SDKs included with X-Ray are part of a tightly integrated instrumentation solution offered by AWS. The
AWS Distro for OpenTelemetry is part of a broader industry solution in which X-Ray is only one of many tracing solutions. You can
implement end-to-end tracing in X-Ray using either approach, but it’s important to understand the differences in
order to determine the most useful approach for you.

We recommend instrumenting your application with the AWS Distro for OpenTelemetry if you need the following:

- The ability to send traces to multiple different tracing back ends without having to re-instrument your
  code
- Support for a large number of library instrumentations for each language, maintained by the OpenTelemetry
  community
- Fully managed Lambda layers that package everything you need to collect telemetry data, without requiring
  code changes when using Java, Python, or Node.js

###### Note

AWS Distro for OpenTelemetry offers a simpler getting started experience for instrumenting your Lambda functions. However, due to the
flexibility OpenTelemetry offers, your Lambda function will require additional memory and invocations may
experience cold start latency increases, which can lead to additional charges. If you're optimizing for
low-latency and do not require OpenTelemetry's advanced capabilities such as dynamically configurable back
end destinations, you may want to use the AWS X-Ray SDK to instrument your application.

We recommend choosing an X-Ray SDK for instrumenting your application if you need the following:

- A tightly integrated single-vendor solution
- Integration with X-Ray centralized sampling rules, including the ability to configure sampling rules from
  the X-Ray console and automatically use them across multiple hosts, when using Node.js, Python, Ruby, or
  .NET
