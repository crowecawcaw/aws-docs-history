# AWS managed policies for App Mesh

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed policy:

AWSAppMeshServiceRolePolicy

You can attach `AWSAppMeshServiceRolePolicy` to your IAM entities. Enables access to
AWS Services and resources used or managed by AWS App Mesh.

To view the permissions for this policy, see [AWSAppMeshServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSAppMeshServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSAppMeshServiceRolePolicy.md") in the _AWS Managed Policy
Reference_.

For information on the permission details for the `AWSAppMeshServiceRolePolicy`, see see [Service-Linked
Role Permissions for App Mesh](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions").

## AWS managed policy:

AWSAppMeshEnvoyAccess

You can attach `AWSAppMeshEnvoyAccess` to your IAM entities. App Mesh Envoy policy for
accessing virtual node configuration.

To view the permissions for this policy, see [AWSAppMeshEnvoyAccess](../../../aws-managed-policy/latest/reference/AWSAppMeshEnvoyAccess.md "../../../aws-managed-policy/latest/reference/AWSAppMeshEnvoyAccess.md")
in the _AWS Managed Policy Reference_.

## AWS managed policy:

AWSAppMeshFullAccess

You can attach `AWSAppMeshFullAccess` to your IAM entities. Provides full access to the
AWS App Mesh APIs and AWS Management Console.

To view the permissions for this policy, see [AWSAppMeshFullAccess](../../../aws-managed-policy/latest/reference/AWSAppMeshFullAccess.md "../../../aws-managed-policy/latest/reference/AWSAppMeshFullAccess.md") in
the _AWS Managed Policy Reference_.

## AWS managed policy:

AWSAppMeshPreviewEnvoyAccess

You can attach `AWSAppMeshPreviewEnvoyAccess` to your IAM entities. App Mesh Preview Envoy
policy for accessing virtual node configuration.

To view the permissions for this policy, see [AWSAppMeshPreviewEnvoyAccess](../../../aws-managed-policy/latest/reference/AWSAppMeshPreviewEnvoyAccess.md "../../../aws-managed-policy/latest/reference/AWSAppMeshPreviewEnvoyAccess.md") in the _AWS Managed Policy
Reference_.

## AWS managed policy:

AWSAppMeshPreviewServiceRolePolicy

You can attach `AWSAppMeshPreviewServiceRolePolicy` to your IAM entities. Enables access
to AWS Services and resources used or managed by AWS App Mesh.

To view the permissions for this policy, see [AWSAppMeshPreviewServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSAppMeshPreviewServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSAppMeshPreviewServiceRolePolicy.md") in the _AWS Managed Policy
Reference_.

## AWS managed policy:

AWSAppMeshReadOnly

You can attach `AWSAppMeshReadOnly` to your IAM entities. Provides read-only access to
the AWS App Mesh APIs and AWS Management Console.

To view the permissions for this policy, see [AWSAppMeshReadOnly](../../../aws-managed-policy/latest/reference/AWSAppMeshReadOnly.md "../../../aws-managed-policy/latest/reference/AWSAppMeshReadOnly.md") in the
_AWS Managed Policy Reference_.

## AWS App Mesh updates to AWS managed policies

View details about updates to AWS managed policies for AWS App Mesh since this service began tracking
these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the
AWS App Mesh Document history page.

| Change                                                                                                                                                                                                                                                                                | Description                                                                                                                                    | Date             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [AWSAppMeshFullAccess](#security-iam-awsmanpol-AWSAppMeshFullAccess "#security-iam-awsmanpol-AWSAppMeshFullAccess") – Updated policy.                                                                                                                                                 | Updated `AWSAppMeshFullAccess` to allow for access to the `TagResource` and `UntagResource`APIs.                                               | April  24, 2024  |
| [AWSAppMeshServiceRolePolicy](#security-iam-awsmanpol-AWSAppMeshServiceRolePolicy "#security-iam-awsmanpol-AWSAppMeshServiceRolePolicy"), [AWSServiceRoleForAppMesh](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") – Updated policy. | Updated `AWSServiceRoleForAppMesh` and `AWSAppMeshServiceRolePolicy` to allow for access to the AWS Cloud Map `DiscoverInstancesRevision` API. | October 12, 2023 | To provide access, add permissions to your users, groups, or roles: <br>• Users and groups in AWS IAM Identity Center: Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_. <br>• Users managed in IAM through an identity provider: Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md") in the _IAM User Guide_. <br>• IAM users: + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_. + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_. |
