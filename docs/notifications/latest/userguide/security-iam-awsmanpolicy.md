# AWS managed policies for AWS User Notifications

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

AWSUserNotificationsServiceLinkedRolePolicy

You can't attach `AWSUserNotificationsServiceLinkedRolePolicy` to your IAM
entities. This policy is attached to `AWSServiceRoleForAWSUserNotifications`, a service-linked role that allows User Notifications to call
AWS services on your behalf, publish Amazon CloudWatch metrics, and use AWS Organizations to manage notification configurations across your organizations. For more information, see
[Using Service-Linked Roles for
User Notifications](using-service-linked-roles.md "using-service-linked-roles.md").

**Permissions details**

This `AWSUserNotificationsServiceLinkedRolePolicy` is grouped into the following sets of permissions:

- `cloudwatch` — allows principals to publish Amazon CloudWatch metrics in the `AWS/Notifications` namespace.
- `events` — allows principals to manage Amazon EventBridge rules and targets for User Notifications.
- `notifications` — allows principals to manage notification configurations and event rules across an organization.
- `organizations` — allows principals to access and list AWS Organizations information, including delegated administrators for the `notifications.amazonaws.com` service principal.

To view the permissions for this policy, see [AWSUserNotificationsServiceLinkedRolePolicy](../../../aws-managed-policy/latest/reference/AWSUserNotificationsServiceLinkedRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSUserNotificationsServiceLinkedRolePolicy.md") in the _AWS Managed Policy Reference_.

## User Notifications updates to AWS managed

policies

View details about updates to AWS managed policies for User Notifications since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the [Document history for the AWS User Notifications User Guide](doc-history.md "doc-history.md") page.

| Change                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                              | Date             |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| [AWSUserNotificationsServiceLinkedRolePolicy](#managed-policy-uno "#managed-policy-uno") - Change     | Added `organizations:ListDelegatedAdministrators`, `notifications:CreateNotificationConfiguration`, `notifications:DeleteNotificationConfiguration`, `notifications:CreateEventRule`, `notifications:UpdateEventRule`, and `notifications:DeleteEventRule` to the policy. These permissions allow management accounts to distribute notification configurations across an organization.                                                                  | August 15, 2025  |
| [AWSUserNotificationsServiceLinkedRolePolicy](#managed-policy-uno "#managed-policy-uno") - Change     | Added `organizations:DescribeAccount`, `organizations:DescribeOrganization`, `organizations:DescribeOrganizationalUnit`, `organizations:ListAccounts`, `organizations:ListAWSServiceAccessForOrganization`, `organizations:ListChildren`, and `organizations:ListParents` to the policy. These permissions allow User Notifications to make calls to the AWS Organizations API so users can manage and monitor notifications across their organizations. | January 15, 2025 |
| [AWSUserNotificationsServiceLinkedRolePolicy](#managed-policy-uno "#managed-policy-uno") - New policy | Allows User Notifications to create, read, update, and delete managed rules in the account. Allows User Notifications to to publish Amazon CloudWatch metrics within the `AWS/Notifications` namespace.                                                                                                                                                                                                                                                  | April 20, 2023   |
| User Notifications started tracking changes                                                           | User Notifications started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                | April 10, 2023   |
