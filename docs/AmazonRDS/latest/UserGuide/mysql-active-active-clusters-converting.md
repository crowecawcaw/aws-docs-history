# Converting an existing DB instance to an active-active cluster

The DB engine version of the DB instance you want to migrate to an active-active
cluster must be one of the following versions:

- All MySQL 8.4 versions
- MySQL 8.0.35 and higher minor versions
  If you need to upgrade the engine version, see [Upgrades of the RDS for MySQL DB engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").

If you are setting up an active-active cluster with DB instances in more than one VPC, make sure you complete the
prerequisites in [Preparing for a
cross-VPC active-active cluster](mysql-active-active-clusters-cross-vpc-prerequisites.md "mysql-active-active-clusters-cross-vpc-prerequisites.md").

Complete the following steps to migrate an existing DB instance to an active-active cluster for RDS for MySQL.

###### Topics

- [Step 1: Set the active-active cluster parameters
  in one or more custom parameter groups](#mysql-active-active-clusters-converting-parameter-group "#mysql-active-active-clusters-converting-parameter-group")
- [Step 2: Associate the DB instance with a DB parameter group that has the
  required Group Replication parameters set](#mysql-active-active-clusters-converting-associate-parameter-group "#mysql-active-active-clusters-converting-associate-parameter-group")
- [Step 3: Create the active-active cluster](#mysql-active-active-clusters-converting-associate-parameter-groups "#mysql-active-active-clusters-converting-associate-parameter-groups")
- [Step 4: Create additional RDS for MySQL DB instances
  for the active-active cluster](#mysql-active-active-clusters-converting-add-db-instances "#mysql-active-active-clusters-converting-add-db-instances")
- [Step 5: Initialize the group on the DB instance
  you are converting](#mysql-active-active-clusters-converting-start-replication-first "#mysql-active-active-clusters-converting-start-replication-first")
- [Step 6: Start replication on the other DB instances
  in the active-active cluster](#mysql-active-active-clusters-converting-start-replication-other "#mysql-active-active-clusters-converting-start-replication-other")
- [Step 7: (Recommended)
  Check the status of the active-active cluster](#mysql-active-active-clusters-converting-view "#mysql-active-active-clusters-converting-view")

## Step 1: Set the active-active cluster parameters

in one or more custom parameter groups

The RDS for MySQL DB instances in an active-active cluster must be associated with a custom parameter group that has the
correct setting for required parameters. For information about the parameters and the required setting for each one,
see [Required parameter settings for active-active clusters](mysql-active-active-clusters-parameters.md "mysql-active-active-clusters-parameters.md").

You can set these parameters in new parameter groups or in existing parameter
groups. However, to avoid accidentally affecting DB instances that aren't part of
the active-active cluster, we strongly recommend that you create a new custom
parameter group. The DB instances in an active-active cluster can be associated with
the same DB parameter group or with different DB parameter groups.

You can use the AWS Management Console or the AWS CLI to create a new custom parameter group. For
more information, see [Creating a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). The following example
runs the [create-db-parameter-group](../../../cli/latest/reference/rds/create-db-parameter-group.md "../../../cli/latest/reference/rds/create-db-parameter-group.md") AWS CLI command to create a custom DB parameter
group named `myactivepg` for RDS for MySQL
8.0:

For Linux, macOS, or Unix:

```
aws rds create-db-parameter-group \
  --db-parameter-group-name `myactivepg` \
  --db-parameter-group-family mysql8.0 \
  --description "`Parameter group for active-active clusters`"
```

For Windows:

```
aws rds create-db-parameter-group ^
  --db-parameter-group-name `myactivepg` ^
  --db-parameter-group-family mysql8.0 ^
  --description "`Parameter group for active-active clusters`"
```

You can also use the AWS Management Console or the AWS CLI to set the parameters in the custom
parameter group. For more information, see [Modifying parameters in a DB parameter group
in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

The following example runs the [modify-db-parameter-group](../../../cli/latest/reference/rds/modify-db-parameter-group.md "../../../cli/latest/reference/rds/modify-db-parameter-group.md") AWS CLI command to set the parameters for
RDS for MySQL 8.0. To use this example with RDS for MySQL 8.4, change
`slave_preserve_commit_order` to
`replica_preserve_commit_order`.

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group \
  --db-parameter-group-name `myactivepg` \
  --parameters "ParameterName='rds.group_replication_enabled',ParameterValue='1',ApplyMethod=pending-reboot" \
               "ParameterName='rds.custom_dns_resolution',ParameterValue='1',ApplyMethod=pending-reboot" \
               "ParameterName='enforce_gtid_consistency',ParameterValue='ON',ApplyMethod=pending-reboot" \
               "ParameterName='gtid-mode',ParameterValue='ON',ApplyMethod=pending-reboot" \
               "ParameterName='binlog_format',ParameterValue='ROW',ApplyMethod=immediate" \
               "ParameterName='slave_preserve_commit_order',ParameterValue='ON',ApplyMethod=immediate" \
               "ParameterName='group_replication_group_name',ParameterValue='`11111111-2222-3333-4444-555555555555`',ApplyMethod=pending-reboot"
```

For Windows:

```
aws rds modify-db-parameter-group ^
  --db-parameter-group-name myactivepg ^
  --parameters "ParameterName='rds.group_replication_enabled',ParameterValue='1',ApplyMethod=pending-reboot" ^
               "ParameterName='rds.custom_dns_resolution',ParameterValue='1',ApplyMethod=pending-reboot" ^
               "ParameterName='enforce_gtid_consistency',ParameterValue='ON',ApplyMethod=pending-reboot" ^
               "ParameterName='gtid-mode',ParameterValue='ON',ApplyMethod=pending-reboot" ^
               "ParameterName='binlog_format',ParameterValue='ROW',ApplyMethod=immediate" ^
               "ParameterName='slave_preserve_commit_order',ParameterValue='ON',ApplyMethod=immediate" ^
               "ParameterName='group_replication_group_name',ParameterValue='`11111111-2222-3333-4444-555555555555`',ApplyMethod=pending-reboot"
```

## Step 2: Associate the DB instance with a DB parameter group that has the

required Group Replication parameters set

Associate the DB instance with a parameter group you created or modified in the previous step.
For instructions, see [Associating a DB parameter group with a
DB instance in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

Reboot the DB instance for the new parameter settings to take effect. For instructions, see
[Rebooting a DB instance](USER_RebootInstance.md "USER_RebootInstance.md").

## Step 3: Create the active-active cluster

In the DB parameter group associated with the DB instance, set the `group_replication_group_seeds` parameter
to the endpoint of the DB instance you are converting.

You can use the AWS Management Console or the AWS CLI to set the parameter. You don't need to reboot the DB instance after setting this
parameter. For more information about setting parameters, see [Modifying parameters in a DB parameter group
in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

The following example runs the [modify-db-parameter-group](../../../cli/latest/reference/rds/modify-db-parameter-group.md "../../../cli/latest/reference/rds/modify-db-parameter-group.md")
AWS CLI command to set the parameters:

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group \
  --db-parameter-group-name `myactivepg` \
  --parameters "ParameterName='group_replication_group_seeds',ParameterValue='`myactivedb1.123456789012.us-east-1.rds.amazonaws.com:3306`',ApplyMethod=immediate"
```

For Windows:

```
aws rds modify-db-parameter-group ^
  --db-parameter-group-name `myactivepg` ^
  --parameters "ParameterName='group_replication_group_seeds',ParameterValue='`myactivedb1.123456789012.us-east-1.rds.amazonaws.com:3306`',ApplyMethod=immediate"
```

## Step 4: Create additional RDS for MySQL DB instances

for the active-active cluster

To create additional DB instances for the active-active cluster, perform point-in-time recovery on the DB instance
you are converting. For instructions, see [Adding a DB instance to an active-active cluster using point-in-time recovery](mysql-active-active-clusters-adding.md#mysql-active-active-clusters-adding-pitr "mysql-active-active-clusters-adding.md#mysql-active-active-clusters-adding-pitr").

An active-active cluster can have up to nine DB instances. Perform point-in-time
recovery on the DB instance until you have the number of DB instances you want for
the cluster. When you perform point-in-recovery, make sure you associate the DB
instance you are adding with a DB parameter group that has
`rds.group_replication_enabled` set to `1`. Otherwise,
Group Replication won't start on the newly added DB instance.

## Step 5: Initialize the group on the DB instance

you are converting

Initialize the group and start replication:

1. Connect to that DB instance you are converting in a SQL client. For more information about connecting to
   an RDS for MySQL DB instance, see [Connecting to your MySQL DB instance](USER_ConnectToInstance.md "USER_ConnectToInstance.md").
2. In the SQL client, run the following stored procedures and replace
   `group_replication_user_password` with the
   password for the `rdsgrprepladmin` user. The
   `rdsgrprepladmin` user is reserved for Group Replication
   connections in an active-active cluster. The password for this user must be
   the same on all of the DB instances in an active-active cluster.

```
call mysql.rds_set_configuration('binlog retention hours', `168`); -- 7 days binlog
call mysql.rds_group_replication_create_user('`group_replication_user_password`');
call mysql.rds_group_replication_set_recovery_channel('`group_replication_user_password`');
call mysql.rds_group_replication_start(1);
```

This example sets the `binlog retention hours` value to `168`, which means that binary log files
are retained for seven days on the DB instance. You can adjust this value to meet your requirements.

This example specifies `1` in the `mysql.rds_group_replication_start` stored procedure to
initialize a new group with the current DB instance.

For more information about the stored procedures called in the example, see [Managing active-active clusters](mysql-stored-proc-active-active-clusters.md "mysql-stored-proc-active-active-clusters.md").

## Step 6: Start replication on the other DB instances

in the active-active cluster

For each of the DB instances in the active-active cluster, use a SQL client to
connect to the instance, and run the following stored procedures. Replace
`group_replication_user_password` with the password for
the `rdsgrprepladmin` user.

```
call mysql.rds_set_configuration('binlog retention hours', `168`); -- 7 days binlog
call mysql.rds_group_replication_create_user('`group_replication_user_password`');
call mysql.rds_group_replication_set_recovery_channel('`group_replication_user_password`');
call mysql.rds_group_replication_start(0);
```

This example sets the `binlog retention hours` value to `168`, which means that binary log files
are retained for seven days on each DB instance. You can adjust this value to meet your requirements.

This example specifies `0` in the `mysql.rds_group_replication_start` stored procedure to
join the current DB instance to an existing group.

###### Tip

Make sure you run these stored procedures on all of the other DB instances in the active-active cluster.

## Step 7: (Recommended)

Check the status of the active-active cluster

To make sure each member of the cluster is configured correctly, check the status
of the cluster by connecting to a DB instance in the active-active cluster, and
running the following SQL command:

```
SELECT * FROM performance_schema.replication_group_members;
```

Your output should show `ONLINE` for the `MEMBER_STATE` of each DB instance, as in the
following sample output:

```
+---------------------------+--------------------------------------+----------------+-------------+--------------+-------------+----------------+----------------------------+
| CHANNEL_NAME              | MEMBER_ID                            | MEMBER_HOST    | MEMBER_PORT | MEMBER_STATE | MEMBER_ROLE | MEMBER_VERSION | MEMBER_COMMUNICATION_STACK |
+---------------------------+--------------------------------------+----------------+-------------+--------------+-------------+----------------+----------------------------+
| group_replication_applier | 9854d4a2-5d7f-11ee-b8ec-0ec88c43c251 | ip-10-15-3-137 |        3306 | ONLINE       | PRIMARY     | 8.0.35         | MySQL                      |
| group_replication_applier | 9e2e9c28-5d7f-11ee-8039-0e5d58f05fef | ip-10-15-3-225 |        3306 | ONLINE       | PRIMARY     | 8.0.35         | MySQL                      |
| group_replication_applier | a6ba332d-5d7f-11ee-a025-0a5c6971197d | ip-10-15-1-83  |        3306 | ONLINE       | PRIMARY     | 8.0.35         | MySQL                      |
+---------------------------+--------------------------------------+----------------+-------------+--------------+-------------+----------------+----------------------------+
3 rows in set (0.00 sec)
```

For information about the possible `MEMBER_STATE` values, see [Group Replication Server States](https://dev.mysql.com/doc/refman/8.0/en/group-replication-server-states.html "https://dev.mysql.com/doc/refman/8.0/en/group-replication-server-states.html") in the MySQL documentation.
