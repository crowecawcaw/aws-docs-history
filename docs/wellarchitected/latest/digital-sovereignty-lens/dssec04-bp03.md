

# DSSEC04-BP03 Establish comprehensive logging and monitoring of operator actions
<a name="dssec04-bp03"></a>

 Enable detailed logging to track operator actions, detect unauthorized access, and retain evidence required for audits. Detailed audit trails provide visibility into change management activities and operator-led actions. This is particularly important for workloads with sovereignty requirements, where you may need to locate operational support teams within specific jurisdictions, strictly control operator actions, and produce documentary evidence of technical and operational controls. 

 **Desired outcome:** 
+  Organizations maintain visibility into operator actions and system changes with detailed audit trails for compliance and security investigations. 
+  Immutable, tamper-evident logs of system changes are preserved and stored within approved jurisdictions for audit and troubleshooting purposes. 

 **Common anti-patterns:** 
+  Failing to detect or alert on unauthorized operator actions. 
+  Not enabling logging consistently across AWS services, Regions, and accounts, resulting in visibility gaps. 
+  Storing sensitive log data without proper encryption, access controls, or immutable storage mechanisms. 
+  Implementing inconsistent logging formats, standards, or retention periods across services and environments. 

 **Benefits of establishing this best practice**: 
+  Visibility into operator activities with early detection of unauthorized or suspicious activities. 
+  Tracks data access patterns, supports data protection initiatives, and enables verification of compliance with data localization mandates, and data residency requirements. 
+  Automated log collection and demonstrable evidence of effective security controls to auditors and stakeholders. 
+  Detailed audit trails and forensic evidence enable faster investigation and event reconstruction. Detailed session logs and activity tracking improve troubleshooting capabilities. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Begin by understanding the support activities performed, and the network routes used by your operational support teams. Mature operational support teams will have a catalog of runbooks they execute for common activities such as taking backups, applying patches, or rotating credentials. 

 For each runbook, identify the systems accessed, the level of privilege required, the network path taken, and the geographic location from which the activity originates. Then document the following: 
+  Specific logging requirements based on your industry and jurisdictional regulations. 
+  Retention periods for different types of logs. 
+  Data localization or data residency constraints for log storage. 
+  The information required to be recorded in each individual log entry for each type of log output. 
+  Critical systems and data that require enhanced logging. 

 [SEC04-BP01 Configure service and application logging](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_app_service_logging.html), and [SEC04-BP02 Capture logs, findings, and metrics in standardized locations](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_logs.html) provide a solid foundation to build on. Review additional capabilities that may be required to fulfill digital sovereignty requirements. Key implementation considerations include: 
+  **Access monitoring:** Monitoring and logging of operator actions performed. 
+  **Log storage:** Log aggregation and log storage including retention periods, costs, and formats identified in your requirements. 
+  **Log sharing:** Sharing operator access logs securely with external organizations such as named auditors, investigative agencies, or other bodies appointed by regulators. 
+  **Alerting:** Detecting, logging, and alerting on deviations from baselines. 

 Verify logs are stored within approved jurisdictions and comply with data residency requirements. Implement encryption using cryptographic keys managed within sovereign boundaries. Maintain audit trails that demonstrate adherence to local data protection and privacy laws. Configure cross-border log transfer as required by regulatory frameworks. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable AWS CloudTrail across Regions and accounts:** Record operator actions by enabling organization-wide logging. 
   +  Enable organization-wide [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) trails that capture [read and write](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-examples.html) management operations that are performed on resources across your AWS accounts. If you have created an organization in AWS Organizations, you can create an organizational trail that [logs all events for all AWS accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) in that organization. Management operations are also referred to as control plane operations. 
   +  By default, trails and event data stores don't log data events. To record data plane operations you can enable [CloudTrail data event logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) for Amazon S3 object-level API activity (for example, GetObject, DeleteObject, and PutObject API operations), Amazon Bedrock (for example API activity on models), and Amazon SNS. See [list of data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events) supported by AWS CloudTrail. These logs assist in the detection of unauthorized operator access to sensitive data. Also see [Logging data events for AWS Config compliance](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#config-data-events-best-practices) which lists logging best practices and how they relate to compliance frameworks. Data events are high volume. To control costs you can filter trails using [advanced event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/filtering-data-events.html). 

    An organization trail is a multi-Region trail and will log events from all AWS Regions enabled in your account, with all log files delivered to a single S3 bucket in your home Region. Make sure that the destination Region is acceptable under your data residency policy. 

1.  **Protect logs**: Protect the integrity and confidentiality of your log data to maintain a trustworthy chain of evidence for auditors and regulators. 
   +  To determine whether a log file was modified, deleted, or unchanged after CloudTrail delivered it, you can use CloudTrail log file integrity validation. See this guide, [Validating CloudTrail log file integrity](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html). 
   +  Implement [encryption for log files](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/encrypting-cloudtrail-log-files-with-aws-kms.html). 
   +  Apply [immutable log storage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) using S3 Object Lock on the S3 bucket that stores your log files. 
   +  Refer to the [Security best practices for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) for additional protective measures. 

1.  **Establish operator identity**: When operators assume a role through the [AWS Security Token Service (AWS STS)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html), to perform actions on resources, CloudTrail logs the IAM role that made the call and not the identity of the user who may have assumed that role. This can make it challenging for administrators to trace which identity was responsible for actions performed. To address this, with AWS STS you can set a unique attribute called [SourceIdentity](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html), which helps you see which identity is responsible for a given action. Refer to this blog post [How to integrate AWS STS SourceIdentity with your identity provider](https://aws.amazon.com/blogs/security/how-to-integrate-aws-sts-sourceidentity-with-your-identity-provider/) to see how this works in practice. 

    After you configure your IDP, and add the sts:SetSourceIdentity permission to your IAM role's trust policy, CloudTrail will start logging the sourceIdentity when an operator makes an API call using that IAM role. For example, for a CreateBucket event, CloudTrail will log the source identity as shown here (and as illustrated in the blog post). 
**Note**  
 The code snippets shown here are for illustration only and may not be accurate. Validate against your own environment and requirements unique to your workload. 

   ```
   {
   "eventVersion": "1.08",
   "userIdentity": {
       "type": "AssumedRole",
       "principalId": "AAAAAAAAAAAAAAAAAAAAA:sourceidentitytest",
       "arn": "arn:aws:sts::111122223333:assumed-role/idsol-org-admin/sourceidentitytest",
       "accountId": "111122223333",
       "accessKeyId": "XXXXXXXXXXXXXXX",
       "sessionContext": {
       "sessionIssuer": {
           "type": "Role",
           "principalId": "AAAAAAAAAAAAAAAAAAAAA",
           "arn": "arn:aws:iam::111122223333:role/idsol-org-admin",
           "accountId": "111122223333",
           "userName": "idsol-org-admin"
       },
       "webIdFederationData": {},
       "attributes": {
           "mfaAuthenticated": "false",
           "creationDate": "2021-05-05T16:29:19Z"
       },
       "sourceIdentity": "<sourceidentitytest@example.com>"
       }
   },
   "eventTime": "2021-05-05T16:33:25Z",
   "eventSource": "s3.amazonaws.com",
   "eventName": "CreateBucket",
   "awsRegion": "us-east-1",
   "sourceIPAddress": "203.0.113.0"
   }
   ```

1.  **Implement session logging:** One-time operator access through terminal emulators should not be the norm. However, such sessions may need to be temporarily allowed for troubleshooting or during incidents. We recommend using AWS Systems Manager [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) as it provides secure node management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys. Session Manager provides you with the ability to log session activity in your AWS account using AWS CloudTrail. See options available under [enabling and disabling session logging](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-logging.html). 

1.  **Configure monitoring and alerting:** 
   +  Configure [Amazon CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html) to monitor your trail logs. Detect and send notifications for unauthorized access or suspicious activities against security and compliance data. 
   +  Implement [metric filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) for important events. Set up [CloudWatch alarms](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html) for suspicious activities. Create automated notifications using [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html). 
   +  Configure [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) rules for automated responses to events (such as IAM policy changes, encryption key deletion, or root account usage). 
   +  Implement real-time log analysis with [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) and configure [dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) for log monitoring. 
   +  Consider using Amazon GuardDuty to detect anomalous behavior. For example, the GuardDuty finding type [Discovery:S3/AnomalousBehavior](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#discovery-s3-anomalousbehavior) uses CloudTrail data events for S3, and built-in ML models to detect potential [anomalous behavior](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-summary.html#finding-anomalous). 

1.  **Verify logging completeness and compliance:** 
   +  Regularly audit logging configurations against requirements. Perform periodic testing to verify logs capture critical activities (such as IAM policy changes, S3 bucket deletions, or security group modifications). 
   +  Conduct simulated security incidents to test the effectiveness of your logging configurations. Consider using [AWS Well-Architected Labs - Security](https://wellarchitectedlabs.com/security/) for hands-on practice. 

1.  **Validate third-party controls:** Organizations often use third-party services that generate, process, or consume security and compliance data (such as APM SaaS providers, SIEM systems, or compliance management solutions). To verify that these services meet the same operator access logging standards: 
   +  Request relevant accreditations or certifications specific to the services they provide (such as SOC 2, ISO 27001, or Region-specific certifications). 
   +  Verify the data residency of the service and confirm it meets your sovereignty requirements. 
   +  Perform independent security assessments of third-party integrations. 
   +  Use [AWS PrivateLink](https://aws.amazon.com/privatelink/) for third-party connectivity to block data exfiltration through the public internet. Don't share raw CloudTrail logs with third parties; use aggregated or anonymized data where possible. 

1.  **Implement continuous improvement:** 
   +  Regularly review and update your logging strategy based on regulatory changes and emerging threats. 
   +  Assess new AWS services for logging requirements as you adopt them. 
   +  Incorporate feedback from security teams, auditors, and incident response exercises. 
   +  Conduct regular training on log analysis techniques using resources like [AWS Skill Builder](https://skillbuilder.aws/) and [AWS Security workshops](https://workshops.aws/categories/Security). 

## Resources
<a name="resources"></a>

 **Related best practices**: 
+  [SEC04-BP01 Configure service and application logging](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_app_service_logging.html) 
+  [SEC04-BP02 Capture logs, findings, and metrics in standardized locations](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_logs.html) 
+  [SEC04-BP03 Correlate and enrich security alerts](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_security_alerts.html) 
+  [SEC04-BP04 Initiate remediation for non-compliant resources](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_noncompliant_resources.html) 
+  [SEC08-BP01 Implement secure key management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_key_mgmt.html) 
+  [SEC08-BP02 Enforce encryption at rest](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_encrypt.html) 
+  [SEC08-BP03 Automate data at rest protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_automate_protection.html) 
+  [SEC03-BP01 Define access requirements](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_define.html) 
+  [SEC03-BP02 Grant least privilege access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privileges.html) 
+  [SEC03-BP03 Establish emergency access process](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_emergency_process.html) 
+  [OPS08-BP02 Analyze workload logs](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_analyze_workload_logs.html) 
+  [OPS08-BP04 Create actionable alerts](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_create_alerts.html) 

 **Related documents**: 
+  [Centralized logging and monitoring](https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/logging-monitoring.html) 
+  [Build your own centralized log analytics platform with Amazon OpenSearch Service](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/solution-overview.html) 
+  [The AWS Security Reference Architecture - Log Archive account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html) 

 **Related videos**: 
+  [AWS re:Invent 2022 - Cloud compliance, assurance, and auditing (COP304)](https://www.youtube.com/watch?v=xREhfrUqpd4) 
+  [AWS re:Inforce 2025 - Operationalizing Amazon Security Lake with analytics and generative AI (TDR342)](https://www.youtube.com/watch?v=cRs9kyWQqWE) 

 **Related examples**: 
+  [AWS Well-Architected Labs - Security](https://wellarchitectedlabs.com/security/) 
+  [AWS CloudTrail samples](https://github.com/aws-samples/aws-cloudtrail-lake-query-samples) 
+  [Amazon Security Lake samples](https://github.com/aws-samples/amazon-security-lake) 

 **Related services**: 
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) 
+  [Amazon SNS](https://aws.amazon.com/sns/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 
+  [Amazon Security Lake](https://aws.amazon.com/security-lake/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [Amazon Athena](https://aws.amazon.com/athena/) 