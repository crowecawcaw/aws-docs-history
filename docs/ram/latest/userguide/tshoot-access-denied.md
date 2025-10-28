# Error: "AccessDeniedException"

## Scenario

You get an **`Access Denied`** exception when trying to share a
resource or view a resource share.

## Cause

You can receive this error if you attempt to create a resource share when you
don't have the required permissions. This can be caused by insufficient permissions
in policies attached to your AWS Identity and Access Management (IAM) principal. It can also happen because
of restrictions in place from an AWS Organizations service control policy (SCP) that affects
your AWS account.

## Solution

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

To resolve the error, you need to ensure the permissions are granted by
`Allow` statements in the permission policy used by the principal
that makes the request. In addition, the permissions must not be blocked by your
organization’s SCPs.

To **create** a resource share, you need the
following two permissions:

- `ram:CreateResourceShare`

- `ram:AssociateResourceShare`

To **view** a resource share, you need the following
permission:

- `ram:GetResourceShares`

To **attach permissions** to a resource share, you
need the following permission:

- ``resourceOwningService`:`PutPolicyAction``

This is a placeholder. You must replace it with the "PutPolicy" permission
(or equivalent) for the service that owns the resource that you want to
share. For example, if you are sharing a Route 53 resolver rule, then the
required permission would be:
`route53resolver:PutResolverRulePolicy`. If you want to allow
the creation of a resource share that contains multiple resource types, then
you must include the relevant permission for each resource type that you
want to permit.

The following example shows what such an IAM permission policy might look
like.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ram:CreateResourceShare",
 "ram:AssociateResourceShare",
 "ram:GetResourceShares",
 "``resourceOwningService`:`PutPolicyAction``"
 ],
 "Resource": "*"
 }
 ]
}`

```
