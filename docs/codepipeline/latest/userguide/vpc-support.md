# Use CodePipeline with Amazon Virtual Private Cloud

AWS CodePipeline now supports [Amazon Virtual Private
Cloud (Amazon VPC)](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/") endpoints powered by [AWS PrivateLink](https://aws.amazon.com/about-aws/whats-new/2017/11/introducing-aws-privatelink-for-aws-services/ "https://aws.amazon.com/about-aws/whats-new/2017/11/introducing-aws-privatelink-for-aws-services/"). This means you can connect directly to CodePipeline through a private
endpoint in your VPC, keeping all traffic inside your VPC and the AWS network.

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual network that
you define. With a VPC, you have control over your network settings, such as:

- IP address range
- Subnets
- Route tables
- Network gateways
  _Interface VPC endpoints_ are powered by AWS PrivateLink,
  an AWS technology that facilitates private communication between AWS services using an
  elastic network interface with private IP addresses. To connect your VPC to CodePipeline, you
  define an interface VPC endpoint for CodePipeline. This type of endpoint makes it possible for you
  to connect your VPC to AWS services. The endpoint provides reliable, scalable connectivity
  to CodePipeline without requiring an internet gateway, network address translation (NAT) instance,
  or VPN connection. For information about setting up a VPC, see the [VPC User Guide](../../../vpc/latest/userguide/VPC_Introduction.md "../../../vpc/latest/userguide/VPC_Introduction.md").

## Availability

CodePipeline currently supports VPC endpoints in the following AWS Regions:

- US East (Ohio)
- US East (N. Virginia)
- US West (N. California)
- US West (Oregon)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Milan)\*
- Europe (Paris)
- Europe (Stockholm)
- Asia Pacific (Hong Kong)\*
- Asia Pacific (Mumbai)
- Asia Pacific (Tokyo)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- South America (São Paulo)
- AWS GovCloud (US-West)

\* You must enable this Region before you can use it.

## Create a VPC endpoint for

CodePipeline

You can use the Amazon VPC console to create the **com.amazonaws.`region`.codepipeline** VPC
endpoint. In the console, `region` is the Region identifier for
an AWS Region supported by CodePipeline, such as `us-east-2` for the
US East (Ohio) Region. For more information, see [Creating an
Interface Endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

The endpoint is prepopulated with the Region you specified when you signed in to
AWS. If you sign in to another Region, the VPC endpoint is updated with the new
Region.

###### Note

Other AWS services that provide VPC support and integrate with CodePipeline, such as
CodeCommit, might not support using Amazon VPC endpoints for that integration. For
example, traffic between CodePipeline and CodeCommit cannot be restricted to the VPC subnet
range.

## Troubleshooting your VPC setup

When troubleshooting VPC issues, use the information that appears in internet
connectivity error messages to help you identify, diagnose, and address issues.

1. [Make sure that your internet gateway is attached to your
   VPC](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway").
2. [Make sure that the route table for your public subnet points to the
   internet gateway](../../../vpc/latest/userguide/VPC_Route_Tables.md#route-tables-internet-gateway "../../../vpc/latest/userguide/VPC_Route_Tables.md#route-tables-internet-gateway").
3. [Make sure that your network
   ACLs allow traffic to flow](../../../vpc/latest/userguide/VPC_ACLs.md#ACLRules "../../../vpc/latest/userguide/VPC_ACLs.md#ACLRules").
4. [Make
   sure that your security groups allow traffic to flow](../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules").
5. [Make sure
   that the route table for private subnets points to the virtual private
   gateway](../../../vpc/latest/userguide/VPC_Route_Tables.md#route-tables-nat "../../../vpc/latest/userguide/VPC_Route_Tables.md#route-tables-nat").
6. Make sure that the service role used by CodePipeline has the appropriate permissions.
   For example, if CodePipeline does not have the Amazon EC2 permissions required to work with
   an Amazon VPC, you might receive an error that says, "Unexpected EC2 error:
   UnauthorizedOperation."
