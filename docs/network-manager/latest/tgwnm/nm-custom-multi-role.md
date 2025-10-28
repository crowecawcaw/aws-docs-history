# Multi-account access roles for AWS Global Networks for Transit Gateways

AWS Global Networks for Transit Gateways uses AWS CloudFormation StackSets to deploy and manage the following two custom IAM roles
in AWS Organizations member accounts to support multi-account permissions. These two roles are
deployed to every member account in the organization when `AWSServiceAccess` is
enabled (trusted access). For more information about multi-account, see [Manage multiple accounts in global networks using AWS Organizations](nm-multi-account.md#tgw-nm-multi "nm-multi-account.md#tgw-nm-multi").

The custom IAM roles are created automatically through the `Network Manager`
service when you enable multi-account access using the global networks console. We strongly recommend
that you use the console for enabling multi-account. Choosing an alternative approach
requires an advanced level of expertise, and opens the multi-account for your global network
to be more prone to error.

## CloudWatch-CrossAccountSharingRole

This policy provides delegated administrators and the management accounts access to
CloudWatch monitoring data from other member accounts. The following is an example of the
template.

```
AWSTemplateFormatVersion: '2010-09-09'
Description: Enables CloudWatch in central monitoring accounts to assume permissions to view CloudWatch data in the current account

Resources:
  CloudWatch-CrossAccountSharingRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: CloudWatch-CrossAccountSharingRole
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              AWS: [
                "arn:aws:iam::<account1-id>:root",
                "arn:aws:iam::<account2-id>:root",
                "arn:aws:iam::<account3-id>:root"
              ]
            Action:
              - sts:AssumeRole
      Path: "/"
      ManagedPolicyArns:
          - arn:aws:iam::aws:policy/CloudWatchReadOnlyAccess
```

## IAMRoleForAWSNetworkManagerCrossAccountResourceAccess

The `IAMRoleForAWSNetworkManagerCrossAccountResourceAccess` IAM policy
role, based on your selection when enabling trusted access through the global networksconsole,
enables either administrative or read-only global networks console switch role access. An
associated administrative or read-only template is also deployed along with the policy.
For information about these templates, see [Permission templates](#nm-permission-templates "#nm-permission-templates").

The following is an example of the administrator role template.

```
AWSTemplateFormatVersion: '2010-09-09'
Description: Enables admin cross account resource access through switch role

Resources:
  IAMRoleForAWSNetworkManagerCrossAccountResourceAccess:
    Type: AWS::IAM::Role
    Properties:
      RoleName: IAMRoleForAWSNetworkManagerCrossAccountResourceAccess
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              AWS: [
                "arn:aws:iam::<account1-id>:root",
                "arn:aws:iam::<account2-id>:root",
                "arn:aws:iam::<account3-id>:root"
              ]
            Action:
              - sts:AssumeRole
      Path: "/"
      ManagedPolicyArns:
          - arn:aws:iam::aws:policy/NetworkAdministrator
```

The following is the read-only role template.

```
AWSTemplateFormatVersion: '2010-09-09'
Description: Enables read only cross account resource access through switch role
Resources:
 IAMRoleForAWSNetworkManagerCrossAccountResourceAccess:
 Type: AWS::IAM::Role
 Properties:
    RoleName: IAMRoleForAWSNetworkManagerCrossAccountResourceAccess
    AssumeRolePolicyDocument:
    Version: '2012-10-17'
    Statement:
      - Effect: Allow
        Principal:
          AWS: [
            "arn:aws:iam::<account1-id>:root",
            "arn:aws:iam::<account2-id>:root",
            "arn:aws:iam::<account3-id>:root"
          ]
       Action:
         - sts:AssumeRole
    Path: "/"
    ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AWSNetworkManagerReadOnlyAccess
        - arn:aws:iam::aws:policy/AWSDirectConnectReadOnlyAccess
        - arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess
        - arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess
```

## Permission templates

When choosing the `IAMRoleForAWSNetworkManagerCrossAccountResourceAccess`
permission, an associated administrative or read-only template is also passed to AWS CloudFormation
StackSets. These templates contain a list of accounts that are able to assume these
roles. These accounts include the AWS Organizations management account and all registered
delegated administrators for the Network Manager service. Deregistering a delegated
administrator removes it from this list so that it can no longer assume these roles.
Disabling trusted access deletes the AWS CloudFormation StackSets, and in turn all member account
stacks and custom IAM roles in those accounts that were StackSets-managed for
multi-account.

###### Template policies for

IAMRoleForAWSNetworkManagerCrossAccountResourceAccess

This policy enables administrator permission for the delegated administrator and
management accounts to modify resources from other accounts in the global
network while using the Network Manager console switch role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "autoscaling:Describe*",
 "cloudfront:ListDistributions",
 "cloudwatch:DeleteAlarms",
 "cloudwatch:DescribeAlarms",
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:PutMetricAlarm",
 "directconnect:*",
 "ec2:AcceptVpcEndpointConnections",
 "ec2:AllocateAddress",
 "ec2:AssignIpv6Addresses",
 "ec2:AssignPrivateIpAddresses",
 "ec2:AssociateAddress",
 "ec2:AssociateDhcpOptions",
 "ec2:AssociateRouteTable",
 "ec2:AssociateSubnetCidrBlock",
 "ec2:AssociateVpcCidrBlock",
 "ec2:AttachInternetGateway",
 "ec2:AttachNetworkInterface",
 "ec2:AttachVpnGateway",
 "ec2:CreateCarrierGateway",
 "ec2:CreateCustomerGateway",
 "ec2:CreateDefaultSubnet",
 "ec2:CreateDefaultVpc",
 "ec2:CreateDhcpOptions",
 "ec2:CreateEgressOnlyInternetGateway",
 "ec2:CreateFlowLogs",
 "ec2:CreateInternetGateway",
 "ec2:CreateNatGateway",
 "ec2:CreateNetworkAcl",
 "ec2:CreateNetworkAclEntry",
 "ec2:CreateNetworkInterface",
 "ec2:CreateNetworkInterfacePermission",
 "ec2:CreatePlacementGroup",
 "ec2:CreateRoute",
 "ec2:CreateRouteTable",
 "ec2:CreateSecurityGroup",
 "ec2:CreateSubnet",
 "ec2:CreateTags",
 "ec2:CreateVpc",
 "ec2:CreateVpcEndpoint",
 "ec2:CreateVpcEndpointConnectionNotification",
 "ec2:CreateVpcEndpointServiceConfiguration",
 "ec2:CreateVpnConnection",
 "ec2:CreateVpnConnectionRoute",
 "ec2:CreateVpnGateway",
 "ec2:DeleteCarrierGateway",
 "ec2:DeleteEgressOnlyInternetGateway",
 "ec2:DeleteFlowLogs",
 "ec2:DeleteNatGateway",
 "ec2:DeleteNetworkInterface",
 "ec2:DeleteNetworkInterfacePermission",
 "ec2:DeletePlacementGroup",
 "ec2:DeleteSubnet",
 "ec2:DeleteTags",
 "ec2:DeleteVpc",
 "ec2:DeleteVpcEndpointConnectionNotifications",
 "ec2:DeleteVpcEndpointServiceConfigurations",
 "ec2:DeleteVpcEndpoints",
 "ec2:DeleteVpnConnection",
 "ec2:DeleteVpnConnectionRoute",
 "ec2:DeleteVpnGateway",
 "ec2:DescribeAccountAttributes",
 "ec2:DescribeAddresses",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeCarrierGateways",
 "ec2:DescribeClassicLinkInstances",
 "ec2:DescribeCustomerGateways",
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeEgressOnlyInternetGateways",
 "ec2:DescribeFlowLogs",
 "ec2:DescribeInstances",
 "ec2:DescribeInternetGateways",
 "ec2:DescribeKeyPairs",
 "ec2:DescribeMovingAddresses",
 "ec2:DescribeNatGateways",
 "ec2:DescribeNetworkAcls",
 "ec2:DescribeNetworkInterfaceAttribute",
 "ec2:DescribeNetworkInterfacePermissions",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribePlacementGroups",
 "ec2:DescribePrefixLists",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroupReferences",
 "ec2:DescribeSecurityGroupRules",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeStaleSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeTags",
 "ec2:DescribeVpcAttribute",
 "ec2:DescribeVpcClassicLink",
 "ec2:DescribeVpcClassicLinkDnsSupport",
 "ec2:DescribeVpcEndpointConnectionNotifications",
 "ec2:DescribeVpcEndpointConnections",
 "ec2:DescribeVpcEndpointServiceConfigurations",
 "ec2:DescribeVpcEndpointServicePermissions",
 "ec2:DescribeVpcEndpointServices",
 "ec2:DescribeVpcEndpoints",
 "ec2:DescribeVpcPeeringConnections",
 "ec2:DescribeVpcs",
 "ec2:DescribeVpnConnections",
 "ec2:DescribeVpnGateways",
 "ec2:DescribePublicIpv4Pools",
 "ec2:DescribeIpv6Pools",
 "ec2:DetachInternetGateway",
 "ec2:DetachNetworkInterface",
 "ec2:DetachVpnGateway",
 "ec2:DisableVgwRoutePropagation",
 "ec2:DisableVpcClassicLinkDnsSupport",
 "ec2:DisassociateAddress",
 "ec2:DisassociateRouteTable",
 "ec2:DisassociateSubnetCidrBlock",
 "ec2:DisassociateVpcCidrBlock",
 "ec2:EnableVgwRoutePropagation",
 "ec2:EnableVpcClassicLinkDnsSupport",
 "ec2:ModifyNetworkInterfaceAttribute",
 "ec2:ModifySecurityGroupRules",
 "ec2:ModifySubnetAttribute",
 "ec2:ModifyVpcAttribute",
 "ec2:ModifyVpcEndpoint",
 "ec2:ModifyVpcEndpointConnectionNotification",
 "ec2:ModifyVpcEndpointServiceConfiguration",
 "ec2:ModifyVpcEndpointServicePermissions",
 "ec2:ModifyVpcPeeringConnectionOptions",
 "ec2:ModifyVpcTenancy",
 "ec2:MoveAddressToVpc",
 "ec2:RejectVpcEndpointConnections",
 "ec2:ReleaseAddress",
 "ec2:ReplaceNetworkAclAssociation",
 "ec2:ReplaceNetworkAclEntry",
 "ec2:ReplaceRoute",
 "ec2:ReplaceRouteTableAssociation",
 "ec2:ResetNetworkInterfaceAttribute",
 "ec2:RestoreAddressToClassic",
 "ec2:UnassignIpv6Addresses",
 "ec2:UnassignPrivateIpAddresses",
 "ec2:UpdateSecurityGroupRuleDescriptionsEgress",
 "ec2:UpdateSecurityGroupRuleDescriptionsIngress",
 "elasticbeanstalk:Describe*",
 "elasticbeanstalk:List*",
 "elasticbeanstalk:RequestEnvironmentInfo",
 "elasticbeanstalk:RetrieveEnvironmentInfo",
 "elasticloadbalancing:*",
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams",
 "logs:GetLogEvents",
 "route53:*",
 "route53domains:*",
 "sns:CreateTopic",
 "sns:ListSubscriptionsByTopic",
 "sns:ListTopics"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AcceptVpcPeeringConnection",
 "ec2:AttachClassicLinkVpc",
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:CreateVpcPeeringConnection",
 "ec2:DeleteCustomerGateway",
 "ec2:DeleteDhcpOptions",
 "ec2:DeleteInternetGateway",
 "ec2:DeleteNetworkAcl",
 "ec2:DeleteNetworkAclEntry",
 "ec2:DeleteRoute",
 "ec2:DeleteRouteTable",
 "ec2:DeleteSecurityGroup",
 "ec2:DeleteVolume",
 "ec2:DeleteVpcPeeringConnection",
 "ec2:DetachClassicLinkVpc",
 "ec2:DisableVpcClassicLink",
 "ec2:EnableVpcClassicLink",
 "ec2:GetConsoleScreenshot",
 "ec2:RejectVpcPeeringConnection",
 "ec2:RevokeSecurityGroupEgress",
 "ec2:RevokeSecurityGroupIngress"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateLocalGatewayRoute",
 "ec2:CreateLocalGatewayRouteTableVpcAssociation",
 "ec2:DeleteLocalGatewayRoute",
 "ec2:DeleteLocalGatewayRouteTableVpcAssociation",
 "ec2:DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations",
 "ec2:DescribeLocalGatewayRouteTableVpcAssociations",
 "ec2:DescribeLocalGatewayRouteTables",
 "ec2:DescribeLocalGatewayVirtualInterfaceGroups",
 "ec2:DescribeLocalGatewayVirtualInterfaces",
 "ec2:DescribeLocalGateways",
 "ec2:SearchLocalGatewayRoutes"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:GetBucketWebsite",
 "s3:ListBucket"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:GetRole",
 "iam:ListRoles",
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::*:role/flow-logs-*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "networkmanager:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AcceptTransitGatewayVpcAttachment",
 "ec2:AssociateTransitGatewayRouteTable",
 "ec2:CreateTransitGateway",
 "ec2:CreateTransitGatewayRoute",
 "ec2:CreateTransitGatewayRouteTable",
 "ec2:CreateTransitGatewayVpcAttachment",
 "ec2:DeleteTransitGateway",
 "ec2:DeleteTransitGatewayRoute",
 "ec2:DeleteTransitGatewayRouteTable",
 "ec2:DeleteTransitGatewayVpcAttachment",
 "ec2:DescribeTransitGatewayAttachments",
 "ec2:DescribeTransitGatewayRouteTables",
 "ec2:DescribeTransitGatewayVpcAttachments",
 "ec2:DescribeTransitGateways",
 "ec2:DisableTransitGatewayRouteTablePropagation",
 "ec2:DisassociateTransitGatewayRouteTable",
 "ec2:EnableTransitGatewayRouteTablePropagation",
 "ec2:ExportTransitGatewayRoutes",
 "ec2:GetTransitGatewayAttachmentPropagations",
 "ec2:GetTransitGatewayRouteTableAssociations",
 "ec2:GetTransitGatewayRouteTablePropagations",
 "ec2:ModifyTransitGateway",
 "ec2:ModifyTransitGatewayVpcAttachment",
 "ec2:RejectTransitGatewayVpcAttachment",
 "ec2:ReplaceTransitGatewayRoute",
 "ec2:SearchTransitGatewayRoutes"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": [
 "transitgateway.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

This policy enables read-only permission for the delegated administrator and
management accounts to review information about resources from other accounts in
the global network while using the global networks console switch role, but doesn't allow
either account to make changes.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "networkmanager:Describe*",
 "networkmanager:Get*",
 "networkmanager:List*"
 ],
 "Resource": "*"
 }
 ]
}`

```
