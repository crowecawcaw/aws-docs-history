

# Getting started with Aurora DSQL

Amazon Aurora DSQL is a serverless, fully managed, distributed relational database optimized for transactional workloads. In the following sections, you'll learn how to create single-Region and multi-Region Aurora DSQL clusters, connect to them, and create and load a sample schema. You will access clusters with the AWS Console and optionally interact with your database using other PostgreSQL clients. By the end, you'll have a working Aurora DSQL cluster set up that is ready to use for test or production workloads.

**Topics**
+ [Prerequisites](#getting-started-prereqs)
+ [Step 1: Create an Aurora DSQL single-Region cluster](#getting-started-create-cluster)
+ [Step 2: Connect to your Aurora DSQL cluster](#connect-dsql-cluster)
+ [Step 3: Run sample SQL commands in Aurora DSQL](#getting-started-sql)
+ [Step 4 (Optional): Create a multi-Region cluster](#getting-started-multi-region)
+ [Troubleshooting](#getting-started-sql-troubleshooting)

## Prerequisites
<a name="getting-started-prereqs"></a>

Before you can begin using Aurora DSQL, make sure you meet the following prerequisites:
+ Your IAM identity must have permission to [sign in to the console](https://docs.aws.amazon.com/signin/latest/userguide/console-sign-in-tutorials.html).
+ Your IAM identity must meet the following criteria:
  + Access to perform any action on any resource in your AWS account
  + `AmazonAuroraDSQLConsoleFullAccess` AWS managed policy is [attached](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonAuroraDSQLConsoleFullAccess.html).

## Step 1: Create an Aurora DSQL single-Region cluster
<a name="getting-started-create-cluster"></a>

The basic unit of Aurora DSQL is the cluster, which is where you store your data. In this task, you create a cluster in a single AWS Region.

**To create a single-Region cluster in Aurora DSQL**

1. Sign in to the AWS Management Console and open the Aurora DSQL console at [https://console.aws.amazon.com/dsql](https://console.aws.amazon.com/dsql).

1. Choose **Create cluster**.

1. In **Cluster topology**, choose **Single Region**.

1. In **Cluster configuration**, choose one of the following:
   + **Quick create** to create the cluster with recommended settings. You can change some settings, such as **Tag: Name** and deletion protection, before you create the cluster.
   + **Advanced configuration** to control all settings, including encryption and resource-based policies.

1. (Optional) If you chose **Advanced configuration**, do any of the following:
   + In **Name and tags**, change the value of the default **Name** tag, or choose **Add additional tags**.
   + In **Cluster settings**, select **Customize encryption settings (advanced)** to choose or create an AWS KMS key. If you use a customer managed key, make sure that the key policy grants Aurora DSQL the required permissions. For more information, see [Key policy for a customer managed key](data-encryption.md#key-policy-customer-managed-key).
   + In **Cluster settings**, keep **Enable deletion protection** selected to prevent a delete operation from removing your cluster. The console selects it by default.
   + In **Cluster settings**, select **Add resource-based policy** to specify access control policies for this cluster.

1. Choose **Create cluster**. The console opens the details page for your new cluster.

## Step 2: Connect to your Aurora DSQL cluster
<a name="connect-dsql-cluster"></a>

Aurora DSQL supports multiple ways to connect to your cluster, including the DSQL Query Editor, AWS CloudShell, the local psql client, and other PostgreSQL-compatible tools. In this step, you connect using the [Aurora DSQL Query Editor](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/getting-started-query-editor.html), which provides a quick way to begin interacting with your new cluster.

**To connect using the Query Editor**

1. In the Aurora DSQL Console ([https://console.aws.amazon.com/dsql](https://console.aws.amazon.com/dsql)), open the **Clusters** page and confirm that your cluster creation has completed and its status is Active.

1. Select your cluster from the list, or choose the **Cluster ID** to open the Cluster details page.

1. Choose **Connect with Query editor**.

1. Choose Connect as **admin** for the cluster that was just created.
   + Optionally you can connect with a custom role, see [Using database roles and IAM authentication](using-database-and-iam-roles.md).

## Step 3: Run sample SQL commands in Aurora DSQL
<a name="getting-started-sql"></a>

Test your Aurora DSQL cluster by running SQL statements. After opening the cluster in the Query Editor, select and run each sample query step by step.

**Run sample SQL commands in Aurora DSQL**

1. Create a schema named `test`.

   ```
   CREATE SCHEMA IF NOT EXISTS test;
   ```

1. Create a hello\_world table that uses an automatically generated UUID as the primary key.

   ```
   CREATE TABLE IF NOT EXISTS test.hello_world (
       id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
       message VARCHAR(255) NOT NULL,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

1. Insert a sample row.

   ```
   INSERT INTO test.hello_world (message)
   VALUES ('Hello, World!!');
   ```

1. Read the inserted values.

   ```
   SELECT * FROM test.hello_world;
   ```

1. Optionally clean up.

   ```
   DROP TABLE test.hello_world;
   DROP SCHEMA test;
   ```

## Step 4 (Optional): Create a multi-Region cluster
<a name="getting-started-multi-region"></a>

A multi-Region cluster has two active peer Regions and one witness Region. When you create one, your current Region is the first peer Region, and you choose the second peer Region and the witness Region. You can choose these Regions from the Regions that support Aurora DSQL multi-Region clusters. All three Regions must be distinct. For more information about the supported Regions, see [Multi-Region cluster availability](what-is-aurora-dsql.html#aurora-dsql-multi-region-availability).

**Peer Region**  
This is the Region that hosts the second active cluster. Both peer clusters accept read and write operations and present a single logical database with strong data consistency. Aurora DSQL replicates writes between the two peer Regions.

**Witness Region**  
This Region stores encrypted transaction logs, does not store encryption keys, has no managed endpoints, and does not make data accessible to users. The witness log supports transactional quorum if a Region becomes unavailable.

Use the following procedure to create a multi-Region cluster. The console creates a cluster in each of the two Regions and peers them for you. The procedures after it show cross-Region write replication and consistent reads from both Regional endpoints.

**To create a multi-Region cluster**

1. Sign in to the [Aurora DSQL console](https://console.aws.amazon.com/dsql).

1. In the navigation pane, choose **Clusters**.

1. Choose **Create cluster**.

1. In **Cluster topology**, choose **2 active Regions \+ Witness**.

1. In **Cluster configuration**, choose one of the following:
   + **Quick create** to create the clusters with recommended settings. **Peer cluster 1** is in your current Region. To change the Region for **Peer cluster 2** or **Witness peer**, choose a Region in the **Region** row of the table.
   + **Advanced configuration** to control all settings for each Region. In **Regions**, choose the **Peer cluster 2 Region** and the **Witness Region**.

1. (Optional) If you chose **Advanced configuration**, change the settings for each Region in **Name and tags**, **Encryption key**, **Deletion protection**, and **Resource-based policy - optional**. If you use a customer managed key, make sure that the key policy grants Aurora DSQL the required permissions. For more information, see [Key policy for a customer managed key](data-encryption.md#key-policy-customer-managed-key).

1. Choose **Create cluster**. The console creates the cluster in your current Region and opens its details page. A notification shows the progress while the console creates the second cluster and peers the two clusters.

**To connect to your second cluster**

1. Open the Aurora DSQL console and choose the Region for your second cluster.

1. Choose **Clusters**.

1. Select the row for the second cluster in your multi-Region cluster.

1. Choose **Connect with Query editor**.

1. Choose **Connect as admin**.

1. Create a sample schema and table, and insert data by following the steps in [Step 3: Run sample SQL commands in Aurora DSQL](#getting-started-sql).

**To query data in the second cluster from the Region hosting your initial cluster**

1. In the Aurora DSQL console, choose the Region for your initial cluster.

1. Choose **Clusters**.

1. Select the row for the second cluster in your multi-Region cluster.

1. Choose **Connect with Query editor**.

1. Choose **Connect as admin**.

1. Query the data that you inserted into the second cluster.  
**Example**  

   ```bash,sh,zsh
   SELECT * FROM test.hello_world;
   ```

## Troubleshooting
<a name="getting-started-sql-troubleshooting"></a>

See the [Troubleshooting](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/troubleshooting.html) section of the Aurora DSQL documentation.