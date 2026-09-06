

# AWS managed policies for App Mesh
<a name="security-iam-awsmanpol"></a>

**Important**  
End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect). 

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## AWS managed policy: AWSAppMeshServiceRolePolicy
<a name="security-iam-awsmanpol-AWSAppMeshServiceRolePolicy"></a>

You can attach `AWSAppMeshServiceRolePolicy` to your IAM entities. Enables access to AWS Services and resources used or managed by AWS App Mesh.

To view the permissions for this policy, see [AWSAppMeshServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAppMeshServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

For information on the permission details for the `AWSAppMeshServiceRolePolicy`, see see [Service-Linked Role Permissions for App Mesh](https://docs.aws.amazon.com/app-mesh/latest/userguide/using-service-linked-roles.html#slr-permissions).

## AWS managed policy: AWSAppMeshEnvoyAccess
<a name="security-iam-awsmanpol-AWSAppMeshEnvoyAccess"></a>

You can attach `AWSAppMeshEnvoyAccess` to your IAM entities. App Mesh Envoy policy for accessing virtual node configuration.

To view the permissions for this policy, see [AWSAppMeshEnvoyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAppMeshEnvoyAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSAppMeshFullAccess
<a name="security-iam-awsmanpol-AWSAppMeshFullAccess"></a>

You can attach `AWSAppMeshFullAccess` to your IAM entities. Provides full access to the AWS App Mesh APIs and AWS Management Console.

To view the permissions for this policy, see [AWSAppMeshFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAppMeshFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSAppMeshPreviewEnvoyAccess
<a name="security-iam-awsmanpol-AWSAppMeshPreviewEnvoyAccess"></a>

You can attach `AWSAppMeshPreviewEnvoyAccess` to your IAM entities. App Mesh Preview Envoy policy for accessing virtual node configuration.

To view the permissions for this policy, see [AWSAppMeshPreviewEnvoyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAppMeshPreviewEnvoyAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSAppMeshPreviewServiceRolePolicy
<a name="security-iam-awsmanpol-AWSAppMeshPreviewServiceRolePolicy"></a>

You can attach `AWSAppMeshPreviewServiceRolePolicy` to your IAM entities. Enables access to AWS Services and resources used or managed by AWS App Mesh.

To view the permissions for this policy, see [AWSAppMeshPreviewServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAppMeshPreviewServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSAppMeshReadOnly
<a name="security-iam-awsmanpol-AWSAppMeshReadOnly"></a>

You can attach `AWSAppMeshReadOnly` to your IAM entities. Provides read-only access to the AWS App Mesh APIs and AWS Management Console.

To view the permissions for this policy, see [AWSAppMeshReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAppMeshReadOnly.html) in the *AWS Managed Policy Reference*.

## AWS App Mesh updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for AWS App Mesh since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the AWS App Mesh Document history page.


| Change | Description | Date | 
| --- | --- | --- | 
| [AWSAppMeshFullAccess](#security-iam-awsmanpol-AWSAppMeshFullAccess) – Updated policy. | Updated `AWSAppMeshFullAccess` to allow for access to the `TagResource` and `UntagResource`APIs. | April  24, 2024 | 
| [AWSAppMeshServiceRolePolicy](#security-iam-awsmanpol-AWSAppMeshServiceRolePolicy), [AWSServiceRoleForAppMesh](https://docs.aws.amazon.com/app-mesh/latest/userguide/using-service-linked-roles.html#slr-permissions) – Updated policy. | Updated `AWSServiceRoleForAppMesh` and `AWSAppMeshServiceRolePolicy` to allow for access to the AWS Cloud Map `DiscoverInstancesRevision` API. | October 12, 2023 | 

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.