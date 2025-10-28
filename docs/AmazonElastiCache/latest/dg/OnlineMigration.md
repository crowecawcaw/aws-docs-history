# Online migration for Valkey or Redis OSS

By using Online Migration, you can migrate your data from your self-hosted open-source Valkey or Redis OSS on Amazon EC2 to Amazon ElastiCache.

This refers to migration from a self-hosted instance to the ElastiCache service. For information on upgrading from Redis OSS to Valkey on ElastiCache see [Upgrading engine versions including cross engine
upgrades](VersionManagement.md "VersionManagement.md").

###### Note

Online migration is not supported to ElastiCache serverless caches or clusters running on the r6gd node type.

## Overview

To migrate your data from open-source Valkey or Redis OSS running on Amazon EC2 to Amazon ElastiCache requires an existing or
newly created Amazon ElastiCache deployment. The deployment must have a configuration that is
ready for migration. It also should be in line with the configuration that you want,
including attributes such as instance type, number of shards, and number of replicas.

Online migration is designed for data migration from self-hosted open-source Valkey or Redis OSS on Amazon EC2
to ElastiCache, and not for moving data between ElastiCache clusters.

###### Important

We strongly recommend you read the following sections in their entirety before
beginning the online migration process.

The migration begins when you call the `StartMigration` API operation or
AWS CLI command. When migrating Valkey or Redis OSS cluster-mode disabled clusters, the migration process makes the primary node of
the ElastiCache Valkey or Redis OSS cluster a replica of your source Valkey or Redis OSS primary. When migrating Valkey or Redis OSS cluster-mode enabled clusters,
the migration process makes the primary node of each ElastiCache shard a replica of your source
cluster's corresponding shard owning the same slots.

After the client-side changes are ready, call the `CompleteMigration` API
operation. This API operation promotes your ElastiCache deployment to your primary Valkey or Redis OSS deployment with primary and replica nodes (as applicable). Now you can redirect your
client application to start writing data to ElastiCache. Throughout the migration, you can
check the status of replication by running the [valkey-cli INFO](https://valkey.io/commands/info "https://valkey.io/commands/info") command on your Valkey nodes and on the ElastiCache primary nodes.

## Migration steps

The following topics outline the process for migrating your data:

- [Preparing your source and target for migration](Migration-Prepare.md "Migration-Prepare.md")
- [Testing the data migration](Migration-Test.md "Migration-Test.md")
- [Starting migration](Migration-Initiate.md "Migration-Initiate.md")
- [Verifying the data migration progress](Migration-Verify.md "Migration-Verify.md")
- [Completing the data migration](Migration-Complete.md "Migration-Complete.md")
