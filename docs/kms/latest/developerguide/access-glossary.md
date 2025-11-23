# AWS KMS access control glossary

The following topic describes important terms and concepts in AWS KMS access control.

## Authentication

_Authentication_ is the process of verifying your
identity. To send a request to AWS KMS, you must sign into AWS using your AWS
credentials.

## Authorization

_Authorization_ provides the permission to send
requests to create, manage, or use AWS KMS resources. For example, you must be authorized
to use a KMS key in a cryptographic operation.

To control access to your AWS KMS resources, use [key
policies](key-policies.md "key-policies.md"), [IAM policies](iam-policies.md "iam-policies.md"), and [grants](grants.md "grants.md"). Every KMS key must have a key policy. If the key
policy allows it, you can also use IAM policies and grants to give principals access
to the KMS key. To refine your authorization, you can use [condition keys](policy-conditions.md "policy-conditions.md") that allow or deny access only
when a request or resource meets the conditions you specify. You can also allow access
to principals you trust in [other
AWS accounts](key-policy-modifying-external-accounts.md "key-policy-modifying-external-accounts.md").

## Authenticating with identities

Authentication is how you sign in to AWS using your identity credentials. You must be authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.

You can sign in as a federated identity using credentials from an identity source like AWS IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook credentials. For more information about signing in, see [How to sign in to your AWS account](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User Guide_.

For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For more information, see [AWS Signature Version 4 for API requests](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") in the _IAM User Guide_.

### AWS account root user

When you create an AWS account, you begin with one sign-in identity called the AWS account _root user_ that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.

### Federated identity

As a best practice, require human users to use federation with an identity provider to access AWS services using temporary credentials.

A _federated identity_ is a user from your enterprise directory, web identity provider, or Directory Service that accesses AWS services using credentials from an identity source. Federated identities assume roles that provide temporary credentials.

For centralized access management, we recommend AWS IAM Identity Center. For more information, see [What is IAM Identity Center?](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") in the _AWS IAM Identity Center User Guide_.

### IAM users and groups

An _[IAM user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md")_ is an identity with specific permissions for a single person or application. We recommend using temporary credentials instead of IAM users with long-term credentials. For more information, see [Require human users to use federation with an identity provider to access AWS using temporary credentials](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_.

An [_IAM group_](../../../IAM/latest/UserGuide/id_groups.md "../../../IAM/latest/UserGuide/id_groups.md") specifies a collection of IAM users and makes permissions easier to manage for large sets of users. For more information, see [Use cases for IAM users](../../../IAM/latest/UserGuide/gs-identities-iam-users.md "../../../IAM/latest/UserGuide/gs-identities-iam-users.md") in the _IAM User Guide_.

### IAM roles

An _[IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")_ is an identity with specific permissions that provides temporary credentials. You can assume a role by [switching from a user to an IAM role (console)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md") or by calling an AWS CLI or AWS API operation. For more information, see [Methods to assume a role](../../../IAM/latest/UserGuide/id_roles_manage-assume.md "../../../IAM/latest/UserGuide/id_roles_manage-assume.md") in the _IAM User Guide_.

IAM roles are useful for federated user access, temporary IAM user permissions, cross-account access, cross-service access, and applications running on Amazon EC2. For more information, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the _IAM User Guide_.

## Managing access using policies

You control access in AWS by creating policies and attaching them to AWS identities or resources. A policy defines permissions when associated with an identity or resource. AWS evaluates these policies when a principal makes a request. Most policies are stored in AWS as JSON documents. For more information about JSON policy documents, see [Overview of JSON policies](../../../IAM/latest/UserGuide/access_policies.md#access_policies-json "../../../IAM/latest/UserGuide/access_policies.md#access_policies-json") in the _IAM User Guide_.

Using policies, administrators specify who has access to what by defining which **principal** can perform **actions** on what **resources**, and under what **conditions**.

By default, users and roles have no permissions. An IAM administrator creates IAM policies and adds them to roles, which users can then assume. IAM policies define permissions regardless of the method used to perform the operation.

### Identity-based

policies

Identity-based policies are JSON permissions policy documents that you attach to an identity (user, group, or role). These policies control what actions identities can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

Identity-based policies can be _inline policies_ (embedded directly into a single identity) or _managed policies_ (standalone policies attached to multiple identities). To learn how to choose between managed and inline policies, see [Choose between managed policies and inline policies](../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md "../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md") in the _IAM User Guide_.

### Resource-based

policies

An AWS KMS [key policy](key-policies.md "key-policies.md") is a resource-based policy
that controls access to a KMS key. Every KMS key must have a key policy. You can
use other authorization mechanism to allow access to the KMS key, but only if the
key policy allows it. (You can use an IAM policy to _deny_ access to a KMS key even if the key policy doesn't explicitly
permit it.)

Resource-based policies are JSON policy documents that you attach to a resource,
such as a KMS key, to control access to the specific resource. The resource-based
policy defines the actions that a specified principal can perform on that resource
and under what conditions. You don't specify the resource in a resource-based
policy, but you must specify a principal, such as accounts, users, roles, federated
users, or AWS services. Resource-based policies are inline policies that are
located in that service that manages the resource. You can't use AWS managed
policies from IAM, such as the [AWSKeyManagementServicePowerUser managed policy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSKeyManagementServicePowerUser "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSKeyManagementServicePowerUser"), in a
resource-based policy.

### Other policy

types

AWS supports additional policy types that can set the maximum permissions granted by more common policy types:

- **Permissions boundaries** – Set the maximum permissions that an identity-based policy can grant to an IAM entity. For more information, see [Permissions boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the _IAM User Guide_.
- **Service control policies (SCPs)** – Specify the maximum permissions for an organization or organizational unit in AWS Organizations. For more information, see [Service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations User Guide_.
- **Resource control policies (RCPs)** – Set the maximum available permissions for resources in your accounts. For more information, see [Resource control policies (RCPs)](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") in the _AWS Organizations User Guide_.
- **Session policies** – Advanced policies passed as a parameter when creating a temporary session for a role or federated user. For more information, see [Session policies](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session") in the _IAM User Guide_.

### Multiple policy

types

When multiple types of policies apply to a request, the resulting permissions are more complicated to understand. To learn how AWS determines whether to allow a request when multiple policy types are involved, see [Policy evaluation logic](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md") in the _IAM User Guide_.

## AWS KMS resources

In AWS KMS, the primary resource is an AWS KMS key. AWS KMS also supports an [alias](kms-alias.md "kms-alias.md"), an independent resource that provides a friendly
name for a KMS key. Some AWS KMS operations allow you to use an alias to identify a
KMS key.

Each instance of a KMS key or alias has a unique [Amazon Resource
Name](../../../general/latest/gr/aws-arns-and-namespaces.md#arns-syntax "../../../general/latest/gr/aws-arns-and-namespaces.md#arns-syntax") (ARN) with a standard format. In AWS KMS resources, the AWS service
name is `kms`.

- **AWS KMS key**

ARN format:

`arn:`AWS partition name`:`AWS
service
name`:`AWS Region`:`AWS account
ID`:key/`key ID``

Example ARN:

`arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

- **Alias**

ARN format:

`arn:`AWS partition name`:`AWS
service
name`:`AWS Region`:`AWS account
ID`:alias/`alias
name``

Example ARN:

`arn:aws:kms:us-west-2:111122223333:alias/example-alias`

AWS KMS provides a set of API operations to work with your AWS KMS resources. For more
information about identifying KMS keys in the AWS Management Console and AWS KMS API operations, see
[Key identifiers (KeyId)](concepts.md#key-id "concepts.md#key-id"). For a list of AWS KMS operations, see
the [AWS Key Management Service API Reference](../APIReference.md "../APIReference.md").
