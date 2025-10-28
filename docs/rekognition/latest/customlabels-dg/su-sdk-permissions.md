# Set up SDK permissions

To use Amazon Rekognition Custom Labels
SDK operations, you need access permissions to the Amazon Rekognition Custom Labels API and the Amazon S3 bucket used
for model training.

###### Topics

- [Granting SDK operation permissions](#su-grant-sdk-permissions "#su-grant-sdk-permissions")
- [Policy updates for using the AWS SDK](#su-sdk-policy-update "#su-sdk-policy-update")
- [Assigning permissions](#su-sdk-assign-permissions "#su-sdk-assign-permissions")

## Granting SDK operation permissions

We recommend that you grant only the permissions required to perform a task
(least-privilege permissions). For example, to call [DetectCustomLabels](../APIReference/API_DetectCustomLabels.md "../APIReference/API_DetectCustomLabels.md"), you need permission to perform
`rekognition:DetectCustomLabels`. To find the permissions for an
operation, check the [API reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

When you are just starting out with an application, you might not know the
specific permissions you need, so you can start with broader permissions. AWS
managed policies provide permissions to help you get started.
You can use the `AmazonRekognitionCustomLabelsFullAccess` AWS managed
policy to get complete access to the Amazon Rekognition Custom Labels API. For more information, see
[AWS managed policy: AmazonRekognitionCustomLabelsFullAccess](../dg/security-iam-awsmanpol.md#security-iam-awsmanpol-custom-labels-full-access "../dg/security-iam-awsmanpol.md#security-iam-awsmanpol-custom-labels-full-access"). When you
know the permissions that your application needs, reduce permissions further by
defining customer managed policies specific to your use cases. For more information,
see [Customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies").

To assign permissions, see [Assigning permissions](#su-sdk-assign-permissions "#su-sdk-assign-permissions").

## Policy updates for using the AWS SDK

To use the AWS SDK with the latest release of Amazon Rekognition Custom Labels, you no longer need to
give Amazon Rekognition Custom Labels permissions to access the
Amazon S3 bucket that contains your training and testing images. If you have previously added
permissions, You don't need to remove them. If you choose to, remove any policy from the
bucket where the
service for the principal is `rekognition.amazonaws.com`. For example:

```
"Principal": {
    "Service": "rekognition.amazonaws.com"
}
```

For more information, see
[Using bucket policies](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md").

## Assigning permissions

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.
