# Release notes

These release notes describe the Amazon DocumentDB features, improvements, and bug fixes
by release date. The release notes include updates for all Amazon DocumentDB engine versions as they occur.

You can determine the current Amazon DocumentDB engine patch version by running the following
command:

```
db.runCommand({getEngineVersion: 1})
```

If your cluster is not on the latest version of the engine, it is likely that you have
pending maintenance available that will upgrade your engine. For more information, see [Maintaining Amazon DocumentDB](db-instance-maintain.md "db-instance-maintain.md") in the Developer Guide.

You can filter new Amazon DocumentDB features on the [What's New with Database?](https://aws.amazon.com/about-aws/whats-new/database/ "https://aws.amazon.com/about-aws/whats-new/database/") page. For **Products**, choose **Amazon DocumentDB**. Then search using keywords such as `elastic clusters` or `vector search`.

###### Topics

- [February 11, 2026](#release-notes.02-11-2026 "#release-notes.02-11-2026")
- [January 08, 2026](#release-notes.01-08-2026 "#release-notes.01-08-2026")
- [November 11, 2025](#release-notes.11-13-2025 "#release-notes.11-13-2025")
- [October 22, 2025](#release-notes.10-22-2025 "#release-notes.10-22-2025")
- [October 16, 2025](#release-notes.10-16-2025 "#release-notes.10-16-2025")
- [October 13, 2025](#release-notes.10-13-2025 "#release-notes.10-13-2025")
- [October 7, 2025](#release-notes.10-7-2025 "#release-notes.10-7-2025")
- [September 26, 2025](#release-notes.9-26-2025 "#release-notes.9-26-2025")
- [September 15, 2025](#release-notes.09-15-2025 "#release-notes.09-15-2025")
- [July 29, 2025](#release-notes.07-29-2025 "#release-notes.07-29-2025")
- [July 28, 2025](#release-notes.7-28-2025 "#release-notes.7-28-2025")
- [June 18, 2025](#release-notes.06-18-2025 "#release-notes.06-18-2025")
- [May 8, 2025](#release-notes.05-08-2025 "#release-notes.05-08-2025")
- [April 2, 2025](#release-notes.04-02-2025 "#release-notes.04-02-2025")
- [March 24, 2025](#release-notes.03-24-2025 "#release-notes.03-24-2025")
- [February 6, 2025](#release-notes.02-06-2025 "#release-notes.02-06-2025")
- [January 28, 2025](#release-notes.01-28-2025 "#release-notes.01-28-2025")
- [January 15, 2025](#release-notes.01-15-20254 "#release-notes.01-15-20254")
- [December 18, 2024](#release-notes.12-18-2024 "#release-notes.12-18-2024")
- [November 12, 2024](#release-notes.11-12-2024 "#release-notes.11-12-2024")
- [November 6, 2024](#release-notes.11-06-2024 "#release-notes.11-06-2024")
- [November 1, 2024](#release-notes.11-01-2024 "#release-notes.11-01-2024")
- [October 22, 2024](#release-notes.10-22-2024 "#release-notes.10-22-2024")
- [September 18, 2024](#release-notes.09-18-2024 "#release-notes.09-18-2024")
- [September 17, 2024](#release-notes.09-17-2024 "#release-notes.09-17-2024")
- [August 22, 2024](#release-notes.08-22-2024 "#release-notes.08-22-2024")
- [August 20, 2024](#release-notes.08-20-2024 "#release-notes.08-20-2024")
- [August 8, 2024](#release-notes.08-08-2024 "#release-notes.08-08-2024")
- [July 23, 2024](#release-notes.07-23-2024 "#release-notes.07-23-2024")
- [July 22, 2024](#release-notes.07-22-2024 "#release-notes.07-22-2024")
- [July 9, 2024](#release-notes.07-09-2024 "#release-notes.07-09-2024")
- [July 8, 2024](#release-notes.07-08-2024 "#release-notes.07-08-2024")
- [June 25, 2024](#release-notes.06-25-2024 "#release-notes.06-25-2024")
- [May 29, 2024](#release-notes.05-29-2024 "#release-notes.05-29-2024")
- [April 3, 2024](#release-notes.04-3-2024 "#release-notes.04-3-2024")
- [February 22, 2024](#release-notes.02-22-2024 "#release-notes.02-22-2024")
- [January 30, 2024](#release-notes.01-30-2024 "#release-notes.01-30-2024")
- [January 10, 2024](#release-notes.1-10-2024 "#release-notes.1-10-2024")
- [December 20, 2023](#release-notes.12-20-2023 "#release-notes.12-20-2023")
- [December 13, 2023](#release-notes.12-13-2023 "#release-notes.12-13-2023")
- [November 29, 2023](#release-notes.11-29-2023 "#release-notes.11-29-2023")
- [November 21, 2023](#release-notes.11-21-2023 "#release-notes.11-21-2023")
- [November 17, 2023](#release-notes.11-17-2023 "#release-notes.11-17-2023")
- [November 6, 2023](#release-notes.11-06-2023 "#release-notes.11-06-2023")
- [September 25, 2023](#release-notes.09-25-2023 "#release-notes.09-25-2023")
- [September 20, 2023](#release-notes.09-20-2023 "#release-notes.09-20-2023")
- [September 15, 2023](#release-notes.09-15-2023 "#release-notes.09-15-2023")
- [September 11, 2023](#release-notes.09-11-2023 "#release-notes.09-11-2023")
- [August 3, 2023](#release-notes.08-03-2023 "#release-notes.08-03-2023")
- [July 13, 2023](#release-notes.07-13-2023 "#release-notes.07-13-2023")
- [June 7, 2023](#release-notes.06-07-2023 "#release-notes.06-07-2023")
- [May 10, 2023](#release-notes.05-10-2023 "#release-notes.05-10-2023")
- [April 4, 2023](#release-notes.04-04-2023 "#release-notes.04-04-2023")
- [March 22, 2023](#release-notes.03-22-2023 "#release-notes.03-22-2023")
- [March 1, 2023](#release-notes.3.1.2023 "#release-notes.3.1.2023")
- [February 27, 2023](#release-notes.2.27.2023 "#release-notes.2.27.2023")
- [February 2, 2023](#release-notes.2.2.2023 "#release-notes.2.2.2023")
- [November 30, 2022](#release-notes.11.30.2022 "#release-notes.11.30.2022")
- [August 9, 2022](#release-notes.08.09.2022 "#release-notes.08.09.2022")
- [July 25, 2022](#release-notes.07.25.2022 "#release-notes.07.25.2022")
- [June 27, 2022](#release-notes.06.27.2022 "#release-notes.06.27.2022")
- [April 29, 2022](#release-notes.04-29-2022 "#release-notes.04-29-2022")
- [April 7, 2022](#relase-notes.04.07.2022 "#relase-notes.04.07.2022")
- [March 16, 2022](#release-notes.03.16.2022 "#release-notes.03.16.2022")
- [February 8, 2022](#release-notes.02.08.2022 "#release-notes.02.08.2022")
- [January 24, 2022](#release-notes.01.24.2022 "#release-notes.01.24.2022")
- [January 21, 2022](#release-notes.01.21.2022 "#release-notes.01.21.2022")
- [October 25, 2021](#release-notes.10.25.2021 "#release-notes.10.25.2021")
- [June 24, 2021](#release-notes.06.24.2021 "#release-notes.06.24.2021")
- [May 4, 2021](#release-notes.05.04.2021 "#release-notes.05.04.2021")
- [January 15, 2021](#release-notes.01-15-2021 "#release-notes.01-15-2021")
- [November 9, 2020](#release-notes.11-09-2020 "#release-notes.11-09-2020")
- [October 30, 2020](#release-notes.10-30-2020 "#release-notes.10-30-2020")
- [September 22, 2020](#release-notes.09-22-2020 "#release-notes.09-22-2020")
- [July 10, 2020](#release-notes.07-10-2020 "#release-notes.07-10-2020")
- [June 30, 2020](#release-notes.06-30-2020 "#release-notes.06-30-2020")

## February 11, 2026

### New feature

Amazon DocumentDB is now available in the Asia Pacific (Melbourne) and Europe (Zurich) regions.
For more information, see
this blog post.

## January 08, 2026

### New feature

Amazon DocumentDB is now available in the Asia Pacific (Jakarta) region.
For more information, see
this [blog post](https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-documentdb-mongodb-compatibility-asia-pacific-jakarta-region "https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-documentdb-mongodb-compatibility-asia-pacific-jakarta-region").

## November 11, 2025

### New features

Amazon DocumentDB now offers full wire protocol compatibility with MongoDB 8.0. Amazon DocumentDB 8.0 improves query performance enabling you to build high-performance applications at a lower cost.

**Amazon DocumentDB 8.0 (Engine Patch Version 4.0.4448)**

- Added support for MongoDB 8.0 API drivers.
- Added support for Planner Version3 that extends performance improvements to aggregation stage operators, along with supporting aggregation pipeline optimizations and distinct commands.
- Added Support for dictionary-based compression through the Zstandard compression algorithm, improving compression ratio by 5x.
- Added new capabilities: Amazon DocumentDB 8.0 supports collation and views.
- Added support for new aggregation stages and operators: $replaceWith, $vectorSearch, $merge, $set, $unset, $bucket, and 3 new aggregation operators $pow, $rand, $dateTrunc.
- Added support for a new version of text index: Text index v2 in Amazon DocumentDB 8.0 introduces additional tokens, enhancing text search capabilities.
- Includes vector search improvements through parallel vector index build reducing index build time by up to 30x.

## October 22, 2025

### New features

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.17983)**

Amazon DocumentDB now supports the latest generation of memory-optimized instances powered by Arm-based AWS Graviton4 processors, providing up to 30% better performance over R6G instances.
For more information, see [Managing instance classes](db-instance-classes.md "db-instance-classes.md") in this guide and this [blog post](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-documentdb-graviton4-based-r8g-database-instances/ "https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-documentdb-graviton4-based-r8g-database-instances/").

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.15902)**

- Added support for longer collection name (namespace length up to 255 chars).
- Introduced a new query planner (planner version 2.0).
  For more information, see [Query planner v2](query-planner.md "query-planner.md") in this guide.
- Added new fields in `collstats` for "MVCCIDStats" and "gcRuntimeStats" that provide information into the overall health of the collection with respect to garbage collection and aging collections.

**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.11747)**

Added new fields in `collstats` for "MVCCIDStats" and "gcRuntimeStats" that provide information into the overall health of the collection with respect to garbage collection and aging collections.

## October 16, 2025

### New feature

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.15902)** and **Amazon DocumentDB 4.0 (Engine Patch Version 2.0.11747)**

Amazon DocumentDB now supports dual-stack mode (IPv4/IPv6) when your cluster is in a virtual private cloud (VPC).

For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-documentdb-ipv6-support "https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-documentdb-ipv6-support") and [Amazon VPC and Amazon DocumentDB](vpc-docdb.md "vpc-docdb.md") in the _Amazon DocumentDB Developer Guide_.

## October 13, 2025

### New feature

Amazon DocumentDB now supports R6G and T4G instances in the Asia Pacific (Hyderabad) region.

For more information, see [Supported instance classes by region](db-instance-classes.md#db-instance-classes-by-region "db-instance-classes.md#db-instance-classes-by-region").

## October 7, 2025

### New feature

Amazon DocumentDB is now available in the following regions:

- Asia Pacific (Malaysia)
- Asia Pacific (Osaka)
- Asia Pacific (Thailand)
- Mexico (Central)

For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-documentdb-mongodb-compatibility-new-regions-asia-pacific-mexico/ "https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-documentdb-mongodb-compatibility-new-regions-asia-pacific-mexico/").

## September 26, 2025

### New features

Amazon DocumentDB now supports cross-region and cross-account snapshot copy and snapshot sharing.

For more information, see [Copying snapshots across AWS Regions](backup_restore-copy_cluster_snapshot.md#backup_restore-copy_snapshot_across_regions "backup_restore-copy_cluster_snapshot.md#backup_restore-copy_snapshot_across_regions") and [Sharing Amazon DocumentDB cluster snapshots](backup_restore-share_cluster_snapshots.md "backup_restore-share_cluster_snapshots.md").

## September 15, 2025

### Bug fixes and other changes

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.17983)**

Fixed engine crash when queries contain subsequent `$replaceRoot` and `$lookup` stage.

## July 29, 2025

### New features

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.15902)**

- Added support of `$regexFindAll` aggregation operator.
- Index bloat and collection based bloat metrics launched
- Added CloudWatch metrics `AvailableMVCCIds` and `LongestActiveGCRuntime` that provide information into the overall health of the cluster with respect to garbage collection and aging collections.
- The `serverStatus` command now includes an "nvme_cache" field that shows the count of pages written and not written to NVMe cache on NVMe-backed instances.
- Removed limitation on number of fields for `$group` and `$project`
- Support for the following String operators: `$trim`, `$rtrim`, `$ltrim`, `$regexFindAll`, `$replaceOne`, and `$replaceAll`
- Support for the following Array operators: `$first` and `$last`
- Support for the following Stage operator: `$collStats`

**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.11747)**

- Index bloat and collection based bloat metrics launched
- Added CloudWatch metrics `AvailableMVCCIds` and `LongestActiveGCRuntime` that provide information into the overall health of the cluster with respect to garbage collection and aging collections.
- Support for the following String operators: `$trim`, `$rtrim`, and `$ltrim`
- Support for the following Stage operator: `$collStats`

### Bug fixes and other changes

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.15902)**

Fixed an issue during index creation that affected large collections.

**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.11747)**

Fixed an issue during index creation that affected large collections.

## July 28, 2025

### New features

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.14228)**

Amazon DocumentDB instance-based clusters now support Amazon DocumentDB Serverless, an on-demand, auto-scaling configuration.

For more information, see [Using Amazon DocumentDB serverless](docdb-serverless.md "docdb-serverless.md") and this [what's new blog post](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-documentdb-serverless/ "https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-documentdb-serverless/").

## June 18, 2025

### New feature

Amazon DocumentDB is now available in the Israel (Tel Aviv) region.

## May 8, 2025

### New feature

Amazon DocumentDB is now available in the Europe (Stockholm) region.
For more information, see
this [blog post](https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-document-db-mongofb-compatibility-aws-europe-stockholm-region/ "https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-document-db-mongofb-compatibility-aws-europe-stockholm-region/").

## April 2, 2025

### Bug fixes and other changes

Fixed a bug in vector index creation with background indexes.

## March 24, 2025

### New feature

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.11800)**

Added support for `postBatchResumeToken` in change streams.

For more information, see [Resuming a change stream with postBatchResumeToken](change_streams.md#change_streams-postBatchResumeToken "change_streams.md#change_streams-postBatchResumeToken").

## February 6, 2025

### New feature

Amazon DocumentDB is now integrated with AWS Toolkit for Visual Studio Code.
For more information, see this [What's New blog post](https://aws.amazon.com/about-aws/whats-new/2025/02/aws-toolkit-visual-studio-code-documentdb-mongodb/ "https://aws.amazon.com/about-aws/whats-new/2025/02/aws-toolkit-visual-studio-code-documentdb-mongodb/"), and see [Working with Amazon DocumentDB in the Toolkit](../../../toolkit-for-vscode/latest/userguide/docdb.md "../../../toolkit-for-vscode/latest/userguide/docdb.md") in the _AWS Toolkit for Visual Studio Code User Guide_.

## January 28, 2025

### New feature

For one-click connectivity, Amazon DocumentDB is now integrated with AWS CloudShell for instance-based and elastic clusters.

For more information see any or all of the following:

- [Get started with Amazon DocumentDB](get-started-guide.md "get-started-guide.md")
- [Get started with Amazon DocumentDB elastic clusters](elastic-get-started.md "elastic-get-started.md")
- [What's new blog post](https://aws.amazon.com/about-aws/whats-new/2025/02//amazon-documentdb-one-click-connectivity-cloudshell/ "https://aws.amazon.com/about-aws/whats-new/2025/02//amazon-documentdb-one-click-connectivity-cloudshell/")
- [Technical how-to blog post](https://aws.amazon.com/blogs/database/amazon-documentdb-quick-start-zero-setup-with-aws-cloudshell/ "https://aws.amazon.com/blogs/database/amazon-documentdb-quick-start-zero-setup-with-aws-cloudshell/")

## January 15, 2025

### New features

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.11800)**

Amazon DocumentDB now maintains read availability through writer instance restarts.
Reader instances will now continue to serve read requests during writer instance restarts.

### Bug fixes and other changes

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.11800)**

- Fixed `killOp` command to handle a special case of bulk inserts.
- Improved network I/O-related memory usage on Amazon DocumentDB instances.
- Fixed `count` command for `$text` filter queries.

**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.11096)**

- Fixed `killOp` command to handle a special case of bulk inserts.
- Improved network I/O-related memory usage on Amazon DocumentDB instances.

## December 18, 2024

### New features

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.5721)**

Amazon DocumentDB instance-based clusters now support NVMe-backed R6GD instances.

For more information, see [NVMe-backed instances](db-instance-nvme.md "db-instance-nvme.md") and this [what's new blog post](https://aws.amazon.com/about-aws/whats-new/2024/12/nvme-backed-r6gd-instances-amazon-documentdb-mongodb-compatibility/ "https://aws.amazon.com/about-aws/whats-new/2024/12/nvme-backed-r6gd-instances-amazon-documentdb-mongodb-compatibility/").

## November 12, 2024

### New features

Amazon DocumentDB elastic clusters now support Background Indexes.

## November 6, 2024

### New features

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.11051)**

- Added support for minimum TLS versions `tls1.2+` and `tls1.3+` to `tls` cluster parameter.
- Enabled support for characters dollar($) and dot(.) in field names. For functional differences, see [Dollar($) and dot(.) in field names](functional-differences.md#functional-differences-dollardot "functional-differences.md#functional-differences-dollardot").

**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.10980)**

- Added support for minimum TLS versions `tls1.2+` and `tls1.3+` to `tls` cluster parameter.

## November 1, 2024

### New feature

Amazon DocumentDB now supports elastic cluster maintenance actions.
For more information, see [Maintaining Amazon DocumentDB elastic clusters](elastic-cluster-maintenance.md "elastic-cluster-maintenance.md").

## October 22, 2024

### New feature

Amazon DocumentDB now supports storage network throughput metrics `StorageNetworkReceiveThroughput`, `StorageNetworkTransmitThroughput`, and `StorageNetworkThroughput`.
For more information, see [Evaluating Amazon DocumentDB instance usage with CloudWatch metrics](best_practices.md#best-practice-evaluating-instance-usage "best_practices.md#best-practice-evaluating-instance-usage").

## September 18, 2024

### New feature

Amazon DocumentDB is now available in the Africa (Cape Town) region.
For more information, see
this [blog post](https://aws.amazon.com/about-aws/whats-new/2024/09/amazon-documentdb-mongodb-compatibility-cape-town-region/ "https://aws.amazon.com/about-aws/whats-new/2024/09/amazon-documentdb-mongodb-compatibility-cape-town-region/").

Amazon DocumentDB is now available in the Europe (Spain) region.
For more information, see
this [blog post](https://aws.amazon.com/about-aws/whats-new/2024/09/amazon-documentdb-mongodb-compatibility-spain-region/ "https://aws.amazon.com/about-aws/whats-new/2024/09/amazon-documentdb-mongodb-compatibility-spain-region/").

## September 17, 2024

### New features

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.10696)**

Amazon DocumentDB now supports rebuilding indexes with `reIndex` in the `runCommand`.
For more information, see [Index maintenance using reIndex](managing-indexes.md#reIndex "managing-indexes.md#reIndex").

###### Note

`reIndex` is only supported on Amazon DocumentDB 5.0 (Engine Patch Version 3.0.10696 and higher).

### Bug fixes and other changes

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.10696)** and **Amazon DocumentDB 4.0 (Engine Patch Version 2.0.10898)**

- `$setOnInsert` now supports the `_id` field during inserts resulting from update operations.
- Fixed issue that prevents reclaiming storage space after a major version upgrade to Amazon DocumentDB 5.0.

## August 22, 2024

### New feature

**Amazon DocumentDB 5.0 (All engine patch versions)** and **Amazon DocumentDB 4.0 (Engine Patch Version 2.0.5704)**

Amazon DocumentDB global clusters now support cluster switchovers and managed cluster failovers.
For more information, see [Performing a switchover for an Amazon DocumentDB global cluster](global-clusters-disaster-recovery.md#global-cluster-switchover "global-clusters-disaster-recovery.md#global-cluster-switchover") and [Performing a managed failover for an Amazon DocumentDB global cluster](global-clusters-disaster-recovery.md#managed-failover "global-clusters-disaster-recovery.md#managed-failover").

###### Note

Global cluster switchovers and failovers are supported on Amazon DocumentDB 4.0 and 5.0 only.

## August 20, 2024

### New feature

For Amazon DocumentDB 3.6 (minimum engine patch version 1.0.208662), TLS CA certificate updates no longer require a system reboot.
For more information, see [Updating your Amazon DocumentDB TLS
certificates](ca_cert_rotation.md "ca_cert_rotation.md").

## August 8, 2024

### New feature

Amazon DocumentDB elastic clusters are now available in the Asia Pacific (Hong Kong), Canada (Central), and Europe (Paris) regions.
For more information, see [Region availability for elastic clusters](docdb-using-elastic-clusters.md#elastic-region-availability "docdb-using-elastic-clusters.md#elastic-region-availability").

## July 23, 2024

### New features

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.8126)** and **Amazon DocumentDB 4.0 (Engine Patch Version 2.0.10709)**

- Added support for longer index names (up to 255 characters).
  For more information, see [Naming constraints](limits.md#limits-naming_constraints "limits.md#limits-naming_constraints")
- Increased the maximum connection limit by two-fold:

| Instance type | Original limit | New limit |
| ------------- | -------------- | --------- |
| t3.medium     | 500            | 1000      |
| t4g.medium    | 500            | 1000      |
| r5.large      | 1700           | 3400      |
| r5.xlarge     | 3500           | 7000      |
| r5.2xlarge    | 7100           | 14200     |
| r5.4xlarge    | 14200          | 28400     |
| r5.8xlarge    | 28400          | 60000     |
| r5.12xlarge   | 30000          | 60000     |
| r5.16xlarge   | 30000          | 60000     |
| r5.24xlarge   | 30000          | 60000     |
| r6g.large     | 1700           | 3400      |
| r6g.xlarge    | 3500           | 7000      |
| r6g.2xlarge   | 7100           | 14200     |
| r6g.4xlarge   | 14200          | 28400     |
| r6g.8xlarge   | 28400          | 60000     |
| r6g.12xlarge  | 30000          | 60000     |
| r6g.16xlarge  | 30000          | 60000     |

For more information, see [Instance limits](limits.md#limits.instance "limits.md#limits.instance").

### Bug fixes and other changes

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.8126)**

Enhanced the logic to synchronize `CurrentTime` and `ResumeToken` for the change stream on readers.

## July 22, 2024

### New features

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.6742)**

- Added support DML Audit filtering.
  You can now setup filter conditions to filter out DML Audit logs based on their specific requirements instead of logging every DML query.
  For more information, see [Filtering DML audit events](event-auditing.md#filtering-dml-events "event-auditing.md#filtering-dml-events").
- Added support in document compression for the following:

      + Setting a minimum compression threshold
      + Enabling compression for existing collections (applicable to new documents)
      + Allow default compression setting at the cluster level

  For more information, see [Managing collection-level document compression](doc-compression.md "doc-compression.md").

- Added support for consuming change streams on reader instances.
  For more information, see [Using change streams on secondary instances](change_streams.md#change-streams-secondary-instances "change_streams.md#change-streams-secondary-instances").

**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.10593)**

- Added support DML Audit filtering.
  You can now setup filter conditions to filter out DML Audit logs based on their specific requirements instead of logging every DML query.
  For more information, see [Filtering DML audit events](event-auditing.md#filtering-dml-events "event-auditing.md#filtering-dml-events").

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.208662)**

Removed index limitations on db.r5.\* and db.r6.\* instances in Amazon DocumentDB MVU.
For more information, see [MVU prerequisites and limitations](docdb-mvu.md#mvu-prerequisites "docdb-mvu.md#mvu-prerequisites").

### Bug fixes and other changes

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.208662)**

Amazon DocumentDB now recognizes -NaN as a valid JSON token.

## July 9, 2024

### New feature

For Amazon DocumentDB 4.0 (minimum engine patch version 2.0.10179) and 5.0 (minimum engine patch version 3.0.4780), TLS CA certificate updates no longer require a system reboot.
For more information, see [Updating your Amazon DocumentDB TLS
certificates](ca_cert_rotation.md "ca_cert_rotation.md").

## July 8, 2024

### New feature

Amazon DocumentDB elastic clusters are now available in the Europe (Milan) region.
For more information, see [Region availability for elastic clusters](docdb-using-elastic-clusters.md#elastic-region-availability "docdb-using-elastic-clusters.md#elastic-region-availability").

## June 25, 2024

### New feature

Authentication with AWS IAM ARNs is available in Amazon DocumentDB instance-based 5.0 clusters across all supported regions.
For more information, see [Authentication using IAM identity](iam-identity-auth.md "iam-identity-auth.md").

## May 29, 2024

### New features

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.6742)**

- Added support for `$regexMatch` and `$regexFind` operators.
- Added support to ensure full precision in audit logs when addressing large integers.
  Audit logs now maintain the exact numeric representation for all numbers, preventing any loss of precision.

**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.10593)**

- Added support to ensure full precision in audit logs when addressing large integers.
  Audit logs now maintain the exact numeric representation for all numbers, preventing any loss of precision.

## April 3, 2024

Amazon DocumentDB is now available in the Middle East (UAE) region.
For more information, see
this [blog post](https://aws.amazon.com/about-aws/whats-new/2024/04/amazon-documentdb-middle-east-uae-region/ "https://aws.amazon.com/about-aws/whats-new/2024/04/amazon-documentdb-middle-east-uae-region/").

### New features

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.5721)**

- Added support for `bypassDocumentValidation` and granular error message for `$jsonSchema`.
  For more information about `bypassDocumentValidation`, see [bypassDocumentValidation](json-schema-validation.md#json-schema-bypass "json-schema-validation.md#json-schema-bypass").
- Added support of `$expr`.
- Added support for Uncorrelated Joins in `$lookup`.
- Added support to retain validation rules in `$out` aggregation stage.

**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.10392)**

- Added support for `bypassDocumentValidation` for `$jsonSchema`.
  For more information about `bypassDocumentValidation`, see [bypassDocumentValidation](json-schema-validation.md#json-schema-bypass "json-schema-validation.md#json-schema-bypass").
- Added support of `$expr`.
- Added support for Uncorrelated Joins in `$lookup`.
- Added support to retain validation rules in `$out` aggregation stage.

### Bug fixes and other changes

- Fixed an error when invoking `db.coll.stats()` on mongo shell version 1.7 and later.
- Fixed a memory leak issue for change stream queries that contain `$regex` as a part of the same aggregation pipeline.

## February 22, 2024

### New features

**Amazon DocumentDB elastic clusters**

Amazon DocumentDB elastic clusters now support the following features:

- Readable secondary shard instance replicas - for more information, see step 5b of [Step 1: Create an elastic cluster](elastic-get-started.md#elastic-get-started-clusters "elastic-get-started.md#elastic-get-started-clusters").
- Start/stop cluster - for more information, see [Stopping and starting an
  Amazon DocumentDB elastic cluster](elastic-cluster-stop-start.md "elastic-cluster-stop-start.md").
- Configurable shard instances - for more information, see step 5b of [Step 1: Create an elastic cluster](elastic-get-started.md#elastic-get-started-clusters "elastic-get-started.md#elastic-get-started-clusters").
- Automatic backups for snapshots - for more information, see [Managing an elastic cluster snapshot automatic backup](elastic-manage-snapshots.md#elastic-auto-snapshot "elastic-manage-snapshots.md#elastic-auto-snapshot").
- Copy snapshot - for more information, see [Copying an elastic cluster snapshot](elastic-manage-snapshots.md#elastic-copy-snapshot "elastic-manage-snapshots.md#elastic-copy-snapshot").

## January 30, 2024

### New features

**Amazon DocumentDB elastic clusters**

Amazon DocumentDB elastic clusters are now available in the following regions:

- Asia Pacific (Mumbai)
- Asia Pacific (Seoul)
- South America (São Paulo)
- Europe (London)

For more information, see [Elastic cluster region and version availability](docdb-using-elastic-clusters.md#elastic-region-version "docdb-using-elastic-clusters.md#elastic-region-version").

**Amazon DocumentDB global clusters**

Global clusters are now available in both AWS GovCloud (US) regions: AWS GovCloud (US-East) and AWS GovCloud (US-West).

## January 10, 2024

### New features

**Amazon DocumentDB 5.0 (Engine Patch Versions 3.0.4574, 3.0.4780, 3.0.4960)**

- Added support for HNSW vector indexes. For more information, see [Vector search for Amazon DocumentDB](vector-search.md "vector-search.md").
- Added a support for partial indexes. For more information, see [Partial index](partial-index.md "partial-index.md").
- Added a support for GC runtime on a collection within `currentOp` command.
- Added text index support for native text search on Amazon DocumentDB. For more information, see [Performing text search with Amazon DocumentDB](text-search.md "text-search.md").
- Added support for `$jsonSchema` schema keywords `type`, `allOf`, `oneOf`, `anyOf`,
  `not`, `maxItems`, `minItems`, `maxProperties`, `minProperties`, `pattern`,
  `patternProperties`, `multipleOf`, `dependencies`, and `uniqueItems`.

For more information see [Using JSON schema validation](json-schema-validation.md "json-schema-validation.md").

- Added support for arithmetic operators `$ceil`, `$floor`, `$ln`, `$log`, `$log10`, `$sqrt`, and `$exp`.

For more information see [Arithmetic operators](mongo-apis.md#mongo-apis-aggregation-pipeline-arithmetic "mongo-apis.md#mongo-apis-aggregation-pipeline-arithmetic").

- Added support for the conditional expression operator `$switch`.
- Added support for parallel `IVFFLAT` vector index builds.
  Documentation was updated by removing the parallel `IVFFLAT` vector index builds limitation from the developer guide.

**Amazon DocumentDB 4.0 (Engine Patch Versions 2.0.10124, 2.0.10179, 2.0.10221)**

- Added a support for GC runtime on a collection within `currentOp` command.
- Added support for `$jsonSchema` schema keywords `type`, `allOf`, `oneOf`, `anyOf`,
  `not`, `maxItems`, `minItems`, `maxProperties`, `minProperties`, `pattern`,
  `patternProperties`, `multipleOf`, `dependencies`, and `uniqueItems`.

For more information see [Using JSON schema validation](json-schema-validation.md "json-schema-validation.md").

- Added support for arithmetic operators `$ceil`, `$floor`, `$ln`, `$log`, `$log10`, `$sqrt`, and `$exp`.

For more information see [Arithmetic operators](mongo-apis.md#mongo-apis-aggregation-pipeline-arithmetic "mongo-apis.md#mongo-apis-aggregation-pipeline-arithmetic").

- Added support for the conditional expression operator `$switch`.

### Bug fixes and other changes

- Added back case-insensitive functionality for invoking `db.runCommand("dbstats")`.
  Amazon DocumentDB 5.0 and 4.0 customers on engine patch versions prior to 3.0.4960 or 2.0.10221 should apply these latest engine patches.
- Fixed an error when invoking `db.coll.stats()` on mongo shell version 1.7 and later.
  Documentation was updated by removing the mongo shell `db.coll.stats()` troubleshooting tip from the developer guide.

## December 20, 2023

### Other changes

Enabled support for in-place major version upgrade in Amazon DocumentDB 3.6 and 4.0.
For more information, see [Amazon DocumentDB in-place major version upgrade](docdb-mvu.md "docdb-mvu.md").

## December 13, 2023

### New features

Added support for 1-click EC2 connectivity.
For more information, see [Connect using Amazon EC2](connect-ec2.md "connect-ec2.md").

## November 29, 2023

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.3727)**

### New features

Added support for vector search.
For more information, see this [blog post](https://aws.amazon.com/blogs/aws/vector-search-for-amazon-documentdb-with-mongodb-compatibility-is-now-generally-available/ "https://aws.amazon.com/blogs/aws/vector-search-for-amazon-documentdb-with-mongodb-compatibility-is-now-generally-available/") and visit [Vector search for Amazon DocumentDB](vector-search.md "vector-search.md") in the _Amazon DocumentDB Developer Guide_.

## November 21, 2023

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.3727)**

### New features

Added support for I/O-optimized storage.
For more information, see [Amazon DocumentDB cluster storage configurations](db-cluster-storage-configs.md "db-cluster-storage-configs.md") in the _Amazon DocumentDB Developer Guide_.

Added integration for no-code machine learning with SageMaker Canvas.
For more information, see [No-code machine learning with Amazon SageMaker AI Canvas](no-code-machine-learning.md "no-code-machine-learning.md") in the _Amazon DocumentDB Developer Guide_.

## November 17, 2023

### New features

Amazon DocumentDB is now available in the AWS GovCloud (US-East) region.
For more information, see
this [blog post](https://aws.amazon.com/about-aws/whats-new/2023/11/amazon-documentdb-mongodb-compatibility-aws-govcloud-us-east-region/ "https://aws.amazon.com/about-aws/whats-new/2023/11/amazon-documentdb-mongodb-compatibility-aws-govcloud-us-east-region/").

### Bug fixes and other changes

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.208570)**

User defined local variable names now support “\_” (underscore) for projection operators such as `$let` and `$filter`.

## November 6, 2023

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.3727) and 4.0 (Engine Patch Version 2.0.9876)**

### New features

- Added support for `$jsonSchema` schema keywords `maxLength`, `minLength`, `maximum`, `minimum`, `exclusiveMaximum`, `exclusiveMinimum`, `items`, and `additionalItems`.

Please note that JSON schema validation is supported in instance-based clusters only.

- Added support for `$convert` aggregation pipeline operator and its shorthand derived operators `$toBool`,
  `$toInt`, `$toLong`, `$toDouble`, `$toString`, `$toDecimal`, `$toObjectId`, and `$toDate`.
- Added support for set expression operators `$setDifference`, `$anyElementTrue`, and `$allElementTrue`.

### Bug fixes and other changes

Fixed issue where a change stream update from `-NaN` to `NaN` was not being displayed.

## September 25, 2023

### New features

Amazon DocumentDB is now available in the Asia Pacific (Hong Kong) region.
For more information, see
this [blog post](https://aws.amazon.com/about-aws/whats-new/2023/09/amazon-documentdb-mongodb-hong-kong/ "https://aws.amazon.com/about-aws/whats-new/2023/09/amazon-documentdb-mongodb-hong-kong/").

## September 20, 2023

### New features

Added support for in-place major version upgrades in Amazon DocumentDB 3.6 and 4.0.
For more information see [Amazon DocumentDB in-place major version upgrade](docdb-mvu.md "docdb-mvu.md").

## September 15, 2023

### New features

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.3140) and 4.0 (Engine Patch Version 2.0.9686)**

Added support for $jsonSchema schema validator in instance-based clusters only.
For more information see [Using JSON schema validation](json-schema-validation.md "json-schema-validation.md").

## September 11, 2023

### New features

Amazon DocumentDB is now available in the Asia Pacific (Hyderabad) region.
For more information, see
this [blog post](https://aws.amazon.com/about-aws/whats-new/2023/09/amazon-documentdb-asia-pacific-hyderabad-region/ "https://aws.amazon.com/about-aws/whats-new/2023/09/amazon-documentdb-asia-pacific-hyderabad-region/").

## August 3, 2023

### New features

**Amazon DocumentDB Elastic clusters**

- Amazon DocumentDB Elastic clusters now support the following operations:

      + `top`
      + `collStats`
      + `hint`
      + `dataSize`

  See [Supported MongoDB APIs, operations, and data types in Amazon DocumentDB](mongo-apis.md "mongo-apis.md") for the complete list of supported commands and operations.

- Time to Live (TTL) indexes are now supported.
- Index `hints` are now supported with index expressions.

## July 13, 2023

### New features

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.1948)**

- Added support for document compression.
- Added support for parallel index builds.
- Added support for index build status.

**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.9259)**

- Added support for parallel index builds.

### Bug fixes and other changes

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.1948)**

- Fixed authentication issue with `createCollection` for Amazon DocumentDB elastic clusters when users don’t have access to system collections.
- Fixed issue where secondary region instances couldn’t use the same primary region instance names.

**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.9259)**

- Stopped adding internal monitoring queries to auditing logs.

## June 7, 2023

### Bug fixes and other changes

**Amazon DocumentDB 5.0**

- r5 and t3.medium instances are now supported in Amazon DocumentDB 5.0.
- `engineVersion` option default is `5.0.0` in AWS SDK, AWS CLI, and CloudFormation.

## May 10, 2023

### Bug fixes and other changes

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.1361)**

- Added support for `ignoreunknownindexoptions` in the **createIndex** command.
- Stopped adding internal monitoring queries to auditing logs.
- User defined local variable names now support “\_” (underscore) for projection operators such as `$let` and `$filter`.

## April 4, 2023

### Bug fixes and other changes

**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.8934)**

- Fixed issue with DML auditing when it is enabled during an ongoing workload.
- Fixed issue with DML auditing when aggregate commands with hint is passed a string value.
- Fixed issue with `listCollections` command not working when users with readwriteanydatabase role having both authorizedCollections and nameOnly options set to true.
- Fixed issue to properly parse numeric string in a field name.
- Cancel long running cursors when they are impacting garbage collection.
- User defined local variable names now support “\_” (underscore) for projection operators such as `$let` and `$filter`.

## March 22, 2023

### New features

Amazon DocumentDB elastic clusters are now available in the Asia Pacific (Singapore), Asia Pacific (Sydney), and Asia Pacific (Tokyo) regions.
For more information, see
[Elastic cluster region and version availability](docdb-using-elastic-clusters.md#elastic-region-version "docdb-using-elastic-clusters.md#elastic-region-version").

## March 1, 2023

### New features

**Amazon DocumentDB 5.0 (Engine Patch Version 3.0.775)**

- Introduced Amazon DocumentDB 5.0
  - MongoDB 5.0 compatibility (support for MongoDB 5.0 API drivers)
  - Support for Client-side Field Level Encryption (FLE).
    You can now encrypt fields at the client-side before writing the data to Amazon DocumentDB cluster.
    For more information, see [Client-side field level encryption](field-level-encryption.md "field-level-encryption.md")
  - New aggregation operators: `$dateAdd`, `$dateSubtract`

- Increased storage limit to 128 TiB for all instance-based Amazon DocumentDB clusters and shard-based elastic clusters.
- Amazon DocumentDB 5.0 now supports index scan with the `$elemMatch` operator in the first nesting level.
  Index scans are supported when query only have one level of the `$elemMatch` filter and the nested `$elemMatch` query does not support index scan.

Query shape that supports index scan:

```
db.foo.find( { "a": {$elemMatch: { "b": "xyz", "c": "abc"} } })
```

Query shape that does not support index scan:

```
db.foo.find( { "a": {$elemMatch: { "b": {$elemMatch: { "d": "xyz", "e": "abc"} }} } })
```

## February 27, 2023

### Bug fixes and other changes

**Amazon DocumentDB 4.0**

Added support for AWS Lambda.
For more information, see [Using AWS Lambda with Change Streams](using-lambda.md "using-lambda.md").

## February 2, 2023

### Bug fixes and other changes

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.208432)**

- Fixed issue with DML auditing when it is enabled during an ongoing workload.
- Fixed issue with DML auditing when aggregate commands with hint is passed a string value.
- Fixed issue with `listCollections` command not working when users with readwriteanydatabase role having both authorizedCollections and nameOnly options set to true.
- Fixed issue to properly parse numeric string in a field name.
- Cancel long running cursors when they are impacting garbage collection.

## November 30, 2022

### New features

**Amazon DocumentDB Elastic clusters**

Amazon DocumentDB elastic clusters is a new type of Amazon DocumentDB cluster that enables users to leverage the MongoDB sharding APIs to scale out their cluster.
Elastic clusters handle virtually any number of reads and writes with petabytes of storage capacity by distributing the data and compute across multiple underlying compute instances and volumes.
To learn more, see [Using Amazon DocumentDB elastic clusters](docdb-using-elastic-clusters.md "docdb-using-elastic-clusters.md").

## August 9, 2022

### New features

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.208152) and 4.0**

- Added support for Decimal128 data type. The Decimal128 is a BSON data type
  supported in all regions where DocumentDB is available.

For more information, see [Data Types](mongo-apis.md#mongo-apis-data-types "mongo-apis.md#mongo-apis-data-types").

- Added support for DML query auditing with Amazon CloudWatch Logs. Now
  **Amazon DocumentDB** can record Data Manipulation Language (DML)
  events and Data Definition Language (DDL) events to Amazon CloudWatch
  Logs.

For more information, see this [blog post](https://aws.amazon.com/blogs/database/introducing-dml-auditing-for-amazon-documentdb-with-mongodb-compatibility/ "https://aws.amazon.com/blogs/database/introducing-dml-auditing-for-amazon-documentdb-with-mongodb-compatibility/").

### Bug fixes and other changes

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.208152) and 4.0**

- You can now change your own passwoprd with own password with
  `changeOwnPassword` privilege.

## July 25, 2022

### New features

**Amazon DocumentDB 4.0**

You can now create clusters faster with the ability to create clones that use the
same DocumentDB cluster volume and have the same data as the original cluster. For
details, see [Managing Amazon DocumentDB Clusters](db-clusters.md "db-clusters.md").

## June 27, 2022

### New features

**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.7509)**

Amazon DocumentDB dynamically resizes your database based on usage
patterns. Adding more data increases the space up to 64 Tebibytes (TiB) and deleting
data decreases allotted space.

## April 29, 2022

### New features

Amazon DocumentDB is now available in China (Beijing) region. For more information, see
this [blog post](https://www.amazonaws.cn/en/new/2022/amazon-documentdb-mongodb-beijing/ "https://www.amazonaws.cn/en/new/2022/amazon-documentdb-mongodb-beijing/").

## April 7, 2022

### New features

**Amazon DocumentDB 3.6 (Engine Patch Versions 1.0.207836 and 1.0.208015) and 4.0 (Engine Patch Versions 2.0.6142 and 2.0.6948)**

Amazon DocumentDB Performance Insights is now in preview.
You can now store seven days of performance history in a rolling window at no additional cost.
For more information, see [Monitoring with Performance Insights](performance-insights.md "performance-insights.md").

## March 16, 2022

### New features

Amazon DocumentDB is now available in Europe (Milan) region.
For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2022/03/amazon-documentdb-mongodb-milan/ "https://aws.amazon.com/about-aws/whats-new/2022/03/amazon-documentdb-mongodb-milan/").

## February 8, 2022

### New features

Amazon DocumentDB R6G and T4G instances are now available in Asia Pacific, South America, and Europe. For more information, see this [blog post](https://aws.amazon.com/about-aws/whats-new/2022/02/amazon-documentdb-mongodb-r6g-t4g-additional-regions/ "https://aws.amazon.com/about-aws/whats-new/2022/02/amazon-documentdb-mongodb-r6g-t4g-additional-regions/").

## January 24, 2022

### New features

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.207684) and 4.0 (Engine Patch Version 2.0.5170)**

- Amazon DocumentDB now offers a free trial. For details, see [Amazon DocumentDB free trial](https://aws.amazon.com/documentdb/free-trial/ "https://aws.amazon.com/documentdb/free-trial/") page.
- You can now use enhanced features with Geospatial query, including the following APIs:
  - `$geoWithin`
  - `$geoIntersects`

- Added support for the following MongoDB operators:

      + `$mergeObjects`
      + `$reduce`

  For more information, see the [Querying Geospatial data with Amazon DocumentDB](geospatial.md "geospatial.md").

## January 21, 2022

### New features

**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.5706)**

- Amazon DocumentDB Graviton2 (r6g.large, r6g.2xlarge, r6g.4xlarge,
  r6g.8xlarge, r6g.12xlarge, r6g.16xlarge and t4g.medium) instances are now supported.

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.207781) and 4.0 (Engine Patch Version 2.0.5706)**

- Added support for the following MongoDB APIs:
  - `$reduce`
  - `$mergeObjects`
  - `$geoWithin`
  - `$geoIntersects`

## October 25, 2021

### New features

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.207780) and 4.0 (Engine Patch Version
2.0.5704)**

- Added support for the following MongoDB APIs
  - `$literal`
  - `$map`
  - `$$ROOT`

- Support for GeoSpatial Query capabilities. See this [blog post](https://aws.amazon.com/blogs/database/introducing-geospatial-query-capabilities-for-amazon-documentdb-with-mongodb-compatibility/ "https://aws.amazon.com/blogs/database/introducing-geospatial-query-capabilities-for-amazon-documentdb-with-mongodb-compatibility/") for more details
- Support for access control with user-defined roles. See this [blog post](https://aws.amazon.com/blogs/database/introducing-amazon-documentdb-with-mongodb-compatibility-user-defined-roles-for-access-control/ "https://aws.amazon.com/blogs/database/introducing-amazon-documentdb-with-mongodb-compatibility-user-defined-roles-for-access-control/") for more details
- Amazon DocumentDB JDBC Driver to enable connectivity from BI tools such as Tableau and query
  tools such as SQL Workbench

### Bug fixes and other changes

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.207780) and 4.0 (Engine Patch Version
2.0.5704)**

- Bug fix for `$natural` to sort correctly when an explicit
  `.sort()` is present along with `$natural`
- Bug fix for change stream to work with `$redact`
- Bug fix for `$ifNull` to work with empty array
- Bug fix for excessive resource consumption/server crash when a currently
  logged-in user is deleted or that user’s privilege for an ongoing activity
  is revoked
- Bug fix in `listDatabase` and `listCollection`
  privilege check
- Bug Fix dedupe logic for multi-key elements

## June 24, 2021

### New features

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.207117) and 4.0 (Engine Patch Version
2.0.3371)**

- r5.8xlarge and r5.16xlarge instances are now supported. Learn more at the
  blog post [Amazon DocumentDB Now Supports r5.8xlarge and r5.16xlarge
  Instances](https://aws.amazon.com/about-aws/whats-new/2021/06/amazon-documentdb-with-mongodb-compatibility-now-supports-large-instances/ "https://aws.amazon.com/about-aws/whats-new/2021/06/amazon-documentdb-with-mongodb-compatibility-now-supports-large-instances/").
- [Global clusters](https://aws.amazon.com/about-aws/whats-new/2021/06/announcing-global-clusters-for-amazon-documentdb-with-mongodb-compatibility/ "https://aws.amazon.com/about-aws/whats-new/2021/06/announcing-global-clusters-for-amazon-documentdb-with-mongodb-compatibility/") are now supported to provide disaster recovery from
  region-wide outages and enable low-latency global reads by allowing reads from
  the nearest Amazon DocumentDB cluster. Note that global clusters are not currently
  supported in the South America (São Paulo), Europe (Milan), China (Beijing),
  and China (Ningxia) Regions.

## May 4, 2021

### New features

See all the new features in this [blog post](https://aws.amazon.com/about-aws/whats-new/2021/05/amazon-documentdb-improves-mongodb-compatibility-and-indexing-improvements/ "https://aws.amazon.com/about-aws/whats-new/2021/05/amazon-documentdb-improves-mongodb-compatibility-and-indexing-improvements/").

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.207117) and 4.0 (Engine Patch Version
2.0.3371)**

- `renameCollection`
- `$zip`
- `$indexOfArray`
- `$reverseArray`
- `$natural`
- `$hint` support for update
- Index scan for `distinct`

### Bug fixes and other changes

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.207117) and 4.0 (Engine Patch Version
2.0.3371)**

- Reduced memory usage for `$in` queries
- Fixed a memory leak in multikey indexes
- Fixed the explain plan and profiler output for `$out`
- Added a timeout for operations from internal monitoring system to improve reliability
- Fixed a defect impacting the query predicates passed to multikey indexes

## January 15, 2021

### New features

**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.722)**

- None

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.206295)**

- Ability to use an index with the `$lookup` aggregation stage
- `find()` queries with projections can be served direction from an index (covered query)
- Ability to use `hint()` with the `findAndModify`
- Performance optimizations for `$addToSet` operator
- Improvements to reduce overall index sizes
- New aggregation operators: `$ifNull`,
  `$replaceRoot`, `$setIsSubset`,
  `$setInstersection`, `$setUnion`, and
  `$setEquals`
- Users can also end their own cursors without requiring the `KillCursor` role

## November 9, 2020

### New features

See all the new features in this [blog post](https://aws.amazon.com/about-aws/whats-new/2020/11/amazon-documentdb-with-mongodb-compatibility-adds-support-for-mongodb-4-and-transactions/ "https://aws.amazon.com/about-aws/whats-new/2020/11/amazon-documentdb-with-mongodb-compatibility-adds-support-for-mongodb-4-and-transactions/").

**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.722)**

- MongoDB 4.0 compatibility
- ACID transactions
- Support for `cluster(client.watch()` or
  `mongo.watch())` and the database level `(db.watch())`
  change streams
- Ability to start or resume a change streams using
  `startAtOperationTime`
- Extend your change stream retention period to 7 days (previously 24
  hours)
- AWS DMS target for Amazon DocumentDB 4.0
- CloudWatch metrics: `TransactionsOpen`,
  `TransactionsOpenMax`, `TransactionsAborted`,
  `TransactionsStarted`, and
  `TransactionsCommitted`
- New fields for transactions in `currentOp`,
  `ServerStatus`, and `profiler`.
- Ability to use an index with the `$lookup` aggregation
  stage
- `find()` queries with projections can be served direction from
  an index (covered query)
- Ability to use `hint()` with the
  `findAndModify`
- Performance optimizations for `$addToSet` operator
- Improvements to reduce overall index sizes.
- New aggregation operators: `$ifNull`,
  `$replaceRoot`, `$setIsSubset`,
  `$setInstersection`, `$setUnion`, and
  `$setEquals`
- With the `ListCollection` and `ListDatabase`
  commands, you can now optionally use the `authorizedCollections` and
  `authorizedDatabases` parameters to allow users to list the
  collections and databases that they have permission to access without requiring
  the `listCollections` and `listDatabase` roles,
  respectively
- Users can also end their own cursors without requiring the
  `KillCursor` role
- Comparing numeric types of subdocuments is now consistent with comparing
  numeric types of first-level documents. The behavior in Amazon DocumentDB 4.0 is now
  compatible with MongoDB.

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.206295)**

- None

### Bug fixes and other changes

**Amazon DocumentDB 4.0 (Engine Patch Version 2.0.722)**

- `$setOnInsert` no longer allow updates when using the
  positional operator `$`. The behavior in Amazon DocumentDB 4.0 is now
  compatible with MongoDB.
- Fixed issue with `$createCollection` and set `autoIndexId`
- Projection for nested documents
- Changed default setting for working memory to scale with instance memory size
- Garbage collection improvements
- Lookup with empty key in path, behavior difference with mongo
- Fixed `dateToString` bug in timezone behavior
- Fixed `$push` (aggregation) to respect sort order
- Fixed bug in `$currentOp` with aggregate
- Fixed issue with `readPreference` on secondary
- Fixed issue with validating `$createIndex` is the same database as the command was issued
- Fixed inconsistent behavior for `minKey`, `maxKey`
  lookup fails
- Fixed issue with `$size` operator not working with composite
  array
- Fixed issue with the negation of `$in` with regex
- Fixed issue with `$distinct` command run against a
  view
- Fixed issue with aggregations and find commands sorting missing fields
  differently
- Fixed `$eq` to regular expression not checking type
- Fixed `$currentDate` bug in timestamp ordinal position
  behavior
- Fixed millisecond granularity for `$currentDate`

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.206295)**

- None

## October 30, 2020

### New features

See all the new features in this [blog post](https://aws.amazon.com/about-aws/whats-new/2020/10/amazon-documentdb-mongodb-compatibility-support-increased-change-stream-retention/ "https://aws.amazon.com/about-aws/whats-new/2020/10/amazon-documentdb-mongodb-compatibility-support-increased-change-stream-retention/").

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.206295)**

- Added the ability to open a change stream cursor at the cluster level
  `(client.watch()` or `mongo.watch())` and the database
  `(db.watch())`
- Ability to increase the change stream retention period to 7 days(previously 24 hours)

### Bug fixes and other changes

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.206295)**

- Various general case performance improvements
- A targeted security improvement
- Fixed an issue with skip sort on second field of a compound index
- Enable regular index for equality on single field of a multi-key index (not compound)
- Fixed authentication race condition
- Fixed issue that caused an infrequent garbage collection crash
- RBAC security improvement
- Added `databaseConnectionsMax` metric
- Performance improvements for certain workloads on `r5.24xlarge` instances

## September 22, 2020

### New features

See all the new features in this [blog post](https://aws.amazon.com/about-aws/whats-new/2020/09/amazon-documentdb-with-mongodb-compatibility-adds-aggregration-stage-increases-number-of-connections-and-cursors/ "https://aws.amazon.com/about-aws/whats-new/2020/09/amazon-documentdb-with-mongodb-compatibility-adds-aggregration-stage-increases-number-of-connections-and-cursors/").

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.206295)**

- `$out` aggregation stage
- Increased the maximum number of connections and cursor per instance by as much as 10x

### Bug fixes and other changes

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.206295)**

- None

## July 10, 2020

### New features

See all the new features in this [blog post](https://aws.amazon.com/about-aws/whats-new/2020/07/amazon-documentdb-support-cross-region-snapshot-copy/ "https://aws.amazon.com/about-aws/whats-new/2020/07/amazon-documentdb-support-cross-region-snapshot-copy/").

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.206295)**

- Cross Region Snapshot Copy

### Bug fixes and other changes

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.206295)**

- None

## June 30, 2020

### New features

See all the new features in this [blog post](https://aws.amazon.com/about-aws/whats-new/2020/07/amazon-documentdb-support-cross-region-snapshot-copy/ "https://aws.amazon.com/about-aws/whats-new/2020/07/amazon-documentdb-support-cross-region-snapshot-copy/").

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.206295)**

- T3 medium instances

### Bug fixes and other changes

**Amazon DocumentDB 3.6 (Engine Patch Version 1.0.206295)**

- Idle memory reclamation for t3 instances
- Authentication improvements
- Improved SASL authentication performance
- Fixed `currentOp` issue when exceeding maximum possible ops
- Fixed `killOps` issue for bulk update and delete
- Improvements to `$sample` performance with
  `$match`
- Fixed support for `$$` in cond case in redact stage
- Fixed various recurring crash root causes
- Improvements to TTL sweeping to reduce IOs and latency
- Optimized memory utilization for `$unwind`
- Fixed collection stats race condition with drop index
- Fixed race condition during concurrent index build
- Fixed infrequent crash in `hash_search` in index
