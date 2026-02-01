Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Setting up Multi-AZ when creating a new

cluster

Amazon Redshift Multi-AZ supports two Availability Zones at a time. Amazon Redshift automatically
selects the Availability Zones based on the selected subnet group configuration. You can
convert an existing single Availability Zone data warehouse into a Multi-AZ data
warehouse or restore from a snapshot to configure it into a Multi-AZ data
warehouse.

Using the Amazon Redshift console, you can easily create new Multi-AZ
deployments. To create a new Multi-AZ
deployment using the Amazon Redshift console, select the Multi-AZ option when creating the data
warehouse. Specify the number of compute nodes required in a single Availability Zone,
and Amazon Redshift will deploy that number of nodes in each of two Availability Zones. All
nodes will be used to read and write workload processing during normal operation. You
can also use the AWS CLI `create-cluster` command to create a new Multi-AZ data
warehouse using the `multi-az` parameter.

You can convert an existing Single-AZ data warehouse into a Multi-AZ data warehouse,
you can use either the Amazon Redshift console or the AWS CLI `modify-cluster` command
using the `multi-az` parameter. Or, you can restore from a snapshot to
configure a Single-AZ data warehouse into a Multi-AZ data warehouse either using the
Amazon Redshift console or the AWS CLI `restore-from-cluster-snapshot` command using
the `multi-az` parameter.

Multi-AZ deployment only supports RA3 node types that use Amazon Redshift Managed Storage (RMS).
Amazon Redshift stores data in RMS, which uses Amazon S3 and is accessible in all Availability Zones
in an AWS Region, without having to replicate the data at the Amazon Redshift level.

You can set up Multi-AZ deployment when creating a new cluster either using the
Amazon Redshift console or the AWS Command Line Interface.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Provisioned clusters
   dashboard**, and choose **Clusters**. The
   clusters for your account in the current AWS Region are listed. A
   subset of properties of each cluster is displayed in columns in the
   list.
3. Choose the button **Create cluster** to open the create
   cluster page.
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
   - To bring your own data to your Amazon Redshift cluster, follow the
     steps in [Bringing your
     own data to Amazon Redshift](../gsg/bring-own-data.md "../gsg/bring-own-data.md").

9. Scroll down to **Additional configurations**, expand
   **Network and security**, and make sure that you
   either accept the default **Cluster subnet group** or
   choose another one. If you choose another cluster subnet group, make
   sure that there are 3 Availability Zones in the subnet group you
   selected.
10. Under **Additional configurations**, expand
    **Database configurations**.
11. To use a custom AWS KMS key instead of the default AWS-owned key, click
    **Customize encryption settings** under
    **Database encryption**.
12. Under **Choose an KMS key**, you can either choose
    an AWS Key Management Service key or enter an ARN. Or, you can click **Create an
    AWS Key Management Service key** in the AWS Key Management Service console. For more
    information about creating KMS keys, see [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
    _AWS Key Management Service Developer Guide_.
13. Click **Create cluster**. When the cluster creation
    succeeds, you can view the details in the cluster details page. You can
    use your SQL client to load and query data.

###### To set up Multi-AZ when creating a cluster using the AWS Command Line Interface

- From the AWS CLI use the `create-cluster` command and the
  `multi-az` parameter as follows.

```
aws redshift create-cluster
    --port 5439
    --master-username master
    --master-user-password #####
    --node-type ra3.4xlarge
    --number-of-nodes 2
    --profile maz-test
    --endpoint-url https://redshift.eu-west-1.amazonaws.com
    --region eu-west-1
    --cluster-identifier test-maz
    --multi-az
    --maintenance-track-name CURRENT
    --encrypted
```
