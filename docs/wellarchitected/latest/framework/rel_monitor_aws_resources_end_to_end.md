# REL06-BP07 Monitor end-to-end tracing of requests through your

system

Trace requests as they process through service components so product teams can more easily analyze and debug issues and improve performance.

**Desired outcome:** Workloads with comprehensive tracing across all components are easy to debug, improving [mean time to resolution](../../../whitepapers/latest/availability-and-beyond-improving-resilience/reducing-mttr.md "../../../whitepapers/latest/availability-and-beyond-improving-resilience/reducing-mttr.md") (MTTR) of errors and latency by simplifying root cause discovery. End-to-end tracing reduces the time it takes to discover impacted components and drill into the detailed root causes of errors or latency.

**Common anti-patterns:**

- Tracing is used for some components but not for all. For example, without tracing for AWS Lambda, teams might not clearly understand latency caused by cold starts in a spiky workload.
- Synthetic canaries or real-user monitoring (RUM) are not configured with tracing. Without canaries or RUM, client interaction telemetry is omitted from the trace analysis yielding an incomplete performance profile.
- Hybrid workloads include both cloud native and third party tracing tools, but steps have not been taken elect and fully integrate a single tracing solution. Based on the elected tracing solution, cloud native tracing SDKs should be used to instrument components that are not cloud native or third party tools should be configured to ingest cloud native trace telemetry.

**Benefits of establishing this best practice:** When development teams are alerted to issues, they can see a full picture of system component interactions, including component by component correlation to logging, performance, and failures. Because tracing makes it easy to visually identify root causes, less time is spent investigating root causes. Teams that understand component interactions in detail make better and faster decisions when resolving issues. Decisions like when to invoke disaster recovery (DR) failover or where to best implement self-healing strategies can be improved by analyzing systems traces, ultimately improving customer satisfaction with your services.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Teams that operate distributed applications can use tracing tools to establish a correlation identifier, collect traces of requests, and build service maps of connected components. All application components should be included in request traces including service clients, middleware gateways and event buses, compute components, and storage, including key value stores and databases. Include synthetic canaries and real-user monitoring in your end-to-end tracing configuration to measure remote client interactions and latency so that you can accurately evaluate your systems performance against your service level agreements and objectives.

You can use [AWS X-Ray](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md") and [Amazon CloudWatch Application Monitoring](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.md") instrumentation services to provide a complete view of requests as they travel through your application. X-Ray collects application telemetry and allows you to visualize and filter it across payloads, functions, traces, services, APIs, and can be turned on for system components with no-code or low-code. CloudWatch application monitoring includes ServiceLens to integrate your traces with metrics, logs, and alarms. CloudWatch application monitoring also includes synthetics to monitor your endpoints and APIs, as well as real-user monitoring to instrument your web application clients.

## Implementation steps

- Use AWS X-Ray on all supported native services like [Amazon S3, AWS Lambda, and Amazon API Gateway](../../../xray/latest/devguide/xray-services.md "../../../xray/latest/devguide/xray-services.md"). These AWS services enable X-Ray with configuration toggles using infrastructure as code, AWS SDKs, or the AWS Management Console.
- Instrument applications [AWS Distro for Open Telemetry and X-Ray](../../../xray/latest/devguide/xray-services-adot.md "../../../xray/latest/devguide/xray-services-adot.md") or third-party collection agents.
- Review the [AWS X-Ray Developer Guide](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md") for programming language specific implementation. These documentation sections detail how to instrument HTTP requests, SQL queries, and other processes specific to your application programming language.
- Use X-Ray tracing for [Amazon CloudWatch Synthetic Canaries](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md") and [Amazon CloudWatch RUM](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md") to analyze the request path from your end user client through your downstream AWS infrastructure.
- Configure CloudWatch metrics and alarms based on resource health and canary telemetry so that teams are alerted to issues quickly, and can then deep dive into traces and service maps with ServiceLens.
- Enable X-Ray integration for third party tracing tools like [Datadog](https://docs.datadoghq.com/tracing/guide/serverless_enable_aws_xray/ "https://docs.datadoghq.com/tracing/guide/serverless_enable_aws_xray/"), [New Relic](https://docs.newrelic.com/docs/infrastructure/amazon-integrations/aws-integrations-list/aws-x-ray-monitoring-integration/ "https://docs.newrelic.com/docs/infrastructure/amazon-integrations/aws-integrations-list/aws-x-ray-monitoring-integration/"), or [Dynatrace](https://www.dynatrace.com/support/help/setup-and-configuration/setup-on-cloud-platforms/amazon-web-services/amazon-web-services-integrations/aws-service-metrics "https://www.dynatrace.com/support/help/setup-and-configuration/setup-on-cloud-platforms/amazon-web-services/amazon-web-services-integrations/aws-service-metrics") if you are using third party tools for your primary tracing solution.

## Resources

**Related best practices:**

- [REL06-BP01 Monitor all components for the workload
  (Generation)](rel_monitor_aws_resources_monitor_resources.md "rel_monitor_aws_resources_monitor_resources.md")
- [REL11-BP01 Monitor all components of the workload to detect
  failures](rel_withstand_component_failures_monitoring_health.md "rel_withstand_component_failures_monitoring_health.md")

**Related documents:**

- [What
  is AWS X-Ray?](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md")
- [Amazon CloudWatch: Application Monitoring](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.md")
- [Debugging
  with Amazon CloudWatch Synthetics and AWS X-Ray](https://aws.amazon.com/blogs/devops/debugging-with-amazon-cloudwatch-synthetics-and-aws-x-ray/ "https://aws.amazon.com/blogs/devops/debugging-with-amazon-cloudwatch-synthetics-and-aws-x-ray/")
- [The
  Amazon Builders' Library: Instrumenting distributed systems
  for operational visibility](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/ "https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/")
- [Integrating AWS X-Ray with other AWS services](../../../xray/latest/devguide/xray-services.md "../../../xray/latest/devguide/xray-services.md")
- [AWS Distro for OpenTelemetry and AWS X-Ray](../../../xray/latest/devguide/xray-services-adot.md "../../../xray/latest/devguide/xray-services-adot.md")
- [Amazon CloudWatch: Using synthetic monitoring](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md")
- [Amazon CloudWatch: Use CloudWatch RUM](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md")
- [Set up Amazon CloudWatch synthetics canary and Amazon CloudWatch alarm](../../../solutions/latest/devops-monitoring-dashboard-on-aws/set-up-amazon-cloudwatch-synthetics-canary-and-amazon-cloudwatch-alarm.md "../../../solutions/latest/devops-monitoring-dashboard-on-aws/set-up-amazon-cloudwatch-synthetics-canary-and-amazon-cloudwatch-alarm.md")
- [Availability and Beyond: Understanding and Improving the Resilience of Distributed Systems on AWS](../../../whitepapers/latest/availability-and-beyond-improving-resilience/reducing-mttr.md "../../../whitepapers/latest/availability-and-beyond-improving-resilience/reducing-mttr.md")

**Related examples:**

- [One Observability Workshop](https://catalog.workshops.aws/observability/en-US "https://catalog.workshops.aws/observability/en-US")

**Related videos:**

- [AWS re:Invent 2022 - How to monitor applications across multiple accounts](https://www.youtube.com/watch?v=kFGOkywu-rw "https://www.youtube.com/watch?v=kFGOkywu-rw")
- [How to Monitor your AWS Applications](https://www.youtube.com/watch?v=UxWU9mrSbmA "https://www.youtube.com/watch?v=UxWU9mrSbmA")

**Related tools:**

- [AWS X-Ray](https://aws.amazon.com/xray/ "https://aws.amazon.com/xray/")
- [Amazon CloudWatch](https://aws.amazon.com/pm/cloudwatch/ "https://aws.amazon.com/pm/cloudwatch/")
- [Amazon Route 53](https://aws.amazon.com/route53/ "https://aws.amazon.com/route53/")
