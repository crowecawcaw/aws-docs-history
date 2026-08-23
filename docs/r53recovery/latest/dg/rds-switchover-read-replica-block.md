# Amazon RDS Switchover Read Replica execution block

**Category:** Database switchover

The Amazon RDS Switchover Read Replica execution block allows you to perform a controlled switchover
of an Amazon RDS Oracle read replica, making it the new primary database instance. This enables
multi-Region database failover for Amazon RDS Oracle deployments that use cross-Region read replicas,
without data loss in the graceful path.

## Key benefits

- **Zero data loss switchover:** The graceful switchover
  path ensures that all data is synchronized between the primary and standby before
  promoting the read replica, preventing any data loss.
- **Automated validation:** Region switch validates engine
  compatibility, replication state, backup configuration, and pending maintenance before
  attempting the switchover.
- **Ungraceful fallback:** If a graceful switchover
  is not possible or an ungraceful execution is requested, Region switch can promote the read
  replica directly, prioritizing recovery speed.

## Configuration

When you configure the Amazon RDS Switchover Read Replica execution block, you provide the database
instance ARNs for each Region in your multi-Region Amazon RDS Oracle deployment.

###### Important

Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place.
For more information, see [Amazon RDS Switchover Read Replica execution block sample policy](security_iam_region_switch_rds_switchover_read_replica.md "security_iam_region_switch_rds_switchover_read_replica.md").

To configure an Amazon RDS Switchover Read Replica execution block, enter the following values:

1. **Step name:** Enter a name.
2. **Step description (optional):** Enter a description of the step.
3. **DB Instance ARN for _Region_:** Enter the
   database instance ARN for each Region in your plan. You must provide an ARN for each Region.
4. **Timeout:** Enter a timeout value.

Then, choose **Save step.**

## How it works

When you execute a plan with an Amazon RDS Switchover Read Replica execution block, Region switch performs
the following operations:

**Graceful switchover (default):**

1. Region switch waits for the target read replica instance to reach an available state.
2. Region switch verifies that the target instance is an Oracle 19c or later read replica in
   a valid standby mode (mounted or open-read-only).
3. Region switch confirms that replication is active between the primary and standby instances.
4. Region switch validates that automatic backups are enabled on the standby instance.
5. Region switch checks for blocking pending maintenance actions on both instances.
6. Region switch validates that the primary instance in the other Region is available.
7. Region switch calls `SwitchoverReadReplica` to promote the standby to primary.
8. Region switch waits for the instance to become the primary and reach an available state.
9. If the original primary had Multi-AZ enabled, Region switch enables Multi-AZ on the new primary to match the original configuration.

**Ungraceful execution (promote read replica):**

When an ungraceful execution is requested with the `promoteReadReplica` behavior,
Region switch promotes the read replica directly using `PromoteReadReplica`. This is faster
but may result in data loss if replication has not fully synchronized. After promotion, Region switch
restores the backup retention period, preferred backup window, and Multi-AZ settings from the
original primary's configuration.

If an ungraceful execution is requested without specifying a behavior, Region switch falls back to
the graceful switchover path.

###### Note

This execution block supports only Amazon RDS Oracle 19c and later. Aurora databases should use
the Aurora Global Databases execution block instead.

## What is evaluated as part of plan evaluation

When Region switch evaluates your plan, Region switch performs several checks on your Amazon RDS Switchover Read
Replica execution block configuration:

- The database instance ARNs are valid and the instances exist in their respective Regions.
- One instance is a read replica of the other (a valid replication relationship exists).
- The engine is Oracle 19c or later (not Aurora, not custom).
- Engine versions match between primary and standby instances.
- The standby instance is in mounted or open-read-only mode.
- The standby instance has automatic backups enabled with a non-zero retention period.
- Replication is actively replicating between instances.
- No blocking pending maintenance actions exist on the in-region instance.
- Option groups are not shared with unrelated instances (which could cause issues during switchover).
- Resource monitor data exists for the other-region instance (used for configuration restoration after ungraceful promote).

Region switch also validates that the plan's IAM role has the correct permissions for Amazon RDS
switchover. For more information about the required permissions for Region switch execution
blocks, see [Amazon RDS Switchover Read Replica execution block sample policy](security_iam_region_switch_rds_switchover_read_replica.md "security_iam_region_switch_rds_switchover_read_replica.md"). If any of the checks
fail, Region switch returns warning messages, which you can view in the console. Or, you can
receive the validation warnings through or by using API operations.

## Related resources

- [Amazon RDS Switchover Read Replica execution block sample policy](security_iam_region_switch_rds_switchover_read_replica.md "security_iam_region_switch_rds_switchover_read_replica.md")
- [Working with Oracle replicas for Amazon RDS](../../../AmazonRDS/latest/UserGuide/oracle-read-replicas.md "../../../AmazonRDS/latest/UserGuide/oracle-read-replicas.md")
  in the _Amazon RDS User Guide_
