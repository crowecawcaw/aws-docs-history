

# Canceling and troubleshooting online migrations to ElastiCache Serverless

## Stopping the data sync
<a name="migration-to-serverless-stop"></a>

When you stop the data sync, ElastiCache stops replicating, and your application continues to be served by your source cache. Nothing about your source cache changes. The migration returns to `ready-to-sync`. If you chose automatic cutover, stopping also cancels the pending cutover, unless the cutover has already begun.

**Note**  
Billing does not stop when you stop the data sync. `StopMigration` leaves the migration infrastructure provisioned. `CompleteMigration` is the call that ends the migration and its charges.

Stopping has a second use besides abandoning a migration. You might stop the data sync to free capacity on your source cache for a period and then start it again when it suits you.

Whether you can start the data sync again depends on why it stopped:
+ If you stopped it yourself, and if the migration has reported no errors, the migration stays open. You can start the data sync again.

  Data that was already synced stays on your target after you stop. To start the data sync again, choose **Authorize automatic clearing of the target cache if it contains data** (`ClearTargetCacheData`). Otherwise, the data sync fails because the target is not empty.
+ If the migration has reported an error, `StopMigration` still succeeds and reports that the data sync stopped, but a later `StartMigration` is rejected. This applies even to a problem you have since fixed, such as a network path that dropped or a credential that changed. The only way to end the migration is force completion.

The confirmation you get from `StopMigration` is the same either way. It does not tell you whether a later start will be accepted.

Check the migration's events before you plan to start the data sync again.

**Note**  
After cutover has begun, you can no longer stop the data sync. While the migration is in `cutting-over`, `StopMigration` fails with `InvalidServerlessCacheStateFault`. With automatic cutover, ElastiCache accepts a `StopMigration` call made during `syncing`. If cutover begins before the stop takes effect, the cutover continues, and the completion event reports that the stop was ignored.

**To stop the data sync (console)**
+ On the migration details page, choose **Stop**. **Stop** is available only while **Current state** is **Data sync in progress**. While the data sync stops, the **Current state** is **Stopping**.

**To stop the data sync (AWS CLI)**

1. Enter the following AWS CLI command, where `{{my-cache}}` is the name of your ElastiCache Serverless cache:

   ```bash
   aws elasticache stop-migration \
       --serverless-cache-name {{my-cache}}
   ```

1. Check the migration state according to the instructions in [Checking status and events using the AWS CLI](migration-to-serverless-monitoring.md#migration-to-serverless-monitoring-cli).

## Force completing the migration
<a name="migration-to-serverless-force-complete"></a>

Force completing skips the pre-cutover health check and the cluster-wide convergence check. Each shard still runs the full cutover process and tries to cut over with consistent data. Use force complete in two cases:
+ To abandon a migration.
+ To end a migration that has reported an error.

Do not use force complete to finish a healthy migration that is still syncing.

**Warning**  
Force completion can leave your target with incomplete or inconsistent data, but only if it was not in sync with your source when you forced. There is no automated rollback. After cutover, your ElastiCache Serverless cache is authoritative. To return to your source cache, move your application traffic back to it yourself before you force complete.

While the migration is `ready-to-sync`, `CompleteMigration` requires force. If you force complete before the data sync starts, your target has no data. To abandon a migration, first move your application traffic back to your source, and then force complete.

**To force complete the migration (console)**
+ On the migration details page, choose **Force complete**. It is available when **Current state** is **Ready to sync** or **Data sync in progress**.

  The console shows "Force complete triggered for {{name}}." For more information, see [Cutting over](migration-to-serverless-procedure.md#migration-to-serverless-complete).

**To force complete the migration (AWS CLI)**

1. Enter the following AWS CLI command to force complete the migration, where `{{my-cache}}` is the name of your ElastiCache Serverless cache.

   ```bash
   aws elasticache complete-migration \
       --serverless-cache-name {{my-cache}} \
       --force
   ```

1. Check the migration state according to the instructions in [Checking status and events using the AWS CLI](migration-to-serverless-monitoring.md#migration-to-serverless-monitoring-cli).

## Errors returned by the migration operations
<a name="migration-to-serverless-troubleshooting-errors"></a>

`StartMigration` and `CompleteMigration` are rejected immediately when the migration is not healthy. The error tells you to check the cache's events for the reason.

The migration operations raise the following exceptions:
+ `MigrationHealthFault` – The migration is not healthy. Set `Force` to true on `CompleteMigration` to bypass the check.
+ `ServerlessCacheAlreadyUnderMigrationFault` – The cache is already the target of a migration.
+ `ServerlessCacheNotUnderMigrationFault` – The cache has no migration to act on.
+ `InvalidServerlessCacheStateFault` – The cache or the migration is not in a state that allows the operation.
+ `InvalidParameterValue` – The request is not valid for the target cache or the migration, for example when the target has a public endpoint or uses the IPv6 or dual-stack network type, or when you call `CompleteMigration` without `Force` while the migration is `ready-to-sync` or an automatic cutover is pending.

## Troubleshooting a failed prepare step
<a name="migration-to-serverless-troubleshooting-prepare-step"></a>

When the prepare step fails, the target cache's **Events** tab shows the reason. The following table lists the reasons and what to check.


| Reason in the event | What to check | 
| --- | --- | 
| "The serverless cache must have no keys before migration can begin." | Your target contains data. Run FLUSHALL on the target before you prepare the migration, or choose an empty cache. | 
| "The serverless cache is not yet ready for migration. Please try again later." | Wait, and then prepare the migration again. | 
| "Unable to connect to source cluster." | This reason covers several causes. Check each of the following:+  The source security group allows inbound TCP on the source port from the target cache's security group or subnets. <br />+  Each source node binds to its private IP address and reports a reachable address in its cluster topology. <br />+  The source address is a private IP address or a host name that resolves through public DNS. <br />+  Protected mode is off on a source that has no password. <br />+  The migration user has every permission in [Permissions for the migration user](migration-to-serverless-auth.md#migration-to-serverless-auth-permissions).  | 
| An access denied message for the secret | The secret's resource policy grants secretsmanager:GetSecretValue to elasticache.amazonaws.com, the key policy grants kms:Decrypt, neither statement has an aws:SourceAccount or aws:SourceArn condition, and your IAM identity has secretsmanager:GetSecretValue, kms:Decrypt and ec2:DescribeSubnets. | 
| A subnet message that names Availability Zones | Create a new target cache with a subnet in each Availability Zone that the message names, and prepare the migration again. | 
| A failure after you provide TLS settings | Provide the PEM-encoded CA certificates with verify-ca. The event might not name the certificate authority. | 

## Troubleshooting a key name that exceeds 4 KiB
<a name="migration-to-serverless-troubleshooting-key-name-size"></a>

An oversized key name fails the migration during the initial data load. Recover as follows:

1. Point your application back at your source's own endpoint.

1. End the migration with force complete, which switches the migration endpoint to your target.

1. Flush the target.

1. Remove or rename every key on your source whose name exceeds 4 KiB.

1. Prepare a new migration.