**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Identity and Access Management for AWS Firewall Manager

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use Firewall Manager resources. IAM is an AWS service that you can
use with no additional charge.

###### Topics

- [Audience](#security_iam_audience "#security_iam_audience")
- [Authenticating with identities](#security_iam_authentication "#security_iam_authentication")
- [Managing access using policies](#security_iam_access-manage "#security_iam_access-manage")
- [How AWS Firewall Manager works with IAM](fms-security_iam_service-with-iam.md "fms-security_iam_service-with-iam.md")
- [Identity-based policy
  examples for AWS Firewall Manager](fms-security_iam_id-based-policy-examples.md "fms-security_iam_id-based-policy-examples.md")
- [AWS managed policies for AWS Firewall Manager](fms-security-iam-awsmanpol.md "fms-security-iam-awsmanpol.md")
- [Troubleshooting AWS Firewall Manager identity and
  access](fms-security_iam_troubleshoot.md "fms-security_iam_troubleshoot.md")
- [Using service-linked roles for Firewall Manager](fms-using-service-linked-roles.md "fms-using-service-linked-roles.md")
- [Cross-service confused deputy
  prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md")

## Audience

How you use AWS Identity and Access Management (IAM) differs, depending on the work that you do in Firewall Manager.

**Service user** – If you use the Firewall Manager service to do your job, then your administrator provides you
with the credentials and permissions that you need. As you use more Firewall Manager features to do your work, you might need additional permissions.
Understanding how access is managed can help you request the right permissions from your administrator. If you cannot access a feature in
Firewall Manager, see [Troubleshooting AWS Shield identity and
access](shd-security_iam_troubleshoot.md "shd-security_iam_troubleshoot.md").

**Service administrator** – If you're in charge of Firewall Manager resources at your company, you probably have
full access to Firewall Manager. It's your job to determine which Firewall Manager features and resources your service users should access. You must then
submit requests to your IAM administrator to change the permissions of your service users. Review the information on this page to understand the
basic concepts of IAM. To learn more about how your company can use IAM with Firewall Manager, see [How AWS Shield works with IAM](shd-security_iam_service-with-iam.md "shd-security_iam_service-with-iam.md").

**IAM administrator** – If you're an IAM administrator, you might want to learn details about how you can
write policies to manage access to Firewall Manager. To view example Firewall Manager identity-based policies that you can use in IAM, see [Identity-based policy examples for
AWS Shield](shd-security_iam_id-based-policy-examples.md "shd-security_iam_id-based-policy-examples.md").

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

Resource-based policies are JSON policy documents that you attach to a resource. Examples include IAM _role trust policies_ and Amazon S3 _bucket policies_. In services that support resource-based policies, service administrators can use them to control access to a specific resource. You must [specify a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in a resource-based policy.

Resource-based policies are inline policies that are located in that service. You can't use AWS managed policies from IAM in a resource-based policy.

### Access control lists (ACLs)

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

Amazon S3, AWS WAF, and Amazon VPC
are examples of services that support ACLs. To learn more about ACLs, see [Access control list (ACL)
overview](../../../AmazonS3/latest/userguide/acl-overview.md "../../../AmazonS3/latest/userguide/acl-overview.md") in the _Amazon Simple Storage Service Developer Guide_.

### Other policy types

AWS supports additional policy types that can set the maximum permissions granted by more common policy types:

- **Permissions boundaries** – Set the maximum permissions that an identity-based policy can grant to an IAM entity. For more information, see [Permissions boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the _IAM User Guide_.
- **Service control policies (SCPs)** – Specify the maximum permissions for an organization or organizational unit in AWS Organizations. For more information, see [Service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations User Guide_.
- **Resource control policies (RCPs)** – Set the maximum available permissions for resources in your accounts. For more information, see [Resource control policies (RCPs)](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") in the _AWS Organizations User Guide_.
- **Session policies** – Advanced policies passed as a parameter when creating a temporary session for a role or federated user. For more information, see [Session policies](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session") in the _IAM User Guide_.

### Multiple policy

types

When multiple types of policies apply to a request, the resulting permissions are more complicated to understand. To learn how AWS determines whether to allow a request when multiple policy types are involved, see [Policy evaluation logic](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md") in the _IAM User Guide_.
