# REL06-BP01 Monitor all components for the workload

(Generation)

Monitor the components of the workload with Amazon CloudWatch or
third-party tools. Monitor AWS services with AWS Health Dashboard.

All components of your workload should be monitored, including the
front-end, business logic, and storage tiers. Define key metrics,
describe how to extract them from logs (if necessary), and set
thresholds for invoking corresponding alarm events. Ensure metrics
are relevant to the key performance indicators (KPIs) of your
workload, and use metrics and logs to identify early warning signs
of service degradation. For example, a metric related to business
outcomes such as the number of orders successfully processed per
minute, can indicate workload issues faster than technical metric,
such as CPU Utilization. Use AWS Health Dashboard for a personalized
view into the performance and availability of the AWS services
underlying your AWS resources.

Monitoring in the cloud offers new opportunities. Most cloud
providers have developed customizable hooks and can deliver insights
to help you monitor multiple layers of your workload. AWS services
such as Amazon CloudWatch apply statistical and machine learning
algorithms to continually analyze metrics of systems and
applications, determine normal baselines, and surface anomalies with
minimal user intervention. Anomaly detection algorithms account for
the seasonality and trend changes of metrics.

AWS makes an abundance of monitoring and log information available
for consumption that can be used to define workload-specific
metrics, change-in-demand processes, and adopt machine learning
techniques regardless of ML expertise.

In addition, monitor all of your external endpoints to ensure that
they are independent of your base implementation. This active
monitoring can be done with synthetic transactions (sometimes
referred to as _user canaries_, but not to be
confused with canary deployments) which periodically run a number of
common tasks matching actions performed by clients of the workload.
Keep these tasks short in duration and be sure not to overload your
workload during testing. Amazon CloudWatch Synthetics allows you
to [create
synthetic canaries](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md") to monitor your endpoints and APIs. You
can also combine the synthetic canary client nodes with AWS X-Ray
console to pinpoint which synthetic canaries are experiencing issues
with errors, faults, or throttling rates for the selected time
frame.

**Desired Outcome:**

Collect and use critical metrics from all components of the workload
to ensure workload reliability and optimal user experience.
Detecting that a workload is not achieving business outcomes allows
you to quickly declare a disaster and recover from an incident.

**Common anti-patterns:**

- Only monitoring external interfaces to your workload.
- Not generating any workload-specific metrics and only relying on
  metrics provided to you by the AWS services your workload uses.
- Only using technical metrics in your workload and not monitoring
  any metrics related to non-technical KPIs the workload
  contributes to.
- Relying on production traffic and simple health checks to
  monitor and evaluate workload state.

**Benefits of establishing this best
practice:** Monitoring at all tiers in your workload
allows you to more rapidly anticipate and resolve problems in the
components that comprise the workload.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

1. **Turn on logging where
   available.** Monitoring data should be obtained from
   all components of the workloads. Turn on additional logging,
   such as S3 Access Logs, and permit your workload to log
   workload specific data. Collect metrics for CPU, network I/O,
   and disk I/O averages from services such as Amazon ECS, Amazon EKS, Amazon EC2, Elastic Load Balancing, AWS Auto Scaling, and
   Amazon EMR. See
   [AWS Services That Publish CloudWatch Metrics](../../../AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.md "../../../AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.md") for a list of
   AWS services that publish metrics to CloudWatch.
2. **Review all default metrics and explore
   any data collection gaps.** Every service generates
   default metrics. Collecting default metrics allows you to
   better understand the dependencies between workload
   components, and how component reliability and performance
   affect the workload. You can also create and
   [publish
   your own metrics](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md") to CloudWatch using the AWS CLI or an
   API.
3. **Evaluate all the metrics to decide
   which ones to alert on for each AWS service in your
   workload.** You may choose to select a subset of
   metrics that have a major impact on workload reliability.
   Focusing on critical metrics and threshold allows you to
   refine the number of
   [alerts](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
   and can help minimize false-positives.
4. **Define alerts and the recovery process
   for your workload after the alert is invoked.**
   Defining alerts allows you to quickly notify, escalate, and
   follow steps necessary to recover from an incident and meet
   your prescribed Recovery Time Objective (RTO). You can use
   [Amazon CloudWatch Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-actions "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-actions") to invoke automated
   workflows and initiate recovery procedures based on defined
   thresholds.
5. **Explore use of synthetic transactions
   to collect relevant data about workloads state.**
   Synthetic monitoring follows the same routes and perform the
   same actions as a customer, which makes it possible for you to
   continually verify your customer experience even when you
   don't have any customer traffic on your workloads. By using
   [synthetic
   transactions](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md"), you can discover issues before your
   customers do.

## Resources

**Related best practices:**

- [REL11-BP03 Automate healing on all layers](rel_withstand_component_failures_auto_healing_system.md "rel_withstand_component_failures_auto_healing_system.md")

**Related documents:**

- [Getting
  started with your AWS Health Dashboard – Your account
  health](../../../health/latest/ug/getting-started-health-dashboard.md "../../../health/latest/ug/getting-started-health-dashboard.md")
- [AWS Services That Publish CloudWatch Metrics](../../../AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.md "../../../AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.md")
- [Access
  Logs for Your Network Load Balancer](../../../elasticloadbalancing/latest/network/load-balancer-access-logs.md "../../../elasticloadbalancing/latest/network/load-balancer-access-logs.md")
- [Access
  logs for your application load balancer](../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md "../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md")
- [Accessing
  Amazon CloudWatch Logs for AWS Lambda](../../../lambda/latest/dg/monitoring-functions-logs.md "../../../lambda/latest/dg/monitoring-functions-logs.md")
- [Amazon S3 Server Access Logging](../../../AmazonS3/latest/dev/ServerLogs.md "../../../AmazonS3/latest/dev/ServerLogs.md")
- [Enable
  Access Logs for Your Classic Load Balancer](../../../elasticloadbalancing/latest/classic/enable-access-logs.md "../../../elasticloadbalancing/latest/classic/enable-access-logs.md")
- [Exporting
  log data to Amazon S3](../../../AmazonCloudWatch/latest/logs/S3Export.md "../../../AmazonCloudWatch/latest/logs/S3Export.md")
- [Install
  the CloudWatch agent on an Amazon EC2 instance](../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.md "../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.md")
- [Publishing
  Custom Metrics](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md")
- [Using
  Amazon CloudWatch Dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md")
- [Using
  Amazon CloudWatch Metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md")
- [Using
  Canaries (Amazon CloudWatch Synthetics)](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md")
- [What
  are Amazon CloudWatch Logs?](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md")

**User guides:**

- [Creating
  a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md")
- [Monitoring
  memory and disk metrics for Amazon EC2 Linux instances](../../../AWSEC2/latest/UserGuide/mon-scripts.md "../../../AWSEC2/latest/UserGuide/mon-scripts.md")
- [Using
  CloudWatch Logs with container instances](../../../AmazonECS/latest/developerguide/using_cloudwatch_logs.md "../../../AmazonECS/latest/developerguide/using_cloudwatch_logs.md")
- [VPC
  Flow Logs](../../../AmazonVPC/latest/UserGuide/flow-logs.md "../../../AmazonVPC/latest/UserGuide/flow-logs.md")
- [What
  is Amazon DevOps Guru?](../../../devops-guru/latest/userguide/welcome.md "../../../devops-guru/latest/userguide/welcome.md")
- [What
  is AWS X-Ray?](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md")

**Related blogs:**

- [Debugging
  with Amazon CloudWatch Synthetics and AWS X-Ray](https://aws.amazon.com/blogs/devops/debugging-with-amazon-cloudwatch-synthetics-and-aws-x-ray/ "https://aws.amazon.com/blogs/devops/debugging-with-amazon-cloudwatch-synthetics-and-aws-x-ray/")

**Related examples:**

- [The
  Amazon Builders' Library: Instrumenting distributed systems
  for operational visibility](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/ "https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/")
- [Observability
  workshop](https://catalog.workshops.aws/observability/en-US "https://catalog.workshops.aws/observability/en-US")
