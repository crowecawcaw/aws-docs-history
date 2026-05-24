# Set up your account

This section describes what you need to do to use Amazon Location Service. You must have an
AWS account and have set up access to Amazon Location for users that want to use it.

### Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

**Grant access to Amazon Location Service**

Your non-admin users have no permissions by default. Before they can access
Amazon Location, you must grant permission by attaching an IAM policy with specific
permissions. Make sure to follow the principle of least privilege when granting
access to resources.

###### Note

For information about giving unauthenticated users access to Amazon Location Service
functionality (for example, in a web-based application), see [Authenticate with Amazon Location Service](access.md "access.md").

The following example policy gives a user permission to access all Amazon Location
operations. For more examples, see [Identity-based policy examples for Amazon Location Service](security-iam.md#security_iam_id-based-policy-examples "security-iam.md#security_iam_id-based-policy-examples").

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "geo:*",
        "geo-maps:*",
        "geo-places:*",
        "geo-routes:*"
      ],
      "Resource": "*",
      "Effect": "Allow"
    }
  ]
}
```

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:

      + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the *IAM User Guide*.
      + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the *IAM User Guide*.

  When creating applications that use Amazon Location Service, you may need some users to have
  unauthenticated access. For these use cases, see [Enabling unauthenticated access using
  Amazon Cognito](authenticating-using-cognito.md "authenticating-using-cognito.md").
