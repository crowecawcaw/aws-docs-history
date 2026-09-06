

# AWS managed policies for AWS Global Networks for Transit Gateways
<a name="security-iam-awsmanpol"></a>

To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the ReadOnlyAccess AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

## AWS managed policy: NetworkAdministrator
<a name="security-iam-NetworkAdministrator"></a>

You can attach the NetworkAdministrator policy to your IAM identities. This policy grants permissions that allow registered delegated administrators and the management account *administrator* access to global networks. For more information, see [Multi-account access roles for AWS Global Networks for Transit Gateways](nm-custom-multi-role.md).

To view the permissions for this policy, see [NetworkAdministrator](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/NetworkAdministrator.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSNetworkManagerReadOnlyAccess
<a name="security-iam-AWSNetworkManagerReadOnlyAccess"></a>

You can attach the AWSNetworkManagerReadOnlyAccess policy to your IAM identities. This policy grants permissions that allow registered delegated administrators and the management account *read-only* access to global networks. For more information, see [Multi-account access roles for AWS Global Networks for Transit Gateways](nm-custom-multi-role.md).

To view the permissions for this policy, see [AWSNetworkManagerReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSNetworkManagerReadOnlyAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSNetworkManagerServiceRolePolicy
<a name="security-iam-AWSNetworkManagerServiceRolePolicy"></a>

This policy is attached to the service-linked role named AWSServiceRoleForNetworkManager to allow AWS Global Networks for Transit Gateways to call API actions on your behalf when you work with global networks. For more information, see [AWS Global Networks for Transit Gateways service-linked roles](nm-service-linked-roles.md).

To view the permissions for this policy, see [AWSNetworkManagerServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSNetworkManagerServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS Global Networks for Transit Gateways updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Network Manager since this service began tracking these changes in April 2021. For automatic alerts about changes to this page, subscribe to the RSS feed on the Network Manager Document history page.


| Change | Description | Date | 
| --- | --- | --- | 
| [AWSNetworkManagerServiceRolePolicy](#security-iam-AWSNetworkManagerServiceRolePolicy) | AWS Global Networks for Transit Gateways added permission to call the following API action: GetTransitGatewayRouteTablePropagations. | July 12, 2022 | 
| [NetworkAdministrator](#security-iam-NetworkAdministrator) | AWS Global Networks for Transit Gateways began using administrative permissions in member accounts for multi-account access. | May 24, 2022 | 
| [AWSNetworkManagerReadOnlyAccess](#security-iam-AWSNetworkManagerReadOnlyAccess) - Updated existing policy | AWS Global Networks for Transit Gateways began using read-only permissions in member accounts for multi-account access. | May 24, 2022 | 
| [AWSNetworkManagerServiceRolePolicy](#security-iam-AWSNetworkManagerServiceRolePolicy) - Updated existing policy | AWS Global Networks for Transit Gateways added permission to call the following API actions: organizations:DescribeAccount, organizations:DescribeOrganization, organizations:ListAccounts, organizations:ListAWSServiceAccessForOrganization, and organizations:ListDelegatedAdministrators. | May 24, 2022 | 
| [AWSNetworkManagerServiceRolePolicy](#security-iam-AWSNetworkManagerServiceRolePolicy) - Updated existing policy | AWS Global Networks for Transit Gateways added permissions to call the following API action: ec2:DescribeRegions. | December 2, 2021 | 
| [AWSNetworkManagerServiceRolePolicy](#security-iam-AWSNetworkManagerServiceRolePolicy): updated existing policy | AWS Global Networks for Transit Gateways added permissions to call the following API actions: directconnect:DescribeDirectConnectGateways, ec2:DescribeVpnConnections, ec2:DescribeVpcs, ec2:GetTransitGatewayRouteTableAssociations, ec2:SearchTransitGatewayRoutes, ec2:DescribeTransitGatewayPeeringAttachments, ec2:DescribeTransitGatewayConnects, and ec2:DescribeTransitGatewayConnectPeers. | June 1, 2021 | 