Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Resizing a Multi-AZ data warehouse

You can resize a Multi-AZ data warehouse and specify a number of nodes or node type
that is different from the current configuration of the data warehouse.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Provisioned clusters
   dashboard**, and choose **Clusters**. The
   clusters for your account in the current AWS Region are listed. A
   subset of properties of each cluster is displayed in columns in the
   list.
3. Choose the cluster you want to resize the Multi-AZ data warehouse. The
   cluster details page appears.
4. For **Actions**, choose **Resize**.
   The Resize cluster page appears.
5. Follow the instructions on the page. You can resize the cluster now,
   once at a specific time, or increase and decrease the size of your
   cluster on a schedule.
6. Under **New configurations**, choose one of the RA3
   node types from the Node type drop-down list.
7. Click **Resize cluster**.

###### To resize a Multi-AZ data warehouse using the AWS Command Line Interface

- From the AWS CLI, use the `resize-cluster` command to change
  the number of nodes for a single Availability Zone as follows.

```
aws redshift resize-cluster \
    --cluster-identifier test-maz-11
    --cluster-type multi-node
    --node-type ra3.4xlarge
    --number-of-nodes 6
```
