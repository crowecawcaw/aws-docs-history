# Getting started

To get started with OpenTelemetry in CloudWatch, you can choose from several options to send telemetry to the
CloudWatch OTLP endpoints. For most customers, the CloudWatch agent is the recommended path. The CloudWatch agent is an
AWS-managed OpenTelemetry Collector with CloudWatch components pre-built, and it provides the most integrated
monitoring experience in CloudWatch.

You also have the flexibility to use an upstream OpenTelemetry Collector, build your own custom OpenTelemetry
Collector, or send telemetry directly to the OTLP endpoint without a collector agent using the AWS Distro for
OpenTelemetry (ADOT) SDK. Make an informed choice based on the feature support:

| Feature                                                                                                  | CloudWatch agent (recommended) | Upstream OpenTelemetry Collector | Custom OpenTelemetry Collector | Collectorless with AWS Distro for OpenTelemetry (ADOT) SDK |
| -------------------------------------------------------------------------------------------------------- | ------------------------------ | -------------------------------- | ------------------------------ | ---------------------------------------------------------- |
| Search and analyze spans and trace summaries                                                             | Yes                            | Yes                              | Yes                            | Yes                                                        |
| Search and analyze logs summaries                                                                        | Yes                            | Yes                              | Yes                            | No                                                         |
| CloudWatch entity correlation (resource linkage in the console and service map)                          | Yes                            | No                               | Yes                            | No                                                         |
| Runtime metrics correlated with your application. For example, JVM metrics                               | Yes                            | No                               | Yes                            | No                                                         |
| CloudWatch Enhanced Container Insights                                                                   | Yes                            | No                               | No                             | No                                                         |
| CloudWatch Application Signals (Application performance metrics, service discovery, and application map) | Yes                            | No                               | Yes                            | Yes                                                        |
| Telemetry supported                                                                                      | Logs, Metrics, Traces          | Logs, Metrics, Traces            | Logs, Metrics, Traces          | Metrics, Traces                                            |

###### Note

Make sure Transaction Search is enabled before you use the OTLP Endpoint for traces.

###### Note

AWS supports telemetry that you send to AWS destinations through the CloudWatch OTLP endpoints.

###### Topics

- [Amazon CloudWatch agent](CloudWatch-OTLPCloudWatchAgent.md "CloudWatch-OTLPCloudWatchAgent.md")
- [OpenTelemetry Collector](CloudWatch-OTLPSimplesetup.md "CloudWatch-OTLPSimplesetup.md")
- [Build your own custom OpenTelemetry Collector](CloudWatch-OTLPAdvancedsetup.md "CloudWatch-OTLPAdvancedsetup.md")
- [Exporting collector-less telemetry using AWS Distro for OpenTelemetry (ADOT) SDK](CloudWatch-OTLP-UsingADOT.md "CloudWatch-OTLP-UsingADOT.md")
- [Managed Prometheus collectors](CloudWatch-OTLPManagedPrometheusCollectors.md "CloudWatch-OTLPManagedPrometheusCollectors.md")
