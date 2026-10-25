

# Online migration to ElastiCache Serverless
<a name="migration-to-serverless"></a>

Amazon ElastiCache Serverless for Valkey supports migration from self-managed Valkey and Redis OSS on Amazon EC2 with zero downtime.

**Zero downtime**  
Zero downtime means zero Errors returned to the client during migration, measured the same way the [ElastiCache SLA](https://aws.amazon.com/elasticache/sla/) measures availability. Your application continues reading and writing through cutover.

These topics cover migration to an ElastiCache Serverless cache. To migrate to a node-based cluster instead, see [Online migration to ElastiCache node-based clusters](OnlineMigration.md).

Online migration moves your self-managed Valkey or Redis OSS data into ElastiCache Serverless for Valkey while your application keeps serving traffic. You do not need a third-party replication tool or a maintenance window to switch over.

During a migration, you point your application at the migration endpoint. The migration endpoint is your serverless cache's standard endpoint, so your application keeps using it after cutover. ElastiCache routes your application's requests to your source cache while it replicates your data to the target cache. When you complete the cutover, ElastiCache switches over at the next fully synced window, and your application is then served by ElastiCache Serverless.

**Console labeling**  
On the migration details page, the **Migration endpoint** field shows this address, and **Copy migration endpoint** copies it. The console hides the field while the migration is in Preparing migration, and shows it in every later state.

You can stop the data sync while it is in progress. Your application continues to be served by your source cache.

For more information about ElastiCache Serverless, see [Serverless caching](WhatIs.md#WhatIs.Overview).

The following topics describe the requirements, source authentication, the console procedure, and cutover modes for online migration.

**Topics**
+ [How a migration works](#w2aac20c13c23)
+ [Migration states](#w2aac20c13c25)
+ [Monitoring a migration](#w2aac20c13c27)
+ [How you learn that a migration finished](#w2aac20c13c29)
+ [What is supported at launch](#w2aac20c13c31)
+ [Prerequisites](migration-to-serverless-prerequisites.md)
+ [Source authentication](migration-to-serverless-auth.md)
+ [Migrate your data](migration-to-serverless-procedure.md)
+ [Cutover modes](migration-to-serverless-cutover.md)

## How a migration works
<a name="w2aac20c13c23"></a>

A migration has four steps. You start three of them with an API operation: prepare the migration, start the data sync, and complete the cutover. The fourth, pointing your application at the migration endpoint, is your own action. ElastiCache publishes an event at every transition.

**Prepare the migration.** ElastiCache validates your source cache against the migration requirements. It provisions the infrastructure that reads from your source and returns the migration endpoint. If a requirement is not met, the prepare step fails. ElastiCache reports a failure event on the cache that names the reason. The migration is rolled back, so the `Migration` object is removed and your cache returns to `available`. Correct the source or the network configuration, then try again. For more information, see [Prerequisites for online migration to ElastiCache Serverless](migration-to-serverless-prerequisites.md).

**Redirect your application.** Point your application at the migration endpoint and confirm that it is serving traffic through the endpoint. The console reminds you to do this before you start the data sync, because ElastiCache cannot detect whether your application has moved. Starting the data sync first does not affect the data on your target.

**Start the data sync.** ElastiCache begins replicating data from your source cache to the target cache. It keeps replicating as your application writes. Your application continues to be served throughout.

**Complete the cutover.** ElastiCache switches your migration endpoint over to serve from the target cache at the next fully synced window. You choose whether to trigger this yourself or have ElastiCache do it for you. Manual cutover is the default. For more information, see [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

`StartMigration` and `CompleteMigration` are rejected immediately when the migration is not healthy. The error tells you to check the cache's events for the reason.

The migration operations raise the following exceptions:


| Exception | When | 
| --- | --- | 
| MigrationHealthFault | The migration is not healthy. Set Force to true on CompleteMigration to bypass the check. | 
| ServerlessCacheAlreadyUnderMigrationFault | The cache is already the target of a migration. | 
| ServerlessCacheNotUnderMigrationFault | The cache has no migration to act on. | 
| InvalidServerlessCacheStateFault | The cache or the migration is not in a state that allows the operation. | 
| InvalidParameterValue | The request is not valid for the target cache or the migration, for example when the target has a public endpoint or uses the IPv6 or dual-stack network type, or when you call CompleteMigration without Force while the migration is ready-to-sync or an automatic cutover is pending. | 

For the console steps, see [Migrate your data to ElastiCache Serverless](migration-to-serverless-procedure.md).

## Migration states
<a name="w2aac20c13c25"></a>

You can check the current state at any time with `describe-serverless-caches`. This command returns a `Migration` object on the cache. The migration can be in one of the following states:


| State | What the console shows | What it means | 
| --- | --- | --- | 
| preparing | Preparing migration | ElastiCache is validating your source cache and provisioning migration infrastructure. | 
| ready-to-sync | Ready to sync | You can route your traffic through the migration endpoint and start the data sync. | 
| initiating-sync | Initializing sync | ElastiCache is starting replication across all shards. | 
| syncing | Data sync in progress | Replication is in progress. | 
| cutting-over | Cutover in progress | ElastiCache is finalizing the cutover to the target cache. | 
| stopping | Stopping | ElastiCache is stopping the data sync at your request. Traffic continues through the migration endpoint. When the data sync stops, the migration returns to Ready to sync. | 

The response also returns the migration endpoint address and port, along with a `CutoverMode` field. `CutoverMode` reports whether you opted in to automatic cutover when you started the data sync. It does not indicate that a cutover is in progress.

The Migrations page shows the current state only. It shows no warning, no error badge, and no failure state. When a step fails, the state moves backward to the previous state, and a failed prepare step removes the migration from the page. These two changes are the only failure signals on this page. A stop that you request also moves the state backward.

To find the reason, open the cache details page for your target cache and read the events on its Events tab.

The `cutting-over` state persists while ElastiCache tears down the migration infrastructure. By this point, your traffic has already moved to your target cache. Do not read this state as a sign that your target is not yet serving.

Before you start the migration, the Cutover method field on the migration details page shows the API default, which can render as Manual (default). It does not reflect a choice you have made. You choose the mode in the Start migration dialog box, where the control is labeled Cutover mode, with the values Manual cutover and Auto-cutover.

On the Valkey caches page, the Status column shows Migrating for a cache that is the target of a migration. This is a cache status, not a migration state.

The primary action button on the migration details page changes its label with the state. It reads Start migration until the data sync begins, and Complete migration afterward, in the same position. Complete migration is available only in Data sync in progress, and only when you chose Manual cutover. With Auto-cutover, it is disabled, because ElastiCache cuts over at the next fully synced window. Stop is available only in Data sync in progress, so it is disabled in Ready to sync and during cutover. Force complete is available in Ready to sync and Data sync in progress, and it is disabled during cutover.

## Monitoring a migration
<a name="w2aac20c13c27"></a>

ElastiCache publishes an event at each phase transition. The transitions are the following:
+ Prepare succeeded or failed
+ Start succeeded or failed
+ Cutover started
+ Complete succeeded or failed
+ Stop succeeded or failed

Failure events carry the reason. You read a migration's events on the target cache's Events tab, or on the Events page in the console navigation. The Events tab filter offers a fixed set of predefined groups, and no migration-specific filter is available. The Migrations page shows migrations that are in progress. A completed migration no longer appears there. To review a finished migration, read the target cache's events.

The console reads the migration state from `DescribeServerlessCaches`, which returns the `Migration` object on your target cache. It uses `DescribeEvents` to refresh the Monitor tab. The console can lag the underlying state.

There are no metrics specific to migration. You watch the target cache with the standard ElastiCache Serverless metrics. The migration details page in the console has a Monitor tab. The Monitor tab shows nine of the target cache's existing metrics: `BytesUsedForCache`, `CurrItems`, `NewConnections`, `NetworkBytesIn`, `NetworkBytesOut`, `GetTypeCmds`, `SetTypeCmds`, `Evictions`, and `CurrConnections`. The useful metrics for confirming that data is arriving are `BytesUsedForCache`, `CurrItems`, and `NetworkBytesIn`. For more information, see [Metrics and events for Valkey and Redis OSS serverless caches](serverless-metrics-events-redis.md).

The tab opens with an information banner, "Track your migration progress". It reads "These metrics show activity on your target cache. Use them to confirm your data is arriving during the migration and to verify traffic after cutover."

The Monitor tab shows no progress percentage and no progress bar. Migration progress can move backward.

The tab has a metric search box.

Before the data sync starts, the tab shows an empty state. It reads "No data to display yet" and "After prepare migration is complete and you have started data sync you will be able to see migration related metrics here."

## How you learn that a migration finished
<a name="w2aac20c13c29"></a>

You do not have to stay on the migration details page. The same status banner appears on the target cache's details page. With automatic cutover, the console takes you to the cache details page when the migration completes.

On success, the cache details page shows a banner that names the completion time and points you to that cache's Events tab. On failure, the same surface shows a failure banner that carries the event detail.

A success banner and a failure banner can both be present at once.

A banner stays until you dismiss it, and it does not come back once dismissed. The console shows outcome banners for migrations from the past 7 days.

A completed migration no longer appears on the Migrations page.

## What is supported at launch
<a name="w2aac20c13c31"></a>

At launch, online migration supports the following source and target combinations:


| Component | Supported at launch | 
| --- | --- | 
| Source | Self-managed Valkey 7.2 through 8.1, or Redis OSS 4.0 through 7.2, running on Amazon EC2 in cluster mode. | 
| Target | An ElastiCache Serverless for Valkey cache running Valkey 7.2, 8.1, or 9.0, that you create before you start. | 

Your source version must be no higher than your target version. ElastiCache managed caches and Amazon MemoryDB caches are not supported as sources. Valkey 9.0 is supported as a target but not as a source.