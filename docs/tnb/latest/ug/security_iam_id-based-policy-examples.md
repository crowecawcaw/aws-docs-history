# Identity-based policy examples for

AWS Telco Network Builder

By default, users and roles don't have permission to create or modify AWS TNB
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by AWS TNB, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for AWS Telco Network Builder](../../../service-authorization/latest/reference/list_awstelconetworkbuilder.md "../../../service-authorization/latest/reference/list_awstelconetworkbuilder.md") in the _Service Authorization Reference_.

###### Contents

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the AWS TNB
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Service role policy examples](#service-role-policy-examples "#service-role-policy-examples")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete AWS TNB resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Using the AWS TNB

console

To access the AWS Telco Network Builder console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the AWS TNB resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

## Service role policy examples

As an administrator, you own and manage the resources that AWS TNB creates as
defined by the environment and service templates. You must attach IAM service roles
to your account to permit AWS TNB to create resources for your network life-cycle
management.

A IAM service role allows AWS TNB to make calls to resources on your behalf to
instantiate and manage your networks. If you specify a service role, AWS TNB uses
that role’s credential.

You create the service role and its permission policy with the IAM service. For
more information about creating a service role, see [Creating a role to
delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_IAM User Guide_.

As a member of the platform team, you can as an administrator create an
AWS TNB service role and provide it to AWS TNB. This role allows AWS TNB to
make calls to other services such as Amazon Elastic Kubernetes Service and CloudFormation to provision the required
infrastructure for your network and provision network functions as defined in your
NSD.

We recommend that you use the following IAM role and trust policy for your
AWS TNB service role. When scoping down permission on this policy, keep in mind
that AWS TNB may fail with Access Denied errors toward resources descoped from
your policy.

The following code shows an AWS TNB service role policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "sts:GetCallerIdentity"
 ],
 "Resource": "*",
 "Effect": "Allow",
 "Sid": "AssumeRole"
 },
 {
 "Action": [
 "tnb:*"
 ],
 "Resource": "*",
 "Effect": "Allow",
 "Sid": "TNBPolicy"
 },
 {
 "Action": [
 "iam:AddRoleToInstanceProfile",
 "iam:CreateInstanceProfile",
 "iam:DeleteInstanceProfile",
 "iam:GetInstanceProfile",
 "iam:RemoveRoleFromInstanceProfile",
 "iam:TagInstanceProfile",
 "iam:UntagInstanceProfile"
 ],
 "Resource": "*",
 "Effect": "Allow",
 "Sid": "IAMPolicy"
 },
 {
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": [
 "eks.amazonaws.com",
 "eks-nodegroup.amazonaws.com"
 ]
 }
 },
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "*",
 "Effect": "Allow",
 "Sid": "TNBAccessSLRPermissions"
 },
 {
 "Action": [
 "autoscaling:CreateAutoScalingGroup",
 "autoscaling:CreateOrUpdateTags",
 "autoscaling:DeleteAutoScalingGroup",
 "autoscaling:DeleteTags",
 "autoscaling:DescribeAutoScalingGroups",
 "autoscaling:DescribeAutoScalingInstances",
 "autoscaling:DescribeScalingActivities",
 "autoscaling:DescribeTags",
 "autoscaling:UpdateAutoScalingGroup",
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:CreateLaunchTemplate",
 "ec2:CreateLaunchTemplateVersion",
 "ec2:CreateSecurityGroup",
 "ec2:DeleteLaunchTemplateVersions",
 "ec2:DescribeLaunchTemplates",
 "ec2:DescribeLaunchTemplateVersions",
 "ec2:DeleteLaunchTemplate",
 "ec2:DeleteSecurityGroup",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeTags",
 "ec2:GetLaunchTemplateData",
 "ec2:RevokeSecurityGroupEgress",
 "ec2:RevokeSecurityGroupIngress",
 "ec2:RunInstances",
 "ec2:AssociateRouteTable",
 "ec2:AttachInternetGateway",
 "ec2:CreateInternetGateway",
 "ec2:CreateNetworkInterface",
 "ec2:CreateRoute",
 "ec2:CreateRouteTable",
 "ec2:CreateSubnet",
 "ec2:CreateTags",
 "ec2:CreateVpc",
 "ec2:DeleteInternetGateway",
 "ec2:DeleteNetworkInterface",
 "ec2:DeleteRoute",
 "ec2:DeleteRouteTable",
 "ec2:DeleteSubnet",
 "ec2:DeleteTags",
 "ec2:DeleteVpc",
 "ec2:DetachNetworkInterface",
 "ec2:DescribeInstances",
 "ec2:DescribeInternetGateways",
 "ec2:DescribeKeyPairs",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroupRules",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:DetachInternetGateway",
 "ec2:DisassociateRouteTable",
 "ec2:ModifySecurityGroupRules",
 "ec2:ModifySubnetAttribute",
 "ec2:ModifyVpcAttribute",
 "ec2:AllocateAddress",
 "ec2:AssignIpv6Addresses",
 "ec2:AssociateAddress",
 "ec2:AssociateNatGatewayAddress",
 "ec2:AssociateVpcCidrBlock",
 "ec2:CreateEgressOnlyInternetGateway",
 "ec2:CreateNatGateway",
 "ec2:DeleteEgressOnlyInternetGateway",
 "ec2:DeleteNatGateway",
 "ec2:DescribeAddresses",
 "ec2:DescribeEgressOnlyInternetGateways",
 "ec2:DescribeNatGateways",
 "ec2:DisassociateAddress",
 "ec2:DisassociateNatGatewayAddress",
 "ec2:DisassociateVpcCidrBlock",
 "ec2:ReleaseAddress",
 "ec2:UnassignIpv6Addresses",
 "ec2:DescribeImages",
 "eks:CreateCluster",
 "eks:ListClusters",
 "eks:RegisterCluster",
 "eks:TagResource",
 "eks:DescribeAddonVersions",
 "events:DescribeRule",
 "iam:GetRole",
 "iam:ListAttachedRolePolicies"
 ],
 "Resource": "*",
 "Effect": "Allow",
 "Sid": "TNBAccessComputePerms"
 },
 {
 "Resource": "*",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "ec2.amazonaws.com",
 "eks.amazonaws.com",
 "eks-nodegroup.amazonaws.com",
 "events.amazonaws.com",
 "autoscaling.amazonaws.com",
 "codebuild.amazonaws.com"
 ]
 }
 }
 },
 {
 "Action": [
 "codebuild:BatchDeleteBuilds",
 "codebuild:BatchGetBuilds",
 "codebuild:CreateProject",
 "codebuild:DeleteProject",
 "codebuild:ListBuildsForProject",
 "codebuild:StartBuild",
 "codebuild:StopBuild",
 "events:DeleteRule",
 "events:PutRule",
 "events:PutTargets",
 "events:RemoveTargets",
 "s3:CreateBucket",
 "s3:GetBucketAcl",
 "s3:GetObject",
 "eks:DescribeNodegroup",
 "eks:DeleteNodegroup",
 "eks:AssociateIdentityProviderConfig",
 "eks:CreateNodegroup",
 "eks:DeleteCluster",
 "eks:DeregisterCluster",
 "eks:UpdateAddon",
 "eks:UpdateClusterVersion",
 "eks:UpdateNodegroupConfig",
 "eks:UpdateNodegroupVersion",
 "eks:DescribeUpdate",
 "eks:UntagResource",
 "eks:DescribeCluster",
 "eks:ListNodegroups",
 "eks:CreateAddon",
 "eks:DeleteAddon",
 "eks:DescribeAddon",
 "eks:DescribeAddonVersions",
 "s3:PutObject",
 "cloudformation:CreateStack",
 "cloudformation:DeleteStack",
 "cloudformation:DescribeStackResources",
 "cloudformation:DescribeStacks",
 "cloudformation:ListStackResources",
 "cloudformation:UpdateStack",
 "cloudformation:UpdateTerminationProtection",
 "ssm:PutParameter",
 "ssm:GetParameters",
 "ssm:GetParameter",
 "ssm:DeleteParameter",
 "ssm:AddTagsToResource",
 "ssm:ListTagsForResource",
 "ssm:RemoveTagsFromResource"
 ],
 "Resource": [
 "arn:aws:events:*:*:rule/tnb*",
 "arn:aws:codebuild:*:*:project/tnb*",
 "arn:aws:logs:*:*:log-group:/aws/tnb*",
 "arn:aws:s3:::tnb*",
 "arn:aws:eks:*:*:addon/tnb*/*/*",
 "arn:aws:eks:*:*:cluster/tnb*",
 "arn:aws:eks:*:*:nodegroup/tnb*/tnb*/*",
 "arn:aws:cloudformation:*:*:stack/tnb*",
 "arn:aws:ssm:*:*:parameter/tnb/*"
 ],
 "Effect": "Allow",
 "Sid": "TNBAccessInfraResourcePerms"
 },
 {
 "Sid": "CFNTemplatePerms",
 "Effect": "Allow",
 "Action": [
 "cloudformation:GetTemplateSummary"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ImageAMISSMPerms",
 "Effect": "Allow",
 "Action": [
 "ssm:GetParameters"
 ],
 "Resource": [
 "arn:aws:ssm:*::parameter/aws/service/eks/optimized-ami/*",
 "arn:aws:ssm:*::parameter/aws/service/bottlerocket/*"
 ]
 },
 {
 "Action": [
 "tag:GetResources"
 ],
 "Resource": "*",
 "Effect": "Allow",
 "Sid": "TaggingPolicy"
 },
 {
 "Action": [
 "outposts:GetOutpost"
 ],
 "Resource": "*",
 "Effect": "Allow",
 "Sid": "OutpostPolicy"
 }
 ]
}`

```

The following code shows the AWS TNB service trust policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "ec2.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "events.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "codebuild.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "eks.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "tnb.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

When you create an Amazon EKS resources in your NSD, you provide the
`cluster_role` attribute to specify which role will be used to
create your Amazon EKS cluster.

The following example shows a AWS CloudFormation template that creates a AWS TNB
service role for the Amazon EKS cluster policy.

```
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  TNBEKSClusterRole:
    Type: "AWS::IAM::Role"
    Properties:
      RoleName: "TNBEKSClusterRole"
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - eks.amazonaws.com
            Action:
              - "sts:AssumeRole"
      Path: /
      ManagedPolicyArns:
        - !Sub "arn:${AWS::Partition}:iam::aws:policy/AmazonEKSClusterPolicy"
```

For more information about IAM roles using AWS CloudFormation template, see the
following sections in the _AWS CloudFormation User Guide_:

- [AWS::IAM::Role](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md")
- [Selecting a stack template](../../../AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-template.md "../../../AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-template.md")
  When you create an Amazon EKS node group resources in your NSD, you provide the
  `node_role` attribute to specify which role will be used to create
  your Amazon EKS node group.

The following example shows a CloudFormation template that creates a AWS TNB service
role for the Amazon EKS node group policy.

```
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  TNBEKSNodeRole:
    Type: "AWS::IAM::Role"
    Properties:
      RoleName: "TNBEKSNodeRole"
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - ec2.amazonaws.com
            Action:
              - "sts:AssumeRole"
      Path: /
      ManagedPolicyArns:
        - !Sub "arn:${AWS::Partition}:iam::aws:policy/AmazonEKSWorkerNodePolicy"
        - !Sub "arn:${AWS::Partition}:iam::aws:policy/AmazonEKS_CNI_Policy"
        - !Sub "arn:${AWS::Partition}:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
        - !Sub "arn:${AWS::Partition}:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy"
      Policies:
        - PolicyName: EKSNodeRoleInlinePolicy
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action:
                  - "logs:DescribeLogStreams"
                  - "logs:PutLogEvents"
                  - "logs:CreateLogGroup"
                  - "logs:CreateLogStream"
                Resource: "arn:aws:logs:*:*:log-group:/aws/tnb/tnb*"
        - PolicyName: EKSNodeRoleIpv6CNIPolicy
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action:
                  - "ec2:AssignIpv6Addresses"
                Resource: "arn:aws:ec2:*:*:network-interface/*"
```

For more information about IAM roles using AWS CloudFormation template, see the
following sections in the _AWS CloudFormation User Guide_:

- [AWS::IAM::Role](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md")
- [Selecting a stack template](../../../AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-template.md "../../../AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-template.md")
  When you create an Amazon EKS resource in your NSD and you want to manage Multus as
  part of your deployment template, you must provide the `multus_role`
  attribute to specify which role will be used for managing Multus.

The following example shows a CloudFormation template that creates a AWS TNB service
role for a Multus policy.

```
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  TNBMultusRole:
    Type: "AWS::IAM::Role"
    Properties:
      RoleName: "TNBMultusRole"
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - events.amazonaws.com
            Action:
              - "sts:AssumeRole"
          - Effect: Allow
            Principal:
              Service:
                - codebuild.amazonaws.com
            Action:
              - "sts:AssumeRole"
      Path: /
      Policies:
        - PolicyName: MultusRoleInlinePolicy
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action:
                  - "codebuild:StartBuild"
                  - "logs:DescribeLogStreams"
                  - "logs:PutLogEvents"
                  - "logs:CreateLogGroup"
                  - "logs:CreateLogStream"
                Resource:
                  - "arn:aws:codebuild:*:*:project/tnb*"
                  - "arn:aws:logs:*:*:log-group:/aws/tnb/*"
              - Effect: Allow
                Action:
                  - "ec2:CreateNetworkInterface"
                  - "ec2:ModifyNetworkInterfaceAttribute"
                  - "ec2:AttachNetworkInterface"
                  - "ec2:DeleteNetworkInterface"
                  - "ec2:CreateTags"
                  - "ec2:DetachNetworkInterface"
                Resource: "*"
```

For more information about IAM roles using AWS CloudFormation template, see the
following sections in the _AWS CloudFormation User Guide_:

- [AWS::IAM::Role](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md")
- [Selecting a stack template](../../../AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-template.md "../../../AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-template.md")
  When your NSD or network function package uses a life-cycle
  hook, you need a service role to allow you to create an environment for
  execution of your life-cycle hooks.

###### Note

Your life-cycle hook policy
should be based on what your life-cycle hook is attempting to do.

The following example shows a CloudFormation template that creates a AWS TNB service
role for a life-cycle hook policy.

```
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  TNBHookRole:
    Type: "AWS::IAM::Role"
    Properties:
      RoleName: "TNBHookRole"
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - codebuild.amazonaws.com
            Action:
              - "sts:AssumeRole"
      Path: /
      ManagedPolicyArns:
        - !Sub "arn:${AWS::Partition}:iam::aws:policy/AdministratorAccess"
```

For more information about IAM roles using AWS CloudFormation template, see the
following sections in the _AWS CloudFormation User Guide_:

- [AWS::IAM::Role](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md")
- [Selecting a stack template](../../../AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-template.md "../../../AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-template.md")

## Allow users

to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```
