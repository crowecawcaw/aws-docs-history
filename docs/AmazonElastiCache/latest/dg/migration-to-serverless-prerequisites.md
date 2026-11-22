

# Prerequisites and limitations for online migration to ElastiCache Serverless

Before you start an online migration, confirm that your source cache and your target cache meet the following requirements. ElastiCache checks these requirements when you prepare the migration and checks some of them again when you start the data sync. If a requirement is not met, the step fails. ElastiCache reports a failure event on the cache that names the requirement. If the prepare step fails, ElastiCache rolls back the migration, removes the `Migration` object and returns your cache to `available`. Correct the requirement, then try again.

## Supported sources and targets
<a name="migration-to-serverless-supported"></a>

Online migration supports the following source and target combinations:
+ **Source** – Self-managed Valkey 7.2 through 8.1, or Redis OSS 4.0 through 7.2, running on Amazon EC2 in cluster mode.
+ **Target** – An ElastiCache Serverless for Valkey cache running Valkey 7.2, 8.1, or 9.0, that you create before you start.

Your source version must be no higher than your target version. ElastiCache managed caches and Amazon MemoryDB caches are not supported as sources. Valkey 9.0 is supported as a target but not as a source.

Your source must run in cluster mode. To migrate a source that runs with cluster mode disabled, use online migration to a node-based cluster. For more information, see [Online migration to ElastiCache node-based clusters](OnlineMigration.md).

## Source cache requirements
<a name="migration-to-serverless-source-requirements"></a>

Your source cache must meet the following requirements. ElastiCache checks each one at the times shown.


| Requirement | What your source must meet | When ElastiCache checks it | 
| --- | --- | --- | 
| Engine and version | Valkey 7.2 through 8.1, or Redis OSS 4.0 through 7.2. Later versions are not supported as a source. | Prepare and start | 
| Version not higher than the target | No higher than the version of your target ElastiCache Serverless cache. Migrating from a higher source version to a lower target version is rejected. | Prepare and start | 
| Cluster mode | Runs in cluster mode. Prepare rejects a source that has cluster mode disabled. If your source stops running in cluster mode after prepare, the migration fails. | Prepare, and during the migration | 
| Deployment | A self-managed cache running on Amazon EC2. ElastiCache managed caches and Amazon MemoryDB caches are not supported as sources. | Prepare | 
| Memory per node | Up to 32 GB of data, measured as used\_memory | Prepare | 
| Shards | Up to 166 shards | Prepare | 
| Slot coverage | Hash slots cover the full range with no gaps and no overlaps. | Prepare | 
| No resharding | Not undergoing a slot migration when you prepare the migration, and not undergoing one while the migration runs. A slot migration that begins mid-flight fails the migration. | Prepare, and during the migration | 
| Node health | Nodes must be healthy. ElastiCache checks node state when you prepare and continues to monitor node state. | Prepare, and during the migration | 
| Protected mode | Protected mode turned off (protected-mode no) on a source that has no password. With protected mode on, a node without a password accepts only local connections, so ElastiCache cannot connect to it. A source that requires a password can keep protected mode on. | Prepare | 
| Replication commands | Your source must accept a replica connection from the migration path. It must support PSYNC and REPLCONF. If you renamed or disabled these commands on your source, restore them before you migrate. | Prepare and start | 
| Key name size | No key name in your source can exceed 4 KiB, which is the ElastiCache Serverless limit. An oversized key name fails the migration during the initial data load, and you cannot start the data sync again. ElastiCache writes the key to your target before it reports the failure. To recover, see [Troubleshooting a key name that exceeds 4 KiB](migration-to-serverless-troubleshooting.md#migration-to-serverless-troubleshooting-key-name-size). | During the initial data load | 
| CPU headroom on source primaries | Your source primaries serve your application's traffic for the whole migration, up until cutover. You need CPU headroom on your source primaries to serve your full read and write workload while the migration runs. Review your workload and scale out before you prepare the migration. A source primary that becomes overloaded can compromise the health of the migration. For more information about when traffic moves off your source, see [Cutting over](migration-to-serverless-procedure.md#migration-to-serverless-complete). | Not checked. Your responsibility. | 
| Memory for the initial full sync | ElastiCache replicates your data with the replication protocol, which starts with a full sync. A full sync forks the process on your source primary. That fork needs memory available on the primary beyond what your dataset already uses. How much it needs rises with your write rate during the sync, because your source primary must hold writes that arrive during the fork. | Not checked. Your responsibility. | 
| Stable environment | Your environment must stay stable for the whole migration. Three things must stay valid until the migration completes: your network path, your source TLS certificate, and your AWS Secrets Manager credentials. If any of them changes mid-migration, ElastiCache reports a migration error event, and the migration cannot be started again. For more information, see [Cutting over](migration-to-serverless-procedure.md#migration-to-serverless-complete). | During the migration | 
| Authentication and encryption | If your source requires authentication, store the credentials in Secrets Manager and grant ElastiCache permission to read the secret. The user name and password in the secret must meet the ElastiCache requirements, whether you created the secret or ElastiCache created it for you. If your source requires TLS, provide the source TLS configuration. For more information, see [Source authentication for online migration to ElastiCache Serverless](migration-to-serverless-auth.md). | Prepare and start | 

Compatibility holds for Redis versions whose data types Valkey supports. Valkey forked from Redis 7.2.4, where the supported range ends.

A second, separate check applies while the migration is running. If your source dataset grows beyond what your target cache can hold, the migration fails with a memory error. Leave headroom if your dataset is growing.

## Target cache requirements
<a name="migration-to-serverless-target-requirements"></a>

Create an ElastiCache Serverless for Valkey cache before you start. Your target must meet all of the following requirements:
+ **Available and idle** – The cache is in the `available` state with no other operation in progress.
+ **Empty** – The cache contains no keys. Flush the target yourself before you prepare the migration. If the target contains data, preparation fails.
+ **No active pub/sub connections** – The cache has no subscribed clients when you prepare the migration.
+ **No public endpoint** – The cache has no public endpoint. Leave public connectivity turned off when you create the target cache. For a cache that already exists, confirm that it has no public endpoint before you prepare the migration.
+ **Network type** – The cache uses the IPv4 network type. ElastiCache rejects a target cache that uses the IPv6 or dual-stack network type.
+ **Version** – The cache runs Valkey 7.2, 8.1, or 9.0, at a version at least as high as your source version.
+ **Authentication** – The cache accepts the credentials that your application uses on your source. If your source requires authentication, set up the same users on your target before you prepare the migration. For more information about setting up target users, see [Setting up your application's users on your target](migration-to-serverless-auth.md#migration-to-serverless-auth-target-users).

Your target inherits the standard ElastiCache Serverless limits, and your data must fit inside them:
+ **Size per cache** – 5,000 GiB
+ **Size per slot** – 32 GiB
+ **ElastiCache processing units** – 15,000,000 ECPUs per second
+ **Key name length** – 4 KiB

## Network requirements
<a name="migration-to-serverless-network-requirements"></a>

ElastiCache connects to your source from the VPC of your target cache. Confirm the following:
+ Confirm that your source is reachable on a private endpoint from that VPC. Also confirm that your source security group allows inbound traffic from ElastiCache.
+ Your source nodes must listen on addresses that this VPC can reach. The default Valkey and Redis OSS configuration file binds to `127.0.0.1`, which accepts only local connections, so bind each node to its private IP address. Each node must also report a reachable address in its cluster topology, because ElastiCache discovers the rest of your nodes from the first one.
+ For the security group rule, allow inbound TCP traffic on your source port from the security group of your target cache, or from the IPv4 CIDR ranges of its subnets.
+ For the source address, enter the private IP address of a source node, or a host name that resolves through public DNS. A host name that resolves only in your VPC's private DNS fails the prepare step.
+ Create your target cache with at least three subnets in different Availability Zones, each with free IP addresses. In a Region where your account has two Availability Zones, such as US West (N. California), use a subnet in each of the two. You cannot change the subnets of a serverless cache after you create it. If the prepare step or the data sync fails on subnets, the error message names the Availability Zones that need a subnet. Because you cannot change the subnets of a serverless cache, create a new target cache with a subnet in each Availability Zone that the message names, and prepare the migration again.
+ Preparing a migration creates network interfaces in the subnets of your target cache. They use the security groups of your target cache, and ElastiCache deletes them when the migration completes. The prepare step fails if your target's subnets have no free IP addresses or your VPC has no network interface quota headroom.
+ Keep the Secrets Manager secret that you provided until the migration completes. If a node is replaced during the migration, ElastiCache runs network and authentication setup again, and a missing secret fails that step.

## Command behavior during a migration
<a name="migration-to-serverless-command-behavior"></a>

While your application is served through the migration endpoint, ElastiCache Serverless command support applies, not your source's command support.

Commands that ElastiCache Serverless does not support are rejected at the migration endpoint, the same as they would be on any serverless cache.

Some commands behave differently on ElastiCache Serverless than on a self-managed cache. These include `FLUSH`, the `CLUSTER` commands, and the publish and subscribe commands. ElastiCache Serverless requires every Lua script call to declare at least one key. A call such as `EVALSHA` with zero keys returns `ERR Lua scripts without any input keys are not supported`. Review your application's use of these commands before you start. For more information, see [Supported and restricted Valkey, Memcached, and Redis OSS commands](SupportedCommands.md).

**Writes during the migration**  
Do not send writes directly to your source during the migration. Commands that ElastiCache Serverless does not support are not replicated. A client can bypass the migration endpoint and write an unsupported command straight to your source. That makes your target diverge. ElastiCache reports a migration error event when it detects this. After ElastiCache reports that error, you cannot start the migration again. To end it, you complete the migration with force, which accepts the inconsistency.

The following commands need your attention during a migration:
+ **Scripts** – Scripts you loaded on your source before the migration are not replicated to your target. Re-issue `SCRIPT LOAD` for them through the migration endpoint any time after the migration reaches `ready-to-sync` and before cutover. A script that is missing on the target returns `NOSCRIPT` after cutover.
+ **Pub/sub subscriptions** – Pub/sub subscriptions do not survive cutover. Subscribed clients are disconnected at cutover and have to reconnect and re-subscribe.

## Client configuration
<a name="migration-to-serverless-client-config"></a>

Your application connects to the migration endpoint with TLS, because all ElastiCache Serverless caches use encryption in transit. If your application reaches your source without TLS, turn on TLS in your client before you point it at the migration endpoint. The security group of your target cache must allow inbound TCP traffic from your application on ports 6379 and 6380, because many clients connect to both.

Instead of caching node IP addresses in your application, use the migration endpoint.

Stay within Valkey's default limit of 10,000 client connections during a migration. If your workload needs more connections than that, open them gradually rather than all at once.

Because commands are serialized during a migration, a client that relies on pipelining needs more concurrent connections to sustain the same request rate. If your client uses a connection pool, review its size before you migrate, and consider raising it for the duration of the migration. For more information about serialized commands, see the pipelining limitation in the Limitations section of this topic.

## Limitations
<a name="migration-to-serverless-limitations"></a>

The following limitations apply during a migration:
+ **Permanent errors** – Migration errors are reported as permanent. A migration that has reported an error cannot be started again, even after you fix the underlying problem. You can stop it, and your only way to end it is to complete the migration with force. For more information, see [Cutting over](migration-to-serverless-procedure.md#migration-to-serverless-complete).
+ **Force complete** – Force complete does not roll back. It skips the pre-cutover health check and the cluster-wide convergence check. For more information, see [Cutting over](migration-to-serverless-procedure.md#migration-to-serverless-complete).
+ **Rollback after cutover** – There is no rollback after cutover. To return to your source cache, you must move your application traffic back to it yourself. Writes that your application makes after cutover exist only on your target. For more information, see [Cutting over](migration-to-serverless-procedure.md#migration-to-serverless-complete).
+ **The reader endpoint is not supported during a migration** – Send your traffic to the migration endpoint and not the cache's reader endpoint.
+ **One migration per cache** – A cache can be the target of only one migration at a time.
+ **Pipelining is not supported during the migration** – If your application pipelines commands, the migration endpoint serializes them from the moment the migration reads `ready-to-sync`. A batch of 100 commands then takes 100 round trips instead of one. Latency for those batches increases in proportion to the batch depth.
+ **RESP3 Pub/Sub with regular commands on the same connection** – RESP3 lets a client run regular commands on a connection that has active Pub/Sub subscriptions (`SUBSCRIBE` or `SSUBSCRIBE`). This isn't supported while a migration is in progress. During migration, use separate connections for Pub/Sub and for regular commands. Most client libraries do this by default. This restriction ends when the migration completes.
+ **Total migration throughput scales with your source shard count** – A source with many shards migrates faster than a source with few.
+ **High-throughput sources with few shards** – This release is not suited to a high-throughput source with few shards. Migration throughput is provisioned per source shard. A source that concentrates high traffic into a small number of shards is most likely to be limited. If that describes your source, review the CPU headroom on source primaries prerequisite in the source cache requirements, or plan the migration for a lower-traffic period.
+ **Billing after you stop the data sync** – Billing does not stop when you stop the data sync. `StopMigration` leaves the migration infrastructure provisioned. `CompleteMigration` is the call that ends the migration and its charges. Your target ElastiCache Serverless cache continues to bill until you delete it.