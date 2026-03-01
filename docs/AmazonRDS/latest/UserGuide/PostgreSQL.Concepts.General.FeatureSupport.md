# Configuring IAM authentication for logical replication connections

Starting with RDS for PostgreSQL versions 11 and higher, you can use AWS Identity and Access Management (IAM) authentication for replication connections. This feature enhances security by allowing you to manage database access using IAM roles instead of passwords. It works both at the cluster and instance granularity and follows the same security model as standard IAM authentication.

IAM authentication for replication connections is an opt-in feature. To enable it, set the `rds.iam_auth_for_replication` parameter to 1 in your DB cluster or DB parameter group. As this is a dynamic parameter, your DB cluster or instance doesn't need to restart, enabling you to leverage IAM authentication with existing workloads without downtime. Before enabling this feature, you must meet the Prerequisites listed below.

###### Topics

- [Prerequisites](#PostgreSQL.Concepts.General.FeatureSupport.IAMLogicalReplication.Prerequisites "#PostgreSQL.Concepts.General.FeatureSupport.IAMLogicalReplication.Prerequisites")
- [Enabling IAM authentication for replication connections](#PostgreSQL.Concepts.General.FeatureSupport.IAMLogicalReplication.Enabling "#PostgreSQL.Concepts.General.FeatureSupport.IAMLogicalReplication.Enabling")
- [Disabling IAM authentication for replication connections](#PostgreSQL.Concepts.General.FeatureSupport.IAMLogicalReplication.Disabling "#PostgreSQL.Concepts.General.FeatureSupport.IAMLogicalReplication.Disabling")
- [Limitations and considerations](#PostgreSQL.Concepts.General.FeatureSupport.IAMLogicalReplication.Limitations "#PostgreSQL.Concepts.General.FeatureSupport.IAMLogicalReplication.Limitations")

## Prerequisites

To use IAM authentication for replication connections, you need to meet all of the following requirements:

- Your RDS for PostgreSQL DB instance must be version 11 or later.
- On your publisher RDS for PostgreSQL DB instance:
  - Enable IAM database authentication. For more information, see [Enabling and disabling IAM database authentication](UsingWithRDS.IAMDBAuth.md "UsingWithRDS.IAMDBAuth.md").
  - Enable logical replication by setting the `rds.logical_replication` parameter to 1.

In logical replication, the publisher is the source RDS for PostgreSQL database that sends data to subscriber database. For more information, see [Performing logical replication for Amazon RDS for PostgreSQL](PostgreSQL.Concepts.General.FeatureSupport.md "PostgreSQL.Concepts.General.FeatureSupport.md").

###### Note

Both IAM authentication and logical replication must be enabled on your publisher RDS for PostgreSQL DB instance. If either one isn't enabled, you can't use IAM authentication for replication connections.

## Enabling IAM authentication for replication connections

Complete the following steps to enable IAM authentication for replication connection.

###### To enable IAM authentication for replication connections

1.  Verify that your RDS for PostgreSQL DB cluster or instance meets all prerequisites for IAM authentication with replication connections. For details, see [Prerequisites](#PostgreSQL.Concepts.General.FeatureSupport.IAMLogicalReplication.Prerequisites "#PostgreSQL.Concepts.General.FeatureSupport.IAMLogicalReplication.Prerequisites").
2.  Configure the `rds.iam_auth_for_replication` parameter based on your RDS for PostgreSQL setup:

        * For RDS for PostgreSQL DB instances: Modify your DB parameter group.
        * For Multi-AZ clusters: Modify your DB cluster parameter group.

    Set `rds.iam_auth_for_replication` to 1. This is a dynamic parameter that takes effect immediately without requiring a reboot.

###### Note

Multi-AZ clusters use only DB cluster parameter groups. Individual instance parameter groups cannot be modified in Multi-AZ clusters. 3. Connect to your database and grant the necessary roles to your replication user:

The following SQL commands grant the necessary roles to enable IAM authentication for replication connections:

```

-- Grant IAM authentication role
GRANT rds_iam TO replication_user_name;

-- Grant replication privileges
ALTER USER replication_user_name WITH REPLICATION;

```

After you complete these steps, the specified user must use IAM authentication for replication connections.

###### Important

When you enable the feature, users with both `rds_iam` and `rds_replication` roles must use IAM authentication for replication connections. This applies whether the roles are assigned directly to the user or inherited through other roles.

## Disabling IAM authentication for replication connections

You can disable IAM authentication for replication connections by using any of the following methods:

- Set the `rds.iam_auth_for_replication` parameter to 0 in your DB parameter group for DB instances or DB cluster parameter group for Multi-AZ clusters.
- Alternatively, you can disable either of these features on your RDS for PostgreSQL DB cluster or instance:
  - Disable logical replication by setting the `rds.logical_replication` parameter to 0
  - Disable IAM authentication

When you disable the feature, replication connections can use database passwords for authentication.

###### Note

Replication connections for users without the `rds_iam` role can use password authentication even when the feature is enabled.

## Limitations and considerations

Consider the following limitations and considerations when using IAM authentication for logical replication connections:

- This feature is available only for RDS for PostgreSQL versions 11 and higher.
- The publisher must support IAM authentication for replication connections.
- The IAM authentication token expires after 15 minutes by default. You might need to refresh long-running replication connections before the token expires.
