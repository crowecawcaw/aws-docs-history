# App Runner identity-based policy examples

By default, IAM users and roles don't have permission to create or modify AWS App Runner resources. They also can't perform tasks using the
AWS Management Console, AWS CLI, or AWS API. An IAM administrator must create IAM policies that grant users and roles permission to perform specific API operations
on the specified resources they need. The administrator must then attach those policies to the IAM users or groups that require those
permissions.

To learn how to create an IAM identity-based policy using these example JSON policy documents, see [Creating Policies on the JSON Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

For other App Runner security topics, see [Security in App Runner](security.md "security.md").

###### Topics

- [Policy best practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [User policies](#security_iam_id-based-policy-examples-users "#security_iam_id-based-policy-examples-users")
- [Controlling access to App Runner services based on tags](#security_iam_id-based-policy-examples-view-widget-tags "#security_iam_id-based-policy-examples-view-widget-tags")

## Policy best practices

Identity-based policies determine whether someone can create, access, or delete App Runner resources in your
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
  if they are used through a specific AWS service, such as AWS CloudFormation. For more information, see
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

## User policies

To access the App Runner console, IAM users must have a minimum set of permissions. These permissions must allow you to list and view
details about the App Runner resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum
required permissions, the console won't function as intended for users with that policy.

App Runner provides two managed policies that you can attach to your users.

- `AWSAppRunnerReadOnlyAccess` – Grants permissions to list and view details about App Runner resources.
- `AWSAppRunnerFullAccess` – Grants permissions to all App Runner actions.

To ensure that users can use the App Runner console, attach, at a minimum, the `AWSAppRunnerReadOnlyAccess` managed policy to
the users. You can attach the `AWSAppRunnerFullAccess` managed policy instead, or add specific additional permissions, to allow users
to create, modify, and delete resource. For more information, see [Adding Permissions to a User](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to
only the actions that match the API operation that you want to allow users to perform.

The following examples demonstrate custom user policies. You can use them as starting points to defining your own custom user policies. Copy the
example, and or remove actions, scope down resources, and add conditions.

### Example: console and connection management user policy

This example policy enables console access and allows connection creation and management. It doesn't allow App Runner service creation and management.
It can be attached to a user whose role is to manage App Runner service access to source code assets.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "apprunner:List*",
 "apprunner:Describe*",
 "apprunner:CreateConnection",
 "apprunner:DeleteConnection"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Example: user policies that use condition keys

The examples in this section demonstrate conditional permissions that depend on some resource properties or action parameters.

This example policy enables creating an App Runner service but denies using a connection named `prod`.

JSON

```
`{ "Version":"2012-10-17",
 "Statement":
 [ { "Sid": "AllowCreateAppRunnerServiceWithNonProdConnections",
 "Effect": "Allow",
 "Action": "apprunner:CreateService",
 "Resource": "*",
 "Condition":
 { "ArnNotLike":
 {"apprunner:ConnectionArn":"`arn:aws:`apprunner:*:*:connection/prod/*"}
 }
 }
 ]
 }`

```

This example policy enables updating an App Runner service named `preprod` only with an auto scaling configuration named
`preprod`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowUpdatePreProdAppRunnerServiceWithPreProdASConfig",
 "Effect": "Allow",
 "Action": "apprunner:UpdateService",
 "Resource": "arn:aws:apprunner:*:*:service/preprod/*",
 "Condition": {
 "ArnLike": {
 "apprunner:AutoScalingConfigurationArn": "arn:aws:apprunner:`us-east-1`:*:autoscalingconfiguration/preprod/*"
 }
 }
 }
 ]
}`

```

## Controlling access to App Runner services based on tags

You can use conditions in your identity-based policy to control access to App Runner resources based on tags. This example shows how you might
create a policy that allows deleting an App Runner service. However, permission is granted only if the service tag `Owner` has the value of that
user's user name. This policy also grants the permissions necessary to complete this action on the console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListServicesInConsole",
 "Effect": "Allow",
 "Action": "apprunner:ListServices",
 "Resource": "*"
 },
 {
 "Sid": "DeleteServiceIfOwner",
 "Effect": "Allow",
 "Action": "apprunner:DeleteService",
 "Resource": "arn:aws:apprunner:`us-east-1`:*:service/*",
 "Condition": {
 "StringEquals": {"aws:ResourceTag/Owner": "${aws:username}"}
 }
 }
 ]
}`

```

You can attach this policy to the IAM users in your account. If a user named `richard-roe` attempts to delete an App Runner service, the
service must be tagged `Owner=richard-roe` or `owner=richard-roe`. Otherwise he is denied access. The condition tag key
`Owner` matches both `Owner` and `owner` because condition key names are not case-sensitive. For more information,
see [IAM JSON Policy Elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
