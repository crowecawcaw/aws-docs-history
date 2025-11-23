# Authentication and access control for

AWS CodeCommit

Access to AWS CodeCommit requires credentials. Those credentials must have permissions
to access AWS resources, such as CodeCommit repositories, and your IAM user, which you use to
manage your Git credentials or the SSH public key that you use for making Git connections.
The following sections provide details on how you can use [AWS Identity and Access Management (IAM)](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") and CodeCommit to
help secure access to your resources:

- [Authentication](#authentication "#authentication")
- [Access control](#access-control "#access-control")

## Authentication

Because CodeCommit repositories are Git-based and support the basic functionality of Git,
including Git credentials, we recommend that you use an IAM user when working with
CodeCommit. You can access CodeCommit with other identity types, but the other identity types are
subject to limitations, as described below.

Identity types:

- **IAM user** – An [IAM user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md") is an identity within
  your Amazon Web Services account that has specific custom permissions. For example, an
  IAM user can have permissions to create and manage Git credentials for
  accessing CodeCommit repositories. **This is the
  recommended user type for working with CodeCommit.** You can use an
  IAM user name and password to sign in to secure AWS webpages like the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/"), [AWS Discussion Forums](https://forums.aws.amazon.com/ "https://forums.aws.amazon.com/"), or the
  [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

You can generate Git credentials or associate SSH public keys with your IAM
user, or you can install and configure **git-remote-codecommit**.
These are the easiest ways to set up Git to work with your CodeCommit repositories.
With [Git credentials](setting-up-gc.md "setting-up-gc.md"), you generate a static
user name and password in IAM. You then use these credentials for HTTPS
connections with Git and any third-party tool that supports Git user name and
password authentication. With SSH connections, you create public and private key
files on your local machine that Git and CodeCommit use for SSH authentication. You
associate the public key with your IAM user, and you store the private key on
your local machine. **[git-remote-codecommit](setting-up-git-remote-codecommit.md "setting-up-git-remote-codecommit.md")** extends Git itself, and does not
require setting up Git credentials for the user.

In addition, you can generate [access keys](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") for
each user. Use access keys when you access AWS services programmatically,
either through [one of the AWS SDKs](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/")
or by using the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"). The
SDK and CLI tools use the access keys to cryptographically sign your requests.
If you don’t use the AWS tools, you must sign the requests yourself.
CodeCommit supports _Signature Version 4_, a
protocol for authenticating inbound API requests. For more information about
authenticating requests, see [Signature Version 4 Signing Process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") in the
_AWS General Reference_.

- **Amazon Web Services account root user** – When you
  sign up for AWS, you provide an email address and password that is associated
  with your Amazon Web Services account. These are your _root
  credentials_, and they provide complete access to all of your
  AWS resources. Some CodeCommit features are not available for root account users.
  In addition, the only way to use Git with your root account is to either install
  and configure **git-remote-codecommit** (recommended) or to
  configure the AWS credential helper, which is included with the AWS CLI. You
  cannot use Git credentials or SSH public-private key pairs with your root
  account user. For these reasons, we do not recommend using your root account
  user when interacting with CodeCommit.

###### Important

For security reasons, we recommend that you use the root credentials only
to create an _administrator user_, which is an
_IAM user_ with full permissions to your AWS
account. Then, you can use this administrator user to create other IAM
users and roles with limited permissions. For more information, see [IAM Best
Practices](../../../IAM/latest/UserGuide/best-practices.md#create-iam-users "../../../IAM/latest/UserGuide/best-practices.md#create-iam-users") and [Creating an
Admin User and Group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in the
_IAM User Guide_.

- **IAM Identity Center and users in IAM Identity Center** – AWS IAM Identity Center
  expands the capabilities of AWS Identity and Access Management to provide a central place that brings
  together administration of users and their access to AWS accounts and cloud
  applications. While recommended as a best practice for most users working with
  AWS, IAM Identity Center does not currently provide mechanisms for Git credentials or SSH
  key pairs. These users can install and configure
  **git-remote-codecommit** to locally clone CodeCommit
  repositories, but not all integrated development environments (IDEs) support
  cloning, pushing, or pulling with
  **git-remote-codecommit**.

As a best practice, require human users to use federation with an identity provider to access AWS services using temporary credentials.

A _federated identity_ is a user from your enterprise directory, web identity provider, or Directory Service that accesses AWS services using credentials from an identity source. Federated identities assume roles that provide temporary credentials.

For centralized access management, we recommend AWS IAM Identity Center. For more information, see [What is IAM Identity Center?](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") in the _AWS IAM Identity Center User Guide_.

- **IAM role** – Like an IAM user, an
  [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an IAM
  identity that you can create in your account to grant specific permissions.

An _[IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")_ is an identity with specific permissions that provides temporary credentials. You can assume a role by [switching from a user to an IAM role (console)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md") or by calling an AWS CLI or AWS API operation. For more information, see [Methods to assume a role](../../../IAM/latest/UserGuide/id_roles_manage-assume.md "../../../IAM/latest/UserGuide/id_roles_manage-assume.md") in the _IAM User Guide_.

IAM roles are useful for federated user access, temporary IAM user permissions, cross-account access, cross-service access, and applications running on Amazon EC2. For more information, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the _IAM User Guide_.

###### Note

You cannot use Git credentials or SSH public-private key pairs with
federated users. In addition, user preferences are not available for
federated users. For information about how to set up connections using
federated access, see [Setup steps for HTTPS connections to AWS CodeCommit with
git-remote-codecommit](setting-up-git-remote-codecommit.md "setting-up-git-remote-codecommit.md").

## Access control

You can have valid credentials to authenticate your requests, but unless you have
permissions you cannot create or access CodeCommit resources. For example, you must
have permissions to view repositories, push code, create and manage Git credentials, and
so on.

The following sections describe how to manage permissions for CodeCommit. We
recommend that you read the overview first.

- [Overview of
  managing access permissions to your CodeCommit resources](#auth-and-access-control-iam-access-control-identity-based "#auth-and-access-control-iam-access-control-identity-based")
- [Using
  identity-based policies (IAM Policies) for CodeCommit](auth-and-access-control-iam-identity-based-access-control.md "auth-and-access-control-iam-identity-based-access-control.md")
- [CodeCommit
  permissions reference](auth-and-access-control-permissions-reference.md "auth-and-access-control-permissions-reference.md")

## Overview of

managing access permissions to your CodeCommit resources

Every AWS resource is owned by an Amazon Web Services account. Permissions to create or access a
resource are governed by permissions policies. An account administrator can attach
permissions policies to IAM identities (that is, users, groups, and roles). Some
services, such as AWS Lambda, also support attaching permissions policies to resources.

###### Note

An _account administrator_ (or administrator user) is a user
with administrator privileges. For more information, see [IAM Best Practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the
_IAM User Guide_.

When granting permissions, you decide who gets the permissions, the resources they get
permissions for, and the specific actions that you want to allow on those
resources.

###### Topics

- [CodeCommit resources and operations](#arn-formats "#arn-formats")
- [Understanding resource
  ownership](#understanding-resource-ownership "#understanding-resource-ownership")
- [Managing access to resources](#managing-access-resources "#managing-access-resources")
- [Resource scoping in CodeCommit](#resource-scoping "#resource-scoping")
- [Specifying policy elements: resources,
  actions, effects, and principals](#actions-effects-principals "#actions-effects-principals")
- [Specifying conditions in a policy](#policy-conditions "#policy-conditions")

### CodeCommit resources and operations

In CodeCommit, the primary resource is a repository. Each
resource has a unique Amazon Resource Names (ARN) associated with it. In a policy,
you use an Amazon Resource Name (ARN) to identify the resource that the policy
applies to. For more information about ARNs, see [Amazon Resource Names (ARN) and
AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") in the _Amazon Web Services General Reference_.
CodeCommit does not currently support other resource types, which are referred to
as subresources.

The following table describes how to specify CodeCommit resources.

| Resource Type                                                                             | ARN Format                                                 |
| ----------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Repository                                                                                | arn:aws:codecommit:`region`:`account-id`:`repository-name` |
| All CodeCommit repositories                                                               | arn:aws:codecommit:\*                                      |
| All CodeCommit repositories owned by the specified account<br>in the specified AWS Region | arn:aws:codecommit:`region`:`account-id`:\*                |

###### Note

Most AWS services treat a colon (:) or a forward slash (/) in ARNs as the
same character. However, CodeCommit requires an exact match in resource
patterns and rules. When creating event patterns, be sure to use the correct ARN
characters so that they match the ARN syntax in the resource.

For example, you can indicate a specific repository
(`MyDemoRepo`) in your statement using its ARN as
follows:

```
"Resource": "arn:aws:codecommit:`us-west-2`:`111111111111`:`MyDemoRepo`"
```

To specify all repositories that belong to a specific account, use the
wildcard character (\*) as follows:

```
"Resource": "arn:aws:codecommit:`us-west-2`:`111111111111`:`*`"
```

To specify all resources, or if a specific API action does not support ARNs, use
the wildcard character (\*) in the `Resource` element as follows:

```
"Resource": "`*`"
```

You can also use the wildcard character(\*) to specify all resources that match
part of a repository name. For example, the following ARN specifies any CodeCommit
repository that begins with the name `MyDemo` and that is registered to
the Amazon Web Services account `111111111111` in the `us-east-2`
AWS Region:

```
arn:aws:codecommit:us-east-2:111111111111:MyDemo*
```

For a list of available operations that work with the CodeCommit resources,
see [CodeCommit
permissions reference](auth-and-access-control-permissions-reference.md "auth-and-access-control-permissions-reference.md").

### Understanding resource

ownership

The Amazon Web Services account owns the resources that are created in the account, regardless
of who created them. Specifically, the resource owner is the Amazon Web Services account of the
[principal
entity](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md") (that is, the root account, an IAM user, or an IAM role) that
authenticates the resource creation request. The following examples illustrate how
this works:

- If you create an IAM user in your Amazon Web Services account and grant permissions to
  create CodeCommit resources to that user, the user can create
  CodeCommit resources. However, your Amazon Web Services account, to which the user
  belongs, owns the CodeCommit resources.
- If you use the root account credentials of your Amazon Web Services account to create a
  rule, your Amazon Web Services account is the owner of the CodeCommit resource.
- If you create an IAM role in your Amazon Web Services account with permissions to
  create CodeCommit resources, anyone who can assume the role can create
  CodeCommit resources. Your Amazon Web Services account, to which the role belongs, owns
  the CodeCommit resources.

### Managing access to resources

To manage access to AWS resources, you use permissions policies. A
_permissions policy_ describes who has access to what. The
following section explains the options for creating permissions policies.

###### Note

This section discusses using IAM in the context of CodeCommit. It
doesn't provide detailed information about the IAM service. For more
information about IAM, see [What
Is IAM?](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") in the _IAM User Guide_. For
information about IAM policy syntax and descriptions, see [IAM Policy Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md")
in the _IAM User Guide_.

Permissions policies that are attached to an IAM identity are referred to as
identity-based policies (IAM policies). Permissions policies that are attached to
a resource are referred to as resource-based policies. Currently, CodeCommit
supports only identity-based policies (IAM policies).

###### Topics

- [Identity-based policies (IAM
  policies)](#identity-based-policies "#identity-based-policies")
- [Resource-based
  policies](#resource-based-policies-overview "#resource-based-policies-overview")

#### Identity-based policies (IAM

policies)

To manage access to AWS resources, you attach permissions policies to IAM
identities. In CodeCommit, you use identity-based policies to control access
to repositories. For example, you can do the following:

- **Attach a permissions policy to a user or a group
  in your account** – To grant a user permissions to
  view CodeCommit resources in the CodeCommit console, attach an
  identity-based permissions policy to a user or group that the user
  belongs to.
- **Attach a permissions policy to a role (to grant
  cross-account permissions)** – Delegation, such as
  when you want to grant cross-account access, involves setting up a trust
  between the account that owns the resource (the trusting account), and
  the account that contains the users who need to access the resource (the
  trusted account). A permissions policy grants the user of a role the
  needed permissions to carry out the intended tasks on the resource. A
  trust policy specifies which trusted accounts are allowed to grant its
  users permissions to assume the role. For more information, see [IAM Terms and
  Concepts](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md").

To grant cross-account permissions, attach an identity-based
permissions policy to an IAM role. For example, the administrator in
Account A can create a role to grant cross-account permissions to
another Amazon Web Services account (for example, Account B) or an AWS service as
follows:

    1. Account A administrator creates an IAM role and attaches a
     permissions policy to the role that grants permissions on
     resources in Account A.
    2. Account A administrator attaches a trust policy to the role
     identifying Account B as the principal who can assume the
     role.
    3. Account B administrator can then delegate permissions to
     assume the role to any users in Account B. Doing this allows
     users in Account B to create or access resources in Account A.
     If you want to grant an AWS service permission to assume the
     role, the principal in the trust policy can also be an AWS
     service principal. For more information, see Delegation in
     [IAM Terms and Concepts](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md").

For more information about using IAM to delegate permissions, see
[Access Management](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in
the _IAM User Guide_.

The following example policy allows a user to create a branch in a repository
named `MyDemoRepo`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [
 {
 "Effect" : "Allow",
 "Action" : [
 "codecommit:CreateBranch"
 ],
 "Resource" : "arn:aws:codecommit:us-east-2:`111122223333`:`MyDemoRepo`"
 }
 ]
}`

```

To restrict the calls and resources that users in your account have access to,
create specific IAM policies, and then attach those policies to IAM users.
For more information about how to create IAM roles and to explore example
IAM policy statements for CodeCommit, see [Customer managed identity
policy examples](customer-managed-policies.md#customer-managed-policies-identity "customer-managed-policies.md#customer-managed-policies-identity").

#### Resource-based

policies

Some services, such as Amazon S3, also support resource-based permissions policies.
For example, you can attach a resource-based policy to an S3 bucket to manage
access permissions to that bucket. CodeCommit doesn't support resource-based
policies, but you can use tags to identify resources, which you can then use in
IAM policies. For an example of a tag-based policy, see
[Identity-based policies (IAM
policies)](#identity-based-policies "#identity-based-policies").

### Resource scoping in CodeCommit

In CodeCommit, you can scope identity-based policies and permissions to resources, as
described in [CodeCommit resources and operations](#arn-formats "#arn-formats"). However, you
cannot scope the `ListRepositories` permission to a resource. Instead,
you must scope it to all resources (using the wildcard `*`). Otherwise,
the action fails.

All other CodeCommit permissions can be scoped to resources.

### Specifying policy elements: resources,

actions, effects, and principals

You can create policies to allow or deny users access to resources, or allow or
deny users to take specific actions on those resources. CodeCommit defines a set
of public API operations that define how users work with the service, whether that
is through the CodeCommit console, the SDKs, the AWS CLI, or by directly calling those
APIs. To grant permissions for these API operations, CodeCommit defines a set of
actions that you can specify in a policy.

Some API operations can require permissions for more than one action. For more
information about resources and API operations, see [CodeCommit resources and operations](#arn-formats "#arn-formats") and [CodeCommit
permissions reference](auth-and-access-control-permissions-reference.md "auth-and-access-control-permissions-reference.md").

The following are the basic elements of a policy:

- **Resource** – To identify the resource
  that the policy applies to, you use an Amazon Resource Name (ARN). For more
  information, see [CodeCommit resources and operations](#arn-formats "#arn-formats").
- **Action** – To identify resource
  operations that you want to allow or deny, you use action keywords. For
  example, depending on the specified `Effect`, the
  `codecommit:GetBranch` permission either allows or denies the
  user to perform the `GetBranch` operation, which gets details
  about a branch in a CodeCommit repository.
- **Effect** – You specify the effect,
  either allow or deny, that takes place when the user requests the specific
  action. If you don't explicitly grant access to (allow) a resource, access
  is implicitly denied. You can also explicitly deny access to a resource to
  make sure that a user cannot access it, even if a different policy grants
  access.
- **Principal** – In identity-based
  policies (IAM policies), the only type of policies that CodeCommit supports,
  the user that the policy is attached to is the implicit principal.

To learn more about IAM policy syntax, see [IAM Policy Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md")
in the _IAM User Guide_.

For a table showing all of the CodeCommit API actions and the resources that
they apply to, see [CodeCommit
permissions reference](auth-and-access-control-permissions-reference.md "auth-and-access-control-permissions-reference.md").

### Specifying conditions in a policy

When you grant permissions, you use the access policy language for IAM to
specify the conditions under which a policy should take effect. For example, you
might want a policy to be applied only after a specific date. For more information
about specifying conditions in a policy language, see [Condition](../../../IAM/latest/UserGuide/reference_policies_elements.md#Condition "../../../IAM/latest/UserGuide/reference_policies_elements.md#Condition")
and [Policy
Grammar](../../../IAM/latest/UserGuide/reference_policies_grammar.md "../../../IAM/latest/UserGuide/reference_policies_grammar.md") in the _IAM User Guide_.

To express conditions, you use predefined condition keys. There are no condition
keys specific to CodeCommit. However, there are AWS-wide condition keys that
you can use as appropriate. For a complete list of AWS-wide keys, see [Available
Keys for Conditions](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the _IAM User Guide_.
