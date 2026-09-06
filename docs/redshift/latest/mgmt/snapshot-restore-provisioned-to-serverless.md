

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Restoring a serverless namespace from a snapshot
<a name="snapshot-restore-provisioned-to-serverless"></a>

 Restoring a serverless namespace from a snapshot replaces all of the namespace’s databases with databases in the snapshot. For more information about serverless snapshots, see [Snapshots and recovery points](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshots-recovery-points.html). Amazon Redshift automatically converts tables with interleaved keys into compound keys when you restore a provisioned cluster snapshot to an Amazon Redshift Serverless namespace. For more information about sort keys, see [Working with sort keys](https://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data.html). 

To restore a snapshot from your provisioned cluster to your serverless namespace.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. On the navigation menu, choose **Clusters**, **Snapshots**, then choose the snapshot to use.

1. Choose **Restore from snapshot**, **Restore to serverless namespace**.

1. Choose the namespace you want to restore to.

1. Confirm you want to restore from your snapshot. Choose **restore**. This action replaces all the databases in serverless namespace with the data from your provisioned cluster.