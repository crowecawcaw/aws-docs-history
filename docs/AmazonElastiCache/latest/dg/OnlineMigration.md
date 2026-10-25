

# Online migration to ElastiCache node-based clusters
<a name="OnlineMigration"></a>

With online migration, you can migrate your data from self-managed Valkey or Redis OSS on Amazon EC2 to a node-based Amazon ElastiCache cluster.

This refers to migration from a self-managed instance to the ElastiCache service. For information on upgrading from Redis OSS to Valkey on ElastiCache see [Upgrading engine versions including cross engine upgrades](VersionManagement.HowTo.md).

**Note**  
This page covers online migration to node-based clusters. To migrate to an ElastiCache Serverless cache, see [Online migration to ElastiCache Serverless](migration-to-serverless.md). Online migration to node-based clusters doesn't support clusters that run on the r6gd node type.

## Overview
<a name="Migration-Overview"></a>

Migrating your data from Valkey or Redis OSS running on Amazon EC2 to Amazon ElastiCache requires an existing or newly created Amazon ElastiCache deployment. The deployment must have a configuration that is ready for migration. It also should be in line with the configuration that you want, including attributes such as node type, number of shards, and number of replicas. 

Online migration is designed for data migration from self-managed Valkey or Redis OSS on Amazon EC2 to ElastiCache, and not for moving data between ElastiCache clusters.

**Important**  
We strongly recommend you read the following sections in their entirety before beginning the online migration process.

The migration begins when you call the `StartMigration` API operation or AWS CLI command. When migrating Valkey or Redis OSS cluster-mode disabled clusters, the migration process makes the primary node of the ElastiCache Valkey or Redis OSS cluster a replica of your source Valkey or Redis OSS primary. When migrating Valkey or Redis OSS cluster-mode enabled clusters, the migration process makes the primary node of each ElastiCache shard a replica of your source cluster's corresponding shard owning the same slots.

After the client-side changes are ready, call the `CompleteMigration` API operation. This API operation promotes your ElastiCache deployment to your primary Valkey or Redis OSS deployment with primary and replica nodes (as applicable). Now you can redirect your client application to start writing data to ElastiCache. Throughout the migration, you can check the status of replication by running the [valkey-cli INFO](https://valkey.io/commands/info) command on your source nodes and on the ElastiCache primary nodes. 

## Migration steps
<a name="Migration-Steps"></a>

The following topics outline the process for migrating your data:
+ [Preparing your source and target for migration](Migration-Prepare.md)
+ [Testing the data migration](Migration-Test.md)
+ [Starting migration](Migration-Initiate.md)
+ [Verifying the data migration progress](Migration-Verify.md)
+ [Completing the data migration](Migration-Complete.md)
+ [Performing online data migration using the Console](Migration-Console.md)