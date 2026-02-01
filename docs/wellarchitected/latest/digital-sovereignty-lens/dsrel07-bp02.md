# DSREL07-BP02 Continually monitor compliance during failures and

failovers

In highly regulated industries, maintaining uninterrupted compliance
visibility during system failures and failovers is non-negotiable
for meeting regulatory requirements and avoiding penalties.
Organizations must implement resilient monitoring architectures that
reduce blind spots during outages and maintain continuous adherence.
Traditional monitoring approaches often fail to maintain adequate
oversight during critical events.

**Desired outcome:** Organizations
maintain continuous compliance monitoring and automated remediation
capabilities across each failure scenario. Regulatory visibility and
audit trails remain uninterrupted during system outages and Regional
failovers. Compliance validation continues without manual
intervention.

**Common anti-patterns:**

- Deploying compliance monitoring tools in a single Availability
  Zone or Region and relying on manual compliance checks without
  automation.
- Insufficient cross-Region control of compliance data and
  inadequate log retention and centralization practices.
- Missing failover testing for compliance systems and lack of
  validation during disaster recovery scenarios.
- Missing meta-data monitoring capabilities, hardcoded compliance
  rules, and insufficient automation for compliance checks.
- Manual failover processes and unvalidated compliance tools in
  backup regions.

**Benefits of establishing this best
practice:**

- Maintains continuous audit trails and compliance evidence across
  each system state, supporting immediate detection of
  non-compliant resources.
- Provides automated remediation and consistent compliance
  controls during Regional failovers without manual intervention.
- Reduces risk, mitigates regulatory penalties, and reduces
  expensive investigations through continuous monitoring.
- Demonstrates robust governance and audit readiness to regulators
  through comprehensive compliance documentation.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

A resilient compliance monitoring architecture should use AWS
services (like AWS CloudTrail, AWS Config, and AWS Security Hub)
across multiple regions using active-passive or active-active
deployment patterns. Key implementation points include:

- Deploy compliance monitoring tools with built-in redundancy
  and automated failover mechanisms across Regions
- Implement cross-Region replication for compliance-critical
  data, configurations, and audit trails
- Establish automated compliance checks, remediation processes,
  and regular testing during disaster recovery exercises
- Embed compliance monitoring into architectural resilience
  mechanisms using AWS tools

### Implementation steps

1. Enable
   [AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md") and configure
   [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") with multi-Region logging. Set up
   [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md") with multi-Region aggregation. Deploy
   [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") rules for cross-Region event routing to
   support continuous compliance monitoring during failures and
   failovers.
2. Configure
   [Amazon S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") bucket replication and set up
   [Amazon DynamoDB](../../../amazondynamodb/latest/developerguide/Introduction.md "../../../amazondynamodb/latest/developerguide/Introduction.md") global tables. Establish
   [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") cross-Region subscriptions and enable
   automated backups. Configure
   [AWS Backup](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md") with cross-Region copy and implement
   [AWS Key Management Service (KMS)](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") multi-Region keys to
   maintain regulatory adherence, data integrity, and
   availability.
3. Create
   [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md") rules for compliance checks and deploy
   [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") functions for automated remediation. Set up
   [AWS Systems Manager](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md") automation runbooks and configure
   [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") alarms for compliance metrics. Implement
   [AWS Audit Manager](../../../audit-manager/latest/userguide/what-is.md "../../../audit-manager/latest/userguide/what-is.md") assessments and establish regular
   compliance testing schedules to support ongoing compliance
   during failures.
4. Set up centralized logging with
   [Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/what-is.md "../../../opensearch-service/latest/developerguide/what-is.md") and create compliance dashboards
   in Amazon CloudWatch. Configure Amazon Simple Notification Service (SNS) topics for compliance alerts and implement
   [AWS Control Tower](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md") for preventive controls. Set up
   [AWS Health](../../../health/latest/ug/what-is-aws-health.md "../../../health/latest/ug/what-is-aws-health.md") API monitoring and enable
   [AWS Trusted Advisor](../../../awssupport/latest/user/trusted-advisor.md "../../../awssupport/latest/user/trusted-advisor.md") checks to monitor and maintain
   regulatory adherence during failures and failovers.

## Resources

**Related best practices:**

- [REL 12. How do you test reliability?](../reliability-pillar/test-reliability.md "../reliability-pillar/test-reliability.md")
- [OPS 8. How do you utilize workload observability in your organization?](../operational-excellence-pillar/utilizing-workload-observability.md "../operational-excellence-pillar/utilizing-workload-observability.md")

**Related documents:**

- [Continuous
  compliance monitoring using custom audit controls and
  frameworks with AWS Audit Manager](https://aws.amazon.com/blogs/security/continuous-compliance-monitoring-using-custom-audit-controls-and-frameworks-with-aws-audit-manager/ "https://aws.amazon.com/blogs/security/continuous-compliance-monitoring-using-custom-audit-controls-and-frameworks-with-aws-audit-manager/")
- [A
  multi-dimensional approach helps you proactively prepare for
  failures, Part 3: Operations and process resiliency](https://aws.amazon.com/blogs/architecture/a-multi-dimensional-approach-helps-you-proactively-prepare-for-failures-part-3-operations-and-process-resiliency/ "https://aws.amazon.com/blogs/architecture/a-multi-dimensional-approach-helps-you-proactively-prepare-for-failures-part-3-operations-and-process-resiliency/")
- [Verify
  the resilience of your workloads using Chaos
  Engineering](https://aws.amazon.com/blogs/architecture/verify-the-resilience-of-your-workloads-using-chaos-engineering/ "https://aws.amazon.com/blogs/architecture/verify-the-resilience-of-your-workloads-using-chaos-engineering/")

**Related videos:**

- [AWS re:Invent 2024 - Intelligent continuous compliance: Redefining
  cloud security for the modern era](https://www.youtube.com/watch?v=QTDumi7TgY8 "https://www.youtube.com/watch?v=QTDumi7TgY8")
- [AWS re:Invent 2019: Designing for failure: Architecting resilient
  systems on AWS (ARC335-R1)](https://www.youtube.com/watch?v=BJVzwaTiOdk "https://www.youtube.com/watch?v=BJVzwaTiOdk")
- [AWS re:Inforce 2024 - Cloud compliance journey: Compliance and
  audits (GRC201)](https://www.youtube.com/watch?v=lwPsDv3rBn8 "https://www.youtube.com/watch?v=lwPsDv3rBn8")

**Related services:**

- [AWS Audit Manager](https://aws.amazon.com/audit-manager/ "https://aws.amazon.com/audit-manager/")
- [AWS Backup](https://aws.amazon.com/aws-backup/ "https://aws.amazon.com/aws-backup/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/")
- [AWS Health](https://aws.amazon.com/premiumsupport/technology/aws-health-dashboard/ "https://aws.amazon.com/premiumsupport/technology/aws-health-dashboard/")
- [AWS Key Management Service](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
- [AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
- [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/ "https://aws.amazon.com/premiumsupport/technology/trusted-advisor/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/")
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/")
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/")
- [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")
- [Amazon SNS](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/")
