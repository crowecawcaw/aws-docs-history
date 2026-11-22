

# Migrating your data to ElastiCache Serverless

This page walks you through an online migration from a self-managed Valkey or Redis OSS source on Amazon EC2 to an ElastiCache Serverless for Valkey cache. You can use the ElastiCache console or the AWS CLI. You create the migration, redirect your application to the migration endpoint, start the data sync, and complete the cutover.

## Before you start
<a name="migration-to-serverless-before-you-start"></a>

Confirm the following:
+ Before you begin, confirm that your source cache and your target cache meet the migration requirements. For more information, see [Prerequisites and limitations for online migration to ElastiCache Serverless](migration-to-serverless-prerequisites.md).
+ If your source requires authentication or TLS, set that up first. For more information, see [Source authentication for online migration to ElastiCache Serverless](migration-to-serverless-auth.md).
+ Before you migrate, test your workload on an ElastiCache Serverless cache to see how it scales and how many ElastiCache Processing Units (ECPUs) it consumes. For more information, see [Scaling ElastiCache Serverless clusters](Scaling-serverless.md).
+ An ElastiCache Serverless for Valkey cache that is available and empty, with the IPv4 network type and no public endpoint.
+ Confirm that you have a self-managed Valkey or Redis OSS source on Amazon EC2 that meets the source requirements.
+ Confirm that you have a AWS Secrets Manager secret that holds your source credentials, if your source requires authentication.
+ Confirm that your application's users are set up on your target cache, with the same user names, passwords, and permissions as on your source, if your source requires authentication. For more information about setting up target users, see [Setting up your application's users on your target](migration-to-serverless-auth.md#migration-to-serverless-auth-target-users).
+ Confirm that you have your source TLS configuration, if your source requires TLS.
+ Confirm that you have at least three subnets in different Availability Zones for your target cache, each with free IP addresses.
+ Confirm that you have AWS CLI version 2.38.3 or later, if you use the AWS CLI.

## Creating the migration
<a name="migration-to-serverless-create"></a>

You can create a migration with the ElastiCache console or the AWS CLI.

**To create the migration (console)**

1. Open the **Create migration** page in one of the following ways:
   + In the navigation pane, choose **Migrations**, choose **Create migration**, and then choose **Migrate to serverless**.
   + On the Valkey caches page, select your target cache, or open its cache details page, and then choose **Migrate data**. This action preselects the target cache.

1. Under **Source details**, for **Server address**, enter your source address. You can also choose an Amazon EC2 instance from the suggestions, which fills in the address. For the source address, enter the private IP address of a source node, or a host name that resolves through public DNS. A host name that resolves only in your VPC's private DNS fails the prepare step.

1. For **Port**, enter your source port.

1. For **Authentication method**, choose one of the following options.
   + **Use an existing secret** – Choose your secret under **Existing secret**.
   + **Create and use a new secret** – Enter a user name if your engine version uses one, enter a password, and choose a customer managed AWS KMS key. ElastiCache creates the secret. The user name and password must meet the requirements in [Source authentication for online migration to ElastiCache Serverless](migration-to-serverless-auth.md).
   + **None** – Your source does not require authentication.

1. For **TLS encryption**, choose **Verify CA** or **None**.

   If you choose **Verify CA**, under **Certificate authority** choose **Public CA** or **Private CA**, and provide the PEM-encoded CA certificates that issued your source's server certificate. Provide them for public and private authorities alike. For more information about why, see [Source authentication for online migration to ElastiCache Serverless](migration-to-serverless-auth.md).
**Warning**  
Your target cache must be empty when you create the migration. If it contains any keys, the prepare step fails and the target's **Events** tab shows "The serverless cache must have no keys before migration can begin." To empty the target, run `FLUSHALL` on it before you create the migration. `FLUSHALL` removes every key in the cache. You can have ElastiCache clear the target for you only when you start the data sync.

1. Under **Target details**, for **Choose target cache**, choose your cache. Only compatible caches are listed.

1. Choose **Create**. The migration details page opens. Its title is **Migration:** followed by your cache name.

   The migration details page shows the state and controls for your migration. The **Migration overview** shows **Target cache**, **Current state**, **Migration endpoint**, and **Cutover method**. The page has a **Monitor** tab and an **Events** tab. It also has **Stop**, **Force complete**, and **Start migration** buttons. While ElastiCache prepares the migration, **Current state** reads **Preparing migration**, and the **Migration endpoint** field is hidden. How long the prepare step takes depends on the size of your source. While **Current state** reads **Preparing migration**, the step is still running.

1. Wait until the **Current state** is **Ready to sync**. The **Migration endpoint** field shows the address.

**To create the migration (AWS CLI)**

1. Enter the following AWS CLI command to prepare the migration, where `{{my-cache}}` is the name of your target cache and where `{{192.0.2.10}}` and `{{6379}}` are the private address and port of one node in your source:

   ```bash
   aws elasticache prepare-migration \
       --serverless-cache-name {{my-cache}} \
       --customer-node-endpoint-list "Address='{{192.0.2.10}}',Port={{6379}}"
   ```

   For the authentication and TLS options, see [Source authentication for online migration to ElastiCache Serverless](migration-to-serverless-auth.md).

1. Wait until the migration state is `ready-to-sync`. For information about checking the migration state, see [Checking status and events using the AWS CLI](migration-to-serverless-monitoring.md#migration-to-serverless-monitoring-cli).

## Redirecting your application
<a name="migration-to-serverless-redirect"></a>

Starting the data sync first does not affect the data on your target. Your traffic is routed to your source until cutover.

**Warning**  
Point your application at the migration endpoint only when the migration state is **Ready to sync**. While the migration is preparing, the endpoint does not accept connections. Before you prepare a migration, and after a prepare step that fails, the endpoint serves your target cache, which is empty.

**Note**  
A client that still connects straight to your source after cutover writes to a cache that no longer replicates to your target.

**To redirect the application (console)**

1. Choose **Copy migration endpoint**. This copies the endpoint address.

1. Update your application to connect to the migration endpoint with TLS, and allow your application in your target cache's security group. For more information, see [Client configuration](migration-to-serverless-prerequisites.md#migration-to-serverless-client-config).

1. Read a key that exists on your source through the migration endpoint, and confirm that it returns the value from your source.

**To redirect the application (AWS CLI)**

1. Get the migration endpoint and point your application at it. Connect with TLS. Before you move all of your traffic, read a key that exists on your source through the migration endpoint. When the read returns the value from your source, the endpoint is routing to your source.

   ```bash
   aws elasticache describe-serverless-caches \
       --serverless-cache-name {{my-cache}} \
       --query "ServerlessCaches[0].Migration.MigrationEndpoint"
   ```

1. To check the migration state, see [Checking status and events using the AWS CLI](migration-to-serverless-monitoring.md#migration-to-serverless-monitoring-cli).

## Starting the data sync
<a name="migration-to-serverless-start"></a>

When you start the data sync, ElastiCache begins replicating data from your source to your target cache. Your application continues to be served throughout. For more information about cutover modes, see [Cutting over](#migration-to-serverless-complete).

**Important**  
If your migration is using Auto-cutover, redirect your application before you start the data sync, because ElastiCache cuts over at the next fully synced window.

**To start the data sync (console)**

1. On the migration details page, choose **Start migration**.

1. In the **Start migration** dialog box, for **Cutover mode**, choose **Manual cutover** or **Auto-cutover**. For more information, see [Cutting over](#migration-to-serverless-complete).

1. Under **Target cache data**, to clear a target that contains data, select **Authorize automatic clearing of the target cache if it contains data**. Your target contains data if you are starting the data sync again after you stopped it. It can also contain data if an earlier start failed. If your target contains data and you do not select this option, the data sync fails because the target is not empty, and the migration returns to **Ready to sync**.
**Warning**  
Clearing the target cannot be undone.

1. Choose **Start migration**. The **Current state** changes to **Initializing sync** and then to **Data sync in progress**. The migration stays in **Initializing sync** until replication begins.

**To start the data sync (AWS CLI)**

1. Start the data sync. To have ElastiCache cut over for you, add `--auto-cutover`, and redirect your application before you run this command.

   ```bash
   aws elasticache start-migration \
       --serverless-cache-name {{my-cache}}
   ```

1. Check the migration state according to the instructions in [Checking status and events using the AWS CLI](migration-to-serverless-monitoring.md#migration-to-serverless-monitoring-cli).

## Cutting over
<a name="migration-to-serverless-complete"></a>

*Cutover* is the point at which your migration endpoint stops serving from your source cache and starts serving from your ElastiCache Serverless cache. Your application does not change its connection, and the endpoint stays the same. You choose how the cutover is triggered, and manual cutover is the default.

There is no way to poll migration health on demand. Prepare the migration close to the cutover window you have planned, and watch the cache's events between starting the data sync and completing the migration. If the migration is unhealthy when you call `CompleteMigration`, the call is rejected immediately, and the events carry the reason.

During cutover, **Current state** is **Cutover in progress**, and **Stop** and **Force complete** are disabled. For most of the **Cutover in progress** state, ElastiCache is removing the migration infrastructure, and your traffic is already on your target cache.

### Cutover modes
<a name="migration-to-serverless-complete-modes"></a>

How the cutover completes depends on the cutover mode you chose:
+ **Manual cutover** – You decide when to complete the migration. ElastiCache keeps replicating and reports the migration as `syncing` until you act, which lets you choose when to switch, for example during a period of low write traffic. **Complete migration** is available only while the data sync is in progress.
+ **Auto-cutover** – ElastiCache completes the cutover for you at the next fully synced window. Opt in when you start the data sync. **Complete migration** is disabled in this mode. The console opens the cache details page when the migration finishes, and shows a **Migration completed successfully** banner until you dismiss it. The **Events** tab lists the migration events.

With either mode, ElastiCache waits for the next fully synced window before it cuts over. Heavy write traffic on your source can increase replication lag and delay that window. Reduce writes to help the cutover happen sooner. There can be an interval between your request and the cutover.

**If a fully synced window is not found, the cutover does not complete.** With manual cutover, ElastiCache reports an event that a suitable window to finalize the migration was not found. With automatic cutover, the cutover times out and ElastiCache reports that it timed out. In either case, reduce the write traffic on your source and try again. If your target is already in sync with your source, you can instead complete the migration with force.

Manual and automatic cutover produce the same result. Choose based on how much control you want over the timing. The following table compares the two cutover modes.


| Behavior | Manual cutover | Automatic cutover | 
| --- | --- | --- | 
| How it starts | You call CompleteMigration | ElastiCache starts it at the next fully synced window, if you opted in when you started the data sync | 
| Trigger the cutover yourself | Yes, call CompleteMigration | Only with force. While the automatic cutover is pending, CompleteMigration without force is rejected. | 
| Default | Yes | No, you opt in | 
| If a fully synced window is not found | The cutover does not complete, and ElastiCache reports that a suitable window to finalize the migration was not found | Automatic cutover times out, and ElastiCache reports that it timed out | 
| Validation window before cutover | You choose when to switch, so you can validate your target first | None, the cutover happens at the next fully synced window | 

**To manually cut over (console)**

1. When the **Current state** is **Data sync in progress** and you are ready, choose **Complete migration**. The console shows "Complete migration triggered for {{name}}."

1. After the migration completes, verify your data and clean up. For the steps, see [Validating and cleaning up](#migration-to-serverless-after-cutover).

**To manually cut over (AWS CLI)**

1. Enter the following AWS CLI command for manual cutover:

   ```bash
   aws elasticache complete-migration \
       --serverless-cache-name {{my-cache}}
   ```

1. Check the migration state according to the instructions in [Checking status and events using the AWS CLI](migration-to-serverless-monitoring.md#migration-to-serverless-monitoring-cli).

1. After the migration completes, verify your data and clean up. For the steps, see [Validating and cleaning up](#migration-to-serverless-after-cutover).

### What your application sees at cutover
<a name="migration-to-serverless-app-at-cutover"></a>

Cutover is not instantaneous, and it is applied per shard. Your application can see the following while cutover runs.


| What your application sees | Why | What to do | 
| --- | --- | --- | 
| Reads and writes keep flowing, and tail latency rises briefly. | Traffic flows continuously throughout cutover. Tail latency rises for roughly 2 to 10 seconds, depending on your workload. | Nothing. Your application keeps being served. | 
| A connection with a write in flight is closed. | If your client sent a write and did not get a definitive reply, ElastiCache closes the connection instead of replaying the write. | Treat it the same way you would treat a connection that died with an in-flight write outside a migration. | 
| Blocking commands and pub/sub subscribers lose their connection. | Blocking commands such as BLPOP and pub/sub subscribers lose their connection at cutover. They must reconnect, and subscribers must re-subscribe. | Reconnect, and re-subscribe your subscribers. | 
| Clients connected directly to your source are disconnected. | ElastiCache ends your source's client connections as part of the cutover. This disconnects anything you have attached straight to your source, such as a monitoring agent or a second application. | Nothing for your application, which keeps using the migration endpoint. | 

## Validating and cleaning up
<a name="migration-to-serverless-after-cutover"></a>

Your migration endpoint now serves from your ElastiCache Serverless cache, and your application needs no change. Your source cache is no longer part of the path. You can decommission it on your own schedule after you confirm that your application is healthy on the target.

Before you decommission your source, confirm that your data arrived on your target.

**To verify your data**

1. Wait a few minutes after the completion event before you compare. Right after completion, `CurrItems` and `DBSIZE` can briefly read higher than the final count.

1. Compare the `CurrItems` metric of your target with the number of keys on your source.

1. Read a few keys that your application wrote during the migration.

**Note**  
Your target can hold more keys than your source, because after cutover your application writes only to your target.

**To clean up**

1. Remove the inbound rule on your source security group.

1. Remove any test client you started.

1. Remove the secret and the customer managed key if nothing else uses them.

Completing the migration ends the migration charges. Your ElastiCache Serverless cache continues to bill at the standard data storage and ECPU rates, as it would at any other time.

## Additional resources
<a name="migration-to-serverless-resources"></a>

For the parameters of each command, see [prepare-migration](https://docs.aws.amazon.com/cli/latest/reference/elasticache/prepare-migration.html), [start-migration](https://docs.aws.amazon.com/cli/latest/reference/elasticache/start-migration.html), [stop-migration](https://docs.aws.amazon.com/cli/latest/reference/elasticache/stop-migration.html), and [complete-migration](https://docs.aws.amazon.com/cli/latest/reference/elasticache/complete-migration.html) in the *AWS CLI Command Reference*.

For more information about migrating with the AWS CLI, see the AWS CLI examples on [Source authentication for online migration to ElastiCache Serverless](migration-to-serverless-auth.md) and [Cutting over](#migration-to-serverless-complete).

For the API operations, see [PrepareMigration](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_PrepareMigration.html), [StartMigration](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_StartMigration.html), [CompleteMigration](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CompleteMigration.html), and [StopMigration](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_StopMigration.html) in the *Amazon ElastiCache API Reference*.