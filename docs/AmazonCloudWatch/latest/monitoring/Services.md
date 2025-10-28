# Monitor the operational health of your applications with Application Signals

Use Application Signals within the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/") to monitor and troubleshoot
the operational health of your applications:

- **Monitor your application services** — As part of daily operational
  monitoring, use the [Services](Services-page.md "Services-page.md") page to see a summary of all your services.
  See services with the highest fault rate or latency, and see which services have unhealthy [service level indicators (SLIs)](CloudWatch-ServiceLevelObjectives.md "CloudWatch-ServiceLevelObjectives.md"). Select a service to open
  the [Service detail](ServiceDetail.md "ServiceDetail.md") page and see detailed metrics, service operations,
  Synthetics canaries, and client requests. This can help you troubleshoot and identify the root cause of
  operational issues.
- **Inspect your application topology** — Use the [Application Map](ServiceMap.md "ServiceMap.md") to understand and monitor your application topology over time,
  including the relationships between clients, Synthetics canaries, services, and dependencies. Instantly see
  service level indicator (SLI) health and view key metrics such as call volume, fault rate, and latency. Drill
  down to see more detailed information in the [Service detail](ServiceDetail.md "ServiceDetail.md") page.
  Explore an [example scenario](Services-example-scenario.md "Services-example-scenario.md") that demonstrates how these pages can be used to quickly troubleshoot
  an operational service health issue, from initial detection to identifying root cause.

**How Application Signals enables operational health monitoring**

After you [enable your application](CloudWatch-Application-Signals-Enable.md "CloudWatch-Application-Signals-Enable.md") for Application
Signals, your application services, APIs, and their dependencies are automatically discovered and displayed in the
**Services**, **Service detail**, and **Application Map** pages.
Application Signals collects information from multiple sources to enable service discovery and operational health
monitoring:

- [AWS Distro for OpenTelemetry (ADOT)](CloudWatch-Application-Signals-supportmatrix.md "CloudWatch-Application-Signals-supportmatrix.md")
  — As part of enabling Application Signals, OpenTelemetry Java and Python auto-instrumentation libraries are
  configured to emit metrics and traces that are collected by the CloudWatch agent. The metrics and traces are used to
  enable discovery of services, operations, dependencies, and other service information.
- [Service-level objectives (SLOs)](CloudWatch-ServiceLevelObjectives.md "CloudWatch-ServiceLevelObjectives.md") — After you create service level objectives for your services,
  the Services, Service detail, and Application Map pages display service level indicator (SLI) health. SLIs can monitor latency, availability, and other
  operational metrics.
- [CloudWatch Synthetics canaries](CloudWatch_Synthetics_Canaries.md "CloudWatch_Synthetics_Canaries.md") — When you configure
  X-Ray tracing on your canaries, calls to your services from your canary scripts are associated with your
  service and displayed within the Service detail page.
- [CloudWatch Real user monitoring (RUM)](CloudWatch-RUM.md "CloudWatch-RUM.md") — When X-Ray tracing is enabled on your CloudWatch RUM web client, requests to your services are automatically associated and
  displayed within the service detail page.
- [AWS Service Catalog AppRegistry](../../../servicecatalog/latest/arguide/intro-app-registry.md "../../../servicecatalog/latest/arguide/intro-app-registry.md")
  — Application Signals auto-discovers AWS resources within your account and allows you to group them
  into logical applications created in AppRegistry. The application name displayed in the Services page is based on
  the underlying compute resource that your services are running on.

###### Note

Application Signals displays your services and operations based on metrics and traces emitted within the
current time filter that you chose. (By default, this is the past three hours.) If there is no activity within
the current time filter for a service, operation, dependency, Synthetics canary, or client page, it won't be
displayed.

Up to 1,000 services can be displayed. Discovery of your services and service topology might be
delayed up to 10 minutes. Evaluation of your service level indicator (SLI) health might be delayed up to 15
minutes.

###### Note

Application Signals console currently only supports choosing a maximum of one day within the 30 days time range.
