# DSSEC02-BP01 Establish comprehensive logging and monitoring of

user actions

Comprehensive logging enables organizations to track user
activities, detect unauthorized access, and provide evidence during
security incidents or audits. This is a key capability required by
sovereign workloads. The logging principles outlined here apply
universally, assisting organizations to safeguard their operations
and maintain data integrity across their digital infrastructure.

**Desired outcome:** Complete
visibility into system activities and data access with tamper-proof
logs stored in compliant regions, enabling rapid incident response
and regulatory audits.

**Common anti-patterns:**

- Failing to enable comprehensive logging across AWS services,
  Regions, and accounts.
- Implementing inconsistent logging formats and standards across
  services.
- Not protecting log data from unauthorized access or
  modification.
- Not defining and enforcing consistent retention periods.
- Storing logs in regions that violate data residency
  requirements.
- Failing to regularly validate logging mechanisms for
  completeness, accuracy and integrity.

**Benefits of establishing this best
practice:**

- Provides evidence for regulatory audits, demonstrates adherence
  to digital sovereignty requirements (such as GDPR in Europe,
  data localization laws in specific countries), and satisfies
  industry-specific compliance standards.
- Enables faster detection, thorough investigation, and more
  effective remediation of security incidents while maintaining
  sovereign control over security operations.
- Tracks data access patterns, supports data protection
  initiatives, and enables verification of compliance with data
  residency requirements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implementing effective logging for digital sovereignty requires a
strategic approach addressing data residency constraints,
retention requirements, and security controls. Your logging
solution should be designed to be comprehensive, tamper-resistant,
and aligned with local regulations. Verify logs are only
accessible to authorized personnel and within authorized
jurisdictions.

Key implementation considerations include defining logging scope
based on regulatory requirements, implementing centralized log
aggregation with data residency controls, establishing retention
periods with immutability where required, and developing automated
monitoring and alerting capabilities. These considerations are
detailed in the implementation steps below.

### Implementation steps

1. **Define logging requirements and
   retention periods:**
   - Document specific logging requirements based on your
     industry and jurisdictional regulations.
   - Identify mandatory retention periods for different types
     of logs.
   - Determine data residency constraints for log storage.
   - Define the scope of actions and access events that must
     be logged. For example, consider
     _who_ accessed
     _what_ and from
     _where_, as some of the minimum
     information required in log files. The granularity of
     logging needs to be carefully calibrated - while some
     systems may require detailed transaction logs, others
     might only need summary-level information.
   - Identify critical systems and data that require enhanced
     logging.

2. **Configure AWS CloudTrail across
   accounts and Regions:**
   - Enable organization-wide
     [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") trails that capture read and write
     management events across AWS accounts.
   - Enable data events for sensitive S3 buckets, Lambda
     functions, DynamoDB tables, and other data services
     identified in the previous step.
   - Configure log file validation to detect unauthorized
     modifications. See this guide,
     [Validating
     CloudTrail log file integrity](../../../awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.md "../../../awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.md").

3. **Based on the defined requirements,
   enable service-specific logging:**
   - Enable
     [VPC
     Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") for network traffic monitoring.
   - Configure
     [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md") to record resource configuration changes.
   - Set up
     [Amazon S3 server access logging](../../../AmazonS3/latest/userguide/ServerLogs.md "../../../AmazonS3/latest/userguide/ServerLogs.md") for data access
     patterns.
   - Configure
     [Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_LogAccess.md "../../../AmazonRDS/latest/UserGuide/USER_LogAccess.md") and
     [Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.md") database audit logging.
   - Activate
     [Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md") and
     [Amazon Inspector](../../../inspector/latest/user/what-is-inspector.md "../../../inspector/latest/user/what-is-inspector.md") as sources of additional security
     findings.

4. **Establish centralized log storage
   with sovereignty controls:** The implementation of
   a centralized logging system must prioritize data residency
   compliance while maintaining operational efficiency. This
   involves selecting and deploying log aggregation solutions
   that can enforce geographic data boundaries while providing
   comprehensive coverage.
   - Create dedicated log archive accounts within regions
     that meet your data residency requirements (for example,
     AWS Regions in specific countries or geographic areas
     that comply with local data sovereignty laws).
   - Implement IAM policies to restrict access, modification,
     or deletion of log files.
   - Implement log retention policies in line with
     jurisdictional data retention requirements.
   - Configure MFA for sensitive data access or tasks (for
     example, deletion of data)
   - Control replication of log files to other AWS Regions to
     maintain data sovereignty:
     - Using
       [service
       control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md"): Apply deny actions for
       PutReplicationConfiguration and
       DeleteReplicationConfiguration to
       specific S3 buckets containing sensitive log files,
       and add
       [Region
       deny controls](../../../controltower/latest/controlreference/ou-region-deny.md "../../../controltower/latest/controlreference/ou-region-deny.md").
     - Using
       [IAM
       policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md"): Blocks users from setting up
       replication using IAM Permission Boundaries.
     - Using
       [S3
       bucket policies](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md"):
       [Temporarily
       block](https://aws.amazon.com/blogs/storage/temporarily-block-data-transfers-between-aws-regions-in-amazon-s3/#:~:text=You%20can%20block%20ingress%20and,tandem%20with%20the%20ip%2Dranges. "https://aws.amazon.com/blogs/storage/temporarily-block-data-transfers-between-aws-regions-in-amazon-s3/#:~:text=You%20can%20block%20ingress%20and,tandem%20with%20the%20ip%2Dranges.") data transfers between AWS Regions in
       Amazon S3 to block replication of log files.

   - Apply encryption using
     [AWS KMS](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") with appropriate key controls. Understand
     [security
     considerations](../../../kms/latest/developerguide/mrk-when-to-use.md "../../../kms/latest/developerguide/mrk-when-to-use.md") before creating multi-Region keys.
   - Configure immutable S3 buckets using object locks with a
     [write-once-read-many
     (WORM) configuration](../../../AmazonS3/latest/userguide/object-lock.md "../../../AmazonS3/latest/userguide/object-lock.md"). Consider
     [AWS CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md"), which provides immutable,
     queryable storage of CloudTrail events for up to 7
     years, simplifying compliance audits and forensic
     investigations without managing S3 buckets directly.

5. **Implement log analysis and
   monitoring:** An effective logging system must
   include robust analysis, monitoring and alerting
   capabilities that provide real-time visibility into system
   activities. This involves implementing continuous log
   analysis for critical events and developing anomaly
   detection algorithms that can identify unusual patterns or
   potential security incidents.
   - Configure
     [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") to monitor your trail logs.
     Detect and send notifications for unauthorized access or
     suspicious activities against security and compliance
     data, including:
     - Attempts to modify or delete security and compliance
       data
     - Attempts to modify security configurations
       protecting the data (such as unauthorized access to
       encryption keys)

   - Create dedicated
     [IAM
     roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") for log analysis and audit functions
   - Configure
     [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") rules for automated responses to
     critical events (such as IAM policy changes, encryption
     key deletion, or root account usage)
   - Consider additional AWS services such as
     [Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/what-is.md "../../../opensearch-service/latest/developerguide/what-is.md"),
     [Quick Suite](../../../quicksight/latest/user/welcome.md "../../../quicksight/latest/user/welcome.md"), or third-party solutions for enhanced
     analytics, reporting, and visualization

6. **Verify logging completeness and
   compliance:**
   - Regularly audit logging configurations against
     requirements:
     - Perform periodic testing to verify logs capture
       critical activities (such as IAM policy changes, S3
       bucket deletions, or security group modifications)
     - Conduct simulated security incidents to test the
       effectiveness of your logging configurations.
       Consider using
       [AWS Well-Architected Labs - Security](https://wellarchitectedlabs.com/security/ "https://wellarchitectedlabs.com/security/") for hands-on
       practice.

   - Validate log retention periods. Log retention policies
     must define clear retention periods based on both legal
     requirements and operational needs, implementing
     automated log rotation and archival strategies to manage
     data lifecycle. Use automated test cases (such as
     [AWS Config Rules](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md") or custom Lambda functions) to
     continuously check configurations.

7. **Validate third-party
   controls:** Organizations often use third-party
   services that generate, process, or consume security and
   compliance data (such as application performance management
   (APM) SaaS providers, security information and event
   management (SIEM) systems, or compliance management
   solutions). To verify these services meet your sovereignty
   and compliance requirements:
   - Review the vendor's compliance:
     - Request relevant accreditations or certifications
       specific to the services they provide (such as SOC
       2, ISO 27001, or Region-specific certifications)
     - Verify the data residency of the service and confirm
       it aligns with your sovereignty requirements. Where
       necessary, validate the security clearance and
       location of personnel who have access to your
       security and compliance data.

   - Assess technical integration points: Verify API security
     controls (such as authentication, encryption in transit,
     and rate limiting), review IAM federation configurations
     to maintain least privilege access, confirm data
     transfer mechanisms comply with your data residency
     requirements, and test integration points to verify logs
     are transmitted securely and completely.

8. **Implement continuous
   improvement:**
   - Regularly review and update your logging strategy based
     on regulatory changes and emerging threats
   - Assess new AWS services for logging requirements as you
     adopt them
   - Optimize log storage and analysis for cost and
     performance:
     - Use
       [S3
       Intelligent-Tiering](../../../AmazonS3/latest/userguide/intelligent-tiering.md "../../../AmazonS3/latest/userguide/intelligent-tiering.md") to automatically move
       logs to cost-effective storage tiers
     - Implement lifecycle policies to transition older
       logs to
       [Amazon Glacier](../../../amazonglacier/latest/dev/introduction.md "../../../amazonglacier/latest/dev/introduction.md") for long-term retention
     - Review
       [AWS Cost Optimization best practices](../cost-optimization-pillar/welcome.md "../cost-optimization-pillar/welcome.md") for
       additional guidance

   - Incorporate feedback from security teams, auditors, and
     incident response exercises
   - Conduct regular training on log analysis techniques
     using resources like
     [AWS Skill
     Builder](https://skillbuilder.aws/ "https://skillbuilder.aws/") and
     [AWS Security workshops](https://workshops.aws/categories/Security "https://workshops.aws/categories/Security")

## Resources

**Related best practices:**

- [SEC04-BP01
  Configure service and application logging](../security-pillar/sec_detect_investigate_events_app_service_logging.md "../security-pillar/sec_detect_investigate_events_app_service_logging.md")
- [SEC04-BP02
  Capture logs, findings, and metrics in standardized
  locations](../security-pillar/sec_detect_investigate_events_logs.md "../security-pillar/sec_detect_investigate_events_logs.md")
- [SEC04-BP03
  Correlate and enrich security alerts](../security-pillar/sec_detect_investigate_events_security_alerts.md "../security-pillar/sec_detect_investigate_events_security_alerts.md")
- [SEC10-BP03
  Prepare forensic capabilities](../security-pillar/sec_incident_response_prepare_forensic.md "../security-pillar/sec_incident_response_prepare_forensic.md")
- [SEC08-BP02
  Enforce encryption at rest](../security-pillar/sec_protect_data_rest_encrypt.md "../security-pillar/sec_protect_data_rest_encrypt.md")

**Related services:**

- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [Amazon CloudWatch Logs](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")
- [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")

**Related documents:**

- [AWS Security Incident Response Technical Guide](../../../security-ir/latest/userguide/security-incident-response-guide.md "../../../security-ir/latest/userguide/security-incident-response-guide.md")
- [Centralized
  logging and monitoring](../../../prescriptive-guidance/latest/designing-control-tower-landing-zone/logging-monitoring.md "../../../prescriptive-guidance/latest/designing-control-tower-landing-zone/logging-monitoring.md")
- [Build
  your own centralized log analytics platform with Amazon OpenSearch Service](../../../solutions/latest/centralized-logging-with-opensearch/solution-overview.md "../../../solutions/latest/centralized-logging-with-opensearch/solution-overview.md")
- [The
  AWS Security Reference Architecture - Log Archive
  account](../../../prescriptive-guidance/latest/security-reference-architecture/log-archive.md "../../../prescriptive-guidance/latest/security-reference-architecture/log-archive.md")
