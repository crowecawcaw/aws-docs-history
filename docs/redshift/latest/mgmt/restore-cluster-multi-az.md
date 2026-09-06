

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Setting up Multi-AZ for a data warehouse restored from a snapshot
<a name="restore-cluster-multi-az"></a>

To create a new Multi-AZ cluster by restoring it from a snapshot, complete the following procedure.

## Using the console
<a name="maz-snapshot-console"></a>

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. On the navigation menu, choose **Clusters**, **Snapshots**, then choose the snapshot to use.

1. Choose **Restore snapshot**, **Restore to a provisioned cluster**.

1. Enter properties for your cluster. For general information about creating clusters, see [Creating a cluster](create-cluster.md).

1. Choose one of the RG or RA3 node types from the **Node type** drop-down list. The AZ configuration option becomes available only when you chose an RG or RA3 node type.

1. Under **AZ configuration**, choose **Multi-AZ**.

1. Under **Number of nodes per AZ**, enter at least two nodes for your cluster.

1. You have the option to load sample data or bring your own data:
   + In **Sample data**, choose **Load sample data** to load the sample dataset into your Amazon Redshift cluster. Amazon Redshift loads the sample dataset Tickit into the default dev database and public schema. Amazon Redshift automatically loads the sample dataset into your Amazon Redshift cluster. You can start using the query editor v2 to query data.
   + To bring your own data to your Amazon Redshift cluster, follow the steps in [Load data from Amazon S3 to Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-sample-db.html).

1. Scroll down to **Additional configurations**, expand **Network and security**, and make sure that you either accept the default **Cluster subnet group** or choose another one. If you choose another cluster subnet group, make sure that there are 3 Availability Zones in the subnet group you selected.

1. Under **Additional configurations**, expand **Database configurations**.

1. Under **Database encryption**, to use a custom KMS key other than the default AWS-owned key, click **Customize encryption settings**. This option is deselected by default.

1. Under **Choose an KMS key**, you can either choose an AWS Key Management Service key or enter an ARN. Or, you can click **Create an AWS Key Management Service key** in the AWS Key Management Service console. For more information about creating KMS keys, see [Creating Keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide*.

1. Click **Restore cluster from snapshot**. When the cluster restoration succeeds, you can view the details in the cluster details page.

## Using the AWS Command Line Interface
<a name="maz-snapshot-cli"></a>
+ From the AWS CLI, use the `restore-from-cluster-snapshot` command as follows.

  ```
  aws redshift restore-from-cluster-snapshot 
  --region eu-west-1
  --multi-az 
  --snapshot-identifier test-snap1
  --cluster-identifier test-saz-11 
  --endpoint-url https://redshift.eu-west-1.amazonaws.com/
  ```