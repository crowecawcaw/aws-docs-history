# Security Hub controls for Amazon DocumentDB

These AWS Security Hub controls evaluate the Amazon DocumentDB (with MongoDB compatibility) service and resources. The controls might
not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [DocumentDB.1] Amazon DocumentDB clusters should be encrypted at

rest

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5
SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[docdb-cluster-encrypted](../../../config/latest/developerguide/docdb-cluster-encrypted.md "../../../config/latest/developerguide/docdb-cluster-encrypted.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon DocumentDB cluster is encrypted at rest. The control
fails if an Amazon DocumentDB cluster isn't encrypted at rest.

Data at rest refers to any data that's stored in persistent, non-volatile storage for
any duration. Encryption helps you protect the confidentiality of such data, reducing
the risk that an unauthorized user gets access to it. Data in Amazon DocumentDB clusters should be
encrypted at rest for an added layer of security. Amazon DocumentDB uses the 256-bit Advanced
Encryption Standard (AES-256) to encrypt your data using encryption keys stored in
AWS Key Management Service (AWS KMS).

### Remediation

You can enable encryption at rest when you create an Amazon DocumentDB cluster. You can't
change encryption settings after creating a cluster. For more information, see
[Enabling encryption at rest for an Amazon DocumentDB cluster](../../../documentdb/latest/developerguide/encryption-at-rest.md#encryption-at-rest-enabling "../../../documentdb/latest/developerguide/encryption-at-rest.md#encryption-at-rest-enabling") in the _Amazon DocumentDB Developer Guide_.

## [DocumentDB.2] Amazon DocumentDB clusters should have an adequate

backup retention period

**Related requirements:** NIST.800-53.r5 SI-12,
PCI DSS v4.0.1/3.2.1

**Category:** Recover > Resilience > Backups
enabled

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[docdb-cluster-backup-retention-check](../../../config/latest/developerguide/docdb-cluster-backup-retention-check.md "../../../config/latest/developerguide/docdb-cluster-backup-retention-check.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter                      | Description                             | Type    | Allowed custom values | Security Hub default value |
| ------------------------------ | --------------------------------------- | ------- | --------------------- | -------------------------- |
| `minimumBackupRetentionPeriod` | Minimum backup retention period in days | Integer | `7` to `35`           | `7`                        |

This control checks whether an Amazon DocumentDB cluster has a backup retention period greater
than or equal to the specified time frame. The control fails if the backup retention
period is less than the specified time frame. Unless you provide a custom parameter
value for the backup retention period, Security Hub uses a default value of 7 days.

Backups help you recover more quickly from a security incident and strengthen the
resilience of your systems. By automating backups for your Amazon DocumentDB clusters, you'll be
able to restore your systems to a point in time and minimize downtime and data loss. In
Amazon DocumentDB, clusters have a default backup retention period of 1 day. This must be
increased to a value between 7 and 35 days to pass this control.

### Remediation

To change the backup retention period for your Amazon DocumentDB clusters, see [Modifying an
Amazon DocumentDB cluster](../../../documentdb/latest/developerguide/db-cluster-modify.md "../../../documentdb/latest/developerguide/db-cluster-modify.md") in the _Amazon DocumentDB Developer Guide_. For **Backup**, choose the backup
retention period.

## [DocumentDB.3] Amazon DocumentDB manual cluster snapshots should

not be public

**Related requirements:** NIST.800-53.r5 AC-21,
NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5
AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11),
NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21),
NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9),
PCI DSS v4.0.1/1.4.4

**Category:** Protect > Secure network
configuration

**Severity:** Critical

**Resource type:**
`AWS::RDS::DBClusterSnapshot`

**AWS Config rule:**
[docdb-cluster-snapshot-public-prohibited](../../../config/latest/developerguide/docdb-cluster-snapshot-public-prohibited.md "../../../config/latest/developerguide/docdb-cluster-snapshot-public-prohibited.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon DocumentDB manual cluster snapshot is public. The
control fails if the manual cluster snapshot is public.

An Amazon DocumentDB manual cluster snapshot should not be public unless intended. If you
share an unencrypted manual snapshot as public, the snapshot is available to all
AWS accounts. Public snapshots may result in unintended data exposure.

###### Note

This control evaluates manual cluster snapshots. You can't share an Amazon DocumentDB
automated cluster snapshot. However, you can create a manual snapshot by copying
the automated snapshot, and then share the copy.

### Remediation

To remove public access for Amazon DocumentDB manual cluster snapshots, see [Sharing a snapshot](../../../documentdb/latest/developerguide/backup_restore-share_cluster_snapshots.md#backup_restore-share_snapshots "../../../documentdb/latest/developerguide/backup_restore-share_cluster_snapshots.md#backup_restore-share_snapshots") in the _Amazon DocumentDB Developer Guide_. Programmatically, you can use the Amazon DocumentDB
operation `modify-db-snapshot-attribute`. Set `attribute-name`
as `restore` and `values-to-remove` as
`all`.

## [DocumentDB.4] Amazon DocumentDB clusters should publish audit

logs to CloudWatch Logs

**Related requirements:** NIST.800-53.r5 AC-2(4),
NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AC-6(9), NIST.800-53.r5 AU-10, NIST.800-53.r5
AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5
AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-3(8),
NIST.800-53.r5 SI-4(20), NIST.800-53.r5 SI-7(8), PCI DSS v4.0.1/10.3.3

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[docdb-cluster-audit-logging-enabled](../../../config/latest/developerguide/docdb-cluster-audit-logging-enabled.md "../../../config/latest/developerguide/docdb-cluster-audit-logging-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon DocumentDB cluster publishes audit logs to Amazon CloudWatch Logs.
The control fails if the cluster doesn't publish audit logs to CloudWatch Logs.

Amazon DocumentDB (with MongoDB compatibility) allows you to audit events that were performed in
your cluster. Examples of logged events include successful and failed authentication
attempts, dropping a collection in a database, or creating an index. By default,
auditing is disabled in Amazon DocumentDB and requires that you take action to enable it.

### Remediation

To publish Amazon DocumentDB audit logs to CloudWatch Logs, see [Enabling auditing](../../../documentdb/latest/developerguide/event-auditing.md#event-auditing-enabling-auditing "../../../documentdb/latest/developerguide/event-auditing.md#event-auditing-enabling-auditing") in the _Amazon DocumentDB Developer Guide_.

## [DocumentDB.5] Amazon DocumentDB clusters should have deletion

protection enabled

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2), NIST.800-53.r5 CM-3, NIST.800-53.r5
SC-5(2)

**Category:** Protect > Data protection > Data deletion
protection

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[docdb-cluster-deletion-protection-enabled](../../../config/latest/developerguide/docdb-cluster-deletion-protection-enabled.md "../../../config/latest/developerguide/docdb-cluster-deletion-protection-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon DocumentDB cluster has deletion protection enabled. The
control fails if the cluster doesn't have deletion protection enabled.

Enabling cluster deletion protection offers an additional layer of protection
against accidental database deletion or deletion by an unauthorized user. An Amazon DocumentDB
cluster can't be deleted while deletion protection is enabled. You must first disable
deletion protection before a delete request can succeed. Deletion protection is enabled
by default when you create a cluster in the Amazon DocumentDB console.

### Remediation

To enable deletion protection for an existing Amazon DocumentDB cluster, see [Modifying an
Amazon DocumentDB cluster](../../../documentdb/latest/developerguide/db-cluster-modify.md "../../../documentdb/latest/developerguide/db-cluster-modify.md") in the _Amazon DocumentDB Developer Guide_. In the **Modify Cluster**
section, choose **Enable** for **Deletion
protection**.

## [DocumentDB.6] Amazon DocumentDB clusters should be encrypted in

transit

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[docdb-cluster-encrypted-in-transit](../../../config/latest/developerguide/docdb-cluster-encrypted-in-transit.md "../../../config/latest/developerguide/docdb-cluster-encrypted-in-transit.md")

**Schedule type:** Periodic

**Parameters:**
`excludeTlsParameters`: `disabled`, `enabled` (not
customizable)

This controls checks whether an Amazon DocumentDB cluster requires TLS for connections to the
cluster. The control fails if the cluster parameter group associated with the cluster is
not in sync, or the TLS cluster parameter is set to `disabled` or
`enabled`.

You can use TLS to encrypt the connection between an application and an Amazon DocumentDB
cluster. Use of TLS can help protect data from being intercepted while the data is in
transit between an application and an Amazon DocumentDB cluster. Encryption in transit for an
Amazon DocumentDB cluster is managed using the TLS parameter in the cluster parameter group
that's associated with the cluster. When encryption in transit is enabled, secure
connections using TLS are required to connect to the cluster. We recommend using the
following TLS parameters: `tls1.2+`, `tls1.3+`, and
`fips-140-3`.

### Remediation

For information about changing the TLS settings for an Amazon DocumentDB cluster, see
[Encrypting data in transit](../../../documentdb/latest/developerguide/security.encryption.md "../../../documentdb/latest/developerguide/security.encryption.md") in the _Amazon DocumentDB
Developer Guide_.
