# Overview of managing access permissions to your

IAM Identity Center resources

Every AWS resource is owned by an AWS account, and permissions to create or access the
resources are governed by permissions policies. To provide access, an account administrator can add permissions to IAM identities (that is, users, groups, and roles). Some services (such as
AWS Lambda) also support adding permissions to resources.

###### Note

An _account administrator_ (or administrator user) is a user with
administrator privileges. For more information, see [IAM best practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the
_IAM User Guide_.

###### Topics

- [IAM Identity Center resources and operations](#creatingiampolicies "#creatingiampolicies")
- [Understanding resource ownership](#accesscontrolresourceowner "#accesscontrolresourceowner")
- [Managing access to resources](#accesscontrolmanagingaccess "#accesscontrolmanagingaccess")
- [Specifying policy elements: actions, effects, resources,
  and principals](#policyactions "#policyactions")
- [Specifying conditions in a policy](#specifyiampolicyconditions "#specifyiampolicyconditions")

## IAM Identity Center resources and operations

In IAM Identity Center, the primary resources are application instances, profiles, and permission
sets.

## Understanding resource ownership

A _resource owner_ is the AWS account that created a resource.
That is, the resource owner is the AWS account of the _principal entity_
(the account, a user, or an IAM role) that authenticates the request that creates the
resource. The following examples illustrate how this works:

- If the AWS account root user creates an IAM Identity Center resource, such as an application instance
  or permission set, your AWS account is the owner of that resource.
- If you create a user in your AWS account and grant that user
  permissions to create IAM Identity Center resources, the user can then create IAM Identity Center resources. However,
  your AWS account, to which the user belongs, owns the resources.
- If you create an IAM role in your AWS account with permissions to create
  IAM Identity Center resources, anyone who can assume the role can create IAM Identity Center resources. Your
  AWS account, to which the role belongs, owns the IAM Identity Center resources.

## Managing access to resources

A _permissions policy_ describes who has access to what. The
following section explains the available options for creating permissions
policies.

###### Note

This section discusses using IAM in the context of IAM Identity Center. It doesn't provide
detailed information about the IAM service. For complete IAM documentation, see
[What is IAM?](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") in the
_IAM User Guide_. For information about IAM policy syntax
and descriptions, see [AWS IAM
policy reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the _IAM User Guide_.

Policies that are attached to an IAM identity are referred to as
_identity-based_ policies (IAM policies). Policies that are attached to
a resource are referred to as _resource-based_ policies. IAM Identity Center supports
only identity-based policies (IAM policies).

###### Topics

- [Identity-based policies (IAM
  policies)](#accesscontrolidentitybased "#accesscontrolidentitybased")
- [Resource-based
  policies](#accesscontrolresourcebased "#accesscontrolresourcebased")

### Identity-based policies (IAM

policies)

You can add permissions to IAM identities. For example, you can do the
following:

- **Attach a permissions policy to a user or a group in
  your AWS account** – An account administrator can use a
  permissions policy that is associated with a particular user to grant
  permissions for that user to add an IAM Identity Center resource, such as a new
  application.
- **Attach a permissions policy to a role (grant
  cross-account permissions)** – You can attach an
  identity-based permissions policy to an IAM role to grant cross-account
  permissions.

For more information about using IAM to delegate permissions, see
[Access management](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in the
_IAM User Guide_.

The following permissions policy grants permissions to a user to run all of the
actions that begin with `List`. These actions show information about an IAM Identity Center
resource, such as an application instance or permissions set. Note that the wildcard
character (\*) in the `Resource` element indicates that the actions are allowed
for all IAM Identity Center resources that are owned by the account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":"sso:List*",
 "Resource":"*"
 }
 ]
}`

```

For more information about using identity-based policies with IAM Identity Center, see [Identity-based policy examples for
IAM Identity Center](iam-auth-access-using-id-policies.md "iam-auth-access-using-id-policies.md"). For more information about
users, groups, roles, and permissions, see [Identities (users, groups, and roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") in the
_IAM User Guide_.

### Resource-based

policies

Other services, such as Amazon S3, also support resource-based permissions policies.
For example, you can attach a policy to an S3 bucket to manage access permissions to
that bucket. IAM Identity Center doesn't support resource-based policies.

## Specifying policy elements: actions, effects, resources,

and principals

For each IAM Identity Center resource (see [IAM Identity Center resources and operations](#creatingiampolicies "#creatingiampolicies")), the service defines a set of API operations.

To grant permissions for these API operations, IAM Identity Center defines a set of actions that you can
specify in a policy. Note that performing an API operation can require permissions for more
than one action.

The following are the basic policy elements:

- **Resource** – In a policy, you use an
  Amazon Resource Name (ARN) to identify the resource to which the policy applies.
- **Action** – You use action keywords to
  identify resource operations that you want to allow or deny. For example, the
  `sso:DescribePermissionsPolicies` permission allows the user
  permissions to perform the IAM Identity Center `DescribePermissionsPolicies`
  operation.
- **Effect** – You specify the effect when
  the user requests the specific action—this can be either allow or deny. If
  you do not explicitly grant access to (allow) a resource, access is implicitly
  denied. You can also explicitly deny access to a resource, which you might do to
  make sure that a user cannot access it, even if a different policy grants
  access.
- **Principal** – In identity-based policies
  (IAM policies), the user that the policy is attached to is the implicit
  principal. For resource-based policies, you specify the user, account, service,
  or other entity that you want to receive permissions (applies to resource-based
  policies only). IAM Identity Center doesn't support resource-based policies.

To learn more about IAM policy syntax and descriptions, see [AWS IAM policy reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in
the _IAM User Guide_.

## Specifying conditions in a policy

When you grant permissions, you can use the access policy language to specify the
conditions that are required for a policy to take effect. For example, you might want a policy
to be applied only after a specific date. For more information about specifying conditions in
a policy language, see [Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.

To express conditions, you use predefined condition keys. There are no condition keys
specific to IAM Identity Center. However, there are AWS condition keys that you can use as appropriate.
For a complete list of AWS keys, see [Available global condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#AvailableKeys") in the _IAM User Guide_.
