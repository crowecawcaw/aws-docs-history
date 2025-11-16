# Auto migrating EC2 databases to Amazon RDS using AWS Database Migration Service

You can use the RDS console to migrate an EC2 database to
RDS.
RDS uses
AWS Database Migration Service (AWS DMS) to migrate your source EC2 database.
AWS DMS allows you to migrate relational databases into your AWS Cloud.
For more information about AWS Database Migration Service, see
[What is AWS Database Migration Service?](../../../dms/latest/userguide/Welcome.md "../../../dms/latest/userguide/Welcome.md")
in the _AWS Database Migration Service User Guide_.

To begin the migration, you must create an equivalent
RDS
DB instance to migrate the data into.
After you create your target database, you can import your EC2 database into it.
For source databases smaller than 1TiB, this migration action reduces
the time and resources required to migrate your data into
RDS.

## Overview

The RDS console allows you to migrate EC2 databases
into equivalent RDS databases. You must create an
RDS database to enable migration from the console.

You can migrate EC2 databases for the following databases engines:

- MySQL
- MariaDB
- PostgreSQL

The migration process involves the following steps:

- Create an equivalent database in RDS.
  For the databases to be equivalent, they must have the same database engine and compatible engine versions. They must also
  be in the same VPC. For instructions on creating your database, see

[Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

- Choose the type of replication for your database:
  - **Full load migration** – RDS copies the complete source database
    to the target database, creating new tables in the target when necessary.

  ###### Note

  This option causes an outage in your RDS database.
  - **Full load and change data capture (CDC) migration** – Similar to full load migration,
    with this option, RDS
    copies over the complete source database to the target database. However, after the full load migration,
    RDS applies any captured changes in the source
    to the target database. Change data capture collects changes to the database logs by using the database engine's native API.

  ###### Note

  This option causes an outage in your RDS database.
  - **Change data capture (CDC)** – Use this option to keep your target database available through the migration.
    RDS migrates ongoing changes in your source database to the target database.

- RDS creates the
  necessary networking resources to facilitate the migration.
  Once RDS
  creates the required resources, it notifies you about the resources
  created and allows you to initiate the data transfer.

The time required to complete the migration depends on the
type of replication and the size of the source database.

## Prerequisites

### MySQL and MariaDB

Before you begin to work with a MySQL or MariaDB
database as the source database, make sure
that you have the following prerequisites. These prerequisites apply to AWS-managed sources.

You must have an account for AWS DMS that has the Replication Admin role. The role
needs the following privileges:

- **REPLICATION CLIENT** – This privilege
  is required for CDC tasks only. In other words, full-load-only tasks
  don't require this privilege.
- **REPLICATION SLAVE** – This privilege is
  required for CDC tasks only. In other words, full-load-only tasks don't
  require this privilege.

The AWS DMS user must also have SELECT privileges for the source tables designated
for replication.

Grant the following privileges if you use MySQL-specific premigration assessments.

```
grant select on mysql.user to <dms_user>;
grant select on mysql.db to <dms_user>;
grant select on mysql.tables_priv to <dms_user>;
grant select on mysql.role_edges to <dms_user>  #only for MySQL version 8.0.11 and higher
```

### PostgreSQL

Before migrating data from an AWS-managed PostgreSQL source database, do the
following:

- We recommend that you use an AWS user account with the minimum required permissions
  for the PostgreSQL DB instance as
  the user account for the PostgreSQL source endpoint for AWS DMS. Using the master
  account is not recommended.
  The account must have the `rds_superuser` role and the
  `rds_replication` role. The `rds_replication`
  role grants permissions to manage logical slots and to stream data using
  logical slots.

###### Note

Some AWS DMS transactions are idle for some time before the DMS engine uses
them again. By using the parameter
`idle_in_transaction_session_timeout` in PostgreSQL versions
9.6 and higher, you can cause idle transactions to time out and fail.

## Limitations

The following limitations apply to the auto-migrate process:

- Your target database status must be **Available** to begin source database migration.
- When migrating from a MySQL source database, your
  RDS account must have the Replication Admin role.
  You must also have the proper privileges applied for that role.
- Your EC2 instance and target database must be in the same VPC.
- You can't migrate your EC2 database to the following target databases when using the
  **Migrate data from EC2 database** action:
  - Database that is a member of a cluster
  - Oracle, SQL Server, and Db2 databases
  - Databases with MySQL version lower than 5.7
  - Databases with PostgreSQL version lower than 10.4
  - Databases with MariaDB version lower than 10.2
