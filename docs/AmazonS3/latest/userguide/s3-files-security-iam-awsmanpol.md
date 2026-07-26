# AWS managed policies for Amazon S3 Files

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

## AWS managed policy: AmazonS3FilesFullAccess

You can attach the `AmazonS3FilesFullAccess` policy to your IAM
identities. This policy grants full access to Amazon S3 Files, including permissions to
create and manage file systems, mount targets, and access points. For more information
about this policy, see
[AmazonS3FilesFullAccess](../../../aws-managed-policy/latest/reference/AmazonS3FilesFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonS3FilesFullAccess.md") in the AWS Managed Policy Reference.

## AWS managed policy: AmazonS3FilesReadOnlyAccess

You can attach the `AmazonS3FilesReadOnlyAccess` policy to your IAM
identities. This policy grants read-only access to Amazon S3 Files, including permissions
to view file systems, mount targets, access points, and related configurations. For more
information about this policy, see
[AmazonS3FilesReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonS3FilesReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonS3FilesReadOnlyAccess.md") in the AWS Managed Policy Reference.

## AWS managed policy: AmazonS3FilesClientFullAccess

You can attach the `AmazonS3FilesClientFullAccess` policy to your IAM
identities. This policy grants full client access to S3 Files file systems, including the
ability to mount, read, write, and access files as the root user. For more information
about this policy, see
[AmazonS3FilesClientFullAccess](../../../aws-managed-policy/latest/reference/AmazonS3FilesClientFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonS3FilesClientFullAccess.md") in the AWS Managed Policy Reference.

## AWS managed policy: AmazonS3FilesClientReadWriteAccess

You can attach the `AmazonS3FilesClientReadWriteAccess` policy to your IAM
identities. This policy grants read and write client access to S3 Files file systems,
including the ability to mount, read, and write. This policy does not grant root access.
For more information about this policy, see
[AmazonS3FilesClientReadWriteAccess](../../../aws-managed-policy/latest/reference/AmazonS3FilesClientReadWriteAccess.md "../../../aws-managed-policy/latest/reference/AmazonS3FilesClientReadWriteAccess.md") in the AWS Managed Policy Reference.

## AWS managed policy: AmazonS3FilesClientReadOnlyAccess

You can attach the `AmazonS3FilesClientReadOnlyAccess` policy to your IAM
identities. This policy grants read-only client access to S3 Files file systems,
including the ability to mount and read from the file system. For more information about
this policy, see
[AmazonS3FilesClientReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonS3FilesClientReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonS3FilesClientReadOnlyAccess.md") in the AWS Managed Policy Reference.

## AWS managed policy: AmazonS3FilesCSIDriverPolicy

You can attach the `AmazonS3FilesCSIDriverPolicy` policy to your IAM
identities. This policy grants permissions for the Amazon EFS Container Storage Interface
(CSI) driver to manage S3 Files access points on behalf of Amazon EKS clusters. For more
information about this policy, see
[AmazonS3FilesCSIDriverPolicy](../../../aws-managed-policy/latest/reference/AmazonS3FilesCSIDriverPolicy.md "../../../aws-managed-policy/latest/reference/AmazonS3FilesCSIDriverPolicy.md") in the AWS Managed Policy Reference.

## AWS managed policy: AmazonElasticFileSystemsUtils

You can attach the `AmazonElasticFileSystemsUtils` policy to your IAM
identities. This policy grants permissions for the S3 Files client utilities
(amazon-efs-utils) to perform operations such as describing mount targets, publishing
CloudWatch metrics and logs, and communicating with AWS Systems Manager. For more
information about this policy, see
[AmazonElasticFileSystemsUtils](../../../aws-managed-policy/latest/reference/AmazonElasticFileSystemsUtils.md "../../../aws-managed-policy/latest/reference/AmazonElasticFileSystemsUtils.md") in the AWS Managed Policy Reference.

## Amazon S3 Files updates to AWS managed policies

View details about updates to AWS managed policies for Amazon S3 Files since S3 Files began tracking these changes.

| Change                                       | Description                                                                                                                                       | Date          |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `AmazonElasticFileSystemsUtils` — Updated    | Added Amazon CloudWatch PutMetricData permissions to support<br>publishing client connectivity metrics.                                           | April 7, 2026 |
| `AmazonS3FilesCSIDriverPolicy` — Added       | New managed policy that grants permissions for the Amazon EFS CSI<br>driver to manage S3 Files access points on behalf of Amazon EKS<br>clusters. | April 7, 2026 |
| `AmazonS3FilesClientReadOnlyAccess` — Added  | New managed policy that grants read-only client access to S3 Files<br>file systems.                                                               | April 7, 2026 |
| `AmazonS3FilesClientReadWriteAccess` — Added | New managed policy that grants read and write client access to S3<br>Files file systems.                                                          | April 7, 2026 |
| `AmazonS3FilesClientFullAccess` — Added      | New managed policy that grants full client access to S3 Files file<br>systems, including root access.                                             | April 7, 2026 |
| `AmazonS3FilesReadOnlyAccess` — Added        | New managed policy that grants read-only access to S3 Files<br>resources.                                                                         | April 7, 2026 |
| `AmazonS3FilesFullAccess` — Added            | New managed policy that grants full access to S3 Files<br>resources.                                                                              | April 7, 2026 |
| S3 Files started tracking changes            | Amazon S3 Files started tracking changes for its AWS managed<br>policies.                                                                         | April 7, 2026 |
