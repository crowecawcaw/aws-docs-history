# Migrating an RDS for MySQL snapshot to Aurora

You can migrate a DB snapshot of an RDS for MySQL DB instance to create an Aurora MySQL DB cluster. The new Aurora MySQL DB
cluster is populated with the data from the original RDS for MySQL DB instance. The DB snapshot must have been made from an
Amazon RDS DB instance running a MySQL version that's compatible with Aurora MySQL.

You can migrate either a manual or automated DB snapshot. After the DB cluster is
created, you can then create optional Aurora Replicas.

###### Note

You can also migrate an RDS for MySQL DB instance to an Aurora MySQL DB cluster by creating an Aurora read replica of your
source RDS for MySQL DB instance. For more information, see [Migrating data from an RDS for MySQL DB instance to an Amazon Aurora MySQL DB cluster by using an Aurora read replica](AuroraMySQL.Migrating.RDSMySQL.md "AuroraMySQL.Migrating.RDSMySQL.md").

You can't migrate to Aurora MySQL version 3.05 and higher from some older MySQL 8.0 versions, including 8.0.11, 8.0.13,
and 8.0.15. We recommend that you upgrade to MySQL version 8.0.28 before migrating.

The general steps you must take are as follows:

1. Determine the amount of space to provision for your Aurora MySQL DB cluster. For more information, see
   [How much space do I need?](#AuroraMySQL.Migrating.RDSMySQL.Space "#AuroraMySQL.Migrating.RDSMySQL.Space")
2. Use the console to create the snapshot in the AWS Region where the Amazon RDS
   MySQL instance is located. For information about creating a DB snapshot, see
   [Creating a DB
   snapshot](../UserGuide/USER_CreateSnapshot.md "../UserGuide/USER_CreateSnapshot.md").
3. If the DB snapshot is not in the same AWS Region as your DB cluster, use
   the Amazon RDS console to copy the DB snapshot to that AWS Region. For
   information about copying a DB snapshot, see [Copying a DB
   snapshot](../UserGuide/USER_CopySnapshot.md "../UserGuide/USER_CopySnapshot.md").
4. Use the console to migrate the DB snapshot and create an Aurora MySQL DB
   cluster with the same databases as the original MySQL DB instance.

###### Warning

Amazon RDS limits each AWS account to one snapshot copy into each AWS Region at a
time.

## How much space do I need?

When you migrate a snapshot of a MySQL DB instance into an Aurora MySQL DB
cluster, Aurora uses an Amazon Elastic Block Store (Amazon EBS) volume to format the data from the
snapshot before migrating it. In some cases, additional space is needed to
format the data for migration.

Tables that are not MyISAM tables and are not compressed can be up to 16 TB in
size. If you have MyISAM tables, then Aurora must use additional space in the
volume to convert the tables to be compatible with Aurora MySQL. If you have
compressed tables, then Aurora must use additional space in the volume to expand
these tables before storing them on the Aurora cluster volume. Because of this
additional space requirement, you should ensure that none of the MyISAM and
compressed tables being migrated from your MySQL DB instance exceeds 8 TB in
size.

## Reducing the amount of space required to migrate data into Amazon Aurora MySQL

You might want to modify your database schema prior to migrating it into
Amazon Aurora. Such modification can be helpful in the following cases:

- You want to speed up the migration process.
- You are unsure of how much space you need to provision.
- You have attempted to migrate your data and the migration has failed
  due to a lack of provisioned space.

You can make the following changes to improve the process of migrating a
database into Amazon Aurora.

###### Important

Be sure to perform these updates on a new DB instance restored from a
snapshot of a production database, rather than on a production instance. You
can then migrate the data from the snapshot of your new DB instance into
your Aurora DB cluster to avoid any service interruptions on your production
database.

| Table type        | Limitation or guideline                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MyISAM tables     | Aurora MySQL supports InnoDB tables only. If you have MyISAM<br>tables in your database, then those tables must be converted<br>before being migrated into Aurora MySQL. The conversion<br>process requires additional space for the MyISAM to InnoDB<br>conversion during the migration procedure.<br>To reduce your chances of running out of space or to speed<br>up the migration process, convert all of your MyISAM tables<br>to InnoDB tables before migrating them. The size of the<br>resulting InnoDB table is equivalent to the size required by<br>Aurora MySQL for that table. To convert a MyISAM table to<br>InnoDB, run the following command:<br>`alter table <schema>.<table_name><br>engine=innodb, algorithm=copy;` |
| Compressed tables | Aurora MySQL doesn't support compressed tables (that is,<br>tables created with `ROW_FORMAT=COMPRESSED`).<br>To reduce your chances of running out of space or to speed up the migration process, expand your<br>compressed tables by setting `ROW_FORMAT` to `DEFAULT`, `COMPACT`,<br>`DYNAMIC`, or `REDUNDANT`. For more information, see [InnoDB row formats](https://dev.mysql.com/doc/refman/8.0/en/innodb-row-format.html "https://dev.mysql.com/doc/refman/8.0/en/innodb-row-format.html")<br>in the MySQL documentation.                                                                                                                                                                                                        |

You can use the following SQL script on your existing MySQL DB instance to
list the tables in your database that are MyISAM tables or compressed
tables.

```
-- This script examines a MySQL database for conditions that block
-- migrating the database into Amazon Aurora.
-- It needs to be run from an account that has read permission for the
-- INFORMATION_SCHEMA database.

-- Verify that this is a supported version of MySQL.

select msg as `==> Checking current version of MySQL.`
from
  (
  select
    'This script should be run on MySQL version 5.6 or higher. ' +
    'Earlier versions are not supported.' as msg,
    cast(substring_index(version(), '.', 1) as unsigned) * 100 +
      cast(substring_index(substring_index(version(), '.', 2), '.', -1)
      as unsigned)
    as major_minor
  ) as T
where major_minor <> 506;


-- List MyISAM and compressed tables. Include the table size.

select concat(TABLE_SCHEMA, '.', TABLE_NAME) as `==> MyISAM or Compressed Tables`,
round(((data_length + index_length) / 1024 / 1024), 2) "Approx size (MB)"
from INFORMATION_SCHEMA.TABLES
where
  ENGINE <> 'InnoDB'
  and
  (
    -- User tables
    TABLE_SCHEMA not in ('mysql', 'performance_schema',
                         'information_schema')
    or
    -- Non-standard system tables
    (
      TABLE_SCHEMA = 'mysql' and TABLE_NAME not in
        (
          'columns_priv', 'db', 'event', 'func', 'general_log',
          'help_category', 'help_keyword', 'help_relation',
          'help_topic', 'host', 'ndb_binlog_index', 'plugin',
          'proc', 'procs_priv', 'proxies_priv', 'servers', 'slow_log',
          'tables_priv', 'time_zone', 'time_zone_leap_second',
          'time_zone_name', 'time_zone_transition',
          'time_zone_transition_type', 'user'
        )
    )
  )
  or
  (
    -- Compressed tables
       ROW_FORMAT = 'Compressed'
  );
```

The script produces output similar to the output in the following example. The
example shows two tables that must be converted from MyISAM to InnoDB. The
output also includes the approximate size of each table in megabytes (MB).

```
+---------------------------------+------------------+
| ==> MyISAM or Compressed Tables | Approx size (MB) |
+---------------------------------+------------------+
| test.name_table                 |          2102.25 |
| test.my_table                   |            65.25 |
+---------------------------------+------------------+
2 rows in set (0.01 sec)
```

## Migrating an RDS for MySQL DB snapshot to an Aurora MySQL DB cluster

You can migrate a DB snapshot of an RDS for MySQL DB instance to create an Aurora MySQL DB cluster using the AWS Management Console or
the AWS CLI. The new Aurora MySQL DB cluster is populated with the data from the original RDS for MySQL DB instance. For
information about creating a DB snapshot, see [Creating a DB
snapshot](../UserGuide/USER_CreateSnapshot.md "../UserGuide/USER_CreateSnapshot.md").

If the DB snapshot is not in the AWS Region where you want to locate your data, copy the DB snapshot to that AWS
Region. For information about copying a DB snapshot, see [Copying a DB
snapshot](../UserGuide/USER_CopySnapshot.md "../UserGuide/USER_CopySnapshot.md").

When you migrate the DB snapshot by using the AWS Management Console, the console takes the actions necessary to create
only the DB cluster.

You can also choose for your new Aurora MySQL DB cluster to be encrypted at rest using an AWS KMS key.

###### To migrate a MySQL DB snapshot by using the AWS Management Console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Either start the migration from the MySQL DB instance or from the snapshot:

To start the migration from the DB instance:

    1. In the navigation pane, choose **Databases**, and then select the MySQL DB
     instance.
    2. For **Actions**, choose **Migrate latest snapshot**.

To start the migration from the snapshot:

    1. Choose **Snapshots**.
    2. On the **Snapshots** page, choose the snapshot that you want to migrate into
     an Aurora MySQL DB cluster.
    3. Choose **Snapshot Actions**, and then choose **Migrate
     Snapshot**.

The **Migrate Database** page appears. 3. Set the following values on the **Migrate Database** page:

    * **Migrate to DB Engine**: Select `aurora`.
    * **DB Engine Version**: Select the DB engine version for the Aurora MySQL DB
     cluster.
    * **DB Instance Class**: Select a DB instance class that has the required
     storage and capacity for your database, for example `db.r3.large`. Aurora cluster
     volumes automatically grow as the amount of data in your database increases. An Aurora cluster
     volume can grow to a maximum size of 128 tebibytes (TiB). So you only need to select a DB
     instance class that meets your current storage requirements. For more information, see [Overview of Amazon Aurora storage](Aurora.Overview.md#Aurora.Overview.Storage "Aurora.Overview.md#Aurora.Overview.Storage").
    * **DB Instance Identifier**: Type a name for the DB cluster that is unique for
     your account in the AWS Region you selected. This identifier is used in the endpoint addresses
     for the instances in your DB cluster. You might choose to add some intelligence to the name,
     such as including the AWS Region and DB engine you selected, for example
     `aurora-cluster1`.


    The DB instance identifier has the following constraints:




    	+ It must contain from 1 to 63 alphanumeric characters or hyphens.
    	+ Its first character must be a letter.
    	+ It cannot end with a hyphen or contain two consecutive hyphens.
    	+ It must be unique for all DB instances per AWS account, per AWS Region.
    * **Virtual Private Cloud (VPC)**: If you have an existing VPC, then you can
     use that VPC with your Aurora MySQL DB cluster by selecting your VPC identifier, for example
     `vpc-a464d1c1`. For information on creating a VPC, see [Tutorial: Create a VPC for use with a DB cluster (IPv4 only)](CHAP_Tutorials.WebServerDB.md "CHAP_Tutorials.WebServerDB.md").


    Otherwise, you can choose to have Aurora create a VPC for you by selecting **Create a
     new VPC**.
    * **DB subnet group**: If you have an existing subnet group, then you can use
     that subnet group with your Aurora MySQL DB cluster by selecting your subnet group identifier,
     for example `gs-subnet-group1`.


    Otherwise, you can choose to have Aurora create a subnet group for you by selecting
     **Create a new subnet group**.
    * **Public accessibility**: Select **No** to specify that
     instances in your DB cluster can only be accessed by resources inside of your VPC. Select
     **Yes** to specify that instances in your DB cluster can be accessed by
     resources on the public network. The default is **Yes**.


    ###### Note

    Your production DB cluster might not need to be in a public subnet, because only your
     application servers require access to your DB cluster. If your DB cluster doesn't need to be
     in a public subnet, set **Publicly Accessible** to
     **No**.
    * **Availability Zone**: Select the Availability Zone to host the primary
     instance for your Aurora MySQL DB cluster. To have Aurora select an Availability Zone for you,
     select **No Preference**.
    * **Database Port**: Type the default port to be used when connecting to
     instances in the Aurora MySQL DB cluster. The default is `3306`.


    ###### Note

    You might be behind a corporate firewall that doesn't allow access to default ports such
     as the MySQL default port, 3306. In this case, provide a port value that your corporate
     firewall allows. Remember that port value later when you connect to the Aurora MySQL DB
     cluster.
    * **Encryption**: Choose **Enable Encryption** for your new
     Aurora MySQL DB cluster to be encrypted at rest. If you choose **Enable
     Encryption**, you must choose a KMS key as the
     **AWS KMS key** value.


    If your DB snapshot isn't encrypted, specify an encryption key to have your DB cluster
     encrypted at rest.


    If your DB snapshot is encrypted, specify an encryption key to have your DB cluster encrypted
     at rest using the specified encryption key. You can specify the encryption key used by the DB
     snapshot or a different key. You can't create an unencrypted DB cluster from an encrypted
     DB snapshot.
    * **Auto Minor Version Upgrade**: This setting doesn't apply to Aurora MySQL DB
     clusters.


    For more information about engine updates for Aurora MySQL, see [Database engine updates for Amazon Aurora MySQL](AuroraMySQL.md "AuroraMySQL.md").

4. Choose **Migrate** to migrate your DB snapshot.
5. Choose **Instances**, and then choose the arrow icon to show the DB cluster details
   and monitor the progress of the migration. On the details page, you can find the cluster endpoint used
   to connect to the primary instance of the DB cluster. For more information on connecting to an
   Aurora MySQL DB cluster, see [Connecting to an Amazon Aurora DB cluster](Aurora.md "Aurora.md").
   You can create an Aurora DB cluster from a DB snapshot of an RDS for MySQL DB instance by using the [`restore-db-cluster-from-snapshot`](../../../cli/latest/reference/rds/restore-db-cluster-from-snapshot.md "../../../cli/latest/reference/rds/restore-db-cluster-from-snapshot.md") command with the following parameters:

- `--db-cluster-identifier` – The name of the DB cluster to create.
- `--engine aurora-mysql` – For a MySQL 5.7–compatible or 8.0–compatible
  DB cluster.
- `--kms-key-id` – The AWS KMS key to optionally encrypt the DB cluster with,
  depending on whether your DB snapshot is encrypted.
  - If your DB snapshot isn't encrypted, specify an encryption key to have your DB cluster
    encrypted at rest. Otherwise, your DB cluster isn't encrypted.
  - If your DB snapshot is encrypted, specify an encryption key to have your DB cluster encrypted
    at rest using the specified encryption key. Otherwise, your DB cluster is encrypted at rest
    using the encryption key for the DB snapshot.

  ###### Note

  You can't create an unencrypted DB cluster from an encrypted DB snapshot.

- `--snapshot-identifier` – The Amazon Resource Name (ARN) of the DB snapshot to
  migrate. For more information about Amazon RDS ARNs, see [Amazon Relational Database Service (Amazon RDS)](../../../general/latest/gr/aws-arns-and-namespaces.md#arn-syntax-rds "../../../general/latest/gr/aws-arns-and-namespaces.md#arn-syntax-rds").
  When you migrate the DB snapshot by using the `RestoreDBClusterFromSnapshot` command, the command
  creates both the DB cluster and the primary instance.

In this example, you create a MySQL 5.7–compatible DB cluster named
`mydbcluster` from a DB snapshot with an ARN set to
`mydbsnapshotARN`.

For Linux, macOS, or Unix:

```
aws rds restore-db-cluster-from-snapshot \
    --db-cluster-identifier `mydbcluster` \
    --snapshot-identifier `mydbsnapshotARN` \
    --engine aurora-mysql
```

For Windows:

```
aws rds restore-db-cluster-from-snapshot ^
    --db-cluster-identifier `mydbcluster` ^
    --snapshot-identifier `mydbsnapshotARN` ^
    --engine aurora-mysql
```

In this example, you create a MySQL 5.7–compatible DB cluster named
`mydbcluster` from a DB snapshot with an ARN set to
`mydbsnapshotARN`.

For Linux, macOS, or Unix:

```
aws rds restore-db-cluster-from-snapshot \
    --db-cluster-identifier `mydbcluster` \
    --snapshot-identifier `mydbsnapshotARN` \
    --engine aurora-mysql
```

For Windows:

```
aws rds restore-db-cluster-from-snapshot ^
    --db-cluster-identifier `mydbcluster` ^
    --snapshot-identifier `mydbsnapshotARN` ^
    --engine aurora-mysql
```
