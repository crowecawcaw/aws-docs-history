# Security Hub controls for Amazon EFS

These Security Hub controls evaluate the Amazon Elastic File System (Amazon EFS) service and resources. The controls
might not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [EFS.1] Elastic File System should be configured to encrypt file data at-rest using AWS KMS

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/2.3.1, CIS AWS Foundations Benchmark v3.0.0/2.4.1, NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5 SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::EFS::FileSystem`

**AWS Config rule:**
[efs-encrypted-check](../../../config/latest/developerguide/efs-encrypted-check.md "../../../config/latest/developerguide/efs-encrypted-check.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether Amazon Elastic File System is configured to encrypt the file data using AWS KMS.
The check fails in the following cases.

- `Encrypted` is set to `false` in the [`DescribeFileSystems`](../../../efs/latest/ug/API_DescribeFileSystems.md "../../../efs/latest/ug/API_DescribeFileSystems.md")
  response.
- The `KmsKeyId` key in the [`DescribeFileSystems`](../../../efs/latest/ug/API_DescribeFileSystems.md "../../../efs/latest/ug/API_DescribeFileSystems.md")
  response does not match the `KmsKeyId` parameter for [`efs-encrypted-check`](../../../config/latest/developerguide/efs-encrypted-check.md "../../../config/latest/developerguide/efs-encrypted-check.md").

Note that this control does not use the `KmsKeyId` parameter for [`efs-encrypted-check`](../../../config/latest/developerguide/efs-encrypted-check.md "../../../config/latest/developerguide/efs-encrypted-check.md"). It only checks the value of
`Encrypted`.

For an added layer of security for your sensitive data in Amazon EFS, you should create
encrypted file systems. Amazon EFS supports encryption for file systems at-rest. You can enable
encryption of data at rest when you create an Amazon EFS file system. To learn more about Amazon EFS
encryption, see [Data encryption
in Amazon EFS](../../../efs/latest/ug/encryption.md "../../../efs/latest/ug/encryption.md") in the _Amazon Elastic File System User Guide_.

### Remediation

For details on how to encrypt a new Amazon EFS file system, see [Encrypting data at rest](../../../efs/latest/ug/encryption-at-rest.md "../../../efs/latest/ug/encryption-at-rest.md") in the _Amazon Elastic File System User Guide_.

## [EFS.2] Amazon EFS volumes should be in backup plans

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6, NIST.800-53.r5 CP-6(1), NIST.800-53.r5 CP-6(2), NIST.800-53.r5 CP-9, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-12, NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > Backup

**Severity:** Medium

**Resource type:**
`AWS::EFS::FileSystem`

**AWS Config rule:**
[efs-in-backup-plan](../../../config/latest/developerguide/efs-in-backup-plan.md "../../../config/latest/developerguide/efs-in-backup-plan.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether Amazon Elastic File System (Amazon EFS) file systems are added to the backup plans in
AWS Backup. The control fails if Amazon EFS file systems are not included in the backup plans.

Including EFS file systems in the backup plans helps you to protect your data from deletion
and data loss.

### Remediation

To enable automatic backups for an existing Amazon EFS file system, see [Getting started 4: Create Amazon EFS automatic backups](../../../aws-backup/latest/devguide/create-auto-backup.md "../../../aws-backup/latest/devguide/create-auto-backup.md") in the _AWS Backup Developer Guide_.

## [EFS.3] EFS access points should enforce a root directory

**Related requirements:** NIST.800-53.r5 AC-6(10)

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:**
`AWS::EFS::AccessPoint`

**AWS Config rule:**
[efs-access-point-enforce-root-directory](../../../config/latest/developerguide/efs-access-point-enforce-root-directory.md "../../../config/latest/developerguide/efs-access-point-enforce-root-directory.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks if Amazon EFS access points are configured to enforce a root directory. The
control fails if the value of `Path` is set to `/` (the default root directory of the file system).

When you enforce a root directory, the NFS client using the access point uses the root
directory configured on the access point instead of the file system's root directory. Enforcing a
root directory for an access point helps restrict data access by ensuring that users of the access
point can only reach files of the specified subdirectory.

### Remediation

For instructions on how to enforce a root directory for an Amazon EFS access point, see [Enforcing a root directory with an access point](../../../efs/latest/ug/efs-access-points.md#enforce-root-directory-access-point "../../../efs/latest/ug/efs-access-points.md#enforce-root-directory-access-point") in the _Amazon Elastic File System User Guide_.

## [EFS.4] EFS access points should enforce a user identity

**Related requirements:** NIST.800-53.r5 AC-6(2), PCI DSS v4.0.1/7.3.1

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:**
`AWS::EFS::AccessPoint`

**AWS Config rule:**
[efs-access-point-enforce-user-identity](../../../config/latest/developerguide/efs-access-point-enforce-user-identity.md "../../../config/latest/developerguide/efs-access-point-enforce-user-identity.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether Amazon EFS access points are configured to enforce a user identity.
This control fails if a POSIX user identity is not defined while creating the EFS
access point.

Amazon EFS access points are application-specific entry points into an EFS file system that make it easier to manage application access to shared
datasets. Access points can enforce a user identity, including the user's POSIX groups, for all file system requests that are made through the access point.
Access points can also enforce a different root directory for the file system so that clients can only access data in the specified directory or its
subdirectories.

### Remediation

To enforce a user identity for an Amazon EFS access point, see [Enforcing a user identity using an access point](../../../efs/latest/ug/efs-access-points.md#enforce-identity-access-points "../../../efs/latest/ug/efs-access-points.md#enforce-identity-access-points") in the _Amazon Elastic File System User Guide_.

## [EFS.5] EFS access points should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::EFS::AccessPoint`

**AWS Configrule:** `tagged-efs-accesspoint` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value           |

This control checks whether an Amazon EFS access point has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the access point doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the access point isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_AWS General Reference_.

### Remediation

To add tags to an EFS access point, see [Tagging Amazon EFS resources](../../../efs/latest/ug/manage-fs-tags.md "../../../efs/latest/ug/manage-fs-tags.md") in the _Amazon Elastic File System User Guide_.

## [EFS.6] EFS mount targets should not be associated with subnets that assign

public IP addresses on launch

**Category:** Protect > Network security > Resources not
publicly accessible

**Severity:** Medium

**Resource type:**
`AWS::EFS::FileSystem`

**AWS Config rule:**
[efs-mount-target-public-accessible](../../../config/latest/developerguide/efs-mount-target-public-accessible.md "../../../config/latest/developerguide/efs-mount-target-public-accessible.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an Amazon EFS mount target is associated with subnets that
assign public IP addresses on launch. The control fails if the mount target is
associated with subnets that assign public IP addresses on launch.

All subnets have an attribute that determines whether a network interface created in
the subnet automatically receives a public IPv4 address. Amazon EFS mount targets that are
launched into subnets that have this attribute enabled have a public IP address assigned
to their primary network interface.

### Remediation

To associate an existing mount target with a different subnet, you must create a
new mount target in a subnet that does not assign public IP addresses on launch and
then remove the old mount target. For information about managing mount targets, see
[Creating and
managing mount targets and security groups](../../../efs/latest/ug/accessing-fs.md "../../../efs/latest/ug/accessing-fs.md") in the _Amazon Elastic File System User Guide_.

## [EFS.7] EFS file systems should have automatic backups enabled

**Category:** Recover > Resilience > Backups
enabled

**Severity:** Medium

**Resource type:**
`AWS::EFS::FileSystem`

**AWS Config rule:**
[efs-automatic-backups-enabled](../../../config/latest/developerguide/efs-automatic-backups-enabled.md "../../../config/latest/developerguide/efs-automatic-backups-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon EFS file system has automatic backups enabled. This control fails if the EFS file
system doesn't have automatic backups enabled.

A data backup is a copy of your system, configuration, or application data that's stored separately from the
original. Enabling regular backups helps you safeguard valuable data against unforeseen events like system failures, cyberattacks,
or accidental deletions. Having a robust backup strategy also facilitates quicker recovery, business continuity, and peace of mind
in the face of potential data loss.

### Remediation

For information about using AWS Backup for EFS file systems, see [Backing up EFS file
systems](../../../efs/latest/ug/awsbackup.md "../../../efs/latest/ug/awsbackup.md") in the _Amazon Elastic File System User Guide_.

## [EFS.8] EFS file systems should be encrypted at rest

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/2.3.1

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::EFS::FileSystem`

**AWS Config rule:**
[efs-filesystem-ct-encrypted](../../../config/latest/developerguide/efs-filesystem-ct-encrypted.md "../../../config/latest/developerguide/efs-filesystem-ct-encrypted.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon EFS file system encrypts data with AWS Key Management Service (AWS KMS). The control fails if a file
system isn't encrypted.

Data at rest refers to data that's stored in persistent, non-volatile storage for any duration. Encrypting data at rest helps you protect its confidentiality, which reduces the risk that an unauthorized user can access it.

### Remediation

To enable encryption at rest for a new EFS file system, see [Encrypting data at rest](../../../efs/latest/ug/encryption-at-rest.md "../../../efs/latest/ug/encryption-at-rest.md")
in the _Amazon Elastic File System User Guide_.
