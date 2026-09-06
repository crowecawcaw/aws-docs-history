

# Configuring IAM authentication for logical replication connections
<a name="AuroraPostgreSQL.Replication.Logical.IAM-auth"></a>

Starting with Aurora PostgreSQL versions 11 and higher, you can use AWS Identity and Access Management (IAM) authentication for replication connections. This feature enhances security by allowing you to manage database access using IAM roles instead of passwords. It works at the cluster level and follows the same security model as standard IAM authentication.

IAM authentication for replication connections is an opt-in feature. To enable it, set the `rds.iam_auth_for_replication` parameter to `1` in your DB cluster parameter group. As this is a dynamic parameter, your DB cluster doesn't need to restart, enabling you to leverage IAM authentication with existing workloads without downtime. Before enabling this feature, you must meet the [Prerequisites](#AuroraPostgreSQL.Replication.Logical.IAM-auth-prerequisites) listed below.

## Prerequisites
<a name="AuroraPostgreSQL.Replication.Logical.IAM-auth-prerequisites"></a>

To use IAM authentication for replication connections, you need to meet all of the following requirements:
+ Your Aurora PostgreSQL DB cluster must be version 11 or later.
+ On your publisher Aurora PostgreSQL DB cluster: 
  + Enable IAM database authentication.

    For more information, see [Enabling and disabling IAM database authentication](UsingWithRDS.IAMDBAuth.Enabling.md).
  + Enable logical replication by setting the `rds.logical_replication` parameter to `1`.

    For more information, see [Setting up logical replication for your Aurora PostgreSQL DB cluster](AuroraPostgreSQL.Replication.Logical.Configure.md).

  In logical replication, the publisher is the source Aurora PostgreSQL DB cluster that sends data to subscriber clusters. For more information, see [Overview of PostgreSQL logical replication with Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Replication.Logical.html).

**Note**  
Both IAM authentication and logical replication must be enabled on your publisher Aurora PostgreSQL DB cluster. If either one isn't enabled, you can't use IAM authentication for replication connections.

## Enabling IAM authentication for replication connections
<a name="AuroraPostgreSQL.Replication.Logical.IAM-auth-enabling"></a>

Complete the following steps to enable IAM authentication for replication connection.

1. Verify that your Aurora PostgreSQL DB cluster meets all prerequisites for IAM authentication with replication connections. For details, see [Prerequisites](#AuroraPostgreSQL.Replication.Logical.IAM-auth-prerequisites).

1. Configure the `rds.iam_auth_for_replication` parameter by modifying your DB cluster parameter group:
   + Set the `rds.iam_auth_for_replication` parameter to `1`. This dynamic parameter doesn't require a reboot.

1. Connect to your database and grant the necessary roles to your replication user:

   The following SQL commands grant the necessary roles to enable IAM authentication for replication connections:

   ```
   -- Grant IAM authentication role
   GRANT rds_iam TO replication_user_name;
   -- Grant replication privileges
   ALTER USER replication_user_name WITH REPLICATION;
   ```

After you complete these steps, the specified user must use IAM authentication for replication connections.

**Important**  
When you enable the feature, users with both `rds_iam` and `rds_replication` roles must use IAM authentication for replication connections. This applies whether the roles are assigned directly to the user or inherited through other roles.

## Disabling IAM authentication for replication connections
<a name="AuroraPostgreSQL.Replication.Logical.IAM-auth-disabling"></a>

You can disable IAM authentication for replication connections by using any of the following methods:
+ Set the `rds.iam_auth_for_replication` parameter to `0` in your DB cluster parameter group
+ Alternatively, you can disable either of these features on your Aurora PostgreSQL DB cluster:
  + Disable logical replication by setting the `rds.logical_replication` parameter to `0`
  + Disable IAM authentication

When you disable the feature, replication connections can use database passwords for authentication if configured.

**Note**  
Replication connections for users without the `rds_iam` role can use password authentication even when the feature is enabled.

## Limitations and considerations
<a name="AuroraPostgreSQL.Replication.Logical.IAM-auth-limitations"></a>

The following limitations and considerations apply when using IAM authentication for replication connections.
+ IAM authentication for replication connections is only available for Aurora PostgreSQL versions 11 and higher.
+ The publisher must support IAM authentication for replication connections.
+ The IAM authentication token expires after 15 minutes by default. You might need to refresh long-running replication connections before the token expires.