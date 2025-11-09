# PERF05-BP02 Use monitoring solutions to understand the areas

where performance is most critical

Understand and identify areas where increasing the performance of
your workload will have a positive impact on efficiency or customer
experience. For example, a website that has a large amount of
customer interaction can benefit from using edge services to move
content delivery closer to customers.

**Common anti-patterns:**

- You assume that standard compute metrics such as CPU utilization
  or memory pressure are enough to catch performance issues.
- You only use the default metrics recorded by your selected
  monitoring software.
- You only review metrics when there is an issue.

**Benefits of establishing this best
practice:** Understanding critical areas of performance
helps workload owners monitor KPIs and prioritize high-impact
improvements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Set up end-to-end tracing to identify traffic patterns, latency,
and critical performance areas. Monitor your data access patterns
for slow queries or poorly fragmented and partitioned data.
Identify the constrained areas of the workload using load testing
or monitoring.

Increase performance efficiency by understanding your
architecture, traffic patterns, and data access patterns, and
identify your latency and processing times. Identify the potential
bottlenecks that might affect the customer experience as the
workload grows. After investigating these areas, look at which
solution you could deploy to remove those performance concerns.

### Implementation steps

- Set up end-to-end monitoring to capture all workload
  components and metrics. Here are examples of monitoring
  solutions on AWS.

| Service                                                                                                                                                                       | Where to use                                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Amazon CloudWatch Real-User Monitoring (RUM)](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md") | To capture application performance metrics from real<br>user client-side and frontend sessions.                                                                                                         |
| [AWS X-Ray](https://aws.amazon.com/xray/ "https://aws.amazon.com/xray/")                                                                                                      | To trace traffic through the application layers and<br>identify latency between components and dependencies.<br>Use X-Ray service maps to see relationships and latency<br>between workload components. |
| [Amazon Relational Database Service Performance Insights](https://aws.amazon.com/rds/performance-insights/ "https://aws.amazon.com/rds/performance-insights/")                | To view database performance metrics and identify<br>performance improvements.                                                                                                                          |
| [Amazon RDS Enhanced Monitoring](../../../AmazonRDS/latest/UserGuide/USER_Monitoring.md "../../../AmazonRDS/latest/UserGuide/USER_Monitoring.md")                             | To view database OS performance metrics.                                                                                                                                                                |
| [Amazon<br>DevOps Guru](https://aws.amazon.com/devops-guru/ "https://aws.amazon.com/devops-guru/")                                                                            | To detect abnormal operating patterns so you can<br>identify operational issues before they impact your<br>customers.                                                                                   |

- Perform tests to generate metrics, identify traffic
  patterns, bottlenecks, and critical performance areas. Here
  are some examples of how to perform testing:
  - Set
    up [CloudWatch
    Synthetic Canaries](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md") to mimic browser-based user
    activities programmatically using Linux cron jobs or
    rate expressions to generate consistent metrics over
    time.
  - Use the [AWS Distributed Load Testing](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/ "https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/") solution to generate
    peak traffic or test the workload at the expected growth
    rate.

- Evaluate the metrics and telemetry to identify your critical
  performance areas. Review these areas with your team to
  discuss monitoring and solutions to avoid bottlenecks.
- Experiment with performance improvements and measure those
  changes with data. As an example, you can
  use [CloudWatch
  Evidently](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently.md") to test new improvements and performance
  impacts to your workload.

## Resources

**Related documents:**

- [What's new in AWS Observability at re:Invent 2023](https://aws.amazon.com/blogs/mt/whats-new-in-aws-observability-at-reinvent-2023/ "https://aws.amazon.com/blogs/mt/whats-new-in-aws-observability-at-reinvent-2023/")
- [Amazon
  Builders’ Library](https://aws.amazon.com/builders-library "https://aws.amazon.com/builders-library")
- [X-Ray
  Documentation](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md")
- [Amazon CloudWatch RUM](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md")
- [Amazon DevOps Guru](https://aws.amazon.com/devops-guru/ "https://aws.amazon.com/devops-guru/")

**Related videos:**

- [AWS re:Invent 2023 - [LAUNCH] Application monitoring for modern workloads](https://www.youtube.com/watch?v=T2TovTLje8w "https://www.youtube.com/watch?v=T2TovTLje8w")
- [AWS re:Invent 2023 - Implementing application observability](https://www.youtube.com/watch?v=IcTcwUSwIs4 "https://www.youtube.com/watch?v=IcTcwUSwIs4")
- [AWS re:Invent 2023 - Building an effective observability strategy](https://www.youtube.com/watch?v=7PQv9eYCJW8 "https://www.youtube.com/watch?v=7PQv9eYCJW8")
- [AWS Summit SF 2022 - Full-stack observability and application monitoring with AWS](https://www.youtube.com/watch?v=or7uFFyHIX0 "https://www.youtube.com/watch?v=or7uFFyHIX0")
- [AWS re:Invent 2022 - AWS optimization: Actionable steps for immediate results](https://www.youtube.com/watch?v=0ifvNf2Tx3w "https://www.youtube.com/watch?v=0ifvNf2Tx3w")
- [AWS re:Invent 2022 - The
  Amazon Builders’ Library: 25 years of Amazon operational
  excellence](https://www.youtube.com/watch?v=DSRhgBd_gtw "https://www.youtube.com/watch?v=DSRhgBd_gtw")
- [AWS re:Invent 2022 - How Amazon uses better metrics for improved website performance](https://www.youtube.com/watch?v=_uaaCiyJCFA "https://www.youtube.com/watch?v=_uaaCiyJCFA")
- [Visual
  Monitoring of Applications with Amazon CloudWatch
  Synthetics](https://www.youtube.com/watch?v=_PCs-ucZz7E "https://www.youtube.com/watch?v=_PCs-ucZz7E")

**Related examples:**

- [Measure
  page load time with Amazon CloudWatch Synthetics](https://github.com/aws-samples/amazon-cloudwatch-synthetics-page-performance "https://github.com/aws-samples/amazon-cloudwatch-synthetics-page-performance")
- [Amazon CloudWatch RUM Web Client](https://github.com/aws-observability/aws-rum-web "https://github.com/aws-observability/aws-rum-web")
- [X-Ray
  SDK for Python](https://github.com/aws/aws-xray-sdk-python "https://github.com/aws/aws-xray-sdk-python")
- [Distributed
  Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/ "https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/")
