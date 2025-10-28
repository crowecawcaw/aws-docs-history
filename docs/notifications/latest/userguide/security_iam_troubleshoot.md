# Troubleshooting AWS User Notifications identity

and access

Use the following information to help you diagnose and fix common issues that you might
encounter when working with User Notifications and IAM.

###### Topics

- [I Am Not Authorized to
  Perform an Action in User Notifications](#security_iam_troubleshoot-no-permissions "#security_iam_troubleshoot-no-permissions")
- [I'm an Administrator and Want
  to Allow Others to Access User Notifications](#security_iam_troubleshoot-admin-delegate "#security_iam_troubleshoot-admin-delegate")
- [I Want to Allow People
  Outside of My AWS Account to Access My User Notifications Resources](#security_iam_troubleshoot-cross-account-access "#security_iam_troubleshoot-cross-account-access")

## I Am Not Authorized to

Perform an Action in User Notifications

If the AWS Management Console tells you that you're not authorized to perform an action, then you
must contact your administrator for assistance. Your administrator is the person that
provided you with your user name and password.

The following example error occurs when the `mateojackson` IAM user
tries to use the console to view details about a notification configuration, but
does not have `notifications:`GetNotificationConfiguration``
permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: notifications:`GetNotificationConfiguration` on resource: `my-example-notificationconfiguration`
```

In this case, Mateo asks his administrator to update his policies to allow him to
access the `my-example-notificationconfiguration` resource using the
`notifications:`GetNotificationConfiguration``
action.

## I'm an Administrator and Want

to Allow Others to Access User Notifications

To allow others to access User Notifications, you must grant permission to the people or applications that need access. If you are using AWS IAM Identity Center
to manage people and applications, you assign permission sets to users or groups to define their level of access. Permission sets automatically create
and assign IAM policies to IAM roles that are associated with the person or application. For more information, see [Permission sets](../../../singlesignon/latest/userguide/permissionsetsconcept.md "../../../singlesignon/latest/userguide/permissionsetsconcept.md") in the _AWS IAM Identity Center User Guide_.

If you are not using IAM Identity Center, you must create IAM entities (users or roles) for the people or applications that need access. You must then attach
a policy to the entity that grants them the correct permissions in User Notifications. After the permissions are granted, provide the credentials to the user
or application developer. They will use those credentials to access AWS. To learn more about creating IAM users, groups, policies, and permissions,
see [IAM Identities](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") and [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.

## I Want to Allow People

Outside of My AWS Account to Access My User Notifications Resources

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who
is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant
people access to your resources.

To learn more, consult the following:

- To learn whether User Notifications supports these features, see [How AWS User Notifications works with
  IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").
- To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you
  own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the _IAM User Guide_.
- To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the
  _IAM User Guide_.
- To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the _IAM User Guide_.
- To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the
  _IAM User Guide_.
