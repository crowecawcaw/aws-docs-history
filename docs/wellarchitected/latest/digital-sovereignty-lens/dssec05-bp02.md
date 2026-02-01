# DSSEC05-BP02 Record operator sessions and retain logs

Implement session recording and log retention to maintain
accountability, support security investigations, and meet regulatory
requirements. This practice provides visibility into infrastructure
changes and audit trails for operational activities.

**Desired outcome:** Organizations
maintain visibility into operator actions and system changes with
detailed audit trails for compliance and security investigations.
Events can be reconstructed during incident response with
demonstrable evidence of security controls effectiveness. A
historical record of infrastructure modifications is preserved for
audit and troubleshooting purposes.

**Common anti-patterns:**

- Failing to enable logging across regions and accounts resulting
  in visibility gaps. Retaining inconsistent configurations across
  environments.
- Storing sensitive log data without proper encryption, access
  controls, or immutable storage mechanisms.
- Implementing inadequate log retention periods and failing to
  establish automated alerting for critical security events.
- Lacking proper access controls for log storage and failing to
  implement centralized log aggregation strategies.
- Inadequate monitoring of operator sessions, missing suspicious
  or unauthorized activities.

**Benefits of establishing this best
practice**:

- Visibility into operator activities with early detection of
  unauthorized or suspicious activities.
- Detailed audit trails and forensic evidence enable faster
  investigation and event reconstruction.
- Automated log collection and demonstrable evidence of security
  controls effectiveness for auditors and stakeholders.
- Detailed session logs and activity tracking improve
  troubleshooting capabilities.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Establish a logging strategy that addresses operational visibility
and compliance requirements. Consider log retention periods,
encryption requirements, and access controls to protect sensitive
operational data. When implementing logging for digital
sovereignty, verify logs are stored within approved jurisdictions
and comply with data residency requirements, implement encryption
using cryptographic keys managed within sovereign boundaries,
maintain audit trails that demonstrate adherence to local data
protection and privacy laws, and configure cross-border log
transfer restrictions where required by regulatory frameworks.

### Implementation steps

1. **Enable AWS CloudTrail across regions
   and accounts:**
   - Configure
     [multi-Region
     logging](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
   - Enable
     [log
     file validation](../../../awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.md "../../../awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.md")
   - Implement
     [encryption
     for log files](../../../awscloudtrail/latest/userguide/encrypting-cloudtrail-log-files-with-aws-kms.md "../../../awscloudtrail/latest/userguide/encrypting-cloudtrail-log-files-with-aws-kms.md")
   - Set up
     [immutable
     log storage](../../../AmazonS3/latest/userguide/object-lock.md "../../../AmazonS3/latest/userguide/object-lock.md") using S3 Object Lock

2. **Implement session
   logging:**
   - Enable
     [session
     logging](../../../systems-manager/latest/userguide/session-manager-logging.md "../../../systems-manager/latest/userguide/session-manager-logging.md")
   - Configure session logging to
     [Amazon S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") and
     [CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md")
   - Enable
     [encrypted
     session data](../../../systems-manager/latest/userguide/session-manager-logging.md#session-manager-logging-encryption "../../../systems-manager/latest/userguide/session-manager-logging.md#session-manager-logging-encryption")
   - Implement session log retention policies

3. **Set up Amazon CloudWatch Logs:**
   - Create
     [log
     groups](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") for different types of operator activities
   - Configure
     [retention
     periods](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#SttingLogRetention "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#SttingLogRetention") based on compliance requirements
   - Implement
     [metric
     filters](../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md "../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md") for important events
   - Set up
     [cross-account
     log aggregation](../../../AmazonCloudWatch/latest/logs/CrossAccountSubscriptions.md "../../../AmazonCloudWatch/latest/logs/CrossAccountSubscriptions.md")

4. **Establish a log storage
   strategy:**
   - Define log retention periods based on compliance
     requirements
   - Implement
     [lifecycle
     policies](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") for log data
   - Configure
     [secure
     archive storage](../../../AmazonS3/latest/userguide/storage-class-intro.md "../../../AmazonS3/latest/userguide/storage-class-intro.md") using S3 storage classes
   - Implement
     [access
     controls](../../../AmazonS3/latest/userguide/access-control-overview.md "../../../AmazonS3/latest/userguide/access-control-overview.md") for log data

5. **Configure monitoring and
   alerting:**
   - Set up
     [CloudWatch
     alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") for suspicious activities
   - Create automated notifications for security events using
     [Amazon SNS](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md")
   - Implement real-time log analysis with
     [CloudWatch Logs Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md")
   - Configure
     [dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md")
     for log monitoring

## Resources

**Related best practices**:

- [SEC04-BP01
  Configure service and application logging](../security-pillar/sec_detect_investigate_events_app_service_logging.md "../security-pillar/sec_detect_investigate_events_app_service_logging.md")
- [SEC04-BP02
  Analyze logs, findings, and metrics centrally](../security-pillar/sec_detect_investigate_events_analyze_logs_findings.md "../security-pillar/sec_detect_investigate_events_analyze_logs_findings.md")
- [SEC04-BP04
  Implement actionable security events](../security-pillar/sec_detect_investigate_events_actionable_events.md "../security-pillar/sec_detect_investigate_events_actionable_events.md")
- [SEC08-BP01
  Implement secure key management](../security-pillar/sec_protect_data_at_rest_key_management.md "../security-pillar/sec_protect_data_at_rest_key_management.md")
- [SEC08-BP02
  Enforce encryption at rest](../security-pillar/sec_protect_data_at_rest_encrypt_data.md "../security-pillar/sec_protect_data_at_rest_encrypt_data.md")
- [SEC08-BP03
  Automate data at rest protection](../security-pillar/sec_protect_data_at_rest_automate_protection.md "../security-pillar/sec_protect_data_at_rest_automate_protection.md")
- [SEC03-BP01
  Define access requirements](../security-pillar/sec_permissions_define.md "../security-pillar/sec_permissions_define.md")
- [SEC03-BP02
  Grant least privilege access](../security-pillar/sec_permissions_least_privileges.md "../security-pillar/sec_permissions_least_privileges.md")
- [SEC03-BP03
  Establish emergency access process](../security-pillar/sec_permissions_emergency_process.md "../security-pillar/sec_permissions_emergency_process.md")
- [OPS08-BP02
  Analyze workload logs](../operational-excellence-pillar/ps_workload_observability_analyze_workload_logs.md "../operational-excellence-pillar/ps_workload_observability_analyze_workload_logs.md")
- [OPS08-BP04
  Create actionable alerts](../operational-excellence-pillar/ops_workload_observability_create_alerts.md "../operational-excellence-pillar/ops_workload_observability_create_alerts.md")

**Related videos**:

- [AWS re:Invent 2022 - Cloud compliance, assurance, and auditing
  (COP304)](https://www.youtube.com/watch?v=xREhfrUqpd4 "https://www.youtube.com/watch?v=xREhfrUqpd4")
- [AWS re:Inforce 2025 - Operationalizing Amazon Security Lake with
  analytics and generative AI (TDR342)](https://www.youtube.com/watch?v=cRs9kyWQqWE "https://www.youtube.com/watch?v=cRs9kyWQqWE")

**Related documents**:

- [AWS CloudTrail Best Practices](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [Centralized
  Logging with Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")

**Related services**:

- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
- [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")
- [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [Amazon SNS](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/")
- [Amazon
  Security Lake](https://aws.amazon.com/security-lake/ "https://aws.amazon.com/security-lake/")
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/")
- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
- [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/")
