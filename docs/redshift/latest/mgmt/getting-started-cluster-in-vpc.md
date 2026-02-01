Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating a Redshift provisioned

cluster or Amazon Redshift Serverless workgroup in a VPC

The following are the general steps how you can deploy a cluster or workgroup in your
virtual private cloud (VPC).

###### To create a cluster or Serverless workgroup in a VPC

1. Configure a VPC – You can create your Redshift resources either in the
   default VPC for your account, if your account has one, or in a VPC that you
   created. For more information, see [Use EC2 to create your cluster](working-with-clusters.md#cluster-platforms "working-with-clusters.md#cluster-platforms"). To create a VPC, see [Subnets for your VPC](../../../vpc/latest/userguide/configure-subnets.md "../../../vpc/latest/userguide/configure-subnets.md") in the _Amazon VPC User Guide._ Make a
   note of the VPC identifier, subnet, and subnet's Availability Zone. You
   need this information when you launch your cluster or workgroup.

###### Note

You must have at least one subnet defined in your VPC, so you can add it
to the subnet group in the next step. For more information about adding a
subnet to your VPC, see [Adding a subnet to your VPC](../../../vpc/latest/userguide/working-with-subnets.md "../../../vpc/latest/userguide/working-with-subnets.md") in the
_Amazon VPC User Guide._ 2. Create an Amazon Redshift cluster subnet group to specify which subnet your Amazon Redshift
cluster can use in the VPC. For Redshift Serverless, you don't create a subnet
group, but rather assign a collection of subnets to your workgroup when you
create it. You can perform this in the **Serverless dashboard**
when you create a workgroup.

You can create a subnet group using either the Amazon Redshift console or
programmatically. For more information, see [Subnets for Redshift resources](working-with-cluster-subnet-groups.md "working-with-cluster-subnet-groups.md"). 3. Authorize access for inbound connections in a VPC security group that you
associate with the cluster or workgroup. You can enable a client outside the VPC
(on the public internet) to connect to the cluster. To do this, you associate
the cluster with a VPC security group that grants inbound access. For more
information, see [Configuring security group
communication settings for an Amazon Redshift cluster or an Amazon Redshift Serverless workgroup](rs-security-group-public-private.md "rs-security-group-public-private.md"). 4. Follow the steps to create a cluster in the Redshift provisioned console or a
workgroup or in the Amazon Redshift Serverless console. In **Network and
security**, specify the **Virtual private cloud
(VPC)**, **Cluster subnet group**, and
**VPC security group** that you set up.

For a walkthrough that shows more detailed steps for creating a provisioned
data-warehouse cluster, see [Get started with Amazon Redshift
provisioned data warehouses](../gsg/new-user.md "../gsg/new-user.md") in the
_Amazon Redshift Getting Started Guide_. For more information about creating an
Amazon Redshift Serverless workgroup, see [Get started with
Amazon Redshift Serverless data warehouses](../gsg/new-user-serverless.md "../gsg/new-user-serverless.md") in the
_Amazon Redshift Getting Started Guide_.
You can follow the Getting Started steps to test the cluster or workgroup by uploading
sample data and trying example queries. For more information, see [Get started with Amazon Redshift Serverless data warehouses](../gsg/rs-gsg-launch-sample-cluster.md "../gsg/rs-gsg-launch-sample-cluster.md") in the _Amazon Redshift Getting Started Guide_.
