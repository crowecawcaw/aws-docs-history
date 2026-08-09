# Incident response, logging, and monitoring in Amazon Quick

|                                                                             |
| --------------------------------------------------------------------------- |
| Intended audience:<br>System administrators and Amazon Quick administrators |

Amazon Quick provides multiple monitoring and audit signals that address different
aspects of security, operations, and compliance. Each signal has distinct coverage,
latency, retention, and access-control characteristics.

- **CloudTrail** – Records supported
  Amazon Quick and Amazon Quick Sight API operations and a documented set of non-API
  events, such as dashboard views and user-management actions. For chat
  conversations and feedback, use CloudWatch vended logs.
- **CloudWatch vended logs** – Deliver chat
  conversations, user feedback, agent and research hours usage, index storage
  usage, and knowledge base file sync results to destinations that you
  control. Configure vended log delivery shortly after enabling
  Amazon Quick.
- **CloudWatch metrics** – Provide
  near-real-time operational metrics and support CloudWatch alarms.
- **Amazon Quick analytics** – Provide
  usage, adoption, feedback, and selected security-related insights to IAM
  administrators.
- **Feature-specific reports** –
  Provide operational detail for the feature that produces them, such as
  knowledge base sync reports.
  Use these sources together when you design monitoring and incident-response
  procedures. Before you rely on a signal for compliance, detection, or
  investigation, confirm that it covers the event you intend to track.

The following table helps you choose the right signal for your monitoring
need.

| To answer                                                                               | Use                                                          | More information                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Who performed an administrative or API action, from where, and<br>when                  | CloudTrail                                                   | [Incident response, logging, and monitoring in Amazon Quick Sight using CloudTrail](incident-response-logging-and-monitoring-qs.md "incident-response-logging-and-monitoring-qs.md")                                                                                                                                             |
| Who viewed a dashboard, or which non-API events<br>occurred                             | CloudTrail non-API events                                    | [Tracking non-API events by using CloudTrail logs](incident-response-logging-and-monitoring-qs.md#logging-non-api "incident-response-logging-and-monitoring-qs.md#logging-non-api")                                                                                                                                              |
| What users asked and what Quick answered                                                | CloudWatch vended logs (`CHAT_LOGS`)                         | [Monitoring Amazon Quick usage using CloudWatch Logs](monitoring-quicksuite-chat-feedback-cloudwatch.md "monitoring-quicksuite-chat-feedback-cloudwatch.md")                                                                                                                                                                     |
| How users rated responses and why                                                       | Vended logs (`FEEDBACK_LOGS`) or<br>analytics                | [Monitoring Amazon Quick usage using CloudWatch Logs](monitoring-quicksuite-chat-feedback-cloudwatch.md "monitoring-quicksuite-chat-feedback-cloudwatch.md");<br>[Using the Amazon Quick analytics dashboard](incident-response-logging-and-monitoring-quick-suite.md "incident-response-logging-and-monitoring-quick-suite.md") |
| Whether a document synced into a knowledge base, and why it<br>failed or was skipped    | Vended logs (`KB_FILE_SYNC_LOGS`) or console sync<br>reports | [Monitoring Amazon Quick usage using CloudWatch Logs](monitoring-quicksuite-chat-feedback-cloudwatch.md "monitoring-quicksuite-chat-feedback-cloudwatch.md");<br>[Sync reports and observability](sync-reports-observability.md "sync-reports-observability.md")                                                                 |
| Whether a specific user can access a specific synced<br>document                        | Sync report ACL verification                                 | [Sync reports and observability](sync-reports-observability.md "sync-reports-observability.md")                                                                                                                                                                                                                                  |
| Index storage per knowledge base or Space                                               | Vended logs (`INDEX_USAGE_LOGS`) or CloudWatch<br>metrics    | [Monitoring Amazon Quick usage using CloudWatch Logs](monitoring-quicksuite-chat-feedback-cloudwatch.md "monitoring-quicksuite-chat-feedback-cloudwatch.md");<br>[Monitoring data in Amazon Quick Sight using CloudWatch](monitoring-quicksight.md "monitoring-quicksight.md")                                                   |
| Operational health: load times, ingestion failures, connector<br>errors, SPICE capacity | CloudWatch metrics and alarms                                | [Monitoring data in Amazon Quick Sight using CloudWatch](monitoring-quicksight.md "monitoring-quicksight.md")                                                                                                                                                                                                                    |
| Adoption, engagement, feedback trends, agent-hours<br>consumption                       | Analytics dashboard                                          | [Using the Amazon Quick analytics dashboard](incident-response-logging-and-monitoring-quick-suite.md "incident-response-logging-and-monitoring-quick-suite.md")                                                                                                                                                                  |

Use the following checklist to configure monitoring for your environment:

1. Create a CloudTrail trail for the AWS accounts and AWS Regions that require
   audit logging.
2. Configure CloudWatch vended log delivery shortly after enabling Amazon Quick
   AI features.
3. When vended-log destinations use a customer managed AWS KMS key, allow
   `delivery.logs.amazonaws.com` in the key policy.
4. Chat logs can contain sensitive or personally identifiable data. Filter
   this information at subscription setup, or apply CloudWatch Logs
   data-protection masking policies.
5. Configure CloudWatch alarms on operational metrics and map them to your
   incident-response procedures.
6. Grant `quicksight:QuickSuiteUsageMetrics` (analytics access)
   only to authorized administrators.
7. Revalidate your monitoring design when you enable a new Amazon Quick
   capability.

###### Topics

- [Monitoring Amazon Quick usage using CloudWatch Logs](monitoring-quicksuite-chat-feedback-cloudwatch.md "monitoring-quicksuite-chat-feedback-cloudwatch.md")
- [Incident response, logging, and monitoring in Amazon Quick Sight using CloudTrail](incident-response-logging-and-monitoring-qs.md "incident-response-logging-and-monitoring-qs.md")
- [Monitoring data in Amazon Quick Sight using CloudWatch](monitoring-quicksight.md "monitoring-quicksight.md")
