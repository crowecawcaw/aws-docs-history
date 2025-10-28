Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Shutting down and deleting a

cluster

You can shut down your cluster if you want to stop it from running and incurring
charges. When you shut it down, you can optionally create a final snapshot. If you
create a final snapshot, Amazon Redshift will create a manual snapshot of your cluster before
shutting it down. If you plan to provision a new cluster with the same data and
configuration as the one you are deleting, you need a manual snapshot. By using a manual
snapshot, you can restore the snapshot later and resume using the cluster.

If you no longer need your cluster and its data, you can shut it down without creating
a final snapshot. In this case, the cluster and data are deleted permanently.

Regardless of whether you shut down your cluster with a final manual snapshot, all
automated snapshots associated with the cluster will be deleted after the cluster is
shut down. Any manual snapshots associated with the cluster are retained. Any manual
snapshots that are retained, including the optional final snapshot, are charged at the
Amazon Simple Storage Service storage rate if you have no other clusters running when you shut down the
cluster, or if you exceed the available free storage that is provided for your running
Amazon Redshift clusters. For more information about snapshot storage charges, see the [Amazon Redshift pricing page](https://aws.amazon.com/redshift/pricing/ "https://aws.amazon.com/redshift/pricing/").

Deleting a cluster also deletes any associated AWS Secrets Manager secrets.

###### To delete a cluster

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**.
3. Choose the cluster to delete.
4. For **Actions**, choose **Delete**. The
   **Delete cluster** page appears.
5. Choose **Delete cluster**.

###### Note

When you delete a cluster and choose to create a final snapshot, Amazon Redshift will stop
the delete request if a restore operation is in progress on the cluster. If this
occurs, you can delete the cluster without a final snapshot, or you can delete it
with a final snapshot after the restore completes.
