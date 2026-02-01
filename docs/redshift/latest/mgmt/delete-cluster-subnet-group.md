Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Deleting a cluster subnet group for a

provisioned cluster

When you're done using a cluster subnet group, you should clean up by deleting the
group. The following procedure walks you through the steps to delete a subnet group for
a provisioned cluster.

###### To delete a cluster subnet group

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Configurations**, then
   choose **Subnet groups**. The list of subnet groups is
   displayed.
3. Choose the subnet group to delete, then choose **Delete**.

###### Note

You can't delete a cluster subnet group that is used by a cluster.
