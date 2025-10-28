# Amazon Aurora Global Database execution block

The Amazon Aurora Global Database execution block allows you to perform a _failover_ or
_switchover_ recovery workflow for a global database.

- Failover – Use this approach to recover from an unplanned outage. With this
  approach, you perform a cross-Region failover to one of the
  secondary DB clusters in your Aurora global databases. The recovery point objective (RPO) for this approach is typically
  a non-zero value measured in seconds. The amount of data loss
  depends on the Aurora global databases replication lag across the AWS Regions at the time
  of the failure. For more information, see [Recovering an Amazon Aurora global database from an
  unplanned outage](../../../AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.md#aurora-global-database-failover "../../../AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.md#aurora-global-database-failover") in the Amazon Aurora User Guide.
- Switchover – This operation was previously called _managed planned failover_.
  Use this approach for controlled scenarios, such as operational maintenance and other planned
  operational procedures where all the Aurora clusters and other services they interact with are
  in a healthy state. Because this feature synchronizes secondary DB clusters with the primary
  before making any other changes, RPO is 0 (no data loss). For more information, see
  [Performing switchovers for Amazon Aurora global databases](../../../AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.md#aurora-global-database-disaster-recovery.managed-failover "../../../AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.md#aurora-global-database-disaster-recovery.managed-failover") in the Amazon Aurora User Guide.

## Configuration

To configure an Aurora Global Database execution block, enter the following values.

###### Important

Before you configure the execution block, make sure that you have the correct IAM policy in place.
For more information, see [Aurora Global Database execution block sample policy](security_iam_region_switch_aurora.md "security_iam_region_switch_aurora.md").

1. **Step name:** Enter a name.
2. **Step description (optional):** Enter a description of the step.
3. **Aurora Global Database cluster name:** Enter the identifier for
   the global database.
4. **Cluster ARN for _Region_:** Enter the
   cluster ARN to use in each Region in the plan.
5. **Specify the option for Aurora database:** Choose
   either **Switchover** or **Failover (data loss)**, depending
   on how you want
6. **Aurora Global Database cluster name:**
7. **Timeout:** Enter a timeout value.

Then, choose **Save step.**

## How it works

By configuring a Aurora Global Databases execution block, you can failover or switchover global
databases as part of your application recovery. If you’re using an active/active approach, Region switch
uses the other configured Region as the source. That is, if a Region is being deactivated, Region switch
uses the other active Region as the source to match for the percent to scale.

This block supports both graceful and ungraceful execution modes. Ungraceful
settings perform an Aurora Global Database _failover_, which might cause data loss.

For more information about Aurora Global Database disaster recovery, including failover and switchover, see
[Using switchover or failover in Amazon Aurora global databases](../../../AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.md "../../../AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.md") in the Amazon Aurora User Guide.

## What is evaluated as part of plan evaluation

When Region switch evaluates your plan, Region switch performs several checks on your Aurora execution block configuration
and permissions. Region switch verifies that the following is correct:

- The Aurora global cluster specified in the configuration exists.
- There are Aurora DB clusters in both the source and destination Regions.
- The source and destination DB clusters are in a state that allows Global Database switchover.
- There are DB instances in both the source and destination clusters
- The global cluster engine versions for the switchover action are compatible. This includes verifying that
  the clusters are on the same Major, Minor, and patch versions, with some exceptions that are listed in
  the Aurora documentation.

Region switch also validates that the plan's IAM role has the required permissions for Aurora failover and switchover.
For more information about the required permissions for Region switch execution
blocks, see [Identity-based policy
examples for Region switch in ARC](security_iam_id-based-policy-examples-region-switch.md "security_iam_id-based-policy-examples-region-switch.md").

The correct IAM permissions are essential for the proper functioning of the Aurora execution block. If
any of these validations fail, Region switch returns warnings that there are issues, and provides specific error messages to help
you resolve the permissions or configuration issues. This ensures that your plan has the necessary access to manage
and interact with the Aurora during when this step runs during a plan execution.
