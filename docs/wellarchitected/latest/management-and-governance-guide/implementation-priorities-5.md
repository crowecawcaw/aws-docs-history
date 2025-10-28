# Implementation priorities

## Collect, aggregate, and protect event and log data

After you have provisioned your multi-account framework with
[AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/"), you will have enabled the centralized
collection of observable metrics and events to a log archive
account, using CloudTrail. This collection uses a dedicated and
encrypted Amazon S3 bucket, in a dedicated account, with access
restricted. Encryption keys should be rotated on a regular basis
to increase the security posture of the log archive. Use log
aggregation to increase your visibility at scale. Use a service
control policy to prevent changes to log configurations.

Use
[AWS Systems Manager Quick Setup](../../../systems-manager/latest/userguide/systems-manager-quick-setup.md "../../../systems-manager/latest/userguide/systems-manager-quick-setup.md") with policies defined at the
organization level, to deploy the
[CloudWatch
agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md") to EC2 instances across your environments. This will
enable system-level metrics to be aggregated alongside your other
log data. Feed events into an event management or SIEM platform
that has been adapted for AWS environments via API integration.
Logs, metrics, and traces should be collected across the following
observability categories:

- **Control plane
  observability**—Enable CloudTrail logging to capture
  API call activity. As accounts are provisioned from AWS Control Tower, a service control policy will be provisioned
  which prevents changes to the CloudTrail configuration and log
  archive account.
- **Network
  observability**—Monitor and track network events and
  behaviors including network firewalls, network intrusion
  detection and prevention, load balancers, AWS WAF, proxy
  tools, and network flow data collection and monitoring. Track
  events and behaviors related to access controls (for example,
  security groups and firewall services) and monitor network
  activity with Amazon VPC Flow Logs and packet inspection with
  Amazon VPC Traffic Mirroring.
- **Workload observability**
  (including distributed tracing within your application
  observability solutions for serverless, container, storage,
  and database workloads)—Track events and behaviors at scale as
  workloads communicate within the cloud environment as a whole,
  in addition to the local application logs on individual
  systems.

## Build capabilities to analyze and visualize log events and traces

Build capabilities to interactively search and analyze your local
and centralized log data. As you scale with AWS, you will need to
include the ability to index and visualize your log insights and
metrics. Correlate logs and performance metrics across different
types of data collection to drive meaningful conclusions and
insights. Use rules to effectively respond to security events or
patterns identified in your logs. Develop a nearly continuous
monitoring strategy to scale your observability capabilities as
you migrate and grow solutions on AWS.

## Add detection and alerts for anomalous patterns across

environments

Proactively assess environments for known vulnerabilities and add
detection for anomalous patterns of events and activities. Monitor
for unusual activity or behavior related to users and workloads
using tools such as
[Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/"),
[Amazon CloudWatch ServiceLens](../../../AmazonCloudWatch/latest/monitoring/ServiceLens.md "../../../AmazonCloudWatch/latest/monitoring/ServiceLens.md"), and
[Amazon CloudWatch dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md"). Start with patterns or indicators of
unintended account usage or permissions including any login
activity to cloud management consoles, any changes, or attempted
changes to important cloud objects and data, and any creation,
deletion, or modification of credentials or cryptographic keys.
Detect incidents and patterns of denials of access, unidentified
network traffic, atypical increases in cloud services costs, and
unusual application traffic behavior. Configure Amazon CloudWatch
alarms, GuardDuty, and SIEMs to initiate alerts and notifications
using [Amazon Simple Notification Service](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/") (Amazon SNS). Identify anomalous
behavior with
[Amazon DevOps Guru](https://aws.amazon.com/devops-guru/ "https://aws.amazon.com/devops-guru/"),
[AWS X-Ray Insights](../../../xray/latest/devguide/xray-console-insights.md "../../../xray/latest/devguide/xray-console-insights.md"), and
[Amazon CloudWatch Contributor Insights](../../../AmazonCloudWatch/latest/monitoring/ContributorInsights.md "../../../AmazonCloudWatch/latest/monitoring/ContributorInsights.md").

## Define, automate, and measure response and remediation

Establish expected behavior thresholds paired with business
metrics to understand KPIs for workloads and environments.
Determine appropriate incident and response actions to pursue. 
Use SIEM solutions to monitor workloads in real-time, identify
security issues, and expedite root-cause analysis.

Automations can be initiated by
[several
different triggers](../../../systems-manager/latest/userguide/automation-executing-triggers.md "../../../systems-manager/latest/userguide/automation-executing-triggers.md"), such as EventBridge, State Manager
associations, and maintenance windows. By using triggers, you can
run automations because of a specific event or on a scheduled
basis. Events can be derived from pattern matching using Amazon CloudWatch alerts or SIEM. Take advantage of security
orchestration, automation, and response platforms (SOAR) while
pairing with responses created from recorded events with tools
like AWS Lambda. Maintain a process to continually improve mean
time to identify (MTTI) root cause and mean time to respond (MTTR)
to problems. Establish and measure goals to reduce the time to
detect, identify, and remediate issues. This can also be done in
conjunction with post-mortem or lessons learned procedures that
align with your existing software development lifecycle or
management practices.
