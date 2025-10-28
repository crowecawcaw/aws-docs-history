# Security Hub controls for Neptune

These AWS Security Hub controls evaluate the Amazon Neptune service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [Neptune.1] Neptune DB clusters should be encrypted at

rest

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5
SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[`neptune-cluster-encrypted`](../../../config/latest/developerguide/neptune-cluster-encrypted.md "../../../config/latest/developerguide/neptune-cluster-encrypted.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether a Neptune DB cluster is encrypted at rest. The control
fails if a Neptune DB cluster isn't encrypted at rest.

Data at rest refers to any data that's stored in persistent, non-volatile storage for
any duration. Encryption helps you protect the confidentiality of such data, reducing
the risk that an unauthorized user can access it. Encrypting your Neptune DB clusters
protects your data and metadata against unauthorized access. It also fulfills compliance
requirements for data-at-rest encryption of production file systems.

### Remediation

You can enable encryption at rest when you create a Neptune DB cluster. You can't change encryption settings after creating a cluster. For more information, see [Encrypting
Neptune resources at rest](../../../neptune/latest/userguide/encrypt.md "../../../neptune/latest/userguide/encrypt.md") in the
_Neptune User Guide_.

## [Neptune.2] Neptune DB clusters should publish audit

logs to CloudWatch Logs

**Related requirements:** NIST.800-53.r5 AC-2(4),
NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AC-6(9), NIST.800-53.r5 AU-10, NIST.800-53.r5
AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(1), NIST.800-53.r5
AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 AU-6(5), NIST.800-53.r5 AU-7(1),
NIST.800-53.r5 AU-9(7), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9), NIST.800-53.r5
SI-20, NIST.800-53.r5 SI-3(8), NIST.800-53.r5 SI-4(20), NIST.800-53.r5 SI-4(5),
NIST.800-53.r5 SI-7(8), PCI DSS v4.0.1/10.3.3

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[`neptune-cluster-cloudwatch-log-export-enabled`](../../../config/latest/developerguide/neptune-cluster-cloudwatch-log-export-enabled.md "../../../config/latest/developerguide/neptune-cluster-cloudwatch-log-export-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether a Neptune DB cluster publishes audit logs to Amazon CloudWatch Logs.
The control fails if a Neptune DB cluster doesn't publish audit logs to CloudWatch Logs.
`EnableCloudWatchLogsExport` should be set to `Audit`.

Amazon Neptune and Amazon CloudWatch are integrated so that you can gather and analyze
performance metrics. Neptune automatically sends metrics to CloudWatch and also supports
CloudWatch Alarms. Audit logs are highly customizable. When you audit a database, each
operation on the data can be monitored and logged to an audit trail, including
information about which database cluster is accessed and how. We recommend sending these
logs to CloudWatch to help you monitor your Neptune DB clusters.

### Remediation

To publish Neptune audit logs to CloudWatch Logs, see [Publishing Neptune logs
to Amazon CloudWatch Logs](../../../neptune/latest/userguide/cloudwatch-logs.md "../../../neptune/latest/userguide/cloudwatch-logs.md") in the _Neptune User Guide_. In the
**Log exports** section, choose **Audit**.

## [Neptune.3] Neptune DB cluster snapshots should not be

public

**Related requirements:** NIST.800-53.r5 AC-21,
NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5
AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11),
NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21),
NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9), PCI DSS v4.0.1/1.4.4

**Category:** Protect > Secure network configuration > Resources not publicly accessible

**Severity:** Critical

**Resource type:**
`AWS::RDS::DBClusterSnapshot`

**AWS Config rule:**
[`neptune-cluster-snapshot-public-prohibited`](../../../config/latest/developerguide/neptune-cluster-snapshot-public-prohibited.md "../../../config/latest/developerguide/neptune-cluster-snapshot-public-prohibited.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether a Neptune manual DB cluster snapshot is public. The
control fails if a Neptune manual DB cluster snapshot is public.

A Neptune DB cluster manual snapshot should not be public unless intended. If you
share an unencrypted manual snapshot as public, the snapshot is available to all
AWS accounts. Public snapshots may result in unintended data exposure.

### Remediation

To remove public access for Neptune manual DB cluster snapshots, see [Sharing a DB
cluster snapshot](../../../neptune/latest/userguide/backup-restore-share-snapshot.md "../../../neptune/latest/userguide/backup-restore-share-snapshot.md") in the _Neptune User Guide_.

## [Neptune.4] Neptune DB clusters should have deletion

protection enabled

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2), NIST.800-53.r5 CM-3, NIST.800-53.r5
SC-5(2)

**Category:** Protect > Data protection > Data deletion
protection

**Severity:** Low

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[`neptune-cluster-deletion-protection-enabled`](../../../config/latest/developerguide/neptune-cluster-deletion-protection-enabled.md "../../../config/latest/developerguide/neptune-cluster-deletion-protection-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks if a Neptune DB cluster has deletion protection enabled. The
control fails if a Neptune DB cluster doesn't have deletion protection enabled.

Enabling cluster deletion protection offers an additional layer of protection against
accidental database deletion or deletion by an unauthorized user. A Neptune DB cluster
can't be deleted while deletion protection is enabled. You must first disable deletion
protection before a delete request can succeed.

### Remediation

To enable deletion protection for an existing Neptune DB cluster, see [Modifying the DB cluster by using the console, CLI, and API](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md#Aurora.Modifying.Settings "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md#Aurora.Modifying.Settings") in the
_Amazon Aurora User Guide_.

## [Neptune.5] Neptune DB clusters should have automated

backups enabled

**Related requirements:** NIST.800-53.r5 SI-12

**Category:** Recover > Resilience > Backups
enabled

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[`neptune-cluster-backup-retention-check`](../../../config/latest/developerguide/neptune-cluster-backup-retention-check.md "../../../config/latest/developerguide/neptune-cluster-backup-retention-check.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter                      | Description                             | Type    | Allowed custom values | Security Hub default value |
| ------------------------------ | --------------------------------------- | ------- | --------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `minimumBackupRetentionPeriod` | Minimum backup retention period in days | Integer | `7` to `35`           | `7`                        | This control checks whether a Neptune DB cluster has automated backups enabled, and a backup retention period greater than or equal to the specified time frame. The control fails if backups aren't enabled for the Neptune DB cluster, or if the retention period is less than the specified time frame. Unless you provide a custom parameter value for the backup retention period, Security Hub uses a default value of 7 days. Backups help you recover more quickly from a security incident and strengthen the resilience of your systems. By automating backups for your Neptune DB clusters, you'll be able to restore your systems to a point in time and minimize downtime and data loss. ### Remediation To enable automated backups and set a backup retention period for your Neptune DB clusters, see [Enabling automated backups](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md#USER_WorkingWithAutomatedBackups.Enabling "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md#USER_WorkingWithAutomatedBackups.Enabling") in the _Amazon RDS User Guide_. For **Backup retention period**, choose a value greater than or equal to 7. ## [Neptune.6] Neptune DB cluster snapshots should be encrypted at rest **Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5 SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SC-7(18) **Category:** Protect > Data Protection > Encryption of data-at-rest **Severity:** Medium **Resource type:** `AWS::RDS::DBClusterSnapshot` **AWS Config rule:** [`neptune-cluster-snapshot-encrypted`](../../../config/latest/developerguide/neptune-cluster-snapshot-encrypted.md "../../../config/latest/developerguide/neptune-cluster-snapshot-encrypted.md") **Schedule type:** Change triggered **Parameters:** None This control checks whether a Neptune DB cluster snapshot is encrypted at rest. The control fails if a Neptune DB cluster isn't encrypted at rest. Data at rest refers to any data that's stored in persistent, non-volatile storage for any duration. Encryption helps you protect the confidentiality of such data, reducing the risk that an unauthorized user gets access to it. Data in Neptune DB clusters snapshots should be encrypted at rest for an added layer of security. ### Remediation You can't encrypt an existing Neptune DB cluster snapshot. Instead, you must restore the snapshot to a new DB cluster and enable encryption on the cluster. You can create an encrypted snapshot from the encrypted cluster. For instructions, see [Restoring from a DB cluster snapshot](../../../neptune/latest/userguide/backup-restore-restore-snapshot.md "../../../neptune/latest/userguide/backup-restore-restore-snapshot.md") and [Creating a DB cluster snapshot in Neptune](../../../neptune/latest/userguide/backup-restore-create-snapshot.md "../../../neptune/latest/userguide/backup-restore-create-snapshot.md") in the _Neptune User Guide_. ## [Neptune.7] Neptune DB clusters should have IAM database authentication enabled **Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-6 **Category:** Protect > Secure access management > Passwordless authentication **Severity:** Medium **Resource type:** `AWS::RDS::DBCluster` **AWS Config rule:** [`neptune-cluster-iam-database-authentication`](../../../config/latest/developerguide/neptune-cluster-iam-database-authentication.md "../../../config/latest/developerguide/neptune-cluster-iam-database-authentication.md") **Schedule type:** Change triggered **Parameters:** None This control checks if a Neptune DB cluster has IAM database authentication enabled. The control fails if IAM database authentication isn't enabled for a Neptune DB cluster. IAM database authentication for Amazon Neptune database clusters removes the need to store user credentials within the database configuration because authentication is managed externally using IAM. When IAM database authentication is enabled, each request needs to be signed using AWS Signature Version 4. ### Remediation By default, IAM database authentication is disabled when you create a Neptune DB cluster. To enable it, see [Enabling IAM database authentication in Neptune](../../../neptune/latest/userguide/iam-auth-enable.md "../../../neptune/latest/userguide/iam-auth-enable.md") in the _Neptune User Guide_. ## [Neptune.8] Neptune DB clusters should be configured to copy tags to snapshots **Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2) **Category:** Identify > Inventory > Tagging **Severity:** Low **Resource type:** `AWS::RDS::DBCluster` **AWS Config rule:** [`neptune-cluster-copy-tags-to-snapshot-enabled`](../../../config/latest/developerguide/neptune-cluster-copy-tags-to-snapshot-enabled.md "../../../config/latest/developerguide/neptune-cluster-copy-tags-to-snapshot-enabled.md") **Schedule type:** Change triggered **Parameters:** None This control checks if a Neptune DB cluster is configured to copy all tags to snapshots when the snapshots are created. The control fails if a Neptune DB cluster isn't configured to copy tags to snapshots. Identification and inventory of your IT assets is a crucial aspect of governance and security. You should tag snapshots in the same way as their parent Amazon RDS database clusters. Copying tags ensures that the metadata for the DB snapshots matches that of the parent database clusters, and that access policies for the DB snapshot also match those of the parent DB instance. ### Remediation To copy tags to snapshots for Neptune DB clusters, see [Copying tags in Neptune](../../../neptune/latest/userguide/tagging.md#tagging-overview "../../../neptune/latest/userguide/tagging.md#tagging-overview") in the _Neptune User Guide_. ## [Neptune.9] Neptune DB clusters should be deployed across multiple Availability Zones **Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6(2), NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5) **Category:** Recover > Resilience > High availability **Severity:** Medium **Resource type:** `AWS::RDS::DBCluster` **AWS Config rule:** [`neptune-cluster-multi-az-enabled`](../../../config/latest/developerguide/neptune-cluster-multi-az-enabled.md "../../../config/latest/developerguide/neptune-cluster-multi-az-enabled.md") **Schedule type:** Change triggered **Parameters:** None This control checks if an Amazon Neptune DB cluster has read-replica instances in multiple Availability Zones (AZs). The control fails if the cluster is deployed in only one AZ. If an AZ is unavailable and during regular maintenance events, read-replicas serve as failover targets for the primary instance. That is, if the primary instance fails, Neptune promotes a read-replica instance to become the primary instance. By contrast, if your DB cluster doesn't include any read-replica instances, your DB cluster remains unavailable when the primary instance fails until it has been re-created. Re-creating the primary instance takes considerably longer than promoting a read-replica. To ensure high availability, we recommend that you create one or more read-replica instances that have the same DB instance class as the primary instance and are located in different AZs than the primary instance. ### Remediation To deploy a Neptune DB cluster in multiple AZs,, see [Read-replica DB instances in a Neptune DB cluster](../../../neptune/latest/userguide/feature-overview-db-clusters.md#feature-overview-read-replicas "../../../neptune/latest/userguide/feature-overview-db-clusters.md#feature-overview-read-replicas") in the _Neptune User Guide_. |
