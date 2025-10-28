Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Restoring a snapshot

###### Note

No-backup tables aren't supported for RA3 provisioned clusters and Amazon Redshift Serverless workgroups.
A table marked as no-backup in an RA3 cluster or serverless workgroup is treated as a permanent table that will
always be backed up while taking a snapshot, and always restored when restoring from a snapshot. To avoid snapshot costs for no-backup tables,
truncate them before taking a snapshot.

Restoring a snapshot to a serverless namespace replaces the current database with the
database in the snapshot.

Restoring a snapshot to a serverless namespace is completed in two phases. The first
phase completes in a few minutes, restores the data to your namespace, and makes it
available for queries. The second phase of restoration is where your database is tuned,
which can cause minor performance issues. This second phase can last from a few hours to
several days, and in some cases, a couple of weeks. The amount of time depends on the
size of the data, but performance progressively improves as the database gets tuned. At
the end of this phase, your serverless namespace is fully tuned, and you can submit
queries without performance issues.

###### To restore a snapshot to a serverless namespace

1. On the Amazon Redshift Serverless console, choose **Data backup**.
2. Choose the snapshot to restore. You can only restore one snapshot at a
   time.
3. Choose **Actions**, **Restore to serverless
   namespace**.
4. Choose an available namespace to restore to. You can only restore to
   namespaces whose statuses are Available.
5. Choose **Restore**.

###### To restore a snapshot to a provisioned cluster

1. On the Amazon Redshift Serverless console, choose **Data backup**.
2. Choose a snapshot to restore.
3. Choose **Action**, **Restore to provisioned
   cluster**.
4. Enter a cluster identifier.
5. Choose a **Node type**. The number of nodes depends on the
   node type.
6. Follow the instructions on the page on the console page to enter the
   properties for **Cluster configuration**. See [Creating a cluster](create-cluster.md "create-cluster.md") for more information.
   For more information about snapshots on provisioned clusters, see [Amazon Redshift snapshots and backups](working-with-snapshots.md "working-with-snapshots.md").
