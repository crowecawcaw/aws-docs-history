# Troubleshooting AWS CloudTrail identity and

access

Use the following information to help you diagnose and fix common issues that you might
encounter when working with CloudTrail and IAM.

###### Topics

- [I am not authorized to
  perform an action in CloudTrail](#security_iam_troubleshoot-no-permissions "#security_iam_troubleshoot-no-permissions")
- [I am not authorized to perform
  iam:PassRole](#security_iam_troubleshoot-passrole "#security_iam_troubleshoot-passrole")
- [I want to allow people
  outside of my AWS account to access my CloudTrail resources](#security_iam_troubleshoot-cross-account-access "#security_iam_troubleshoot-cross-account-access")
- [I am not authorized to perform
  iam:PassRole](#security_iam_troubleshoot-passrole "#security_iam_troubleshoot-passrole")
- [I am getting a NoManagementAccountSLRExistsException exception when I try to create an organization trail or event data store](#security_iam_troubleshoot-no-slr "#security_iam_troubleshoot-no-slr")

## I am not authorized to

perform an action in CloudTrail

If you receive an error that you're not authorized to perform an action, your
policies must be updated to allow you to perform the action.

The following example error occurs when the `mateojackson` IAM user
tries to use the console to view details about a fictional
`my-example-widget` resource but doesn't
have the fictional `cloudtrail:`GetWidget`` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: cloudtrail:GetWidget on resource: my-example-widget
```

In this case, the policy for the `mateojackson` user must be updated to allow access to the
`my-example-widget` resource by using the
`cloudtrail:`GetWidget`` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

If the AWS Management Console tells you that you're not authorized to perform an action, then you must contact your administrator for assistance. Your administrator is the person that provided you
with your sign-in credentials.

The following example error occurs when the `mateojackson` IAM user
tries to use the console to view details about a trail but doesn't have either the
appropriate CloudTrail managed policy
(**AWSCloudTrail_FullAccess** or
**AWSCloudTrail_ReadOnlyAccess**) or the
equivalent permissions applied to his account.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: cloudtrail:GetTrailStatus on resource: `My-Trail`
```

In this case, Mateo asks his administrator to update his policies to allow him to access trail information and status in the console.

If you sign in with an IAM user or role that has the
**AWSCloudTrail_FullAccess** managed policy or its
equivalent permissions, and you can't configure AWS Config or Amazon CloudWatch Logs integration with a
trail, you might be missing the required permissions for integration with those
services. For more information, see [Granting permission to view AWS Config information on the CloudTrail console](security_iam_id-based-policy-examples.md#grant-aws-config-permissions-for-cloudtrail-users "security_iam_id-based-policy-examples.md#grant-aws-config-permissions-for-cloudtrail-users") and [Granting permission to view and configure Amazon CloudWatch Logs information on the CloudTrail console](security_iam_id-based-policy-examples.md#grant-cloudwatch-permissions-for-cloudtrail-users "security_iam_id-based-policy-examples.md#grant-cloudwatch-permissions-for-cloudtrail-users").

## I am not authorized to perform

`iam:PassRole`

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to CloudTrail.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do
this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in
CloudTrail. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the
role to the service.

```
User: arn:aws:iam::123456789012:user/`marymajor` is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## I want to allow people

outside of my AWS account to access my CloudTrail resources

You can create a role and share CloudTrail information between multiple AWS accounts. For
more information, see [Sharing CloudTrail log files between AWS accounts](cloudtrail-sharing-logs.md "cloudtrail-sharing-logs.md").

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who
is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant
people access to your resources.

To learn more, consult the following:

- To learn whether CloudTrail supports these features, see [How AWS CloudTrail works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").
- To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you
  own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the _IAM User Guide_.
- To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the
  _IAM User Guide_.
- To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the _IAM User Guide_.
- To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the
  _IAM User Guide_.

## I am not authorized to perform

`iam:PassRole`

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to CloudTrail.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do
this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in
CloudTrail. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the
role to the service.

```
User: arn:aws:iam::123456789012:user/`marymajor` is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## I am getting a `NoManagementAccountSLRExistsException` exception when I try to create an organization trail or event data store

The `NoManagementAccountSLRExistsException` exception is thrown when the management account does not have a service-linked role.

When you add a delegated administrator using the AWS Organizations CLI or API operation, CloudTrail service-linked roles won't be created automatically if they don't exist.
The service-linked roles are only created when you make a call from the management account directly to the CloudTrail service. For example, when you add a delegated
administrator or create an organization trail or event data store using the CloudTrail console, AWS CLI or CloudTrail API, the AWSServiceRoleForCloudTrail
service-linked role is created.

When you add a delegated administrator using the AWS CloudTrail; CLI or API operation, CloudTrail will create both the AWSServiceRoleForCloudTrail and
the AWSServiceRoleForCloudTrailEventContext service-linked roles.

When you use your organization's management account to add a delegated administrator or create an
organization trail or event data store in the CloudTrail console, or by using the AWS CLI or CloudTrail
API, CloudTrail automatically creates the AWSServiceRoleForCloudTrail service-linked role for your management account if it does not already exist.
For more information, see [Using service-linked roles for
CloudTrail](using-service-linked-roles.md "using-service-linked-roles.md").

If you haven't added a delegated administrator, use the CloudTrail console, AWS CLI or CloudTrail API to add the delegated administrator. For more information about adding a delegated administrator, see [Add a CloudTrail delegated administrator](cloudtrail-add-delegated-administrator.md "cloudtrail-add-delegated-administrator.md") and [RegisterOrganizationDelegatedAdmin](../APIReference/API_RegisterOrganizationDelegatedAdmin.md "../APIReference/API_RegisterOrganizationDelegatedAdmin.md") (API).

If you've already added the delegated administrator, use the management account to create the organization trail or event data store in the CloudTrail console, or by using the AWS CLI or CloudTrail API. For more information about creating an organization trail, see [Creating a trail for
your organization in the console](creating-an-organizational-trail-in-the-console.md "creating-an-organizational-trail-in-the-console.md"), [Creating a trail for an organization with the AWS CLI](cloudtrail-create-and-update-an-organizational-trail-by-using-the-aws-cli.md "cloudtrail-create-and-update-an-organizational-trail-by-using-the-aws-cli.md"), and [CreateTrail](../APIReference/API_CreateTrail.md "../APIReference/API_CreateTrail.md") (API).
