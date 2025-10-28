# Troubleshooting for

Amazon RDS

Use the following sections to help troubleshoot problems you have with DB instances in
Amazon RDS and Amazon Aurora.

###### Topics

- [Can't connect to Amazon RDS DB instance](#CHAP_Troubleshooting.Connecting "#CHAP_Troubleshooting.Connecting")
- [Amazon RDS security issues](#CHAP_Troubleshooting.Security "#CHAP_Troubleshooting.Security")
- [Troubleshooting
  incompatible-network state](#CHAP_Troubleshooting.IncompatibleNetworkMode "#CHAP_Troubleshooting.IncompatibleNetworkMode")
- [Resetting the DB instance owner
  password](#CHAP_Troubleshooting.ResetPassword "#CHAP_Troubleshooting.ResetPassword")
- [Amazon RDS DB instance outage or
  reboot](#CHAP_Troubleshooting.Reboots "#CHAP_Troubleshooting.Reboots")
- [Amazon RDS DB parameter changes not taking
  effect](#CHAP_Troubleshooting.Parameters "#CHAP_Troubleshooting.Parameters")
- [Amazon RDS DB instance running out of
  storage](#CHAP_Troubleshooting.Storage "#CHAP_Troubleshooting.Storage")
- [Amazon RDS insufficient DB instances available](#CHAP_Troubleshooting.Capacity "#CHAP_Troubleshooting.Capacity")
- [Freeable memory issues in Amazon RDS](#Troubleshooting.FreeableMemory "#Troubleshooting.FreeableMemory")
- [MySQL and MariaDB issues](#CHAP_Troubleshooting.MySQL "#CHAP_Troubleshooting.MySQL")
- [Can't set backup retention
  period to 0](#CHAP_Troubleshooting.Backup.Retention "#CHAP_Troubleshooting.Backup.Retention")
  For information about debugging problems using the Amazon RDS API, see [Troubleshooting applications on Amazon RDS](APITroubleshooting.md "APITroubleshooting.md").

## Can't connect to Amazon RDS DB instance

When you can't connect to a DB instance, the following are common causes:

- **Inbound rules** – The access rules
  enforced by your local firewall and the IP addresses authorized to access your
  DB instance might not match. The problem is most likely the inbound rules in
  your security group.

By default, DB instances don't allow access. Access is granted through a
security group associated with the VPC that allows traffic into and out of the
DB instance. If necessary, add inbound and outbound rules for your particular
situation to the security group. You can specify an IP address, a range of IP
addresses, or another VPC security group.

###### Note

When adding a new inbound rule, you can choose **My IP**
for **Source** to allow access to the DB instance from the
IP address detected in your browser.

For more information about setting up security groups,
see [Provide access to your DB instance in your VPC by
creating a security group](CHAP_SettingUp.md#CHAP_SettingUp.SecurityGroup "CHAP_SettingUp.md#CHAP_SettingUp.SecurityGroup").

###### Note

Client connections from IP addresses within the range 169.254.0.0/16
aren't permitted. This is the Automatic Private IP Addressing Range
(APIPA), which is used for local-link addressing.

- **Public accessibility** – To connect to
  your DB instance from outside of the VPC, such as by using a client application,
  the instance must have a public IP address assigned to it.

To make the instance publicly accessible, modify it and choose
**Yes** under **Public accessibility**.
For more information, see [Hiding a DB instance in a VPC from
the internet](USER_VPC.md#USER_VPC.Hiding "USER_VPC.md#USER_VPC.Hiding").

- **Port** – The port that you specified when you
  created the DB instance can't be used to send or receive communications
  because of your local firewall restrictions. To determine if your network allows
  the specified port to be used for inbound and outbound communication, check with
  your network administrator.
- **Availability** – For a newly created DB
  instance, the DB instance has a status of `creating` until the DB
  instance is ready to use. When the state changes to `available`, you
  can connect to the DB instance. Depending on the size of your DB instance, it
  can take up to 20 minutes before an instance is available.
- **Internet gateway** – For a DB instance
  to be publicly accessible, the subnets in its DB subnet group must have an
  internet gateway.

###### To configure an internet gateway for a subnet

    1. Sign in to the AWS Management Console and open the Amazon RDS console at
     [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
    2. In the navigation pane, choose **Databases**, and
     then choose the name of the DB instance.
    3. In the **Connectivity & security** tab, write
     down the values of the VPC ID under **VPC** and the
     subnet ID under **Subnets**.
    4. Open the Amazon VPC console at
     [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
    5. In the navigation pane, choose **Internet Gateways**.
     Verify that there is an internet gateway attached to your VPC.
     Otherwise, choose **Create Internet Gateway** to create
     an internet gateway. Select the internet gateway, and then choose
     **Attach to VPC** and follow the directions to
     attach it to your VPC.
    6. In the navigation pane, choose **Subnets**, and then
     select your subnet.
    7. On the **Route Table** tab, verify that there is a
     route with `0.0.0.0/0` as the destination and the internet
     gateway for your VPC as the target.


    If you're connecting to your instance using its IPv6 address, verify
     that there is a route for all IPv6 traffic (`::/0`) that
     points to the internet gateway. Otherwise, do the following:


    	1. Choose the ID of the route table
    	 (rtb-*xxxxxxxx*) to navigate to the route
    	 table.
    	2. On the **Routes** tab, choose **Edit
    	 routes**. Choose **Add route**,
    	 use `0.0.0.0/0` as the destination and the internet
    	 gateway as the target.


    	For IPv6, choose **Add route**, use
    	 `::/0` as the destination and the internet
    	 gateway as the target.
    	3. Choose **Save routes**.Also, if you are trying to connect to IPv6 endpoint, make sure that
     client IPv6 address range is authorized to connect to the DB
     instance.

For more information, see [Working with a DB instance in a VPC](USER_VPC.md "USER_VPC.md").

For engine-specific connection issues, see the following
topics:

- [Troubleshooting connections to your SQL Server DB instance](USER_ConnectToMicrosoftSQLServerInstance.md "USER_ConnectToMicrosoftSQLServerInstance.md")
- [Troubleshooting connections to your Oracle DB
  instance](USER_ConnectToOracleInstance.md "USER_ConnectToOracleInstance.md")
- [Troubleshooting
  connections to your RDS for PostgreSQL instance](USER_ConnectToPostgreSQLInstance.md "USER_ConnectToPostgreSQLInstance.md")
- [Maximum MySQL and MariaDB
  connections](#USER_ConnectToInstance.max_connections "#USER_ConnectToInstance.max_connections")

### Testing a connection to a DB

instance

You can test your connection to a DB instance using common Linux or Microsoft
Windows tools.

From a Linux or Unix terminal, you can test the connection by entering the
following. Replace `DB-instance-endpoint` with
the endpoint and `port` with the port of your
DB instance.

```
nc -zv `DB-instance-endpoint` `port`
```

For example, the following shows a sample command and the return value.

```
nc -zv postgresql1.c6c8mn7fake0.us-west-2.rds.amazonaws.com 8299

  Connection to postgresql1.c6c8mn7fake0.us-west-2.rds.amazonaws.com 8299 port [tcp/vvr-data] succeeded!
```

Windows users can use Telnet to test the connection to a DB instance. Telnet
actions aren't supported other than for testing the connection. If a connection
is successful, the action returns no message. If a connection isn't successful,
you receive an error message such as the following.

```
C:\>telnet sg-postgresql1.c6c8mntfake0.us-west-2.rds.amazonaws.com 819

  Connecting To sg-postgresql1.c6c8mntfake0.us-west-2.rds.amazonaws.com...Could not open
  connection to the host, on port 819: Connect failed
```

If Telnet actions return success, your security group is properly
configured.

###### Note

Amazon RDS doesn't accept internet control message protocol (ICMP) traffic,
including ping.

### Troubleshooting

connection authentication

In some cases, you can connect to your DB instance but you get authentication
errors. In these cases, you might want to reset the master user password for the DB
instance. You can do this by modifying the RDS instance.

For more information about modifying a DB instance, see
[Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

## Amazon RDS security issues

To avoid security issues, never use your AWS account root user email address and
password for a user account. Best practice is to use your root user to create users and
assign those to DB user accounts. You can also use your root user to create other user
accounts, if necessary.

For information about creating users, see [Creating an IAM user in your
AWS account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md"). For information about creating users in AWS IAM Identity Center, see [Manage
identities in IAM Identity Center](../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md "../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md").

### Error message

"failed to retrieve account attributes, certain console functions may be
impaired."

You can get this error for several reasons. It might be because your account is
missing permissions, or your account hasn't been properly set up. If your
account is new, you might not have waited for the account to be ready. If this is an
existing account, you might lack permissions in your access policies to perform
certain actions such as creating a DB instance. To fix the issue, your administrator
needs to provide the necessary roles to your account. For more information, see
[the IAM
documentation](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

## Troubleshooting

incompatible-network state

The incompatible-network state means that the database might still be accessible at
the database level but you can't modify or reboot it.

### Causes

The incompatible-network state of your DB instance could be a result of one of the
following actions:

- Modifying the DB instance class.
- Modifying the DB instance to use Multi-AZ DB cluster deployment.
- Replacing a host because of a maintenance event.
- Launching a replacement DB instance.
- Restoring from a snapshot backup.
- Starting a DB instance that was stopped.

### Resolution

#### Use

start-db-instance command

To fix a database that is in an incompatible-network state, follow these
instructions:

1. Open the [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/") and choose **Databases**
   from the navigation pane.
2. Choose the DB instance that is in the incompatible-network state and
   note the DB instance identifier, VPC ID, and subnet IDs from the
   **Connectivity & Security** tab.
3. Use the AWS CLI to run the `start-db-instance` command.
   Specify the `--db-instance-identifier` value.

###### Note

Running this command when your database is in incompatible mode
might cause some downtime.

The `start-db-instance` command does not resolve this
issue for RDS for SQL Server DB instances.

Your database status changes to **Available** if the command
executes successfully.

If your database restarts, the DB instance might execute the last operation run on
the instance before it was moved to incompatible-network state. This might move
the instance back to the incompatible-network state.

If the `start-db-instance` command is unsuccessful or the instance
moves back to incompatible-network state, open the
**Databases** page in the RDS console and select the
database. Navigate to the **Logs & events** section. The
**Recent events** section displays further resolution steps
to follow. The messages are classified as follows:

- **INTERNAL RESOURCE CHECK**: There might be issues
  with your internal resources.
- **DNS CHECK**: Check DNS resolution and hostnames for
  the VPC in the VPC console.
- **ENI CHECK**: The elastic network interface (ENI)
  for your database might not exist.
- **GATEWAY CHECK**: The internet gateway for your
  publicly available database is not attached to the VPC.
- **IP CHECK**: There are no free IP addresses in your
  subnets.
- **SECURITY GROUP CHECK**: There are no security
  groups associated with your database or the security groups are
  invalid.
- **SUBNET CHECK**: There are no valid subnets in your
  DB subnet group or there are issues with your subnet.
- **VPC CHECK**: The VPC associated with your database
  is invalid.

#### Perform point-in-time recovery

It is best practice to have a backup (snapshot or logical), in case your
database enters incompatible-network state. See [Introduction to backups](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md"). If you turned on
automated backups, then temporarily stop any writes to the database and perform
a point-in-time recovery.

###### Note

After an instance enters the incompatible-network state, the DB instance
might not be accessible to perform a logical backup.

If you didn't turn on automated backups, create a new DB instance. Then migrate the data
using [AWS Database Migration Service (AWS DMS)](../../../dms/latest/userguide.md "../../../dms/latest/userguide.md"), or by
using a backup and restore tool.

If this does not resolve the issue, contact Support for further
assistance.

## Resetting the DB instance owner

password

If you get locked out of your DB instance, you can log in as the
master user. Then you can reset the credentials for other administrative users or roles.
If you can't log in as the master user, the AWS account owner can reset the master
user password. For details of which administrative accounts or roles you might need to
reset, see [Master user account privileges](UsingWithRDS.md "UsingWithRDS.md").

You can change the DB instance password by using the Amazon RDS
console, the AWS CLI command [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md"), or by using the [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") API operation.
For more information about modifying a DB instance, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

## Amazon RDS DB instance outage or

reboot

A DB instance outage can occur when a DB instance is rebooted. It can also occur when
the DB instance is put into a state that prevents access to it, and when the database is
restarted. A reboot can occur when you manually reboot your DB instance. A reboot can
also occur when you change a DB instance setting that requires a reboot before it can
take effect.

A DB instance reboot occurs when you change a setting that requires a reboot, or when
you manually cause a reboot. A reboot can occur immediately if you change a setting and
request that the change take effect immediately. Or it can occur during the DB
instance's maintenance window.

A DB instance reboot occurs immediately when one of the following occurs:

- You change the backup retention period for a DB instance from 0 to a nonzero
  value or from a nonzero value to 0. You then set **Apply
  Immediately** to `true`.
- You change the DB instance class, and **Apply
  Immediately** is set to `true`.
- You change the storage type from **Magnetic (Standard)** to
  **General Purpose (SSD**) or **Provisioned IOPS
  (SSD)**, or from **Provisioned IOPS (SSD)** or
  **General Purpose (SSD)** to **Magnetic
  (Standard)**.

A DB instance reboot occurs during the maintenance window when one of the following
occurs:

- You change the backup retention period for a DB instance from 0 to a nonzero
  value or from a nonzero value to 0, and **Apply
  Immediately** is set to `false`.
- You change the DB instance class, and **Apply
  Immediately** is set to `false`.

When you change a static parameter in a DB parameter group, the change doesn't
take effect until the DB instance associated with the parameter group is rebooted. The
change requires a manual reboot. The DB instance isn't automatically rebooted
during the maintenance window.

To see a table that shows DB instance actions and the effect
that setting the **Apply Immediately** value has, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

## Amazon RDS DB parameter changes not taking

effect

In some cases, you might change a parameter in a DB parameter group but don't see the
changes take effect. If so, you likely need to reboot the DB instance associated with
the DB parameter group. When you change a dynamic parameter, the change takes effect
immediately. When you change a static parameter, the change doesn't take effect
until you reboot the DB instance associated with the parameter group.

You can reboot a DB instance using the RDS console. Or you can explicitly call the
[`RebootDBInstance`](../APIReference/API_RebootDBInstance.md "../APIReference/API_RebootDBInstance.md") API operation. You can reboot without
failover if the DB instance is in a Multi-AZ deployment. The requirement to reboot the associated
DB instance after a static parameter change helps mitigate the risk of a parameter
misconfiguration affecting an API call. An example of this is calling
`ModifyDBInstance` to change the DB instance class. For more information,
see [Modifying parameters in a DB parameter group
in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

## Amazon RDS DB instance running out of

storage

If your DB instance runs out of storage space, it might no longer be available. We
highly recommend that you constantly monitor the `FreeStorageSpace` metric
published in CloudWatch to make sure that your DB instance has enough free storage
space.

If your database instance runs out of storage, its status changes to
`storage-full`. For example, a call to the
`DescribeDBInstances` API operation for a DB instance that has used up
its storage outputs the following.

```
aws rds describe-db-instances --db-instance-identifier `mydbinstance`

DBINSTANCE  mydbinstance  2009-12-22T23:06:11.915Z  db.m5.large  mysql8.0  50  sa
storage-full  mydbinstance.clla4j4jgyph.us-east-1.rds.amazonaws.com  3306
us-east-1b  3
	SECGROUP  default  active
	PARAMGRP  default.mysql8.0  in-sync
```

To recover from this scenario, add more storage space to your instance using the
`ModifyDBInstance` API operation or the following AWS CLI command.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `mydbinstance` \
    --allocated-storage `60` \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --allocated-storage `60` ^
    --apply-immediately
```

```
DBINSTANCE  mydbinstance  2009-12-22T23:06:11.915Z  db.m5.large  mysql8.0  50  sa
storage-full  mydbinstance.clla4j4jgyph.us-east-1.rds.amazonaws.com  3306
us-east-1b  3  60
	SECGROUP  default  active
	PARAMGRP  default.mysql8.0  in-sync
```

Now, when you describe your DB instance, you see that your DB instance has
`modifying` status, which indicates the storage is being scaled.

```
aws rds describe-db-instances --db-instance-identifier `mydbinstance`
```

```
DBINSTANCE  mydbinstance  2009-12-22T23:06:11.915Z  db.m5.large  mysql8.0  50  sa
modifying  mydbinstance.clla4j4jgyph.us-east-1.rds.amazonaws.com
3306  us-east-1b  3  60
	SECGROUP  default  active
	PARAMGRP  default.mysql8.0  in-sync
```

After storage scaling is complete, your DB instance status changes to
`available`.

```
aws rds describe-db-instances --db-instance-identifier `mydbinstance`
```

```
DBINSTANCE  mydbinstance  2009-12-22T23:06:11.915Z  db.m5.large  mysql8.0  60  sa
available  mydbinstance.clla4j4jgyph.us-east-1.rds.amazonaws.com  3306
us-east-1b  3
	SECGROUP  default  active
	PARAMGRP  default.mysql8.0  in-sync
```

You can receive notifications when your storage space is exhausted using the
`DescribeEvents` operation. For example, in this scenario, if you make a
`DescribeEvents` call after these operations you see the following
output.

```
aws rds describe-events --source-type `db-instance` --source-identifier `mydbinstance`
```

```
2009-12-22T23:44:14.374Z  mydbinstance  Allocated storage has been exhausted db-instance
2009-12-23T00:14:02.737Z  mydbinstance  Applying modification to allocated storage db-instance
2009-12-23T00:31:54.764Z  mydbinstance  Finished applying modification to allocated storage
```

## Amazon RDS insufficient DB instances available

The `InsufficientDBInstanceCapacity` error can be returned when you try to
create, start, or modify a DB instance. It can also be returned when you try to restore
a DB instance from a DB snapshot. When this error is returned, a common cause is that
the specific DB instance class isn't available in the requested Availability Zone.
You can try one of the following to solve the problem:

- Retry the request with a different DB instance class.
- Retry the request with a different Availability Zone.
- Retry the request without specifying an explicit Availability Zone.

For information about troubleshooting instance capacity issues for Amazon EC2, see [Insufficient instance capacity](../../../AWSEC2/latest/UserGuide/troubleshooting-launch.md#troubleshooting-launch-capacity "../../../AWSEC2/latest/UserGuide/troubleshooting-launch.md#troubleshooting-launch-capacity") in the _Amazon EC2 User
Guide_.

For information about modifying a DB instance, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

## Freeable memory issues in Amazon RDS

_Freeable memory_ is the total random access memory (RAM) on a DB
instance that can be made available to the database engine. It's the sum of the
free operating-system (OS) memory and the available buffer and page cache memory. The
database engine uses most of the memory on the host, but OS processes also use some RAM.
Memory currently allocated to the database engine or used by OS processes isn't included
in freeable memory. When the database engine
is running out of memory, the DB instance can use the temporary space that is normally
used for buffering and caching. As previously mentioned, this temporary space is
included in freeable memory.

You use the `FreeableMemory` metric in Amazon CloudWatch to monitor the freeable
memory. For more information, see [Monitoring tools for Amazon RDS](MonitoringOverview.md "MonitoringOverview.md").

If your DB instance consistently runs low on freeable memory or uses swap space,
consider scaling up to a larger DB instance class. For more information, see [DB instance classes](Concepts.md "Concepts.md").

You can also change the memory settings. For example, on
RDS for MySQL, you might adjust the size of the
`innodb_buffer_pool_size` parameter. This parameter is set by default to
75 percent of physical memory. For more MySQL troubleshooting tips, see [How can I troubleshoot low freeable memory in an Amazon RDS for MySQL
database?](https://aws.amazon.com/premiumsupport/knowledge-center/low-freeable-memory-rds-mysql-mariadb/ "https://aws.amazon.com/premiumsupport/knowledge-center/low-freeable-memory-rds-mysql-mariadb/")

## MySQL and MariaDB issues

You can diagnose and correct issues with MySQL and MariaDB DB
instances.

###### Topics

- [Maximum MySQL and MariaDB
  connections](#USER_ConnectToInstance.max_connections "#USER_ConnectToInstance.max_connections")
- [Diagnosing and
  resolving incompatible parameters status for a memory limit](#CHAP_Troubleshooting.incompatible-parameters-memory "#CHAP_Troubleshooting.incompatible-parameters-memory")
- [Diagnosing and resolving lag
  between read replicas](#CHAP_Troubleshooting.MySQL.ReplicaLag "#CHAP_Troubleshooting.MySQL.ReplicaLag")
- [Diagnosing and resolving a
  MySQL or MariaDB read replication
  failure](#CHAP_Troubleshooting.MySQL.RR "#CHAP_Troubleshooting.MySQL.RR")
- [Creating triggers with
  binary logging enabled requires SUPER privilege](#CHAP_Troubleshooting.MySQL.CreatingTriggers "#CHAP_Troubleshooting.MySQL.CreatingTriggers")
- [Diagnosing and resolving
  point-in-time restore failures](#CHAP_Troubleshooting.MySQL.PITR "#CHAP_Troubleshooting.MySQL.PITR")
- [Replication stopped
  error](#CHAP_Troubleshooting.MySQL.ReplicationStopped "#CHAP_Troubleshooting.MySQL.ReplicationStopped")
- [Read replica create fails
  or replication breaks with fatal error 1236](#CHAP_Troubleshooting.MySQL.ReadReplicas "#CHAP_Troubleshooting.MySQL.ReadReplicas")
- [Read replica
  replication fails to initialize metadata structure](#CHAP_Troubleshooting.MySQL.ReadReplicas.ReplicationErrorMetadata "#CHAP_Troubleshooting.MySQL.ReadReplicas.ReplicationErrorMetadata")

### Maximum MySQL and MariaDB

connections

The maximum number of connections allowed to an RDS for MySQL or RDS for MariaDB DB instance is based on the amount
of memory available for its DB instance class. A DB instance class with more memory
available results in a larger number of connections available. For more information
on DB instance classes, see [DB instance classes](Concepts.md "Concepts.md").

The connection limit for a DB instance is set by default to the maximum for the DB
instance class. You can limit the number of concurrent connections to any value up
to the maximum number of connections allowed. Use the `max_connections`
parameter in the parameter group for the DB instance. For more information, see
[Maximum number of database
connections](CHAP_Limits.md#RDS_Limits.MaxConnections "CHAP_Limits.md#RDS_Limits.MaxConnections") and [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

You can retrieve the maximum number of connections allowed for a MySQL or MariaDB DB instance by running the following
query.

```
SELECT @@max_connections;
```

You can retrieve the number of active connections to a MySQL or MariaDB DB instance by running the following
query.

```
SHOW STATUS WHERE `variable_name` = 'Threads_connected';
```

### Diagnosing and

resolving incompatible parameters status for a memory limit

A MariaDB or MySQL DB instance can be placed in
**incompatible-parameters** status for a memory limit when the
following conditions are met:

- The DB instance is restarted at least three times in one hour or at least
  five times in one day when the DB instance status is **Available**.
- An attempt to restart the DB instance fails because a maintenance action
  or monitoring process couldn't restart the DB instance.
- The potential memory usage of the DB instance exceeds 1.2 times the memory
  allocated to its DB instance class.

When a DB instance is restarted for the third time in one hour or for the fifth
time in one day, it performs a check for memory usage. The check makes a calculation
of the potential memory usage of the DB instance. The value returned by the
calculation is the sum of the following values:

- **Value 1** – The sum of the following
  parameters:
  - `innodb_additional_mem_pool_size`
  - `innodb_buffer_pool_size`

  You can modify the value for `innodb_buffer_pool_size`.
  However, the value won't always match what you input. This mismatch
  occurs for several reasons. First, if the DB instance is a micro DB
  instance, then we override the default value and set it to 256 MB.
  For more information, see [Overriding
  innodb_buffer_pool_size](MySQL.md#MySQL.Concepts.KnownIssuesAndLimitations.innodb-bp-size "MySQL.md#MySQL.Concepts.KnownIssuesAndLimitations.innodb-bp-size").

  Second, we make sure that 500 MB of memory is reserved on the DB
  instance for the host manager, the engine, the operating system, and
  the kernel.

  Last, we optimize `innodb_buffer_pool_size` by dividing
  it into units. The host manager rounds down to the closest multiple
  of those units. The units are calculated by multiplying
  `innodb_buffer_pool_chunk_size` by
  `innodb_buffer_pool_instances`. For more information,
  see [Configuring InnoDB Buffer Pool Size](https://dev.mysql.com/doc/refman/8.0/en/innodb-buffer-pool-resize.html "https://dev.mysql.com/doc/refman/8.0/en/innodb-buffer-pool-resize.html") in the MySQL
  documentation.

  The default for `innodb_buffer_pool_instances` is 8,
  unless `innodb_buffer_pool_size` is less than 1 GB. If
  `innodb_buffer_pool_size` is less than 1 GB, then the
  default for `innodb_buffer_pool_instances` is 1. The
  default for `innodb_buffer_pool_chunk_size` is 128 MB.
  - `innodb_log_buffer_size`
  - `key_buffer_size`
  - `query_cache_size` (MySQL version 5.7 only)
  - `tmp_table_size`

- **Value 2** – The
  `max_connections` parameter multiplied by the sum of the
  following parameters:
  - `binlog_cache_size`
  - `join_buffer_size`
  - `read_buffer_size`
  - `read_rnd_buffer_size`
  - `sort_buffer_size`
  - `thread_stack`

- **Value 3** – If the
  `performance_schema` parameter is enabled, then multiply the
  `max_connections` parameter by `429498`.

If the `performance_schema` parameter is disabled, then this
value is zero.

So, the value returned by the calculation is the following:

`Value 1 + Value 2 + Value 3`

When this value exceeds 1.2 times the memory allocated to the DB instance class
used by the DB instance, the DB instance is placed in
**incompatible-parameters** status. For information about the
memory allocated to DB instance classes, see [Hardware specifications for DB instance
classes](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").

The calculation multiplies the value of the `max_connections` parameter
by the sum of several parameters. If the `max_connections` parameter is
set to a large value, it might cause the check to return an inordinately high value
for the potential memory usage of the DB instance. In this case, consider lowering
the value of the `max_connections` parameter.

To resolve the problem, complete the following steps:

1. Adjust the memory parameters in the DB parameter group associated with the
   DB instance. Do so such that the potential memory usage is lower than 1.2
   times the memory allocated to its DB instance class.

For information about setting parameters, see [Modifying parameters in a DB parameter group
in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). 2. Restart the DB instance.

For information about setting parameters, see [Starting an Amazon RDS DB instance that was previously stopped](USER_StartInstance.md "USER_StartInstance.md").

### Diagnosing and resolving lag

between read replicas

After you create a MySQL or MariaDB read
replica and the replica is available, Amazon RDS first replicates the changes made to the
source DB instance from the time the read replica create operation started. During
this phase, the replication lag time for the read replica is greater than 0. You can
monitor this lag time in Amazon CloudWatch by viewing the Amazon RDS `ReplicaLag`

metric.

The `ReplicaLag` metric reports the value of the
`Seconds_Behind_Master` field of the MariaDB or MySQL `SHOW
 REPLICA STATUS` command. For more information, see [SHOW
REPLICA STATUS Statement](https://dev.mysql.com/doc/refman/8.0/en/show-replica-status.html "https://dev.mysql.com/doc/refman/8.0/en/show-replica-status.html") in the MySQL documentation.

When the `ReplicaLag` metric reaches 0, the
replica has caught up to the source DB instance. If the `ReplicaLag`
metric returns -1, replication might not be active. To troubleshoot a replication
error, see [Diagnosing and resolving a
MySQL or MariaDB read replication
failure](#CHAP_Troubleshooting.MySQL.RR "#CHAP_Troubleshooting.MySQL.RR"). A `ReplicaLag` value
of -1 can also mean that the `Seconds_Behind_Master` value can't be
determined or is `NULL`.

###### Note

Previous versions of MariaDB used `SHOW SLAVE STATUS` instead of
`SHOW REPLICA STATUS`. If you are using a MariaDB version lower
than 10.5, then use `SHOW SLAVE STATUS`.

The `ReplicaLag`
metric
returns -1 during a network outage or when a patch is applied during the maintenance
window. In this case, wait for network connectivity to be restored or for the
maintenance window to end before you check the `ReplicaLag`
metric
again.

The MySQL and MariaDB read replication
technology is asynchronous. Thus, you can expect occasional increases for the
`BinLogDiskUsage` metric on the source DB instance and for the
`ReplicaLag`
metric on
the read replica. For example, consider a situation where a high volume of write
operations to the source DB instance occur in parallel. At the same time, write
operations to the read replica are serialized using a single I/O thread. Such a
situation can lead to a lag between the source instance and read replica.

For more information about read replicas and MySQL, see [Replication implementation details](https://dev.mysql.com/doc/refman/8.0/en/replication-implementation-details.html "https://dev.mysql.com/doc/refman/8.0/en/replication-implementation-details.html") in the MySQL documentation. For more information about read replicas and MariaDB, see
[Replication overview](http://mariadb.com/kb/en/mariadb/replication-overview/ "http://mariadb.com/kb/en/mariadb/replication-overview/") in the MariaDB documentation.

You can reduce the lag between updates to a source DB instance and the subsequent
updates to the read replica by doing the following:

- Set the DB instance class of the read replica to have a storage size
  comparable to that of the source DB instance.
- Make sure that parameter settings in the DB parameter groups used by the
  source DB instance and the read replica are compatible. For more information
  and an example, see the discussion of the `max_allowed_packet`
  parameter in the next section.
- Disable the query cache. For tables that are modified often, using the
  query cache can increase replica lag because the cache is locked and
  refreshed often. If this is the case, you might see less replica lag if you
  disable the query cache. You can disable the query cache by setting the
  `query_cache_type parameter` to 0 in the DB parameter group
  for the DB instance. For more information on the query cache, see [Query cache configuration](https://dev.mysql.com/doc/refman/5.7/en/query-cache-configuration.html "https://dev.mysql.com/doc/refman/5.7/en/query-cache-configuration.html").
- Warm the buffer pool on the read replica for InnoDB for MySQL or MariaDB. For example, suppose that
  you have a small set of tables that are being updated often and you're
  using the InnoDB or XtraDB table schema. In this case, dump those tables on
  the read replica. Doing this causes the database engine to scan through the
  rows of those tables from the disk and then cache them in the buffer pool.
  This approach can reduce replica lag. The following shows an example.

For Linux, macOS, or Unix:

```
PROMPT> mysqldump \
    -h `<endpoint>` \
    --port=`<port>` \
    -u=`<username>` \
    -p `<password>` \
    database_name `table1 table2` > /dev/null
```

For Windows:

```
PROMPT> mysqldump ^
    -h `<endpoint>` ^
    --port=`<port>` ^
    -u=`<username>` ^
    -p `<password>` ^
    database_name `table1 table2` > /dev/null
```

### Diagnosing and resolving a

MySQL or MariaDB read replication
failure

Amazon RDS monitors the replication status of your read replicas. RDS updates the
**Replication State** field of the read replica instance to
`Error` if replication stops for any reason. You can
review the details of the associated error thrown by the MySQL or MariaDB engines by viewing the
**Replication Error** field. Events that indicate the status of
the read replica are also generated, including [RDS-EVENT-0045](USER_Events.md#RDS-EVENT-0045 "USER_Events.md#RDS-EVENT-0045"),
[RDS-EVENT-0046](USER_Events.md#RDS-EVENT-0046 "USER_Events.md#RDS-EVENT-0046"), and [RDS-EVENT-0057](USER_Events.md#RDS-EVENT-0057 "USER_Events.md#RDS-EVENT-0057"). For more
information about events and subscribing to events, see [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md"). If a MySQL error message is returned, check the
error in the [MySQL error message documentation](https://dev.mysql.com/doc/mysql-errors/8.0/en/server-error-reference.html "https://dev.mysql.com/doc/mysql-errors/8.0/en/server-error-reference.html"). If a
MariaDB error message is returned, check the error in the [MariaDB error
message documentation](http://mariadb.com/kb/en/mariadb/mariadb-error-codes/ "http://mariadb.com/kb/en/mariadb/mariadb-error-codes/").

Common situations that can cause replication errors include the following:

- The value for the `max_allowed_packet` parameter for a read
  replica is less than the `max_allowed_packet` parameter for the
  source DB instance.

The `max_allowed_packet` parameter is a custom parameter that
you can set in a DB parameter group. The `max_allowed_packet`
parameter is used to specify the maximum size of data manipulation language
(DML) that can be run on the database. In some cases, the
`max_allowed_packet` value for the source DB instance might
be larger than the `max_allowed_packet` value for the read
replica. If so, the replication process can throw an error and stop
replication. The most common error is `packet bigger than
 'max_allowed_packet' bytes`. You can fix the error by having the
source and read replica use DB parameter groups with the same
`max_allowed_packet` parameter values.

- Writing to tables on a read replica. If you're creating indexes on a
  read replica, you need to have the `read_only` parameter set to
  _0_ to create the indexes. If
  you're writing to tables on the read replica, it can break
  replication.
- Using a nontransactional storage engine such as MyISAM. Read replicas
  require a transactional storage engine. Replication is only supported for
  the following storage engines: InnoDB for MySQL or MariaDB.

You can convert a MyISAM table to InnoDB with the following
command:

`alter table <schema>.<table_name>
 engine=innodb;`

- Using unsafe nondeterministic queries such as `SYSDATE()`. For
  more information, see [Determination of safe and unsafe statements in binary logging](https://dev.mysql.com/doc/refman/8.0/en/replication-rbr-safe-unsafe.html "https://dev.mysql.com/doc/refman/8.0/en/replication-rbr-safe-unsafe.html")
  in the MySQL documentation.

The following steps can help resolve your replication error:

- If you encounter a logical error and you can safely skip the error, follow
  the steps described in [Skipping the current
  replication error for RDS for MySQL](Appendix.MySQL.CommonDBATasks.md "Appendix.MySQL.CommonDBATasks.md"). Your MySQL or
  MariaDB DB instance must be running a version that includes the
  `mysql_rds_skip_repl_error` procedure. For more information,
  see [mysql.rds_skip_repl_error](mysql-stored-proc-replicating.md#mysql_rds_skip_repl_error "mysql-stored-proc-replicating.md#mysql_rds_skip_repl_error").
- If you encounter a binary log (binlog) position issue, you can change the
  replica replay position with the [mysql.rds_next_source_log (RDS for MySQL major versions 8.4 and higher)](mysql-stored-proc-replicating.md#mysql_rds_next_source_log "mysql-stored-proc-replicating.md#mysql_rds_next_source_log") or [mysql.rds_next_master_log (RDS for MariaDB and RDS for MySQL major versions 8.0 and
  lower)](mysql-stored-proc-replicating.md#mysql_rds_next_master_log "mysql-stored-proc-replicating.md#mysql_rds_next_master_log") command.
- You might encounter a temporary performance issue because of high DML
  load. If so, you can set the `innodb_flush_log_at_trx_commit`
  parameter to 2 in the DB parameter group on the read replica. Doing this can
  help the read replica catch up, though it temporarily reduces atomicity,
  consistency, isolation, and durability (ACID).
- You can delete the read replica and create an instance using the same DB
  instance identifier. If you do this, the endpoint remains the same as that
  of your old read replica.

If a replication error is fixed, the **Replication
State** changes to **replicating**. For more
information, see [Troubleshooting a MySQL read replica problem](USER_ReadRepl.md "USER_ReadRepl.md").

### Creating triggers with

binary logging enabled requires SUPER privilege

When trying to create triggers in an RDS for MySQL or RDS for MariaDB DB instance, you
might receive the following error.

```
"You do not have the SUPER privilege and binary logging is enabled"
```

To use triggers when binary logging is enabled requires the SUPER privilege, which
is restricted for RDS for MySQL and RDS for MariaDB DB instances. You can create triggers
when binary logging is enabled without the SUPER privilege by setting the
`log_bin_trust_function_creators` parameter to true. To set the
`log_bin_trust_function_creators` to true, create a new DB parameter
group or modify an existing DB parameter group.

You can create a new DB parameter group so you can create triggers in your
RDS for MySQL or RDS for MariaDB DB instance with binary logging enabled. To do so, use the
following CLI commands. To modify an existing parameter group, start with step 2.

###### To create a new parameter group to allow triggers with binary logging enabled

using the CLI

1. Create a new parameter group.

For Linux, macOS, or Unix:

```
aws rds create-db-parameter-group \
    --db-parameter-group-name `allow-triggers` \
    --db-parameter-group-family `mysql8.0` \
    --description "`parameter group allowing triggers`"
```

For Windows:

```
aws rds create-db-parameter-group ^
    --db-parameter-group-name `allow-triggers` ^
    --db-parameter-group-family `mysql8.0` ^
    --description "`parameter group allowing triggers`"
```

2. Modify the DB parameter group to allow triggers.

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group \
    --db-parameter-group-name `allow-triggers` \
    --parameters "`ParameterName=log_bin_trust_function_creators, ParameterValue=true, ApplyMethod=pending-reboot`"
```

For Windows:

```
aws rds modify-db-parameter-group ^
    --db-parameter-group-name `allow-triggers` ^
    --parameters "`ParameterName=log_bin_trust_function_creators, ParameterValue=true, ApplyMethod=pending-reboot`"
```

3. Modify your DB instance to use the new DB parameter group.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `mydbinstance` \
    --db-parameter-group-name `allow-triggers` \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --db-parameter-group-name `allow-triggers` ^
    --apply-immediately
```

4. For the changes to take effect, manually reboot the DB instance.

```
aws rds reboot-db-instance --db-instance-identifier `mydbinstance`
```

### Diagnosing and resolving

point-in-time restore failures

**Restoring a DB instance that includes temporary
tables**

When attempting a point-in-time restore (PITR) of your MySQL or MariaDB DB
instance, you might encounter the following error.

```
Database instance could not be restored because there has been incompatible database activity for restore
functionality. Common examples of incompatible activity include using temporary tables, in-memory tables,
or using MyISAM tables. In this case, use of Temporary table was detected.
```

PITR relies on both backup snapshots and binary logs (binlogs) from MySQL or
MariaDB to restore your DB instance to a particular time. Temporary table
information can be unreliable in binlogs and can cause a PITR failure. If you use
temporary tables in your MySQL or MariaDB DB instance, you can decrease the
possibility of a PITR failure by performing more frequent backups. A PITR failure is
most probable in the time between a temporary table's creation and the next backup
snapshot.

**Restoring a DB instance that includes in-memory
tables**

You might encounter a problem when restoring a database that has in-memory tables.
In-memory tables are purged during a restart. As a result, your in-memory tables
might be empty after a reboot. We recommend that when you use in-memory tables, you
architect your solution to handle empty tables in the event of a restart. If you're
using in-memory tables with replicated DB instances, you might need to recreate the
read replicas after a restart. This might be necessary if a read replica reboots and
can't restore data from an empty in-memory table.

For more information about backups and PITR, see [Introduction to backups](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md") and [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").

### Replication stopped

error

When you call the `mysql.rds_skip_repl_error` command, you might
receive an error message stating that replication is down or disabled.

This error message appears because replication is stopped and can't be
restarted.

If you need to skip a large number of errors, the replication lag can increase
beyond the default retention period for binary log files. In this case, you might
encounter a fatal error because of binary log files being purged before they have
been replayed on the replica. This purge causes replication to stop, and you can no
longer call the `mysql.rds_skip_repl_error` command to skip replication
errors.

You can mitigate this issue by increasing the number of hours that binary log
files are retained on your replication source. After you have increased the binlog
retention time, you can restart replication and call the
`mysql.rds_skip_repl_error` command as needed.

To set the binlog retention time, use the [mysql.rds_set_configuration](mysql-stored-proc-configuring.md#mysql_rds_set_configuration "mysql-stored-proc-configuring.md#mysql_rds_set_configuration") procedure. Specify a configuration
parameter of 'binlog retention hours' along with the number of hours to retain
binlog files on the DB cluster, up to 720 (30 days). The following example sets the
retention period for binlog files to 48 hours.

```
CALL mysql.rds_set_configuration('binlog retention hours', 48);
```

### Read replica create fails

or replication breaks with fatal error 1236

After changing default parameter values for a MySQL or MariaDB DB instance, you
might encounter one of the following problems:

- You can't create a read replica for the DB instance.
- Replication fails with `fatal error 1236`.

Some default parameter values for MySQL and MariaDB DB instances help to make sure
that the database is ACID compliant and read replicas are crash-safe. They do this
by making sure that each commit is fully synchronized by writing the transaction to
the binary log before it's committed. Changing these parameters from their default
values to improve performance can cause replication to fail when a transaction
hasn't been written to the binary log.

To resolve this issue, set the following parameter values:

- `sync_binlog = 1`
- `innodb_support_xa = 1`
- `innodb_flush_log_at_trx_commit = 1`

### Read replica

replication fails to initialize metadata structure

When you attempted to start replication, you received the following error message:

```
Read Replica Replication Error - SQLError: 13124, reason: Replica failed to initialize applier metadata structure from the repository
```

This error occurs when there is a problem with the metadata structure of the replica. To
fix the metadata structure, you must create a new replica.

To prevent this from happening in the future, perform one of the following actions:

- If possible, disable multi-threading on your replicas. Starting with MySQL 8.0.27,
  multi-threading is enabled by default.
- If you need to use multi-threading on your replicas, then we recommend that you use
  GTID-based replication. For more information, see [Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md").

## Can't set backup retention

period to 0

There are several reasons why you might need to set the backup retention period to 0.
For example, you can disable automatic backups immediately by setting the retention
period to 0.

In some cases, you might set the value to 0 and receive a message saying that the
retention period must be between 1 and 35. In these cases, check to make sure that you
haven't set up a read replica for the instance. Read replicas require backups for
managing read replica logs, and therefore you can't set a retention period of 0.
