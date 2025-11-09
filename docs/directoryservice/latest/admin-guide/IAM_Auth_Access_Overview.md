# Overview of managing access permissions to

your AWS Directory Service resources

Every AWS resource is owned by an AWS account. As a result, permissions to create
or access the resources are governed by permissions policies. However, an account
administrator, which is a user with administrator permissions, can attach permissions to
resources. The also have the ability to attach permissions policies to IAM identities,
such as users, groups, and roles, and some services, such as AWS Lambda also support
attaching permissions policies to resources.

###### Note

For information about the account administrator role, see [IAM best practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the
_IAM User Guide_.

###### Topics

- [AWS Directory Service resources and operations](#CreatingIAMPolicies_DS "#CreatingIAMPolicies_DS")
- [Understanding resource
  ownership](#IAM_Auth_Access_ResourceOwner "#IAM_Auth_Access_ResourceOwner")
- [Managing access to
  resources](#IAM_Auth_Access_ManagingAccess "#IAM_Auth_Access_ManagingAccess")
- [Specifying policy elements: Actions,
  effects, resources, and principals](#SpecifyingIAMPolicyActions_DS "#SpecifyingIAMPolicyActions_DS")
- [Specifying conditions in a
  policy](#SpecifyingIAMPolicyConditions_DS "#SpecifyingIAMPolicyConditions_DS")

## AWS Directory Service resources and operations

In AWS Directory Service, the primary resource is a _directory_. Because AWS Directory Service
supports directory snapshot resources, you can create snapshots only in the context
of an existing directory. This snapshot is referred to as a
_subresource_.

These resources have unique Amazon Resource Names (ARNs) associated with them as
shown in the following table.

| **Resource Type** | **ARN Format**                                                       |
| ----------------- | -------------------------------------------------------------------- |
| Directory         | `arn:aws:ds:`region`:`account-id`:directory/`external-directory-id`` |
| Snapshot          | `arn:aws:ds:`region`:`account-id`:snapshot/`external-snapshot-id``   |

AWS Directory Service includes two service namespaces based on the type of operations that you
perform.

- The `ds` service namespace provides a set of operations to work
  with the appropriate resources. For a list of available operations, see
  [Directory
  Service Actions](../devguide/API_Operations.md "../devguide/API_Operations.md").
- The `ds-data` service namespace provides a set of operations
  to Active Directory objects. For a list of available operations, see [Directory Service Data API Reference](../../../directoryservicedata/latest/DirectoryServiceDataAPIReference/Welcome.md "../../../directoryservicedata/latest/DirectoryServiceDataAPIReference/Welcome.md").

## Understanding resource

ownership

A _resource owner_ is the AWS account that created a
resource. That is, the resource owner is the AWS account of the
_principal entity_ (the root account, an IAM user, or an
IAM role) that authenticates the request that creates the resource. The following
examples illustrate how this works:

- If you use the root account credentials of your AWS account to create an
  AWS Directory Service resource, such as a directory, your AWS account is the owner of that
  resource.
- If you create an IAM user in your AWS account and grant permissions to
  create AWS Directory Service resources to that user, the user can also create AWS Directory Service
  resources. However, your AWS account, to which the user belongs, owns the
  resources.
- If you create an IAM role in your AWS account with permissions to
  create AWS Directory Service resources, anyone who can assume the role can create AWS Directory Service
  resources. Your AWS account, to which the role belongs, owns the AWS Directory Service
  resources.

## Managing access to

resources

A _permissions policy_ describes who has access to what. The
following section explains the available options for creating permissions
policies.

###### Note

This section discusses using IAM in the context of AWS Directory Service. It doesn't provide
detailed information about the IAM service. For complete IAM documentation,
see [What is IAM?](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") in the
_IAM User Guide_. For information about IAM policy
syntax and descriptions, see [IAM JSON policy reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the
_IAM User Guide_.

Policies attached to an IAM identity are referred to as
_identity-based_ policies (IAM polices) and policies
attached to a resource are referred to as _resource-based_
policies. AWS Directory Service supports only identity-based policies (IAM policies).

###### Topics

- [Identity-based
  policies (IAM policies)](#IAM_Auth_Access_ManagingAccess_IdentityBased "#IAM_Auth_Access_ManagingAccess_IdentityBased")
- [Resource-based
  policies](#IAM_Auth_Access_ManagingAccess_ResourceBased "#IAM_Auth_Access_ManagingAccess_ResourceBased")

### Identity-based

policies (IAM policies)

You can attach policies to IAM identities. For example, you can do the
following:

- **Attach a permissions policy to a user or a group
  in your account** – An account administrator can use
  a permissions policy that is associated with a particular user to grant
  permissions for that user to create an AWS Directory Service resource, such as a new
  directory.
- **Attach a permissions policy to a role (grant
  cross-account permissions)** – You can attach an
  identity-based permissions policy to an IAM role to grant
  cross-account permissions.

For more information about using IAM to delegate permissions, see
[Access management](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in
the _IAM User Guide_.

The following permissions policy grants permissions to a user to run all of
the actions that begin with `Describe`. These actions show
information about an AWS Directory Service resource, such as a directory or snapshot. Note that
the wildcard character (\*) in the `Resource` element indicates that
the actions are allowed for all AWS Directory Service resources owned by the account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":"ds:Describe*",
 "Resource":"*"
 }
 ]
}`

```

For more information about using identity-based policies with AWS Directory Service, see [Using identity-based policies (IAM
policies) for AWS Directory Service](IAM_Auth_Access_IdentityBased.md "IAM_Auth_Access_IdentityBased.md"). For more information about
users, groups, roles, and permissions, see [Identities (users, groups, and roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") in the
_IAM User Guide_.

### Resource-based

policies

Other services, such as Amazon S3, also support resource-based permissions
policies. For example, you can attach a policy to an S3 bucket to manage access
permissions to that bucket. AWS Directory Service doesn't support resource-based policies.

## Specifying policy elements: Actions,

effects, resources, and principals

For each AWS Directory Service resource, the service defines a set of API operations. For more
information, see [AWS Directory Service resources and operations](#CreatingIAMPolicies_DS "#CreatingIAMPolicies_DS"). For a list of available API
operations, see [Directory Service
Actions](../devguide/API_Operations.md "../devguide/API_Operations.md").

To grant permissions for these API operations, AWS Directory Service defines a set of actions that
you can specify in a policy. Note that performing an API operation can require
permissions for more than one action.

The following are the basic policy elements:

- **Resource** – In a policy, you use an
  Amazon Resource Name (ARN) to identify the resource to which the policy
  applies. For AWS Directory Service resources, you always use the wildcard character (\*) in
  IAM policies. For more information, see [AWS Directory Service resources and operations](#CreatingIAMPolicies_DS "#CreatingIAMPolicies_DS").
- **Action** – You use action keywords to
  identify resource operations that you want to allow or deny. For example,
  the `ds:DescribeDirectories` permission allows the user
  permissions to perform the AWS Directory Service `DescribeDirectories` operation.
- **Effect** – You specify the effect
  when the user requests the specific action. This can be either allow or
  deny. If you don't explicitly grant access to (allow) a resource, access is
  implicitly denied. You can also explicitly deny access to a resource, which
  you might do to make sure that a user cannot access it, even if a different
  policy grants access.
- **Principal** – In identity-based
  policies (IAM policies), the user that the policy is attached to is the
  implicit principal. For resource-based policies, you specify the user,
  account, service, or other entity that you want to receive permissions
  (applies to resource-based policies only). AWS Directory Service doesn't support
  resource-based policies.

To learn more about IAM policy syntax and descriptions, see [IAM JSON policy reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md")
in the _IAM User Guide_.

For a table showing all of the AWS Directory Service API actions and the resources that they apply
to, see [AWS Directory Service API permissions: Actions,
resources, and conditions reference](UsingWithDS_IAM_ResourcePermissions.md "UsingWithDS_IAM_ResourcePermissions.md").

## Specifying conditions in a

policy

When you grant permissions, you can use the access policy language to specify the
conditions when a policy should take effect. For example, you might want a policy to
be applied only after a specific date. For more information about specifying
conditions in a policy language, see [Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md")
in the _IAM User Guide_.

To express conditions, you use predefined condition keys. There are no condition
keys specific to AWS Directory Service. However, there are AWS condition keys that you can use as
appropriate. For a complete list of AWS keys, see [Available global condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#AvailableKeys") in the
_IAM User Guide_.
