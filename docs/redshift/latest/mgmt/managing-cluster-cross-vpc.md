Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Redshift-managed VPC endpoints

By default, an Amazon Redshift cluster or an Amazon Redshift Serverless workgroup is provisioned in a virtual
private cloud (VPC). The VPC can be accessed from another VPC or subnet when you either
allow public access or set up an internet gateway, a NAT device, or an AWS Direct Connect
connection to route traffic to it. You can also access a cluster or workgroup by setting up
a Redshift-managed VPC endpoint (powered by AWS PrivateLink).

You can set up a Redshift-managed VPC endpoint as a private connection between a VPC that
contains a cluster or workgroup and a VPC where a client tool is running. If the cluster or
workgroup is in another account, the account owner (grantor) must grant access to the
connecting account (grantee). With this approach, you can access the data warehouse without
using a public IP address or routing traffic through the internet.

These are common reasons to allow access using a Redshift-managed VPC endpoint:

- AWS account A wants to allow a VPC in AWS account B to have access to a
  cluster or workgroup.
- AWS account A wants to allow a VPC that is also in AWS account A to have
  access to a cluster or workgroup.
- AWS account A wants to allow a different subnet in the VPC within AWS account
  A to have access to a cluster or workgroup.
  The workflow to set up a Redshift-managed VPC endpoint to access a cluster or workgroup in
  another account is as follows:

1. The owner account grants access authorization to another account and specifies the
   AWS account ID and VPC identifier (or all VPCs) of the grantee.
2. The grantee account is notified that they have permission to create a
   Redshift-managed VPC endpoint.
3. The grantee account creates a Redshift-managed VPC endpoint.
4. The grantee account accesses the cluster or workgroup of the owner account using
   the Redshift-managed VPC endpoint.
   You can do this using the Amazon Redshift console, the AWS CLI, or the Amazon Redshift API.

## Considerations when using

Redshift-managed VPC endpoints

###### Note

To create or modify Redshift-managed VPC endpoints, you need permission
`ec2:CreateVpcEndpoint` or `ec2:ModifyVpcEndpoint` in your
IAM policy, in addition to other permissions specified in the AWS managed policy
`AmazonRedshiftFullAccess`.

When using Redshift-managed VPC endpoints, keep the following in mind:

- If you're using a provisioned cluster, it must have the RA3 node type. An
  Amazon Redshift Serverless workgroup works for setting up a VPC endpoint too.
- For provisioned clusters, make sure that the cluster is enabled for either
  cluster relocation or Multi-AZ. For information about requirements to turn on
  cluster relocation, see [Relocating a cluster](managing-cluster-recovery.md "managing-cluster-recovery.md"). For information about enabling
  Multi-AZ, see [Setting up Multi-AZ when creating a new
  cluster](create-cluster-multi-az.md "create-cluster-multi-az.md").
- Make sure that the cluster or workgroup to access through its security group
  is available within the valid port ranges 5431-5455 and 8191-8215. The default
  is 5439.
- You can modify the VPC security groups associated with an existing
  Redshift-managed VPC endpoint. To modify other settings, delete the current
  Redshift-managed VPC endpoint and create a new one.
- The number of Redshift-managed VPC endpoints that you can create is limited to
  your VPC endpoint quota.
- The Redshift-managed VPC endpoints aren't accessible from the internet. A
  Redshift-managed VPC endpoint is accessible only within the VPC where the
  endpoint is provisioned or from any VPCs peered with the VPC where the endpoint
  is provisioned as permitted by the route tables and security groups.
- You can't use the Amazon VPC console to manage Redshift-managed VPC
  endpoints.
- When you create a Redshift-managed VPC endpoint for a provisioned cluster, the
  VPC you choose must have a subnet group. To create a subnet group, see [Creating a cluster subnet group](create-cluster-subnet-group.md "create-cluster-subnet-group.md").
- If an Availability Zone is down, Amazon Redshift does not create a new elastic network
  interface in another Availability Zone. You might need to create a new endpoint
  in this case.

For information about quotas and naming constraints, see [Quotas and limits in Amazon Redshift](amazon-redshift-limits.md "amazon-redshift-limits.md").

For information about pricing, see [AWS PrivateLink pricing](https://aws.amazon.com/privatelink/pricing/ "https://aws.amazon.com/privatelink/pricing/").
