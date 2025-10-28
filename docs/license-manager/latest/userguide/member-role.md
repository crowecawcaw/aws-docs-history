# License Manager – Member account role

License Manager requires a service-linked role that allows the management account to manage
licenses.

## Permissions for the member account role

The service-linked role named
`AWSServiceRoleForAWSLicenseManagerMemberAccountRole` allows License Manager to
access AWS resources for license management actions from a configured management account
on your behalf.

The `AWSServiceRoleForAWSLicenseManagerMemberAccountRole`
service-linked role trusts the `license-manager.member-account.amazonaws.com`
service to assume the role.

To review permissions for the **AWSLicenseManagerMemberAccountRolePolicy**,
see [AWS managed
policy: AWSLicenseManagerMemberAccountRolePolicy](security-iam-awsmanpol.md#security-iam-AWSLicenseManagerMemberAccountRolePolicy "security-iam-awsmanpol.md#security-iam-AWSLicenseManagerMemberAccountRolePolicy"). To learn more
about configuring permissions for a service-linked role, see
[Service-Linked
Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Create the service-linked role for License Manager

You don't need to manually create the service-linked role. You can enable integration
with AWS Organizations from the management account in the License Manager console on the
**Settings** page. You can also do this using the AWS CLI (run
`update-service-settings`) or the AWS API (call
`UpdateServiceSettings`). When you do, License Manager creates the service-linked role
for you in the Organizations member accounts.

If you delete this service-linked role and then need to create it again, you can use the
same process to recreate the role in your account.

You can also use the IAM console, AWS CLI, or the AWS API to create a service-linked
role manually. For more information, see [Creating a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_.

###### Important

This service-linked role can appear in your account if you completed an action in
another service that uses the features supported by this role. If you were using the License Manager
service before January 1, 2017, when it began supporting service-linked roles, then
License Manager created the `AWSServiceRoleForAWSLicenseManagerMemberAccountRole`
role in your account. For more information, see [A New
Role Appeared in My IAM Account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

You can use the License Manager console to create a service-linked role.

###### To create the service-linked role

1. Log in to your AWS Organizations management account.
2. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
3. In the left navigation pane, choose **Settings**, and then choose
   **Edit**.
4. Choose **Link AWS Organizations accounts**.
5. Choose **Apply**. This creates the roles [AWSServiceRoleForAWSLicenseManagerRole](license-manager-role-core.md "license-manager-role-core.md") and [AWSServiceRoleForAWSLicenseManagerMemberAccountRole](member-role.md "member-role.md") in
   all child accounts.

You can also use the IAM console to create a service-linked role with the `License Manager

- Member account`use case. Alternatively, in the AWS CLI or AWS API, create a
service-linked role with the`license-manager.member-account.amazonaws.com`
  service name. For more information, see [Creating a
  Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_.

If you delete this service-linked role, you can use the same IAM process to create the
role again.

## Edit a service-linked role for License Manager

License Manager does not allow you to edit the
`AWSServiceRoleForAWSLicenseManagerMemberAccountRole` service-linked
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
`AWSServiceRoleForAWSLicenseManagerMemberAccountRole` service-linked
role. For more information, see [Deleting
a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.
