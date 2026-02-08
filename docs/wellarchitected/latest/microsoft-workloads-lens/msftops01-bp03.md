# MSFTOPS01-BP03 Implement Application Performance Monitoring

(APM) for your Microsoft workload

Microsoft workloads developed with .NET and SQL technologies should
also have Application Performance Monitoring (APM) implemented.
Amazon CloudWatch Application Insights for .NET and SQL Server can
be used for that purpose. AWS X-Ray can be used as well to improve
traceability over the workload.

**Desired outcome:** Establish
comprehensive Application Performance Monitoring (APM) for your
Microsoft workloads, providing deep visibility into application
behavior, performance bottlenecks, and user experience while
enabling proactive optimization and rapid troubleshooting of .NET
applications and SQL Server databases.

**Common anti-patterns:**

- Monitoring only infrastructure metrics without implementing
  application-level monitoring, missing critical insights into
  application performance, user experience, and business
  transaction flows that could indicate problems before they
  affect users.
- Implementing APM tools without proper configuration for
  Microsoft-specific technologies, failing to capture important
  .NET application metrics, SQL Server performance indicators, and
  transaction traces that are essential for effective
  troubleshooting.
- Using APM reactively only during incidents rather than
  proactively monitoring application performance trends, missing
  opportunities to optimize performance and prevent issues before
  they impact business operations.

**Benefits of establishing this best
practice:**

- Enhanced application visibility and faster issue resolution
  through detailed monitoring of .NET application performance, SQL
  Server operations, and end-to-end transaction tracing, enabling
  rapid identification and resolution of performance bottlenecks.
- Improved user experience and business outcomes by monitoring
  application performance from the user perspective, identifying
  slow transactions, and optimizing critical business processes
  before they impact customer satisfaction.
- Proactive performance optimization through continuous monitoring
  of application metrics, enabling data-driven decisions for code
  optimization, database tuning, and infrastructure scaling to
  maintain optimal performance.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing Application Performance Monitoring for Microsoft
workloads requires a comprehensive approach that covers both .NET
applications and SQL Server databases. Start by configuring Amazon CloudWatch Application Insights to automatically discover and
monitor your Microsoft applications, then enhance visibility with
AWS X-Ray for distributed tracing. This approach provides
end-to-end visibility into application performance and enables
proactive optimization of your Microsoft workloads.

### Implementation steps

1. Enable Amazon CloudWatch Application Insights for your .NET
   applications and SQL Server instances to automatically
   discover and monitor application components.
2. Configure Application Insights to collect custom metrics
   specific to your Microsoft workload business logic and
   critical transactions.
3. Implement AWS X-Ray daemon in your .NET applications to
   track requests across distributed components and identify
   performance bottlenecks.
4. Set up custom dashboards in Amazon CloudWatch to visualize
   application performance metrics, error rates, and response
   times for critical business transactions.
5. Configure automated alerts for application performance
   thresholds, error rates, and anomaly detection to enable
   proactive issue identification.
6. Implement synthetic monitoring using Amazon CloudWatch
   Synthetics to continuously test critical application
   workflows and user journeys.
7. Establish performance baselines and regularly review APM
   data to identify optimization opportunities and performance
   trends.
8. Integrate APM data with your incident response processes to
   enable faster troubleshooting and root cause analysis.

## Resources

**Related documents:**

- [Monitoring
  .NET applications on AWS](../../../whitepapers/latest/develop-deploy-dotnet-apps-on-aws/monitoring.md "../../../whitepapers/latest/develop-deploy-dotnet-apps-on-aws/monitoring.md")
- [Amazon CloudWatch Synthetic monitoring (canaries)](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md")
- [Monitor
  .NET and SQL Server applications using CloudWatch Application Insights](../../../AWSEC2/latest/UserGuide/monitoring-appinsights.md "../../../AWSEC2/latest/UserGuide/monitoring-appinsights.md")
- [.NET
  observability with Amazon CloudWatch and AWS X-Ray: Part 1 —
  Metrics](https://aws.amazon.com/blogs/modernizing-with-aws/net-observability-cloudwatch-aws-x-ray-part1-metrics/ "https://aws.amazon.com/blogs/modernizing-with-aws/net-observability-cloudwatch-aws-x-ray-part1-metrics/")
- [.NET
  observability with Amazon CloudWatch and AWS X-Ray: Part 2 —
  Logging](https://aws.amazon.com/blogs/modernizing-with-aws/net-observability-cloudwatch-aws-x-ray-part2-logging/ "https://aws.amazon.com/blogs/modernizing-with-aws/net-observability-cloudwatch-aws-x-ray-part2-logging/")
- [.NET
  Observability with Amazon CloudWatch and AWS X-Ray: Part 3 –
  Distributed Trace](https://aws.amazon.com/blogs/modernizing-with-aws/net-observability-cloudwatch-aws-x-ray-part3-distributed-trace/ "https://aws.amazon.com/blogs/modernizing-with-aws/net-observability-cloudwatch-aws-x-ray-part3-distributed-trace/")

**Related tools:**

- [What
  is APM (Application Performance Monitoring)?](https://aws.amazon.com/what-is/application-performance-monitoring/ "https://aws.amazon.com/what-is/application-performance-monitoring/")
- [Detect
  common application problems with CloudWatch Application Insights](../../../AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.md")
- [AWS X-Ray](../../../xray/latest/devguide/xray-gettingstarted.md "../../../xray/latest/devguide/xray-gettingstarted.md")
- [Amazon CloudWatch Synthetics](https://github.com/aws-samples/amazon-cloudwatch-synthetics-page-performance/actions "https://github.com/aws-samples/amazon-cloudwatch-synthetics-page-performance/actions")
