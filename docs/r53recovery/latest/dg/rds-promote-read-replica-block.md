# Amazon RDS Promote Read Replica execution block

The Amazon RDS Promote Read Replica execution block allows you to promote an Amazon RDS read replica
to a standalone database instance as part of your multi-Region recovery process. This enables you to
failover to a healthy Region by promoting the read replica in that Region to become the new primary database.

## Configuration

To configure an Amazon RDS Promote Read Replica execution block, enter the following values.

###### Important

Before you configure the execution block, make sure that you have the correct IAM policy in place.
For more information, see [Amazon RDS execution block sample policy](security_iam_region_switch_rds.md "security_iam_region_switch_rds.md").

1. **Step name:** Enter a name.
2. **Step description (optional):** Enter a description of the step.
3. **RDS DB instance ARN for Region:** Enter the
   database instance ARN for the read replica in each Region in the plan.
4. **Timeout:** Enter a timeout value.

Then, choose **Save step.**

## How it works

By configuring an Amazon RDS Promote Read Replica execution block, you can promote a read replica to a
standalone database instance as part of your application recovery. When you execute the plan, Region switch
promotes the read replica in the Region that you're activating to become an independent database instance.

###### Note

This block only supports active/passive plans

During promotion, the DNS endpoint that you use to connect to the database will remain the same.
However, the promoted instance will no longer replicate from the original primary database. You are
responsible for ensuring their application is configured to use the correct endpoint after the operation completes.

After promotion, the promoted instance inherits the following settings from the original primary instance:

- Backup retention period
- Preferred backup window
- Multi-AZ configuration

## What is evaluated as part of plan evaluation

When Region switch evaluates your plan, Region switch performs several checks on your Amazon RDS execution block configuration
and permissions. Region switch verifies that the following is correct:

- The Amazon RDS database instances specified in the configuration exist.
- The database instances in the non-primary Regions are read replicas.
- The read replicas are in an available state.
- The database instances are properly configured for cross-Region replication.

Region switch also validates that the plan's IAM role has the required permissions for Amazon RDS read replica promotion.
For more information about the required permissions for Region switch execution
blocks, see [Identity-based policy examples for Region switch in ARC](security_iam_id-based-policy-examples-region-switch.md "security_iam_id-based-policy-examples-region-switch.md").

The correct IAM permissions are essential for the proper functioning of the Amazon RDS execution block. If
any of these validations fail, Region switch returns warnings that there are issues, and provides specific error messages to help
you resolve the permissions or configuration issues. This ensures that your plan has the necessary access to manage
and interact with Amazon RDS during when this step runs during a plan execution.
