

# `AWSSupportRemediator-RemediateRdsParameterGroupParameter`

**Description**

Updates a single parameter on an Amazon Relational Database Service (Amazon RDS) DB parameter group or DB cluster parameter group to the value recommended by AWS Trusted Advisor.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from the following AWS Trusted Advisor checks:
+ c1qf5bt021: [Amazon RDS InnoDB\_Change\_Buffering parameter using less than optimum value](https://docs.aws.amazon.com/awssupport/latest/user/performance-checks.html#rds-innodb-parameter-less-than-optimal) - recommended value: ALL
+ c1qf5bt025: [Amazon RDS autovacuum parameter is turned off](https://docs.aws.amazon.com/awssupport/latest/user/performance-checks.html#rds-autovacuum-off) - recommended value: 1
+ c1qf5bt026: [Amazon RDS synchronous\_commit parameter is turned off](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#rds-synchronous-commit-parameter-off) - recommended value: ON
+ c1qf5bt028: [Amazon RDS enable\_indexonlyscan parameter is turned off](https://docs.aws.amazon.com/awssupport/latest/user/performance-checks.html#rds-enable-indexonlyscan-parameter-off) - recommended value: 1
+ c1qf5bt029: [Amazon RDS enable\_indexscan parameter is turned off](https://docs.aws.amazon.com/awssupport/latest/user/performance-checks.html#rds-enable-indexscan-parameter-off) - recommended value: 1
+ c1qf5bt030: [Amazon RDS innodb\_flush\_log\_at\_trx\_commit parameter is not 1](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#rds-innodb-flush-log-at-trx-parameter-off) - recommended value: 1
+ c1qf5bt031: [Amazon RDS sync\_binlog parameter is turned off](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#rds-sync-binlog-parameter-off) - recommended value: 1
+ c1qf5bt032: [Amazon RDS innodb\_stats\_persistent parameter is turned off](https://docs.aws.amazon.com/awssupport/latest/user/performance-checks.html#rds-innodb-stats-persistent-parameter-off) - recommended value: ON
+ c1qf5bt036: [Amazon RDS innodb\_default\_row\_format parameter setting is unsafe](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#rds-innodb-default-row-format-unsafe) - recommended value: DYNAMIC
+ c1qf5bt037: [Amazon RDS general\_logging parameter is turned on](https://docs.aws.amazon.com/awssupport/latest/user/performance-checks.html#rds-general-logging-on) - recommended value: 0

The runbook applies the recommended value with `ApplyMethod: immediate`. The change propagates to every Amazon RDS DB instance and DB cluster that uses the parameter group. For parameters that Amazon RDS classifies as `static`, the new value takes effect only after the next reboot of the associated DB instance or DB cluster.

Trusted Advisor chooses recommended values to improve durability, correctness, or observability, and those values can change the runtime performance characteristics of the DB instances and DB clusters that use the parameter group. Review the linked Trusted Advisor check before running the runbook.

If the Amazon RDS parameter group does not exist or the flagged parameter is already set to the recommended value, the automation completes successfully without making changes.

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
+ ParameterGroupArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the Amazon RDS DB parameter group or DB cluster parameter group that Trusted Advisor flagged.
+ ParameterName

  Type: String

  Description: (Required) The name of the Amazon RDS parameter that Trusted Advisor flagged.
+ RecommendedValue

  Type: String

  Description: (Required) The recommended value to mitigate the Trusted Advisor finding. Valid values: `0`, `1`, `ALL`, `ON`, or `DYNAMIC`.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `rds:DescribeDBClusterParameters`
+ `rds:DescribeDBParameters`
+ `rds:ModifyDBClusterParameterGroup`
+ `rds:ModifyDBParameterGroup`

**Document Steps**

1. **validateParameterGroup** - Validates the Amazon RDS parameter group, checks whether the flagged parameter already matches the recommended value, and captures the initial value for traceability. Returns `ChangeRequired: false` when the parameter group does not exist so the automation ends without making changes.

1. **branchOnChangeRequired** - Branches on whether the parameter needs a change and routes to the update step that matches the parameter group type (`pg` or `cluster-pg`). The runbook ends here when the parameter already matches the recommended value or the parameter group does not exist.

1. **updateParameterGroupForDB** - Applies the recommended value to the Amazon RDS DB parameter group by calling `rds:ModifyDBParameterGroup` with `ApplyMethod: immediate`. For `static` parameters, the new value takes effect only after the next reboot of the DB instances that use the parameter group.

1. **updateParameterGroupForCluster** - Applies the recommended value to the Amazon RDS DB cluster parameter group by calling `rds:ModifyDBClusterParameterGroup` with `ApplyMethod: immediate`. For `static` parameters, the new value takes effect only after the next reboot of the DB clusters that use the parameter group.

**Outputs**
+ validateParameterGroup.ChangeRequired: Whether the parameter needs a change.
+ validateParameterGroup.InitialParameterValue: The parameter value before modification, for traceability and rollback.
+ validateParameterGroup.ParameterGroupName: The parameter group name that the runbook derives from the ARN.
+ validateParameterGroup.ParameterGroupType: The type of the parameter group (`pg` or `cluster-pg`).
+ validateParameterGroup.ValidationMessage: A message describing the validation outcome.