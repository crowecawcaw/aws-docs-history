# Identity and access management for

License Manager

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be authenticated (signed in) and
authorized (have permissions) to use AWS resources. With IAM you can create users and
groups under your AWS account. You control the permissions that users have to perform
tasks using AWS resources. You can use IAM for no additional charge.

By default, users don't have permissions for License Manager resources and operations. To allow
users to manage License Manager resources, you must create an IAM policy that explicitly grants them
permissions.

When you attach a policy to a user or group of users, it allows or denies the users
permission to perform the specified tasks on the specified resources. For more information,
see [Policies and Permissions](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the
_IAM User Guide_ guide.

## Create users, groups, and

roles

You can create users and groups for your AWS account and then assign them the
permissions they require. As a best practice, users should acquire the permissions by
assuming IAM roles. For more information on how to set up users and groups for your
AWS account, see [Get started with License Manager](getting-started.md "getting-started.md").

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an IAM identity that
you can create in your account that has specific permissions. An IAM role is similar to
an IAM user in that it is an AWS identity with permissions policies that determine
what the identity can and cannot do in AWS. However, instead of being uniquely associated
with one person, a role is intended to be assumable by anyone who needs it. Also, a role
does not have standard long-term credentials such as a password or access keys associated
with it. Instead, when you assume a role, it provides you with temporary security credentials
for your role session.

## IAM policy structure

An IAM policy is a JSON document that consists of one or more statements. Each
statement is structured as follows.

```
{
  "Statement":[{
    "Effect":"`effect`",
    "Action":"`action`",
    "Resource":"`arn`",
    "Condition":{
      "`condition`":{
        "`key`":"`value`"
        }
      }
    }
  ]
}
```

Various elements make up a statement:

- **Effect:** The _effect_ can be `Allow` or
  `Deny`. By default, users don't have permission to use resources
  and API operations, so all requests are denied. An explicit _allow_ overrides the default. An explicit _deny_ overrides any allows.
- **Action**: The _action_ is the specific
  API operation for which you are granting or denying permission.
- **Resource**: The resource is affected by the action. Some
  License Manager API operations allow you to include specific resources in your policy that
  can be created or modified by the operation. To specify a resource in the
  statement, you need to use its Amazon Resource Name (ARN). For more information,
  see [Actions Defined by AWS License Manager](../../../IAM/latest/UserGuide/list_awslicensemanager.md#awslicensemanager-actions-as-permissions "../../../IAM/latest/UserGuide/list_awslicensemanager.md#awslicensemanager-actions-as-permissions").
- **Condition**: Conditions are optional. They can be used to
  control when your policy is in effect. For more information, see [Condition Keys for AWS License Manager](../../../IAM/latest/UserGuide/list_awslicensemanager.md#awslicensemanager-policy-keys "../../../IAM/latest/UserGuide/list_awslicensemanager.md#awslicensemanager-policy-keys").

## Create IAM policies for License Manager

In an IAM policy statement, you can specify any API operation from any service that
supports IAM. License Manager, uses the following prefixes with the name of the API
operation:

- `license-manager:`
- `license-manager-user-subscriptions:`
- `license-manager-linux-subscriptions:`

For example:

- `license-manager:CreateLicenseConfiguration`
- `license-manager:ListLicenseConfigurations`
- `license-manager-user-subscriptions:ListIdentityProviders`
- `license-manager-linux-subscriptions:ListLinuxSubscriptionInstances`

For more information on the available License Manager APIs, see the following API
references:

- [AWS License Manager API
  Reference](../APIReference/Welcome.md "../APIReference/Welcome.md")
- [AWS License Manager User Subscriptions API Reference](../../../license-manager-user-subscriptions/latest/APIReference/Welcome.md "../../../license-manager-user-subscriptions/latest/APIReference/Welcome.md")
- [AWS License Manager Linux Subscriptions API Reference](../../../license-manager-linux-subscriptions/latest/APIReference/Welcome.md "../../../license-manager-linux-subscriptions/latest/APIReference/Welcome.md")

To specify multiple operations in a single statement, separate them with commas as
follows:

```
"Action": ["license-manager:*action1*", "license-manager:*action2*"]
```

You can also specify multiple operations using wildcards. For example, you can specify
all License Manager API operations whose name begins with the word _List_ as follows:

```
"Action": "license-manager:List*"
```

To specify all License Manager API operations, use the \* wildcard as follows:

```
"Action": "license-manager:*"
```

### Example policy for an ISV using

License Manager

ISVs that distribute licenses through License Manager require the following
permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "license-manager:CreateLicense",
 "license-manager:ListLicenses",
 "license-manager:CreateLicenseVersion",
 "license-manager:ListLicenseVersions",
 "license-manager:GetLicense",
 "license-manager:DeleteLicense",
 "license-manager:CheckoutLicense",
 "license-manager:CheckInLicense",
 "kms:GetPublicKey"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Grant permissions to users, groups, and

roles

Once you have created the IAM policies you require, you must grant these permissions to your users, groups, and roles.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.
