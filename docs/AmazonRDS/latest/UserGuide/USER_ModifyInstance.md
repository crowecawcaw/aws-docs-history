# Using the schedule modifications

setting

When you modify your DB instance, you decide when you want the modifications to
occur.

![Schedule modifications either immediately or during the maintenance window.](images/schedule-modifications.png)
To apply changes immediately rather than in the next maintenance window, choose the
**Apply Immediately** option in the AWS Management Console. Or you
use the `--apply-immediately` parameter when calling the AWS CLI or set the
`ApplyImmediately` parameter to `true` when using the Amazon RDS
API.

If you don't choose to apply changes immediately, RDS puts the changes into the
pending modifications queue. During the next maintenance window, RDS applies any pending
changes in the queue. If you choose to apply changes immediately, your new changes and
any changes in the pending modifications queue are applied.

To see the modifications that are pending for the next maintenance window, use the [describe-db-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-instances.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-instances.html") AWS CLI command and check the `PendingModifiedValues` field.

###### Important

If any of the pending modifications require the DB instance to be temporarily unavailable (_downtime_),
choosing the apply immediately option can cause unexpected downtime.

When you choose to apply a change immediately, any pending modifications are also applied
immediately, instead of during the next maintenance window.

If you don't want a pending change to be applied in the next maintenance
window, you can modify the DB instance to revert the change. You can do this by
using the AWS CLI and specifying the `--apply-immediately` option.

Changes to some database settings are applied immediately,
even if you choose to defer your changes.
To see how the different database settings interact with the apply immediately setting,
see [Settings for DB instances](USER_ModifyInstance.md "USER_ModifyInstance.md").
