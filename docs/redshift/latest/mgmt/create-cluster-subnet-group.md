Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating a cluster subnet group

The following procedure walks you through how to create a subnet group for a
provisioned cluster. You must have at least one cluster subnet group defined to
provision a cluster in a VPC.

###### To create a cluster subnet group for a provisioned cluster

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Configurations**, then
   choose **Subnet groups**. The list of subnet groups is
   displayed.
3. Choose **Create cluster subnet group** to display the create
   page.
4. Enter information for the subnet group, including which subnets to add.
5. Choose **Create cluster subnet group** to create the group
   with the subnets that you chose.

###### Note

For information about how to create an Amazon Redshift Serverless workgroup with a
collection of subnets, see [Creating a workgroup with a namespace](serverless-console-workgroups-create-workgroup-wizard.md "serverless-console-workgroups-create-workgroup-wizard.md") or [Create a subnet](../../../vpc/latest/userguide/create-subnets.md "../../../vpc/latest/userguide/create-subnets.md") in the Amazon VPC
User Guide.
