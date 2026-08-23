AWS FinOps Agent is in preview release and is subject to change.

# Identity and access management for AWS FinOps Agent

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use AWS FinOps Agent resources. IAM is an AWS service that you can
use with no additional charge.

###### Topics

- [Audience](#security_iam_audience "#security_iam_audience")
- [Authenticating with identities](#security_iam_authentication "#security_iam_authentication")
- [Managing access using policies](#security_iam_access-manage "#security_iam_access-manage")
- [How AWS FinOps Agent works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md")
- [Identity-based policy examples for AWS FinOps Agent](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md")
- [Troubleshooting AWS FinOps Agent identity and access](security_iam_troubleshoot.md "security_iam_troubleshoot.md")

## Audience

How you use AWS Identity and Access Management (IAM) differs based on your role:

- **Service user** - request permissions from your
  administrator if you cannot access features (see [Troubleshooting AWS FinOps Agent identity and access](security_iam_troubleshoot.md "security_iam_troubleshoot.md"))
- **Service administrator** - determine user access and
  submit permission requests (see [How AWS FinOps Agent works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md"))
- **IAM administrator** - write policies to manage
  access (see [Identity-based policy examples for AWS FinOps Agent](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md"))

## Authenticating with identities

To use AWS FinOps Agent, sign in to AWS as an IAM user or assume an IAM role that has the required permissions.

### AWS account root user

When you create an AWS account, you begin with one sign-in identity called the AWS account _root user_ that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.

### Federated identity

AWS FinOps Agent does not support federated identities.

### IAM users and groups

An _IAM user_ is an identity with specific permissions for a single person or application. An _IAM group_ specifies a collection of IAM users and makes permissions easier to manage for large sets of users.

### IAM roles

An _IAM role_ is an identity with specific permissions that provides temporary credentials. To use a role with AWS FinOps Agent, configure the role with the permissions required for the workflows it performs. For more information, see [Methods to assume a role](../../../IAM/latest/UserGuide/id_roles_manage-assume.md "../../../IAM/latest/UserGuide/id_roles_manage-assume.md") in the _IAM User Guide_.

## Managing access using policies

You control access in AWS by creating policies and attaching them to AWS identities or resources. A policy defines permissions when associated with an identity or resource. AWS evaluates these policies when a principal makes a request. Most policies are stored in AWS as JSON documents. For more information about JSON policy documents, see [Overview of JSON policies](../../../IAM/latest/UserGuide/access_policies.md#access_policies-json "../../../IAM/latest/UserGuide/access_policies.md#access_policies-json") in the _IAM User Guide_.

Using policies, administrators specify who has access to what by defining which **principal** can perform **actions** on what **resources**, and under what **conditions**.

By default, users and roles have no permissions. An IAM administrator creates IAM policies and adds them to roles, which users can then assume. IAM policies define permissions regardless of the method used to perform the operation.

### Identity-based policies

Identity-based policies are JSON permissions policy documents that you attach to an identity (user, group, or role). These policies control what actions identities can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

Identity-based policies can be _inline policies_ (embedded directly into a single identity) or _managed policies_ (standalone policies attached to multiple identities). To learn how to choose between managed and inline policies, see [Choose between managed policies and inline policies](../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md "../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md") in the _IAM User Guide_.

### Resource-based policies

AWS FinOps Agent does not support resource-based policies. You cannot use a resource-based policy to grant another AWS account access to an agent or its data. AWS FinOps Agent uses the roles and policies described in the [IAM setup guide](setting-up.md "setting-up.md"). Adding a policy to the agent role does not add supported access to additional AWS services or resources.

To analyze organization-wide cost data, deploy AWS FinOps Agent in your organization's management account (the payer account). Cost Explorer in that account provides organization-wide visibility, subject to the IAM permissions you configure.

### Other policy types

AWS supports additional policy types that can set the maximum permissions granted by more common policy types:

- **Permissions boundaries** – Set the maximum permissions that an identity-based policy can grant to an IAM entity. For more information, see [Permissions boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the _IAM User Guide_.
- **Service control policies (SCPs)** – Specify the maximum permissions for an organization or organizational unit in AWS Organizations. For more information, see [Service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations User Guide_.
- **Resource control policies (RCPs)** – Set the maximum available permissions for resources in your accounts. For more information, see [Resource control policies (RCPs)](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") in the _AWS Organizations User Guide_.
- **Session policies** – Advanced policies passed as a parameter when creating a temporary session for a role or federated user. For more information, see [Session policies](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session") in the _IAM User Guide_.

### Multiple policy types

When multiple types of policies apply to a request, the resulting permissions are more complicated to understand. To learn how AWS determines whether to allow a request when multiple policy types are involved, see [Policy evaluation logic](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md") in the _IAM User Guide_.
