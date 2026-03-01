# Setting up an active-active cluster with new DB instances

Complete the following steps to set up an active-active cluster using new
Amazon RDS for MySQL DB instances.

If you are setting up an active-active cluster with DB instances in more than one VPC, make sure you complete the
prerequisites in [Preparing for a cross-VPC active-active cluster](mysql-active-active-clusters-cross-vpc-prerequisites.md "mysql-active-active-clusters-cross-vpc-prerequisites.md").

###### Topics

- [Step 1: Set the active-active cluster parameters in one or more custom parameter groups](#mysql-active-active-clusters-setting-up-parameter-group "#mysql-active-active-clusters-setting-up-parameter-group")
- [Step 2: Create new RDS for MySQL DB instances for the active-active cluster](#mysql-active-active-clusters-setting-up-db-instances "#mysql-active-active-clusters-setting-up-db-instances")
- [Step 3: Specify the DB instances in the active-active cluster](#mysql-active-active-clusters-setting-up-associate-parameter-groups "#mysql-active-active-clusters-setting-up-associate-parameter-groups")
- [Step 4: Initialize the group on a DB instance and start replication](#mysql-active-active-clusters-setting-up-start-replication-first "#mysql-active-active-clusters-setting-up-start-replication-first")
- [Step 5: Start replication on the other DB instances in the active-active cluster](#mysql-active-active-clusters-setting-up-start-replication-other "#mysql-active-active-clusters-setting-up-start-replication-other")
- [Step 6: (Recommended) Check the status of the active-active cluster](#mysql-active-active-clusters-setting-up-view "#mysql-active-active-clusters-setting-up-view")
- [Step 7: (Optional) Import data into a DB instance in the active-active cluster](#mysql-active-active-clusters-import "#mysql-active-active-clusters-import")

## Step 1: Set the active-active cluster parameters in one or more custom parameter groups

The RDS for MySQL DB instances in an active-active cluster must be associated with a custom parameter group that has the
correct setting for required parameters. For information about the parameters and the required setting for each one,
see [Required parameter settings for active-active clusters](mysql-active-active-clusters-parameters.md "mysql-active-active-clusters-parameters.md").

You can set these parameters in new parameter groups or in existing parameter groups. However, to avoid accidentally affecting
DB instances that aren't part of the active-active cluster, we strongly recommend that you create a new custom
parameter group. The DB instances in an active-active cluster can be associated with the same DB parameter group or with
different DB parameter groups.

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
parameter group. For more information, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

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

## Step 2: Create new RDS for MySQL DB instances for the active-active cluster

Active-active clusters are supported for the following versions of RDS for MySQL DB
instances:

- All MySQL version 8.4 versions
- MySQL version 8.0.35 and higher minor versions

You can create up to nine new DB instances for the cluster.

You can use the AWS Management Console or the AWS CLI to create new DB instances. For more information about creating a DB
instance, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md"). When you create
the DB instance, associate it with a DB parameter group that you created or modified in the previous step.

## Step 3: Specify the DB instances in the active-active cluster

In the DB parameter group associated with each DB instance, set the `group_replication_group_seeds` parameter
to the endpoints of the DB instances you want to include in the cluster.

You can use the AWS Management Console or the AWS CLI to set the parameter. You don't need to reboot the DB instance after setting this
parameter. For more information about setting parameters, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

The following example runs the [modify-db-parameter-group](../../../cli/latest/reference/rds/modify-db-parameter-group.md "../../../cli/latest/reference/rds/modify-db-parameter-group.md")
AWS CLI command to set the parameters:

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group \
  --db-parameter-group-name `myactivepg` \
  --parameters "ParameterName='group_replication_group_seeds',ParameterValue='`myactivedb1.123456789012.us-east-1.rds.amazonaws.com:3306,myactivedb2.123456789012.us-east-1.rds.amazonaws.com:3306,myactivedb3.123456789012.us-east-1.rds.amazonaws.com:3306`',ApplyMethod=immediate"
```

For Windows:

```
aws rds modify-db-parameter-group ^
  --db-parameter-group-name `myactivepg` ^
  --parameters "ParameterName='group_replication_group_seeds',ParameterValue='`myactivedb1.123456789012.us-east-1.rds.amazonaws.com:3306,myactivedb2.123456789012.us-east-1.rds.amazonaws.com:3306,myactivedb3.123456789012.us-east-1.rds.amazonaws.com:3306`',ApplyMethod=immediate"
```

###### Tip

Make sure you set the `group_replication_group_seeds` parameter in each DB parameter group that is
associated with a DB instance in the active-active cluster.

## Step 4: Initialize the group on a DB instance and start replication

You can choose any new DB to initialize the group and start replication. To do so, complete the following steps:

1. Choose a DB instance in the active-active cluster, and connect to that DB instance in a SQL client.
   For more information about connecting to an RDS for MySQL DB instance, see [Connecting to your MySQL DB instance](USER_ConnectToInstance.md "USER_ConnectToInstance.md").
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

## Step 5: Start replication on the other DB instances in the active-active cluster

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

## Step 6: (Recommended) Check the status of the active-active cluster

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

## Step 7: (Optional) Import data into a DB instance in the active-active cluster

You can import data from a MySQL database into a DB instance in the active-active
cluster. After the data is imported, Group Replication replicates it to the other DB
instances in the cluster.

For information about importing data, see [Importing data to an Amazon RDS for MySQL database with reduced downtime](mysql-importing-data-reduced-downtime.md "mysql-importing-data-reduced-downtime.md").
