

# Application Signals (Classic)

The Amazon CloudWatch Observability add-on and Helm chart turn on CloudWatch Application Signals by default. The CloudWatch agent operator injects the AWS Distro for OpenTelemetry (ADOT) SDK into the Java, Python, .NET, and Node.js workloads that you choose to instrument, and the CloudWatch agent receives their metrics and traces. Application Signals then shows the request volume, availability, latency, and dependencies of each service. You can also set service level objectives (SLOs) on each service.

Application Signals (Classic) sends its metrics to CloudWatch as classic CloudWatch metrics, through embedded metric format (EMF) log events, not as OpenTelemetry metrics. You query them with the CloudWatch metrics APIs and Metrics Insights, not PromQL. Traces go to X-Ray.

To send telemetry from your own OpenTelemetry SDK or collector instead, use the OTLP endpoint. For more information, see [OTLP ingestion](eks-observability-addon-otlp-endpoint.md).

For more information about Application Signals, see the following topics:
+ [Application Signals](CloudWatch-Application-Monitoring-Sections.md)
+ [Enable your applications on Amazon EKS clusters](CloudWatch-Application-Signals-Enable-EKS.md)
+ [Enabling APM through Application Signals for your Amazon EKS cluster](install-CloudWatch-Observability-EKS-addon.md#Container-Insights-setup-EKS-appsignalsconfiguration)