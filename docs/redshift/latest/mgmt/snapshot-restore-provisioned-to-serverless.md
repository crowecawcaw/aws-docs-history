Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Restoring a serverless

namespace from a snapshot

Restoring a serverless namespace from a snapshot replaces all of the namespace’s
databases with databases in the snapshot. For more information about serverless snapshots,
see [Snapshots and
recovery points](serverless-snapshots-recovery-points.md "serverless-snapshots-recovery-points.md"). Amazon Redshift automatically converts tables with interleaved keys
into compound keys when you restore a provisioned cluster snapshot to an Amazon Redshift Serverless
namespace. For more information about sort keys, see [Working with sort keys](../dg/t_Sorting_data.md "../dg/t_Sorting_data.md").

To restore a snapshot from your provisioned cluster to your serverless
namespace.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**,
   **Snapshots**, then choose the snapshot to use.
3. Choose **Restore from snapshot**, **Restore to serverless
   namespace**.
4. Choose the namespace you want to restore to.
5. Confirm you want to restore from your snapshot. Choose
   **restore**. This action replaces all the databases in
   serverless namespace with the data from your provisioned cluster.
