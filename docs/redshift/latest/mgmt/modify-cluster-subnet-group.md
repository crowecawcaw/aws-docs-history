Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Modifying a cluster subnet group

After you've created a subnet group, you can modify its information on the Amazon Redshift
console.The following procedure walks you through how to modify a subnet group for a
provisioned cluster.

###### To modify a cluster subnet group for a provisioned cluster

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Configurations**, then
   choose **Subnet groups**. The list of subnet groups is
   displayed.
3. Choose the subnet group to modify.
4. For **Actions**, choose **Modify** to
   display the details of the subnet group.
5. Update information for the subnet group.
6. Choose **Save** to modify the group.
   To change or remove subnets in some cases requires extra steps. For example, this
   AWS Knowledge Center article, [How do I move my
   provisioned Amazon Redshift cluster into a different subnet?](https://repost.aws//knowledge-center/redshift-move-subnet "https://repost.aws//knowledge-center/redshift-move-subnet"), describes a use case that
   covers moving a cluster.
