

# `AWSSupportRemediator-StopIdleRdsInstance`

**Description**

Stops an Amazon Relational Database Service (Amazon RDS) DB instance that remains idle with no database connections over the last 7 days.

Before stopping, the automation creates a DB snapshot. Supported engines are MariaDB, Microsoft SQL Server, MySQL, Oracle, and PostgreSQL. This runbook does not support Aurora DB instances, custom DB instances, or DB instances that are part of a cluster.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Amazon RDS Idle DB Instances](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#amazon-rds-idle-dbs-instances) and AWS Compute Optimizer [Idle Amazon RDS instance](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html).

If the DB instance does not exist, is already stopped, or is in stopping state, the automation completes successfully without making changes. If the DB instance is in stopping state, the automation waits for the DB instance to reach stopped state.

The automation creates a DB snapshot named `{DBInstanceIdentifier}-snapshot-by-ssm-execution-{ExecutionId}` before stopping the DB instance. Amazon RDS automatically restarts a stopped DB instance after 7 days. Stopping a DB instance might temporarily affect availability. The snapshot incurs standard Amazon RDS snapshot storage costs. For more information about pricing, see [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/).

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
+ DBInstanceIdentifier

  Type: String

  Description: (Required) The identifier of the Amazon RDS DB instance to evaluate and stop if idle.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `cloudwatch:GetMetricStatistics`
+ `rds:CreateDBSnapshot`
+ `rds:DescribeDBInstances`
+ `rds:DescribeDBSnapshots`
+ `rds:StopDBInstance`

**Document Steps**

1. **validateRdsEngineAndStatus** - Validates that the Amazon RDS DB instance exists, is in a supported state, uses a supported engine, and is not part of a cluster.

1. **branchOnInitialInstanceStatus** - Branches on whether the DB instance is available or in stopping state.

1. **validateRdsIdleStatus** - Validates that the Amazon RDS DB instance has had no database connections over the last 7 days using Amazon CloudWatch metrics.

1. **stopDBInstance** - Creates a DB snapshot and stops the Amazon RDS DB instance.

1. **waitForStopCompletion** - Waits for the Amazon RDS DB instance to reach stopped state.

1. **branchOnStoppingStatus** - Branches on whether the DB instance was initially in stopping state to skip snapshot verification.

1. **validateSnapshot** - Verifies that the DB snapshot created during the stop operation completed successfully.

**Outputs**
+ validateRdsEngineAndStatus.InitialInstanceStatus: The initial status of the Amazon RDS DB instance.
+ validateRdsEngineAndStatus.ChangeRequired: Whether the DB instance needs to be stopped.
+ validateRdsEngineAndStatus.ValidationMessage: A message describing the validation result.
+ validateSnapshot.DBSnapshotArn: The Amazon Resource Name (ARN) of the snapshot created before stopping the DB instance.