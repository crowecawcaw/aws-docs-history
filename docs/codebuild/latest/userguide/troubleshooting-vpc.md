

# Troubleshoot your VPC setup
<a name="troubleshooting-vpc"></a>

Use the information that appears in the error message to help you identify, diagnose, and address issues.

The following are some guidelines to assist you when troubleshooting a common CodeBuild VPC error: `Build does not have internet connectivity. Please check subnet network configuration`. 

1. [Make sure that your internet gateway is attached to VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html#Add_IGW_Attach_Gateway).

1. [Make sure that the route table for your public subnet points to the internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#route-tables-internet-gateway).

1. [Make sure that your network ACLs allow traffic to flow](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#SecurityGroupRules).

1. [Make sure that your security groups allow traffic to flow](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#SecurityGroupRules).

1. [Troubleshoot your NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC-nat-gateway.html#nat-gateway-troubleshooting).

1. [Make sure that the route table for private subnets points to the NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#route-tables-nat).

1. Make sure that the service role used by CodeBuild to interact with services on behalf of the IAM user has the permissions in [ this policy](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#customer-managed-policies-example-create-vpc-network-interface). For more information, see [Allow CodeBuild to interact with other AWS services](setting-up-service-role.md). 

   If CodeBuild is missing permissions, you might receive an error that says, `Unexpected EC2 error: UnauthorizedOperation`. This error can occur if CodeBuild does not have the Amazon EC2 permissions required to work with a VPC.