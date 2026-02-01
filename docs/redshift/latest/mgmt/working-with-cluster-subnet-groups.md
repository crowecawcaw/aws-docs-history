Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Subnets for Redshift resources

You create a subnet group if you are creating a provisioned cluster in a virtual private
cloud (VPC). Each VPC can have one or more subnets, which are subsets of IP addresses within
the VPC that enable you to group resources based on your security and operation needs. You
create a subnet group to specify a set of subnets in your VPC when you create a provisioned
cluster. In the **Provisioned clusters dashboard**, you can find and edit
cluster subnet groups under **Configurations**. During initial configuration
for a provisioned cluster, you specify the subnet group and Amazon Redshift creates the cluster in
one of its subnets. For more information about the VPC service, see the [Amazon VPC](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/") product detail page.

Subnet configuration for an Amazon Redshift Serverless workgroup is similar to a provisioned
cluster, but the steps differ slightly. When you create and set up a Serverless workgroup,
you specify subnets for the workgroup, and they're added to a list. You can view the subnets
for an existing workgroup by selecting the workgroup properties, in the **Serverless
dashboard**. They're available in the **Network and security**
properties. For more information, see [Creating a
workgroup with a namespace](serverless-console-workgroups-create-workgroup-wizard.md "serverless-console-workgroups-create-workgroup-wizard.md").

For more information about creating a VPC, go to [Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") documentation.

After creating a subnet group for a provisioned cluster, or choosing subnets for a
Serverless workgroup, it's possible to remove subnets previously added or to add more. You
can make these changes using the console, or using API operations. For more information
regarding API operations for a provisioned cluster, see [ModifyClusterSubnetGroup](../APIReference/API_ModifyClusterSubnetGroup.md "../APIReference/API_ModifyClusterSubnetGroup.md").
For API operations for a Serverless workgroup, see [UpdateWorkgroup](../../../redshift-serverless/latest/APIReference/API_UpdateWorkgroup.md "../../../redshift-serverless/latest/APIReference/API_UpdateWorkgroup.md").

You can provision a cluster on one of the subnets in the subnet group. A cluster subnet
group enables you to specify a set of subnets in your virtual private cloud (VPC).

###### Warning

During cluster maintenance operations such as classic resize, pause and resume,
Multi-AZ failovers, or other events, your provisioned compute nodes might be moved to
another subnet within your Amazon Redshift cluster subnet group. Note that all subnets in a subnet
group must have the same Network ACL inbound and outbound rules and the same route-table
routes. This ensures connectivity to and from the Amazon Redshift compute resources, so they can
communicate and function optimally after such maintenance events. Avoid adding subnets
with varying network ACL or route-table configurations to the same Amazon Redshift cluster subnet
group.

For more information about configuring subnets, see [Subnets for your VPC](../../../vpc/latest/userguide/configure-subnets.md "../../../vpc/latest/userguide/configure-subnets.md") in the Amazon VPC
user guide. For more information about Redshift Multi-AZ deployments, see [Multi-AZ deployment](managing-cluster-multi-az.md "managing-cluster-multi-az.md") in
the Redshift management guide. [Resizing a cluster](resizing-cluster.md "resizing-cluster.md") is also covered in the Redshift management
guide.
