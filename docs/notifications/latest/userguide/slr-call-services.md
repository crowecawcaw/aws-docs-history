# AWS User Notifications service-Linked Role for calling AWS services, publishing metrics, and using AWS Organizations

User Notifications uses the service-linked role named **AWSServiceRoleForAWSUserNotifications**. This
role allows User Notifications to call AWS services on your behalf and use AWS Organizations to manage your notification configurations across your organizations. It also allows the role to
publish metrics in the `AWS/Notifications` namespace.

## Service-Linked Role Permissions for

User Notifications

User Notifications uses the service-linked role named **AWSServiceRoleForAWSUserNotifications**. This
role allows User Notifications to call AWS services on your behalf and use AWS Organizations to manage your notification configurations across your organizations. It also allows the role to
publish metrics in the `AWS/Notifications` namespace.

The **AWSServiceRoleForAWSUserNotifications** service-linked role trusts the following services to assume the
role:

- `notifications.amazonaws.com`

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

When you create a notification hub or a notification configuration, it creates the `AWSUserNotificationsServiceLinkedRolePolicy`. For more information, see [AWS managed policy:
AWSUserNotificationsServiceLinkedRolePolicy](security-iam-awsmanpolicy.md#managed-policy-uno "security-iam-awsmanpolicy.md#managed-policy-uno")

You don't need to take any action to support this role beyond using User Notifications.

## Creating a Service-Linked Role for

User Notifications

You don't need to manually create a service-linked role. When you
create a notification hub or a notification configuration in the AWS Management Console, or when you enable service trust with AWS Organizations, User Notifications
creates the service-linked role for you.

If you delete this service-linked role and need to create it again later, you can use the
same process to recreate the role in your account. When you create a notification hub or a notification configuration,
User Notifications creates the service-linked role for you again.

## Editing a Service-Linked Role for

User Notifications

User Notifications doesn't allow you to edit the AWSServiceRoleForAWSUserNotifications service-linked role. After you
create a service-linked role, you can't change the name of the role. This is because
various entities might reference the role. However, you can edit the description of the
role using IAM. For more information, see [Editing a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Manually deleting a Service-Linked Role for

User Notifications

Under specific circumstances, you can manually delete the AWSServiceRoleForAWSUserNotifications service-linked role.
To delete the User Notifications service-linked role, you must first delete all notification
configurations in the account. You can delete all User Notifications notification configurations
using the User Notifications console. You then use the IAM console, the AWS CLI, or the AWS API to
delete the AWSServiceRoleForAWSUserNotifications service-linked role. For more information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

###### Note

If the User Notifications service is using the role when you try to delete the resources, the
deletion might fail. If that happens, wait for a few minutes and try the operation
again.

###### To delete notification configurations

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
   1. In the navigation pane, choose **Notification configurations**.

2. Select the configuration you want to delete.
3. Choose **Delete**.
