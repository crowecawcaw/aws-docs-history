

# `AWSSupportRemediator-EnableRdsLogExports`

**Description**

Enables the export of Amazon Relational Database Service (Amazon RDS) database logs to Amazon CloudWatch Logs.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [RDS DB instances should publish logs to CloudWatch Logs](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-9).

The automation completes successfully without making changes in any of the following cases: the Amazon RDS DB instance does not exist, the database engine has no exportable log types, all exportable log types for the database engine are already enabled, or another in-progress run of this runbook is already modifying the same Amazon RDS DB cluster.

If the Amazon RDS DB instance is a member of an Amazon RDS DB cluster, the runbook configures log exports at the DB cluster level instead of at the DB instance. This affects every DB instance in the cluster.

Enabling log exports requires the Amazon RDS service-linked role `AWSServiceRoleForRDS` to be present in the account. For more information, see [Publishing database logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Procedural.UploadtoCloudWatch.html#integrating_cloudwatchlogs.configure).

Enabling log exports to Amazon CloudWatch Logs might increase costs because the exported logs are ingested and retained in Amazon CloudWatch Logs. For more information about pricing, see [Amazon CloudWatch Logs pricing](https://aws.amazon.com/cloudwatch/pricing/).

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
+ DBInstanceArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the Amazon RDS DB instance.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `rds:DescribeDBClusters`
+ `rds:DescribeDBEngineVersions`
+ `rds:DescribeDBInstances`
+ `rds:ModifyDBCluster`
+ `rds:ModifyDBInstance`
+ `ssm:DescribeAutomationExecutions`
+ `ssm:GetAutomationExecution`

**Document Steps**

1. **validateDatabase** - Validates that the Amazon RDS DB instance exists and is available, identifies the exportable log types, and determines whether changes are required.

1. **branchOnChangeRequired** - Branches based on whether a change is required. For a DB instance, the step continues to `updateDBInstance`. For a DB cluster, it continues to `validateIdempotencyDbCluster`.

1. **updateDBInstance** - Modifies the Amazon RDS DB instance to enable all the exportable Amazon CloudWatch Logs log types that `validateDatabase` identified.

1. **validateIdempotencyDbCluster** - Checks whether another in-progress run of this runbook is already modifying a member of the same Amazon RDS DB cluster. This prevents concurrent `ModifyDBCluster` calls.

1. **branchOnChangeRequiredOnIdempotencyCheck** - Branches on whether the idempotency check requires modifying the Amazon RDS DB cluster, continuing to `updateDBCluster` when a change is required.

1. **updateDBCluster** - Modifies the Amazon RDS DB cluster to enable all the exportable Amazon CloudWatch Logs log types that `validateDatabase` identified.

1. **sleepWaitingForDBClusterStartUpdate** - Waits 20 seconds to allow the Amazon RDS DB cluster members to transition out of the `available` status before polling for readiness.

1. **loopOnClusterMemberStatus** - Iterates over every DB instance in the Amazon RDS DB cluster, waiting for each to return to the `available` status.

**Outputs**
+ validateDatabase.ChangeRequired: Boolean indicating whether a change is required for the Amazon RDS DB instance or DB cluster.
+ validateDatabase.ValidationMessage: The reason returned when no change is required.
+ validateDatabase.InitialEnabledLogTypes: The Amazon CloudWatch Logs log types enabled before this automation runs.