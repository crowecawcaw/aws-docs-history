# Amazon RDS Create Cross-Region Replica execution block

The Amazon RDS Create Cross-Region Replica execution block allows you to create a cross-Region read replica
for an Amazon RDS database instance as part of your post-recovery process. This execution block is typically used
after promoting a read replica to re-establish cross-Region replication, ensuring your application is prepared
for future regional events.

## Configuration

To configure an Amazon RDS Create Cross-Region Replica execution block, enter the following values.

###### Important

Before you configure the execution block, make sure that you have the correct IAM policy in place.
For more information, see [Amazon RDS execution block sample policy](security_iam_region_switch_rds.md "security_iam_region_switch_rds.md").

1. **Step name:** Enter a name.
2. **Step description (optional):** Enter a description of the step.
3. **Source DB instance ARN for Region:** Enter the
   database instance ARN for the source database in each Region in the plan. The execution block uses the
   identifier from the Region being activated as the source database for creating the cross-Region read replica.
4. **Replica DB instance ARN:** Enter the instance ARN to use
   for the new read replica.
5. **Timeout:** Enter a timeout value.

Then, choose **Save step.**

## How it works

By configuring an Amazon RDS Create Cross-Region Replica execution block, you can create a read replica in the
other Region as part of your post-recovery process. This execution block is designed to run after a successful
failover to re-establish cross-Region replication.

This block can only be added to active/passive plans.

During the execution, the old primary instance will be renamed and tagged with _renamedByRegionSwitch_.
Then a new read replica instance will be created with the following settings copied from the old primary:

- Instance identifier
- DB parameter groups
- DB subnet groups
- KMS key
- VPC security groups
- Option groups
- Multi-AZ configuration
- Domain authentication secret ARN

###### Important

The renamed primary instance remains running and continues to incur charges. Region switch tags it with _renamedByRegionSwitch_ for identification,
but does not otherwise modify or delete it. You are responsible for managing the renamed instance,
including deciding whether to keep it running, stop it, or delete it based on your operational and cost requirements.

###### Note

This execution block is designed for post-recovery workflows and requires the source Region to be
healthy and accessible. It should be used after a successful failover to re-establish cross-Region replication.

## What is evaluated as part of plan evaluation

When Region switch evaluates your plan, Region switch performs several checks on your Amazon RDS execution block configuration
and permissions. Region switch verifies that the following is correct:

- The database instance ARNs in the configuration are valid and properly formatted.
- The source database instances exist in their respective Regions.
- The source database instances are in an available state.

Region switch also validates that the plan's IAM role has the required permissions for creating Amazon RDS read replicas.
For more information about the required permissions for Region switch execution
blocks, see [Identity-based policy examples for Region switch in ARC](security_iam_id-based-policy-examples-region-switch.md "security_iam_id-based-policy-examples-region-switch.md").

The correct IAM permissions are essential for the proper functioning of the Amazon RDS execution block. If
any of these validations fail, Region switch returns warnings that there are issues, and provides specific error messages to help
you resolve the permissions or configuration issues. This ensures that your plan has the necessary access to manage
and interact with Amazon RDS during when this step runs during a plan execution.
