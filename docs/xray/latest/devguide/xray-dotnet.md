# Working with .NET

###### Note

X-Ray SDK/Daemon Maintenance Notice – On February 25th, 2026, the AWS X-Ray SDKs/Daemon will enter maintenance mode, where AWS will limit X-Ray SDK and Daemon releases to address security issues only. For more information on the support timeline, see
[X-Ray SDK and Daemon Support timeline](xray-sdk-daemon-timeline.md "xray-sdk-daemon-timeline.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

There are two ways to instrument your .NET application to send traces to X-Ray:

- [AWS Distro for OpenTelemetry .NET](xray-dotnet-opentel-sdk.md "xray-dotnet-opentel-sdk.md") – An AWS distribution that provides a
  set of open source libraries for sending correlated metrics and traces to multiple AWS monitoring solutions
  including Amazon CloudWatch, AWS X-Ray, and Amazon OpenSearch Service, via the [AWS Distro for OpenTelemetry Collector](https://aws-otel.github.io/docs/getting-started/collector "https://aws-otel.github.io/docs/getting-started/collector").
- [AWS X-Ray SDK for .NET](xray-sdk-dotnet.md "xray-sdk-dotnet.md") – A set of libraries for generating
  and sending traces to X-Ray via the [X-Ray daemon](xray-daemon.md "xray-daemon.md").
  For more information, see [Choosing between the AWS Distro for OpenTelemetry and X-Ray SDKs](xray-instrumenting-your-app.md#xray-instrumenting-choosing "xray-instrumenting-your-app.md#xray-instrumenting-choosing").
