# Using AWS managed policies for AWS Artifact

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

## AWS managed policy: [AWSArtifactReportsReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSArtifactReportsReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSArtifactReportsReadOnlyAccess.md")

You can attach the
`AWSArtifactReportsReadOnlyAccess` policy to your IAM identities.

This policy grants
`read-only`
permissions that allow listing, viewing, and downloading reports.

**Permissions details**

This policy includes the following permissions.

- `artifact` – Allows principals to list, view, and download reports from AWS Artifact.

## AWS managed policy: [AWSArtifactAgreementsReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSArtifactAgreementsReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSArtifactAgreementsReadOnlyAccess.md")

You can attach the
`AWSArtifactAgreementsReadOnlyAccess` policy to your IAM identities.

This policy grants
`read-only` access to list the AWS Artifact service agreements and to download the accepted agreements. It also includes permissions to list as well as describe the organization details. Additionally, the policy provides the ability to check if the required service-linked role exists.

**Permissions details**

This policy includes the following permissions.

- `artifact` – Allows principals to list all the agreements and to view accepted agreements from AWS Artifact.
- `iam` – Allows principals to check if the required service linked role exists.
- `organizations` – Allows principals to describe the current organization and to list service access for that organization.

## AWS managed policy: [AWSArtifactAgreementsFullAccess](../../../aws-managed-policy/latest/reference/AWSArtifactAgreementsFullAccess.md "../../../aws-managed-policy/latest/reference/AWSArtifactAgreementsFullAccess.md")

You can attach the
`AWSArtifactAgreementsFullAccess` policy to your IAM identities.

This policy grants
`full` permissions to list, download, accept, and terminate AWS Artifact agreements. It also includes permissions to list and enable AWS service access in the AWS Organizations service, as well as describe the organization details. Additionally, the policy provides the ability to check if the required service-linked role exists and creates one if it doesn't.

**Permissions details**

This policy includes the following permissions.

- `artifact` – Allows principals to list, download, accept, and terminate the agreements from AWS Artifact.
- `iam` – Allows principals to check if the required service linked role exists, and create one if it doesn't.
- `organizations` – Allows principals to describe the current organization and to list/enable service access for that organization.

## AWS Artifact updates to AWS managed

policies

View details about updates to AWS managed policies for AWS Artifact since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the AWS Artifact [Document history](doc-history.md "doc-history.md") page.

| Change                                     | Description                                                                                                                                                                                                           | Date       |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| Updated AWS Agreements managed policies    | Updated AWSArtifactAgreementsFullAccess managed policy to scope `organizations:EnableAWSServiceAccess` permissions down to AWS Artifact's service principal. This does not impact the managed policy's functionality. | 2025-10-16 |
| Updated AWS Reports managed policies       | Updated AWSArtifactReportsReadOnlyAccess managed policy to remove the artifact:get permission.                                                                                                                        | 2025-03-21 |
| Introduced AWS Agreements managed policies | Introduced AWSArtifactAgreementsReadOnlyAccess and AWSArtifactAgreementsFullAccess managed policies.                                                                                                                  | 2024-11-21 |
| AWS Artifact started tracking changes      | AWS Artifact started tracking changes for its AWS managed policies and introduced AWSArtifactReportsReadOnlyAccess.                                                                                                   | 2023-12-15 |
