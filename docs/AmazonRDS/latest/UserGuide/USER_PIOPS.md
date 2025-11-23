# Managing capacity automatically with Amazon RDS storage autoscaling

If your workload is unpredictable, you can enable storage autoscaling for an Amazon RDS DB instance. To
do so, you can use the Amazon RDS console, the Amazon RDS API, or the AWS CLI.

For
example, you might use this feature for a new mobile gaming application that users are
adopting rapidly. In this case, a rapidly increasing workload might exceed the available
database storage. To avoid having to manually scale up database storage, you can use
Amazon RDS storage autoscaling.

With storage autoscaling enabled, when Amazon RDS detects that you are running out of free
database space it automatically scales up your storage. Amazon RDS starts a storage
modification for an autoscaling-enabled DB instance when these factors apply:

- Free available space is less than or equal to 10 percent of the allocated storage.
- The low-storage condition lasts at least five minutes.
- At least six hours have passed since the last storage modification, or storage optimization has completed on the instance,
  whichever is longer.
  The additional storage is in increments of whichever of the following is greater:

- 10 GiB
- 10 percent of currently allocated storage
- Predicted storage growth exceeding the current allocated storage size in the next 7 hours based on the `FreeStorageSpace` metrics from the past hour. For more information on metrics, see [Monitoring with Amazon CloudWatch](MonitoringOverview.md#monitoring-cloudwatch "MonitoringOverview.md#monitoring-cloudwatch").
  The maximum storage threshold is the limit that you set for autoscaling the DB instance. It has the following constraints:

- You must set the maximum storage threshold to at least 10% more than the current allocated storage. We recommend setting
  it to at least 26% more to avoid receiving an [event notification](USER_Events.md#RDS-EVENT-0225 "USER_Events.md#RDS-EVENT-0225") that the storage
  size is approaching the maximum storage threshold.

For example, if you have DB instance with 1000 GiB of allocated storage, then set the maximum storage threshold to at
least 1100 GiB. If you don't, you get an error such as **`Invalid max storage size for
 `engine_name``**. However, we recommend that you set the maximum storage
threshold to at least 1260 GiB to avoid the event notification.

- For a DB instance that uses Provisioned IOPS (io1 or io2 Block Express) storage, the ratio of IOPS to maximum storage
  threshold (in GiB) must be within a certain range. For more information, see [Provisioned IOPS SSD storage](CHAP_Storage.md#USER_PIOPS "CHAP_Storage.md#USER_PIOPS").
- You can't set the maximum storage threshold for autoscaling-enabled instances to a value greater than the maximum
  allocated storage for the database engine and DB instance class.

For example, SQL Server Standard Edition on db.m5.xlarge has a default allocated storage for the instance of 20 GiB
(the minimum) and a maximum allocated storage of 16,384 GiB. The default maximum storage threshold for autoscaling is
1,000 GiB. If you use this default, the instance doesn't autoscale above 1,000 GiB. This is true even though the
maximum allocated storage for the instance is 16,384 GiB.

###### Note

We recommend that you carefully choose the maximum storage threshold based on usage
patterns and customer needs. If there are any aberrations in the usage patterns, the
maximum storage threshold can prevent scaling storage to an unexpectedly high value
when autoscaling predicts a very high threshold. After a DB instance has been
autoscaled, its allocated storage can't be reduced.

###### Topics

- [Limitations of storage autoscaling](#autoscaling-limitations "#autoscaling-limitations")
- [Enabling storage autoscaling for a new DB instance](#USER_PIOPS.EnablingAutoscaling "#USER_PIOPS.EnablingAutoscaling")
- [Changing the storage autoscaling settings for a DB instance](#USER_PIOPS.ModifyingAutoscaling "#USER_PIOPS.ModifyingAutoscaling")
- [Manually scaling your DB instance down or in](#USER_PIOPS.ScalingDown "#USER_PIOPS.ScalingDown")
- [Turning off storage autoscaling for a DB
  instance](#USER_PIOPS.DisablingAutoscaling "#USER_PIOPS.DisablingAutoscaling")

## Limitations of storage autoscaling

The following limitations apply to storage autoscaling:

- Autoscaling doesn't occur if the maximum storage threshold would be
  exceeded by the storage increment.
- When autoscaling, RDS predicts the storage size for subsequent autoscaling operations. If a subsequent operation
  is predicted to exceed the maximum storage threshold, then RDS autoscales to the maximum storage threshold.
- Autoscaling can't completely prevent storage-full situations for large data loads. This is because further
  storage modifications can't be made for either six (6) hours or until storage optimization has completed on the
  instance, whichever is longer.

If you perform a large data load, and autoscaling doesn't provide
enough space, the database might remain in the storage-full state for
several hours. This can harm the database.

- If you start a storage scaling operation at the same time that Amazon RDS starts an autoscaling operation, your storage
  modification takes precedence. The autoscaling operation is canceled.
- Autoscaling can't decrease the allocated storage. You can't reduce the amount of storage for a DB instance
  after storage has been allocated.
- Autoscaling can't be used with magnetic storage.
- Autoscaling can't be used with the following previous-generation instance classes that have less than 6 TiB
  of orderable storage: db.m3.large, db.m3.xlarge, and db.m3.2xlarge.
- Autoscaling operations aren't logged by AWS CloudTrail. For more information on CloudTrail, see [Monitoring Amazon RDS API calls in AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

Although automatic scaling helps you to increase storage on your Amazon RDS DB instance dynamically, you should still configure
the initial storage for your DB instance to an appropriate size for your typical workload.

## Enabling storage autoscaling for a new DB instance

When you create a new Amazon RDS DB instance, you can choose whether to enable storage autoscaling. You can also set an upper limit
on the storage that Amazon RDS can allocate for the DB instance.

Enabling storage autoscaling doesn't require a database reboot and doesn't cause any downtime. The feature takes effect immediately without disrupting database operations.

###### Note

When you clone an Amazon RDS DB instance that has storage autoscaling enabled, that setting isn't automatically
inherited by the cloned instance. The new DB instance has the same amount of allocated storage as the original instance.
You can turn storage autoscaling on again for the new instance if the cloned instance continues to increase its storage
requirements.

###### To enable storage autoscaling for a new DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the upper-right corner of the Amazon RDS console, choose the AWS Region where you want
   to create the DB instance.
3. In the navigation pane, choose **Databases**.
4. Choose **Create database**. On the **Select engine**
   page, choose your database engine and specify your DB instance
   information as described in [Getting started with Amazon RDS](CHAP_GettingStarted.md "CHAP_GettingStarted.md").
5. In the **Storage autoscaling** section, set the **Maximum
   storage threshold** value for the DB instance.
6. Specify the rest of your DB instance information as described in [Getting started with Amazon RDS](CHAP_GettingStarted.md "CHAP_GettingStarted.md").
   To enable storage autoscaling for a new DB instance, use the AWS CLI command [`create-db-instance`](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md"). Set the following parameter:

- `--max-allocated-storage` – Turns on storage autoscaling and sets the upper limit on storage size, in gibibytes.
  To verify that Amazon RDS storage autoscaling is available for your DB
  instance, use the AWS CLI
  [`describe-valid-db-instance-modifications`](../../../cli/latest/reference/rds/describe-valid-db-instance-modifications.md "../../../cli/latest/reference/rds/describe-valid-db-instance-modifications.md")
  command. To check based on the instance class before creating an instance, use the
  [`describe-orderable-db-instance-options`](../../../cli/latest/reference/rds/describe-orderable-db-instance-options.md "../../../cli/latest/reference/rds/describe-orderable-db-instance-options.md")
  command. Check the following field in the return value:

- `SupportsStorageAutoscaling` – Indicates whether
  the DB instance or instance class supports storage autoscaling.
  For more information about storage, see [Amazon RDS DB instance storage](CHAP_Storage.md "CHAP_Storage.md").

To enable storage autoscaling for a new DB instance, use the Amazon RDS API operation [`CreateDBInstance`](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md"). Set the following parameter:

- `MaxAllocatedStorage` – Turns on Amazon RDS storage
  autoscaling and sets the upper limit on storage size, in gibibytes.
  To verify that Amazon RDS storage autoscaling is available for your DB
  instance, use the Amazon RDS API
  [`DescribeValidDbInstanceModifications`](../APIReference/API_DescribeValidDbInstanceModifications.md "../APIReference/API_DescribeValidDbInstanceModifications.md")
  operation for an existing instance, or the
  [`DescribeOrderableDBInstanceOptions`](../APIReference/API_DescribeOrderableDBInstanceOptions.md "../APIReference/API_DescribeOrderableDBInstanceOptions.md")
  operation before creating an instance. Check the following field in the return value:

- `SupportsStorageAutoscaling` – Indicates whether
  the DB instance supports storage autoscaling.
  For more information about storage, see [Amazon RDS DB instance storage](CHAP_Storage.md "CHAP_Storage.md").

## Changing the storage autoscaling settings for a DB instance

You can turn storage autoscaling on for an existing Amazon RDS DB instance. You can also change
the upper limit on the storage that Amazon RDS can allocate for the DB instance.

Changing storage autoscaling settings doesn't require a database reboot and doesn't cause any downtime. The changes take effect immediately without disrupting database operations.

###### To change the storage autoscaling settings for a DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose
   **Databases**.
3. Choose the DB instance that you want to modify, and choose **Modify**.
   The **Modify DB instance** page appears.
4. Change the storage limit in the **Autoscaling**
   section. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
5. When all the changes are as you want them, choose **Continue** and
   check your modifications.
6. On the confirmation page, review your changes. If they're correct, choose
   **Modify DB instance** to save your changes. If
   they aren't correct, choose **Back** to edit
   your changes or **Cancel** to cancel your
   changes.

Changing the storage autoscaling limit occurs immediately. This
setting ignores the **Apply immediately**
setting.
To change the storage autoscaling settings for a DB instance, use the AWS CLI command
[`modify-db-instance`](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md"). Set the following
parameter:

- `--max-allocated-storage` – Sets the upper limit on storage size, in gibibytes.
  If the value is greater than the `--allocated-storage` parameter, storage autoscaling
  is turned on. If the value is the same as the `--allocated-storage` parameter,
  storage autoscaling is turned off.
  To verify that Amazon RDS storage autoscaling is available for your DB
  instance, use the AWS CLI
  [`describe-valid-db-instance-modifications`](../../../cli/latest/reference/rds/describe-valid-db-instance-modifications.md "../../../cli/latest/reference/rds/describe-valid-db-instance-modifications.md")
  command. To check based on the instance class before creating an instance, use the
  [`describe-orderable-db-instance-options`](../../../cli/latest/reference/rds/describe-orderable-db-instance-options.md "../../../cli/latest/reference/rds/describe-orderable-db-instance-options.md")
  command. Check the following field in the return value:

- `SupportsStorageAutoscaling` – Indicates whether
  the DB instance supports storage autoscaling.
  For more information about storage, see [Amazon RDS DB instance storage](CHAP_Storage.md "CHAP_Storage.md").

To change the storage autoscaling settings for a DB instance, use the Amazon RDS API
operation [`ModifyDBInstance`](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md"). Set the following parameter:

- `MaxAllocatedStorage` – Sets the upper limit on
  storage size, in gibibytes.
  To verify that Amazon RDS storage autoscaling is available for your DB instance, use the
  Amazon RDS API [`DescribeValidDbInstanceModifications`](../APIReference/API_DescribeValidDbInstanceModifications.md "../APIReference/API_DescribeValidDbInstanceModifications.md") operation
  for an existing instance, or the [`DescribeOrderableDBInstanceOptions`](../APIReference/API_DescribeOrderableDBInstanceOptions.md "../APIReference/API_DescribeOrderableDBInstanceOptions.md") operation
  before creating an instance. Check the following field in the return value:

- `SupportsStorageAutoscaling` – Indicates whether
  the DB instance supports storage autoscaling.
  For more information about storage, see [Amazon RDS DB instance storage](CHAP_Storage.md "CHAP_Storage.md").

## Manually scaling your DB instance down or in

Amazon RDS provides storage autoscaling to meet growing demand. However, there are limitations
regarding scaling down and in:

- **RDS storage** – While RDS supports automatic
  scaling up of storage as demand increases, it doesn't automatically scale
  down.
- **Read replicas** – RDS doesn't support automatic
  scaling out (adding) or scaling in (deleting) of read replicas. You must
  manually add or remove read replicas according to your load
  requirements.

To scale down your RDS resources, perform the following manual actions:

- For storage, you can't manually reduce the allocated storage of a DB instance using the
  `modify-db-instance` command. Instead, choose one of the
  following techniques:
  - Use a blue/green deployment if your DB engine supports it. Create
    a green database with a lower storage size, and then promote your
    green database to be your blue database. For more information, see
    [Modify storage and performance
    settings](blue-green-deployments-creating.md#blue-green-deployments-resize "blue-green-deployments-creating.md#blue-green-deployments-resize").
  - Create a new DB instance with lower allocated storage, manually
    migrate the data from your current database to the newly created
    database instance, and switch your database endpoints.

- For read replicas, manually delete any unused replicas through the RDS console or
  AWS CLI.

## Turning off storage autoscaling for a DB

instance

If you no longer need Amazon RDS to automatically increase the storage for an Amazon RDS DB
instance, you can turn off storage autoscaling. After you do, you can still manually
increase the amount of storage for your DB instance.

###### To turn off storage autoscaling for a DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose
   **Databases**.
3. Choose the DB instance that you want to modify and choose
   **Modify**. The **Modify DB
   instance** page appears.
4. Clear the **Enable storage autoscaling** check box in the
   **Storage autoscaling** section. For more
   information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
5. When all the changes are as you want them, choose **Continue** and
   check the modifications.
6. On the confirmation page, review your changes. If they're
   correct, choose **Modify DB instance** to save your
   changes. If they aren't correct, choose
   **Back** to edit your changes or
   **Cancel** to cancel your changes.
   Changing the storage autoscaling limit occurs immediately. This setting ignores the **Apply immediately**
   setting.

To turn off storage autoscaling for a DB instance, use the AWS CLI command [`modify-db-instance`](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md")
and the following parameter:

- `--max-allocated-storage` – Specify a value equal to the
  `--allocated-storage` setting to
  prevent further Amazon RDS storage autoscaling for the specified DB instance.
  For more information about storage, see [Amazon RDS DB instance storage](CHAP_Storage.md "CHAP_Storage.md").

To turn off storage autoscaling for a DB instance, use the Amazon RDS API operation [`ModifyDBInstance`](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md"). Set the following
parameter:

- `MaxAllocatedStorage` – Specify a value equal to the
  `AllocatedStorage` setting to
  prevent further Amazon RDS storage autoscaling for the specified DB instance.

For more information about storage, see [Amazon RDS DB instance storage](CHAP_Storage.md "CHAP_Storage.md").
