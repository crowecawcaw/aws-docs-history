# Rename an IAM user

###### Note

As a [best practice](best-practices.md "best-practices.md"), we recommend that you require
human users to use federation with an identity provider to access AWS using temporary
credentials. If you follow the best practices, you are not managing IAM users and groups.
Instead, your users and groups are managed outside of AWS and are able to access AWS
resources as a _federated identity_. A federated identity is a user from
your enterprise user directory, a web identity provider, the AWS Directory Service, the
Identity Center directory, or any user that accesses AWS services by using credentials
provided through an identity source. Federated identities use the groups defined by their
identity provider. If you are using AWS IAM Identity Center, see [Manage identities
in IAM Identity Center](../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md "../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md") in the _AWS IAM Identity Center User Guide_ for information about creating
users and groups in IAM Identity Center.

Amazon Web Services offers multiple tools for managing the IAM users in your AWS account. You can
list the IAM users in your account or in a user group, or list all IAM groups that a user is
a member of. You can rename or change the path of an IAM user. If you are moving to using
federated identities instead of IAM users, you can delete an IAM user from your AWS
account, or deactivate the user.

For more information about adding, changing, or removing managed policies for an IAM user,
see [Change permissions for an IAM user](id_users_change-permissions.md "id_users_change-permissions.md").
For information about managing inline policies for IAM users, see [Adding and removing IAM identity
permissions](access_policies_manage-attach-detach.md "access_policies_manage-attach-detach.md"), [Edit IAM policies](access_policies_manage-edit.md "access_policies_manage-edit.md"), and [Delete IAM policies](access_policies_manage-delete.md "access_policies_manage-delete.md"). As a
best practice, use managed policies instead of inline policies. _AWS managed
policies_ grant permissions for many common use cases. Keep in mind that AWS
managed policies might not grant least-privilege permissions for your specific use cases because
they are available for use by all AWS customers. As a result, we recommend that you reduce
permissions further by defining [customer managed policies](access_policies_managed-vs-inline.md#customer-managed-policies "access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases. For more information,
see [AWS managed policies](access_policies_managed-vs-inline.md#aws-managed-policies "access_policies_managed-vs-inline.md#aws-managed-policies"). For more
information about AWS managed policies that are designed for specific job functions, see [AWS managed policies for job functions](access_policies_job-functions.md "access_policies_job-functions.md").

To learn about validating IAM policies, see [IAM policy validation](access_policies_policy-validator.md "access_policies_policy-validator.md").

###### Tip

[IAM Access Analyzer](what-is-access-analyzer.md "what-is-access-analyzer.md") can analyze the services and actions that your IAM roles use, and
then generate a fine-grained policy that you can use. After you test each generated policy,
you can deploy the policy to your production environment. This ensures that you grant only the
required permissions to your workloads. For more information about policy generation, see
[IAM Access Analyzer policy
generation](access-analyzer-policy-generation.md "access-analyzer-policy-generation.md").

For information about managing IAM user passwords, see [Manage passwords for
IAM users](id_credentials_passwords_admin-change-user.md "id_credentials_passwords_admin-change-user.md").

## Renaming an IAM user

To change a user's name or path, you must use the AWS CLI, Tools for Windows PowerShell, or AWS API. There is no
option in the console to rename a user. For information about the permissions that you need in
order to rename a user, see [Permissions required to access IAM
resources](access_permissions-required.md "access_permissions-required.md").

When you change a user's name or path, the following happens:

- Any policies attached to the user stay with the user under the new name.
- The user stays in the same IAM groups under the new name.
- The unique ID for the user remains the same. For more information about unique IDs,
  see [Unique identifiers](reference_identifiers.md#identifiers-unique-ids "reference_identifiers.md#identifiers-unique-ids").
- Any resource or role policies that refer to the user _as a
  principal_ (the user is being granted access) are automatically updated to use
  the new name or path. For example, any queue-based policies in Amazon SQS or resource-based
  policies in Amazon S3 are automatically updated to use the new name and path.

IAM does not automatically update policies that refer to the user _as a
resource_ to use the new name or path; you must manually do that. For example,
imagine that user `Richard` has a policy attached to him that lets him manage his
security credentials. If an administrator renames `Richard` to `Rich`,
the administrator also needs to update that policy to change the resource from this:

```
arn:aws:iam::111122223333:user/division_abc/subdivision_xyz/Richard
```

to this:

```
arn:aws:iam::111122223333:user/division_abc/subdivision_xyz/Rich
```

This is true also if an administrator changes the path; the administrator needs to update
the policy to reflect the new path for the user.

### To rename a user

- AWS CLI: [aws iam
  update-user](../../../cli/latest/reference/iam/update-user.md "../../../cli/latest/reference/iam/update-user.md")
- AWS API: [UpdateUser](../APIReference/API_UpdateUser.md "../APIReference/API_UpdateUser.md")
