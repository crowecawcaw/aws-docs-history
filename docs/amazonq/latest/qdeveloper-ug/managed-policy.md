# AWS managed policies for Amazon Q Developer

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS
managed policies are designed to provide permissions for many common use cases so that you can start
assigning permissions to users, groups, and roles.

The quickest way for an administrator to grant access to users is through an AWS managed policy.
The following AWS managed policies for Amazon Q Developer can be attached to IAM identities:

- `AmazonQFullAccess` provides full access to enable interactions with Amazon Q Developer,
  including administrator access.
- `AmazonQDeveloperAccess` provides full access to enable interactions with
  Amazon Q Developer, without administrator access.

###### Note

Users accessing Amazon Q in the IDE or on the command line don't require
IAM permissions.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your
specific use cases because they’re available for all AWS customers to use. We recommend that you
reduce permissions further by defining [customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the
permissions defined in an AWS managed policy, the update affects all principal identities (users,
groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed
policy when a new AWS service is launched or new API operations become available for existing
services.

For more information, see [AWS
managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

## AmazonQFullAccess

The `AmazonQFullAccess` managed policy provides administrator access
to allow users in your organization to access Amazon Q Developer. It also provides full access to enable
interactions with Amazon Q Developer, including logging in with IAM Identity Center to access Amazon Q through an
Amazon Q Developer Pro subscription.

###### Note

To enable full access to complete administrative tasks in the Amazon Q subscription management
console and Amazon Q Developer Pro console, additional permissions are needed. For more information, see
[Administrator permissions](id-based-policy-examples-admins.md "id-based-policy-examples-admins.md").

To view the permissions for this policy, see [AmazonQFullAccess](../../../aws-managed-policy/latest/reference/AmazonQFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonQFullAccess.md") in the _AWS Managed Policy Reference_.

## AmazonQDeveloperAccess

The `AmazonQDeveloperAccess` managed policy provides full access to
enable interactions with Amazon Q Developer, without administrator access. It includes access to log in
with IAM Identity Center to access Amazon Q through an Amazon Q Developer Pro subscription.

To use some features of Amazon Q, you might need additional permissions. See the topic for the
feature you want to use for information on permissions.

To view the permissions for this policy, see [AmazonQDeveloperAccess](../../../aws-managed-policy/latest/reference/AmazonQDeveloperAccess.md "../../../aws-managed-policy/latest/reference/AmazonQDeveloperAccess.md") in the _AWS Managed Policy Reference_.

## AWSServiceRoleForAmazonQDeveloper

This AWS managed policy grants permissions commonly needed to use Amazon Q Developer. The policy is
added to the AWSServiceRoleForAmazonQDeveloper service linked role that is created when you
onboard to Amazon Q.

You can't attach AWSServiceRoleForAmazonQDeveloper to your IAM entities. This policy is
attached to [a service-linked role](using-service-linked-roles.md "using-service-linked-roles.md") that allows
Amazon Q to perform actions on your behalf. For more information, see [Using service-linked roles for Amazon Q Developer and User Subscriptions](using-service-linked-roles.md "using-service-linked-roles.md").

This policy grants `administrator` permissions that allows metrics to
be published for Billing / Usage.

**Permissions details**

This policy includes the following permissions.

- `cloudwatch` – Allows principals to publish usage metrics to CloudWatch for
  Billing / Usage. This is required so that you can track your usage of Amazon Q in CloudWatch.

To view the permissions for this policy, see [AWSServiceRoleForAmazonQDeveloper](../../../aws-managed-policy/latest/reference/AWSServiceRoleForAmazonQDeveloper.md "../../../aws-managed-policy/latest/reference/AWSServiceRoleForAmazonQDeveloper.md") in the _AWS Managed Policy Reference_.

## AWSServiceRoleForUserSubscriptions

This AWS managed policy grants permissions commonly needed to use Amazon Q Developer. The policy is
added to the AWSServiceRoleForUserSubscriptions service-linked role that is created when you
create Amazon Q subscriptions.

You can't attach AWSServiceRoleForUserSubscriptions to your IAM entities. This policy is
attached to [a service-linked role](using-service-linked-roles.md "using-service-linked-roles.md") that allows
Amazon Q to perform actions on your behalf. For more information, see [Using service-linked roles for Amazon Q Developer and User Subscriptions](using-service-linked-roles.md "using-service-linked-roles.md").

This policy provides access for Amazon Q Subscriptions to your Identity Center resources to
automatically update your subscriptions.

**Permissions details**

This policy includes the following permissions.

- `identitystore` – Allows principals to track Identity Center directory
  changes so that subscriptions can be automatically updated.
- `organizations` – Allows principals to track AWS Organizations changes
  so that subscriptions can be automatically updated.
- `sso` – Allows principals to track Identity Center instance changes so
  that subscriptions can be automatically updated.
- `kms` – Allows principals to access to KMS keys to authorize with Identity Center.

To view the permissions for this policy, see [AWSServiceRoleForUserSubscriptions](../../../aws-managed-policy/latest/reference/AWSServiceRoleForUserSubscriptions.md "../../../aws-managed-policy/latest/reference/AWSServiceRoleForUserSubscriptions.md") in the _AWS Managed Policy Reference_.

## GitLabDuoWithAmazonQPermissionsPolicy

This policy grants permission to connect with Amazon Q and utilize the features in the GitLab Duo
with Amazon Q integration. The policy is added to the IAM role created from the Amazon Q Developer console to
access Amazon Q. You need to manually provide the IAM role to GitLab as an Amazon Resource Name
(ARN). The policy allows the following:

- **GitLab Duo usage permissions** - Allows basic operations such as sending
  events and messages, creating and updating auth grants, generating code recommendations,
  listing plugins, and verifying OAuth app connections.
- **GitLab Duo management permissions** - Enables the creation and deletion
  of OAuth app connections, providing control over the integration setup.
- **GitLab Duo plugin permissions** - Grants specific permissions to create,
  delete, and retrieve plugins related to the GitLab Duo integration with Amazon Q.

To view the permissions for this policy, see [GitLabDuoWithAmazonQPermissionsPolicy](../../../aws-managed-policy/latest/reference/GitLabDuoWithAmazonQPermissionsPolicy.md "../../../aws-managed-policy/latest/reference/GitLabDuoWithAmazonQPermissionsPolicy.md") in the _AWS Managed Policy Reference_.

## Policy updates

View details about updates to AWS managed policies for Amazon Q Developer since this service began
tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed
on the [Document history for Amazon Q Developer User Guide](doc-history.md "doc-history.md") page.

| Change                                                                                                                                                                        | Description                                                                                                                                                                             | Date              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AmazonQDeveloperAccess](#amazonq-policy-developeraccess "#amazonq-policy-developeraccess")<br>• Updated policy                                                               | Additional permissions have been added to enable access to KMS keys to authorize with Identity Center.                                                                                  | October 29, 2025  |
| [AmazonQFullAccess](#amazonq-policy-fullaccess "#amazonq-policy-fullaccess")<br>• Updated policy                                                                              | Additional permissions have been added to enable access to KMS keys to authorize with Identity Center.                                                                                  | October 29, 2025  |
| [AWSServiceRoleForUserSubscriptions](#amazonq-policy-AWSServiceRoleForUserSubscriptions "#amazonq-policy-AWSServiceRoleForUserSubscriptions")<br>• Updated policy             | Additional permissions have been added to enable access to KMS keys to authorize with Identity Center.                                                                                  | October 29, 2025  |
| [AmazonQDeveloperAccess](#amazonq-policy-developeraccess "#amazonq-policy-developeraccess")<br>• Updated policy                                                               | Additional permissions have been added to manage conversation history in Amazon Q<br>chat.                                                                                              | May 14, 2025      |
| [AmazonQFullAccess](#amazonq-policy-fullaccess "#amazonq-policy-fullaccess")<br>• Updated policy                                                                              | Additional permissions have been added to manage conversation history in Amazon Q<br>chat.                                                                                              | May 14, 2025      |
| [AmazonQFullAccess](#amazonq-policy-fullaccess "#amazonq-policy-fullaccess")<br>• Updated policy                                                                              | Additional permission has been added to update feature enablement controls for<br>third-party integration plugin.                                                                       | May 2, 2025       |
| [AmazonQFullAccess](#amazonq-policy-fullaccess "#amazonq-policy-fullaccess")<br>• Updated policy                                                                              | Additional permissions have been added to allow access and enable interactions<br>with Amazon Q Developer for third-party plugins.                                                      | April 30, 2025    |
| [GitLabDuoWithAmazonQPermissionsPolicy](#amazonq-policy-GitLabDuoWithAmazonQPermissionsPolicy "#amazonq-policy-GitLabDuoWithAmazonQPermissionsPolicy")<br>• Updated<br>policy | Additional permission has been added to allow updates to a third-party OAuth<br>application with Amazon Q Developer.                                                                    | April 30, 2025    |
| [GitLabDuoWithAmazonQPermissionsPolicy](#amazonq-policy-GitLabDuoWithAmazonQPermissionsPolicy "#amazonq-policy-GitLabDuoWithAmazonQPermissionsPolicy")<br>• New<br>policy     | Allows GitLab to connect with Amazon Q Developer to use GitLab Duo with Amazon Q integration<br>features.                                                                               | April 17, 2025    |
| [AWSServiceRoleForUserSubscriptions](#amazonq-policy-AWSServiceRoleForUserSubscriptions "#amazonq-policy-AWSServiceRoleForUserSubscriptions")<br>• Updated<br>policy          | Allows Amazon Q to discover the email verification status of end users.                                                                                                                 | February 17, 2025 |
| [AmazonQDeveloperAccess](#amazonq-policy-developeraccess "#amazonq-policy-developeraccess")<br>• Updated policy                                                               | Additional permissions have been added to enable the use of Amazon Q Developer<br>plugins.                                                                                              | November 13, 2024 |
| [AmazonQFullAccess](#amazonq-policy-fullaccess "#amazonq-policy-fullaccess")<br>• Updated policy                                                                              | Additional permissions have been added to configure and use Amazon Q Developer plugins<br>and to create and manage tags for Amazon Q Developer resources.                               | November 13, 2024 |
| [AmazonQDeveloperAccess](#amazonq-policy-developeraccess "#amazonq-policy-developeraccess")<br>• Updated policy                                                               | Additional permissions have been added to enable code generation from CLI<br>commands with Amazon Q.                                                                                    | October 28, 2024  |
| [AmazonQFullAccess](#amazonq-policy-fullaccess "#amazonq-policy-fullaccess")<br>• Updated policy                                                                              | Additional permissions have been added to enable code generation from CLI<br>commands with Amazon Q.                                                                                    | October 28, 2024  |
| [AmazonQFullAccess](#amazonq-policy-fullaccess "#amazonq-policy-fullaccess")<br>• Updated policy                                                                              | Additional permissions have been added to enable Amazon Q to access downstream<br>resources.                                                                                            | July 9, 2024      |
| [AmazonQDeveloperAccess](#amazonq-policy-developeraccess "#amazonq-policy-developeraccess")<br>• New policy                                                                   | Provides full access to enable interactions with Amazon Q Developer, without<br>administrator access.                                                                                   | July 9, 2024      |
| [AmazonQFullAccess](#amazonq-policy-fullaccess "#amazonq-policy-fullaccess")<br>• Updated policy                                                                              | Additional permissions have been added to enable subscriptions checks for<br>Amazon Q Developer.                                                                                        | April 30, 2024    |
| [AWSServiceRoleForUserSubscriptions](#amazonq-policy-AWSServiceRoleForUserSubscriptions "#amazonq-policy-AWSServiceRoleForUserSubscriptions")<br>• New<br>policy              | Allows Amazon Q Subscriptions to automatically update subscriptions from changes<br>in AWS IAM Identity Center, AWS IAM Identity Center directory and AWS Organizations on your behalf. | April 30, 2024    |
| [AWSServiceRoleForAmazonQDeveloper](#amazonq-policy-AWSServiceRoleForAmazonQDeveloper "#amazonq-policy-AWSServiceRoleForAmazonQDeveloper")<br>• New<br>policy                 | Allows Amazon Q to call Amazon CloudWatch and Amazon CodeGuru on your behalf.                                                                                                           | April 30, 2024    |
| [AmazonQFullAccess](#amazonq-policy-fullaccess "#amazonq-policy-fullaccess") -<br>New policy                                                                                  | Provides full access to enable interactions with Amazon Q Developer.                                                                                                                    | November 28, 2023 |
| Amazon Q Developer started tracking changes                                                                                                                                   | Amazon Q Developer started tracking changes to AWS managed policies.                                                                                                                    | November 28, 2023 |
