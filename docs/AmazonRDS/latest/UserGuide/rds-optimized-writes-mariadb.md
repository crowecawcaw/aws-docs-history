# Improving write performance with Amazon RDS Optimized Writes for MariaDB

You can improve the performance of write transactions with RDS Optimized Writes for
MariaDB. When your RDS for MariaDB database uses RDS Optimized Writes, it can achieve up to two
times higher write transaction throughput.

###### Topics

- [Overview of RDS Optimized Writes](#rds-optimized-writes-overview "#rds-optimized-writes-overview")
- [Using RDS Optimized Writes](#rds-optimized-writes-using-mariadb "#rds-optimized-writes-using-mariadb")
- [Enabling RDS Optimized Writes on an existing database](#rds-optimized-writes-modify-enable-mariadb "#rds-optimized-writes-modify-enable-mariadb")
- [Limitations for RDS Optimized Writes](#rds-optimized-writes-limitations-mariadb "#rds-optimized-writes-limitations-mariadb")

## Overview of RDS Optimized Writes

When you turn on RDS Optimized Writes, your RDS for MariaDB databases write only once
when flushing data to durable storage without the need for the doublewrite buffer. The
databases continue to provide ACID property protections for reliable database
transactions, along with improved performance.

Relational databases, like MariaDB, provide the _ACID properties_
of atomicity, consistency, isolation, and durability for reliable database transactions.
To help provide these properties, MariaDB uses a data storage area called the
_doublewrite buffer_ that prevents partial page write errors.
These errors occur when there is a hardware failure while the database is updating a
page, such as in the case of a power outage. A MariaDB database can detect partial page
writes and recover with a copy of the page in the doublewrite buffer. While this
technique provides protection, it also results in extra write operations. For more
information about the MariaDB doublewrite buffer, see [InnoDB
Doublewrite Buffer](https://mariadb.com/kb/en/innodb-doublewrite-buffer/ "https://mariadb.com/kb/en/innodb-doublewrite-buffer/") in the MariaDB documentation.

With RDS Optimized Writes turned on, RDS for MariaDB databases write only once when
flushing data to durable storage without using the doublewrite buffer. RDS Optimized
Writes is useful if you run write-heavy workloads on your RDS for MariaDB databases. Examples
of databases with write-heavy workloads include ones that support digital payments,
financial trading, and gaming applications.

These databases run on DB instance classes that use the AWS Nitro System. Because of the hardware configuration in these systems, the database can write 16-KiB pages directly to data files reliably and durably in one step. The AWS Nitro System makes RDS Optimized Writes possible.

You can set the new database parameter `rds.optimized_writes` to control
the RDS Optimized Writes feature for RDS for MariaDB databases. Access this parameter in the
DB parameter groups of RDS for MariaDB for the following versions:

- All available minor versions of 11.8 and higher major releases
- 11.4.3 and higher 11.4 versions
- 10.11.4 and higher 10.11 versions
- 10.6.10 and higher 10.6 versions

Set the parameter using the following values:

- `AUTO` – Turn on RDS Optimized Writes if the database supports it. Turn off RDS
  Optimized Writes if the database doesn't support it. This setting is the default.
- `OFF` – Turn off RDS Optimized Writes even if the database supports it.

If you migrate an RDS for MariaDB database that is configured to use RDS Optimized Writes
to a DB instance class that doesn't support the feature, RDS automatically turns off RDS
Optimized Writes for the database.

When RDS Optimized Writes is turned off, the database uses the MariaDB doublewrite
buffer.

To determine whether an RDS for MariaDB database is using RDS Optimized Writes, view the
current value of the `innodb_doublewrite` parameter for the database. If the
database is using RDS Optimized Writes, this parameter is set to `FALSE`
(`0`).

## Using RDS Optimized Writes

You can turn on RDS Optimized Writes when you create an RDS for MariaDB database with the
RDS console, the AWS CLI, or the RDS API. RDS Optimized Writes is turned on automatically
when both of the following conditions apply during database creation:

- You specify a DB engine version and DB instance class that support RDS
  Optimized Writes.
  - RDS Optimized Writes is supported for the following RDS for MariaDB
    versions:

        - All available minor versions of 11.8 and higher major releases
        - 11.4.3 and higher 11.4 versions
        - 10.11.4 and higher 10.11 versions
        - 10.6.10 and higher 10.6 versions

    For information about RDS for MariaDB versions, see [MariaDB on Amazon RDS versions](MariaDB.Concepts.md "MariaDB.Concepts.md").

  - RDS Optimized Writes is supported for RDS for MariaDB databases that use
    the following DB instance classes:

        - db.m7i
        - db.m7g
        - db.m6g
        - db.m6gd
        - db.m6i
        - db.m5
        - db.m5d
        - db.r7i
        - db.r7g
        - db.r6g
        - db.r6gd
        - db.r6i
        - db.r5
        - db.r5b
        - db.r5d
        - db.x2idn
        - db.x2iedn

    For information about DB instance classes, see [DB instance classes](Concepts.md "Concepts.md").

  DB instance class availability differs for AWS Regions. To determine whether a
  DB instance class is supported in a specific AWS Region, see [Determining DB instance class support in AWS Regions](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").

- In the parameter group associated with the database, the `rds.optimized_writes`
  parameter is set to `AUTO`. In default parameter groups, this parameter is always set to
  `AUTO`.

If you want to use a DB engine version and DB instance class that support RDS
Optimized Writes, but you don't want to use this feature, then specify a custom
parameter group when you create the database. In this parameter group, set the `rds.optimized_writes` parameter to `OFF`. If you want the database to use RDS Optimized Writes later, you can set the parameter to
`AUTO` to turn it on. For information about creating custom parameter
groups and setting parameters, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

For information about creating a DB instance, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

When you use the RDS console to create an RDS for MariaDB database, you can filter
for the DB engine versions and DB instance classes that support RDS Optimized
Writes. After you turn on the filters, you can choose from the available DB
engine versions and DB instance classes.

To choose a DB engine version that supports RDS Optimized Writes, filter for
the RDS for MariaDB DB engine versions that support it in **Engine
version**, and then choose a version.

![The Engine options section with the Amazon RDS Optimized Writes filter turned on for Engine Version.](images/rds-optimized-writes-version-filter-mariadb.png)
In the **Instance configuration** section, filter for the DB instance classes that support
RDS Optimized Writes, and then choose a DB instance class.

![The Instance configuration section with the Amazon RDS Optimized Writes filter turned on for DB instance class.](images/rds-optimized-writes-class-filter.png)
After you make these selections, you can choose other settings that meet your
requirements and finish creating the RDS for MariaDB database with the
console.

To create a DB instance by using the AWS CLI, run the [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md")
command. Make sure the `--engine-version` and
`--db-instance-class` values support RDS Optimized Writes. In
addition, make sure the parameter group associated with the DB instance has the
`rds.optimized_writes` parameter set to `AUTO`. This
example associates the default parameter group with the DB instance.

###### Example Creating a DB instance that uses RDS Optimized Writes

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --db-instance-identifier `mydbinstance` \
    --engine mariadb \
    --engine-version `10.6.10` \
    --db-instance-class `db.r5b.large` \
    --manage-master-user-password \
    --master-username `admin` \
    --allocated-storage `200`
```

For Windows:

```
aws rds create-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --engine mariadb ^
    --engine-version `10.6.10` ^
    --db-instance-class `db.r5b.large` ^
    --manage-master-user-password ^
    --master-username `admin` ^
    --allocated-storage `200`
```

You can create a DB instance using the [CreateDBInstance](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md")
operation. When you use this operation, make sure the `EngineVersion`
and `DBInstanceClass` values support RDS Optimized Writes. In
addition, make sure the parameter group associated with the DB instance has the
`rds.optimized_writes` parameter set to `AUTO`.

## Enabling RDS Optimized Writes on an existing database

In order to modify an existing RDS for MariaDB database to turn on RDS Optimized Writes, the database must
have been created with a supported DB engine version and DB instance class. In addition,
the database must have been created _after_ RDS Optimized Writes was
released on March 7, 2023, as the required underlying file system configuration is
incompatible with that of databases created before it was released. If these conditions
are met, you can turn on RDS Optimized Writes by setting the `rds.optimized_writes` parameter
to `AUTO`.

If your database was _not_ created with a supported engine version,
instance class, or file system configuration, you can use RDS Blue/Green Deployments to
migrate to a supported configuration. While creating the blue/green deployment, do the
following:

- Select **Enable Optimized Writes on green database**, then
  specify an engine version and DB instance class that supports RDS Optimized Writes. For a list
  of supported engine versions and instance classes, see [Using RDS Optimized Writes](#rds-optimized-writes-using-mariadb "#rds-optimized-writes-using-mariadb").
- Under **Storage**, choose **Upgrade storage file
  system configuration**. This option upgrades the database to a
  compatible underlying file system configuration.

When you create the blue/green deployment, if the `rds.optimized_writes`
parameter is set to `AUTO`, RDS Optimized Writes will be automatically
enabled on the green environment. You can then switch over the blue/green deployment,
which promotes the green environment to be the new production environment.

For more information, see [Creating a blue/green deployment in Amazon RDS](blue-green-deployments-creating.md "blue-green-deployments-creating.md").

## Limitations for RDS Optimized Writes

When you're restoring an RDS for MariaDB database from a snapshot, you can only
turn on RDS Optimized Writes for the database if all of the following conditions apply:

- The snapshot was created from a database that supports RDS Optimized
  Writes.
- The snapshot was created from a database that was created _after_ RDS Optimized Writes was released.
- The snapshot is restored to a database that supports RDS Optimized
  Writes.
- The restored database is associated with a parameter group that has
  the `rds.optimized_writes` parameter set to
  `AUTO`.
