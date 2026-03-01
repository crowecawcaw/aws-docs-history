# Troubleshooting AWS AppSync identity and access

Use the following information to help you diagnose and fix common issues that you might
encounter when working with AWS AppSync and IAM.

## I am not authorized to perform an action in AWS AppSync

If the AWS Management Console tells you that you're not authorized to perform an action, then you must contact your
administrator for assistance. Your administrator is the person that provided you with your user name and
password.

The following example error occurs when the
IAM
user `mateojackson`
tries to use the console to view details about a fictional
`my-example-widget`
resource, but
he does not have the
fictional `appsync:`GetWidget`` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: appsync:`GetWidget` on resource: `my-example-widget`
```

In this case, Mateo asks his administrator to update his policies to allow him to access the
`my-example-widget` resource using the
`appsync:`GetWidget`` action.

## I am not authorized to perform iam:PassRole

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to AWS AppSync.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do
this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in
AWS AppSync. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the
role to the service.

```
User: arn:aws:iam::123456789012:user/`marymajor` is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## I want to view my access keys

After you create your IAM user access keys, you can view your access key ID at any time. However, you can't view your secret access key again.
If you lose your secret key, you must create a new access key pair.

Access keys consist of two parts: an access key ID (for example, `AKIAIOSFODNN7EXAMPLE`) and a secret access key (for example,
`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`). Like a user name and password, you must use both the access key ID and secret access key
together to authenticate your requests. Manage your access keys as securely as you do your user name and password.

###### Important

Do not provide your access keys to a third party, even to help [find your canonical user ID](../../../accounts/latest/reference/manage-acct-identifiers.md#FindCanonicalId "../../../accounts/latest/reference/manage-acct-identifiers.md#FindCanonicalId").
By doing this, you might give someone permanent access to your AWS account.

When you create an access key pair, you are prompted to save the access key ID and secret access key in a secure location. The secret access key
is available only at the time you create it. If you lose your secret access key, you must add new access keys to your IAM user. You can have a
maximum of two access keys. If you already have two, you must delete one key pair before creating a new one. To view instructions, see [Managing access keys](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_CreateAccessKey "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_CreateAccessKey") in the
_IAM User Guide_.

## I'm an administrator and want to allow others to access AWS AppSync

To allow others to access AWS AppSync, you must grant permission to the people or applications that need access. If you are using AWS IAM Identity Center
to manage people and applications, you assign permission sets to users or groups to define their level of access. Permission sets automatically create
and assign IAM policies to IAM roles that are associated with the person or application. For more information, see [Permission sets](../../../singlesignon/latest/userguide/permissionsetsconcept.md "../../../singlesignon/latest/userguide/permissionsetsconcept.md") in the _AWS IAM Identity Center User Guide_.

If you are not using IAM Identity Center, you must create IAM entities (users or roles) for the people or applications that need access. You must then attach
a policy to the entity that grants them the correct permissions in AWS AppSync. After the permissions are granted, provide the credentials to the user
or application developer. They will use those credentials to access AWS. To learn more about creating IAM users, groups, policies, and permissions,
see [IAM Identities](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") and [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.

## I want to allow people outside of my AWS account to access my AWS AppSync resources

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who
is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant
people access to your resources.

To learn more, consult the following:

- To learn whether AWS AppSync supports these features, see [How AWS AppSync works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").
- To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you
  own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the _IAM User Guide_.
- To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") in the
  _IAM User Guide_.
- To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the _IAM User Guide_.
- To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the
  _IAM User Guide_.
