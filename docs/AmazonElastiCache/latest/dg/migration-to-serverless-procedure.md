

# Migrate your data to ElastiCache Serverless
<a name="migration-to-serverless-procedure"></a>

This page walks you through an online migration from a self-managed Valkey or Redis OSS source on Amazon EC2 to an ElastiCache Serverless for Valkey cache. You use the ElastiCache console from start to finish. You create the migration, redirect your application to the migration endpoint, start the data sync, and complete the cutover.

## Before you start
<a name="w2aac20c13c37b5"></a>

Before you begin, confirm that your source cache and your target cache meet the migration requirements. For more information, see [Prerequisites for online migration to ElastiCache Serverless](migration-to-serverless-prerequisites.md). If your source requires authentication or TLS, set that up first. For more information, see [Source authentication for online migration to ElastiCache Serverless](migration-to-serverless-auth.md).

Confirm that you have the following:
+ An ElastiCache Serverless for Valkey cache that is available and empty, with the IPv4 network type and no public endpoint.
+ A self-managed Valkey or Redis OSS source on Amazon EC2 that meets the source requirements.
+ A Secrets Manager secret that holds your source credentials, if your source requires authentication.
+ Your source TLS configuration, if your source requires TLS.

## Create the migration
<a name="w2aac20c13c37b7"></a>

You create a migration with the ElastiCache console. You can open the **Create migration** page in two ways.
+ In the navigation pane, choose **Migrations**, choose **Create migration**, and then choose **Migrate to serverless**.
+ On the Valkey caches page, select your target cache, or open its cache details page, and then choose **Migrate data**. This action preselects the target cache.

On the **Create migration** page, complete the following steps.

1. Under **Source details**, for **Server address**, enter your source address. You can also choose an Amazon EC2 instance from the suggestions, which fills in the address.

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

1. Under **Target details**, for **Choose target cache**, choose your cache. Only compatible caches are listed.

1. Choose **Create**.

The console opens the migration details page. Its title reads **Migration:** followed by your cache name.

## The migration details page
<a name="w2aac20c13c37b9"></a>

The migration details page shows the state and controls for your migration. The **Migration overview** shows **Target cache**, **Current state**, **Migration endpoint**, and **Cutover method**. The page has a **Monitor** tab and an **Events** tab. It also has **Stop**, **Force complete**, and **Start migration** buttons.

While ElastiCache prepares the migration, **Current state** reads **Preparing migration**, and the **Migration endpoint** field is hidden. The banner reads "Step 1 of 3: Preparing migration" and "This may take a few minutes. Once complete, choose Start migration to begin the data sync. You can remain on this page or return later to continue."

## Redirect your application
<a name="w2aac20c13c37c11"></a>

When **Current state** reads **Ready to sync**, the banner reads "Migration is ready to sync" and "Your migration endpoint is active and traffic is routed to your source. Update your application to point to the migration endpoint, then choose Start migration when ready." The **Migration endpoint** field now shows the address. Update your application to connect to the migration endpoint. To copy the address, choose **Copy migration endpoint**. Your traffic is routed to your source until cutover. The console reminds you to do this before you start the data sync, because ElastiCache cannot detect whether your application has moved. Starting the data sync first does not affect the data on your target.

## Start the data sync
<a name="w2aac20c13c37c13"></a>

When you start the data sync, ElastiCache begins replicating data from your source to your target cache. Your application continues to be served throughout. For more information about cutover modes, see [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

1. On the migration details page, choose **Start migration**.

1. In the **Start migration** dialog box, for **Cutover mode**, choose **Manual cutover** or **Auto-cutover**. For more information, see [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

1. 
**Warning**  
Clearing the target cannot be undone.

   Under **Target cache data**, to clear a target that contains data, select **Authorize automatic clearing of the target cache if it contains data**. Your target contains data if you are starting the data sync again after you stopped it. It can also contain data if an earlier start failed. If your target contains data and you do not select this option, the data sync fails because the target is not empty, and the migration returns to **Ready to sync**.

1. Choose **Start migration**.

**Current state** moves to **Initializing sync** and then to **Data sync in progress**. While the data sync initializes, the banner reads "Step 2 of 3: Data sync is initiating". With Manual cutover it reads "Connecting to your source and initializing data sync. Once syncing begins, you can choose Complete migration and cutover will occur on the next fully synced window." With Auto-cutover it reads "Connecting to your source and initializing data sync. Once syncing begins, cutover will be performed automatically on the next fully synced window." When the data sync is running, the banner reads "Step 2 of 3: Data sync is in progress". With Manual cutover it reads "Choose Complete migration and cutover will occur on the next fully synced window." With Auto-cutover it reads "We will perform auto-cutover for you on the next fully synced window." The **Monitor** tab shows a selected set of the target cache's metrics.

## Complete the cutover
<a name="w2aac20c13c37c15"></a>

How the cutover completes depends on the cutover mode you chose.

**Manual cutover**  
When **Current state** reads **Data sync in progress** and you are ready, choose **Complete migration**. The console shows "Complete migration triggered for {{name}}." **Complete migration** is available only while the data sync is in progress.

**Auto-cutover**  
ElastiCache cuts over at the next fully synced window. **Complete migration** is disabled in this mode.

During cutover, **Current state** reads **Cutover in progress** and the banner reads "Step 3 of 3: Cutover is in progress" and "Traffic is being switched from your source to the target cache. This might take a few minutes." **Stop** and **Force complete** are disabled during cutover.

With Auto-cutover, the console opens the cache details page when the migration finishes. This page shows a **Migration completed successfully** banner until you dismiss it. The **Events** tab lists the migration events.

## If you need to stop
<a name="w2aac20c13c37c17"></a>

To stop the data sync, choose **Stop** on the migration details page. **Stop** is available only while **Current state** reads **Data sync in progress**. While the data sync stops, **Current state** reads **Stopping** and the banner reads "Data sync is being stopped. Traffic continues through the migration endpoint. Once stopped, the migration will return to Ready to sync." For more information about what stopping does, see [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

**Force complete**  
Force complete ends the migration even if your target is not in sync with your source. Your migration endpoint then serves from your target, which can have incomplete data. To return to your source, you must move your application traffic back to it yourself.

To end a migration that has reported an error, use **Force complete**. It is available when **Current state** reads **Ready to sync** or **Data sync in progress**. The console shows "Force complete triggered for {{name}}." For more information, see [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

## Using the AWS CLI
<a name="w2aac20c13c37c19"></a>

For more information about migrating with the AWS CLI, see the AWS CLI examples on [Source authentication for online migration to ElastiCache Serverless](migration-to-serverless-auth.md) and [Cutover modes for online migration to ElastiCache Serverless](migration-to-serverless-cutover.md).

For the API operations, see [PrepareMigration](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_PrepareMigration.html), [StartMigration](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_StartMigration.html), [CompleteMigration](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CompleteMigration.html), and [StopMigration](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_StopMigration.html) in the *Amazon ElastiCache API Reference*.