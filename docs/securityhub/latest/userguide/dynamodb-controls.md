# Security Hub CSPM controls for DynamoDB

These AWS Security Hub CSPM controls evaluate the Amazon DynamoDB service and resources. The controls might
not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [DynamoDB.1] DynamoDB tables should automatically scale capacity with demand

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-2(2), NIST.800-53.r5 CP-6(2), NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:**
`AWS::DynamoDB::Table`

**AWS Config rule:**
[`dynamodb-autoscaling-enabled`](../../../config/latest/developerguide/dynamodb-autoscaling-enabled.md "../../../config/latest/developerguide/dynamodb-autoscaling-enabled.md")

**Schedule type:** Periodic

**Parameters:**

| Parameter                     | Description                                                                  | Type    | Valid custom values | Security Hub CSPM default value |
| ----------------------------- | ---------------------------------------------------------------------------- | ------- | ------------------- | ------------------------------- |
| `minProvisionedReadCapacity`  | Minimum number of provisioned read capacity units for DynamoDB auto scaling  | Integer | `1` to `40000`      | No default value                |
| `targetReadUtilization`       | Target utilization percentage for read capacity                              | Integer | `20` to `90`        | No default value                |
| `minProvisionedWriteCapacity` | Minimum number of provisioned write capacity units for DynamoDB auto scaling | Integer | `1` to `40000`      | No default value                |
| `targetWriteUtilization`      | Target utilization percentage for write capacity                             | Integer | `20` to `90`        | No default value                |

This control checks whether an Amazon DynamoDB table can scale its read and write capacity as
needed. The control fails if the table doesn't use on-demand capacity mode or provisioned mode
with auto scaling configured. By default, this control only requires that one of these modes be configured, without regard to
specific levels of read or write capacity. Optionally, you can provide custom parameter values to require specific levels of read
and write capacity or target utilization.

Scaling capacity with demand avoids throttling exceptions, which
helps to maintain availability of your applications. DynamoDB tables that use on-demand capacity mode are limited only by the DynamoDB throughput default
table quotas. To raise these quotas, you can file a support ticket with Support. DynamoDB tables that use provisioned mode with auto scaling adjust the provisioned throughput
capacity dynamically in response to traffic patterns. For more information about DynamoDB
request throttling, see [Request throttling and burst capacity](../../../amazondynamodb/latest/developerguide/ProvisionedThroughput.md#ProvisionedThroughput.Throttling "../../../amazondynamodb/latest/developerguide/ProvisionedThroughput.md#ProvisionedThroughput.Throttling") in the _Amazon DynamoDB Developer Guide_.

### Remediation

To enable DynamoDB automatic scaling on existing tables in
capacity mode, see [Enabling DynamoDB auto scaling on existing tables](../../../amazondynamodb/latest/developerguide/AutoScaling.md#AutoScaling.Console.ExistingTable "../../../amazondynamodb/latest/developerguide/AutoScaling.md#AutoScaling.Console.ExistingTable") in the _Amazon DynamoDB Developer Guide_.

## [DynamoDB.2] DynamoDB tables should have point-in-time recovery enabled

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6(2), NIST.800-53.r5 CP-9, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-12, NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > Backups enabled

**Severity:** Medium

**Resource type:**
`AWS::DynamoDB::Table`

**AWS Config rule:**
[`dynamodb-pitr-enabled`](../../../config/latest/developerguide/dynamodb-pitr-enabled.md "../../../config/latest/developerguide/dynamodb-pitr-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether point-in-time recovery (PITR) is enabled for an Amazon DynamoDB
table.

Backups help you to recover more quickly from a security incident. They also strengthen the
resilience of your systems. DynamoDB point-in-time recovery automates backups for DynamoDB tables. It
reduces the time to recover from accidental delete or write operations. DynamoDB tables that have
PITR enabled can be restored to any point in time in the last 35 days.

### Remediation

To restore a DynamoDB table to a point in time, see [Restoring a DynamoDB table to a point in time](../../../amazondynamodb/latest/developerguide/PointInTimeRecovery.md "../../../amazondynamodb/latest/developerguide/PointInTimeRecovery.md") in the _Amazon DynamoDB Developer Guide_.

## [DynamoDB.3] DynamoDB Accelerator (DAX) clusters should be encrypted at rest

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5 SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::DAX::Cluster`

**AWS Config rule:**
[`dax-encryption-enabled`](../../../config/latest/developerguide/dax-encryption-enabled.md "../../../config/latest/developerguide/dax-encryption-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an Amazon DynamoDB Accelerator (DAX) cluster is encrypted at rest. The control
fails if the DAX cluster isn't encrypted at rest.

Encrypting data at rest reduces the risk of data stored on disk being accessed by a user
not authenticated to AWS. The encryption adds another set of access controls to limit the
ability of unauthorized users to access to the data. For example, API permissions are required
to decrypt the data before it can be read.

### Remediation

You cannot enable or disable encryption at rest after a cluster is created. You must
recreate the cluster in order to enable encryption at rest. For detailed instructions on how to
create a DAX cluster with encryption at rest enabled, see [Enabling encryption at rest using the AWS Management Console](../../../amazondynamodb/latest/developerguide/DAXEncryptionAtRest.md#dax.encryption.tutorial-console "../../../amazondynamodb/latest/developerguide/DAXEncryptionAtRest.md#dax.encryption.tutorial-console") in the _Amazon DynamoDB Developer Guide_.

## [DynamoDB.4] DynamoDB tables should be present in a backup plan

**Related requirements:** NIST.800-53.r5 CP-10,
NIST.800-53.r5 CP-6,
NIST.800-53.r5 CP-6(1),
NIST.800-53.r5 CP-6(2),
NIST.800-53.r5 CP-9,
NIST.800-53.r5 SC-5(2),
NIST.800-53.r5 SI-12,
NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > Backups enabled

**Severity:** Medium

**Resource type:**
`AWS::DynamoDB::Table`

**AWS Config rule:**
[`dynamodb-resources-protected-by-backup-plan`](../../../config/latest/developerguide/dynamodb-resources-protected-by-backup-plan.md "../../../config/latest/developerguide/dynamodb-resources-protected-by-backup-plan.md")

**Schedule type:** Periodic

**Parameters:**

| Parameter              | Description                                                                                                               | Type    | Allowed custom values | Security Hub CSPM default value |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------- | --------------------- | ------------------------------- |
| `backupVaultLockCheck` | The control produces a `PASSED` finding if the parameter is set to `true` and<br>the resource uses AWS Backup Vault Lock. | Boolean | `true` or `false`     | No default value                |

This control evaluates whether an Amazon DynamoDB table in `ACTIVE` state is covered by a backup plan. The control
fails if the DynamoDB table isn't covered by a backup plan. If you set the `backupVaultLockCheck`
parameter equal to `true`, the control passes only if the DynamoDB table is backed up in an AWS Backup locked vault.

AWS Backup is a fully managed backup service that helps you centralize and automate the backing up of data across
AWS services. With AWS Backup, you can create backup plans that define your backup requirements, such as how
frequently to back up your data and how long to retain those backups. Including DynamoDB tables in your backup plans helps
you protect your data from unintended loss or deletion.

### Remediation

To add a DynamoDB table to an AWS Backup backup plan, see [Assigning resources to a backup plan](../../../aws-backup/latest/devguide/assigning-resources.md "../../../aws-backup/latest/devguide/assigning-resources.md") in the _AWS Backup Developer Guide_.

## [DynamoDB.5] DynamoDB tables should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::DynamoDB::Table`

**AWS Config rule:** `tagged-dynamodb-table` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | `No default value`              |

This control checks whether an Amazon DynamoDB table has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the table doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the table isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
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

To add tags to a DynamoDB table, see [Tagging resources in DynamoDB](../../../amazondynamodb/latest/developerguide/Tagging.md "../../../amazondynamodb/latest/developerguide/Tagging.md") in the
_Amazon DynamoDB Developer Guide_.

## [DynamoDB.6] DynamoDB tables should have deletion protection enabled

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-2,
NIST.800-53.r5 CM-2(2),
NIST.800-53.r5 CM-3,
NIST.800-53.r5 SC-5(2)

**Category:** Protect > Data protection > Data deletion protection

**Severity:** Medium

**Resource type:**
`AWS::DynamoDB::Table`

**AWS Config rule:**
[`dynamodb-table-deletion-protection-enabled`](../../../config/latest/developerguide/dynamodb-table-deletion-protection-enabled.md "../../../config/latest/developerguide/dynamodb-table-deletion-protection-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon DynamoDB table has deletion protection enabled. The control fails if a DynamoDB table
doesn't have deletion protection enabled.

You can protect a DynamoDB table from accidental deletion with the deletion protection property. Enabling this property
for tables helps ensure that tables don't get accidentally deleted during regular table management operations by your
administrators. This helps prevent disruption to your normal business operations.

### Remediation

To enable deletion protection for a DynamoDB table, see [Using deletion protection](../../../amazondynamodb/latest/developerguide/WorkingWithTables.md#WorkingWithTables.Basics.DeletionProtection "../../../amazondynamodb/latest/developerguide/WorkingWithTables.md#WorkingWithTables.Basics.DeletionProtection") in the
_Amazon DynamoDB Developer Guide_.

## [DynamoDB.7] DynamoDB Accelerator clusters should be encrypted in transit

**Related requirements:** NIST.800-53.r5 AC-17,
NIST.800-53.r5 SC-8,
NIST.800-53.r5 SC-13,
NIST.800-53.r5 SC-23, PCI DSS v4.0.1/4.2.1

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::DAX::Cluster`

**AWS Config rule:**
[`dax-tls-endpoint-encryption`](../../../config/latest/developerguide/dax-tls-endpoint-encryption.md "../../../config/latest/developerguide/dax-tls-endpoint-encryption.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an Amazon DynamoDB Accelerator (DAX) cluster is encrypted in transit, with the endpoint
encryption type set to TLS. The control fails if the DAX cluster isn't encrypted in transit.

HTTPS (TLS) can be used to help prevent potential attackers from using person-in-the-middle or similar attacks to
eavesdrop on or manipulate network traffic. You should only allow encrypted connections over TLS to access DAX clusters. However,
encrypting data in transit can affect performance. You should test your application with encryption turned on to understand the
performance profile and the impact of TLS.

### Remediation

You can't change the TLS encryption setting after creating a DAX cluster. To encrypt an existing DAX cluster, create a new cluster with encryption in transit enabled, shift your application's traffic to it, and then delete the old cluster. For more information, see [Using deletion protection](../../../amazondynamodb/latest/developerguide/WorkingWithTables.md#WorkingWithTables.Basics.DeletionProtection "../../../amazondynamodb/latest/developerguide/WorkingWithTables.md#WorkingWithTables.Basics.DeletionProtection") in the
_Amazon DynamoDB Developer Guide_.
