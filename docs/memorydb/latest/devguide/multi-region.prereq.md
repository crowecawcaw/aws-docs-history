# Prerequisites and limitations

Before getting started with MemoryDB Multi-Region, be aware of the following:

- **MemoryDB Multi-Region replicates data between Regions of your choice** - By creating a Multi-Region cluster, you understand and agree that data will be moved between your selected Regions.

Removing a Region from the Multi-Region group also deletes the regional cluster in that region.

- **Regional availability** - MemoryDB Multi-Region is supported in the following AWS Regions: US East (N. Virginia and Ohio), US West (Oregon, N. California), Europe (Ireland, Frankfurt, and London), and Asia Pacific (Tokyo, Sydney, Mumbai, Seoul and Singapore).
- **Behaviors and settings** - All Multi-Region regional clusters will have the same number of shards, instance types, Valkey engine version, TLS and parameter group settings. You can choose differing IAM authentication, ACLs, snapshot windows, tags, Customer Managed Keys (CMKs), and maintenance windows for each of your regional clusters.

With MemoryDB multi-Region, clusters in different Regions can have a different number of replicas.

- **Node types supported** - MemoryDB Multi-Region is supported on R7g nodes of size XL and above.

MemoryDB Multi-Region supports Valkey engine version 7.3 and above.

- **Data types supported** - MemoryDB Multi-Region currently supports most Redis OSS or Valkey data types, and we will add support for more data types in future. Supported data types include Strings, Hashes, Sets, and Sorted Sets, although not all commands that manipulates those data types are supported.
- **Total number of Regions** - With MemoryDB Multi-Region, you will be able to automatically replicate MemoryDB cluster data between up to five AWS Regions.
- **Supported options** - MemoryDB Multi-Region supports horizontal/vertical scaling, IAM integration, ACLs, automatic and on-demand snapshotting, automatic software patching, and monitoring.
- **Backup and restore** - You can create snapshots to back up the data of your Multi-Region regional clusters. You can manually create a snapshot, or you can use MemoryDB’s automated snapshot scheduler to take a new snapshot each day at a time you specify individually for each regional cluster.
- **Migration** - You can choose to restore any MemoryDB or Redis OSS/Valkey RDB format backups. To migrate the data from a backup, create a new MemoryDB Multi-Region regional cluster and specify the snapshot location from Amazon S3. If it is a MemoryDB snapshot you can also specify the name. MemoryDB Multi-Region will create the regional cluster with the data from the snapshot. As MemoryDB Multi-Region supports Strings, Hashes, Sets, Sorted Sets data types, you can migrate snapshot data for these supported data types only. If the backup file contains unsupported Redis OSS data types, MemoryDB Multi-Region will fail the migration operation by default.
- **Resource reservation** - MemoryDB Multi-Region is designed to protect regional availability. Some resources are permanently reserved on each node to ensure that local read and write requests can be served independently of the workload in the peer regions. These resources also serve to protect the local availability during events in the peer regions, including during Regionisolation events and recovery thereof. This results in different performance characteristics compared to single-region MemoryDB. MemoryDB Multi-Region supports both horizontal and vertical scaling to expand the available resources.
- **No RPO/RTO SLAs** - MemoryDB Multi-Region does not provide a stated RPO/RTO SLA. It will continue to accept writes in a AWS Region that has been isolated from other AWS Regions, potentially increasing cross replication lag indefinitely. We expect customers to detect isolation using the “MultiRegionClusterReplicationLag” metric and redirect their application traffic to another Region depending on the RPO they want.
- **No single end-point or auto-failover:** - In case of a regional outage, you will have to manually redirect your customer traffic to their application stack in another Region. You will have to ensure they have properly configured multi-region access to MemoryDB clusters.
- **No TTL support** - MemoryDB Multi-Region does not support TTL (Time to live).
- **No data tiering or vector search support** - MemoryDB Multi-Region does not support vector search and data tiering features.
- MemoryDB Multi-Region does not support read-modify-write commands (APPEND, RENAMENX, etc.).
- Redis OSS transaction atomicity and consistency are not guaranteed in MemoryDB Multi-Region.
- **Auth model** - MemoryDB Multi-Region API actions can be invoked from any supported region. The scope of permissions can be restricted by specifying the ARN of the multi-region cluster in an IAM policy. The format of the multi-region cluster ARN is `arn:aws:memorydb::<account-id>:multiregioncluster/multi-region-cluster-name`. There is no region information in the ARN.
- **Throughput limitations** - MemoryDB Multi-Region can support up to 1.3 GB/s read throughput per node in a Region and ~50 MB/s globally aggregated write throughput per shard.
- **AWS policy** - The AWS ReadOnlyAccess policy provides read-only access to AWS services and resources, but will not automatically retrieve details about one or more multi-Region clusters. In order to retrieve details about one or more multi-Region clusters, use the [AmazonMemoryDBReadOnlyAccess](security-iam-awsmanpol.md#iam.identitybasedpolicies.predefinedpolicies-readonly "security-iam-awsmanpol.md#iam.identitybasedpolicies.predefinedpolicies-readonly") policy or create [IAM customer managed policies](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") .
- **Deleting a regional cluster** - When deleting a regional cluster any associated Customer Managed Keys (CMKs) must remain valid until the regional cluster has finished deleting. This ensures that the remaining regional clusters can converge to a consistent state.
