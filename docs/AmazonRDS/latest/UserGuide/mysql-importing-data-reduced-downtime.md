# Importing data to an Amazon RDS for MySQL

database with reduced downtime

In some cases, you might need to import data from an external MySQL database that supports
a live application to an RDS for MySQL DB instance or an RDS for MySQL Multi-AZ DB cluster. Use the following
procedure to minimize the impact on availability of applications. This procedure can also
help if you are working with a very large database. Using this procedure, you can reduce the
cost of the import by reducing the amount of data that is passed across the network to
AWS.

In this procedure, you transfer a copy of your database data to an Amazon EC2 instance and
import the data into a new Amazon RDS database. You then use replication to bring the Amazon RDS
database up-to-date with your live external instance, before redirecting your application to
the Amazon RDS database. Configure replication based on binary log coordinates.

###### Note

If you want to import data into an RDS for MySQL DB instance and your scenario supports
it, we recommend moving data in and out of Amazon RDS by using backup files and Amazon S3. For
more information, see [Restoring a backup into an Amazon RDS for MySQL DB
instance](MySQL.Procedural.md "MySQL.Procedural.md").

The following diagram shows importing an external MySQL database into a MySQL database on
Amazon RDS.

![Workflow that shows importing an external MySQL database into a MySQL database on Amazon RDS.](images/MigrateMySQLToRDS_1.png)

## Task 1: Create a

copy of your existing database

The first step in the process of migrating a large amount of data to an RDS for MySQL
database with minimal downtime is to create a copy of the source data.

The following diagram shows creating a backup of the MySQL database.

![Workflow that shows creating a backup of the MySQL database.](images/MigrateMySQLToRDS_2.png)

You can use the `mysqldump` utility to create a database backup in either
SQL or delimited-text format. We recommend that you do a test run with each format in a
non-production environment to see which method minimizes the amount of time that
`mysqldump` runs.

We also recommend that you weigh `mysqldump` performance against the
benefit offered by using the delimited-text format for loading. A backup using
delimited-text format creates a tab-separated text file for each table being dumped. To
reduce the amount of time required to import your database, you can load these files in
parallel using the `LOAD DATA LOCAL INFILE` command. For more information,
see [Step 5: Load the
data](mysql-importing-data-any-source.md#mysql-importing-data-any-source-load-data "mysql-importing-data-any-source.md#mysql-importing-data-any-source-load-data") in the Importing data
from any source procedure.

Before you start the backup operation, make sure to set the replication options on the
MySQL database that you are copying to Amazon RDS. The replication options include turning on
binary logging and setting a unique server ID. Setting these options causes your server
to start logging database transactions and prepares it to be a source replication
instance later in this process.

Make sure that you're aware of the following recommendations and
considerations:

- Use the `--single-transaction` option with `mysqldump`
  because it dumps a consistent state of the database. To ensure a valid dump
  file, don't run data definition language (DDL) statements while
  `mysqldump` is running. You can schedule a maintenance window for
  these operations.
- Exclude the following schemas from the dump file:

      + `sys`
      + `performance_schema`
      + `information_schema`

  The `mysqldump` utility excludes
  these schemas by default.

- If you need to migrate users and privileges, consider using a tool that
  generates the data control language (DCL) for recreating them, such as the
  [pt-show-grants](https://www.percona.com/doc/percona-toolkit/LATEST/pt-show-grants.html "https://www.percona.com/doc/percona-toolkit/LATEST/pt-show-grants.html") utility.

### To

set replication options

1. Edit the `my.cnf` file. This file is usually located under
   `/etc`.

```
sudo vi /etc/my.cnf
```

Add the `log_bin` and `server_id` options to the
`[mysqld]` section. The `log_bin` option provides
a file name identifier for binary log files. The `server_id`
option provides a unique identifier for the server in source-replica
relationships.

The following example shows the updated `[mysqld]` section of a
`my.cnf` file:

```
[mysqld]
log-bin=mysql-bin
server-id=1
```

For more information, see [Setting the Replication Source Configuration](https://dev.mysql.com/doc/refman/8.4/en/replication-howto-masterbaseconfig.html "https://dev.mysql.com/doc/refman/8.4/en/replication-howto-masterbaseconfig.html") in the MySQL
documentation. 2. For replication with a Multi-AZ DB cluster set the `ENFORCE_GTID_CONSISTENCY`
and the `GTID_MODE` parameter to `ON`.

```
mysql> SET @@GLOBAL.ENFORCE_GTID_CONSISTENCY = ON;
```

```
mysql> SET @@GLOBAL.GTID_MODE = ON;
```

These settings aren't required for replication with a DB instance. 3. Restart the `mysql` service.

```
sudo service mysqld restart
```

### To create a

backup copy of your existing database

1. Create a backup of your data using the `mysqldump` utility,
   specifying either SQL or delimited-text format.

For MySQL 8.0.25 and lower versions, specify `--master-data=2`
to create a backup file that can be used to start replication between
servers. For MySQL 8.0.26 and higher versions, specify
`--source-data=2` to create a backup file that can be used to
start replication between servers. For more information, see the [mysqldump
— A Database Backup Program](https://dev.mysql.com/doc/refman/8.4/en/mysqldump.html "https://dev.mysql.com/doc/refman/8.4/en/mysqldump.html") in the MySQL
documentation.

To improve performance and ensure data integrity, use the
`--order-by-primary` and `--single-transaction`
options for `mysqldump`.

To
avoid including the MySQL system database in the backup, don't use the
`--all-databases` option with `mysqldump`. For
more information, see [Creating a Data Snapshot Using mysqldump](https://dev.mysql.com/doc/mysql-replication-excerpt/8.0/en/replication-howto-mysqldump.html "https://dev.mysql.com/doc/mysql-replication-excerpt/8.0/en/replication-howto-mysqldump.html") in the MySQL
documentation.

Use `chmod`, if necessary, to make sure that the directory
where the backup file is being created is writeable.

###### Important

On Windows, run the command window as an administrator.

    * To produce SQL output, use the following command:


    For Linux, macOS, or Unix:



    ```
    sudo mysqldump \
        --databases `database_name` \
        --master-data=2  \
        --single-transaction \
        --order-by-primary \
        -r backup.sql \
        -u `local_user` \
        -p`password`
    ```

    ###### Note

    As a security best practice, specify credentials other than
     the prompts shown in the example.


    For Windows:



    ```
    mysqldump ^
        --databases `database_name` ^
        --master-data=2  ^
        --single-transaction ^
        --order-by-primary ^
        -r backup.sql ^
        -u `local_user` ^
        -p`password`
    ```

    ###### Note

    As a security best practice, specify credentials other than
     the prompts shown in the example.
    * To produce delimited-text output, use the following
     command:


    For Linux, macOS, or Unix:



    ```
    sudo mysqldump \
        --tab=`target_directory` \
        --fields-terminated-by ',' \
        --fields-enclosed-by '"' \
        --lines-terminated-by 0x0d0a \
        `database_name` \
        --master-data=2 \
        --single-transaction \
        --order-by-primary \
        -p`password`
    ```

    For Windows:



    ```
    mysqldump ^
        --tab=`target_directory` ^
        --fields-terminated-by "," ^
        --fields-enclosed-by """ ^
        --lines-terminated-by 0x0d0a ^
        `database_name` ^
        --master-data=2 ^
        --single-transaction ^
        --order-by-primary ^
        -p`password`
    ```

    ###### Note

    As a security best practice, specify credentials other than
     the prompts shown in the example.

    Make sure to create any stored procedures, triggers,
     functions, or events manually in your Amazon RDS database. If you
     have any of these objects in the database that you are copying,
     then exclude them when you run `mysqldump`. To do so,
     include the following arguments with your `mysqldump`
     command:



    	+ `--routines=0`
    	+ `--triggers=0`
    	+ `--events=0`
    For MySQL 8.0.22 and lower versions, when you run
     `mysqldump` and specify the delimited-text format, a
     `CHANGE MASTER TO` comment is returned. This comment
     contains the master log file name and position. For MySQL 8.0.23 and
     higher versions, when you run `mysqldump` using the
     delimited-text format, a `CHANGE REPLICATION SOURCE TO`
     comment is returned. This comment contains the source log file name
     and position. If the external instance is MySQL 8.0.23 and higher
     versions, note the values for `MASTER_LOG_FILE` and
     `MASTER_LOG_POS`. You need these values when setting
     up replication.


    The following output is returned for MySQL 8.0.22 and lower
     versions:



    ```
    -- Position to start replication or point-in-time recovery from
    --
    -- CHANGE MASTER TO MASTER_LOG_FILE='mysql-bin-changelog.000031', MASTER_LOG_POS=107;
    ```

    The following output is returned for MySQL 8.0.23 and higher
     versions:



    ```
    -- Position to start replication or point-in-time recovery from
    --
    -- CHANGE SOURCE TO SOURCE_LOG_FILE='mysql-bin-changelog.000031', SOURCE_LOG_POS=107;
    ```

    For MySQL 8.0.22 and lower versions, if you are using SQL format,
     you can get the master log file name and position in the
     `CHANGE MASTER TO` comment in the backup file. For
     MySQL 8.0.23 and higher versions, if you are using SQL format, you
     can get the source log file name and position in the `CHANGE
     REPLICATION SOURCE TO` comment in the backup file.

2. Compress the copied data to reduce the amount of network resources needed
   to copy your data to the Amazon RDS database. Note the size of the backup file.
   You need this information when determining how large an Amazon EC2 instance to
   create. When you are done, compress the backup file using GZIP or your
   preferred compression utility.
   - To compress SQL output, use the following command:

   ```
   gzip backup.sql
   ```

   - To compress delimited-text output, use the following
     command:

   ```
   tar -zcvf backup.tar.gz `target_directory`
   ```

## Task 2:

Create an Amazon EC2 instance and copy the compressed database

Copying your compressed database backup file to an Amazon EC2 instance takes fewer network
resources than doing a direct copy of uncompressed data between database instances.
After your data is in Amazon EC2, you can copy it from there directly to your MySQL database.
For you to save on the cost of network resources, your Amazon EC2 instance must be in the
same AWS Region as your Amazon RDS DB instance. Having the Amazon EC2 instance in the same
AWS Region as your Amazon RDS database also reduces network latency during the
import.

The following diagram shows copying the database backup to an Amazon EC2 instance.

![Workflow that shows copying the database backup to an Amazon EC2 instance.](images/MigrateMySQLToRDS_3.png)

### To create an

Amazon EC2 instance and copy your data

1. In the AWS Region where you plan to create the Amazon RDS database, create a
   virtual private cloud (VPC), a VPC security group, and a VPC subnet. Ensure
   that the inbound rules for your VPC security group allow the IP addresses
   required for your application to connect to AWS. You can specify a range
   of IP addresses—for example, `203.0.113.0/24`—or
   another VPC security group. You can use the [Amazon VPC console](https://console.aws.amazon.com/vpc "https://console.aws.amazon.com/vpc") to create and manage VPCs, subnets, and security
   groups. For more information, see [Getting started with Amazon VPC](../../../vpc/latest/userguide/what-is-amazon-vpc.md#getting-started "../../../vpc/latest/userguide/what-is-amazon-vpc.md#getting-started") in the _Amazon Virtual Private Cloud User
   Guide_.
2. Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2") and choose
   the AWS Region to contain both your Amazon EC2 instance and your Amazon RDS
   database. Launch an Amazon EC2 instance using the VPC, subnet, and security group
   that you created in Step 1. Ensure that you select an instance type with
   enough storage for your database backup file when it is uncompressed. For
   details on Amazon EC2 instances, see [Getting started with
   Amazon EC2](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md") in the _Amazon Elastic Compute Cloud User
   Guide_.
3. To connect to your Amazon RDS database from your Amazon EC2 instance, edit your VPC
   security group. Add an inbound rule specifying the private IP address of
   your EC2 instance. You can find the private IP address on the
   **Details** tab of the **Instance**
   pane in the EC2 console window. To edit the VPC security group and add an
   inbound rule, choose **Security Groups** in the EC2 console
   navigation pane, choose your security group, and then add an inbound rule
   for MySQL or Aurora specifying the private IP address of your EC2 instance.
   To learn how to add an inbound rule to a VPC security group, see [Security group
   rules](../../../vpc/latest/userguide/security-group-rules.md "../../../vpc/latest/userguide/security-group-rules.md") in the _Amazon Virtual Private Cloud User Guide_.
4. Copy your compressed database backup file from your local system to your
   Amazon EC2 instance. Use `chmod`, if necessary, to make sure that you
   have write permission for the target directory of the Amazon EC2 instance. You
   can use `scp` or a Secure Shell (SSH) client to copy the file.
   The following command is an example `scp` command:

```
scp -r -i `key pair`.pem backup.sql.gz ec2-user@`EC2 DNS`:/`target_directory`/backup.sql.gz
```

###### Important

When copying sensitive data, be sure to use a secure network transfer
protocol. 5. Connect to your Amazon EC2 instance and install the latest updates and the
MySQL client tools using the following commands:

```
sudo yum update -y
sudo yum install mysql -y
```

For more information, see [Connect to your instance](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-connect-to-instance-linux "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-connect-to-instance-linux") for Linux instances in the
_Amazon Elastic Compute Cloud User Guide_.

###### Important

This example installs the MySQL client on an Amazon Machine Image
(AMI) for an Amazon Linux distribution. This example doesn't install the
MySQL client on a different distribution, such as Ubuntu or Red Hat
Enterprise Linux. For information about installing MySQL, see [Installing MySQL](https://dev.mysql.com/doc/refman/8.4/en/installing.html "https://dev.mysql.com/doc/refman/8.4/en/installing.html") in the MySQL documentation. 6. While connected to your Amazon EC2 instance, decompress your database backup
file. The following commands are examples.

    * To decompress SQL output, use the following command:



    ```
    gzip backup.sql.gz -d
    ```
    * To decompress delimited-text output, use the following
     command:



    ```
    tar xzvf backup.tar.gz
    ```

## Task

3: Create a MySQL database and import data from your Amazon EC2 instance

By creating an RDS for MySQL DB instance or an RDS for MySQL Multi-AZ DB cluster in the same AWS Region
as your Amazon EC2 instance, you can import the database backup file from Amazon EC2 faster than
over the internet.

The following diagram shows importing the backup from an Amazon EC2 instance into a MySQL
database.

![Workflow that shows importing the backup from the EC2 instance into the MySQL database.](images/MigrateMySQLToRDS_4.png)

### To create a

MySQL database and import your data

1. Determine which DB instance class and what amount of storage space is
   required to support the expected workload for this Amazon RDS database. As part
   of this process, decide what is sufficient space and processing capacity for
   your data load procedures. Also, decide what is required to handle the
   production workload. You can estimate this based on the size and resources
   of the source MySQL database. For more information, see [DB instance classes](Concepts.md "Concepts.md").
2. Create a DB instance or Multi-AZ DB cluster in the AWS Region that contains your Amazon EC2
   instance.

To create an RDS for MySQL Multi-AZ DB cluster, follow the instructions in [Creating a Multi-AZ DB cluster for Amazon RDS](create-multi-az-db-cluster.md "create-multi-az-db-cluster.md").

To create an RDS for MySQL DB instance, follow the instructions in [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md")
and use the following guidelines:

    * Specify a DB engine version that is compatible with your source DB
     instance.
    * Specify the same virtual private cloud (VPC) and VPC security
     group as for your Amazon EC2 instance. This approach ensures that your
     Amazon EC2 instance and your Amazon RDS instance are visible to each other
     over the network. Make sure your DB instance is publicly accessible.
     To set up replication with your source database as described in a
     following section, your DB instance must be publicly
     accessible.
    * Don't configure multiple Availability Zones, backup retention, or
     read replicas until after you have imported the database backup.
     When that import is completed, you can configure Multi-AZ and backup
     retention for the production instance.

3. Review the default configuration options for the Amazon RDS database. If the
   default parameter group for the database doesn't have the configuration
   options that you want, find a different one that does or create a new
   parameter group. For more information about creating a parameter group, see
   [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
4. Connect to the new Amazon RDS database as the master user. Create the users
   required to support the administrators, applications, and services that need
   to access the DB instance. The hostname for the Amazon RDS database is the
   **Endpoint** value for this DB instance without the
   port number, for example,
   `mysampledb.123456789012.us-west-2.rds.amazonaws.com`. You can find
   the endpoint value in the database details in the Amazon RDS console.
5. Connect to your Amazon EC2 instance. For more information, see [Connect to your instance](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-connect-to-instance-linux "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-connect-to-instance-linux") for Linux instances in the
   _Amazon Elastic Compute Cloud User Guide_.
6. Connect to your Amazon RDS database as a remote host from your Amazon EC2 instance
   using the `mysql` command. The following command is an
   example:

```
mysql -h `host_name` -P 3306 -u `db_master_user` -p
```

The `host_name` is the Amazon RDS database
endpoint. 7. At the `mysql` prompt, run the `source` command and
pass it the name of your database dump file. This command loads the data
into the Amazon RDS DB instance.

    * For SQL format, use the following command:



    ```
    mysql> source backup.sql;
    ```
    * For delimited-text format, first create the database, if it
     isn't the default database that you created when setting up the
     Amazon RDS database.



    ```
    mysql> create database `database_name`;
    mysql> use `database_name`;
    ```

    Then create the tables.



    ```
    mysql> source `table1`.sql
    mysql> source `table2`.sql
    etc...
    ```

    Then import the data.



    ```
    mysql> LOAD DATA LOCAL INFILE 'table1.txt' INTO TABLE table1 FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '0x0d0a';
    mysql> LOAD DATA LOCAL INFILE 'table2.txt' INTO TABLE table2 FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '0x0d0a';
    etc...
    ```

    To improve performance, you can perform these operations in
     parallel from multiple connections so that all of your tables are
     created and then loaded at the same time.


    ###### Note

    If you used any data-formatting options with
     `mysqldump` when you initially dumped the table,
     make sure to use the same options with `LOAD DATA LOCAL
     INFILE` to ensure proper interpretation of the data
     file contents.

8. Run a simple `SELECT` query against one or two of the tables in
   the imported database to verify that the import was successful.

If you no longer need the Amazon EC2 instance used in this procedure, terminate the EC2
instance to reduce your AWS resource usage. To terminate an EC2 instance, see
[Terminate an instance](../../../AWSEC2/latest/UserGuide/terminating-instances.md#terminating-instances-console "../../../AWSEC2/latest/UserGuide/terminating-instances.md#terminating-instances-console") in the _Amazon Elastic Compute Cloud User
Guide_.

## Task 4: Replicate

data from your external database to your new Amazon RDS database

Your source database was likely updated during the time that it took to copy and
transfer the data to the MySQL database. Thus, you can use replication to bring the
copied database up-to-date with the source database.

![Workflow that shows replicating data from the external MySQL database to the database on Amazon RDS.](images/MigrateMySQLToRDS_5.png)

The permissions required to start replication on an Amazon RDS database are restricted and
aren't available to your Amazon RDS master user. Because of this, use the appropriate Amazon RDS
stored procedure for your major engine version:

- [mysql_rds_set_external_master
  (RDS for MySQL major versions 8.0 and lower)](mysql-stored-proc-replicating.md#mysql_rds_set_external_master "mysql-stored-proc-replicating.md#mysql_rds_set_external_master")
- [mysql.rds_set_external_source (RDS for MySQL major versions 8.4 and higher)](mysql-stored-proc-replicating.md#mysql_rds_set_external_source "mysql-stored-proc-replicating.md#mysql_rds_set_external_source")
- [mysql.rds_set_external_master_gtid](mysql_rds_set_external_master_gtid.md "mysql_rds_set_external_master_gtid.md") to configure
  replication and [mysql.rds_start_replication](mysql-stored-proc-replicating.md#mysql_rds_start_replication "mysql-stored-proc-replicating.md#mysql_rds_start_replication") to start replication

### To start

replication

In Task 1, [when you
set replication options](#mysql-importing-data-reduced-downtime-set-replication-options "#mysql-importing-data-reduced-downtime-set-replication-options"), you turned on binary logging and set a unique
server ID for your source database. Now, you can set up your Amazon RDS database as a
replica with your live database as the source replication instance.

1. In the Amazon RDS console, add the IP address of the server that hosts the
   source database to the VPC security group for the Amazon RDS database. For more
   information on configuring a VPC security group, see [Configure security group rules](../../../vpc/latest/userguide/working-with-security-group-rules.md "../../../vpc/latest/userguide/working-with-security-group-rules.md") in the _Amazon Virtual Private Cloud User
   Guide_.

You might also need to configure your local network to permit connections
from the IP address of your Amazon RDS database so that it can communicate with
your source instance. To find the IP address of the Amazon RDS database, use the
`host` command:

```
host `host_name`
```

The `host_name` is the DNS name from the Amazon RDS
database endpoint, for example
`myinstance.123456789012.us-east-1.rds.amazonaws.com`. You
can find the endpoint value in the DB instance details in the Amazon RDS
console. 2. Using the client of your choice, connect to the source instance and create
a user to be used for replication. This account is used solely for
replication and must be restricted to your domain to improve security. The
following command is an example:

```
CREATE USER 'repl_user'@'`mydomain.com`' IDENTIFIED BY '`password`';
```

###### Note

Specify credentials other than the prompts shown here as a security
best practice. 3. For the source instance, grant `REPLICATION CLIENT` and
`REPLICATION SLAVE` privileges to your replication user. For
example, to grant the `REPLICATION CLIENT` and `REPLICATION
 SLAVE` privileges on all databases for the
'`repl_user`' user for your domain, issue the following
command:

```
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO '`repl_user`'@'`mydomain.com`';
```

4.  Make the Amazon RDS database the replica. Connect to the Amazon RDS database as the
    master user and identify the source database as the source replication
    instance by using the appropriate Amazon RDS stored procedure:

        * [mysql\_rds\_set\_external\_master (RDS for MySQL major versions 8.0
         and lower)](mysql-stored-proc-replicating.md#mysql_rds_set_external_master "mysql-stored-proc-replicating.md#mysql_rds_set_external_master")
        * [mysql.rds\_set\_external\_source (RDS for MySQL major versions 8.4 and higher)](mysql-stored-proc-replicating.md#mysql_rds_set_external_source "mysql-stored-proc-replicating.md#mysql_rds_set_external_source")

    If you have a SQL format backup file, use the master log file name and
    master log position that you determined in Step 4. If you used
    delimited-text format, use the name and position that you determined when
    creating the backup files. The following commands are examples:

**MySQL 8.4 and higher versions**

```
CALL mysql.rds_set_external_source ('myserver.mydomain.com', 3306,
    'repl_user', '`password`', 'mysql-bin-changelog.000031', 107, 1);
```

**MySQL 8.0 and lower versions**

```
CALL mysql.rds_set_external_master ('myserver.mydomain.com', 3306,
    'repl_user', '`password`', 'mysql-bin-changelog.000031', 107, 1);
```

###### Note

Specify credentials other than the prompts shown here as a security
best practice. 5. On the Amazon RDS database, to start replication, run the following command
that uses the [mysql.rds_start_replication](mysql-stored-proc-replicating.md#mysql_rds_start_replication "mysql-stored-proc-replicating.md#mysql_rds_start_replication") stored procedure:

```
CALL mysql.rds_start_replication;
```

6. On the Amazon RDS database, to determine when the replica is up to date with
   the source replication instance, run the [SHOW REPLICA STATUS](https://dev.mysql.com/doc/refman/8.0/en/show-replica-status.html "https://dev.mysql.com/doc/refman/8.0/en/show-replica-status.html") command. The results of the `SHOW
REPLICA STATUS` command include the
   `Seconds_Behind_Master` field. When the
   `Seconds_Behind_Master` field returns 0, then the replica is
   up to date with the source replication instance.

###### Note

Previous versions of MySQL used `SHOW SLAVE STATUS` instead
of `SHOW REPLICA STATUS`. If you are using a MySQL version
before 8.0.23, then use `SHOW SLAVE STATUS`. 7. After the Amazon RDS database is up to date, turn on automated backups so you
can restore that database if needed. You can turn on or modify automated
backups for your Amazon RDS database by using the [Amazon RDS console](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/"). For more information, see [Introduction to backups](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md").

## Task 5: Redirect

your live application to your Amazon RDS instance

After the MySQL database is up to date with the source replication instance, you can
now update your live application to use the Amazon RDS instance.

![Workflow that shows stopping replication and directing the live application to the database on Amazon RDS.](images/MigrateMySQLToRDS_6.png)

### To

redirect your live application to your MySQL database and stop
replication

1. To add the VPC security group for the Amazon RDS database, add the IP address
   of the server that hosts the application. For more information on modifying
   a VPC security group, see [Configure security group rules](../../../vpc/latest/userguide/working-with-security-group-rules.md "../../../vpc/latest/userguide/working-with-security-group-rules.md") in the _Amazon Virtual Private Cloud User
   Guide_.
2. Verify that the `Seconds_Behind_Master` field in the [SHOW REPLICA STATUS](https://dev.mysql.com/doc/refman/8.0/en/show-replica-status.html "https://dev.mysql.com/doc/refman/8.0/en/show-replica-status.html") command results is 0, which indicates that
   the replica is up to date with the source replication instance.

```
SHOW REPLICA STATUS;
```

###### Note

Previous versions of MySQL used `SHOW SLAVE STATUS` instead
of `SHOW REPLICA STATUS`. If you are using a MySQL version
before 8.0.23, then use `SHOW SLAVE STATUS`. 3. Close all connections to the source when their transactions
complete. 4. Update your application to use the Amazon RDS database. This update typically
involves changing the connection settings to identify the hostname and port
of the Amazon RDS database, the user account and password to connect with, and
the database to use. 5. Connect to the DB instance.

For a Multi-AZ DB cluster, connect to the writer DB instance. 6. Stop replication for the Amazon RDS instance by running the following command
that uses the [mysql.rds_stop_replication](mysql-stored-proc-replicating.md#mysql_rds_stop_replication "mysql-stored-proc-replicating.md#mysql_rds_stop_replication") stored procedure:

```
CALL mysql.rds_stop_replication;
```

7.  Reset the replication configuration so this instance is no longer
    identified as a replica by using the appropriate Amazon RDS stored procedure on
    your Amazon RDS database:

        * [mysql\_rds\_reset\_external\_master (RDS for MySQL major versions 8.0
         and lower)](mysql-stored-proc-replicating.md#mysql_rds_reset_external_master "mysql-stored-proc-replicating.md#mysql_rds_reset_external_master")
        * [mysql.rds\_reset\_external\_source
         (RDS for MySQL major versions 8.4 and
         higher)](mysql-stored-proc-replicating.md#mysql_rds_reset_external_source "mysql-stored-proc-replicating.md#mysql_rds_reset_external_source")

    **MySQL 8.4 and higher versions**

```
CALL mysql.rds_reset_external_source;
```

**MySQL 8.0 and lower versions**

```
CALL mysql.rds_reset_external_master;
```

8. Turn on additional Amazon RDS features such as Multi-AZ support and read
   replicas. For more information, see [Configuring and managing a Multi-AZ deployment for Amazon RDS](Concepts.md "Concepts.md") and [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").
