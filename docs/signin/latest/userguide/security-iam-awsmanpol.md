# AWS managed policies for AWS Sign-In

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed

policy: AmazonManagedSignUpServicePolicy

The `AmazonManagedSignUpServicePolicy` policy grants permissions required
to complete AWS account sign-up processes.

You can attach `AmazonManagedSignUpServicePolicy` to your users, groups,
and roles.

**Permissions details**

This policy includes the following permissions:

- **Customer verification** - Allows creating,
  retrieving, and updating customer verification details and eligibility status,
  including creating upload URLs for verification documents.

To view more details about the policy, including the latest version of the JSON policy
document, see [AmazonManagedSignUpServicePolicy](../../../aws-managed-policy/latest/reference/AmazonManagedSignUpServicePolicy.md "../../../aws-managed-policy/latest/reference/AmazonManagedSignUpServicePolicy.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed

policy: ApplicationProvisioningPolicy

The ApplicationProvisioningPolicy policy grants comprehensive permissions for
application provisioning and identity management operations, including IAM role and
policy management, SSO configuration, and identity store operations.

You can attach `ApplicationProvisioningPolicy` to your users, groups, and
roles.

**Permissions details**

This policy includes the following permissions:

- **IAM management** - Allows comprehensive IAM
  operations including creating, updating, and deleting roles and policies,
  managing role attachments, and creating service-linked roles.
- **Research and Engineering Studio on AWS** - Allows all operations on
  Research and Engineering Studio on AWS resources.
- **Role passing** - Allows passing IAM roles to
  other services.
- **IAM Identity Center** - Allows managing IAM Identity Center instances,
  applications, assignments, grants, and authentication methods.
- **Identity Store** - Allows reading user and group
  information from the Identity Store.
- **IAM Identity Center OAuth** - Allows authenticating IAM
  sessions through IAM Identity Center OAuth.
- **User Profile and Directory** - Allows managing
  IAM Identity Center connectors, user profiles, and directory configurations including external
  identity provider setup.
- **User Subscriptions** - Allows listing user
  subscriptions.

To view more details about the policy, including the latest version of the JSON policy
document, see [ApplicationProvisioningPolicy](../../../aws-managed-policy/latest/reference/ApplicationProvisioningPolicy.md "../../../aws-managed-policy/latest/reference/ApplicationProvisioningPolicy.md") in the _AWS Managed Policy
Reference Guide_.

## AWS Sign-In updates to AWS managed

policies

View details about updates to AWS managed policies for AWS Sign-In since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the AWS Sign-In Document history page.

| Change                                                                                                                                                               | Description                                                                                                                                                                                                                                       | Date               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [ApplicationProvisioningPolicy](#security-iam-awsmanpol-ApplicationProvisioningPolicy "#security-iam-awsmanpol-ApplicationProvisioningPolicy") – New policy          | Added a new AWS managed policy that grants comprehensive permissions for application provisioning and identity management operations, including IAM role and policy management, IAM Identity Center configuration, and Identity Store operations. | September 30, 2025 |
| [AmazonManagedSignUpServicePolicy](#security-iam-awsmanpol-AmazonManagedSignUpServicePolicy "#security-iam-awsmanpol-AmazonManagedSignUpServicePolicy") – New policy | Added a new AWS managed policy that grants permissions required for AWS account sign-up processes, including customer verification and payment setup operations.                                                                                  | September 30, 2025 |
| AWS Sign-In started tracking changes                                                                                                                                 | AWS Sign-In started tracking changes for its AWS managed policies.                                                                                                                                                                                | September 30, 2025 |
