# Amazon Neptune parameter groups

You manage your database configuration in Amazon Neptune by using [parameters](parameters.md "parameters.md") in a parameter group. Parameter groups act as
a _container_ for engine configuration values that are applied to
one or more DB instances.

There are two types of parameter group, namely DB cluster parameter groups and
DB parameter groups:

- _DB parameter groups_ apply at the instance level
  and generally are associated with settings for the Neptune graph engine, such as
  the `neptune_query_timeout` parameter.
- _DB cluster parameter groups_ apply to every instance in
  the cluster and generally have broader settings. Every Neptune cluster is associated
  with a DB cluster parameter group. Every DB instance within that cluster inherits the
  engine configuration values contained in the DB cluster parameter group.
  Any configuration values that you modify in the DB cluster parameter group override
  default values in the DB parameter group. If you edit the corresponding values in the
  DB parameter group, those values override the settings in the DB cluster parameter group.

A default DB parameter group is used if you create a DB instance without specifying a custom
DB parameter group. You can't modify the parameter settings of the default DB parameter group.
Instead, to change the default parameter settings you must create a new DB parameter group.
Not all DB engine parameters can be changed in a DB parameter group that you create.

Parameter groups are created in families that are compatible with different
Neptune engine versions. The default parameter group family is `neptune1`,
which is compatible with all engine versions prior to `1.2.0.0`. Starting
with [Release: 1.2.0.0 (2022-07-21)](engine-releases-1.2.0.md "engine-releases-1.2.0.md"),
the `neptune1.2` parameter group family must be used instead. That means that
when you upgrade to `1.2.0.0` or higher, you must first recreate all your
custom parameter groups in the `neptune1.2` family so that you can attach them
when you upgrade.

Some Neptune parameters are static, and others are dynamic. The differences are
as follows:

**Static parameters**

- A static parameter is one that takes effect only after a DB instance
  is rebooted. In other words, when you change a static parameter and save the instance
  DB parameter group, you must manually reboot the DB instance for the parameter change
  to take effect. Currently, all the Neptune instance-level parameters (in a DB parameter
  group rather than a DB cluster parameter group) are static.
- When you change a cluster-level static parameter and save the DB
  cluster parameter group, the parameter change takes effect after you manually
  reboot every DB instance in the cluster.
  **Dynamic parameters**

- A dynamic parameter is one that takes effect almost immediately
  after the parameter is updated in its parameter group. In other words, there
  is no need to reboot a DB instance after updating a dynamic parameter for the
  parameter change to take effect.
- Expect some minor delay for a dynamic cluster parameter change
  to be applied across all DB instances.
- An updated dynamic parameter value is not applied
  to currently running requests, but only to ones submitted after the
  change took place.
- When you change a dynamic cluster-level parameter, by default
  the parameter change is applied to your DB cluster immediately, without
  requiring any reboot. To defer the parameter change until after the DB
  instances in the cluster are rebooted, you can use the AWS CLI to set
  the `ApplyMethod` to `pending-reboot` for the
  parameter change.
  Currently all parameters are static except for the following new
  cluster parameters:

- `neptune_enable_slow_query_log`   (cluster-level)
- `neptune_slow_query_log_threshold`   (cluster-level)
  Here are some important points you should know about working with parameters in a DB
  parameter group:

- Improperly setting parameters in a DB parameter group can have unintended adverse
  effects, including degraded performance and system instability. Always exercise caution when
  modifying database parameters, and back up your data before modifying a DB parameter group.
  Try out your parameter group setting changes on a test DB instance before applying those
  changes to a production DB instance.
- When you change the DB parameter group associated with a DB instance,
  you must manually reboot the instance before the new DB parameter group is used by
  the DB instance.

###### Note

Before [Release: 1.2.0.0 (2022-07-21)](engine-releases-1.2.0.md "engine-releases-1.2.0.md"),
all the read-replica instances in a DB cluster were automatically rebooted whenever the primary
(writer) instance restarted.

From [Release: 1.2.0.0 (2022-07-21)](engine-releases-1.2.0.md "engine-releases-1.2.0.md")
going forwards, restarting the primary instance does not cause any of the replica instances to restart.
This means that if you are changing a cluster-level parameter, you must restart each instance
separately to pick up the parameter change.

## Editing a DB Cluster Parameter Group or DB Parameter Group

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. Choose **Parameter groups** in the navigation pane.
3. Choose the **Name** link for the DB parameter group that you want to
   edit.

(Optional) Choose **Create parameter group** to create a new cluster
parameter group and create the new group. Then choose the **Name** of the
new parameter group.

###### Important

This step is _required_ if you only have the default DB cluster parameter
group because the default DB cluster parameter group can't be modified. 4. Search for the parameter and click on the **Value** field next to the
**Name** column. 5. Enter the allowed value and choose the check beside the value field. 6. Choose **Save changes**. 7. Reboot every DB instance in the Neptune cluster if you are changing a
DB cluster parameter, or one or more specific instances if you are changing a DB
instance parameter.

## Creating a DB parameter group or DB cluster

parameter group

You can easily use the Neptune console to create a new parameter group:

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. Choose **Parameter groups** in the left navigation pane.
3. Choose **Create DB parameter group**.

The **Create DB parameter group** page appears. 4. In the **Parameter group family** list, choose **neptune1**
or, if you are targeting engine version 1.2.0.0 or higher, choose **neptune1.2**. 5. In the **Type** list, choose **DB Parameter Group**
or **DB Cluster Parameter Group**. 6. In the **Group name** box, type the name of the new DB parameter
group. 7. In the **Description** box, type a description for the new DB
parameter group. 8. Choose **Create**.

You can also create a new parameter group using the AWS CLI:

```
aws neptune create-db-parameter-group \
  --db-parameter-group-name `(a name for the new DB parameter group)` \
  --db-parameter-group-family `(either neptune1 or neptune1.2, depending on the engine version)` \
  --description `(a description for the new DB parameter group)`
```
