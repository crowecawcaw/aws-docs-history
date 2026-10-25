

# Cutover modes for online migration to ElastiCache Serverless
<a name="migration-to-serverless-cutover"></a>

Cutover is the point at which your migration endpoint stops serving from your source cache and starts serving from your ElastiCache Serverless cache. Your application does not change its connection. The endpoint stays the same.

You choose how the cutover is triggered. Manual cutover is the default.

## The Start migration dialog box
<a name="w2aac20c13c39b7"></a>

You start the data sync from the Start migration dialog box in the console. It presents the following:
+ The Cutover mode control, with the values Manual cutover and Auto-cutover. With manual cutover, you call `CompleteMigration` when you are ready. With automatic cutover, ElastiCache completes the cutover for you at the next fully synced window.
+ An option to clear data from the target cache. Use it when you start the data sync again after you stopped it or after an earlier start failed. Without it, the data sync fails if your target contains data. For more information, see [Prerequisites for online migration to ElastiCache Serverless](migration-to-serverless-prerequisites.md).
+ A reminder to point your application at the migration endpoint, with a button that copies it.

To start the data sync with the AWS CLI, run the following command:

```
aws elasticache start-migration \
    --serverless-cache-name {{my-cache}} \
    --auto-cutover
```

Where:
+ `my-cache` is the name of your ElastiCache Serverless cache.
+ `--auto-cutover` sets automatic cutover. Omit it for manual cutover, which is the default.
+ `--clear-target-cache-data` clears data from your target cache before the data sync starts. Add it when you start the data sync again after you stopped it or after an earlier start failed. Clearing the target cannot be undone.

## Before you cut over
<a name="w2aac20c13c39b9"></a>

There is no way to poll migration health on demand. Prepare the migration close to the cutover window you have planned. Watch the cache's events between starting the data sync and completing the migration. If the migration is unhealthy when you call `CompleteMigration`, the call is rejected immediately. The events carry the reason.

## Manual cutover
<a name="w2aac20c13c39c11"></a>

You decide when to complete the migration. ElastiCache keeps replicating and reports the migration as `syncing` until you act. This gives you time to validate your target cache before you cut over.

When you are ready, complete the migration:

```
aws elasticache complete-migration \
    --serverless-cache-name {{my-cache}}
```

Where:
+ `my-cache` is the name of your ElastiCache Serverless cache.

ElastiCache then waits for the next fully synced window before it cuts over. Heavy write traffic on your source can increase replication lag and delay that window. Reduce writes to help the cutover happen sooner. There can be an interval between your request and the cutover.

**If a fully synced window is not found, the cutover does not complete.** ElastiCache reports an event on the cache that a suitable window to finalize the migration was not found. Reduce the write traffic on your source and try again. If your target is already in sync with your source, you can instead complete the migration with force.

## Automatic cutover
<a name="w2aac20c13c39c13"></a>

ElastiCache completes the cutover for you at the next fully synced window. Opt in when you start the data sync. This is the simpler path when you do not need a validation window before switching.

If ElastiCache cannot find a fully synced window, automatic cutover times out. ElastiCache reports an event on the cache that automatic cutover timed out. You then call `CompleteMigration` yourself after reducing write traffic. If your target is already in sync with your source, you can call `CompleteMigration` with force instead.

Manual and automatic cutover produce the same result. Choose based on how much control you want over the timing.

The following table compares the two cutover modes.


| Behavior | Manual cutover | Automatic cutover | 
| --- | --- | --- | 
| How it starts | You call CompleteMigration | ElastiCache starts it at the next fully synced window, if you opted in when you started the data sync | 
| Trigger the cutover yourself | Yes, call CompleteMigration | Only with force. While the automatic cutover is pending, CompleteMigration without force is rejected. | 
| Default | Yes | No, you opt in | 
| If a fully synced window is not found | The cutover does not complete, and ElastiCache reports that a suitable window to finalize the migration was not found | Automatic cutover times out, and ElastiCache reports that it timed out | 
| Validation window before cutover | You choose when to switch, so you can validate your target first | None, the cutover happens at the next fully synced window | 

## Stopping the data sync
<a name="w2aac20c13c39c15"></a>

You can stop the data sync while it is in progress:

```
aws elasticache stop-migration \
    --serverless-cache-name {{my-cache}}
```

Where:
+ `my-cache` is the name of your ElastiCache Serverless cache.

ElastiCache stops replicating and your application continues to be served by your source cache. Nothing about your source cache changes. The migration returns to `ready-to-sync`. If you chose automatic cutover, stopping also cancels the pending cutover, unless the cutover has already begun.

Stopping has a second use besides abandoning a migration. You might stop the data sync to free capacity on your source cache for a period, then start it again when it suits you.

**Whether you can start the data sync again depends on why it stopped.**
+ If you stopped it yourself and the migration has reported no errors, the migration stays open and you can start the data sync again.

  Data that was already synced stays on your target after you stop. To start the data sync again, choose **Authorize automatic clearing of the target cache if it contains data** (`ClearTargetCacheData`). Otherwise, the data sync fails because the target is not empty.
+ If the migration has reported an error, `StopMigration` still succeeds and reports that the data sync stopped, but a later `StartMigration` is rejected. This applies even to a problem you have since fixed, such as a network path that dropped or a credential that changed. The only way to end the migration is then to complete it with force.

The confirmation you get from `StopMigration` is the same either way. It does not tell you whether a later start will be accepted.

Check the migration's events before you plan to start the data sync again.

**Once cutover has begun, stopping no longer applies.** While the migration is in `cutting-over`, `StopMigration` fails with `InvalidServerlessCacheStateFault`. With automatic cutover, ElastiCache accepts a `StopMigration` call made during `syncing`. If cutover begins before the stop takes effect, the cutover continues, and the completion event reports that the stop was ignored.

## What your application sees at cutover
<a name="w2aac20c13c39c17"></a>

Cutover is not instantaneous, and it is applied per shard. Your application can see the following while cutover runs:


| What your application sees | Why | What to do | 
| --- | --- | --- | 
| Reads and writes keep flowing, and tail latency rises briefly. | Traffic flows continuously throughout cutover. Tail latency rises for roughly 2 to 10 seconds, depending on your workload. | Nothing. Your application keeps being served. | 
| A connection with a write in flight is closed. | If your client sent a write and did not get a definitive reply, ElastiCache closes the connection instead of replaying the write. | Treat it the same way you would treat a connection that died with an in-flight write outside a migration. | 
| Blocking commands and pub/sub subscribers lose their connection. | Blocking commands such as BLPOP and pub/sub subscribers lose their connection at cutover. They must reconnect, and subscribers must re-subscribe. | Reconnect, and re-subscribe your subscribers. | 
| Clients connected directly to your source are disconnected. | ElastiCache ends your source's client connections as part of the cutover. This disconnects anything you have attached straight to your source, such as a monitoring agent or a second application. | Nothing for your application, which keeps using the migration endpoint. | 

## Force completing a migration
<a name="w2aac20c13c39c19"></a>

Force completing skips the pre-cutover health check and the cluster-wide convergence check. Each shard still runs the full cutover process and tries to cut over with consistent data.

**Incomplete data after force complete.** Force can leave your target with incomplete data. Your target can be left with incomplete or inconsistent data only if it was not in sync with your source when you forced. There is no automated rollback. After cutover, your ElastiCache Serverless cache is authoritative. To return to your source cache, you must move your application traffic back to it yourself.

Use force complete in two cases:
+ Abandoning a migration.
+ Ending a migration that has reported an error, because force complete is then the only way to end it.

Do not use force complete to finish a healthy migration that is still syncing.

To force complete a migration, run the following command:

```
aws elasticache complete-migration \
    --serverless-cache-name {{my-cache}} \
    --force
```

Where:
+ `my-cache` is the name of your ElastiCache Serverless cache.

## After cutover
<a name="w2aac20c13c39c21"></a>

Your migration endpoint now serves from your ElastiCache Serverless cache, and your application needs no change. Your source cache is no longer part of the path. You can decommission it on your own schedule after you confirm that your application is healthy on the target.

Completing the migration ends the migration charges. Your ElastiCache Serverless cache continues to bill at the standard data storage and ECPU rates, as it would at any other time.

## Related topics
<a name="w2aac20c13c39c23"></a>
+ [Online migration to ElastiCache Serverless](migration-to-serverless.md)
+ [Prerequisites for online migration to ElastiCache Serverless](migration-to-serverless-prerequisites.md)
+ [Source authentication for online migration to ElastiCache Serverless](migration-to-serverless-auth.md)
+ [Migrate your data to ElastiCache Serverless](migration-to-serverless-procedure.md)