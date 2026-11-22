

# Monitoring a migration to ElastiCache Serverless

## Migration states and events
<a name="migration-to-serverless-states-events"></a>

A migration moves through a sequence of states, and ElastiCache emits an event at each transition.

### Migration states
<a name="migration-to-serverless-states"></a>

A migration can be in one of the following states.


| State | What the console shows | What it means | What you can do | 
| --- | --- | --- | --- | 
| preparing | Preparing migration | ElastiCache is validating your source cache and provisioning migration infrastructure. | Wait for Ready to sync. | 
| ready-to-sync | Ready to sync | You can route your traffic through the migration endpoint and start the data sync. | Choose Start migration to start the data sync. Force complete is available. Stop is disabled. | 
| initiating-sync | Initializing sync | ElastiCache is starting replication across all shards. | Wait for Data sync in progress. | 
| syncing | Data sync in progress | Replication is in progress. | Choose Complete migration. Complete migration is available only when you chose Manual cutover. With Auto-cutover, it is disabled, because ElastiCache cuts over at the next fully synced window. Stop and Force complete are available. | 
| cutting-over | Cutover in progress | ElastiCache is finalizing the cutover to the target cache. | Wait for the cutover to finish. Stop and Force complete are disabled. | 
| stopping | Stopping | ElastiCache is stopping the data sync at your request. Traffic continues through the migration endpoint. When the data sync stops, the migration returns to Ready to sync. | Wait for Ready to sync. | 

How long the prepare step takes depends on the size of your source, because ElastiCache provisions migration infrastructure to match it. While the migration state reads `preparing`, the step is still running, so wait for `ready-to-sync`. After you start the data sync, the migration stays in `initiating-sync` until replication begins.

ElastiCache spends most of the `cutting-over` state tearing down the migration infrastructure. With Manual cutover, the state starts when you complete the migration, and ElastiCache first waits for a fully synced window to switch your traffic to your target. With Auto-cutover, the state stays `syncing` until ElastiCache finds that window. After the switch, your traffic is on your target for the rest of the state.

### Migration events
<a name="migration-to-serverless-events"></a>

ElastiCache publishes an event at each phase transition. The transitions are the following:
+ Prepare succeeded or failed
+ Start succeeded or failed
+ Cutover started
+ Complete succeeded or failed
+ Stop succeeded or failed

If a migration succeeds, the events read as follows, where `my-cache` is the name of your target cache:
+ **Prepare succeeded** – `Successfully prepared serverless cache {{my-cache}} for migration.`
+ **Start succeeded** – `Successfully started data sync for serverless cache {{my-cache}}.`
+ **Cutover started** – `Cutover initiated for serverless cache {{my-cache}}. Waiting for a suitable window to finalize the migration.`
+ **Complete succeeded** – `Successfully completed the migration for serverless cache {{my-cache}}.`
+ **Stop succeeded** – `Successfully stopped data sync for serverless cache {{my-cache}}.`
+ **Force complete succeeded** – `Successfully completed the migration for serverless cache {{my-cache}} with Force.`

If a migration step fails, the event names the step and gives the reason:
+ **Prepare failed** – `Failed to prepare migration for serverless cache {{my-cache}}. {{reason}}`
+ **Start failed** – `Failed to start data sync for serverless cache {{my-cache}}. {{reason}}`
+ **Complete failed** – `Failed to complete the migration for serverless cache {{my-cache}}. {{reason}}`
+ **Stop failed** – `Failed to stop the migration for serverless cache {{my-cache}}. {{reason}}`
+ **Migration error** – `Migration error for serverless cache {{my-cache}}. {{reason}}`

For example, a `preparing` status on a target that contains data would report `Failed to prepare migration for serverless cache {{my-cache}}. The serverless cache must have no keys before migration can begin.`

## Checking status and events using the AWS CLI
<a name="migration-to-serverless-monitoring-cli"></a>

**To check the migration status (AWS CLI)**
+ Enter the following AWS CLI command to check the migration status, where `{{my-cache}}` is the name of the target cache:

  ```bash
  aws elasticache describe-serverless-caches \
      --serverless-cache-name {{my-cache}} \
      --query "ServerlessCaches[0].[Status,Migration.Status]" \
      --output text
  ```

  The command returns the cache status and the migration status.


<table>
<thead>
  <tr><th>Cache status</th><th>Migration status</th><th>What it means</th></tr>
</thead>
<tbody>
  <tr><td><code>migrating</code></td><td><code>preparing</code></td><td>The prepare step is running.</td></tr>
  <tr><td><code>migrating</code></td><td><code>ready-to-sync</code></td><td>The prepare step succeeded.</td></tr>
  <tr><td><code>migrating</code></td><td><code>syncing</code></td><td>The data sync is running.</td></tr>
  <tr><td><code>available</code></td><td><code>None</code></td><td>The migration ended. It completed, it was force completed, or the prepare step failed, so read the events.</td></tr>
</tbody>
</table>


  The response also returns the migration endpoint address and port, along with a `CutoverMode` field. `CutoverMode` reports whether you opted in to automatic cutover when you started the data sync. It does not indicate that a cutover is in progress.

**To list the migration events (AWS CLI)**
+ Enter the following AWS CLI command to list the events, where `{{my-cache}}` is the name of the target cache and `{{120}}` is the number of minutes of events to return:

  ```bash
  aws elasticache describe-events \
      --source-type serverless-cache \
      --source-identifier {{my-cache}} \
      --duration {{120}}
  ```

## Monitoring progress using the console
<a name="migration-to-serverless-monitoring-console"></a>

The primary action button on the migration details page changes its label with the state. It reads **Start migration** until the data sync begins, and **Complete migration** afterward, in the same position.

The **Migrations** page shows migrations that are in progress, and shows the current state only. It shows no warning, no error badge, and no failure state. When a step fails, the state moves backward to the previous state, and a failed prepare step removes the migration from the page. These two changes are the only failure signals on this page. A stop that you request also moves the state backward.

You read a migration's events on the target cache's **Events** tab, or on the **Events** page in the console navigation. The **Events** tab filter offers a fixed set of predefined groups, with no migration-specific filter. To find the reason a step failed, open the cache details page for your target cache and read the events on its **Events** tab.

The console reads the migration state from `DescribeServerlessCaches`, which returns the `Migration` object on your target cache. It uses `DescribeEvents` to refresh the **Monitor** tab. The console can lag the underlying state.

There are no metrics specific to migration. You watch the target cache with the standard ElastiCache Serverless metrics. The migration details page in the console has a **Monitor** tab. The **Monitor** tab shows nine of the target cache's existing metrics:
+ `BytesUsedForCache`
+ `CurrItems`
+ `NewConnections`
+ `NetworkBytesIn`
+ `NetworkBytesOut`
+ `GetTypeCmds`
+ `SetTypeCmds`
+ `Evictions`
+ `CurrConnections`

The tab opens with an information banner, "Track your migration progress". It reads "These metrics show activity on your target cache. Use them to confirm your data is arriving during the migration and to verify traffic after cutover."

The **Monitor** tab shows no progress percentage and no progress bar. Migration progress can move backward.

Before the data sync starts, the tab shows an empty state.

**Console labeling**  
On the migration details page, the **Migration endpoint** field shows the migration endpoint address, and **Copy migration endpoint** copies it. The console hides the field while the migration status is `preparing`, and shows it in every later state.

**Note**  
Before you start the migration, the **Cutover method** field on the migration details page shows the API default, which can render as **Manual (default)**. It does not reflect a choice you have made. You choose the mode in the **Start migration** dialog box, where the control is labeled **Cutover mode**, with the values **Manual cutover** and **Auto-cutover**.

**Note**  
On the Valkey caches page, the **Status** column shows **Migrating** for a cache that is the target of a migration. This is a cache status, not a migration state.

## Confirming replication on your source
<a name="migration-to-serverless-confirm-replication"></a>

To confirm that replication is running, run `INFO replication` on each primary of your source. The migration appears there as a connected replica with `state=online` and a `lag` value. For more information, see [Metrics and events for Valkey and Redis OSS serverless caches](serverless-metrics-events-redis.md).

## How you know a migration is complete
<a name="migration-to-serverless-complete-check"></a>

You do not have to stay on the migration details page. The same status banner appears on the target cache's details page. With automatic cutover, the console takes you to the cache details page when the migration completes.

The console reports the migration outcome as follows:
+ On success, the cache details page shows a banner that names the completion time and points you to that cache's **Events** tab. On failure, the same surface shows a failure banner that carries the event detail.
+ A success banner and a failure banner can both be present at once.
+ A banner stays until you dismiss it, and it does not come back once dismissed. The console shows outcome banners for migrations from the past 7 days.
+ A completed migration no longer appears on the **Migrations** page.