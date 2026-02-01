Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating a manual snapshot

You can create a manual snapshot of a cluster from the snapshots list as follows. Or,
you can take a snapshot of a cluster in the cluster configuration pane. For more
information, see [Amazon Redshift snapshots and backups](working-with-snapshots.md "working-with-snapshots.md").

###### Note

No-backup tables aren't supported for RA3 provisioned clusters and Amazon Redshift Serverless workgroups.
A table marked as no-backup in an RA3 cluster or serverless workgroup is treated as a permanent table that will
always be backed up while taking a snapshot, and always restored when restoring from a snapshot. To avoid snapshot costs for no-backup tables,
truncate them before taking a snapshot.

###### To create a manual snapshot

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**,
   **Snapshots**, then choose **Create snapshot**.
   The snapshot page to create a manual snapshot is displayed.
3. Enter the properties of the snapshot definition, then choose **Create
   snapshot**. It might take some time for the snapshot to be available.
