

# FND05-BP03 Configure audit logging of cloud operations

 Enable audit logging across your cloud environment and verify it produces a complete, accurate record of actions taken. Use these logs to investigate incidents, alert on specific operations or behavioral anomalies, and reconstruct the timeline and scope of an incident. 

 **Desired outcome:** 
+  You have established full audit logging across your entire cloud environment to improve visibility into actions taken by users, roles, and services. 
+  Your logs capture enough detail to support rapid incident response, so you can identify the timeline of actions, scope of an incident, and the path to recovery. 
+  Your organization uses these logs to meet compliance requirements, enforce organization policies, and detect violations of those policies. 
+  You have defined a centralized location for storing and querying logs across all accounts and Regions in your organization. 
+  Your logs are protected from tampering or unauthorized modification through encryption, access controls, and immutability features. 

 **Common anti-patterns:** 
+  Failing to enable logging for all relevant cloud services and environments, leading to blind spots in visibility and inability to detect incidents. 
+  Keeping logs for insufficient time, limiting historical analysis of events and preventing retrospective security investigations. 
+  Granting overly broad access to logs, potentially exposing sensitive information. 
+  Failing to protect logs from tampering or unauthorized modification or deletion. 
+  Storing logs only in the same account or Region where the resources exist, creating a single point of failure. 
+  Enabling logging without establishing processes to analyze, alert on, or respond to the events captured. 

 **Benefits of establishing this best practice:** 
+  Full audit logging supports rapid incident response by giving visibility into the timeline, scope, and effect of security events. 
+  Anomalous behavior and potential security threats are detected faster through log analysis and alerting. 
+  Compliance posture is strengthened through detailed, auditable records that support regulatory requirements and internal policies. 
+  Centralized logging improves operational efficiency by providing a single source of truth for investigating issues. 
+  Protected, tamper-proof logs improve forensic integrity and support security investigations and legal proceedings. 
+  Long-term retention supports historical analysis, trend identification, and retrospective security assessments. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Audit logging creates a permanent record of which identities took an action, when they did it, and the location of the action across your cloud environment. The absence of logging limits your ability to detect threats, investigate incidents, or answer auditor questions. 

 The architecture for audit logging must balance completeness, protection, cost, and queryability. Completeness means capturing all relevant events across all accounts and services. Protection means making sure that logs cannot be tampered with or deleted by an unauthorized user who gains access to your environment. Cost management means being selective about what you log and where you store it, particularly for high-volume data like network flow logs. Queryability means organizing logs so you can search them efficiently during an investigation. 

 Centralize audit logs by collecting them from all accounts into a dedicated log archive account with restricted access. This separation prevents an unauthorized user with broad access to a workload account from removing evidence of their activity. Enable multiple types of logging for overlapping visibility: [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) tracks API calls, [AWS Config](https://aws.amazon.com/config/) captures resource configuration state and tracks changes over time, network logs ([VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) and [Amazon Route 53 Resolver query logs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs.html)) capture communication patterns between resources, and compute and workload logs from [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html), [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html), [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html), and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html) capture what happens inside the workloads themselves. 

 Deliver CloudTrail log files from every AWS account into a single [Amazon S3](https://aws.amazon.com/s3/) bucket in the Log Archive account for centralized storage and long-term retention. Query these logs directly from S3 with [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html), or centralize them alongside other operational, security, and compliance telemetry in [Amazon CloudWatch Unified Data Store](https://aws.amazon.com/cloudwatch/features/unified-data-and-telemetry/) with [cross-account cross-Region log centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html) for OCSF-aware analytics across logs, metrics, and traces. For real-time investigation and alerting, stream CloudTrail to [Amazon CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html) so you can run [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) queries and set [metric filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) that trigger alarms. 

 Encrypt logs in transit and at rest. Restrict access so only security and compliance teams can query the log archive account. Where possible, use [Amazon S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) to prevent even authorized users from deleting or modifying historical logs during the retention period. Validate regularly that logging remains active, so failures do not leave gaps in the audit trail. 

 Retention depends on compliance requirements and operational needs. Many frameworks require 90 days to one year of accessible logs, with longer periods in cold storage for legal or forensic purposes. Some organizations retain API logs for seven years or more. Because network flow logs are high volume, retain them for shorter periods or sample them to manage cost while keeping enough visibility for most investigations. 

**Important**  
 Full logging alone is not enough. Assign humans or automated systems to analyze and act on the events captured. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Design your logging architecture:** Consider using [AWS SRA Logging Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html) guidance to design and deploy your logging account and services. Plan a multi-account architecture where logs from all member accounts are delivered to a dedicated log archive account with restricted access. 

1.  **Set up CloudTrail logs:** Configure [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) to capture API activity across your AWS environment. The default [CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) retains 90 days of management events with no action required. For longer retention and data events, create a [CloudTrail trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) associated with an S3 bucket in the Log Archive account. If you use [AWS Organizations](https://aws.amazon.com/organizations/), create an [organization trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) that logs events for every account, and enable [CloudTrail Insights](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html) on the trail to surface unusual API call patterns. Query the stored logs with [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html) for one-time investigation, and stream the trail to [Amazon CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html) for real-time alerting through [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) and [metric filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html). 

1.  **Enable VPC Flow Logs and DNS query logging:** Configure [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) to capture network traffic information and [Amazon Route 53 Resolver query logs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs.html) to record DNS queries. Stream these logs to either an [Amazon S3](https://aws.amazon.com/s3/) bucket or an [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) log group. Be selective about where you enable flow logs to balance visibility needs with cost. 

1.  **Capture compute and workload logs:** Configure logging for the compute services that run your workloads alongside service-level logs, so the audit trail reaches into the workloads themselves. Send [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html) operating-system and application logs through the [CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html), ship [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html) and [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html) container and control-plane logs to CloudWatch Logs, and rely on [AWS Lambda's built-in CloudWatch Logs integration](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html) for function logs. Apply the same retention and access standards to these logs as to service-level audit logs so investigators can correlate API activity with what happened inside the workload. 

1.  **Centralize logs for unified analytics:** Bring CloudTrail events, VPC Flow Logs, Route 53 Resolver query logs, and application logs into a single, analytics-ready location. Use [Amazon CloudWatch Unified Data Store](https://aws.amazon.com/cloudwatch/features/unified-data-and-telemetry/) as the destination for operational, security, and compliance telemetry, and [cross-account cross-Region log centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html) to copy log data from your organization into a central account and Region. CloudWatch Unified Data Store supports [Open Cybersecurity Schema Framework (OCSF)](https://github.com/ocsf) and OpenTelemetry formats, so you can query the same data from [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html), [Amazon Athena](https://aws.amazon.com/athena/), [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/), and third-party Iceberg-compatible tools without duplicating data. 

1.  **Enable AWS Config across accounts and Regions:** Enable [AWS Config](https://aws.amazon.com/config/) in each Region where you have resources deployed (for configuration details, see [Setting Up AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html)). Centralize AWS Config across accounts by [setting up an aggregator](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html). If using [AWS Control Tower](https://aws.amazon.com/controltower/), enable the AWS Config integration. In recent AWS Control Tower deployments, AWS Config is an optional service integration that must be explicitly enabled. For details, see [Govern Resource Configurations with AWS Config](https://docs.aws.amazon.com/controltower/latest/userguide/config.html). 

1.  **Implement log protection and access controls:** Enable [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) on log buckets to prevent deletion during the retention period. Use [S3 bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html) and [IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) to restrict access to the log archive account. Enable [S3 server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html) with [AWS KMS customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) for key management control. 

1.  **Monitor logging health:** Create [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) or [AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) that alert when logging is stopped, modified, or deleted. Use [AWS Config managed rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) such as cloudtrail-enabled and vpc-flow-logs-enabled to verify logging is active. 

1.  **Define log lifecycle and retention policies:** Configure [S3 lifecycle policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to automatically transition older logs to lower-cost storage tiers (such as S3 Glacier Deep Archive) and delete logs that exceed your retention period. Document the retention policy with business and compliance justifications. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND05-BP04 Configure standardized locations for logs, traces, and metrics](fnd05-bp04.md) 
+  [FND05-BP11 Establish encryption and key management standards](fnd05-bp11.md) 
+  [OPS02-BP04 Regularly analyze workload logs](ops02-bp04.md) 

 **Related documents:** 
+  [Logging strategies for security incident response](https://aws.amazon.com/blogs/security/logging-strategies-for-security-incident-response/) 
+  [AWS Security Incident Response Technical Guide](https://docs.aws.amazon.com/security-ir/latest/userguide/) 
+  [AWS SRA Logging Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html) 
+  [Querying AWS CloudTrail logs with Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html) 
+  [Monitoring CloudTrail log files with Amazon CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html) 
+  [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html) 
+  [Amazon CloudWatch Unified Data Store](https://aws.amazon.com/cloudwatch/features/unified-data-and-telemetry/) 
+  [Cross-account cross-Region log centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html) 
+  [Govern Resource Configurations with AWS Config](https://docs.aws.amazon.com/controltower/latest/userguide/config.html) 