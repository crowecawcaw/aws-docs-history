# Working with Python

###### Note

End-of-support notice – On February 25th, 2027, AWS X-Ray will discontinue support for AWS X-Ray SDKs and daemon. After February 25th, 2027, you will no longer receive updates or releases. For more information on the support timeline, see
[X-Ray SDK and daemon end of support timeline](xray-daemon-eos.md "xray-daemon-eos.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

There are two ways to instrument your Python application to send traces to X-Ray:

- [AWS Distro for OpenTelemetry Python](xray-python-opentel-sdk.md "xray-python-opentel-sdk.md") – An AWS distribution that provides a
  set of open source libraries for sending correlated metrics and traces to multiple AWS monitoring
  solutions, including
  Amazon CloudWatch, AWS X-Ray, and Amazon OpenSearch Service, via the [AWS Distro for OpenTelemetry Collector](https://aws-otel.github.io/docs/getting-started/collector "https://aws-otel.github.io/docs/getting-started/collector").
- [AWS X-Ray SDK for Python](xray-sdk-python.md "xray-sdk-python.md") – A set of libraries for generating
  and sending traces to X-Ray via the [X-Ray daemon](xray-daemon.md "xray-daemon.md").

For more information, see [Choosing between the AWS Distro for OpenTelemetry and X-Ray SDKs](xray-instrumenting-your-app.md#xray-instrumenting-choosing "xray-instrumenting-your-app.md#xray-instrumenting-choosing").
