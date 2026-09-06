

# Using the Aurora PostgreSQL Limitless Database data loading utility
<a name="limitless-load.utility"></a>

Aurora provides a utility for loading data directly into Limitless Database from an Aurora PostgreSQL DB cluster or RDS for PostgreSQL DB instance.

You perform the following steps to use the data loading utility:

1. [Prerequisites](#limitless-load.prereqs)

1. [Preparing the source database](#limitless-load.source)

1. [Preparing the destination database](#limitless-load.destination)

1. [Creating database credentials](#limitless-load.users)

1. One of the following:
   + [Setting up database authentication and resource access using a script](limitless-load.script.md) (recommended)
   + [Setting up database authentication and resource access manually](limitless-load.manual.md)

1. [Loading data from an Aurora PostgreSQL DB cluster or RDS for PostgreSQL DB instance](limitless-load.data.md)

## Limitations
<a name="limitless-load.limitations"></a>

The data loading utility has the following limitations:
+ The following data types aren't supported: `enum`, `ARRAY`, `BOX`, `CIRCLE`, `LINE`, `LSEG`, `PATH`, `PG_LSN`, `PG_SNAPSHOT`, `POLYGON`, `TSQUERY`, `TSVECTOR`, and `TXID_SNAPSHOT`.
+ Leading zeroes (`0`) are stripped from the `VARBIT` data type during loading.
+ Data migration fails when there are foreign keys on the destination tables.
+ Limitless Data Utility supports the following source configurations for Amazon RDS for PostgreSQL Multi-AZ DB clusters:
  + Primary instance
    + Supported modes: snapshot, snapshot\_then\_cdc
  + Replica instance
    + Supported mode: snapshot only
      + Requirement: hot\_standby\_feedback must be enabled
    + Not supported: snapshot\_then\_cdc

## Prerequisites
<a name="limitless-load.prereqs"></a>

The data loading utility has the following prerequisites:
+ The source database uses Aurora PostgreSQL or RDS for PostgreSQL version 11.x and higher.
+ The source database is in the same AWS account and AWS Region as the destination DB shard group.
+ The source DB cluster or DB instance is in the `available` state.
+ Tables on the source database and limitless database have the same table names, column names, and column data types.
+ The source and destination tables have primary keys that use the same columns and column orders.
+ You must have an environment for connecting to a limitless database to run data loading commands. Available commands are the following:
  + `rds_aurora.limitless_data_load_start`
  + `rds_aurora.limitless_data_load_cancel`
+ For CDC:
  + Both the source database and the destination DB shard group must use the same DB subnet group, VPC security group, and database port. These setups are for network connections to both the source database and the routers in the DB shard group.
  + You must enable logical replication on the source database. The source database user must have privileges to read logical replication.

## Preparing the source database
<a name="limitless-load.source"></a>

To access the source database for data loading, you must allow incoming network traffic to it. Perform the following steps.

**To allow network traffic to the source database**

1. Sign in to the AWS Management Console and open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Navigate to the **Security groups** page.

1. Choose the **Security group ID** for the security group used by the source DB cluster or instance.

   For example, its security group ID is `sg-056a84f1712b77926`.

1. On the **Inbound rules** tab:

   1. Choose **Edit inbound rules**.

   1. Add a new inbound rule for the source DB cluster or instance:
      + Port range – Database port for the source database, usually `5432`
      + Security group ID – `sg-056a84f1712b77926` in this example  
![Add inbound rule for the source database.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/limitless_self_access_inbound_rule.png)

1. On the **Outbound rules** tab:

   1. Choose **Edit outbound rules**.

   1. Add a new outbound rule for the source DB cluster or instance:
      + Database port – `All traffic` (includes ports `0-65535`)
      + Security group ID – `sg-056a84f1712b77926` in this example  
![Add outbound rule for the source database.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/limitless_self_access_outbound_rule.png)

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. Navigate to the **Network ACLs** page.

1. Add the default network ACL configuration as outlined in [Default network ACL](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#default-network-acl).

## Preparing the destination database
<a name="limitless-load.destination"></a>

Follow the procedures in [Creating Aurora PostgreSQL Limitless Database tables](limitless-creating.md) to create the destination tables in the DB shard group.

Your destination tables must have the same schemas, table names, and primary keys as the source tables.

## Creating database credentials
<a name="limitless-load.users"></a>

You must create database users in the source and destination databases, and grant necessary privileges to the users. For more information, see [CREATE USER](https://www.postgresql.org/docs/current/sql-createuser.html) and [GRANT](https://www.postgresql.org/docs/current/sql-grant.html) in the PostgreSQL documentation.

### Create the source database credentials
<a name="limitless-load.users.source"></a>

The source database user is passed in the command to start loading. This user must have privileges to perform replication from the source database.

1. Use the database master user (or another user with the `rds_superuser` role) to create a source database user with `LOGIN` privileges.

   ```
   CREATE USER {{source_db_username}} WITH PASSWORD '{{source_db_user_password}}';
   ```

1. Grant the `rds_superuser` role to your source database user.

   ```
   GRANT rds_superuser to {{source_db_username}};
   ```

1. If you're using `full_load_and_cdc` mode, grant the `rds_replication` role to your source database user. The `rds_replication` role grants permissions to manage logical slots and to stream data using logical slots.

   ```
   GRANT rds_replication to {{source_db_username}};
   ```

### Create the destination database credentials
<a name="limitless-load.users.destination"></a>

The destination database user must have permission to write to the destination tables in the DB shard group.

1. Use the database master user (or another user with the `rds_superuser` role) to create a destination database user with `LOGIN` privileges.

   ```
   CREATE USER {{destination_db_username}} WITH PASSWORD '{{destination_db_user_password}}';
   ```

1. Grant the `rds_superuser` role to your destination database user.

   ```
   GRANT rds_superuser to {{destination_db_username}};
   ```