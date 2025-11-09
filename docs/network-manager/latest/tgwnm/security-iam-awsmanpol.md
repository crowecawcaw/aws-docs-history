# AWS managed policies for AWS Global Networks for Transit Gateways

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't break
your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the ReadOnlyAccess AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed policy: NetworkAdministrator

You can attach the NetworkAdministrator policy to your IAM identities.
This policy grants permissions that allow registered delegated administrators and the
management account _administrator_ access to global networks. For more
information, see [Multi-account access roles for AWS Global Networks for Transit Gateways](nm-custom-multi-role.md "nm-custom-multi-role.md").

To view the permissions for this policy, see [NetworkAdministrator](../../../aws-managed-policy/latest/reference/NetworkAdministrator.md "../../../aws-managed-policy/latest/reference/NetworkAdministrator.md")
in the _AWS Managed Policy Reference_.

## AWS managed policy: AWSNetworkManagerReadOnlyAccess

You can attach the AWSNetworkManagerReadOnlyAccess policy to your IAM
identities. This policy grants permissions that allow registered delegated administrators
and the management account _read-only_ access to global networks. For more
information, see [Multi-account access roles for AWS Global Networks for Transit Gateways](nm-custom-multi-role.md "nm-custom-multi-role.md").

To view the permissions for this policy, see [AWSNetworkManagerReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSNetworkManagerReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSNetworkManagerReadOnlyAccess.md")
in the _AWS Managed Policy Reference_.

## AWS managed policy: AWSNetworkManagerServiceRolePolicy

This policy is attached to the service-linked role named
AWSServiceRoleForNetworkManager to allow AWS Global Networks for Transit Gateways to call API actions
on your behalf when you work with global networks. For more information, see [AWS Global Networks for Transit Gateways service-linked roles](nm-service-linked-roles.md "nm-service-linked-roles.md").

To view the permissions for this policy, see [AWSNetworkManagerServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSNetworkManagerServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSNetworkManagerServiceRolePolicy.md")
in the _AWS Managed Policy Reference_.

## AWS Global Networks for Transit Gateways updates to AWS managed policies

View details about updates to AWS managed policies for Network Manager since this service
began tracking these changes in April 2021. For automatic alerts about changes to this
page, subscribe to the RSS feed on the Network Manager Document history page.

| Change                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                              | Date             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| [AWSNetworkManagerServiceRolePolicy](#security-iam-AWSNetworkManagerServiceRolePolicy "#security-iam-AWSNetworkManagerServiceRolePolicy")                              | AWS Global Networks for Transit Gateways added permission to call the following API<br>action: `GetTransitGatewayRouteTablePropagations`.                                                                                                                                                                                                                                                                                                | July 12, 2022    |
| [NetworkAdministrator](#security-iam-NetworkAdministrator "#security-iam-NetworkAdministrator")                                                                        | AWS Global Networks for Transit Gateways began using administrative permissions in member accounts for<br>multi-account access.                                                                                                                                                                                                                                                                                                          | May 24, 2022     |
| [AWSNetworkManagerReadOnlyAccess](#security-iam-AWSNetworkManagerReadOnlyAccess "#security-iam-AWSNetworkManagerReadOnlyAccess")<br>• Updated existing policy          | AWS Global Networks for Transit Gateways began using read-only permissions in member accounts for<br>multi-account access.                                                                                                                                                                                                                                                                                                               | May 24, 2022     |
| [AWSNetworkManagerServiceRolePolicy](#security-iam-AWSNetworkManagerServiceRolePolicy "#security-iam-AWSNetworkManagerServiceRolePolicy")<br>• Updated existing policy | AWS Global Networks for Transit Gateways added permission to call the following API<br>actions: `organizations:DescribeAccount`,<br>`organizations:DescribeOrganization`,<br>`organizations:ListAccounts`,<br>`organizations:ListAWSServiceAccessForOrganization`, and<br>`organizations:ListDelegatedAdministrators`.                                                                                                                   | May 24, 2022     |
| [AWSNetworkManagerServiceRolePolicy](#security-iam-AWSNetworkManagerServiceRolePolicy "#security-iam-AWSNetworkManagerServiceRolePolicy")<br>• Updated existing policy | AWS Global Networks for Transit Gateways added permissions to call the following API action:<br>`ec2:DescribeRegions`.                                                                                                                                                                                                                                                                                                                   | December 2, 2021 |
| [AWSNetworkManagerServiceRolePolicy](#security-iam-AWSNetworkManagerServiceRolePolicy "#security-iam-AWSNetworkManagerServiceRolePolicy"): updated existing policy     | AWS Global Networks for Transit Gateways added permissions to call the following API actions:<br>`directconnect:DescribeDirectConnectGateways`,<br>`ec2:DescribeVpnConnections`, `ec2:DescribeVpcs`,<br>`ec2:GetTransitGatewayRouteTableAssociations`,<br>`ec2:SearchTransitGatewayRoutes`,<br>`ec2:DescribeTransitGatewayPeeringAttachments`,<br>`ec2:DescribeTransitGatewayConnects`, and<br>`ec2:DescribeTransitGatewayConnectPeers`. | June 1, 2021     |
