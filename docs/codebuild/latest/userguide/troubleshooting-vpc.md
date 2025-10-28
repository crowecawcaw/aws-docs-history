# Troubleshoot your VPC setup

Use the information that appears in the error message to help you identify, diagnose,
and address issues.

The following are some guidelines to assist you when troubleshooting a common CodeBuild
VPC error: `Build does not have internet connectivity. Please check subnet network
 configuration`.

1. [Make sure that your internet gateway is attached to VPC](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway").
2. [Make sure that the route table for your public subnet points to the
   internet gateway](../../../vpc/latest/userguide/VPC_Route_Tables.md#route-tables-internet-gateway "../../../vpc/latest/userguide/VPC_Route_Tables.md#route-tables-internet-gateway").
3. [Make
   sure that your network ACLs allow traffic to flow](../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules").
4. [Make
   sure that your security groups allow traffic to flow](../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules").
5. [Troubleshoot your NAT gateway](../../../vpc/latest/userguide/VPC-nat-gateway.md#nat-gateway-troubleshooting "../../../vpc/latest/userguide/VPC-nat-gateway.md#nat-gateway-troubleshooting").
6. [Make sure
   that the route table for private subnets points to the NAT
   gateway](../../../vpc/latest/userguide/VPC_Route_Tables.md#route-tables-nat "../../../vpc/latest/userguide/VPC_Route_Tables.md#route-tables-nat").
7. Make sure that the service role used by CodeBuild to interact with services on
   behalf of the IAM user has the permissions in [this policy](auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-create-vpc-network-interface "auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-create-vpc-network-interface"). For more information, see [Allow CodeBuild to interact with other AWS
   services](setting-up-service-role.md "setting-up-service-role.md").

If CodeBuild is missing permissions, you might receive an error that says,
`Unexpected EC2 error: UnauthorizedOperation`. This error can
occur if CodeBuild does not have the Amazon EC2 permissions required to work with a
VPC.
