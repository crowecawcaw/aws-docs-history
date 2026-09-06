

# Incident response, logging, and monitoring in Amazon Quick
<a name="incident-response-logging-and-monitoring"></a>


|  | 
| --- |
|    Intended audience:  System administrators and Amazon Quick administrators  | 

Amazon Quick provides multiple monitoring and audit signals that address different aspects of security, operations, and compliance. Each signal has distinct coverage, latency, retention, and access-control characteristics.
+ **CloudTrail** – Records supported Amazon Quick and Amazon Quick Sight API operations and a documented set of non-API events, such as dashboard views and user-management actions. For chat conversations and feedback, use CloudWatch vended logs.
+ **CloudWatch vended logs** – Deliver chat conversations, user feedback, agent hours usage, index storage usage, and knowledge base file sync results to destinations that you control. Configure vended log delivery shortly after enabling Amazon Quick.
+ **CloudWatch metrics** – Provide near-real-time operational metrics and support CloudWatch alarms.
+ **Amazon Quick analytics** – Provide usage, adoption, feedback, and selected security-related insights to IAM administrators.
+ **Feature-specific reports** – Provide operational detail for the feature that produces them, such as knowledge base sync reports.
+ **Amazon EventBridge** – CloudTrail events route to Amazon EventBridge on a best-effort basis. You can create rules that match Amazon Quick events and route them to targets such as Lambda functions, Amazon SNS topics, or Amazon SQS queues for automated response.

Use these sources together when you design monitoring and incident-response procedures. Before you rely on a signal for compliance, detection, or investigation, confirm that it covers the event you intend to track.

The following table helps you choose the right signal for your monitoring need.


| To answer | Use | More information | 
| --- | --- | --- | 
| Who performed an administrative or API action, from where, and when | CloudTrail | [Monitoring Amazon Quick using CloudTrail](monitoring-cloudtrail.md) | 
| Who viewed a dashboard, or which non-API events occurred | CloudTrail non-API events | [Tracking non-API events by using CloudTrail logs](monitoring-cloudtrail.md#logging-non-api) | 
| Which API calls occurred for AI features (flows, agents, automations, connectors) | CloudTrail (management and data events) | [Monitoring Amazon Quick using CloudTrail](monitoring-cloudtrail.md); [Logging Amazon Quick data events in CloudTrail](monitoring-cloudtrail.md#logging-data-events) | 
| What users asked and what Quick answered | CloudWatch vended logs (CHAT\_LOGS) | [Monitoring Amazon Quick using CloudWatch Logs](monitoring-cloudwatch-logs.md) | 
| How users rated responses and why | Vended logs (FEEDBACK\_LOGS) or analytics | [Monitoring Amazon Quick using CloudWatch Logs](monitoring-cloudwatch-logs.md); [Using the Amazon Quick analytics dashboard](incident-response-logging-and-monitoring-quick-suite.md) | 
| Whether a document synced into a knowledge base, and why it failed or was skipped | Vended logs (KB\_FILE\_SYNC\_LOGS) or console sync reports | [Monitoring Amazon Quick using CloudWatch Logs](monitoring-cloudwatch-logs.md); [Sync reports and observability](sync-reports-observability.md) | 
| Whether a specific user can access a specific synced document | Sync report ACL verification | [Sync reports and observability](sync-reports-observability.md) | 
| Index storage per knowledge base or Space | Vended logs (INDEX\_USAGE\_LOGS) or CloudWatch metrics | [Monitoring Amazon Quick using CloudWatch Logs](monitoring-cloudwatch-logs.md); [Monitoring Amazon Quick using CloudWatch metrics](monitoring-cloudwatch-metrics.md) | 
| Operational health: load times, ingestion failures, connector errors, SPICE capacity | CloudWatch metrics and alarms | [Monitoring Amazon Quick using CloudWatch metrics](monitoring-cloudwatch-metrics.md) | 
| Adoption, engagement, feedback trends, agent-hours consumption | Analytics dashboard | [Using the Amazon Quick analytics dashboard](incident-response-logging-and-monitoring-quick-suite.md) | 

Use the following checklist to configure monitoring for your environment:

1. Create a CloudTrail trail for the AWS accounts and AWS Regions that require audit logging.

1. Configure CloudWatch vended log delivery shortly after enabling Amazon Quick AI features.

1. When vended-log destinations use a customer managed AWS KMS key, allow `delivery.logs.amazonaws.com` in the key policy.

1. Chat logs can contain sensitive or personally identifiable data. Filter this information at subscription setup, or apply CloudWatch Logs data-protection masking policies.

1. Configure CloudWatch alarms on operational metrics and map them to your incident-response procedures.

1. Grant `quicksight:QuickSuiteUsageMetrics` (analytics access) only to authorized administrators.

1. Revalidate your monitoring design when you enable a new Amazon Quick capability.

**Topics**
+ [Monitoring Amazon Quick using CloudWatch Logs](monitoring-cloudwatch-logs.md)
+ [Monitoring Amazon Quick using CloudTrail](monitoring-cloudtrail.md)
+ [Monitoring Amazon Quick using CloudWatch metrics](monitoring-cloudwatch-metrics.md)