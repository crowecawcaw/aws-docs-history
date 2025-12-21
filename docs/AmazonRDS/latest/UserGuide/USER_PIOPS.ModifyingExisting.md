# Scaling up DB instance storage

You can scale up the storage of an existing DB instance by increasing the allocated storage for
the primary volume. When you increase the allocated storage, you must increase it by
at least 10 percent. If you try to increase the value by less than 10 percent, you
get an error. You can't reduce the amount of storage on a volume after you have
allocated storage for it.

###### Note

For RDS for SQL Server DB instances, you can scale storage for only the General Purpose SSD and Provisioned
IOPS SSD storage types.

To monitor the amount of free storage for your DB instance so you can respond when
necessary, we recommend that you create an Amazon CloudWatch alarm. For more information on
setting CloudWatch alarms, see [Using CloudWatch alarms](../../../AmazonCloudWatch/latest/DeveloperGuide/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/DeveloperGuide/AlarmThatSendsEmail.md").

Scaling storage usually doesn't cause any outage or performance degradation of the
DB instance. After you modify the storage size for a DB instance, the status of the DB instance is
**storage-optimization**.

Storage optimization can take several hours. You can't make further storage
modifications for either six (6) hours or until storage optimization has completed
on the instance, whichever is longer. You can view the storage optimization progress
in the AWS Management Console or by using the [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md")
AWS CLI command.

###### To increase storage for a DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose
   **Databases**.
3. Choose the DB instance that you want to modify.
4. Choose **Modify**.
5. Enter a new value for **Allocated storage**. It
   must be at least 10% greater than the current value.

![Modify the amount of storage for a DB instance](images/scale-gs2.png) 6. Choose **Continue**. 7. Choose **Apply immediately** in the
**Scheduling of modifications** section to
apply the storage changes to the DB instance immediately.

Or choose **Apply during the next scheduled maintenance
window** to apply the changes during the next
maintenance window. 8. When the settings are as you want them, choose **Modify DB
instance**.
To increase the storage for a DB instance, use the AWS CLI command [`modify-db-instance`](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md"). Set the following
parameters:

- `--allocated-storage` – Amount of storage to be
  allocated for the DB instance, in gibibytes.
- `--apply-immediately` – Use
  `--apply-immediately` to apply the storage changes
  immediately.

Or use `--no-apply-immediately` (the default) to apply
the changes during the next maintenance window. An immediate outage
occurs when the changes are applied.
The following example scales up the storage for `mydbinstance`
to 1,000 GiB and applies the change immediately. The command also migrates
the storage volume to gp3 and sets the provisioned IOPS to 6000.

```
aws rds modify-db-instance \
    --db-instance-identifier mydbinstance \
    --allocated-storage 1000 \
    --storage-type gp3 \
    --iops 6000 \
    --apply-immediately
```

For more information about storage, see [Amazon RDS DB instance storage](CHAP_Storage.md "CHAP_Storage.md").

To increase storage for a DB instance, use the Amazon RDS API operation [`ModifyDBInstance`](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md"). Set the following
parameters:

- `AllocatedStorage` – Amount of storage to be
  allocated for the DB instance, in gibibytes.
- `ApplyImmediately` – Set this option to
  `True` to apply the storage changes immediately. Set
  this option to `False` (the default) to apply the changes
  during the next maintenance window. An immediate outage occurs when
  the changes are applied.
  For more information about storage, see [Amazon RDS DB instance storage](CHAP_Storage.md "CHAP_Storage.md").
