# Overview of managing access permissions to your ElastiCache resources

Every AWS resource is owned by an AWS account, and permissions to create or access a
resource are governed by permissions policies. An account administrator can attach
permissions policies to IAM identities (that is, users, groups, and roles). In addition,
Amazon ElastiCache also supports attaching permissions policies to
resources.

###### Note

An _account administrator_ (or administrator user) is a user
with administrator privileges. For more information, see [IAM Best
Practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

###### Topics

- [Amazon ElastiCache resources and operations](#IAM.Overview.ResourcesAndOperations "#IAM.Overview.ResourcesAndOperations")
- [Understanding resource ownership](#access-control-resource-ownership "#access-control-resource-ownership")
- [Managing access to resources](#IAM.Overview.ManagingAccess "#IAM.Overview.ManagingAccess")
- [AWS managed policies for Amazon ElastiCache](IAM.IdentityBasedPolicies.md "IAM.IdentityBasedPolicies.md")
- [Using identity-based policies (IAM policies) for Amazon ElastiCache](IAM.md "IAM.md")
- [Resource-level permissions](IAM.md "IAM.md")
- [Using condition keys](IAM.md "IAM.md")
- [Using Service-Linked Roles for
  Amazon ElastiCache](using-service-linked-roles.md "using-service-linked-roles.md")
- [ElastiCache API permissions: Actions, resources, and conditions reference](IAM.md "IAM.md")

## Amazon ElastiCache resources and operations

To see a list of ElastiCache resource types and their ARNs, see [Resources Defined by Amazon ElastiCache](../../../service-authorization/latest/reference/list_amazonelasticache.md#amazonelasticache-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonelasticache.md#amazonelasticache-resources-for-iam-policies") in the
_Service Authorization Reference_. To learn with which actions you can specify the ARN of each resource, see
[Actions Defined by Amazon ElastiCache](../../../service-authorization/latest/reference/list_amazonelasticache.md#amazonelasticache-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonelasticache.md#amazonelasticache-actions-as-permissions").

## Understanding resource ownership

A _resource owner_ is the AWS account that created the resource. That
is, the resource owner is the AWS account of the principal
entity that authenticates the request that creates the resource. A
_principal entity_ can be the root account, an IAM user, or
an IAM role). The following examples illustrate how this works:

- Suppose that you use the root account credentials of your AWS account to create a cache
  cluster. In this case, your AWS account is the owner of the resource. In
  ElastiCache, the resource is the cluster.
- Suppose that you create an IAM user in your AWS account and grant permissions to
  create a cluster to that user. In this case, the user can create a
  cluster. However, your AWS account, to which the user belongs, owns
  the cluster resource.
- Suppose that you create an IAM role in your AWS account with permissions to create a
  cluster. In this case, anyone who can assume the role can create a
  cluster. Your AWS account, to which the role belongs, owns the cache
  cluster resource.

## Managing access to resources

A _permissions policy_ describes who has access to what. The
following section explains the available options for creating permissions
policies.

###### Note

This section discusses using IAM in the context of Amazon ElastiCache. It doesn't
provide detailed information about the IAM service. For complete IAM
documentation, see [What Is
IAM?](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") in the _IAM User Guide_. For information
about IAM policy syntax and descriptions, see [AWS IAM
Policy Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the _IAM User Guide_.

Policies attached to an IAM identity are referred to as
_identity-based_ policies (IAM policies). Policies attached
to a resource are referred to as _resource-based_ policies.

###### Topics

- [Identity-based policies (IAM policies)](#IAM.Overview.ManagingAccess.IdentityBasedPolicies "#IAM.Overview.ManagingAccess.IdentityBasedPolicies")
- [Specifying policy elements: Actions, effects, resources, and principals](#IAM.Overview.PolicyElements "#IAM.Overview.PolicyElements")
- [Specifying conditions in a policy](#IAM.Overview.Conditions "#IAM.Overview.Conditions")

### Identity-based policies (IAM policies)

You can attach policies to IAM identities. For example, you can do the following:

- **Attach a permissions policy to a user or a group in your
  account** – An account administrator can use a
  permissions policy that is associated with a particular user to grant
  permissions. In this case, the permissions are for that user to create
  an ElastiCache resource, such as a cluster, parameter group, or security
  group.
- **Attach a permissions policy to a role
  (grant cross-account permissions)** – You can attach an
  identity-based permissions policy to an IAM role to grant cross-account
  permissions. For example, the administrator in Account A can create a
  role to grant cross-account permissions to another AWS account (for
  example, Account B) or an AWS service as follows:

      1. Account A administrator creates an IAM role and attaches a
       permissions policy to the role that grants permissions on
       resources in Account A.
      2. Account A administrator attaches a trust policy to the role
       identifying Account B as the principal who can assume the role.
      3. Account B administrator can then delegate permissions to assume the role to any users
       in Account B. Doing this allows users in Account B to create or
       access resources in Account A. In some cases, you might want to
       grant an AWS service permissions to assume the role. To support
       this approach, the principal in the trust policy can also be an
       AWS service principal.

  For more information about using IAM to delegate permissions, see
  [Access
  Management](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in the _IAM User Guide_.

The following is an example policy that allows a user to perform the
`DescribeCacheClusters` action for your AWS account. ElastiCache also supports identifying specific resources
using the resource ARNs for API actions. (This approach is also referred to as
resource-level permissions).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DescribeCacheClusters",
 "Effect": "Allow",
 "Action": [
 "elasticache:DescribeCacheClusters"
 ],
 "Resource": "arn:aws:iam::*:role/*"
 }
 ]
}`

```

For more information about using identity-based policies with ElastiCache, see [Using identity-based policies (IAM policies) for Amazon ElastiCache](IAM.md "IAM.md"). For more information about
users, groups, roles, and permissions, see [Identities (Users,
Groups, and Roles](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") in the _IAM User Guide_.

### Specifying policy elements: Actions, effects, resources, and principals

For each Amazon ElastiCache resource (see [Amazon ElastiCache resources and operations](#IAM.Overview.ResourcesAndOperations "#IAM.Overview.ResourcesAndOperations")), the service defines a
set of API operations (see [Actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md")). To grant permissions for these API operations, ElastiCache defines
a set of actions that you can specify in a policy. For example, for the ElastiCache
cluster resource, the following actions are defined:
`CreateCacheCluster`, `DeleteCacheCluster`, and
`DescribeCacheCluster`. Performing an API operation can require
permissions for more than one action.

The following are the most basic policy elements:

- **Resource** – In a policy, you use
  an Amazon Resource Name (ARN) to identify the resource to which the policy
  applies. For more information, see [Amazon ElastiCache resources and operations](#IAM.Overview.ResourcesAndOperations "#IAM.Overview.ResourcesAndOperations").
- **Action** – You use action keywords
  to identify resource operations that you want to allow or deny. For example,
  depending on the specified `Effect`, the
  `elasticache:CreateCacheCluster`
  permission allows or denies the user permissions to perform the Amazon ElastiCache
  `CreateCacheCluster` operation.
- **Effect** – You specify the effect when the user
  requests the specific action—this can be either allow or deny. If you
  don't explicitly grant access to (allow) a resource, access is implicitly
  denied. You can also explicitly deny access to a resource. For example, you
  might do this to make sure that a user can't access a resource, even if
  a different policy grants access.
- **Principal** – In
  identity-based policies (IAM policies), the user that the policy is
  attached to is the implicit principal. For resource-based
  policies, you specify the user, account, service, or other entity that you
  want to receive permissions (applies to resource-based policies only).

To learn more about IAM policy syntax and descriptions, see [AWS IAM
Policy Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the _IAM User Guide_.

For a table showing all of the Amazon ElastiCache API actions, see [ElastiCache API permissions: Actions, resources, and conditions reference](IAM.md "IAM.md").

### Specifying conditions in a policy

When you grant permissions, you can use the IAM policy language to specify the
conditions when a policy should take effect. For example, you might want a policy to
be applied only after a specific date. For more information about specifying
conditions in a policy language, see [Condition](../../../IAM/latest/UserGuide/reference_policies_elements.md#Condition "../../../IAM/latest/UserGuide/reference_policies_elements.md#Condition") in the _IAM User Guide_.

To express conditions, you use predefined condition keys. To use ElastiCache-specific condition keys, see [Using condition keys](IAM.md "IAM.md"). There are AWS-wide condition keys that you can
use as appropriate. For a complete list of AWS-wide keys, see [Available Keys for Conditions](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the _IAM User Guide_.
