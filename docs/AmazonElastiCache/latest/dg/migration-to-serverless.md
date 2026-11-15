

# Online migration to ElastiCache Serverless
<a name="migration-to-serverless"></a>

Amazon ElastiCache Serverless for Valkey supports migration from self-managed Valkey and Redis OSS on Amazon EC2 with zero downtime.

**Zero downtime**  
Zero downtime means zero Errors returned to the client during migration, measured the same way the [ElastiCache SLA](https://aws.amazon.com/elasticache/sla/) measures availability. Your application continues reading and writing through cutover.

These topics cover migration to an ElastiCache Serverless cache. To migrate to a node-based cluster instead, see [Online migration to ElastiCache node-based clusters](OnlineMigration.md).

For more information about ElastiCache Serverless, see [Serverless caching](WhatIs.md#WhatIs.Overview).

Online migration moves your self-managed Valkey or Redis OSS data into ElastiCache Serverless for Valkey while your application keeps serving traffic. You do not need a third-party replication tool or a maintenance window to switch over.

Migration usage is free for the first 180 days per AWS account, starting when the account first prepares a migration. Your target ElastiCache Serverless cache bills at the standard rates during the migration. For more information, see [Amazon ElastiCache pricing](https://aws.amazon.com/elasticache/pricing/) on the AWS website.

During a migration, you point your application at the migration endpoint. The migration endpoint is your serverless cache's standard endpoint, so your application keeps using it after cutover. ElastiCache routes your application's requests to your source cache while it replicates your data to the target cache. When you complete the cutover, ElastiCache switches over at the next fully synced window, and your application is then served by ElastiCache Serverless.

You can stop the data sync while it is in progress. Your application continues to be served by your source cache.

The following topics describe the requirements, source authentication, the console and AWS CLI procedure, and cutover modes for online migration.

**Topics**
+ [How a migration works](#w2aac20c13c23)
+ [Migration states](#migration-to-serverless-states)
+ [Monitoring a migration](#w2aac20c13c27)
+ [How you learn that a migration finished](#w2aac20c13c29)
+ [Supported sources and targets](#w2aac20c13c31)
+ [Errors returned by the migration operations](#w2aac20c13c33)
+ [Prerequisites](migration-to-serverless-prerequisites.md)
+ [Source authentication](migration-to-serverless-auth.md)
+ [Migrate your data](migration-to-serverless-procedure.md)
+ [Cutover modes](migration-to-serverless-cutover.md)

## How a migration works
<a name="w2aac20c13c23"></a>

A migration has three steps, each with its own API operation: prepare the migration, start the data sync, and complete the cutover. ElastiCache publishes an event at every transition.

1. **Prepare the migration.** ElastiCache validates your source cache and your target cache against the migration requirements. It provisions the infrastructure that reads from your source and returns the migration endpoint. You then point your application at the migration endpoint and confirm that it is serving traffic through the endpoint. The console reminds you to do this before you start the data sync, because ElastiCache cannot detect whether your application has moved. For more information, see [Prerequisites for online migration to ElastiCache Serverless](migration-to-serverless-prerequisites.md) and [Redirect your application](migration-to-serverless-procedure.md#migration-to-serverless-redirect).

1. **Start the data sync.** ElastiCache begins replicating data from your source cache to the target cache. It keeps replicating as your application writes. For more information, see [Start the data sync](migration-to-serverless-procedure.md#migration-to-serverless-start).

1. **Complete the cutover.** ElastiCache switches your migration endpoint over to serve from the target cache at the next fully synced window. You choose whether to trigger this yourself or have ElastiCache do it for you. For more information, see [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

For the console and AWS CLI steps, see [Migrate your data to ElastiCache Serverless](migration-to-serverless-procedure.md).

## Migration states
<a name="migration-to-serverless-states"></a>

You can check the current state at any time with `describe-serverless-caches`. This command returns a `Migration` object on the cache, which is the record of your migration that `describe-serverless-caches` returns. The migration can be in one of the following states:


| State | What the console shows | What it means | What you can do | 
| --- | --- | --- | --- | 
| preparing | Preparing migration | ElastiCache is validating your source cache and provisioning migration infrastructure. | Wait for Ready to sync. | 
| ready-to-sync | Ready to sync | You can route your traffic through the migration endpoint and start the data sync. | Choose Start migration to start the data sync. Force complete is available. Stop is disabled. | 
| initiating-sync | Initializing sync | ElastiCache is starting replication across all shards. | Wait for Data sync in progress. | 
| syncing | Data sync in progress | Replication is in progress. | Choose Complete migration. Complete migration is available only when you chose Manual cutover. With Auto-cutover, it is disabled, because ElastiCache cuts over at the next fully synced window. Stop and Force complete are available. | 
| cutting-over | Cutover in progress | ElastiCache is finalizing the cutover to the target cache. | Wait for the cutover to finish. Stop and Force complete are disabled. | 
| stopping | Stopping | ElastiCache is stopping the data sync at your request. Traffic continues through the migration endpoint. When the data sync stops, the migration returns to Ready to sync. | Wait for Ready to sync. | 

The primary action button on the migration details page changes its label with the state. It reads Start migration until the data sync begins, and Complete migration afterward, in the same position.

How long the prepare step takes depends on the size of your source, because ElastiCache provisions migration infrastructure to match it. While the migration state reads `preparing`, the step is still running, so wait for `ready-to-sync`. After you start the data sync, the migration stays in `initiating-sync` until replication begins.

You can check the status with the AWS CLI. Run the following command:

```
aws elasticache describe-serverless-caches \
    --serverless-cache-name {{my-cache}} \
    --query "ServerlessCaches[0].[Status,Migration.Status]" \
    --output text
```

The command returns the cache status and the migration status:


| Cache status | Migration status | What it means | 
| --- | --- | --- | 
| migrating | preparing | The prepare step is running. | 
| migrating | ready-to-sync | The prepare step succeeded. | 
| migrating | syncing | The data sync is running. | 
| available | None | The migration ended. It completed, it was force completed, or the prepare step failed, so read the events. | 

The response also returns the migration endpoint address and port, along with a `CutoverMode` field. `CutoverMode` reports whether you opted in to automatic cutover when you started the data sync. It does not indicate that a cutover is in progress.

**Console labeling**  
On the migration details page, the **Migration endpoint** field shows this address, and **Copy migration endpoint** copies it. The console hides the field while the migration is in Preparing migration, and shows it in every later state.

The Migrations page shows the current state only. It shows no warning, no error badge, and no failure state. When a step fails, the state moves backward to the previous state, and a failed prepare step removes the migration from the page. These two changes are the only failure signals on this page. A stop that you request also moves the state backward.

To find the reason, open the cache details page for your target cache and read the events on its Events tab.

ElastiCache spends most of the `cutting-over` state tearing down the migration infrastructure. With Manual cutover, the state starts when you complete the migration, and ElastiCache first waits for a fully synced window to switch your traffic to your target. With Auto-cutover, the state stays `syncing` until ElastiCache finds that window. After the switch, your traffic is on your target for the rest of the state.

**Note**  
Before you start the migration, the **Cutover method** field on the migration details page shows the API default, which can render as **Manual (default)**. It does not reflect a choice you have made. You choose the mode in the **Start migration** dialog box, where the control is labeled **Cutover mode**, with the values **Manual cutover** and **Auto-cutover**.

**Note**  
On the Valkey caches page, the **Status** column shows **Migrating** for a cache that is the target of a migration. This is a cache status, not a migration state.

## Monitoring a migration
<a name="w2aac20c13c27"></a>

ElastiCache publishes an event at each phase transition. The transitions are the following:
+ Prepare succeeded or failed
+ Start succeeded or failed
+ Cutover started
+ Complete succeeded or failed
+ Stop succeeded or failed

Failure events carry the reason.

For a migration that succeeds, the events read as follows, where `my-cache` is the name of your target cache:


| Transition | Event message | 
| --- | --- | 
| Prepare succeeded | Successfully prepared serverless cache {{my-cache}} for migration. | 
| Start succeeded | Successfully started data sync for serverless cache {{my-cache}}. | 
| Cutover started | Cutover initiated for serverless cache {{my-cache}}. Waiting for a suitable window to finalize the migration. | 
| Complete succeeded | Successfully completed the migration for serverless cache {{my-cache}}. | 
| Stop succeeded | Successfully stopped data sync for serverless cache {{my-cache}}. | 
| Force complete succeeded | Successfully completed the migration for serverless cache {{my-cache}} with Force. | 

When a step fails, the event names the step and gives the reason:
+ Failed to prepare migration for serverless cache {{my-cache}}. {{reason}}
+ Failed to start data sync for serverless cache {{my-cache}}. {{reason}}
+ Failed to complete the migration for serverless cache {{my-cache}}. {{reason}}
+ Failed to stop the migration for serverless cache {{my-cache}}. {{reason}}
+ Migration error for serverless cache {{my-cache}}. {{reason}}

For example, a prepare step on a target that contains data reports Failed to prepare migration for serverless cache {{my-cache}}. The serverless cache must have no keys before migration can begin.

To list the events with the AWS CLI, run the following command:

```
aws elasticache describe-events \
    --source-type serverless-cache \
    --source-identifier {{my-cache}} \
    --duration {{120}}
```

Where:
+ `my-cache` is the name of your target cache.
+ `120` is the number of minutes of events to return.

To follow a migration's progress, check the migration state that `describe-serverless-caches` returns. Use the events to learn the reason when a step fails. An event can appear up to about a minute after the state changes.

You read a migration's events on the target cache's Events tab, or on the Events page in the console navigation. The Events tab filter offers a fixed set of predefined groups, and no migration-specific filter is available. The Migrations page shows migrations that are in progress. A completed migration no longer appears there. To review a finished migration, read the target cache's events.

The console reads the migration state from `DescribeServerlessCaches`, which returns the `Migration` object on your target cache. It uses `DescribeEvents` to refresh the Monitor tab. The console can lag the underlying state.

There are no metrics specific to migration. You watch the target cache with the standard ElastiCache Serverless metrics. The migration details page in the console has a Monitor tab. The Monitor tab shows nine of the target cache's existing metrics:
+ `BytesUsedForCache`
+ `CurrItems`
+ `NewConnections`
+ `NetworkBytesIn`
+ `NetworkBytesOut`
+ `GetTypeCmds`
+ `SetTypeCmds`
+ `Evictions`
+ `CurrConnections`

To confirm that replication is running, run `INFO replication` on each primary of your source. The migration appears there as a connected replica with `state=online` and a `lag` value. For more information, see [Metrics and events for Valkey and Redis OSS serverless caches](serverless-metrics-events-redis.md).

The tab opens with an information banner, "Track your migration progress". It reads "These metrics show activity on your target cache. Use them to confirm your data is arriving during the migration and to verify traffic after cutover."

The Monitor tab shows no progress percentage and no progress bar. Migration progress can move backward.

Before the data sync starts, the tab shows an empty state.

## How you learn that a migration finished
<a name="w2aac20c13c29"></a>

You do not have to stay on the migration details page. The same status banner appears on the target cache's details page. With automatic cutover, the console takes you to the cache details page when the migration completes.

On success, the cache details page shows a banner that names the completion time and points you to that cache's Events tab. On failure, the same surface shows a failure banner that carries the event detail.

A success banner and a failure banner can both be present at once.

A banner stays until you dismiss it, and it does not come back once dismissed. The console shows outcome banners for migrations from the past 7 days.

A completed migration no longer appears on the Migrations page.

## Supported sources and targets
<a name="w2aac20c13c31"></a>

Online migration supports the following source and target combinations:


| Component | Supported | 
| --- | --- | 
| Source | Self-managed Valkey 7.2 through 8.1, or Redis OSS 4.0 through 7.2, running on Amazon EC2 in cluster mode. | 
| Target | An ElastiCache Serverless for Valkey cache running Valkey 7.2, 8.1, or 9.0, that you create before you start. | 

Your source version must be no higher than your target version. ElastiCache managed caches and Amazon MemoryDB caches are not supported as sources. Valkey 9.0 is supported as a target but not as a source.

Your source must run in cluster mode. To migrate a source that runs with cluster mode disabled, use online migration to a node-based cluster. For more information, see [Online migration to ElastiCache node-based clusters](OnlineMigration.md).

## Errors returned by the migration operations
<a name="w2aac20c13c33"></a>

`StartMigration` and `CompleteMigration` are rejected immediately when the migration is not healthy. The error tells you to check the cache's events for the reason.

The migration operations raise the following exceptions:


| Exception | When | 
| --- | --- | 
| MigrationHealthFault | The migration is not healthy. Set Force to true on CompleteMigration to bypass the check. | 
| ServerlessCacheAlreadyUnderMigrationFault | The cache is already the target of a migration. | 
| ServerlessCacheNotUnderMigrationFault | The cache has no migration to act on. | 
| InvalidServerlessCacheStateFault | The cache or the migration is not in a state that allows the operation. | 
| InvalidParameterValue | The request is not valid for the target cache or the migration, for example when the target has a public endpoint or uses the IPv6 or dual-stack network type, or when you call CompleteMigration without Force while the migration is ready-to-sync or an automatic cutover is pending. | 