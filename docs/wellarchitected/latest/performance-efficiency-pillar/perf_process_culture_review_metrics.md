# PERF05-BP07 Review metrics at regular intervals

As part of routine maintenance or in response to events or
incidents, review which metrics are collected. Use these reviews to
identify which metrics were essential in addressing issues and which
additional metrics, if they were being tracked, could help identify,
address, or prevent issues.

**Common anti-patterns:**

- You allow metrics to stay in an alarm state for an extended
  period of time.
- You create alarms that are not actionable by an automation
  system.

**Benefits of establishing this best
practice:** Continually review metrics that are being
collected to verify that they properly identify, address, or prevent
issues. Metrics can also become stale if you let them stay in an
alarm state for an extended period of time.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Constantly improve metric collection and monitoring. As part of
responding to incidents or events, evaluate which metrics were
helpful in addressing the issue and which metrics could have
helped that are not currently being tracked. Use this method to
improve the quality of metrics you collect so that you can prevent,
or more quickly resolve future incidents.

As part of responding to incidents or events, evaluate which
metrics were helpful in addressing the issue and which metrics
could have helped that are not currently being tracked. Use this
to improve the quality of metrics you collect so that you can
prevent or more quickly resolve future incidents.

### Implementation steps

- **Define metrics:** Define critical performance metrics to monitor that are aligned to your workload
  objective, including metrics such as response time and resource utilization.
- **Establish baselines:** Set a baseline and desirable value for each metric. The baseline should provide reference points to identify deviation or anomalies.
- **Set up a cadence:** Set a cadence (like weekly or monthly) to review critical metrics.
- **Identify performance issues:** During each review, assess trends and deviation from the baseline values. Look for
  any performance bottlenecks or anomalies. For identified issues, conduct in-depth root cause analysis to understand the main
  reason behind the issue.
- **Identify corrective actions:** Use your analysis to identify corrective actions. This may include parameter tuning, fixing bugs, and scaling resources.
- **Document findings:** Document your findings, including identified issues, root causes, and corrective actions.
- **Iterate and improve:** Continually assess and improve the metrics review process. Use the lesson learned from previous review to enhance the process over time.

## Resources

**Related documents:**

- [CloudWatch
  Documentation](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md")
- [Collect
  metrics and logs from Amazon EC2 Instances and on-premises
  servers with the CloudWatch Agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md")
- [Query your metrics with CloudWatch Metrics Insights](../../../AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.md "../../../AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.md")
- [Monitoring,
  Logging, and Performance AWS Partner Network Partners](https://aws.amazon.com/devops/partner-solutions/#_Monitoring.2C_Logging.2C_and_Performance "https://aws.amazon.com/devops/partner-solutions/#_Monitoring.2C_Logging.2C_and_Performance")
- [X-Ray
  Documentation](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md")

**Related videos:**

- [AWS re:Invent 2022 - Setting
  up controls at scale in your AWS environment](https://www.youtube.com/watch?v=NkE9_okfPG8 "https://www.youtube.com/watch?v=NkE9_okfPG8")
- [AWS re:Invent 2022 - How
  Amazon uses better metrics for improved website
  performance](https://www.youtube.com/watch?v=_uaaCiyJCFA&ab_channel=AWSEvents "https://www.youtube.com/watch?v=_uaaCiyJCFA&ab_channel=AWSEvents")
- [AWS re:Invent 2023 - Building an effective observability strategy](https://www.youtube.com/watch?v=7PQv9eYCJW8 "https://www.youtube.com/watch?v=7PQv9eYCJW8")
- [AWS Summit SF 2022 - Full-stack observability and application monitoring with AWS](https://www.youtube.com/watch?v=or7uFFyHIX0 "https://www.youtube.com/watch?v=or7uFFyHIX0")
- [AWS re:Invent 2023 - Take a load off: Diagnose & resolve performance issues with Amazon RDS](https://www.youtube.com/watch?v=Ulj88e5Aqzg "https://www.youtube.com/watch?v=Ulj88e5Aqzg")

**Related examples:**

- [Creating
  a dashboard with Quick Suite](https://github.com/aws-samples/amazon-quicksight-sdk-proserve "https://github.com/aws-samples/amazon-quicksight-sdk-proserve")
- [CloudWatch Dashboards](https://catalog.us-east-1.prod.workshops.aws/workshops/a8e9c6a6-0ba9-48a7-a90d-378a440ab8ba/en-US/300-cloudwatch/340-cloudwatch-dashboards "https://catalog.us-east-1.prod.workshops.aws/workshops/a8e9c6a6-0ba9-48a7-a90d-378a440ab8ba/en-US/300-cloudwatch/340-cloudwatch-dashboards")
