# License Manager – Linux subscriptions role

License Manager requires a service-linked role to manage AWS resources that provide Linux subscriptions.

## Permissions for the Linux

subscriptions role

The service-linked role named
`AWSServiceRoleForAWSLicenseManagerLinuxSubscriptionsService` allows License Manager
to perform the following actions for Linux subscriptions.

- Discover Amazon Elastic Compute Cloud and AWS Organizations resources.
- Retrieve secrets tagged with `"LicenseManagerLinuxSubscriptions": "enabled"`
  from AWS Secrets Manager for access to third-party Linux subscription providers to get
  subscription information.
- Use KMS keys tagged with `"LicenseManagerLinuxSubscriptions": "enabled"`
  to decrypt secrets.

To review permissions for the **AWSLicenseManagerLinuxSubscriptionsServiceRolePolicy**,
see [AWS managed policy:
AWSLicenseManagerLinuxSubscriptionsServiceRolePolicy](security-iam-awsmanpol.md#security-iam-AWSLicenseManagerLinuxSubscriptionsServiceRolePolicy "security-iam-awsmanpol.md#security-iam-AWSLicenseManagerLinuxSubscriptionsServiceRolePolicy"). To learn more
about configuring permissions for a service-linked role, see
[Service-Linked
Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Create the service-linked role for License Manager

You don't need to manually create the service-linked role as you will be prompted on the
License Manager console **Linux subscriptions** pages to create the role.

If you delete this service-linked role and then need to create it again, you can use the
same process to recreate the role in your account.

You can also use the IAM console, AWS CLI, or IAM API to create a service-linked role
manually. For more information, see [Creating a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_.

You can use the License Manager console to create a service-linked role.

###### To create the service-linked role

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, choose **Subscriptions** or
   **Instances**.
3. Agree to the terms for License Manager to create the Linux subscriptions role.
4. Choose **Create**. This creates the role.

You can also use the IAM console to create a service-linked role with the `License Manager

- Linux subscriptions`use case. Alternatively, in the AWS CLI or AWS API, create a
service-linked role with the`license-manager-linux-subscriptions.amazonaws.com`
  service name. For more information, see [Creating a
  Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_.

If you delete this service-linked role, you can use the same IAM process to create the
role again.

## Edit a service-linked role for License Manager

License Manager does not allow you to edit the
`AWSServiceRoleForAWSLicenseManagerLinuxSubscriptionsService` service-linked
role. After you create a service-linked role, you cannot change the name of the role because
various entities might reference the role. However, you can edit the description of the role
using IAM. For more information, see [Editing a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Delete a service-linked role for License Manager

If you no longer need to use a feature or service that requires a service-linked
role, we recommend that you delete that role. That way, you only have entities that are
actively monitored or maintained. However, you must clean up your service-linked role
before you can manually delete it.

### Manually delete the service-linked role

Use the IAM console, AWS CLI, or AWS API to delete the
`AWSServiceRoleForAWSLicenseManagerLinuxSubscriptionsService` service-linked
role. For more information, see [Deleting
a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.
