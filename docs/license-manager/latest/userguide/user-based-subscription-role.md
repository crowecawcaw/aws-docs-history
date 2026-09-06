

# License Manager – User-based subscription role
<a name="user-based-subscription-role"></a>

License Manager requires a service-linked role for managing AWS resources that will provide user-based subscriptions.

## Permissions for the user-based subscription role
<a name="user-based-subscription-role-permissions"></a>

The service-linked role named `AWSServiceRoleForAWSLicenseManagerUserSubscriptionsService` allows License Manager to utilize AWS Systems Manager and manage Amazon EC2 resources providing user-based subscriptions, as well as describe Directory Service resources.

To review permissions for the **AWSLicenseManagerUserSubscriptionsServiceRolePolicy**, see [AWS managed policy: AWSLicenseManagerUserSubscriptionsServiceRolePolicy](security-iam-awsmanpol.md#security-iam-AWSLicenseManagerUserSubscriptionsServiceRolePolicy). To learn more about configuring permissions for a service-linked role, see [Service-Linked Role Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Create the service-linked role for License Manager
<a name="create-slr-user-based-subscription"></a>

You don't need to manually create the service-linked role as you will be prompted on the License Manager console **User-based subscriptions** pages to create the role.

If you delete this service-linked role and then need to create it again, you can use the same process to recreate the role in your account.

You can also use the IAM console, AWS CLI, or IAM API to create a service-linked role manually. For more information, see [Creating a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*.

You can use the License Manager console to create a service-linked role.

**To create the service-linked role**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the left navigation pane, choose **User Association** or **Products**.

1. Agree to the terms for License Manager to create the user-based subscription role.

1. Choose **Create**. This creates the role.

You can also use the IAM console to create a service-linked role with the `License Manager - User-based subscriptions` use case. Alternatively, in the AWS CLI or AWS API, create a service-linked role with the `license-manager-user-subscriptions.amazonaws.com` service name. For more information, see [Creating a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*. 

If you delete this service-linked role, you can use the same IAM process to create the role again.

## Edit a service-linked role for License Manager
<a name="edit-slr-user-based-subscription"></a>

License Manager does not allow you to edit the `AWSServiceRoleForAWSLicenseManagerUserSubscriptionsService` service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Delete a service-linked role for License Manager
<a name="delete-slr-user-based-subscription"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way, you only have entities that are actively monitored or maintained. However, you must clean up your service-linked role before you can manually delete it.

### Manually delete the service-linked role
<a name="slr-manual-delete-user-based-subscription"></a>

Use the IAM console, AWS CLI, or AWS API to delete the `AWSServiceRoleForAWSLicenseManagerUserSubscriptionsService` service-linked role. For more information, see [Deleting a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.