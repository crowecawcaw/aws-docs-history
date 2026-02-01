Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Setting up Multi-AZ for a data warehouse

restored from a snapshot

To create a new Multi-AZ cluster by restoring it from a snapshot, complete the
following procedure.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**,
   **Snapshots**, then choose the snapshot to
   use.
3. Choose **Restore snapshot**, **Restore to a
   provisioned cluster**.
4. Enter properties for your cluster. For general information about
   creating clusters, see [Creating a cluster](create-cluster.md "create-cluster.md").
5. Choose one of the RA3 node types from the **Node
   type** drop-down list. The AZ configuration option becomes
   available only when you chose an RA3 node type.
6. Under **AZ configuration**, choose
   **Multi-AZ**.
7. Under **Number of nodes per AZ**, enter at least two
   nodes for your cluster.
8. You have the option to load sample data or bring your own data:
   - In **Sample data**, choose **Load
     sample data** to load the sample dataset into your
     Amazon Redshift cluster. Amazon Redshift loads the sample dataset Tickit into
     the default dev database and public schema. Amazon Redshift
     automatically loads the sample dataset into your Amazon Redshift
     cluster. You can start using the query editor v2 to query
     data.
   - To bring your own data to your Amazon Redshift cluster, follow
     the steps in [Load
     data from Amazon S3 to Amazon Redshift](../gsg/rs-gsg-create-sample-db.md "../gsg/rs-gsg-create-sample-db.md").

9. Scroll down to **Additional configurations**, expand
   **Network and security**, and make sure that you
   either accept the default **Cluster subnet group** or
   choose another one. If you choose another cluster subnet group, make
   sure that there are 3 Availability Zones in the subnet group you
   selected.
10. Under **Additional configurations**, expand
    **Database configurations**.
11. Under **Database encryption**, to use a custom
    KMS key other than the default AWS-owned key, click
    **Customize encryption settings**. This option is
    deselected by default.
12. Under **Choose an KMS key**, you can either choose
    an AWS Key Management Service key or enter an ARN. Or, you can click **Create an
    AWS Key Management Service key** in the AWS Key Management Service console. For more
    information about creating KMS keys, see [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
    _AWS Key Management Service Developer Guide_.
13. Click **Restore cluster from snapshot**. When the
    cluster restoration succeeds, you can view the details in the cluster
    details page.

- From the AWS CLI, use the `restore-from-cluster-snapshot`
  command as follows.

```
aws redshift restore-from-cluster-snapshot
--region eu-west-1
--multi-az
--snapshot-identifier test-snap1
--cluster-identifier test-saz-11
--endpoint-url https://redshift.eu-west-1.amazonaws.com/
```
