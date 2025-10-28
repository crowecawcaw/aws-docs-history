# Configuring IAM permissions

This topic describes the IAM permissions that you configure for the Amazon Q chat experience, and the AWS Glue Studio notebook experience.

###### Topics

- [Configuring IAM permissions for Amazon Q chat](#q-setting-up-permissions-amazon-q-chat "#q-setting-up-permissions-amazon-q-chat")
- [Configuring IAM permissions for AWS Glue Studio notebooks](#q-setting-up-permissions-notebooks "#q-setting-up-permissions-notebooks")

## Configuring IAM permissions for Amazon Q chat

Granting permissions to the APIs used by Amazon Q data integration in AWS Glue requires appropriate AWS Identity and Access Management (IAM) permissions. You can obtain permissions by attaching the following custom AWS policy to your IAM identity (such as a user, role, or group):

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:StartCompletion",
 "glue:GetCompletion"
 ],
 "Resource": [
 "arn:aws:glue:*:*:completion/*"
 ]
 }
 ]
}`

```

## Configuring IAM permissions for AWS Glue Studio notebooks

To enable Amazon Q data integration in AWS Glue Studio notebooks, ensure the following permission is attached to the notebook IAM role:

###### Note

The `codewhisperer` prefix is a legacy name from a service that merged
with Amazon Q Developer. For more information, see [Amazon Q Developer rename - Summary of changes](../../../amazonq/latest/qdeveloper-ug/service-rename.md "../../../amazonq/latest/qdeveloper-ug/service-rename.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:StartCompletion",
 "glue:GetCompletion"
 ],
 "Resource": [
 "arn:aws:glue:*:*:completion/*"
 ]
 },
 {
 "Sid": "AmazonQDeveloperPermissions",
 "Effect": "Allow",
 "Action": [
 "codewhisperer:GenerateRecommendations"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

Amazon Q data integration in AWS Glue does not have APIs available through the AWS SDK that you can use programmatically. The following two APIs are used in the IAM policy for enabling this experience through the Amazon Q chat panel or AWS Glue Studio notebooks: `StartCompletion` and `GetCompletion`.

### Assigning permissions

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center: Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.
- Users managed in IAM through an identity provider: Create a role for identity federation. Follow the instructions in [Creating a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md") in the _IAM User Guide_.
- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Creating a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.
