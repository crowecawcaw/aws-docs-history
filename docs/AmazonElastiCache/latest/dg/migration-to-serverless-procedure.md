

# Migrate your data to ElastiCache Serverless
<a name="migration-to-serverless-procedure"></a>

This page walks you through an online migration from a self-managed Valkey or Redis OSS source on Amazon EC2 to an ElastiCache Serverless for Valkey cache. You can use the ElastiCache console or the AWS CLI. You create the migration, redirect your application to the migration endpoint, start the data sync, and complete the cutover.

## Before you start
<a name="w2aac20c13c39b5"></a>

Before you begin, confirm that your source cache and your target cache meet the migration requirements. For more information, see [Prerequisites for online migration to ElastiCache Serverless](migration-to-serverless-prerequisites.md). If your source requires authentication or TLS, set that up first. For more information, see [Source authentication for online migration to ElastiCache Serverless](migration-to-serverless-auth.md).

Before you migrate, test your workload on an ElastiCache Serverless cache to see how it scales and how many ElastiCache Processing Units (ECPUs) it consumes. For more information, see [Scaling ElastiCache Serverless clusters](Scaling-serverless.md).

Confirm that you have the following:
+ An ElastiCache Serverless for Valkey cache that is available and empty, with the IPv4 network type and no public endpoint.
+ A self-managed Valkey or Redis OSS source on Amazon EC2 that meets the source requirements.
+ A Secrets Manager secret that holds your source credentials, if your source requires authentication.
+ Your application's users set up on your target cache, with the same user names, passwords, and permissions as on your source, if your source requires authentication. For more information about setting up target users, see [Setting up your application's users on your target](migration-to-serverless-auth.md#migration-to-serverless-auth-target-users).
+ Your source TLS configuration, if your source requires TLS.
+ At least three subnets in different Availability Zones for your target cache, each with free IP addresses.
+ AWS CLI version 2.38.3 or later, if you use the AWS CLI.

## Create the migration
<a name="migration-to-serverless-create"></a>

You can create a migration with the ElastiCache console or the AWS CLI. You can open the **Create migration** page in two ways.
+ In the navigation pane, choose **Migrations**, choose **Create migration**, and then choose **Migrate to serverless**.
+ On the Valkey caches page, select your target cache, or open its cache details page, and then choose **Migrate data**. This action preselects the target cache.

On the **Create migration** page, complete the following steps.

1. Under **Source details**, for **Server address**, enter your source address. You can also choose an Amazon EC2 instance from the suggestions, which fills in the address. For the source address, enter the private IP address of a source node, or a host name that resolves through public DNS. A host name that resolves only in your VPC's private DNS fails the prepare step.

1. For **Port**, enter your source port.

1. For **Authentication method**, choose one of the following options.  
**Use an existing secret**  
Choose your secret under **Existing secret**.  
**Create and use a new secret**  
Enter a user name if your engine version uses one, enter a password, and choose a customer managed AWS KMS key. ElastiCache creates the secret. The user name and password must meet the requirements in [Source authentication for online migration to ElastiCache Serverless](migration-to-serverless-auth.md).  
**None**  
Your source does not require authentication.

1. For **TLS encryption**, choose **Verify CA** or **None**.

   If you choose **Verify CA**, under **Certificate authority** choose **Public CA** or **Private CA**, and provide the PEM-encoded CA certificates that issued your source's server certificate. Provide them for public and private authorities alike. For more information about why, see [Source authentication for online migration to ElastiCache Serverless](migration-to-serverless-auth.md).

1. 
**Important**  
Your target cache must be empty when you create the migration. If it contains any keys, the prepare step fails and the target's Events tab shows "The serverless cache must have no keys before migration can begin." To empty the target, run `FLUSHALL` on it before you create the migration. `FLUSHALL` removes every key in the cache. You can have ElastiCache clear the target for you only when you start the data sync.

   Under **Target details**, for **Choose target cache**, choose your cache. Only compatible caches are listed.

1. Choose **Create**.

The console opens the migration details page. Its title reads **Migration:** followed by your cache name.

**To do this with the AWS CLI**
+ Prepare the migration. For the authentication and TLS options, see [Source authentication for online migration to ElastiCache Serverless](migration-to-serverless-auth.md).

  ```
  aws elasticache prepare-migration \
      --serverless-cache-name {{my-cache}} \
      --customer-node-endpoint-list "Address='{{10.0.0.10}}',Port={{6379}}"
  ```

  Where:
  + `my-cache` is the name of your target cache.
  + `10.0.0.10` and `6379` are the private address and port of one node in your source.

To check the migration state, see [Migration states](migration-to-serverless.md#migration-to-serverless-states).

## The migration details page
<a name="w2aac20c13c39b9"></a>

The migration details page shows the state and controls for your migration. The **Migration overview** shows **Target cache**, **Current state**, **Migration endpoint**, and **Cutover method**. The page has a **Monitor** tab and an **Events** tab. It also has **Stop**, **Force complete**, and **Start migration** buttons.

While ElastiCache prepares the migration, **Current state** reads **Preparing migration**, and the **Migration endpoint** field is hidden.

How long the prepare step takes depends on the size of your source. While **Current state** reads **Preparing migration**, the step is still running.

## Redirect your application
<a name="migration-to-serverless-redirect"></a>

**Warning**  
Point your application at the migration endpoint only when Current state reads Ready to sync. While the migration is preparing, the endpoint does not accept connections. Before you prepare a migration, and after a prepare step that fails, the endpoint serves your target cache, which is empty.

When **Current state** reads **Ready to sync**, the **Migration endpoint** field shows the address.

1. To copy the address, choose **Copy migration endpoint**.

1. Update your application to connect to the migration endpoint with TLS, and allow your application in your target cache's security group. For more information, see [Client configuration](migration-to-serverless-prerequisites.md#migration-to-serverless-client-config).

1. Read a key that exists on your source through the migration endpoint, and confirm that it returns the value from your source.

Starting the data sync first does not affect the data on your target. Your traffic is routed to your source until cutover.

**Important**  
If you use Auto-cutover, redirect your application before you start the data sync, because ElastiCache cuts over at the next fully synced window.

**Note**  
A client that still connects straight to your source after cutover writes to a cache that no longer replicates to your target.

**To do this with the AWS CLI**
+ Get the migration endpoint and point your application at it. Connect with TLS. Before you move all of your traffic, read a key that exists on your source through the migration endpoint. When the read returns the value from your source, the endpoint is routing to your source.

  ```
  aws elasticache describe-serverless-caches \
      --serverless-cache-name {{my-cache}} \
      --query "ServerlessCaches[0].Migration.MigrationEndpoint"
  ```

To check the migration state, see [Migration states](migration-to-serverless.md#migration-to-serverless-states).

## Start the data sync
<a name="migration-to-serverless-start"></a>

When you start the data sync, ElastiCache begins replicating data from your source to your target cache. Your application continues to be served throughout. For more information about cutover modes, see [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

1. On the migration details page, choose **Start migration**.

1. In the **Start migration** dialog box, for **Cutover mode**, choose **Manual cutover** or **Auto-cutover**. For more information, see [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

1. 
**Warning**  
Clearing the target cannot be undone.

   Under **Target cache data**, to clear a target that contains data, select **Authorize automatic clearing of the target cache if it contains data**. Your target contains data if you are starting the data sync again after you stopped it. It can also contain data if an earlier start failed. If your target contains data and you do not select this option, the data sync fails because the target is not empty, and the migration returns to **Ready to sync**.

1. Choose **Start migration**.

**Current state** moves to **Initializing sync** and then to **Data sync in progress**. The migration stays in **Initializing sync** until replication begins.

**To do this with the AWS CLI**
+ Start the data sync. To have ElastiCache cut over for you, add `--auto-cutover`, and redirect your application before you run this command.

  ```
  aws elasticache start-migration \
      --serverless-cache-name {{my-cache}}
  ```

To check the migration state, see [Migration states](migration-to-serverless.md#migration-to-serverless-states).

## Complete the cutover
<a name="migration-to-serverless-complete"></a>

How the cutover completes depends on the cutover mode you chose.

**Manual cutover**  
When **Current state** reads **Data sync in progress** and you are ready, choose **Complete migration**. The console shows "Complete migration triggered for {{name}}." **Complete migration** is available only while the data sync is in progress.

**Auto-cutover**  
ElastiCache cuts over at the next fully synced window. **Complete migration** is disabled in this mode.

During cutover, **Current state** reads **Cutover in progress**. **Stop** and **Force complete** are disabled during cutover.

For most of the **Cutover in progress** state, ElastiCache is removing the migration infrastructure, and your traffic is already on your target cache.

With Auto-cutover, the console opens the cache details page when the migration finishes. This page shows a **Migration completed successfully** banner until you dismiss it. The **Events** tab lists the migration events.

**To do this with the AWS CLI**
+ Complete the migration. Skip this step if you chose automatic cutover.

  ```
  aws elasticache complete-migration \
      --serverless-cache-name {{my-cache}}
  ```

To check the migration state, see [Migration states](migration-to-serverless.md#migration-to-serverless-states).

After the migration completes, verify your data and clean up. For the steps, see [After cutover](migration-to-serverless-cutover.md#migration-to-serverless-after-cutover).

## If you need to stop
<a name="migration-to-serverless-stop"></a>

To stop the data sync, choose **Stop** on the migration details page. **Stop** is available only while **Current state** reads **Data sync in progress**. While the data sync stops, **Current state** reads **Stopping**. For more information about what stopping does, see [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

**Force complete**  
Force complete ends the migration even if your target is not in sync with your source. Your migration endpoint then serves from your target, which can have incomplete data. To return to your source, move your application traffic back to it yourself before you force complete.

To end a migration that has reported an error, use **Force complete**. It is available when **Current state** reads **Ready to sync** or **Data sync in progress**. The console shows "Force complete triggered for {{name}}." For more information, see [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

**To do this with the AWS CLI**

1. To stop the data sync, run the following command.

   ```
   aws elasticache stop-migration \
       --serverless-cache-name {{my-cache}}
   ```

   Where:
   + `my-cache` is the name of your ElastiCache Serverless cache.

1. To end a migration that has reported an error instead, force complete it.

   ```
   aws elasticache complete-migration \
       --serverless-cache-name {{my-cache}} \
       --force
   ```

   Where:
   + `my-cache` is the name of your ElastiCache Serverless cache.

To check the migration state, see [Migration states](migration-to-serverless.md#migration-to-serverless-states).

For the parameters of each command, see [prepare-migration](https://docs.aws.amazon.com/cli/latest/reference/elasticache/prepare-migration.html), [start-migration](https://docs.aws.amazon.com/cli/latest/reference/elasticache/start-migration.html), [stop-migration](https://docs.aws.amazon.com/cli/latest/reference/elasticache/stop-migration.html), and [complete-migration](https://docs.aws.amazon.com/cli/latest/reference/elasticache/complete-migration.html) in the *AWS CLI Command Reference*.

For more information about migrating with the AWS CLI, see the AWS CLI examples on [Source authentication for online migration to ElastiCache Serverless](migration-to-serverless-auth.md) and [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

For the API operations, see [PrepareMigration](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_PrepareMigration.html), [StartMigration](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_StartMigration.html), [CompleteMigration](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CompleteMigration.html), and [StopMigration](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_StopMigration.html) in the *Amazon ElastiCache API Reference*.