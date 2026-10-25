

# Prerequisites for online migration to ElastiCache Serverless
<a name="migration-to-serverless-prerequisites"></a>

Before you start an online migration, confirm that your source cache and your target cache meet the following requirements. ElastiCache checks these requirements when you prepare the migration and checks some of them again when you start the data sync. If a requirement is not met, the step fails. ElastiCache reports a failure event on the cache that names the requirement. If the prepare step fails, the migration is rolled back, so the `Migration` object is removed and your cache returns to `available`. Correct the requirement, then try again.

## Source cache requirements
<a name="w2aac20c13c33b5"></a>

Your source cache must meet the following requirements. ElastiCache checks each one at the times shown.


| Requirement | What your source must meet | When ElastiCache checks it | 
| --- | --- | --- | 
| Engine and version | Valkey 7.2 through 8.1, or Redis OSS 4.0 through 7.2. Later versions are not supported as a source. | Prepare and start | 
| Version not higher than the target | No higher than the version of your target ElastiCache Serverless cache. Migrating from a higher source version to a lower target version is rejected. | Prepare and start | 
| Cluster mode | Runs in cluster mode. A cluster-mode-disabled source is rejected. A source that leaves cluster mode during a migration fails the migration. | Prepare, and during the migration | 
| Deployment | A self-managed cache running on Amazon EC2. ElastiCache managed caches and Amazon MemoryDB caches are not supported as sources. | Prepare | 
| Memory per node | Up to 32 GB of data, measured as used\_memory | Prepare | 
| Shards | Up to 166 shards | Prepare | 
| Slot coverage | Hash slots cover the full range with no gaps and no overlaps. | Prepare | 
| No resharding | Not undergoing a slot migration when you prepare the migration, and not undergoing one while the migration runs. A slot migration that begins mid-flight fails the migration. | Prepare, and during the migration | 
| Node health | Nodes must be healthy. ElastiCache checks node state when you prepare and continues to monitor node state. | Prepare, and during the migration | 

Compatibility holds for Redis versions whose data types Valkey supports. Valkey forked from Redis 7.2.4, where the supported range ends.

A second, separate check applies while the migration is running. If your source dataset grows beyond what your target cache can hold, the migration fails with a memory error. Leave headroom if your dataset is growing.

**Key name size.** No key name in your source can exceed 4 KiB, which is the ElastiCache Serverless limit. An oversized key name fails the migration during the initial data load, and you cannot start the data sync again. ElastiCache writes the key to your target before it reports the failure. To try again, end the migration with force complete. Your migration endpoint then serves from your target, so move your application traffic back to your source. Then flush the target and prepare a new migration. For more information, see [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

**Replication support.** Your source must accept a replica connection from the migration path. It must support `PSYNC` and `REPLCONF`. If you renamed or disabled these commands on your source, restore them before you migrate.

**Stable environment.** Your environment must stay stable for the whole migration. Three things must stay valid until the migration completes: your network path, your source TLS certificate, and your AWS Secrets Manager credentials. If any of them changes mid-migration, ElastiCache reports a migration error event, and the migration cannot be started again. For more information, see [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

**Source primary capacity.** Your source primaries serve your application's traffic for the whole migration, up until cutover. You need CPU headroom on your source primaries to serve your full read and write workload while the migration runs. Review your workload and scale out before you prepare the migration. A source primary that becomes overloaded can compromise the health of the migration. For more information about when traffic moves off your source, see [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

**Memory for the initial full sync.** ElastiCache replicates your data with the replication protocol, which starts with a full sync. A full sync forks the process on your source primary. That fork needs memory available on the primary beyond what your dataset already uses. How much it needs rises with your write rate during the sync, because your source primary must hold writes that arrive during the fork.

**Authentication and encryption.** If your source requires authentication, store the credentials in Secrets Manager and grant ElastiCache permission to read the secret. The user name and password in the secret must meet the ElastiCache requirements, whether you created the secret or ElastiCache created it for you. If your source requires TLS, provide the source TLS configuration. For more information, see [Source authentication for online migration to ElastiCache Serverless](migration-to-serverless-auth.md).

## Target cache requirements
<a name="w2aac20c13c33b7"></a>

Create an ElastiCache Serverless for Valkey cache before you start. Your target must meet all of the following requirements.


| Requirement | What your target cache must meet | 
| --- | --- | 
| Available and idle | In the available state with no other operation in progress. | 
| Empty | Contains no keys. Flush the target yourself before you prepare the migration. If the target contains data, preparation fails. | 
| No active pub/sub connections | No subscribed clients when you prepare the migration. | 
| No public endpoint | No public endpoint. Leave public connectivity turned off when you create the target cache. For a cache that already exists, confirm that it has no public endpoint before you prepare the migration. | 
| Network type | IPv4. ElastiCache rejects a target cache that uses the IPv6 or dual-stack network type. | 
| Version | Runs Valkey 7.2, 8.1, or 9.0, at a version at least as high as your source version. | 

Your target inherits the standard ElastiCache Serverless limits, and your data must fit inside them:


| Limit | Value | 
| --- | --- | 
| Size per cache | 5,000 GiB | 
| Size per slot | 32 GiB | 
| ElastiCache processing units | 15,000,000 ECPUs per second | 
| Key name length | 4 KiB | 

## Network requirements
<a name="w2aac20c13c33b9"></a>

ElastiCache connects to your source from the VPC of your target cache. Confirm that your source is reachable on a private endpoint from that VPC. Also confirm that your source security group allows inbound traffic from ElastiCache.

Your target cache must have a subnet in each Availability Zone that ElastiCache Serverless uses in your AWS Region. If it does not, the prepare step fails.

Preparing a migration creates network interfaces and a security group in your account, so you need quota headroom in four places. The prepare step fails if any of them is exhausted:
+ Free IP addresses in the subnets your target cache uses.
+ Network interface quota for the VPC.
+ Security group quota for the VPC.
+ Security group rule quota.

**Resources that prepare creates.** Do not delete the resources that prepare creates. The security group that ElastiCache creates when you prepare the migration, and the Secrets Manager secret you provided, both must keep existing until the migration completes. If a node is replaced during the migration, ElastiCache re-runs network and authentication setup. A missing security group or secret fails that step.

## Command behavior during a migration
<a name="w2aac20c13c33c11"></a>

While your application is served through the migration endpoint, ElastiCache Serverless command support applies, not your source's command support.

Commands that ElastiCache Serverless does not support are rejected at the migration endpoint, the same as they would be on any serverless cache.

Some commands behave differently on ElastiCache Serverless than on a self-managed cache. These include `FLUSH`, the `CLUSTER` commands, and the publish and subscribe commands. Review your application's use of these commands before you start. For more information, see [Supported and restricted Valkey, Memcached, and Redis OSS commands](SupportedCommands.md).

**Do not send writes directly to your source during the migration.** Commands that ElastiCache Serverless does not support are not replicated. A client can bypass the migration endpoint and write an unsupported command straight to your source. That makes your target diverge. ElastiCache reports a migration error event when it detects this. After ElastiCache reports that error, you cannot start the migration again. To end it, you complete the migration with force, which accepts the inconsistency.

**Scripts.** Scripts you loaded on your source before the migration are not replicated to your target. Re-issue `SCRIPT LOAD` for them through the migration endpoint. A script that is missing on the target returns `NOSCRIPT` after cutover.

**Pub/sub subscriptions.** Pub/sub subscriptions do not survive cutover. Subscribed clients are disconnected at cutover and have to reconnect and re-subscribe.

## Client configuration
<a name="w2aac20c13c33c13"></a>

Instead of caching node IP addresses in your application, use the migration endpoint.

Stay within Valkey's default limit of 10,000 client connections during a migration. If your workload needs more connections than that, open them gradually rather than all at once.

Because commands are serialized during a migration, a client that relies on pipelining needs more concurrent connections to sustain the same request rate. If your client uses a connection pool, review its size before you migrate, and consider raising it for the duration of the migration. For more information about serialized commands, see the pipelining limitation in the Limitations section of this topic.

## What ElastiCache manages and what you manage
<a name="w2aac20c13c33c15"></a>

A migration spans your infrastructure and ours.


| ElastiCache manages | You manage | 
| --- | --- | 
| The migration endpoint that your application connects to. | Your source cache, including its capacity, its engine version, and its availability. ElastiCache reads from your source but does not operate it. | 
| The infrastructure that reads from your source cache and replicates to your target during the migration. | The source requirements on this page, including replication support, the memory limit per node, the engine version range, and network reachability. | 
| The target ElastiCache Serverless cache. | Your client configuration, including retry behavior, connection pooling, and not caching node IP addresses. | 

A failed request can originate on either side. If you see errors during a migration, check your source cache health and capacity first. A source that is unavailable or out of memory surfaces as errors through the migration endpoint.

The ElastiCache Service Level Agreement applies to your ElastiCache Serverless cache during a migration on the same terms as at any other time.

## Limitations
<a name="w2aac20c13c33c17"></a>

**Default cutover mode.** Cutover is manual by default. You can opt in to automatic cutover when you start the data sync. For more information, see [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

**Stopping the data sync.** You can stop the data sync while it is in progress. Your application continues to be served by your source cache. For more information, see [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

**Permanent errors.** Migration errors are reported as permanent. A migration that has reported an error cannot be started again, even after you fix the underlying problem. You can stop it, and your only way to end it is to complete the migration with force. For more information, see [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

**Force complete.** Force complete does not roll back. It skips the pre-cutover health check and the cluster-wide convergence check. For more information, see [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

**Rollback after cutover.** There is no rollback after cutover. To return to your source cache, you must move your application traffic back to it yourself. For more information, see [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

**The reader endpoint is not supported during a migration.** Send your traffic to the migration endpoint and not the cache's reader endpoint.

**One migration per cache.** A cache can be the target of only one migration at a time.

**Pipelining is not supported during the migration.** If your application pipelines commands, they are serialized during the migration. A batch of 100 commands then takes 100 round trips instead of one. Latency for those batches increases in proportion to the batch depth.

**RESP3 Pub/Sub with regular commands on the same connection.** RESP3 lets a client run regular commands on a connection that has active Pub/Sub subscriptions (`SUBSCRIBE` or `SSUBSCRIBE`). This isn't supported while a migration is in progress. During migration, use separate connections for Pub/Sub and for regular commands. Most client libraries do this by default. This restriction ends when the migration completes.

**Total migration throughput scales with your source shard count.** A source with many shards migrates faster than a source with few.

**High-throughput sources with few shards.** This release is not suited to a high-throughput source with few shards. Migration throughput is provisioned per source shard. A source that concentrates high traffic into a small number of shards is most likely to be limited. If that describes your source, review the source primary capacity prerequisite in the source cache requirements, or plan the migration for a lower-traffic period.

**Billing after you stop the data sync.** Billing does not stop when you stop the data sync. `StopMigration` leaves the migration infrastructure provisioned. `CompleteMigration` is the call that ends the migration and its charges. Your target ElastiCache Serverless cache continues to bill until you delete it.

## Related topics
<a name="w2aac20c13c33c19"></a>
+ [Online migration to ElastiCache Serverless](migration-to-serverless.md)
+ [Source authentication for online migration to ElastiCache Serverless](migration-to-serverless-auth.md)
+ [Migrate your data to ElastiCache Serverless](migration-to-serverless-procedure.md)
+ [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md)
+ [Create a Valkey serverless cache](GettingStarted.serverless-valkey.step1.md)