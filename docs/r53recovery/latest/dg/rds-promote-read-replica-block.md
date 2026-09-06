

# Amazon RDS Promote Read Replica execution block
<a name="rds-promote-read-replica-block"></a>

The Amazon RDS Promote Read Replica execution block allows you to promote an Amazon RDS read replica to a standalone database instance as part of your multi-Region recovery process. This enables you to failover to a healthy Region by promoting the read replica in that Region to become the new primary database.

## Configuration
<a name="rds-promote-read-replica-block-config"></a>

To configure an Amazon RDS Promote Read Replica execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Amazon RDS execution block sample policy](security_iam_region_switch_rds.md).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **RDS DB instance ARN for Region: **Enter the database instance ARN for the read replica in each Region in the plan.

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

## How it works
<a name="rds-promote-read-replica-block-how"></a>

By configuring an Amazon RDS Promote Read Replica execution block, you can promote a read replica to a standalone database instance as part of your application recovery. When you execute the plan, Region switch promotes the read replica in the Region that you're activating to become an independent database instance.

**Note**  
This block only supports active/passive plans

During promotion, the DNS endpoint that you use to connect to the database will remain the same. However, the promoted instance will no longer replicate from the original primary database. You are responsible for ensuring their application is configured to use the correct endpoint after the operation completes.

After promotion, the promoted instance inherits the following settings from the original primary instance:
+ Backup retention period
+ Preferred backup window
+ Multi-AZ configuration