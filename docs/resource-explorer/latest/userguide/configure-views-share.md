AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# Sharing Resource Explorer views

Views in AWS Resource Explorer primarily use [resource-based
policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") to grant access. Similar to Amazon S3 bucket policies, these policies are
attached to the view and specify who can use the view. This is in contrast to AWS Identity and Access Management
(IAM) identity-based policies. An IAM identity-based policy is assigned to a role,
group, or user, and it specifies which actions and resources that role, group, or user can
access. You can use either type of policy with Resource Explorer views, as follows:

- Within the management account or delegated administrator account that owns the
  resource, use **_either_** policy
  type to grant access, provided that no other policy explicitly denies access to the
  view for that principal.
- Across accounts, you must use **_both_** policy types. The resource-based policy
  attached to the view in the _sharing_ account turns on sharing
  with another _consuming_ account. However, that policy doesn't
  grant access to the individual users or roles in the consuming account. The
  administrator in the consuming account must also assign an identity-based policy to
  the desired roles and users in the consuming account. That policy grants access to
  the [Amazon resource name (ARN)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") of the view.
  To share views with other accounts, you must use AWS Resource Access Manager (AWS RAM). AWS RAM handles the
  complexity of resource-based policies for you. Before you can share, you must perform the
  following tasks:

- [Turn on multi-account
  search](manage-service-multi-account.md "manage-service-multi-account.md").
- Ensure that your resource-based policy or the IAM identity-based policy you use
  to share and unshare views includes the
  `resource-explorer-2:GetResourcePolicy`,
  `resource-explorer-2:PutResourcePolicy` and
  `resource-explorer-2:DeleteResourcePolicy` permissions.
  To share a view, you must be the organization's management account or a delegated
  administrator. You specify the accounts or identities that you want to share the resource
  with. AWS RAM fully supports Resource Explorer views. AWS RAM uses policies similar to those described in
  the following sections, based on the types of the principals that you choose to share with.
  For instructions on how to share resources, see [Sharing your AWS
  resources](../../../ram/latest/userguide/getting-started-sharing.md "../../../ram/latest/userguide/getting-started-sharing.md") in the _AWS Resource Access Manager User Guide_.

Administrators and delegated administrators can create and share 3 types of views:
organization scope view, organizational unit (OU) scope views, and account-level scope
views. They can share with organizations, OUs, or accounts. When accounts join or leave the
organization, AWS RAM automatically grants or revokes the shared view.

## Permissions policy to share view

with AWS accounts

The following example policy shows how you can make a view available to the principals
in two different AWS accounts:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "`111122223333`",
 "`444455556666`"
 ]
 },
 "Action": [
 "resource-explorer-2:Search",
 "resource-explorer-2:GetView"
 ],
 "Resource": [
 "arn:aws:resource-explorer-2:us-east-1:`123456789012`:view/`policy-name`/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
 ]
 }
 ]
 }`

```

The administrator in each of the specified accounts must now specify which roles and
users can access the view by attaching identity-based permissions policies to the roles,
groups, and users. The administrators of accounts 111122223333 or
444455556666 can create the following example policy. Then, they can assign
the policy to roles, groups, and users in those accounts who are to be allowed to search
using the view shared from the originating account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "resource-explorer-2:Search",
 "resource-explorer-2:GetView"
 ],
 "Resource": [
 "arn:aws:resource-explorer-2:us-east-1:`123456789012`:view/`policy-name`/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
 ]
 }
 ]
 }`

```

You can use these IAM identity-based policies as part of an attribute-based access
control (ABAC) security strategy. In that paradigm, you make sure that all of your
resources and all of your identities are tagged. Then, you specify in your policies
which tag keys and values must match between the identity and the resource for access to
be allowed. For information about tagging the views in your account, see [Adding tags to views](configure-views-tag.md "configure-views-tag.md"). For more
information about attribute-based access control, see [What is
ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") and [Controlling access to AWS resources
using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md"), both in the _IAM User Guide_.
