# Granting access to Resource Explorer views for

search

Before users can search with a new view, you must grant access to AWS Resource Explorer views. To do
this, use an identity-based permission policy to the AWS Identity and Access Management (IAM) principals that need
to search with the view.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:

      + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the *IAM User Guide*.
      + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the *IAM User Guide*.

  You can use either of the following methods:

- **Use an existing AWS managed policy**. Resource Explorer
  provides several pre-defined AWS managed policies for your use. For details of all
  of the available AWS managed policies, see [AWS managed policies for AWS Resource Explorer](security_iam_awsmanpol.md "security_iam_awsmanpol.md").

For example, you could use the `AWSResourceExplorerReadOnlyAccess` policy to
grant search permissions to all views in the account.

- **Create your own permission policy and assign it to the
  principals**. If you create your own policy, you can restrict access to
  a single view, or a subset of the available views by specifying the [Amazon resource name (ARN)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md")
  of each view in the `Resource` element of the policy statement. For
  example, You can use the following example policy to grant that principal the
  ability to search using only that one view.

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
 "Resource": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/MyTestView/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
 }
 ]
}`

```

Use the IAM console to create the permission policies and to use them with the
principals that need those permissions. For more information about IAM permission
policies, see the following topics:

    + [Policies and permissions
     in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md")
    + [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md")
    + [Understanding
     permissions granted by a policy](../../../IAM/latest/UserGuide/access_policies_understand.md "../../../IAM/latest/UserGuide/access_policies_understand.md")

## Using tag-based authorization to

control access to your views

If you choose to create multiple views with filters that return results with only
certain resources, then you might also want to restrict access to those views to only
the principals who need to see those resources. You can provide this type of security
for the views in your account by using an [attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") strategy. The _attributes_ used by ABAC are the tags attached both to the principals
attempting to perform operations in AWS and to the resources they attempt to
access.

ABAC uses standard IAM permission policies attached to the principals. The policies
use `Condition` elements in the policy statements to allow access only when
both the tags attached to the requesting principal and the tags attached to the affected
resource match the requirements in the policy.

For example, you could attach a tag `"Environment" = "Production"` to all
of the AWS resources that support your company's production application. To ensure
that only principals that are authorized to access the production environment can see
those resources, create a Resource Explorer view that uses that tag as a [filter](using-search-query-syntax.md#query-syntax-filters "using-search-query-syntax.md#query-syntax-filters"). Then, to restrict access to the view
to only the appropriate principals, you grant permissions using a policy that has a
condition similar to the following example elements.

```
{
    "Effect": "Allow",
    "Action": [ "`service:Action1`", "`service:Action2`" ],
    "Resource": "arn:aws:`arn-of-a-resource`",
    "Condition": { "StringEquals": {"aws:ResourceTag/`Environment`": "${aws:PrincipalTag/`Environment`}"} }
}
```

That `Condition` in the previous example specifies that the request is
allowed **_only_** if the
`Environment` tag attached to the principal making the request matches
the `Environment` tag attached to the resource specified in the request. If
those two tags don't exactly match, or if either tag is missing, then the Resource Explorer denies
the request.

###### Important

To successfully use ABAC to secure access to your resources, you must first
restrict access to the ability to add or modify the tags attached to your principals
and resources. If a user can add or modify the tags attached an AWS principal or
resource then that user can affect the permissions controlled by those tags. In a
secure ABAC environment, only approved security administrators have permission to
add or modify the tags attached to principals, and only security administrators and
resource owners can add or modify the tags attached to resources.

For more information about how to successfully implement an ABAC strategy, see the
following topics in the _IAM User Guide_:

- [IAM tutorial: Define permissions to access AWS resources based on
  tags](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md")
- [Controlling access to AWS resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md")

After you have the necessary ABAC infrastructure in place, you can use start using
tags to control who can search using the Resource Explorer views in your account. For example
policies that illustrate the principle, see the following example permission
policies:

- [Granting access to a
  view based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-abac-views "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-abac-views")
- [Granting access
  to create a view based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-abac-createview "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-abac-createview")
