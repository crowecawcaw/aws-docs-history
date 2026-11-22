

# `AWSSupportRemediator-EnableRdsPerformanceInsights`

**Description**

Enables [Performance Insights](https://aws.amazon.com/rds/performance-insights/) on an Amazon Relational Database Service (Amazon RDS) DB instance or Amazon Aurora DB cluster.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Amazon RDS Performance Insights is turned off](https://docs.aws.amazon.com/awssupport/latest/user/operational-excellence-checks.html#rds-performance-insights-off).

If the Amazon RDS DB instance or Amazon Aurora DB cluster does not exist, or Performance Insights is already enabled, the automation completes successfully without making changes.

The target Amazon RDS DB instance or Amazon Aurora DB cluster must be in the `available` state for this automation to run.

The automation calls the Amazon RDS `ModifyDBInstance` API for a DB instance, or `ModifyDBCluster` for an Amazon Aurora DB cluster. Enabling Performance Insights is an online modification and does not cause downtime on the target resource. Amazon RDS encrypts Performance Insights data with the AWS Key Management Service (AWS KMS) key that the `KmsKeyAlias` parameter identifies. Amazon RDS creates a grant on that key so that the service can perform the encryption on your behalf. If you do not provide `KmsKeyAlias`, Amazon RDS uses the AWS managed key `alias/aws/rds`. Disabling Performance Insights later does not automatically revoke the AWS KMS grant; remove the grant manually if you no longer need it.

To disable Performance Insights after enabling it, call the corresponding modify API and pass `false` for `EnablePerformanceInsights`.

Retention periods longer than 7 days incur additional charges. For more information about pricing, see [Performance Insights pricing](https://aws.amazon.com/rds/performance-insights/pricing/).

**Important considerations**  
You are responsible for reviewing automation actions before they run.
This automation might cause stack drift if the resource is part of an AWS CloudFormation stack.
Access to `AWSSupportRemediator-*` runbooks requires an active Business Support\+, Enterprise Support, or Unified Operations Support plan. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) on the AWS website.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ DBIdentifierArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the Amazon RDS DB instance or Amazon Aurora DB cluster.
+ KmsKeyAlias

  Type: String

  Description: (Optional) The AWS KMS key alias that Amazon RDS uses to encrypt Performance Insights data. If you do not specify `KmsKeyAlias`, Amazon RDS uses the AWS managed key.

  Default: alias/aws/rds
+ PerformanceInsightsRetentionPeriod

  Type: Integer

  Description: (Optional) The number of days to retain Performance Insights data. Valid values are 7, 731, or any multiple of 31 from 31 through 713. Retention periods longer than 7 days incur additional charges.

  Default: 7

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `kms:CreateGrant`
+ `kms:DescribeKey`
+ `rds:DescribeDBClusters`
+ `rds:DescribeDBInstances`
+ `rds:ModifyDBCluster`
+ `rds:ModifyDBInstance`

**Document Steps**

1. **validateDB** - Parses the `DBIdentifierArn` to determine whether the target is an Amazon RDS DB instance or an Amazon Aurora DB cluster. Describes the resource to verify that it exists, is in the `available` state, and does not already have Performance Insights enabled.

1. **branchOnChangeRequired** - Branches on whether a change is required and on the DB type. Routes to `updateDBInstance` for an Amazon RDS DB instance, to `updateDBCluster` for an Amazon Aurora DB cluster, or ends the automation if no change is required.

1. **updateDBInstance** - Calls the Amazon RDS `ModifyDBInstance` API to enable Performance Insights on the target DB instance using the specified retention period and AWS KMS key alias.

1. **updateDBCluster** - Calls the Amazon RDS `ModifyDBCluster` API to enable Performance Insights on the target Amazon Aurora DB cluster using the specified retention period and AWS KMS key alias.

**Outputs**
+ validateDB.ChangeRequired: Boolean indicating whether the target resource requires a change.
+ validateDB.DBIdentifier: The identifier of the Amazon RDS DB instance or Amazon Aurora DB cluster parsed from `DBIdentifierArn`.
+ validateDB.ValidationMessage: Message describing the result of the validation step.