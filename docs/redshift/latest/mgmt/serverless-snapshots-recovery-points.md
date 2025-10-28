Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Snapshots and recovery points

A backup in Amazon Redshift Serverless is a point-in-time representation of the objects and data in your
namespace. There are two types of backups: snapshots that are manually created and recovery
points that Amazon Redshift Serverless automatically creates for you.

Amazon Redshift Serverless automatically creates recovery points every 30 minutes or after every 5 GB of
data changes per node, whichever happens first. For larger datasets (more than 5 GB × number
of nodes), the minimal interval between recovery points is 15 minutes. All recovery points
are kept for 24 hours.

###### Note

You cannot create your own snapshot schedule to control when recovery points are
created.

Amazon Redshift Serverless creates snapshots in Redshift Managed Storage (RMS). For more information, see
[Compute capacity for Amazon Redshift Serverless](serverless-capacity.md "serverless-capacity.md").

###### Note

No-backup tables aren't supported for RA3 provisioned clusters and Amazon Redshift Serverless workgroups.
A table marked as no-backup in an RA3 cluster or serverless workgroup is treated as a permanent table that will
always be backed up while taking a snapshot, and always restored when restoring from a snapshot. To avoid snapshot costs for no-backup tables,
truncate them before taking a snapshot.

If you find that you want to retrieve the data in a snapshot or a recovery point, you can
restore a snapshot to a serverless namespace or to a provisioned cluster. There are three
scenarios in which you can restore snapshots:

- Restore a serverless snapshot to a serverless namespace.
- Restore a serverless snapshot to a provisioned cluster.
- Restore a provisioned cluster snapshot to a serverless namespace.
  When you restore a serverless snapshot to a provisioned cluster, you must choose the node
  type to use, such as RA3, and the number of nodes, letting you control settings at the
  cluster or node level.

To restore a provisioned cluster snapshot to a serverless namespace, start from the
Redshift provisioned console, choose the snapshot to restore, then choose **Restore
from snapshot**, **Restore to serverless namespace**. Amazon Redshift
converts tables with interleaved keys into compound sort keys when you restore a provisioned
cluster snapshot to a serverless namespace. For more information about sort keys, see [Working with sort
keys](../dg/t_Sorting_data.md "../dg/t_Sorting_data.md").

If you want to add additional context, you can tag snapshots and recovery points with
key-value pairs that provide metadata and information to snapshots and recovery points. For
more information about tagging resources, see [Tagging resources
overview](serverless-tagging-resources.md "serverless-tagging-resources.md").

Finally, you can also share snapshots with other AWS accounts, which lets them access
data within the snapshot and run queries.

## AWS Backup integration

You can also create and restore snapshots using AWS Backup, a fully managed service that
helps you centralize and automate data protection across AWS services, in the cloud,
and on premises. For more information, see [AWS Backup integration with Amazon Redshift](managing-aws-backup.md "managing-aws-backup.md").
For information on AWS Backup, see
[What is AWS Backup?](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md") in the _AWS Backup Developer Guide_.
