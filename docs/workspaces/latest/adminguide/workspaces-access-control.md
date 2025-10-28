# Identity and access management for WorkSpaces

By default, IAM users don't have permissions for WorkSpaces resources and operations. To allow
IAM users to manage WorkSpaces resources, you must create an IAM policy that explicitly grants
them permissions, and attach the policy to the IAM users or groups that require those
permissions.

###### Note

Amazon WorkSpaces doesn’t support the provisioning of IAM credentials into a WorkSpace (such as
with an instance profile).

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:

      + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the *IAM User Guide*.
      + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the *IAM User Guide*.

  Following are additional resources for IAM:

- For more information about IAM policies, see [Policies and Permissions](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the
  _IAM User Guide_ guide.
- For more information about IAM, see [Identity and
  Access Management (IAM)](https://aws.amazon.com/iam "https://aws.amazon.com/iam") and the [_IAM User Guide_](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").
- For more information about WorkSpaces-specific resources, actions, and condition context keys
  for use in IAM permission policies, see [Actions, Resources, and Condition Keys for
  Amazon WorkSpaces](../../../IAM/latest/UserGuide/list_amazonworkspaces.md "../../../IAM/latest/UserGuide/list_amazonworkspaces.md") in the _IAM User Guide_.
- For a tool that helps you create IAM policies, see the [AWS Policy Generator](https://aws.amazon.com/blogs/aws/aws-policy-generator/ "https://aws.amazon.com/blogs/aws/aws-policy-generator/"). You can also use the
  [IAM Policy Simulator](../../../IAM/latest/UsingPolicySimulatorGuide.md "../../../IAM/latest/UsingPolicySimulatorGuide.md") to test whether a policy would allow or deny a
  specific request to AWS.

###### Contents

- [Example policies](#workspaces-example-iam-policies "#workspaces-example-iam-policies")
- [Specify WorkSpaces resources in an IAM policy](#wsp_iam_resource "#wsp_iam_resource")
- [Create the workspaces_DefaultRole Role](#create-default-role "#create-default-role")
- [Create the AmazonWorkSpacesPCAAccess service
  role](#create-pca-access-role "#create-pca-access-role")
- [AWS managed policies for WorkSpaces](managed-policies.md "managed-policies.md")
- [Access to WorkSpaces and scripts on streaming instances](using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.md "using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.md")
- [Amazon WorkSpaces Console operations permissions reference](wsp-console-permissions-ref.md "wsp-console-permissions-ref.md")

## Example policies

The following examples show policy statements that you could use to control the
permissions that IAM users have to Amazon WorkSpaces.

The following policy statement grants an IAM user permission to perform WorkSpaces
personal and pools tasks.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ds:*",
 "workspaces:*",
 "application-autoscaling:DeleteScalingPolicy",
 "application-autoscaling:DeleteScheduledAction",
 "application-autoscaling:DeregisterScalableTarget",
 "application-autoscaling:DescribeScalableTargets",
 "application-autoscaling:DescribeScalingActivities",
 "application-autoscaling:DescribeScalingPolicies",
 "application-autoscaling:DescribeScheduledActions",
 "application-autoscaling:PutScalingPolicy",
 "application-autoscaling:PutScheduledAction",
 "application-autoscaling:RegisterScalableTarget",
 "cloudwatch:DeleteAlarms",
 "cloudwatch:DescribeAlarms",
 "cloudwatch:PutMetricAlarm",
 "ec2:AssociateRouteTable",
 "ec2:AttachInternetGateway",
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:CreateInternetGateway",
 "ec2:CreateNetworkInterface",
 "ec2:CreateRoute",
 "ec2:CreateRouteTable",
 "ec2:CreateSecurityGroup",
 "ec2:CreateSubnet",
 "ec2:CreateTags",
 "ec2:CreateVpc",
 "ec2:DeleteNetworkInterface",
 "ec2:DeleteSecurityGroup",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeInternetGateways",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:RevokeSecurityGroupEgress",
 "ec2:RevokeSecurityGroupIngress",
 "iam:AttachRolePolicy",
 "iam:CreatePolicy",
 "iam:CreateRole",
 "iam:GetRole",
 "iam:ListRoles",
 "iam:PutRolePolicy",
 "kms:ListAliases",
 "kms:ListKeys",
 "secretsmanager:ListSecrets",
 "tag:GetResources",
 "sso-directory:SearchUsers",
 "sso:CreateApplication",
 "sso:DeleteApplication",
 "sso:DescribeApplication",
 "sso:DescribeInstance",
 "sso:GetApplicationGrant",
 "sso:ListInstances",

 "sso:PutApplicationAssignmentConfiguration",
 "sso:PutApplicationAuthenticationMethod",
 "sso:PutApplicationGrant"
 ],
 "Resource": "*"
 },
 {
 "Sid": "iamPassRole",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "workspaces.amazonaws.com"
 }
 }
 }
 ]
}`

```

The following policy statement grants an IAM user permission to perform all
WorkSpaces Personal tasks.

Although Amazon WorkSpaces fully supports the `Action` and `Resource`
elements when using the API and command line tools, to use Amazon WorkSpaces from the AWS Management Console,
an IAM user must have permissions for the following actions and resources:

- Actions: `"ds:*"`
- Resources: `"Resource": "*"`
  The following example policy shows how to allow an IAM user to use Amazon WorkSpaces from
  the AWS Management Console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "workspaces:*",
 "ds:*",
 "iam:GetRole",
 "iam:CreateRole",
 "iam:PutRolePolicy",
 "iam:CreatePolicy",
 "iam:AttachRolePolicy",
 "iam:ListRoles",
 "kms:ListAliases",
 "kms:ListKeys",
 "ec2:CreateVpc",
 "ec2:CreateSubnet",
 "ec2:CreateNetworkInterface",
 "ec2:CreateInternetGateway",
 "ec2:CreateRouteTable",
 "ec2:CreateRoute",
 "ec2:CreateTags",
 "ec2:CreateSecurityGroup",
 "ec2:DescribeInternetGateways",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeRouteTables",
 "ec2:DescribeVpcs",
 "ec2:DescribeSubnets",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeAvailabilityZones",
 "ec2:AttachInternetGateway",
 "ec2:AssociateRouteTable",
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:DeleteSecurityGroup",
 "ec2:DeleteNetworkInterface",
 "ec2:RevokeSecurityGroupEgress",
 "ec2:RevokeSecurityGroupIngress",
 "secretsmanager:ListSecrets",
 "sso-directory:SearchUsers",
 "sso:CreateApplication",
 "sso:DeleteApplication",
 "sso:DescribeApplication",
 "sso:DescribeInstance",
 "sso:GetApplicationGrant",
 "sso:ListInstances",

 "sso:PutApplicationAssignmentConfiguration",
 "sso:PutApplicationAuthenticationMethod",
 "sso:PutApplicationGrant"
 ],
 "Resource": "*"
 },
 {
 "Sid": "iamPassRole",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "workspaces.amazonaws.com"
 }
 }
 }
 ]
}`

```

The following policy statement grants an IAM user permission to perform all
WorkSpaces Pools tasks.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "workspaces:*",
 "application-autoscaling:DeleteScalingPolicy",
 "application-autoscaling:DeleteScheduledAction",
 "application-autoscaling:DeregisterScalableTarget",
 "application-autoscaling:DescribeScalableTargets",
 "application-autoscaling:DescribeScalingActivities",
 "application-autoscaling:DescribeScalingPolicies",
 "application-autoscaling:DescribeScheduledActions",
 "application-autoscaling:PutScalingPolicy",
 "application-autoscaling:PutScheduledAction",
 "application-autoscaling:RegisterScalableTarget",
 "cloudwatch:DeleteAlarms",
 "cloudwatch:DescribeAlarms",
 "cloudwatch:PutMetricAlarm",
 "ec2:CreateSecurityGroup",
 "ec2:CreateTags",
 "ec2:DescribeInternetGateways",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "iam:AttachRolePolicy",
 "iam:CreatePolicy",
 "iam:CreateRole",
 "iam:GetRole",
 "iam:ListRoles",
 "iam:PutRolePolicy",
 "secretsmanager:ListSecrets",
 "tag:GetResources"
 ],
 "Resource": "*"
 },
 {
 "Sid": "iamPassRole",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "workspaces.amazonaws.com"
 }
 }
 },
 {
 "Action": "iam:CreateServiceLinkedRole",
 "Effect": "Allow",
 "Resource": "arn:aws:iam::*:role/aws-service-role/workspaces.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_WorkSpacesPool",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "workspaces.application-autoscaling.amazonaws.com"
 }
 }
 }
 ]
}`

```

The following policy statement grants an IAM user permission to perform all WorkSpaces
tasks, including those Amazon EC2 tasks necessary for creating Bring Your Own License (BYOL)
WorkSpaces.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ds:*",
 "workspaces:*",
 "ec2:AssociateRouteTable",
 "ec2:AttachInternetGateway",
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:CreateInternetGateway",
 "ec2:CreateNetworkInterface",
 "ec2:CreateRoute",
 "ec2:CreateRouteTable",
 "ec2:CreateSecurityGroup",
 "ec2:CreateSubnet",
 "ec2:CreateTags",
 "ec2:CreateVpc",
 "ec2:DeleteNetworkInterface",
 "ec2:DeleteSecurityGroup",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeImages",
 "ec2:DescribeInternetGateways",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:ModifyImageAttribute",
 "ec2:RevokeSecurityGroupEgress",
 "ec2:RevokeSecurityGroupIngress",
 "iam:CreateRole",
 "iam:GetRole",
 "iam:PutRolePolicy",
 "kms:ListAliases",
 "kms:ListKeys"
 ],
 "Resource": "*"
 },
 {
 "Sid": "iamPassRole",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "workspaces.amazonaws.com"
 }
 }
 }
 ]
}`

```

## Specify WorkSpaces resources in an IAM policy

To specify an WorkSpaces resource in the `Resource` element of the policy statement,
use the Amazon Resource Name (ARN) of the resource. You control access to your WorkSpaces resources
by either allowing or denying permissions to use the API actions that are specified in the
`Action` element of your IAM policy statement. WorkSpaces defines ARNs for WorkSpaces,
bundles, IP groups, and directories.

A WorkSpace ARN has the syntax shown in the following example.

```
arn:aws:workspaces:`region`:`account_id`:workspace/`workspace_identifier`
```

_region_

The Region that the WorkSpace is in (for example,
`us-east-1`).

_account_id_

The ID of the AWS account, with no hyphens (for example,
`123456789012`).

_workspace_identifier_

The ID of the WorkSpace (for example, `ws-a1bcd2efg`).

The following is the format of the `Resource` element of a policy statement
that identifies a specific WorkSpace.

```
"Resource": "arn:aws:workspaces:`region`:`account_id`:workspace/`workspace_identifier`"
```

You can use the `*` wildcard to specify all WorkSpaces that belong to a specific
account in a specific Region.

A WorkSpace pool ARN has the syntax shown in the following example.

```
arn:aws:workspaces:`region`:`account_id`:workspacespool/`workspacespool_identifier`
```

_region_

The Region that the WorkSpace is in (for example,
`us-east-1`).

_account_id_

The ID of the AWS account, with no hyphens (for example,
`123456789012`).

_workspacespool_identifier_

The ID of the WorkSpace pool (for example,
`ws-a1bcd2efg`).

The following is the format of the `Resource` element of a policy statement
that identifies a specific WorkSpace.

```
"Resource": "arn:aws:workspaces:`region`:`account_id`:workspacespool/`workspacespool_identifier`"
```

You can use the `*` wildcard to specify all WorkSpaces that belong to a specific
account in a specific Region.

A WorkSpace certificate ARN has the syntax shown in the following example.

```
arn:aws:workspaces:`region`:`account_id`:workspacecertificate/`workspacecertificateidentifier`
```

_region_

The Region that the WorkSpace is in (for example,
`us-east-1`).

_account_id_

The ID of the AWS account, with no hyphens (for example,
`123456789012`).

_workspacecertificate_identifier_

The ID of the WorkSpace certificate (for example,
`ws-a1bcd2efg`).

The following is the format of the `Resource` element of a policy statement that identifies a specific WorkSpace certificate.

```
"Resource": "arn:aws:workspaces:`region`:`account_id`:workspacecertificate/`workspacecertificate_identifier`"
```

You can use the `*` wildcard to specify all WorkSpaces that belong to a specific
account in a specific Region.

A WorkSpace image ARN has the syntax shown in the following example.

```
arn:aws:workspaces:`region`:`account_id`:workspaceimage/`image_identifier`
```

_region_

The Region that the WorkSpace image is in (for example,
`us-east-1`).

_account_id_

The ID of the AWS account, with no hyphens (for example,
`123456789012`).

_bundle_identifier_

The ID of the WorkSpace image (for example,
`wsi-a1bcd2efg`).

The following is the format of the `Resource` element of a policy statement
that identifies a specific image.

```
"Resource": "arn:aws:workspaces:`region`:`account_id`:workspaceimage/`image_identifier`"
```

You can use the `*` wildcard to specify all images that belong to a
specific account in a specific Region.

A bundle ARN has the syntax shown in the following example.

```
arn:aws:workspaces:`region`:`account_id`:workspacebundle/`bundle_identifier`
```

_region_

The Region that the WorkSpace is in (for example,
`us-east-1`).

_account_id_

The ID of the AWS account, with no hyphens (for example,
`123456789012`).

_bundle_identifier_

The ID of the WorkSpace bundle (for example,
`wsb-a1bcd2efg`).

The following is the format of the `Resource` element of a policy statement
that identifies a specific bundle.

```
"Resource": "arn:aws:workspaces:`region`:`account_id`:workspacebundle/`bundle_identifier`"
```

You can use the `*` wildcard to specify all bundles that belong to a
specific account in a specific Region.

An IP group ARN has the syntax shown in the following example.

```
arn:aws:workspaces:`region`:`account_id`:workspaceipgroup/`ipgroup_identifier`
```

_region_

The Region that the WorkSpace is in (for example,
`us-east-1`).

_account_id_

The ID of the AWS account, with no hyphens (for example,
`123456789012`).

_ipgroup_identifier_

The ID of the IP group (for example,
`wsipg-a1bcd2efg`).

The following is the format of the `Resource` element of a policy statement
that identifies a specific IP group.

```
"Resource": "arn:aws:workspaces:`region`:`account_id`:workspaceipgroup/`ipgroup_identifier`"
```

You can use the `*` wildcard to specify all IP groups that belong to a
specific account in a specific Region.

A directory ARN has the syntax shown in the following example.

```
arn:aws:workspaces:`region`:`account_id`:directory/`directory_identifier`
```

_region_

The Region that the WorkSpace is in (for example,
`us-east-1`).

_account_id_

The ID of the AWS account, with no hyphens (for example,
`123456789012`).

_directory_identifier_

The ID of the directory (for example,
`d-12345a67b8`).

The following is the format of the `Resource` element of a policy statement
that identifies a specific directory.

```
"Resource": "arn:aws:workspaces:`region`:`account_id`:directory/`directory_identifier`"
```

You can use the `*` wildcard to specify all directories that belong to a
specific account in a specific Region.

A connection alias ARN has the syntax shown in the following example.

```
arn:aws:workspaces:`region`:`account_id`:connectionalias/`connectionalias_identifier`
```

_region_

The Region that the connection alias is in (for example,
`us-east-1`).

_account_id_

The ID of the AWS account, with no hyphens (for example,
`123456789012`).

_connectionalias_identifier_

The ID of the connection alias (for example,
`wsca-12345a67b8`).

The following is the format of the `Resource` element of a policy statement
that identifies a specific connection alias.

```
"Resource": "arn:aws:workspaces:`region`:`account_id`:connectionalias/`connectionalias_identifier`"
```

You can use the `*` wildcard to specify all connection aliases that belong
to a specific account in a specific Region.

You can't specify a resource ARN with the following API actions:

- `AssociateIpGroups`
- `CreateIpGroup`
- `CreateTags`
- `DeleteTags`
- `DeleteWorkspaceImage`
- `DescribeAccount`
- `DescribeAccountModifications`
- `DescribeIpGroups`
- `DescribeTags`
- `DescribeWorkspaceDirectories`
- `DescribeWorkspaceImages`
- `DescribeWorkspaces`
- `DescribeWorkspacesConnectionStatus`
- `DisassociateIpGroups`
- `ImportWorkspaceImage`
- `ListAvailableManagementCidrRanges`
- `ModifyAccount`
  For API actions that don't support resource-level permissions, you must specify the
  resource statement shown in the following example.

```
"Resource": "*"
```

For the following API actions, you can't specify an account ID in the resource ARN
when the resource isn't owned by the account:

- `AssociateConnectionAlias`
- `CopyWorkspaceImage`
- `DisassociateConnectionAlias`
  For these API actions, you can specify an account ID in the resource ARN only when
  that account owns the resources to be acted upon. When the account doesn't own the
  resources, you must specify `*` for the account ID, as shown in the following
  example.

```
"arn:aws:workspaces:`region`:*:`resource_type`/`resource_identifier`"
```

## Create the workspaces_DefaultRole Role

Before you can register a directory using the API, you must verify that a role named
`workspaces_DefaultRole` exists. This role is created by the Quick Setup or if
you launch a WorkSpace using the AWS Management Console, and it grants Amazon WorkSpaces permission to access
specific AWS resources on your behalf. If this role does not exist, you can create it using
the following procedure.

###### To create the workspaces_DefaultRole role

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Roles**.
3. Choose **Create role**.
4. Under **Select type of trusted entity**, choose **Another
   AWS account**.
5. For **Account ID**, enter your account ID with no hyphens or
   spaces.
6. For **Options**, do not specify multi-factor authentication
   (MFA).
7. Choose **Next: Permissions**.
8. On the **Attach permissions policies** page, select the AWS managed
   policies **AmazonWorkSpacesServiceAccess**,
   **AmazonWorkSpacesSelfServiceAccess**, and
   **AmazonWorkSpacesPoolServiceAccess**. For more information about these
   managed policies, see [AWS managed policies for WorkSpaces](managed-policies.md "managed-policies.md").
9. Under **Set permissions boundary**, we recommend that you not use a
   permissions boundary because of the potential for conflicts with the policies that are
   attached to this role. Such conflicts could block certain necessary permissions for the
   role.
10. Choose **Next: Tags**.
11. On the **Add tags (optional)** page, add tags if needed.
12. Choose **Next: Review**.
13. On the **Review** page, for **Role name**, enter
    `workspaces_DefaultRole`.
14. (Optional) For **Role description**, enter a description.
15. Choose **Create Role**.
16. On the **Summary** page for the workspaces_DefaultRole role, choose
    the **Trust relationships** tab.
17. On the **Trust relationships** tab, choose **Edit trust
    relationship**.
18. On the **Edit Trust Relationship** page, replace the existing policy
    statement with the following statement.

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "workspaces.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

19. Choose **Update Trust Policy**.

## Create the AmazonWorkSpacesPCAAccess service

role

Before users can login using certificate-based authentication, you must verify that a role
named `AmazonWorkSpacesPCAAccess` exists. This role is created when you enable
certificate-based authentication on a Directory using the AWS Management Console, and it grants Amazon WorkSpaces
permission to access AWS Private CA resources on your behalf. If this role does not exist because you
are not using the console to manage certificate-based authentication, you can create it using
the following procedure.

###### To create the AmazonWorkSpacesPCAAccess service role using the AWS CLI

1. Create a JSON file named `AmazonWorkSpacesPCAAccess.json` with the
   following text.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "prod.euc.ecm.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. Adjust the `AmazonWorkSpacesPCAAccess.json` path as needed and run the
   following AWS CLI commands to create the service role and attach the [AmazonWorkspacesPCAAccess](managed-policies.md#workspaces-pca-access "managed-policies.md#workspaces-pca-access") managed policy.

```
aws iam create-role --path /service-role/ --role-name AmazonWorkSpacesPCAAccess --assume-role-policy-document file://AmazonWorkSpacesPCAAccess.json
```

```
aws iam attach-role-policy —role-name AmazonWorkSpacesPCAAccess —policy-arn arn:aws:iam::aws:policy/AmazonWorkspacesPCAAccess
```
