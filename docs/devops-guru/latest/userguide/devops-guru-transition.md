

End of support notice: Amazon DevOps Guru will stop accepting new customers on October 29, 2026. Current customers will not be impacted and can continue using Amazon DevOps Guru until September 30, 2027. After September 30, 2027 you will no longer be able to access Amazon DevOps Guru. For more information, see [Amazon DevOps Guru end of support](devops-guru-end-of-support.md).

# Transitioning from Amazon DevOps Guru to Amazon CloudWatch and Amazon DevOps Agent
<a name="devops-guru-transition"></a>

Amazon DevOps Guru reaches end of support on September 30, 2027. After this date, DevOps Guru no longer analyzes your resources and previously generated insights are no longer available. Your underlying AWS infrastructure and workloads aren't affected. Only the DevOps Guru monitoring layer is removed.

This guide helps you understand what is changing and what actions you need to take. Amazon CloudWatch provides anomaly detection and alerting for your resources, and Amazon DevOps Agent provides AI-assisted investigation. Your workloads remain in place with no migration required.

**Topics**
+ [How DevOps Guru and its replacements differ](#transition-how-differ)
+ [How the transition works](#transition-how-works)
+ [How we support you through the transition](#transition-support)
+ [Who needs to act, and by when](#transition-who-acts)
+ [What changes at a glance](#transition-at-a-glance)
+ [Metric anomaly detection and alerting](#transition-metric-anomaly)
+ [Log anomaly detection](#transition-log-anomaly)
+ [Database anomaly detection](#transition-database-anomaly)
+ [Investigation and root cause analysis](#transition-investigation)
+ [Proactive insights](#transition-proactive)
+ [Infrastructure as code and CLI usage](#transition-iac)
+ [API integrations](#transition-api)
+ [Export your data](#transition-export)
+ [Delete your DevOps Guru resources](#transition-delete)
+ [Timeline and support](#transition-timeline)
+ [Transition checklist](#transition-checklist)
+ [Frequently asked questions](#transition-faq)
+ [Related resources](#transition-related)

## How DevOps Guru and its replacements differ
<a name="transition-how-differ"></a>

Amazon DevOps Guru uses a managed model: you add resources to its coverage, and it learns their normal behavior, detects anomalies, groups related anomalies into insights, and recommends actions. You don't choose which metrics to analyze or configure thresholds.

Amazon CloudWatch uses a configured model: you choose the metrics and log groups to monitor, and you create the anomaly detectors, alarms, and notification actions. This requires a one-time setup, and it gives you direct control over what is monitored, how sensitive each alarm is, and where notifications go. Amazon DevOps Agent provides the investigation and root cause analysis that DevOps Guru insights provided, started from a CloudWatch alarm or on demand.

You can use both together: CloudWatch detects and alerts, and Amazon DevOps Agent helps you investigate and find root cause.

## How the transition works
<a name="transition-how-works"></a>

We don't migrate your workloads. Your applications, databases, and infrastructure stay exactly where they are. This is a monitoring configuration change, not a workload migration.

The transition has four parts:

1. Reproduce the detection and alerting you rely on in Amazon CloudWatch.

1. Set up Amazon DevOps Agent for investigation.

1. Remove DevOps Guru from your infrastructure as code templates and API integrations.

1. Export any insights you want to keep, then set your analysis coverage to None.

You can transition one account or application at a time, and you can run DevOps Guru and CloudWatch side by side while you validate your new configuration. Because DevOps Guru doesn't host your workloads, there is no downtime during the transition. For guidance on which service to move each use case to, see [Choosing the right migration path](devops-guru-end-of-support.md#eos-choosing-path) on the end of support page.

## How we support you through the transition
<a name="transition-support"></a>

Until September 30, 2027, DevOps Guru continues to operate normally. We continue to provide security patches, critical bug fixes, and support through AWS Support channels, and we maintain service availability. No new features are added.

The [Amazon DevOps Guru end of support](devops-guru-end-of-support.md) page is the maintained reference for dates and migration steps. If you have questions during the transition, contact [AWS Support](https://console.aws.amazon.com/support). We recommend completing your transition by June 30, 2027 to allow buffer before the end of support date September 30, 2027.

## Who needs to act, and by when
<a name="transition-who-acts"></a>

The impact of this change depends on how you use DevOps Guru.


| If you | What happens at end of support | Priority | 
| --- | --- | --- | 
| Declare DevOps Guru resources in AWS CloudFormation, AWS CDK, or Terraform templates | Stack operations that reference the withdrawn resource types fail. A single failed resource can block an entire stack update. | Highest. Complete this first. | 
| Call the DevOps Guru API from dashboards, ticketing systems, or internal tools | Integrations stop returning data. | High | 
| Use the DevOps Guru console for insights and alerts, including DevOps Guru for Amazon RDS | You lose anomaly detection and recommendations for the resources in coverage. | Medium | 
| Want to keep a record of past insights | Insights are no longer available. Export them before you remove coverage. | Before you offboard | 

Complete all actions before September 30, 2027. We recommend finishing your transition by June 30, 2027 so you can validate your CloudWatch and Amazon DevOps Agent configuration while DevOps Guru is still available for comparison.

## What changes at a glance
<a name="transition-at-a-glance"></a>

The following table summarizes what's available after the transition and what's different from DevOps Guru.


| Capability | Available after transition? | What's different | 
| --- | --- | --- | 
| Metric anomaly detection | Yes, customer-configured | CloudWatch anomaly detection learns the expected range of each metric automatically. You choose which metrics to enable it on. | 
| Operational alerting | Yes, customer-configured | Use anomaly detection alarms and composite alarms, and route alarm state changes to Amazon SNS or Amazon EventBridge. You define the alarms rather than receiving them automatically. | 
| Log anomaly detection | Yes, same coverage | Enable anomaly detection directly on your CloudWatch Logs log groups and investigate with CloudWatch Logs Insights. | 
| Database anomaly detection (DevOps Guru for Amazon RDS) | Yes, same coverage | CloudWatch Database Insights shows the same database load, wait event, and top SQL data that DevOps Guru for Amazon RDS analyzed. Create a CloudWatch anomaly detection alarm on the DBLoad metric to be notified of abnormal load, then run an on-demand performance analysis in Database Insights for the alarm period to identify the cause. | 
| CloudWatch alarms you added to DevOps Guru | Yes, same coverage | Your alarms are unchanged. Use them to start an investigation in AWS DevOps Agent or CloudWatch. | 
| Grouped insights with root cause analysis | Yes, customer-initiated | Amazon DevOps Agent and CloudWatch investigations correlate metrics, logs, change events, and traces to identify root cause. Investigations start from an alarm or on demand rather than running continuously. | 
| Service dependency context | Yes, customer-configured | Enable AWS X-Ray and CloudWatch Application Signals so investigations can map service relationships. | 
| Recommendations and remediation | Yes, customer-initiated | DevOps Guru attached a recommendation to each insight. Amazon DevOps Agent generates recommendations during an investigation, and AWS Systems Manager Automation runs the remediation runbooks you define. | 
| Notifications | Yes, same coverage | Amazon SNS, Amazon EventBridge, and Systems Manager OpsCenter are the same destinations DevOps Guru used. You connect them to CloudWatch alarms. | 
| Proactive insights | Not available | DevOps Guru proactive insights end with the service. For the resources where early warning matters to you, you can create CloudWatch alarms on utilization thresholds and Service Quotas usage alarms on your account quotas. | 

## Metric anomaly detection and alerting
<a name="transition-metric-anomaly"></a>

In DevOps Guru, anomaly detection on a resource's metrics starts automatically when the resource is in coverage. In CloudWatch, you enable anomaly detection on the metrics you choose and create alarms on them.

**What you need to do**

1. Identify the metrics you relied on DevOps Guru to analyze, such as CPU utilization, request count, 4XX and 5XX error rates, latency, unhealthy host count, memory, and disk.

1. Enable CloudWatch anomaly detection on those metrics. CloudWatch learns the expected range of each metric from its history.

1. Create anomaly detection alarms. Use composite alarms to combine related alarms and reduce noise.

1. Add alarm actions that send notifications to your existing Amazon SNS topics or Amazon EventBridge rules.

**What changes**

Detection applies to the metrics you choose rather than to every resource in a coverage boundary. You control the alarm sensitivity, evaluation periods, and notification routing.

## Log anomaly detection
<a name="transition-log-anomaly"></a>

In DevOps Guru, log anomalies appear alongside the metric anomalies in an insight. In CloudWatch, you enable anomaly detection on each log group and view anomalies in the CloudWatch Logs console.

**What you need to do**

1. Enable CloudWatch Logs anomaly detection on your critical log groups.

1. Use CloudWatch Logs Insights to query and investigate the log events behind an anomaly.

1. If you declared the `AWS::DevOpsGuru::LogAnomalyDetectionIntegration` resource type, remove it from your templates. See [Infrastructure as code and CLI usage](#transition-iac).

**What changes**

Log anomalies are shown per log group in CloudWatch rather than grouped into a DevOps Guru insight. To correlate log anomalies with metric anomalies, start an Amazon DevOps Agent investigation.

## Database anomaly detection
<a name="transition-database-anomaly"></a>

In DevOps Guru for Amazon RDS, anomalies in database load for your Amazon Relational Database Service and Amazon Aurora databases were reported as insights with recommendations for the wait events involved. In CloudWatch, Database Insights provides the same Performance Insights data, and you create alarms for alerting.

**What you need to do**

1. Enable [CloudWatch Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights.html) for the databases that DevOps Guru for Amazon RDS covered.

1. Create CloudWatch alarms on the `DBLoad` metric and the wait event metrics that matter for your workload.

1. Include database alarms in your Amazon DevOps Agent investigations alongside your application alarms.

**What changes**

Database Insights provides fleet-level dashboards and top contributor analysis for database load. Anomaly detection on database load becomes an alarm that you configure rather than an insight that DevOps Guru opened for you.

## Investigation and root cause analysis
<a name="transition-investigation"></a>

In DevOps Guru, related anomalies were grouped into an insight with a recommendation. AWS DevOps Agent provides AI-assisted investigation that correlates metrics, logs, traces, and recent deployments and configuration changes to identify root cause. CloudWatch investigations provides the same type of investigation from within the CloudWatch console.

**What you need to do**

1. Set up Amazon DevOps Agent for your accounts.

1. Enable AWS X-Ray and CloudWatch Application Signals so investigations have service topology and trace context.

1. Configure CloudWatch alarms to start an investigation, or start one on demand when an issue occurs.

**What changes**

Investigations start from an alarm or on demand rather than running continuously. You receive root cause hypotheses that you can review and act on, and you can run the remediation runbooks you have defined in AWS Systems Manager Automation.

## Proactive insights
<a name="transition-proactive"></a>

In DevOps Guru, proactive insights warned you about conditions that could lead to a problem, such as a resource approaching its capacity limit or a configuration that increases risk. Proactive insights are not part of CloudWatch or Amazon DevOps Agent, and they end with the service.

For the resources where early warning matters to you, create CloudWatch alarms that notify you before a limit is reached:

1. Create alarms on utilization metrics with a threshold below the limit, for example at 80 percent of provisioned capacity, with an evaluation period long enough to ignore brief spikes.

1. Create Service Quotas usage alarms for the account-level quotas your workloads depend on, such as Lambda concurrent executions and DynamoDB account capacity. For more information, see [Creating CloudWatch alarms for Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/configure-cloudwatch.html).

**What changes**

You define the conditions that warn you, and you choose the resources they apply to. DevOps Guru selected the conditions and resources for you.

## Infrastructure as code and CLI usage
<a name="transition-iac"></a>

Templates and stacks that reference the following resource types fail to create or update after the resource types are withdrawn:
+ `AWS::DevOpsGuru::ResourceCollection`
+ `AWS::DevOpsGuru::NotificationChannel`
+ `AWS::DevOpsGuru::LogAnomalyDetectionIntegration`

The Terraform AWS provider exposes the equivalent `aws_devopsguru_resource_collection`, `aws_devopsguru_notification_channel`, `aws_devopsguru_event_sources_config`, and `aws_devopsguru_service_integration` resources.

**What you need to do**

1. Inventory the AWS CloudFormation, AWS CDK, and Terraform templates and the AWS CLI scripts that reference these resource types.

1. Create the equivalent CloudWatch configuration: the alarms, Amazon SNS topics, and Amazon EventBridge rules that replace your DevOps Guru notification channel and coverage, and the CloudWatch Logs anomaly detectors that replace the log anomaly detection integration.

1. Remove the DevOps Guru resources from your templates and deploy the change so the resources are no longer managed by your stacks. Remove them from your templates rather than deleting them out of band, so your stacks and templates stay in agreement.

**What changes**

Because a single failed resource can block an entire stack operation, this is the highest severity impact. Complete it first.

## API integrations
<a name="transition-api"></a>

If your dashboards, ticketing systems, or internal tools call the DevOps Guru API, update them to use the equivalent CloudWatch API operations before end of support. After end of support, DevOps Guru API operations are no longer available.


| If your tooling calls | Use instead | 
| --- | --- | 
| ListInsights, DescribeInsight, ListAnomaliesForInsight | CloudWatch DescribeAlarms, DescribeAlarmHistory, and GetMetricData; CloudWatch Logs ListLogAnomalyDetectors and ListAnomalies | 
| ListRecommendations | Amazon DevOps Agent investigation results | 
| DescribeAccountHealth, DescribeResourceCollectionHealth | CloudWatch DescribeAlarms filtered by alarm state, or a composite alarm for each application | 
| ListNotificationChannels, AddNotificationChannel | Amazon SNS topics and Amazon EventBridge rules for CloudWatch alarm state changes | 

For API details, see the [Amazon DevOps Guru API Reference](https://docs.aws.amazon.com/devops-guru/latest/APIReference/Welcome.html) and the [Amazon CloudWatch API Reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/Welcome.html).

## Export your data
<a name="transition-export"></a>

DevOps Guru insights are not available after September 30, 2027. If you want to keep a record of your insights, export them before that date. We recommend that most customers do both of the following:

1. **Capture new insights until end of support.** Configure an Amazon SNS notification channel so that each new insight is delivered to a topic you can archive.

1. **Export the insights you have already accumulated.** Call `ListInsights` to list them, then call `DescribeInsight`, `ListAnomaliesForInsight`, and `ListRecommendations` for each insight you want to keep. Store the responses in Amazon S3 or your ticketing system.

Complete your export before you reduce coverage or remove resources.

## Delete your DevOps Guru resources
<a name="transition-delete"></a>

To stop analysis and stop incurring charges before end of support, remove your coverage and notification channels after you have exported your data and set up your CloudWatch configuration.

1. Set your analysis coverage to **None** for each account and AWS Region where DevOps Guru is enabled. In the console, choose **Settings**, then **DevOps Guru analysis coverage**, then **Manage**, then **None**. You can also call `UpdateResourceCollection` to remove the CloudFormation stacks or tags that define your coverage boundary.

1. Remove your notification channels. Call `RemoveNotificationChannel`, or delete them from **Settings** in the console. Removing a channel does not delete the Amazon SNS topic or anything you have already archived through it.

1. If you declare DevOps Guru resources in infrastructure as code, remove them from your templates rather than deleting them out of band. See [Infrastructure as code and CLI usage](#transition-iac).

## Timeline and support
<a name="transition-timeline"></a>


| Milestone | Date | 
| --- | --- | 
| Announcement | September 29, 2026 | 
| No new customers | October 29, 2026 | 
| Recommended transition completion | June 30, 2027 | 
| End of support | September 30, 2027 | 

We recommend completing your transition by June 30, 2027 so you can validate your CloudWatch and Amazon DevOps Agent configuration against live operations while DevOps Guru is still available for comparison. If you have questions during the transition, contact [AWS Support](https://console.aws.amazon.com/support).

## Transition checklist
<a name="transition-checklist"></a>
+ Inventory AWS CloudFormation, AWS CDK, Terraform, and AWS CLI usage of `AWS::DevOpsGuru::ResourceCollection`, `AWS::DevOpsGuru::NotificationChannel`, and `AWS::DevOpsGuru::LogAnomalyDetectionIntegration`.
+ Identify every API integration that reads DevOps Guru insights.
+ Enable CloudWatch anomaly detection on your key metrics and create alarms.
+ Enable CloudWatch Logs anomaly detection on your critical log groups.
+ Enable CloudWatch Database Insights for the databases that DevOps Guru for Amazon RDS covered.
+ Enable AWS X-Ray and CloudWatch Application Signals.
+ Set up Amazon DevOps Agent for investigation.
+ Configure notifications with Amazon SNS, Amazon EventBridge, or Systems Manager OpsCenter.
+ Export DevOps Guru insights through an Amazon SNS notification channel and the API.
+ Remove DevOps Guru resources from your templates and set analysis coverage to None.

## Frequently asked questions
<a name="transition-faq"></a>

**Will my applications or databases stop working after end of support?**  
No. DevOps Guru is a monitoring service. It observes resources you run, it does not host them. After end of support you lose DevOps Guru's visibility and recommendations, but your workloads continue to run.

**What happens if I do not migrate in time?**  
You will no longer be able to access the DevOps Guru console or API, and DevOps Guru resource types will fail in AWS CloudFormation and the AWS CLI. Insights will no longer be available.

**Can I keep using DevOps Guru until end of support?**  
Yes, if your account signed up before October 29, 2026. Until end of support, we provide security patches, critical bug fixes, support, and maintained availability. No new features are added.

**Is there a single service that replaces DevOps Guru one-to-one?**  
No. DevOps Guru's detection and alerting maps to Amazon CloudWatch, and its investigation and root cause analysis maps to Amazon DevOps Agent. You can use both together.

**What happens to DevOps Guru for Amazon RDS?**  
It ends with the rest of the service. CloudWatch Database Insights provides the same Performance Insights data. Create alarms on database load for alerting.

## Related resources
<a name="transition-related"></a>
+ [Amazon DevOps Guru end of support](devops-guru-end-of-support.md)
+ [Services in Sunset](https://docs.aws.amazon.com/general/latest/gr/sunset_services.html) in the *AWS General Reference*
+ [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+ [Using CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)
+ [CloudWatch Logs anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection.html)
+ [CloudWatch Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights.html)
+ [CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html)
+ [Amazon DevOps Agent User Guide](https://docs.aws.amazon.com/devopsagent/)
+ [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/)
+ [AWS Support](https://console.aws.amazon.com/support)