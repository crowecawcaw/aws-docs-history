# Configure EMR Studio user permissions for

Amazon EC2 or Amazon EKS

You must configure user permissions policies for Amazon EMR Studio so that you can set
fine-grained user and group permissions. For information about how user permissions work in
EMR Studio, see [Access control](how-emr-studio-works.md#emr-studio-access-control "how-emr-studio-works.md#emr-studio-access-control") in [How Amazon EMR Studio works](how-emr-studio-works.md "how-emr-studio-works.md").

###### Note

The permissions covered in this section don't enforce data access control. To manage
access to input datasets, you should configure permissions for the clusters that your
Studio uses. For more information, see [Security in Amazon EMR](emr-security.md "emr-security.md").

## Create an EMR Studio user role for IAM Identity Center

authentication mode

You must create an EMR Studio user role when you use IAM Identity Center authentication mode.

###### To create a user role for EMR Studio

1. Follow the instructions in [Creating a role to
   delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _AWS Identity and Access Management User
   Guide_ to create a user role.

When you create the role, use the following trust relationship policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole",
 "sts:SetContext"
 ],
 "Resource": "arn:aws:iam::123456789012:role/EMRStudioServiceRole",
 "Sid": "AllowSTSAssumerole"
 }
 ]
}`

```

2. Remove the default role permissions and policies.
3. Before you assign users and groups to a Studio, attach your EMR Studio
   session policies to the user role. For instructions on how to create session policies,
   see [Create permissions policies for
   EMR Studio users](#emr-studio-permissions-policies "#emr-studio-permissions-policies").

## Create permissions policies for

EMR Studio users

Refer to the following sections to create permissions policies for
EMR Studio.

###### Topics

- [Create the permissions
  policies](#emr-studio-permissions-policies-create "#emr-studio-permissions-policies-create")
- [Set ownership for
  Workspace collaboration](#emr-studio-workspace-collaboration-permissions "#emr-studio-workspace-collaboration-permissions")
- [Create user-level Git secrets
  policy](#emr-studio-permissions-policies-git "#emr-studio-permissions-policies-git")
- [Attach the permissions policy
  to your IAM identity](#emr-studio-permissions-policies-attach "#emr-studio-permissions-policies-attach")

###### Note

To set Amazon S3 access permissions for storing notebook files, and to set
AWS Secrets Manager access permissions to read secrets when you link
Workspaces to Git repositories, use the EMR Studio service role.

### Create the permissions

policies

Create one or more IAM permissions policies that specify what actions a user can
take in your Studio. For example, you can create three separate policies for
basic, intermediate, and advanced Studio user
types with the example policies on this page.

For a breakdown of each Studio operation that a user might perform, and the
minimum IAM actions that are required to perform each operation, see [AWS Identity and Access Management permissions for
EMR Studio users](#emr-studio-iam-permissions-table "#emr-studio-iam-permissions-table"). For steps to create the policies,
see [Creating IAM
policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the _IAM User Guide_.

Your permissions policy must include the following statements.

```
{
            "Sid": "AllowAddingTagsOnSecretsWithEMRStudioPrefix",
            "Effect": "Allow",
            "Action": "secretsmanager:TagResource",
            "Resource": "arn:aws:secretsmanager:*:*:secret:emr-studio-*"
},
{
            "Sid": "AllowPassingServiceRoleForWorkspaceCreation",
            "Action": "iam:PassRole",
            "Resource": [
                "arn:aws:iam::*:role/`your-emr-studio-service-role`"
            ],
            "Effect": "Allow"
}
```

### Set ownership for

Workspace collaboration

Workspace collaboration lets multiple users work simultaneously in the same
Workspace and can be configured with the **Collaboration**
panel in the Workspace UI. In order to see and use the
**Collaboration** panel, a user must have the following permissions.
Any user with these permissions can see and use the **Collaboration**
panel.

```
"elasticmapreduce:UpdateEditor",
"elasticmapreduce:PutWorkspaceAccess",
"elasticmapreduce:DeleteWorkspaceAccess",
"elasticmapreduce:ListWorkspaceAccessIdentities"
```

To restrict access to the **Collaboration** panel, you can use
tag-based access control. When a user creates a Workspace, EMR Studio
applies a default tag with a key of `creatorUserId` whose value is the ID of
the user creating the Workspace.

###### Note

EMR Studio adds the `creatorUserId` tag to Workspaces
created after November 16, 2021. To restrict who can configure collaboration for
workspaces that you created before this date, we recommend that you manually add the
`creatorUserId` tag to your Workspace, and then use tag-based
access control in your user permissions policies.

The following example statement allows a user to configure collaboration for any
Workspace with the tag key `creatorUserId` whose value matches the
user's ID (indicated by the policy variable `aws:userId`). In other words,
the statement lets a user configure collaboration for the Workspaces that they
create. To learn more about policy variables, see [IAM policy elements:
Variables and tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the _IAM User Guide_.

```
    {
        "Sid": "UserRolePermissionsForCollaboration",
        "Action": [
            "elasticmapreduce:UpdateEditor",
            "elasticmapreduce:PutWorkspaceAccess",
            "elasticmapreduce:DeleteWorkspaceAccess",
            "elasticmapreduce:ListWorkspaceAccessIdentities"
        ],
        "Resource": "*",
        "Effect": "Allow",
        "Condition": {
            "StringEquals": {
                "elasticmapreduce:ResourceTag/creatorUserId": "${aws:userid}"
            }
        }
    }
```

### Create user-level Git secrets

policy

###### Topics

- [To use user-level
  permissions](#emr-studio-permissions-policies-user "#emr-studio-permissions-policies-user")
- [To transition from
  service-level permissions to user-level permissions](#emr-studio-permissions-policies-transition "#emr-studio-permissions-policies-transition")
- [To use service-level
  permissions](#emr-studio-permissions-policies-service "#emr-studio-permissions-policies-service")

#### To use user-level

permissions

EMR Studio automatically adds the
`for-use-with-amazon-emr-managed-user-policies` tag when it creates Git
secrets. If you want to control access to Git secrets at the user level, add tag-based
permissions to the EMR Studio **user role policy**
with `secretsmanager:GetSecretValue` as shown in the [To transition from
service-level permissions to user-level permissions](#emr-studio-permissions-policies-transition "#emr-studio-permissions-policies-transition") section below.

If you have existing permissions for `secretsmanager:GetSecretValue` in
the EMR Studio **service role policy**, you should
remove those permissions.

#### To transition from

service-level permissions to user-level permissions

###### Note

The `for-use-with-amazon-emr-managed-user-policies` tag ensures that
the permissions from **Step 1** below grant the creator of the
workspace access to the Git secret. However, if you linked Git repositories before
September 1, 2023, then the corresponding Git secrets will be denied access because
they don't have the `for-use-with-amazon-emr-managed-user-policies` tag
applied. To apply user-level permissions, you must recreate the old secrets from
JupyterLab and link the appropriate Git repositories again.

For more information about policy variables, see [IAM policy
elements: Variables and tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the
_IAM User Guide_.

1. Add the following permissions to the the [EMR Studio user role
   policy](emr-studio-service-role.md "emr-studio-service-role.md"). It uses the
   `for-use-with-amazon-emr-managed-user-policies` key with value
   `"${aws:`userid`}"`.

```
{
   "Sid": "AllowSecretsManagerReadOnlyActionsWithEMRTags",
    "Effect": "Allow",
    "Action": "secretsmanager:GetSecretValue",
    "Resource": "arn:aws:secretsmanager:*:*:`secret`:*",
    "Condition": {
        "StringEquals": {
            "secretsmanager:ResourceTag/for-use-with-amazon-emr-managed-user-policies": "${aws:`userid`}"
        }
    }
}
```

2. If present, remove the following permission from the [EMR Studio service
   role policy](emr-studio-service-role.md "emr-studio-service-role.md"). Because the service role policy applies to all
   secrets defined by each user, you only need to do this one time.

```
{
    "Sid": "AllowSecretsManagerReadOnlyActionsWithEMRTags",
    "Effect": "Allow",
    "Action": [
        "secretsmanager:GetSecretValue"
     ],
    "Resource": "arn:aws:secretsmanager:*:*:`secret`:*",
    "Condition": {
        "StringEquals": {
            "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
        }
    }
}
```

#### To use service-level

permissions

As of September 1, 2023, EMR Studio automatically adds the
`for-use-with-amazon-emr-managed-user-policies` tag for user-level access
control. Because this is an added capability, you can continue to use service-level
access that's available through the `GetSecretValue` permission in the
[EMR Studio service role](emr-studio-service-role.md "emr-studio-service-role.md").

For secrets created before September 1, 2023, EMR Studio didn't add the
`for-use-with-amazon-emr-managed-user-policies` tag. To keep using
service-level permissions, simply retain your existing [EMR Studio service role](emr-studio-service-role.md "emr-studio-service-role.md") and user role
permissions. However, to restrict who can access an individual secret, we recommend
that you follow the steps in [To use user-level
permissions](#emr-studio-permissions-policies-user "#emr-studio-permissions-policies-user") to manually add the
`for-use-with-amazon-emr-managed-user-policies` tag to your secrets, and
then use tag-based access control in your user permissions policies.

For more information about policy variables, see [IAM policy elements:
Variables and tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the _IAM User Guide_.

### Attach the permissions policy

to your IAM identity

The following table summarizes which IAM identity you attach a permissions policy
to, depending on your EMR Studio authentication mode. For instructions on how to
attach a policy, see [Adding and
removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").

| If you use...                                           | Attach the policy to...                                                                                                                                                                                                             |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IAM authentication                                      | Your IAM identities (users, groups of users, or roles). For example, you<br>can attach a permissions policy to a user in your AWS account.                                                                                          |
| IAM federation with an external identity provider (IdP) | The IAM role or roles that you create for your external IdP. For<br>example, an IAM for SAML 2.0 federation.<br>EMR Studio uses the permissions that you attach to your IAM role(s)<br>for users with federated access to a Studio. |
| IAM Identity Center                                     | Your Amazon EMR Studio user role.                                                                                                                                                                                                   |

## Example user policies

The following basic user policy allows most EMR Studio actions, but does not let a
user create new Amazon EMR clusters.

###### Important

The example policy does not include the `CreateStudioPresignedUrl` permission, which you must allow for a user when you use IAM authentication mode. For more information, see [Assign a user or group to an
EMR Studio](emr-studio-manage-users.md#emr-studio-assign-users-groups "emr-studio-manage-users.md#emr-studio-assign-users-groups").

The example policy includes `Condition` elements to enforce tag-based access
control (TBAC) so that you can use the policy with the example service role for EMR Studio. For more
information, see [Create an EMR Studio service role](emr-studio-service-role.md "emr-studio-service-role.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowDefaultEC2SecurityGroupsCreationInVPCWithEMRTags",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateSecurityGroup"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:vpc/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "AllowAddingEMRTagsDuringDefaultSecurityGroupCreation",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:security-group/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/for-use-with-amazon-emr-managed-policies": "true",
 "ec2:CreateAction": "CreateSecurityGroup"
 }
 }
 },
 {
 "Sid": "AllowSecretManagerListSecrets",
 "Action": [
 "secretsmanager:ListSecrets"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowSecretCreationWithEMRTagsAndEMRStudioPrefix",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:CreateSecret"
 ],
 "Resource": [
 "arn:aws:secretsmanager:*:*:secret:emr-studio-*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "AllowAddingTagsOnSecretsWithEMRStudioPrefix",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:TagResource"
 ],
 "Resource": [
 "arn:aws:secretsmanager:*:*:secret:emr-studio-*"
 ]
 },
 {
 "Sid": "AllowPassingServiceRoleForWorkspaceCreation",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/`your-emr-studio-service-role>`"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowS3ListAndLocationPermissions",
 "Action": [
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowS3ReadOnlyAccessToLogs",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::aws-logs-`aws-111122223333>`-`region>`/elasticmapreduce/*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowConfigurationForWorkspaceCollaboration",
 "Action": [
 "elasticmapreduce:UpdateEditor",
 "elasticmapreduce:PutWorkspaceAccess",
 "elasticmapreduce:DeleteWorkspaceAccess",
 "elasticmapreduce:ListWorkspaceAccessIdentities"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow",
 "Condition": {
 "StringEquals": {
 "elasticmapreduce:ResourceTag/creatorUserId": "${aws:userId}"
 }
 }
 },
 {
 "Sid": "DescribeNetwork",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeVpcs",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "ListIAMRoles",
 "Effect": "Allow",
 "Action": [
 "iam:ListRoles"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

The following intermediate user policy allows most EMR Studio actions, and lets a
user create new Amazon EMR clusters using a cluster template.

###### Important

The example policy does not include the `CreateStudioPresignedUrl` permission, which you must allow for a user when you use IAM authentication mode. For more information, see [Assign a user or group to an
EMR Studio](emr-studio-manage-users.md#emr-studio-assign-users-groups "emr-studio-manage-users.md#emr-studio-assign-users-groups").

The example policy includes `Condition` elements to enforce tag-based access
control (TBAC) so that you can use the policy with the example service role for EMR Studio. For more
information, see [Create an EMR Studio service role](emr-studio-service-role.md "emr-studio-service-role.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowEMRBasicActions",
 "Action": [
 "elasticmapreduce:CreateEditor",
 "elasticmapreduce:DescribeEditor",
 "elasticmapreduce:ListEditors",
 "elasticmapreduce:StartEditor",
 "elasticmapreduce:StopEditor",
 "elasticmapreduce:DeleteEditor",
 "elasticmapreduce:OpenEditorInConsole",
 "elasticmapreduce:AttachEditor",
 "elasticmapreduce:DetachEditor",
 "elasticmapreduce:CreateRepository",
 "elasticmapreduce:DescribeRepository",
 "elasticmapreduce:DeleteRepository",
 "elasticmapreduce:ListRepositories",
 "elasticmapreduce:LinkRepository",
 "elasticmapreduce:UnlinkRepository",
 "elasticmapreduce:DescribeCluster",
 "elasticmapreduce:ListInstanceGroups",
 "elasticmapreduce:ListBootstrapActions",
 "elasticmapreduce:ListClusters",
 "elasticmapreduce:ListSteps",
 "elasticmapreduce:CreatePersistentAppUI",
 "elasticmapreduce:DescribePersistentAppUI",
 "elasticmapreduce:GetPersistentAppUIPresignedURL",
 "elasticmapreduce:GetOnClusterAppUIPresignedURL"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowEMRContainersBasicActions",
 "Action": [
 "emr-containers:DescribeVirtualCluster",
 "emr-containers:ListVirtualClusters",
 "emr-containers:DescribeManagedEndpoint",
 "emr-containers:ListManagedEndpoints",
 "emr-containers:DescribeJobRun",
 "emr-containers:ListJobRuns"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowRetrievingManagedEndpointCredentials",
 "Effect": "Allow",
 "Action": [
 "emr-containers:GetManagedEndpointSessionCredentials"
 ],
 "Resource": [
 "arn:aws:emr-containers:us-west-1:123456789012:/virtualclusters/virtual-cluster-id/endpoints/managed-endpoint-id"
 ],
 "Condition": {
 "StringEquals": {
 "emr-containers:ExecutionRoleArn": [
 "arn:aws:iam::123456789012:role/emr-on-eks-execution-role"
 ]
 }
 }
 },
 {
 "Sid": "AllowSecretManagerListSecrets",
 "Action": [
 "secretsmanager:ListSecrets"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowSecretCreationWithEMRTagsAndEMRStudioPrefix",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:CreateSecret"
 ],
 "Resource": [
 "arn:aws:secretsmanager:*:*:secret:emr-studio-*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "AllowAddingTagsOnSecretsWithEMRStudioPrefix",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:TagResource"
 ],
 "Resource": [
 "arn:aws:secretsmanager:*:*:secret:emr-studio-*"
 ]
 },
 {
 "Sid": "AllowClusterTemplateRelatedIntermediateActions",
 "Action": [
 "servicecatalog:DescribeProduct",
 "servicecatalog:DescribeProductView",
 "servicecatalog:DescribeProvisioningParameters",
 "servicecatalog:ProvisionProduct",
 "servicecatalog:SearchProducts",
 "servicecatalog:UpdateProvisionedProduct",
 "servicecatalog:ListProvisioningArtifacts",
 "servicecatalog:ListLaunchPaths",
 "servicecatalog:DescribeRecord",
 "cloudformation:DescribeStackResources"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowPassingServiceRoleForWorkspaceCreation",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/your-emr-studio-service-role"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowS3ListAndLocationPermissions",
 "Action": [
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowS3ReadOnlyAccessToLogs",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::aws-logs-123456789012-us-east-1/elasticmapreduce/*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowConfigurationForWorkspaceCollaboration",
 "Action": [
 "elasticmapreduce:UpdateEditor",
 "elasticmapreduce:PutWorkspaceAccess",
 "elasticmapreduce:DeleteWorkspaceAccess",
 "elasticmapreduce:ListWorkspaceAccessIdentities"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow",
 "Condition": {
 "StringEquals": {
 "elasticmapreduce:ResourceTag/creatorUserId": "${aws:userId}"
 }
 }
 },
 {
 "Sid": "DescribeNetwork",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeVpcs",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "ListIAMRoles",
 "Effect": "Allow",
 "Action": [
 "iam:ListRoles"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AllowServerlessActions",
 "Action": [
 "emr-serverless:CreateApplication",
 "emr-serverless:UpdateApplication",
 "emr-serverless:DeleteApplication",
 "emr-serverless:ListApplications",
 "emr-serverless:GetApplication",
 "emr-serverless:StartApplication",
 "emr-serverless:StopApplication",
 "emr-serverless:StartJobRun",
 "emr-serverless:CancelJobRun",
 "emr-serverless:ListJobRuns",
 "emr-serverless:GetJobRun",
 "emr-serverless:GetDashboardForJobRun",
 "emr-serverless:AccessInteractiveEndpoints"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowPassingRuntimeRoleForRunningServerlessJob",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/serverless-runtime-role"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

The following advanced user policy allows all EMR Studio actions, and lets a user
create new Amazon EMR clusters using a cluster template or by providing a cluster
configuration.

###### Important

The example policy does not include the `CreateStudioPresignedUrl` permission, which you must allow for a user when you use IAM authentication mode. For more information, see [Assign a user or group to an
EMR Studio](emr-studio-manage-users.md#emr-studio-assign-users-groups "emr-studio-manage-users.md#emr-studio-assign-users-groups").

The example policy includes `Condition` elements to enforce tag-based access
control (TBAC) so that you can use the policy with the example service role for EMR Studio. For more
information, see [Create an EMR Studio service role](emr-studio-service-role.md "emr-studio-service-role.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowEMRBasicActions",
 "Action": [
 "elasticmapreduce:CreateEditor",
 "elasticmapreduce:DescribeEditor",
 "elasticmapreduce:ListEditors",
 "elasticmapreduce:StartEditor",
 "elasticmapreduce:StopEditor",
 "elasticmapreduce:DeleteEditor",
 "elasticmapreduce:OpenEditorInConsole",
 "elasticmapreduce:AttachEditor",
 "elasticmapreduce:DetachEditor",
 "elasticmapreduce:CreateRepository",
 "elasticmapreduce:DescribeRepository",
 "elasticmapreduce:DeleteRepository",
 "elasticmapreduce:ListRepositories",
 "elasticmapreduce:LinkRepository",
 "elasticmapreduce:UnlinkRepository",
 "elasticmapreduce:DescribeCluster",
 "elasticmapreduce:ListInstanceGroups",
 "elasticmapreduce:ListBootstrapActions",
 "elasticmapreduce:ListClusters",
 "elasticmapreduce:ListSteps",
 "elasticmapreduce:CreatePersistentAppUI",
 "elasticmapreduce:DescribePersistentAppUI",
 "elasticmapreduce:GetPersistentAppUIPresignedURL",
 "elasticmapreduce:GetOnClusterAppUIPresignedURL"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowEMRContainersBasicActions",
 "Action": [
 "emr-containers:DescribeVirtualCluster",
 "emr-containers:ListVirtualClusters",
 "emr-containers:DescribeManagedEndpoint",
 "emr-containers:ListManagedEndpoints",
 "emr-containers:DescribeJobRun",
 "emr-containers:ListJobRuns"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowRetrievingManagedEndpointCredentials",
 "Effect": "Allow",
 "Action": [
 "emr-containers:GetManagedEndpointSessionCredentials"
 ],
 "Resource": [
 "arn:aws:emr-containers:*:123456789012:/virtualclusters/virtual-cluster-id/endpoints/managed-endpoint-id"
 ],
 "Condition": {
 "StringEquals": {
 "emr-containers:ExecutionRoleArn": [
 "arn:aws:iam::123456789012:role/emr-on-eks-execution-role"
 ]
 }
 }
 },
 {
 "Sid": "AllowSecretManagerListSecrets",
 "Action": [
 "secretsmanager:ListSecrets"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowSecretCreationWithEMRTagsAndEMRStudioPrefix",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:CreateSecret"
 ],
 "Resource": [
 "arn:aws:secretsmanager:*:*:secret:emr-studio-*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/for-use-with-amazon-emr-managed-policies": "true"
 }
 }
 },
 {
 "Sid": "AllowAddingTagsOnSecretsWithEMRStudioPrefix",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:TagResource"
 ],
 "Resource": [
 "arn:aws:secretsmanager:*:*:secret:emr-studio-*"
 ]
 },
 {
 "Sid": "AllowClusterTemplateRelatedIntermediateActions",
 "Action": [
 "servicecatalog:DescribeProduct",
 "servicecatalog:DescribeProductView",
 "servicecatalog:DescribeProvisioningParameters",
 "servicecatalog:ProvisionProduct",
 "servicecatalog:SearchProducts",
 "servicecatalog:UpdateProvisionedProduct",
 "servicecatalog:ListProvisioningArtifacts",
 "servicecatalog:ListLaunchPaths",
 "servicecatalog:DescribeRecord",
 "cloudformation:DescribeStackResources"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowEMRCreateClusterAdvancedActions",
 "Action": [
 "elasticmapreduce:RunJobFlow"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowPassingServiceRoleForWorkspaceCreation",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/your-emr-studio-service-role",
 "arn:aws:iam::*:role/EMR_DefaultRole_V2",
 "arn:aws:iam::*:role/EMR_EC2_DefaultRole"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowS3ListAndLocationPermissions",
 "Action": [
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowS3ReadOnlyAccessToLogs",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::aws-logs-123456789012-us-east-1/elasticmapreduce/*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowConfigurationForWorkspaceCollaboration",
 "Action": [
 "elasticmapreduce:UpdateEditor",
 "elasticmapreduce:PutWorkspaceAccess",
 "elasticmapreduce:DeleteWorkspaceAccess",
 "elasticmapreduce:ListWorkspaceAccessIdentities"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow",
 "Condition": {
 "StringEquals": {
 "elasticmapreduce:ResourceTag/creatorUserId": "${aws:userId}"
 }
 }
 },
 {
 "Sid": "SageMakerDataWranglerForEMRStudio",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreatePresignedDomainUrl",
 "sagemaker:DescribeDomain",
 "sagemaker:ListDomains",
 "sagemaker:ListUserProfiles"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "DescribeNetwork",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeVpcs",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "ListIAMRoles",
 "Effect": "Allow",
 "Action": [
 "iam:ListRoles"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AllowServerlessActions",
 "Action": [
 "emr-serverless:CreateApplication",
 "emr-serverless:UpdateApplication",
 "emr-serverless:DeleteApplication",
 "emr-serverless:ListApplications",
 "emr-serverless:GetApplication",
 "emr-serverless:StartApplication",
 "emr-serverless:StopApplication",
 "emr-serverless:StartJobRun",
 "emr-serverless:CancelJobRun",
 "emr-serverless:ListJobRuns",
 "emr-serverless:GetJobRun",
 "emr-serverless:GetDashboardForJobRun",
 "emr-serverless:AccessInteractiveEndpoints"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowPassingRuntimeRoleForRunningServerlessJob",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/serverless-runtime-role"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowCodeWhisperer",
 "Effect": "Allow",
 "Action": [
 "codewhisperer:GenerateRecommendations"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AllowAthenaSQL",
 "Action": [
 "athena:StartQueryExecution",
 "athena:StopQueryExecution",
 "athena:GetQueryExecution",
 "athena:GetQueryRuntimeStatistics",
 "athena:GetQueryResults",
 "athena:ListQueryExecutions",
 "athena:BatchGetQueryExecution",
 "athena:GetNamedQuery",
 "athena:ListNamedQueries",
 "athena:BatchGetNamedQuery",
 "athena:UpdateNamedQuery",
 "athena:DeleteNamedQuery",
 "athena:ListDataCatalogs",
 "athena:GetDataCatalog",
 "athena:ListDatabases",
 "athena:GetDatabase",
 "athena:ListTableMetadata",
 "athena:GetTableMetadata",
 "athena:ListWorkGroups",
 "athena:GetWorkGroup",
 "athena:CreateNamedQuery",
 "athena:GetPreparedStatement",
 "glue:CreateDatabase",
 "glue:DeleteDatabase",
 "glue:GetDatabase",
 "glue:GetDatabases",
 "glue:UpdateDatabase",
 "glue:CreateTable",
 "glue:DeleteTable",
 "glue:BatchDeleteTable",
 "glue:UpdateTable",
 "glue:GetTable",
 "glue:GetTables",
 "glue:BatchCreatePartition",
 "glue:CreatePartition",
 "glue:DeletePartition",
 "glue:BatchDeletePartition",
 "glue:UpdatePartition",
 "glue:GetPartition",
 "glue:GetPartitions",
 "glue:BatchGetPartition",
 "kms:ListAliases",
 "kms:ListKeys",
 "kms:DescribeKey",
 "lakeformation:GetDataAccess",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:ListBucketMultipartUploads",
 "s3:ListMultipartUploadParts",
 "s3:AbortMultipartUpload",
 "s3:PutObject",
 "s3:PutBucketPublicAccessBlock",
 "s3:ListAllMyBuckets"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

The following user policy contains the minimum user permissions that are required to
use an EMR Serverless interactive application with EMR Studio
Workspaces.

In this example policy that has user permissions for EMR Serverless interactive
applications with EMR Studio, replace the placeholders for
`serverless-runtime-role` and
`emr-studio-service-role` with your correct [EMR Studio service role](emr-studio-service-role.md "emr-studio-service-role.md") and [EMR Serverless runtime role](../EMR-Serverless-UserGuide/security-iam-runtime-role.md "../EMR-Serverless-UserGuide/security-iam-runtime-role.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowServerlessActions",
 "Action": [
 "emr-serverless:CreateApplication",
 "emr-serverless:UpdateApplication",
 "emr-serverless:DeleteApplication",
 "emr-serverless:ListApplications",
 "emr-serverless:GetApplication",
 "emr-serverless:StartApplication",
 "emr-serverless:StopApplication",
 "emr-serverless:StartJobRun",
 "emr-serverless:CancelJobRun",
 "emr-serverless:ListJobRuns",
 "emr-serverless:GetJobRun",
 "emr-serverless:GetDashboardForJobRun",
 "emr-serverless:AccessInteractiveEndpoints"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowEMRBasicActions",
 "Action": [
 "elasticmapreduce:CreateEditor",
 "elasticmapreduce:DescribeEditor",
 "elasticmapreduce:ListEditors",
 "elasticmapreduce:UpdateStudio",
 "elasticmapreduce:StartEditor",
 "elasticmapreduce:StopEditor",
 "elasticmapreduce:DeleteEditor",
 "elasticmapreduce:OpenEditorInConsole",
 "elasticmapreduce:AttachEditor",
 "elasticmapreduce:DetachEditor",
 "elasticmapreduce:CreateStudio",
 "elasticmapreduce:DescribeStudio",
 "elasticmapreduce:DeleteStudio",
 "elasticmapreduce:ListStudios",
 "elasticmapreduce:CreateStudioPresignedUrl"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowPassingRuntimeRoleForRunningEMRServerlessJob",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/`serverless-runtime-role`"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowPassingServiceRoleForWorkspaceCreation",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/`emr-studio-service-role`"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "AllowS3ListAndGetPermissions",
 "Action": [
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:GetBucketLocation",
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "DescribeNetwork",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeVpcs",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "ListIAMRoles",
 "Effect": "Allow",
 "Action": [
 "iam:ListRoles"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## AWS Identity and Access Management permissions for

EMR Studio users

The following table includes each Amazon EMR Studio operation that a user might perform,
and lists the minimum IAM actions needed to perform that operation. You allow these
actions in your IAM permissions policies (when you use IAM authentication) or in your
user role session policies (when you use IAM Identity Center authentication) for EMR Studio.

The table also displays the operations allowed in each of example permissions policy
for EMR Studio. For more information about the example permissions policies, see [Create permissions policies for
EMR Studio users](#emr-studio-permissions-policies "#emr-studio-permissions-policies").

| Action                                                                                                                                                                                                                                                                                                                                                                                                                                                | Basic | Intermediate | Advanced | Associated actions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create and delete Workspaces                                                                                                                                                                                                                                                                                                                                                                                                                          | Yes   | Yes          | Yes      | `<br>"elasticmapreduce:CreateEditor",<br>"elasticmapreduce:DescribeEditor",<br>"elasticmapreduce:ListEditors",<br>"elasticmapreduce:DeleteEditor"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| View the \*_Collaboration_<br>• panel, enable<br>Workspace collaboration, and add collaborators. For more information, see<br>[Set ownership for<br>Workspace collaboration](#emr-studio-workspace-collaboration-permissions "#emr-studio-workspace-collaboration-permissions").                                                                                                                                                                      | Yes   | Yes          | Yes      | `<br>"elasticmapreduce:UpdateEditor",<br>"elasticmapreduce:PutWorkspaceAccess",<br>"elasticmapreduce:DeleteWorkspaceAccess",<br>"elasticmapreduce:ListWorkspaceAccessIdentities"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| See a list of Amazon S3 Control storage buckets in the same account<br>as the Studio when creating a new EMR cluster, and access container logs<br>when using a web UI to debug applications                                                                                                                                                                                                                                                          | Yes   | Yes          | Yes      | `<br>"s3:ListAllMyBuckets",<br>"s3:ListBucket",<br>"s3:GetBucketLocation",<br>"s3:GetObject"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Access Workspaces                                                                                                                                                                                                                                                                                                                                                                                                                                     | Yes   | Yes          | Yes      | `<br>"elasticmapreduce:DescribeEditor",<br>"elasticmapreduce:ListEditors",<br>"elasticmapreduce:StartEditor",<br>"elasticmapreduce:StopEditor",<br>"elasticmapreduce:OpenEditorInConsole"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Attach or detach existing Amazon EMR clusters associated with the<br>Workspace                                                                                                                                                                                                                                                                                                                                                                        | Yes   | Yes          | Yes      | `<br>"elasticmapreduce:AttachEditor",<br>"elasticmapreduce:DetachEditor",<br>"elasticmapreduce:ListClusters",<br>"elasticmapreduce:DescribeCluster",<br>"elasticmapreduce:ListInstanceGroups",<br>"elasticmapreduce:ListBootstrapActions"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Attach or detach Amazon EMR on EKS clusters                                                                                                                                                                                                                                                                                                                                                                                                           | Yes   | Yes          | Yes      | `<br>"elasticmapreduce:AttachEditor",<br>"elasticmapreduce:DetachEditor",<br>"emr-containers:ListVirtualClusters",<br>"emr-containers:DescribeVirtualCluster",<br>"emr-containers:ListManagedEndpoints",<br>"emr-containers:DescribeManagedEndpoint",<br>"emr-containers:GetManagedEndpointSessionCredentials"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Attach or detach EMR Serverless applications that are associated with the<br>Workspace                                                                                                                                                                                                                                                                                                                                                                | No    | Yes          | Yes      | `<br>"elasticmapreduce:AttachEditor",<br>"elasticmapreduce:DetachEditor",<br>"emr-serverless:GetApplication",<br>"emr-serverless:StartApplication",<br>"emr-serverless:ListApplications",<br>"emr-serverless:GetDashboardForJobRun",<br>"emr-serverless:AccessInteractiveEndpoints",<br>"iam:PassRole"<br>`<br>The `PassRole` permission is required to pass the EMR Serverless<br>job runtime role. For more information, see [Job<br>runtime roles](../EMR-Serverless-UserGuide/security-iam-runtime-role.md "../EMR-Serverless-UserGuide/security-iam-runtime-role.md") in the _Amazon EMR Serverless User<br>Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Debug Amazon EMR on EC2 jobs with persistent application user interfaces                                                                                                                                                                                                                                                                                                                                                                              | Yes   | Yes          | Yes      | `<br>"elasticmapreduce:CreatePersistentAppUI",<br>"elasticmapreduce:DescribePersistentAppUI",<br>"elasticmapreduce:GetPersistentAppUIPresignedURL",<br>"elasticmapreduce:ListClusters",<br>"elasticmapreduce:ListSteps",<br>"elasticmapreduce:DescribeCluster",<br>"s3:ListBucket",<br>"s3:GetObject"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Debug Amazon EMR on EC2 jobs with on-cluster application user interfaces                                                                                                                                                                                                                                                                                                                                                                              | Yes   | Yes          | Yes      | `<br>"elasticmapreduce:GetOnClusterAppUIPresignedURL"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Debug Amazon EMR on EKS job runs using the Spark History Server                                                                                                                                                                                                                                                                                                                                                                                       | Yes   | Yes          | Yes      | `<br>"elasticmapreduce:CreatePersistentAppUI",<br>"elasticmapreduce:DescribePersistentAppUI",<br>"elasticmapreduce:GetPersistentAppUIPresignedURL",<br>"emr-containers:ListVirtualClusters",<br>"emr-containers:DescribeVirtualCluster",<br>"emr-containers:ListJobRuns",<br>"emr-containers:DescribeJobRun",<br>"s3:ListBucket",<br>"s3:GetObject"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Create and delete Git repositories                                                                                                                                                                                                                                                                                                                                                                                                                    | Yes   | Yes          | Yes      | `<br>"elasticmapreduce:CreateRepository",<br>"elasticmapreduce:DeleteRepository",<br>"elasticmapreduce:ListRepositories",<br>"elasticmapreduce:DescribeRepository",<br>"secretsmanager:CreateSecret",<br>"secretsmanager:ListSecrets",<br>"secretsmanager:TagResource"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Link and unlink Git repositories                                                                                                                                                                                                                                                                                                                                                                                                                      | Yes   | Yes          | Yes      | `<br>"elasticmapreduce:LinkRepository",<br>"elasticmapreduce:UnlinkRepository",<br>"elasticmapreduce:ListRepositories",<br>"elasticmapreduce:DescribeRepository"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Create new clusters from predefined cluster templates                                                                                                                                                                                                                                                                                                                                                                                                 | No    | Yes          | Yes      | `<br>"servicecatalog:SearchProducts",<br>"servicecatalog:DescribeProduct",<br>"servicecatalog:DescribeProductView",<br>"servicecatalog:DescribeProvisioningParameters",<br>"servicecatalog:ProvisionProduct",<br>"servicecatalog:UpdateProvisionedProduct",<br>"servicecatalog:ListProvisioningArtifacts",<br>"servicecatalog:DescribeRecord",<br>"servicecatalog:ListLaunchPaths",<br>"cloudformation:DescribeStackResources",<br>"elasticmapreduce:ListClusters",<br>"elasticmapreduce:DescribeCluster"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Provide a cluster configuration to create new clusters.                                                                                                                                                                                                                                                                                                                                                                                               | No    | No           | Yes      | `<br>"elasticmapreduce:RunJobFlow",<br>"iam:PassRole",<br>"elasticmapreduce:ListClusters",<br>"elasticmapreduce:DescribeCluster"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Assign a user to a<br>Studio when you use IAM authentication mode.](emr-studio-manage-users.md#emr-studio-assign-users-groups "emr-studio-manage-users.md#emr-studio-assign-users-groups")                                                                                                                                                                                                                                                           | No    | No           | No       | `<br>"elasticmapreduce:CreateStudioPresignedUrl"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Describe network objects.                                                                                                                                                                                                                                                                                                                                                                                                                             | Yes   | Yes          | Yes      | JSON<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Sid": "DescribeNetwork",<br>"Effect": "Allow",<br>"Action": [<br>"ec2:DescribeVpcs",<br>"ec2:DescribeSubnets",<br>"ec2:DescribeSecurityGroups"<br>],<br>"Resource": [<br>"*"<br>]<br>}<br>]<br>}`<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| List IAM roles.                                                                                                                                                                                                                                                                                                                                                                                                                                       | Yes   | Yes          | Yes      | JSON<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Sid": "ListIAMRoles",<br>"Effect": "Allow",<br>"Action": [<br>"iam:ListRoles"<br>],<br>"Resource": [<br>"*"<br>]<br>}<br>]<br>}`<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Connect to EMR Studio from Amazon SageMaker AI Studio and use the Data Wrangler visual<br>interface.](https://aws.amazon.com/blogs/machine-learning/prepare-data-from-amazon-emr-for-machine-learning-using-amazon-sagemaker-data-wrangler/ "https://aws.amazon.com/blogs/machine-learning/prepare-data-from-amazon-emr-for-machine-learning-using-amazon-sagemaker-data-wrangler/")                                                                 | No    | No           | Yes      | `<br>"sagemaker:CreatePresignedDomainUrl",<br>"sagemaker:DescribeDomain",<br>"sagemaker:ListDomains",<br>"sagemaker:ListUserProfiles"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Use Amazon CodeWhisperer in your<br>EMR Studio.](emr-studio-codewhisperer.md "emr-studio-codewhisperer.md")                                                                                                                                                                                                                                                                                                                                          | No    | No           | Yes      | `<br>"codewhisperer:GenerateRecommendations"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Access Amazon Athena SQL editor from your<br>EMR Studio.](emr-studio-athena.md "emr-studio-athena.md") This list might not include all of the permissions that<br>you need to use all Athena features. For the most up-to-date list, see the [Athena full access policy](../../../athena/latest/ug/managed-policies.md#amazonathenafullaccess-managed-policy "../../../athena/latest/ug/managed-policies.md#amazonathenafullaccess-managed-policy"). | No    | No           | Yes      | `<br>"athena:StartQueryExecution",<br>"athena:StopQueryExecution",<br>"athena:GetQueryExecution",<br>"athena:GetQueryRuntimeStatistics",<br>"athena:GetQueryResults",<br>"athena:ListQueryExecutions",<br>"athena:BatchGetQueryExecution",<br>"athena:GetNamedQuery",<br>"athena:ListNamedQueries",<br>"athena:BatchGetNamedQuery",<br>"athena:UpdateNamedQuery",<br>"athena:DeleteNamedQuery",<br>"athena:ListDataCatalogs",<br>"athena:GetDataCatalog",<br>"athena:ListDatabases",<br>"athena:GetDatabase",<br>"athena:ListTableMetadata",<br>"athena:GetTableMetadata",<br>"athena:ListWorkGroups",<br>"athena:GetWorkGroup",<br>"athena:CreateNamedQuery",<br>"athena:GetPreparedStatement",<br>"glue:CreateDatabase",<br>"glue:DeleteDatabase",<br>"glue:GetDatabase",<br>"glue:GetDatabases",<br>"glue:UpdateDatabase",<br>"glue:CreateTable",<br>"glue:DeleteTable",<br>"glue:BatchDeleteTable",<br>"glue:UpdateTable",<br>"glue:GetTable",<br>"glue:GetTables",<br>"glue:BatchCreatePartition",<br>"glue:CreatePartition",<br>"glue:DeletePartition",<br>"glue:BatchDeletePartition",<br>"glue:UpdatePartition",<br>"glue:GetPartition",<br>"glue:GetPartitions",<br>"glue:BatchGetPartition",<br>"kms:ListAliases",<br>"kms:ListKeys",<br>"kms:DescribeKey",<br>"lakeformation:GetDataAccess",<br>"s3:GetBucketLocation",<br>"s3:GetBucketLocation",<br>"s3:GetObject",<br>"s3:ListBucket",<br>"s3:ListBucketMultipartUploads",<br>"s3:ListMultipartUploadParts",<br>"s3:AbortMultipartUpload",<br>"s3:PutObject",<br>"s3:PutBucketPublicAccessBlock",<br>"s3:ListAllMyBuckets"<br>` |
