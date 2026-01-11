# Auto migrating EC2 databases to Amazon Aurora using AWS Database Migration Service

You can use the Aurora console to migrate an EC2 database to
Aurora.
Aurora uses
AWS Database Migration Service (AWS DMS) to migrate your source EC2 database.
AWS DMS allows you to migrate relational databases into your AWS Cloud.
For more information about AWS Database Migration Service, see
[What is AWS Database Migration Service?](../../../dms/latest/userguide/Welcome.md "../../../dms/latest/userguide/Welcome.md")
in the _AWS Database Migration Service User Guide_.

To begin the migration, you must create an equivalent Aurora
DB cluster
to migrate the data into.
After you create your target database, you can import your EC2 database into it.
For source databases smaller than 1TiB, this migration action reduces
the time and resources required to migrate your data into Aurora
.

## Overview

The Aurora console allows you to migrate EC2 databases
into equivalent Aurora databases. You must create an
Aurora database to enable migration from the console.

You can migrate EC2 databases for the following databases engines:

- MySQL
- PostgreSQL

The migration process involves the following steps:

- Create an equivalent database in Aurora.
  For the databases to be equivalent, they must have the same database engine and compatible engine versions. They must also
  be in the same VPC. For instructions on creating your database, see
  [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md")
  .
- Choose the type of replication for your database:
  - **Full load migration** – Aurora copies the complete source database
    to the target database, creating new tables in the target when necessary.

  ###### Note

  This option causes an outage in your Aurora database.
  - **Full load and change data capture (CDC) migration** – Similar to full load migration,
    with this option, Aurora
    copies over the complete source database to the target database. However, after the full load migration,
    Aurora applies any captured changes in the source
    to the target database. Change data capture collects changes to the database logs by using the database engine's native API.

  ###### Note

  This option causes an outage in your Aurora database.
  - **Change data capture (CDC)** – Use this option to keep your target database available through the migration.
    Aurora migrates ongoing changes in your source database to the target database.

- Aurora creates the
  necessary networking resources to facilitate the migration.
  Once Aurora
  creates the required resources, it notifies you about the resources
  created and allows you to initiate the data transfer.

The time required to complete the migration depends on the
type of replication and the size of the source database.

## Prerequisites

### MySQL

Before you begin to work with a MySQL
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
- When migrating from a MySQL source database, your Aurora
  account must have the Replication Admin role.
  You must also have the proper privileges applied for that role.
- Your EC2 instance and target database must be in the same VPC.
- You can't migrate your EC2 database to the following target databases when using the
  **Migrate data from EC2 database** action:
  - Aurora global database
  - Aurora Limitless database
  - Aurora Serverless v1
  - Databases with MySQL version lower than 5.7
  - Databases with PostgreSQL version lower than 10.4
