# Amazon RDS Create Cross-Region Replica execution block

The Amazon RDS Create Cross-Region Replica execution block allows you to create a cross-Region read replica
for an Amazon RDS database instance as part of your post-recovery process. This execution block is typically used
after promoting a read replica to re-establish cross-Region replication, ensuring your application is prepared
for future regional events.

## Configuration

To configure an Amazon RDS Create Cross-Region Replica execution block, enter the following values.

###### Important

Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place.
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
- Domain authentication secret ARN

###### Important

The renamed primary instance remains running and continues to incur charges. Region switch tags it with _renamedByRegionSwitch_ for identification,
but does not otherwise modify or delete it. You are responsible for managing the renamed instance,
including deciding whether to keep it running, stop it, or delete it based on your operational and cost requirements.

###### Note

This execution block is designed for post-recovery workflows and requires the source Region to be
healthy and accessible. It should be used after a successful failover to re-establish cross-Region replication.
