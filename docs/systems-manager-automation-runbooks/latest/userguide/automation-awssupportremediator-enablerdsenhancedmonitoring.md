

# `AWSSupportRemediator-EnableRdsEnhancedMonitoring`

**Description**

Enables enhanced monitoring on an Amazon Relational Database Service (Amazon RDS) DB instance or Multi-AZ DB cluster.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Enhanced monitoring should be configured for RDS DB instances](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-6).

If the Amazon RDS DB instance or cluster does not exist, or if enhanced monitoring is already enabled, the automation completes successfully without making changes.

For a Multi-AZ DB cluster instance, the automation updates enhanced monitoring at the cluster level. The Amazon RDS API does not support `ModifyDBInstance` for cluster members. Amazon RDS does not support enhanced monitoring at the cluster level for the Aurora engine, and the automation fails for Aurora clusters.

The specified AWS Identity and Access Management (IAM) monitoring role must already exist with a trust policy that allows Amazon RDS to assume it. The automation does not create the monitoring role.

After the automation enables enhanced monitoring, Amazon RDS writes operating-system metrics to an Amazon CloudWatch Logs log group named `RDSOSMetrics`. This log group is created in your account if it does not already exist. Enhanced monitoring and the associated CloudWatch Logs ingestion incur ongoing costs. For more information about pricing, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/) and [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/).

To roll back, run the Amazon RDS `ModifyDBInstance` or `ModifyDBCluster` API with `MonitoringInterval` set to 0. The automation does not save the prior `MonitoringInterval` value.

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

  Description: (Required) The Amazon Resource Name (ARN) of the Amazon RDS DB instance or cluster.
+ MonitoringInterval

  Type: Integer

  Description: (Required) The interval, in seconds, at which Amazon RDS collects enhanced monitoring metrics for the DB instance or cluster. Valid values are 1, 5, 10, 15, 30, and 60.
+ MonitoringRoleName

  Type: String

  Description: (Required) The name of the IAM role that Amazon RDS uses to send enhanced monitoring metrics to Amazon CloudWatch Logs.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `iam:GetRole`
+ `iam:PassRole`
+ `rds:DescribeDBClusters`
+ `rds:DescribeDBInstances`
+ `rds:ModifyDBCluster`
+ `rds:ModifyDBInstance`

**Document Steps**

1. **validateDB** - Validates the target Amazon RDS DB instance or cluster and decides whether to enable enhanced monitoring. This step redirects Multi-AZ DB cluster instance requests to the cluster-level update path. This step fails for Aurora clusters because Amazon RDS does not support enhanced monitoring at the cluster level for that engine.

1. **branchOnChangeRequired** - Branches on whether the automation enables enhanced monitoring. This step ends the automation successfully when no change is required.

1. **branchOnDBType** - Branches on whether the target resource is an Amazon RDS DB instance or DB cluster.

1. **updateDBInstance** - Enables enhanced monitoring on the Amazon RDS DB instance using the specified `MonitoringInterval` and IAM monitoring role.

1. **updateDBCluster** - Enables enhanced monitoring on the Amazon RDS DB cluster using the specified `MonitoringInterval` and IAM monitoring role.

**Outputs**
+ validateDB.ChangeRequired: Whether the automation enables enhanced monitoring on the target resource.
+ validateDB.DBIdentifier: The identifier of the Amazon RDS DB instance or cluster that the automation modifies.
+ validateDB.MonitoringRoleArn: The ARN of the IAM monitoring role the automation passes to Amazon RDS.
+ validateDB.ValidationMessage: The reason the automation skips the change, when applicable.