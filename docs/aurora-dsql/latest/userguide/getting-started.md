# Getting started with Aurora DSQL

Amazon Aurora DSQL is a serverless, fully managed, distributed relational database optimized for transactional
workloads. In the following sections, you'll learn how to create single-Region and multi-Region
Aurora DSQL clusters, connect to them, and create and load a sample schema. You will access clusters
with the AWS Console and optionally interact with your database using other PostgreSQL clients.
By the end, you'll have a working Aurora DSQL cluster set up that is ready to use for test or
production workloads.

###### Topics

- [Prerequisites](#getting-started-prereqs "#getting-started-prereqs")
- [Step 1: Create an Aurora DSQL single-Region
  cluster](#getting-started-create-cluster "#getting-started-create-cluster")
- [Step 2: Connect to your Aurora DSQL cluster](#connect-dsql-cluster "#connect-dsql-cluster")
- [Step 3: Run sample SQL commands in Aurora DSQL](#getting-started-sql "#getting-started-sql")
- [Step 4 (Optional): Create a multi-Region
  cluster](#getting-started-multi-region "#getting-started-multi-region")
- [Troubleshooting](#getting-started-sql-troubleshooting "#getting-started-sql-troubleshooting")

## Prerequisites

Before you can begin using Aurora DSQL, make sure you meet the following prerequisites:

- Your IAM identity must have permission to [sign in to the
  console](../../../signin/latest/userguide/console-sign-in-tutorials.md "../../../signin/latest/userguide/console-sign-in-tutorials.md").
- Your IAM identity must meet the following criteria:
  - Access to perform any action on any resource in your AWS account
  - `AmazonAuroraDSQLConsoleFullAccess` AWS managed policy is [attached](../../../aws-managed-policy/latest/reference/AmazonAuroraDSQLConsoleFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonAuroraDSQLConsoleFullAccess.md").

## Step 1: Create an Aurora DSQL single-Region

cluster

The basic unit of Aurora DSQL is the cluster, which is where you store your data. In this task,
you create a cluster in a single AWS Region.

###### To create a single-Region cluster in Aurora DSQL

1. Sign in to the AWS Management Console and open the Aurora DSQL console at [https://console.aws.amazon.com/dsql](https://console.aws.amazon.com/dsql "https://console.aws.amazon.com/dsql").
2. Choose **Create cluster** and then
   **Single-Region**.
3. (Optional) change the value of the default **Name** tag.
4. (Optional) Add additional **Tags** for this cluster.
5. (Optional) In **Cluster settings**, select any of the following
   options:
   - Select **Customize encryption settings (advanced)** to choose or
     create an AWS KMS key.
   - Select **Enable deletion protection** to prevent a delete operation
     from removing your cluster. By default, deletion protection is selected.
   - Select **Resource-based policy (advanced)** to specify access control
     policies for this cluster.

6. Choose **Create cluster**.
7. The console returns you to the **Clusters** page. A notification banner
   appears indicating that the cluster is being created. Select the **Cluster
   ID** to open the cluster details view.

## Step 2: Connect to your Aurora DSQL cluster

Aurora DSQL supports multiple ways to connect to your cluster, including the DSQL Query Editor,
AWS CloudShell, the local psql client, and other PostgreSQL-compatible tools. In this step, you connect
using the [Aurora DSQL Query
Editor](getting-started-query-editor.md "getting-started-query-editor.md"), which provides a quick way to begin interacting with your new cluster.

###### To connect using the Query Editor

1. In the Aurora DSQL Console ([https://console.aws.amazon.com/dsql](https://console.aws.amazon.com/dsql "https://console.aws.amazon.com/dsql")), open the
   **Clusters** page and confirm that your cluster creation has completed and
   its status is Active.
2. Select your cluster from the list, or choose the **Cluster ID** to open
   the Cluster details page.
3. Choose **Connect with Query editor**.
4. Choose Connect as **admin** for the cluster that was just created.
   - Optionally you can connect with a custom role, see
     [Using database roles and IAM authentication](using-database-and-iam-roles.md "using-database-and-iam-roles.md").

## Step 3: Run sample SQL commands in Aurora DSQL

Test your Aurora DSQL cluster by running SQL statements. After opening the cluster in the Query
Editor, select and run each sample query step by step.

###### Run sample SQL commands in Aurora DSQL

1. Create a schema named `test`.

```
CREATE SCHEMA IF NOT EXISTS test;
```

2. Create a hello_world table that uses an automatically generated UUID as the primary
   key.

```
CREATE TABLE IF NOT EXISTS test.hello_world (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    message VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

3. Insert a sample row.

```
INSERT INTO test.hello_world (message)
VALUES ('Hello, World!!');
```

4. Read the inserted values.

```
SELECT * FROM test.hello_world;
```

5. Optionally clean up

```
DROP TABLE test.hello_world;
DROP SCHEMA test;
```

## Step 4 (Optional): Create a multi-Region

cluster

When you create a multi-Region cluster, you specify the following Regions:

**Remote Region**

This is the Region in which you create a second cluster. You create a second cluster in
this Region and peer it to your initial cluster. Aurora DSQL replicates all writes on the initial
cluster to the remote cluster. You can read and write on any cluster.

**Witness Region**

This Region receives all data that is written to the multi-Region cluster. However,
witness Regions don't host client endpoints and don't provide user data access. A limited
window of the encrypted transaction log is maintained in witness Regions. This log facilitates
recovery and supports transactional quorum if a Region becomes unavailable.

Use the following procedure to create an initial cluster, create a second cluster in a
different Region, and then peer the two clusters to create a multi-Region cluster. It also
demonstrates cross-Region write replication and consistent reads from both Regional
endpoints.

###### To create a multi-Region cluster

1. Sign in to the [Aurora DSQL
   console](https://console.aws.amazon.com/dsql "https://console.aws.amazon.com/dsql").
2. In the navigation pane, choose **Clusters**.
3. Choose **Create cluster** and then
   **Multi-Region**.
4. (Optional) change the value of the default **Name** tag.
5. (Optional) Add additional **Tags** for this cluster.
6. In **Multi-Region settings**, choose the following options for your
   initial cluster:
   - In **Witness Region**, choose a Region. Currently, only US-based
     Regions are supported for witness Regions in multi-Region clusters.
   - (Optional) In **Remote Region cluster ARN**, enter an ARN for an
     existing cluster in another Region. If no cluster exists to serve as the second cluster in
     your multi-Region cluster, complete setup after you create the initial cluster.

7. (Optional) In **Cluster settings**, select any of the following options
   for your initial cluster:
   - Select **Customize encryption settings (advanced)** to choose or
     create an AWS KMS key.
   - Select **Enable deletion protection** to prevent a delete operation
     from removing your cluster. By default, deletion protection is selected.
   - Select **Resource-based policy (advanced)** to specify access control
     policies for this cluster.

8. Choose **Create cluster** to create your initial cluster. If you didn't
   enter an ARN in the previous step, the console shows the **Cluster setup
   pending** notification.
9. In the **Cluster setup pending** notification, choose **Complete
   multi-Region cluster setup**. This action initiates creation of a second cluster in
   another Region.
10. Choose one of the following options for your second cluster:
    - **Add remote Region cluster ARN** – Choose this option if a
      cluster exists, and you want it to be the second cluster in your multi-Region cluster.
    - **Create cluster in another Region** – Choose this option to
      create a second cluster. In **Remote Region**, choose the Region for this
      second cluster.

11. Choose **Create cluster in
    `your-second-region`**, where
    `your-second-region` is the location of your second cluster. The
    console opens in your second Region.
12. (Optional) Choose cluster settings for your second cluster. For example, you can choose an
    AWS KMS key.
13. Choose **Create cluster** to create your second cluster.
14. Choose **Peer in `initial-cluster-region`**,
    where is `initial-cluster-region` is the Region that hosts the first
    cluster that you created.
15. When prompted, choose **Confirm**. This step completes the creation of
    your multi-Region cluster.

###### To connect to your second cluster

1. Open the Aurora DSQL console and choose the Region for your second cluster.
2. Choose **Clusters**.
3. Select the row for the second cluster in your multi-Region cluster.
4. Choose **Connect with Query editor**.
5. Choose **Connect as admin**.
6. Create a sample schema and table, and insert data by following the steps in [Step 3: Run sample SQL commands in Aurora DSQL](#getting-started-sql "#getting-started-sql").

###### To query data in the second cluster from the Region hosting your initial cluster

1. In the Aurora DSQL console, choose the Region for your initial cluster.
2. Choose **Clusters**.
3. Select the row for the second cluster in your multi-Region cluster.
4. Choose **Connect with Query editor**.
5. Choose **Connect as admin**.
6. Query the data that you inserted into the second cluster.

###### Example

```
SELECT * FROM test.hello_world;
```

## Troubleshooting

See the [Troubleshooting](troubleshooting.md "troubleshooting.md") section of the Aurora DSQL documentation.
