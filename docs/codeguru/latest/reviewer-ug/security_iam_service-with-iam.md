As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Overview of managing access permissions

to your CodeGuru Reviewer resources

Every AWS resource is owned by an AWS account, and permissions to create or access
a resource are governed by permissions policies. An account administrator can attach
permissions policies to IAM identities (that is, users, groups, and roles).

###### Note

An account administrator (or administrator user) is a user with administrator
privileges. For more information, see [Security best practices in
IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

When you grant permissions, you decide who is getting the permissions, the resources
they can access, and the actions that can be performed on those resources.

###### Topics

- [CodeGuru Reviewer resources and operations](#arn-formats "#arn-formats")
- [Understanding resource
  ownership](#understanding-resource-ownership "#understanding-resource-ownership")
- [Managing access to resources](#managing-access-resources "#managing-access-resources")
- [Specifying policy elements: actions,
  effects, and principals](#actions-effects-principals "#actions-effects-principals")

## CodeGuru Reviewer resources and operations

In Amazon CodeGuru Reviewer, the primary resources are repository associations and code reviews.
In a policy, you use an Amazon Resource Name (ARN) to identify the resource the
policy applies to. In the following ARNs, the repository association ID and the code
review ID are universally unique identifiers (UUIDs). For more information, see
[Amazon Resource Names (ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") in the
_Amazon Web Services General Reference_.

| Resource type                                                                                                         | ARN format                                                                                     |
| --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| [Repository association](../reviewer-api/API_RepositoryAssociation.md "../reviewer-api/API_RepositoryAssociation.md") | `arn:aws:codeguru-reviewer:`region-ID`:`account-ID`:association:`repository-association-uuid`` |
| [Code<br>review](../reviewer-api/API_CodeReview.md "../reviewer-api/API_CodeReview.md")                               | `arn:aws:codeguru-reviewer:`region-ID`:`account-ID`:code-review:`code-review-uuid``            |

For example, you can indicate a specific repository association with id
`my-repository-association-id` in your statement using
its ARN, as follows.

```
"Resource": "arn:aws:codeguru-reviewer:`us-east-2`:`123456789012`:association:`my-repository-association-id`"
```

To specify all resources, or if an API action does not support ARNs, use the
wildcard character (\*) in the `Resource` element, as follows.

```
"Resource": "*"
```

To specify multiple resources in a single statement, separate their ARNs with
commas, as follows.

```
"Resource": [
     "arn:aws:codeguru-reviewer:`us-east-2`:`123456789012`:association:`my-repository-association-id-1`",
     "arn:aws:codeguru-reviewer:`us-east-2`:`123456789012`:association:`my-repository-association-id-2`"
   ]
```

CodeGuru Reviewer provides a set of operations to work with the CodeGuru Reviewer resources. For a list,
see [Amazon CodeGuru Reviewer permissions
reference](auth-and-access-control-permissions-reference.md "auth-and-access-control-permissions-reference.md").

## Understanding resource

ownership

The AWS account owns the resources that are created in it, regardless of who
created the resources. Specifically, the resource owner is the AWS account of the
[principal
entity](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md") (that is, the root account, user, or an IAM role) that
authenticates the resource creation request. The following examples illustrate how
this works:

- If you use the root account credentials of your AWS account to create a
  rule, your AWS account is the owner of the CodeGuru Reviewer resource.
- If you grant permissions to
  create CodeGuru Reviewer resources to a user, the user can create CodeGuru Reviewer resources.
  However, your AWS account, to which the user belongs, owns the CodeGuru Reviewer
  resources.
- If you create an IAM role in your AWS account with permissions to
  create CodeGuru Reviewer resources, anyone who can assume the role can create CodeGuru Reviewer
  resources. Your AWS account, to which the role belongs, owns the CodeGuru Reviewer
  resources.

## Managing access to resources

A permissions policy describes who has access to which resources.

###### Note

This section discusses the use of IAM in CodeGuru Reviewer. It doesn't
provide detailed information about the IAM service. For complete IAM
documentation, see [What is IAM?](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") in the
_IAM User Guide_. For information about IAM policy
syntax and descriptions, see [IAM JSON policy
reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the _IAM User Guide_.

Policies attached to an IAM identity are referred to as _identity-based
policies_ (IAM policies). Policies attached to a resource are
referred to as _resource-based policies_. CodeGuru Reviewer supports
identity-based (IAM policies) only.

### Identity-based policies

You can attach policies to IAM identities. To grant a user permissions to
view repository associations and code reviews in the CodeGuru Reviewer console, you can
attach a permissions policy to a role that the user has. For IAM best practices,
see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the
_IAM User Guide_.

In CodeGuru Reviewer, identity-based policies are used to manage permissions to the
resources related to associated repositories and code reviews. For example, you
can control access to code reviews.

You can create IAM policies to restrict the calls and resources that users
in your account have access to, and then attach those policies to IAM roles that users can use.
For more information about how to create IAM roles and to explore example
IAM policy statements for CodeGuru Reviewer, see [Customer managed policy
examples](auth-and-access-control-iam-identity-based-access-control.md#security_iam_id-based-policy-examples "auth-and-access-control-iam-identity-based-access-control.md#security_iam_id-based-policy-examples").

## Specifying policy elements: actions,

effects, and principals

For each CodeGuru Reviewer resource, the service defines a set of API operations. To grant
permissions for these API operations, CodeGuru Reviewer defines a set of actions that you can
specify in a policy. Some API operations can require permissions for more than one
action to perform the API operation. For more information, see [CodeGuru Reviewer resources and operations](#arn-formats "#arn-formats") and [Amazon CodeGuru Reviewer permissions
reference](auth-and-access-control-permissions-reference.md "auth-and-access-control-permissions-reference.md").

The following are the basic policy elements:

- Resource – You use an ARN to
  identify the resource that the policy applies to.
- Action – You use action keywords to
  identify resource operations to allow or deny. For example, the
  `codeguru-reviewer:DisassociateRepository` permission gives the user
  permissions to perform the `DisassociateRepository` operation.
- Effect – You specify the effect,
  either allow or deny, when the user requests the action. If you don't
  explicitly grant access to (allow) a resource, access is implicitly denied.
  You can also explicitly deny access to a resource. You might do this to make
  sure that a user cannot access a resource, even if a different policy grants
  access.
- Principal – In identity-based
  policies (IAM policies), the user the policy is attached to is the
  implicit principal. For resource-based policies, you specify the user,
  account, service, or other entity that you want to receive
  permissions.

To learn more about IAM policy syntax and descriptions, see [IAM JSON policy reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md")
in the _IAM User Guide_.

For a table showing all of the CodeGuru Reviewer API actions and the resources they apply to,
see [Amazon CodeGuru Reviewer permissions
reference](auth-and-access-control-permissions-reference.md "auth-and-access-control-permissions-reference.md").
