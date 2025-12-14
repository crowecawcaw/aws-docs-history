# Security Hub CSPM controls for Amazon RDS

These AWS Security Hub CSPM controls evaluate the Amazon Relational Database Service (Amazon RDS) and Amazon RDS resources. The controls
might not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [RDS.1] RDS snapshot should be private

**Related requirements:** PCI DSS v3.2.1/1.2.1, PCI DSS v3.2.1/1.3.1, PCI DSS v3.2.1/1.3.4, PCI DSS v3.2.1/1.3.6, PCI DSS v3.2.1/7.2.1, NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9)

**Category:** Protect > Secure network configuration

**Severity:** Critical

**Resource type:**
`AWS::RDS::DBClusterSnapshot`, `AWS::RDS::DBSnapshot`

**AWS Config rule:**
[`rds-snapshots-public-prohibited`](../../../config/latest/developerguide/rds-snapshots-public-prohibited.md "../../../config/latest/developerguide/rds-snapshots-public-prohibited.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether Amazon RDS snapshots are public.
The control fails if RDS snapshots are public. This control evaluates RDS instances,
Aurora DB instances, Neptune DB instances, and Amazon DocumentDB clusters.

RDS snapshots are used to back up the data on your RDS instances at a specific point in
time. They can be used to restore previous states of RDS instances.

An RDS snapshot must not be public unless intended. If you share an unencrypted manual
snapshot as public, this makes the snapshot available to all AWS accounts. This may result in
unintended data exposure of your RDS instance.

Note that if the configuration is changed to allow public access, the AWS Config rule may not be
able to detect the change for up to 12 hours. Until the AWS Config rule detects the change, the check
passes even though the configuration violates the rule.

To learn more about sharing a DB snapshot, see [Sharing a DB snapshot](../../../AmazonRDS/latest/UserGuide/USER_ShareSnapshot.md "../../../AmazonRDS/latest/UserGuide/USER_ShareSnapshot.md") in the
_Amazon RDS User Guide_.

### Remediation

To remove public access from RDS snapshots, see [Sharing a snapshot](../../../AmazonRDS/latest/UserGuide/USER_ShareSnapshot.md#USER_ShareSnapshot.Sharing "../../../AmazonRDS/latest/UserGuide/USER_ShareSnapshot.md#USER_ShareSnapshot.Sharing") in the _Amazon RDS User Guide_. For **DB snapshot visibility**, we
choose **Private**.

## [RDS.2] RDS DB Instances should prohibit public access, as determined by the PubliclyAccessible configuration

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/2.2.3, CIS AWS Foundations Benchmark v3.0.0/2.3.3, NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(5), PCI DSS v3.2.1/1.2.1, PCI DSS v3.2.1/1.3.1, PCI DSS v3.2.1/1.3.2, PCI DSS v3.2.1/1.3.4, PCI DSS v3.2.1/1.3.6, PCI DSS v3.2.1/7.2.1, PCI DSS v4.0.1/1.4.4

**Category:** Protect > Secure network configuration

**Severity:** Critical

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
[`rds-instance-public-access-check`](../../../config/latest/developerguide/rds-instance-public-access-check.md "../../../config/latest/developerguide/rds-instance-public-access-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether Amazon RDS instances are publicly accessible by evaluating the
`PubliclyAccessible` field in the instance configuration item.

Neptune DB instances and Amazon DocumentDB clusters do not have the `PubliclyAccessible`
flag and cannot be evaluated. However, this control can still generate findings for these
resources. You can suppress these findings.

The `PubliclyAccessible` value in the RDS instance configuration indicates
whether the DB instance is publicly accessible. When the DB instance is configured with
`PubliclyAccessible`, it is an Internet-facing instance with a publicly resolvable
DNS name, which resolves to a public IP address. When the DB instance isn't publicly accessible,
it is an internal instance with a DNS name that resolves to a private IP address.

Unless you intend for your RDS instance to be publicly accessible, the RDS instance should
not be configured with `PubliclyAccessible` value. Doing so might allow unnecessary
traffic to your database instance.

### Remediation

To remove public access from RDS DB instances, see [Modifying an Amazon RDS DB instance](../../../AmazonRDS/latest/UserGuide/Overview.DBInstance.md "../../../AmazonRDS/latest/UserGuide/Overview.DBInstance.md") in the _Amazon RDS User Guide_. For **Public access**,
choose **No**.

## [RDS.3] RDS DB instances should have encryption at-rest enabled

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/2.2.1, CIS AWS Foundations Benchmark v3.0.0/2.3.1, CIS AWS Foundations Benchmark v1.4.0/2.3.1, NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5 SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
[`rds-storage-encrypted`](../../../config/latest/developerguide/rds-storage-encrypted.md "../../../config/latest/developerguide/rds-storage-encrypted.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether storage encryption is enabled for your Amazon RDS DB
instances.

This control is intended for RDS DB instances. However, it can also generate findings for
Aurora DB instances, Neptune DB instances, and Amazon DocumentDB clusters. If these findings are not
useful, then you can suppress them.

For an added layer of security for your sensitive data in RDS DB instances, you should
configure your RDS DB instances to be encrypted at rest. To encrypt your RDS DB instances and
snapshots at rest, enable the encryption option for your RDS DB instances. Data that is
encrypted at rest includes the underlying storage for DB instances, its automated backups, read
replicas, and snapshots.

RDS encrypted DB instances use the open standard AES-256 encryption algorithm to encrypt
your data on the server that hosts your RDS DB instances. After your data is encrypted, Amazon RDS
handles authentication of access and decryption of your data transparently with a minimal impact
on performance. You do not need to modify your database client applications to use encryption.

Amazon RDS encryption is currently available for all database engines and storage types. Amazon RDS
encryption is available for most DB instance classes. To learn about DB instance classes that do
not support Amazon RDS encryption, see [Encrypting Amazon RDS resources](../../../AmazonRDS/latest/UserGuide/Overview.md "../../../AmazonRDS/latest/UserGuide/Overview.md") in
the _Amazon RDS User Guide_.

### Remediation

For information about encrypting DB instances in Amazon RDS, see [Encrypting Amazon RDS
resources](../../../AmazonRDS/latest/UserGuide/Overview.md "../../../AmazonRDS/latest/UserGuide/Overview.md") in the _Amazon RDS User Guide_.

## [RDS.4] RDS cluster snapshots and database snapshots should be encrypted at rest

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5 SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBClusterSnapshot`, `AWS::RDS::DBSnapshot`

**AWS Config rule:**
[`rds-snapshot-encrypted`](../../../config/latest/developerguide/rds-snapshot-encrypted.md "../../../config/latest/developerguide/rds-snapshot-encrypted.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an RDS DB snapshot is encrypted. The control fails if an RDS DB snapshot isn't encrypted.

This control is intended for RDS DB instances. However, it can also generate findings for
snapshots of Aurora DB instances, Neptune DB instances, and Amazon DocumentDB clusters. If these findings
are not useful, then you can suppress them.

Encrypting data at rest reduces the risk that an unauthenticated user gets access to data
that is stored on disk. Data in RDS snapshots should be encrypted at rest for an added layer of
security.

### Remediation

To encrypt an RDS snapshot, see [Encrypting Amazon RDS resources](../../../AmazonRDS/latest/UserGuide/Overview.md "../../../AmazonRDS/latest/UserGuide/Overview.md")
in the _Amazon RDS User Guide_. When you encrypt an RDS DB instance, the encrypted
data includes the underlying storage for the instance, its automated backups, read replicas, and snapshots.

You can only encrypt an RDS DB instance when you create it, not after the DB instance is created. However,
because you can encrypt a copy of an unencrypted snapshot, you can effectively add encryption to an unencrypted DB
instance. That is, you can create a snapshot of your DB instance, and then create an encrypted copy of that snapshot.
You can then restore a DB instance from the encrypted snapshot, and thus you have an encrypted copy of your original
DB instance.

## [RDS.5] RDS DB instances should be configured with multiple Availability Zones

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/2.2.4, NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6(2), NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
[`rds-multi-az-support`](../../../config/latest/developerguide/rds-multi-az-support.md "../../../config/latest/developerguide/rds-multi-az-support.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether high availability is enabled for your RDS DB instances. The
control fails if an RDS DB instance isn't configured with multiple Availability Zones
(AZs). This control doesn't apply to RDS DB instances that are part of a Multi-AZ DB
cluster deployment.

Configuring Amazon RDS DB instances with AZs helps ensure
the availability of stored data. Multi-AZ deployments allow for automated failover if there
is an issue with AZ availability and during regular RDS maintenance.

### Remediation

To deploy your DB instances in multiple AZs, [Modifying a DB instance to be a Multi-AZ DB instance deployment](../../../AmazonRDS/latest/UserGuide/Concepts.md#Concepts.MultiAZ.Migrating "../../../AmazonRDS/latest/UserGuide/Concepts.md#Concepts.MultiAZ.Migrating") in the
_Amazon RDS User Guide_.

## [RDS.6] Enhanced monitoring should be configured for RDS DB instances

**Related requirements:** NIST.800-53.r5 CA-7, NIST.800-53.r5 SI-2

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
[`rds-enhanced-monitoring-enabled`](../../../config/latest/developerguide/rds-enhanced-monitoring-enabled.md "../../../config/latest/developerguide/rds-enhanced-monitoring-enabled.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter            | Description                                                      | Type | Allowed custom values            | Security Hub CSPM default value |
| -------------------- | ---------------------------------------------------------------- | ---- | -------------------------------- | ------------------------------- |
| `monitoringInterval` | Number of seconds between monitoring metric collection intervals | Enum | `1`, `5`, `10`, `15`, `30`, `60` | No default value                |

This control checks whether enhanced monitoring is enabled for an Amazon Relational Database Service (Amazon RDS) DB
instance. The control fails if enhanced monitoring isn't enabled for the instance. If you provide a custom value for the
`monitoringInterval` parameter, the control passes only if enhanced monitoring metrics are collected for the instance
at the specified interval.

In Amazon RDS, Enhanced Monitoring enables a more rapid response to performance changes in
underlying infrastructure. These performance changes could result in a lack of availability of
the data. Enhanced Monitoring provides real-time metrics of the operating system that your RDS
DB instance runs on. An agent is installed on the instance. The agent can obtain metrics more
accurately than is possible from the hypervisor layer.

Enhanced Monitoring metrics are useful when you want to see how different processes or
threads on a DB instance use the CPU. For more information, see [Enhanced Monitoring](../../../AmazonRDS/latest/UserGuide/USER_Monitoring.md "../../../AmazonRDS/latest/UserGuide/USER_Monitoring.md") in the
_Amazon RDS User Guide_.

### Remediation

For detailed instructions on enabling Enhanced Monitoring for your DB instance, see
[Setting
up for and enabling Enhanced Monitoring](../../../AmazonRDS/latest/UserGuide/USER_Monitoring.OS.md "../../../AmazonRDS/latest/UserGuide/USER_Monitoring.OS.md") in the _Amazon RDS User Guide_.

## [RDS.7] RDS clusters should have deletion protection enabled

**Related requirements:** NIST.800-53.r5 CM-3, NIST.800-53.r5 SC-5(2)

**Category:** Protect > Data protection > Data deletion protection

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[`rds-cluster-deletion-protection-enabled`](../../../config/latest/developerguide/rds-cluster-deletion-protection-enabled.md "../../../config/latest/developerguide/rds-cluster-deletion-protection-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an RDS DB cluster has deletion protection enabled. The control fails if an RDS DB cluster
doesn't have deletion protection enabled.

This control is intended for RDS DB instances. However, it can also generate findings for
Aurora DB instances, Neptune DB instances, and Amazon DocumentDB clusters. If these findings are not
useful, then you can suppress them.

Enabling cluster deletion protection is an additional layer of protection against
accidental database deletion or deletion by an unauthorized entity.

When deletion protection is enabled, an RDS cluster cannot be deleted. Before a deletion
request can succeed, deletion protection must be disabled.

### Remediation

To enable deletion protection for an RDS DB cluster, see [Modifying
the DB cluster by using the console, CLI, and API](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md#Aurora.Modifying.Cluster "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md#Aurora.Modifying.Cluster") in the _Amazon RDS User Guide_. For
**Deletion protection**, choose **Enable deletion protection**.

## [RDS.8] RDS DB instances should have deletion protection enabled

**Related requirements:** NIST.800-53.r5 CM-3, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Protect > Data protection > Data deletion
protection

**Severity:** Low

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
[`rds-instance-deletion-protection-enabled`](../../../config/latest/developerguide/rds-instance-deletion-protection-enabled.md "../../../config/latest/developerguide/rds-instance-deletion-protection-enabled.md")

**Schedule type:** Change triggered

**Parameters:**

- `databaseEngines`:
  `mariadb,mysql,custom-oracle-ee,oracle-ee-cdb,oracle-se2-cdb,oracle-ee,oracle-se2,oracle-se1,oracle-se,postgres,sqlserver-ee,sqlserver-se,sqlserver-ex,sqlserver-web` (not customizable)

This control checks whether your RDS DB instances that use one of the listed database
engines have deletion protection enabled. The control fails if an RDS DB instance doesn't have deletion protection enabled.

Enabling instance deletion protection is an additional layer of protection against
accidental database deletion or deletion by an unauthorized entity.

While deletion protection is enabled, an RDS DB instance cannot be deleted. Before a
deletion request can succeed, deletion protection must be disabled.

### Remediation

To enable deletion protection for an RDS DB instance, see [Modifying
an Amazon RDS DB instance](../../../AmazonRDS/latest/UserGuide/Overview.DBInstance.md "../../../AmazonRDS/latest/UserGuide/Overview.DBInstance.md") in the _Amazon RDS User Guide_. For
**Deletion protection**, choose **Enable deletion protection**.

## [RDS.9] RDS DB instances should publish logs to CloudWatch Logs

**Related requirements:** NIST.800-53.r5 AC-2(4), NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AC-6(9), NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-3(8), NIST.800-53.r5 SI-4(20), NIST.800-53.r5 SI-7(8), PCI DSS v4.0.1/10.2.1

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
[`rds-logging-enabled`](../../../config/latest/developerguide/rds-logging-enabled.md "../../../config/latest/developerguide/rds-logging-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon RDS DB instance is configured to publish the following logs to Amazon CloudWatch Logs.
The control fails if the instance isn’t configured to publish the following logs to CloudWatch Logs:

- Oracle: Alert, Audit, Trace, Listener
- PostgreSQL: Postgresql, Upgrade
- MySQL: Audit, Error, General, SlowQuery
- MariaDB: Audit, Error, General, SlowQuery
- SQL Server: Error, Agent
- Aurora: Audit, Error, General, SlowQuery
- Aurora-MySQL: Audit, Error, General, SlowQuery
- Aurora-PostgreSQL: Postgresql

RDS databases should have relevant logs enabled. Database logging provides detailed records
of requests made to RDS. Database logs can assist with security and access audits and can help
to diagnose availability issues.

### Remediation

For information about publishing RDS database logs to CloudWatch Logs, see [Specifying the logs to publish to CloudWatch Logs](../../../AmazonRDS/latest/UserGuide/USER_LogAccess.Procedural.md#integrating_cloudwatchlogs.configure "../../../AmazonRDS/latest/UserGuide/USER_LogAccess.Procedural.md#integrating_cloudwatchlogs.configure") in the
_Amazon RDS User Guide_.

## [RDS.10] IAM authentication should be configured for RDS instances

**Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-6

**Category:** Protect > Secure access management >
Passwordless authentication

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
[`rds-instance-iam-authentication-enabled`](../../../config/latest/developerguide/rds-instance-iam-authentication-enabled.md "../../../config/latest/developerguide/rds-instance-iam-authentication-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an RDS DB instance has IAM database authentication
enabled. The control fails if IAM authentication is not configured for RDS DB instances.
This control only evaluates RDS instances with the following engine types: `mysql`,
`postgres`, `aurora`, `aurora-mysql`, `aurora-postgresql`, and `mariadb`.
An RDS instance must also be in one of the following states for a finding to be generated:
`available`, `backing-up`, `storage-optimization`, or `storage-full`.

IAM database authentication allows authentication to database instances with an
authentication token instead of a password. Network traffic to and from the database is
encrypted using SSL. For more information, see [IAM database
authentication](../../../AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.md") in the _Amazon Aurora User Guide_.

### Remediation

To activate IAM database authentication on an RDS DB instance, see [Enabling and disabling IAM database authentication](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.md") in the _Amazon RDS User Guide_.

## [RDS.11] RDS instances should have automatic backups enabled

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6, NIST.800-53.r5 CP-6(1), NIST.800-53.r5 CP-6(2), NIST.800-53.r5 CP-9, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-12, NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > Backups enabled

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
[`db-instance-backup-enabled`](../../../config/latest/developerguide/db-instance-backup-enabled.md "../../../config/latest/developerguide/db-instance-backup-enabled.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter                | Description                                                            | Type    | Allowed custom values | Security Hub CSPM default value |
| ------------------------ | ---------------------------------------------------------------------- | ------- | --------------------- | ------------------------------- |
| `backupRetentionMinimum` | Minimum backup retention period in days                                | Integer | `7` to `35`           | `7`                             |
| `checkReadReplicas`      | Checks whether RDS DB instances have backups enabled for read replicas | Boolean | Not customizable      | `false`                         |

This control checks whether an Amazon Relational Database Service instance has automated backups enabled, and a backup retention period greater
than or equal to the specified time frame. Read replicas are excluded from evaluation. The control fails if backups aren't enabled for the instance, or if the retention period is less than
the specified time frame. Unless you provide a custom parameter value for the backup retention period, Security Hub CSPM uses a default value
of 7 days.

Backups help you more quickly recover from a security incident and strengthens the resilience of your systems. Amazon RDS
lets you configure daily full instance volume snapshots. For more information about Amazon RDS automated backups, see
[Working with Backups](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md") in
the _Amazon RDS User Guide_.

### Remediation

To enable automated backups on an RDS DB instance, see [Enabling automated backups](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md#USER_WorkingWithAutomatedBackups.Enabling "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md#USER_WorkingWithAutomatedBackups.Enabling") in the _Amazon RDS User Guide_.

## [RDS.12] IAM authentication should be configured for RDS clusters

**Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-6

**Category:** Protect > Secure access management >
Passwordless authentication

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[`rds-cluster-iam-authentication-enabled`](../../../config/latest/developerguide/rds-cluster-iam-authentication-enabled.md "../../../config/latest/developerguide/rds-cluster-iam-authentication-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon RDS DB cluster has IAM database authentication
enabled.

IAM database authentication allows for password-free authentication to database
instances. The authentication uses an authentication token. Network traffic to and from the
database is encrypted using SSL. For more information, see [IAM database
authentication](../../../AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.md") in the _Amazon Aurora User Guide_.

### Remediation

To enable IAM authentication for a DB cluster, see [Enabling and disabling IAM database authentication](../../../AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.md "../../../AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.md") in the _Amazon Aurora User Guide_.

## [RDS.13] RDS automatic minor version upgrades should be enabled

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/2.2.2, CIS AWS Foundations Benchmark v3.0.0/2.3.2, NIST.800-53.r5 SI-2, NIST.800-53.r5 SI-2(2), NIST.800-53.r5 SI-2(4), NIST.800-53.r5 SI-2(5), PCI DSS v4.0.1/6.3.3

**Category:** Identify > Vulnerability, patch, and version management

**Severity:** High

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
[`rds-automatic-minor-version-upgrade-enabled`](../../../config/latest/developerguide/rds-automatic-minor-version-upgrade-enabled.md "../../../config/latest/developerguide/rds-automatic-minor-version-upgrade-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether automatic minor version upgrades are enabled for the RDS
database instance.

Automatic minor version upgrades periodically update a database to recent database engine
versions. However, the upgrade might not always include the latest database engine
version. If you need to keep your databases on specific versions at particular times, we
recommend that you manually upgrade to the database versions that you need according to
your required schedule. In cases of critical security issues or when a version reaches
its end-of-support date, Amazon RDS might apply a minor version upgrade even if you haven't
enabled the **Auto minor version upgrade** option. For more
information, see the Amazon RDS upgrade documentation for your specific database
engine:

- [Automatic minor version upgrades for RDS for MariaDB](../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MariaDB.md "../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MariaDB.md")
- [Automatic minor version upgrades for RDS for MySQL](../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MySQL.md "../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MySQL.md")
- [Automatic minor version upgrades for RDS for PostgreSQL](../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.md "../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.md")
- [Db2 on
  Amazon RDS versions](../../../AmazonRDS/latest/UserGuide/Db2.Concepts.md "../../../AmazonRDS/latest/UserGuide/Db2.Concepts.md")
- [Oracle minor version upgrades](../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Oracle.md "../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Oracle.md")
- [Upgrades of the Microsoft SQL Server DB engine](../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.md "../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.md")

### Remediation

To enable automatic minor version upgrades for an existing DB instance, see [Modifying an Amazon RDS DB instance](../../../AmazonRDS/latest/UserGuide/Overview.DBInstance.md "../../../AmazonRDS/latest/UserGuide/Overview.DBInstance.md") in the _Amazon RDS User Guide_.
For **Auto minor version upgrade**, select **Yes**.

## [RDS.14] Amazon Aurora clusters should have backtracking enabled

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6, NIST.800-53.r5 CP-6(1), NIST.800-53.r5 CP-6(2), NIST.800-53.r5 CP-9, NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > Backups enabled

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[`aurora-mysql-backtracking-enabled`](../../../config/latest/developerguide/aurora-mysql-backtracking-enabled.md "../../../config/latest/developerguide/aurora-mysql-backtracking-enabled.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter                | Description                                          | Type   | Allowed custom values | Security Hub CSPM default value |
| ------------------------ | ---------------------------------------------------- | ------ | --------------------- | ------------------------------- |
| `BacktrackWindowInHours` | Number of hours to backtrack an Aurora MySQL cluster | Double | `0.1` to `72`         | No default value                |

This control checks whether an Amazon Aurora cluster has backtracking enabled. The control fails if the cluster doesn't
have backtracking enabled. If you provide a custom value for the `BacktrackWindowInHours` parameter, the control passes
only if the cluster is backtracked for the specified length of time.

Backups help you to recover more quickly from a security incident. They also strengthens
the resilience of your systems. Aurora backtracking reduces the time to recover a database to a
point in time. It does not require a database restore to do so.

### Remediation

To enable Aurora backtracking, see [Configuring backtracking](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.md#AuroraMySQL.Managing.Backtrack.Configuring "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.md#AuroraMySQL.Managing.Backtrack.Configuring") in the _Amazon Aurora User Guide_.

Note that you cannot enable backtracking on an existing cluster. Instead, you can create a
clone that has backtracking enabled. For more information about the limitations of Aurora
backtracking, see the list of limitations in [Overview of
backtracking](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.md").

## [RDS.15] RDS DB clusters should be configured for multiple Availability Zones

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/2.2.4, NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6(2), NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[`rds-cluster-multi-az-enabled`](../../../config/latest/developerguide/rds-cluster-multi-az-enabled.md "../../../config/latest/developerguide/rds-cluster-multi-az-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether high availability is enabled for your RDS DB clusters. The control fails
if an RDS DB cluster isn't deployed in multiple Availability Zones (AZs).

RDS DB clusters should be configured for multiple AZs to ensure availability
of stored data. Deployment to multiple AZs allows for automated
failover in the event of an AZ availability issue and during regular RDS
maintenance events.

### Remediation

To deploy your DB clusters in multiple AZs, [Modifying a DB instance to be a Multi-AZ DB instance deployment](../../../AmazonRDS/latest/UserGuide/Concepts.md#Concepts.MultiAZ.Migrating "../../../AmazonRDS/latest/UserGuide/Concepts.md#Concepts.MultiAZ.Migrating") in the
_Amazon RDS User Guide_.

Remediation steps differ for Aurora global databases. To configure multiple Availability Zones for an Aurora global database,
select your DB cluster. Then, choose **Actions** and **Add reader**, and specify multiple AZs. For more information,
see [Adding Aurora Replicas to a DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/aurora-replicas-adding.md "../../../AmazonRDS/latest/AuroraUserGuide/aurora-replicas-adding.md") in the _Amazon Aurora User Guide_.

## [RDS.16] Aurora DB clusters should be configured to copy tags to DB

snapshots

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2)

**Category:** Identify > Inventory

**Severity:** Low

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
`rds-cluster-copy-tags-to-snapshots-enabled` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Aurora DB cluster is configured to automatically copy
tags to snapshots of the DB cluster when the snapshots are created. The control fails if
the Aurora DB cluster isn't configured to automatically copy tags to snapshots of the
cluster when the snapshots are created.

Identification and inventory of your IT assets is a crucial aspect of governance and
security. You need to have visibility of all your Amazon Aurora DB clusters so that you can
assess their security posture and take action on potential areas of weakness. Aurora DB
snapshots should have the same tags as their parent DB clusters. In Amazon Aurora, you can
configure a DB cluster to automatically copy all the tags for the cluster to snapshots
of the cluster. Enabling this setting ensures that DB snapshots inherit the same tags as
their parent DB clusters.

### Remediation

For information about configuring an Amazon Aurora DB cluster to automatically copy tags to
DB snapshots, see [Modifying an
Amazon Aurora DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md") in the _Amazon Aurora User
Guide_.

## [RDS.17] RDS DB instances should be configured to copy tags to snapshots

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2)

**Category:** Identify > Inventory

**Severity:** Low

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
`rds-instance-copy-tags-to-snapshots-enabled` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether RDS DB instances are configured to copy all tags to snapshots
when the snapshots are created.

Identification and inventory of your IT assets is a crucial aspect of governance and
security. You need to have visibility of all your RDS DB instances so that you can assess their
security posture and take action on potential areas of weakness. Snapshots should be tagged in
the same way as their parent RDS database instances. Enabling this setting ensures that
snapshots inherit the tags of their parent database instances.

### Remediation

To automatically copy tags to snapshots for an RDS DB instance, see [Modifying an Amazon RDS DB instance](../../../AmazonRDS/latest/UserGuide/Overview.DBInstance.md "../../../AmazonRDS/latest/UserGuide/Overview.DBInstance.md") in the _Amazon RDS User Guide_. Select **Copy tags to snapshots**.

## [RDS.18] RDS instances should be deployed in a VPC

**Category:** Protect > Secure network configuration >
Resources within VPC

**Severity:** High

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
`rds-deployed-in-vpc` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon RDS instance is deployed on an EC2-VPC.

VPCs provide a number of network controls to secure access to RDS resources. These controls
include VPC Endpoints, network ACLs, and security groups. To take advantage of these controls,
we recommend that you create your RDS instances on an EC2-VPC.

### Remediation

For instructions on moving RDS instances to a VPC, see [Updating
the VPC for a DB instance](../../../AmazonRDS/latest/UserGuide/USER_VPC.md "../../../AmazonRDS/latest/UserGuide/USER_VPC.md") in the _Amazon RDS User Guide_.

## [RDS.19] Existing RDS event notification subscriptions should be configured for critical cluster events

**Related requirements:** NIST.800-53.r5 CA-7, NIST.800-53.r5 SI-2

**Category:** Detect > Detection services > Application
monitoring

**Severity:** Low

**Resource type:**
`AWS::RDS::EventSubscription`

**AWS Config rule:**
`rds-cluster-event-notifications-configured` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an existing Amazon RDS event subscription for database clusters
has notifications enabled for the following source type and event category key-value pairs:

```
DBCluster: ["maintenance","failure"]
```

The control passes if there are no existing event subscriptions in your account.

RDS event notifications uses Amazon SNS to make you aware of changes in the availability or
configuration of your RDS resources. These notifications allow for rapid response. For
additional information about RDS event notifications, see [Using Amazon RDS event notification](../../../AmazonRDS/latest/UserGuide/USER_Events.md "../../../AmazonRDS/latest/UserGuide/USER_Events.md") in the
_Amazon RDS User Guide_.

### Remediation

To subscribe to RDS cluster event notifications, see [Subscribing to Amazon RDS event notification](../../../AmazonRDS/latest/UserGuide/USER_Events.md "../../../AmazonRDS/latest/UserGuide/USER_Events.md") in the _Amazon RDS User Guide_. Use the following values:

| Field                       | Value                                                    |
| --------------------------- | -------------------------------------------------------- |
| Source type                 | Clusters                                                 |
| Clusters to include         | All clusters                                             |
| Event categories to include | Select specific event categories or All event categories |

## [RDS.20] Existing RDS event notification subscriptions should be configured for critical database instance events

**Related requirements:** NIST.800-53.r5 CA-7, NIST.800-53.r5 SI-2, PCI DSS v4.0.1/11.5.2

**Category:** Detect > Detection services > Application
monitoring

**Severity:** Low

**Resource type:**
`AWS::RDS::EventSubscription`

**AWS Config rule:**
`rds-instance-event-notifications-configured` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an existing Amazon RDS event subscription for database instances has notifications enabled
for the following source type and event category key-value pairs:

```
DBInstance: ["maintenance","configuration change","failure"]
```

The control passes if there are no existing event subscriptions in your account.

RDS event notifications use Amazon SNS to make you aware of changes in the availability or
configuration of your RDS resources. These notifications allow for rapid response. For
additional information about RDS event notifications, see [Using Amazon RDS event notification](../../../AmazonRDS/latest/UserGuide/USER_Events.md "../../../AmazonRDS/latest/UserGuide/USER_Events.md") in the
_Amazon RDS User Guide_.

### Remediation

To subscribe to RDS instance event notifications, see [Subscribing to Amazon RDS event notification](../../../AmazonRDS/latest/UserGuide/USER_Events.md "../../../AmazonRDS/latest/UserGuide/USER_Events.md") in the _Amazon RDS User Guide_. Use the following values:

| Field                       | Value                                                    |
| --------------------------- | -------------------------------------------------------- |
| Source type                 | Instances                                                |
| Instances to include        | All instances                                            |
| Event categories to include | Select specific event categories or All event categories |

## [RDS.21] An RDS event notifications subscription should be configured for critical database parameter group events

**Related requirements:** NIST.800-53.r5 CA-7, NIST.800-53.r5 SI-2, PCI DSS v4.0.1/11.5.2

**Category:** Detect > Detection services > Application
monitoring

**Severity:** Low

**Resource type:**
`AWS::RDS::EventSubscription`

**AWS Config rule:**
`rds-pg-event-notifications-configured` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon RDS event subscription exists with notifications enabled
for the following source type, event category key-value pairs. The control passes if there are no existing event subscriptions in your account.

```
DBParameterGroup: ["configuration change"]
```

RDS event notifications use Amazon SNS to make you aware of changes in the availability or
configuration of your RDS resources. These notifications allow for rapid response. For
additional information about RDS event notifications, see [Using Amazon RDS event notification](../../../AmazonRDS/latest/UserGuide/USER_Events.md "../../../AmazonRDS/latest/UserGuide/USER_Events.md") in the
_Amazon RDS User Guide_.

### Remediation

To subscribe to RDS database parameter group event notifications, see [Subscribing to Amazon RDS event notification](../../../AmazonRDS/latest/UserGuide/USER_Events.md "../../../AmazonRDS/latest/UserGuide/USER_Events.md") in the _Amazon RDS User Guide_. Use the following values:

| Field                       | Value                                                    |
| --------------------------- | -------------------------------------------------------- |
| Source type                 | Parameter groups                                         |
| Parameter groups to include | All parameter groups                                     |
| Event categories to include | Select specific event categories or All event categories |

## [RDS.22] An RDS event notifications subscription should be configured for critical database security group events

**Related requirements:** NIST.800-53.r5 CA-7, NIST.800-53.r5 SI-2, PCI DSS v4.0.1/11.5.2

**Category:** Detect > Detection Services > Application
monitoring

**Severity:** Low

**Resource type:**
`AWS::RDS::EventSubscription`

**AWS Config rule:**
`rds-sg-event-notifications-configured` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon RDS event subscription exists with notifications enabled
for the following source type, event category key-value pairs. The control passes if there are no existing event subscriptions in your account.

```
DBSecurityGroup: ["configuration change","failure"]
```

RDS event notifications use Amazon SNS to make you aware of changes in the availability or
configuration of your RDS resources. These notifications allow for a rapid response. For
additional information about RDS event notifications, see [Using Amazon RDS event notification](../../../AmazonRDS/latest/UserGuide/USER_Events.md "../../../AmazonRDS/latest/UserGuide/USER_Events.md") in the
_Amazon RDS User Guide_.

### Remediation

To subscribe to RDS instance event notifications, see [Subscribing to Amazon RDS event notification](../../../AmazonRDS/latest/UserGuide/USER_Events.md "../../../AmazonRDS/latest/UserGuide/USER_Events.md") in the _Amazon RDS User Guide_. Use the following values:

| Field                       | Value                                                    |
| --------------------------- | -------------------------------------------------------- |
| Source type                 | Security groups                                          |
| Security groups to include  | All security groups                                      |
| Event categories to include | Select specific event categories or All event categories |

## [RDS.23] RDS instances should not use a database engine default port

**Related requirements:** NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(5)

**Category:** Protect > Secure network configuration

**Severity:** Low

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
`rds-no-default-ports` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an RDS cluster or instance uses a port other than the default
port of the database engine. The control fails if the RDS cluster or instance uses the default port.
This control doesn't apply to RDS instances that are part of a cluster.

If you use a known port to deploy an RDS cluster or instance, an attacker can guess
information about the cluster or instance. The attacker can use this information in conjunction
with other information to connect to an RDS cluster or instance or gain additional information
about your application.

When you change the port, you must also update the existing connection strings that were
used to connect to the old port. You should also check the security group of the DB instance to
ensure that it includes an ingress rule that allows connectivity on the new port.

### Remediation

To modify the default port of an existing RDS DB instance, see [Modifying an Amazon RDS DB instance](../../../AmazonRDS/latest/UserGuide/Overview.DBInstance.md "../../../AmazonRDS/latest/UserGuide/Overview.DBInstance.md") in the _Amazon RDS User Guide_. To modify the default port of an existing RDS DB cluster, see
[Modifying the DB cluster by using the console, CLI, and API](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md#Aurora.Modifying.Cluster "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md#Aurora.Modifying.Cluster") in the _Amazon Aurora User Guide_.
For **Database port**, change the port
value to a non-default value.

## [RDS.24] RDS Database clusters should use a custom administrator username

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, PCI DSS v4.0.1/2.2.2

**Category:** Identify > Resource Configuration

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
`rds-cluster-default-admin-check`

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon RDS database cluster has changed the admin username from its default value.
The control does not apply to engines of the type neptune (Neptune DB) or docdb (DocumentDB). This rule will fail if the
admin username is set to the default value.

When creating an Amazon RDS database, you should change the default admin username to a unique value. Default usernames are public knowledge and should be changed during RDS database creation. Changing the default usernames reduces the risk of unintended access.

### Remediation

For changing the admin username associated with the Amazon RDS database cluster, [create a new RDS database cluster](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md") and change the default admin username while creating the database.

## [RDS.25] RDS database instances should use a custom administrator username

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, PCI DSS v4.0.1/2.2.2

**Category:** Identify > Resource Configuration

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
`rds-instance-default-admin-check`

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether you've changed the administrative username for Amazon Relational Database Service (Amazon RDS) database instances from
the default value. The control
fails if the administrative username is set to the default value. The control doesn't apply to engines of the type neptune (Neptune DB) or docdb (DocumentDB), and to
RDS instances that are part of a cluster.

Default administrative usernames on Amazon RDS databases are public knowledge. When creating an
Amazon RDS database, you should change the default administrative username to a unique value to
reduce the risk of unintended access.

### Remediation

To change the administrative username associated with an RDS database instance, first
[create
a new RDS database instance](../../../AmazonRDS/latest/UserGuide/USER_CreateDBInstance.md "../../../AmazonRDS/latest/UserGuide/USER_CreateDBInstance.md"). Change the default administrative username while
creating the database.

## [RDS.26] RDS DB instances should be protected by a backup plan

**Category:** Recover > Resilience > Backups enabled

**Related requirements:**
NIST.800-53.r5 CP-10,
NIST.800-53.r5 CP-6,
NIST.800-53.r5 CP-6(1),
NIST.800-53.r5 CP-6(2),
NIST.800-53.r5 CP-9,
NIST.800-53.r5 SC-5(2),
NIST.800-53.r5 SI-12,
NIST.800-53.r5 SI-13(5)

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
[`rds-resources-protected-by-backup-plan`](../../../config/latest/developerguide/rds-resources-protected-by-backup-plan.md "../../../config/latest/developerguide/rds-resources-protected-by-backup-plan.md")

**Schedule type:** Periodic

**Parameters:**

| Parameter              | Description                                                                                                             | Type    | Allowed custom values | Security Hub CSPM default value |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------- | --------------------- | ------------------------------- |
| `backupVaultLockCheck` | The control produces a `PASSED` finding if the parameter is set to true and the resource<br>uses AWS Backup Vault Lock. | Boolean | `true` or `false`     | No default value                |

This control evaluates if Amazon RDS DB instances are covered by a backup plan. This control fails if the RDS DB instance isn't
covered by a backup plan. If you set the `backupVaultLockCheck`
parameter equal to `true`, the control passes only if the instance is backed up in an AWS Backup locked vault.

###### Note

This control doesn't evaluate Neptune and DocumentDB instances. It also doesn't evaluate RDS DB instances that are members
of a cluster.

AWS Backup is a fully managed backup service that centralizes and automates the backing up of data across AWS services.
With AWS Backup, you can create backup policies called backup plans. You can use these plans to define your backup requirements, such as
how frequently to back up your data and how long to retain those backups. Including RDS DB instances in a backup plan
helps you protect your data from unintended loss or deletion.

### Remediation

To add an RDS DB instance to an AWS Backup backup plan, see [Assigning resources to a backup plan](../../../aws-backup/latest/devguide/assigning-resources.md "../../../aws-backup/latest/devguide/assigning-resources.md") in the _AWS Backup Developer Guide_.

## [RDS.27] RDS DB clusters should be encrypted at rest

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5
SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[`rds-cluster-encrypted-at-rest`](../../../config/latest/developerguide/rds-cluster-encrypted-at-rest.md "../../../config/latest/developerguide/rds-cluster-encrypted-at-rest.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks if an RDS DB cluster is encrypted at rest. The control fails if an
RDS DB cluster isn't encrypted at rest.

Data at rest refers to any data that's stored in persistent, non-volatile storage for
any duration. Encryption helps you protect the confidentiality of such data, reducing
the risk that an unauthorized user can access it. Encrypting your RDS DB clusters
protects your data and metadata against unauthorized access. It also fulfills compliance
requirements for data-at-rest encryption of production file systems.

### Remediation

You can enable encryption at rest when you create an RDS DB cluster. You can't change encryption settings after creating a cluster. For more information, see [Encrypting an Amazon Aurora DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/Overview.md#Overview.Encryption.Enabling "../../../AmazonRDS/latest/AuroraUserGuide/Overview.md#Overview.Encryption.Enabling") in the
_Amazon Aurora User Guide_.

## [RDS.28] RDS DB clusters should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**`tagged-rds-dbcluster` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value                |

This control checks whether an Amazon RDS DB cluster has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the DB cluster doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the DB cluster isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
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

To add tags to an RDS DB cluster, see [Tagging Amazon RDS resources](../../../AmazonRDS/latest/UserGuide/USER_Tagging.md "../../../AmazonRDS/latest/UserGuide/USER_Tagging.md") in the _Amazon RDS User Guide_.

## [RDS.29] RDS DB cluster snapshots should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::RDS::DBClusterSnapshot`

**AWS Config rule:**`tagged-rds-dbclustersnapshot` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value                |

This control checks whether an Amazon RDS DB cluster snapshot has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the DB cluster snapshot doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the DB cluster snapshot isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
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

To add tags to an RDS DB cluster snapshot, see [Tagging Amazon RDS resources](../../../AmazonRDS/latest/UserGuide/USER_Tagging.md "../../../AmazonRDS/latest/UserGuide/USER_Tagging.md") in the _Amazon RDS User Guide_.

## [RDS.30] RDS DB instances should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**`tagged-rds-dbinstance` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value                |

This control checks whether an Amazon RDS DB instance has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the DB instance doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the DB instance isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
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

To add tags to an RDS DB instance, see [Tagging Amazon RDS resources](../../../AmazonRDS/latest/UserGuide/USER_Tagging.md "../../../AmazonRDS/latest/UserGuide/USER_Tagging.md") in the _Amazon RDS User Guide_.

## [RDS.31] RDS DB security groups should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::RDS::DBSecurityGroup`

**AWS Config rule:**`tagged-rds-dbsecuritygroup` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value                |

This control checks whether an Amazon RDS DB security group has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the DB security group doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the DB security group isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
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

To add tags to an RDS DB security group, see [Tagging Amazon RDS resources](../../../AmazonRDS/latest/UserGuide/USER_Tagging.md "../../../AmazonRDS/latest/UserGuide/USER_Tagging.md") in the _Amazon RDS User Guide_.

## [RDS.32] RDS DB snapshots should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::RDS::DBSnapshot`

**AWS Config rule:**`tagged-rds-dbsnapshot` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value                |

This control checks whether an Amazon RDS DB snapshot has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the DB snapshot doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the DB snapshot isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
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

To add tags to an RDS DB snapshot, see [Tagging Amazon RDS resources](../../../AmazonRDS/latest/UserGuide/USER_Tagging.md "../../../AmazonRDS/latest/UserGuide/USER_Tagging.md") in the _Amazon RDS User Guide_.

## [RDS.33] RDS DB subnet groups should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::RDS::DBSubnetGroup`

**AWS Config rule:**`tagged-rds-dbsubnetgroups` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value                |

This control checks whether an Amazon RDS DB subnet group has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the DB subnet group doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the DB subnet group isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
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

To add tags to an RDS DB subnet group, see [Tagging Amazon RDS resources](../../../AmazonRDS/latest/UserGuide/USER_Tagging.md "../../../AmazonRDS/latest/UserGuide/USER_Tagging.md") in the _Amazon RDS User Guide_.

## [RDS.34] Aurora MySQL DB clusters should publish audit logs to CloudWatch Logs

**Related requirements:** NIST.800-53.r5 AC-2(4),
NIST.800-53.r5 AC-4(26),
NIST.800-53.r5 AC-6(9),
NIST.800-53.r5 AU-10,
NIST.800-53.r5 AU-12,
NIST.800-53.r5 AU-2,
NIST.800-53.r5 AU-3,
NIST.800-53.r5 AU-6(3),
NIST.800-53.r5 AU-6(4),
NIST.800-53.r5 CA-7,
NIST.800-53.r5 SC-7(9),
NIST.800-53.r5 SI-3(8),
NIST.800-53.r5 SI-4(20),
NIST.800-53.r5 SI-7(8), PCI DSS v4.0.1/10.2.1

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[`rds-aurora-mysql-audit-logging-enabled`](../../../config/latest/developerguide/rds-aurora-mysql-audit-logging-enabled.md "../../../config/latest/developerguide/rds-aurora-mysql-audit-logging-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Aurora MySQL DB cluster is configured to publish audit logs to Amazon CloudWatch Logs. The
control fails if the cluster isn't configured to publish audit logs to CloudWatch Logs. The control doesn't generate
findings for Aurora Serverless v1 DB clusters.

Audit logs capture a record of database activity, including login attempts, data modifications, schema changes, and
other events that can be audited for security and compliance purposes. When you configure an Aurora MySQL DB cluster to publish
audit logs to a log group in Amazon CloudWatch Logs, you can perform real-time analysis of the log data. CloudWatch Logs retains logs in highly durable
storage. You can also create alarms and view metrics in CloudWatch.

###### Note

An alternative way to publish audit logs to CloudWatch Logs is by enabling advanced auditing and setting the cluster-level DB
parameter `server_audit_logs_upload` to `1`. The default for the `server_audit_logs_upload parameter`
is `0`. However, we recommend you use the following remediation instructions instead to pass this control.

### Remediation

To publish Aurora MySQL DB cluster audit logs to CloudWatch Logs, see [Publishing Amazon Aurora MySQL logs to Amazon CloudWatch Logs](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md") in the
_Amazon Aurora User Guide_.

## [RDS.35] RDS DB clusters should have automatic minor version upgrade enabled

**Related requirements:** NIST.800-53.r5 SI-2,
NIST.800-53.r5 SI-2(2),
NIST.800-53.r5 SI-2(4),
NIST.800-53.r5 SI-2(5), PCI DSS v4.0.1/6.3.3

**Category:** Identify > Vulnerability, patch, and version management

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[`rds-cluster-auto-minor-version-upgrade-enable`](../../../config/latest/developerguide/rds-cluster-auto-minor-version-upgrade-enable.md "../../../config/latest/developerguide/rds-cluster-auto-minor-version-upgrade-enable.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks if automatic minor version upgrade is enabled for an Amazon RDS Multi-AZ DB cluster. The control fails
if automatic minor version upgrade isn't enabled for the Multi-AZ DB cluster.

RDS provides automatic minor version upgrade so that you can keep your Multi-AZ DB cluster up to date. Minor
versions can introduce new software features, bug fixes, security patches, and performance improvements. By enabling automatic
minor version upgrade on RDS database clusters, the cluster, along with the instances in the cluster, will receive automatic
updates to the minor version when new versions are available. The updates are applied automatically during the maintenance window.

### Remediation

To enable automatic minor version upgrade on Multi-AZ DB clusters, see [Modifying a Multi-AZ DB cluster](../../../AmazonRDS/latest/UserGuide/modify-multi-az-db-cluster.md "../../../AmazonRDS/latest/UserGuide/modify-multi-az-db-cluster.md") in the
_Amazon RDS User Guide_.

## [RDS.36] RDS for PostgreSQL DB instances should publish logs to CloudWatch Logs

**Related requirements:** PCI DSS v4.0.1/10.4.2

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
[rds-postgresql-logs-to-cloudwatch](../../../config/latest/developerguide/rds-postgresql-logs-to-cloudwatch.md "../../../config/latest/developerguide/rds-postgresql-logs-to-cloudwatch.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter  | Description                                                          | Type       | Allowed custom values | Security Hub CSPM default value |
| ---------- | -------------------------------------------------------------------- | ---------- | --------------------- | ------------------------------- |
| `logTypes` | Comma-separated list of log types to be published to CloudWatch Logs | StringList | Not customizable      | `postgresql`                    |

This control checks whether an Amazon RDS for PostgreSQL DB instance is configured to publish logs to Amazon CloudWatch Logs. The
control fails if the PostgreSQL DB instance isn't configured to publish the log types mentioned in the `logTypes`
parameter to CloudWatch Logs.

Database logging provides detailed records of requests made to an RDS instance. PostgreSQL generates event logs that
contain useful information for administrators. Publishing these logs to CloudWatch Logs centralizes log management and helps you perform
real-time analysis of the log data. CloudWatch Logs retains logs in highly durable storage. You can also create alarms and view metrics in
CloudWatch.

### Remediation

To publish PostgreSQL DB instance logs to CloudWatch Logs, see [Publishing PostgreSQL logs to Amazon CloudWatch Logs](../../../AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.md#USER_LogAccess.Concepts.PostgreSQL.PublishtoCloudWatchLogs "../../../AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.md#USER_LogAccess.Concepts.PostgreSQL.PublishtoCloudWatchLogs") in the
_Amazon RDS User Guide_.

## [RDS.37] Aurora PostgreSQL DB clusters should publish logs to CloudWatch Logs

**Related requirements:** PCI DSS v4.0.1/10.4.2

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[rds-aurora-postgresql-logs-to-cloudwatch](../../../config/latest/developerguide/rds-aurora-postgresql-logs-to-cloudwatch.md "../../../config/latest/developerguide/rds-aurora-postgresql-logs-to-cloudwatch.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Aurora PostgreSQL DB cluster is configured to publish logs to Amazon CloudWatch Logs. The
control fails if the Aurora PostgreSQL DB cluster isn't configured to publish PostgreSQL logs to CloudWatch Logs.

Database logging provides detailed records of requests made to an RDS cluster. Aurora PostgreSQL generates event
logs that contain useful information for administrators. Publishing these logs to CloudWatch Logs centralizes log management and
helps you perform real-time analysis of the log data. CloudWatch Logs retains logs in highly durable storage. You can also create
alarms and view metrics in CloudWatch.

### Remediation

To publish Aurora PostgreSQL DB cluster logs to CloudWatch Logs, see [Publishing Aurora PostgreSQL logs to Amazon CloudWatch Logs](../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.md") in the
_Amazon RDS User Guide_.

## [RDS.38] RDS for PostgreSQL DB instances should be encrypted in transit

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
[rds-postgres-instance-encrypted-in-transit](../../../config/latest/developerguide/rds-postgres-instance-encrypted-in-transit.md "../../../config/latest/developerguide/rds-postgres-instance-encrypted-in-transit.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether a connection to an Amazon RDS for PostgreSQL database (DB) instance is encrypted in transit. The control fails if the `rds.force_ssl`
parameter for the parameter group associated with the instance is set to `0` (off). This control doesn't evaluate RDS DB instances that are part of a DB cluster.

Data in transit refers to data that moves from one location to another, such as between nodes in your cluster or between your cluster and your application. Data may move across the internet or within a private network. Encrypting data in transit reduces the risk that an unauthorized user can eavesdrop on network traffic.

### Remediation

To require all connections to your RDS for PostgreSQL DB instance to use SSL, see [Using SSL with a PostgreSQL DB instance](../../../AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.md "../../../AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.md")
in the _Amazon RDS User Guide_.

## [RDS.39] RDS for MySQL DB instances should be encrypted in transit

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
[rds-mysql-instance-encrypted-in-transit](../../../config/latest/developerguide/rds-mysql-instance-encrypted-in-transit.md "../../../config/latest/developerguide/rds-mysql-instance-encrypted-in-transit.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether a connection to an Amazon RDS for MySQL database (DB) instance is encrypted in transit. The control fails if the `rds.require_secure_transport`
parameter for the parameter group associated with the instance is set to `0` (off). This control doesn't evaluate RDS DB instances that are part of a DB cluster.

Data in transit refers to data that moves from one location to another, such as between nodes in your cluster or between your cluster and your application. Data may move across the internet or within a private network. Encrypting data in transit reduces the risk that an unauthorized user can eavesdrop on network traffic.

### Remediation

To require all connections to your RDS for MySQL DB instance to use SSL, see [SSL/TLS support for MySQL DB instances on Amazon RDS](../../../AmazonRDS/latest/UserGuide/MySQL.Concepts.md "../../../AmazonRDS/latest/UserGuide/MySQL.Concepts.md")
in the _Amazon RDS User Guide_.

## [RDS.40] RDS for SQL Server DB instances should publish logs to CloudWatch Logs

**Related requirements:** NIST.800-53.r5 AC-2(4),
NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AC-6(9), NIST.800-53.r5 AU-10, NIST.800-53.r5
AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5
AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SC-7(9),
NIST.800-53.r5 SI-3(8), NIST.800-53.r5 SI-4(20), NIST.800-53.r5 SI-7(8)

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
[rds-sql-server-logs-to-cloudwatch](../../../config/latest/developerguide/rds-sql-server-logs-to-cloudwatch.md "../../../config/latest/developerguide/rds-sql-server-logs-to-cloudwatch.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter  | Description                                                                                                                                                                                                                          | Type                          | Allowed custom values | Security Hub CSPM default value |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- | --------------------- | ------------------------------- |
| `logTypes` | A list of the types of logs that an RDS for SQL Server DB instance should be<br>configured to publish to CloudWatch Logs. This control fails if a DB instance<br>isn't configured to publish a type of log specified in the<br>list. | EnumList (maximum of 2 items) | `agent`, `error`      | `agent`, `error`                |

This control checks whether an Amazon RDS for Microsoft SQL Server DB instance is configured to publish
logs to Amazon CloudWatch Logs. The control fails if the RDS for SQL Server DB instance isn't configured to
publish logs to CloudWatch Logs. You can optionally specify the types of logs that a DB instance
should be configured to publish.

Database logging provides detailed records of requests made to an Amazon RDS DB instance.
Publishing logs to CloudWatch Logs centralizes log management and helps you perform real-time
analysis of log data. CloudWatch Logs retains logs in highly durable storage. In addition, you can
use it to create alarms for specific errors that can occur, such as frequent restarts
that are recorded in an error log. Similarly, you can create alarms for errors or
warnings that are recorded in SQL Server agent logs related to SQL agent jobs.

### Remediation

For information about publishing logs to CloudWatch Logs for an RDS for SQL Server DB instance, see
[Amazon RDS for Microsoft SQL Server database log files](../../../AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.md "../../../AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.md") in the _Amazon Relational Database Service User Guide_.

## [RDS.41] RDS for SQL Server DB instances should be encrypted in transit

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
[rds-sqlserver-encrypted-in-transit](../../../config/latest/developerguide/rds-sqlserver-encrypted-in-transit.md "../../../config/latest/developerguide/rds-sqlserver-encrypted-in-transit.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether a connection to an Amazon RDS for Microsoft SQL Server DB instance is
encrypted in transit. The control fails if the `rds.force_ssl` parameter of
the parameter group associated with the DB instance is set to `0
 (off)`.

Data in transit refers to data that moves from one location to another, such as
between nodes in a DB cluster or between a DB cluster and a client application. Data can
move across the internet or within a private network. Encrypting data in transit reduces
the risk of unauthorized users eavesdropping on network traffic.

### Remediation

For information about enabling SSL/TLS for connections to Amazon RDS DB instances
running Microsoft SQL Server, see [Using
SSL with a Microsoft SQL Server DB Instance](../../../AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.SSL.md "../../../AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.SSL.md") in the _Amazon Relational Database Service User Guide_.

## [RDS.42] RDS for MariaDB DB instances should publish logs to CloudWatch Logs

**Related requirements:** NIST.800-53.r5 AC-2(4),
NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AC-6(9), NIST.800-53.r5 AU-2, NIST.800-53.r5
AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 AU-10,
NIST.800-53.r5 AU-12, NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9), NIST.800-53.r5
SC-7(10), NIST.800-53.r5 SI-3(8), NIST.800-53.r5 SI-4(20), NIST.800-53.r5 SI-7(8)

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
[mariadb-publish-logs-to-cloudwatch-logs](../../../config/latest/developerguide/mariadb-publish-logs-to-cloudwatch-logs.md "../../../config/latest/developerguide/mariadb-publish-logs-to-cloudwatch-logs.md")

**Schedule type:** Periodic

**Parameters:**

| Parameter  | Description                                                                                                                                                                                                                                 | Type                          | Allowed custom values                       | Security Hub CSPM default value |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------- | ------------------------------- |
| `logTypes` | A list of the types of logs that a MariaDB DB instance should be<br>configured to publish to CloudWatch Logs. The control generates a<br>`FAILED` finding if a DB instance isn't configured to<br>publish a log type specified in the list. | EnumList (maximum of 4 items) | `audit`, `error`, `general`,<br>`slowquery` | `audit, error`                  |

This control checks whether an Amazon RDS for MariaDB DB instance is configured to publish
certain types of logs to Amazon CloudWatch Logs. The control fails if the MariaDB DB instance isn't
configured to publish the logs to CloudWatch Logs. You can optionally specify which types of logs
a MariaDB DB instance should be configured to publish.

Database logging provides detailed records of requests made to an Amazon RDS for MariaDB DB
instance. Publishing logs to Amazon CloudWatch Logs centralizes log management and helps you perform
real-time analysis of the log data. In addition, CloudWatch Logs retains the logs in durable
storage, which can support security, access, and availability reviews and audits. With
CloudWatch Logs, you can also create alarms and review metrics.

### Remediation

For information about configuring an Amazon RDS for MariaDB DB instance to publish logs to
Amazon CloudWatch Logs, see [Publishing MariaDB logs to Amazon CloudWatch Logs](../../../AmazonRDS/latest/UserGuide/USER_LogAccess.MariaDB.md "../../../AmazonRDS/latest/UserGuide/USER_LogAccess.MariaDB.md") in the _Amazon Relational Database Service User Guide_.

## [RDS.43] RDS DB proxies should require TLS encryption for

connections

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBProxy`

**AWS Config rule:**
[rds-proxy-tls-encryption](../../../config/latest/developerguide/rds-proxy-tls-encryption.md "../../../config/latest/developerguide/rds-proxy-tls-encryption.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an Amazon RDS DB proxy requires TLS for all connections between
the proxy and the underlying RDS DB instance. The control fails if the proxy doesn't
require TLS for all connections between the proxy and the RDS DB instance.

Amazon RDS Proxy can act as an additional layer of security between client applications and
underlying RDS DB instances. For example, you can connect to an RDS proxy using TLS 1.3,
even if the underlying DB instance supports an older version of TLS. By using RDS Proxy,
you can enforce strong authentication requirements for database applications.

### Remediation

For information about changing the settings for an Amazon RDS proxy to require TLS, see
[Modifying
an RDS proxy](../../../AmazonRDS/latest/UserGuide/rds-proxy-modifying-proxy.md "../../../AmazonRDS/latest/UserGuide/rds-proxy-modifying-proxy.md") in the _Amazon Relational Database Service User
Guide_.

## [RDS.44] RDS for MariaDB DB instances should be encrypted in transit

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
[rds-mariadb-instance-encrypted-in-transit](../../../config/latest/developerguide/rds-mariadb-instance-encrypted-in-transit.md "../../../config/latest/developerguide/rds-mariadb-instance-encrypted-in-transit.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether connections to an Amazon RDS for MariaDB DB instance are encrypted
in transit. The control fails if the DB parameter group associated with the DB instance
is not in sync, or the `require_secure_transport` parameter of the parameter
group is not set to `ON`.

###### Note

This control doesn't evaluate Amazon RDS DB instances that use MariaDB versions earlier
than version 10.5. The `require_secure_transport` parameter is supported
only for MariaDB versions 10.5 and later.

Data in transit refers to data that moves from one location to another, such as
between nodes in a DB cluster or between a DB cluster and a client application. Data can
move across the internet or within a private network. Encrypting data in transit reduces
the risk of unauthorized users eavesdropping on network traffic.

### Remediation

For information about enabling SSL/TLS for connections to an Amazon RDS for MariaDB DB
instance, see [Requiring SSL/TLS for all connections to a MariaDB DB instance](../../../AmazonRDS/latest/UserGuide/mariadb-ssl-connections.md "../../../AmazonRDS/latest/UserGuide/mariadb-ssl-connections.md") in the
_Amazon Relational Database Service User Guide_.

## [RDS.45] Aurora MySQL DB clusters should have audit logging enabled

**Related requirements:** NIST.800-53.r5 AC-2(4),
NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AC-6(9), NIST.800-53.r5 AU-2, NIST.800-53.r5
AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 AU-10,
NIST.800-53.r5 AU-12, NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9), NIST.800-53.r5
SI-3(8), NIST.800-53.r5 SI-4(20), NIST.800-53.r5 SI-7(8)

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[aurora-mysql-cluster-audit-logging](../../../config/latest/developerguide/aurora-mysql-cluster-audit-logging.md "../../../config/latest/developerguide/aurora-mysql-cluster-audit-logging.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an Amazon Aurora MySQL DB cluster has audit logging enabled.
The control fails if the DB parameter group associated with the DB cluster is not in
sync, the `server_audit_logging` parameter is not set to `1`, or
the `server_audit_events` parameter is set to an empty value.

Database logs can assist with security and access audits and help diagnose
availability issues. Audit logs capture a record of database activity, including login
attempts, data modifications, schema changes, and other events that can be audited for
security and compliance purposes.

### Remediation

For information about enabling logging for an Amazon Aurora MySQL DB cluster, see
[Publishing Amazon Aurora MySQL logs to Amazon CloudWatch Logs](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md") in the _Amazon Aurora User Guide_.

## [RDS.46] RDS DB instances should not be deployed in public subnets with routes to internet gateways

**Category:** Protect > Secure network configuration > Resources not publicly accessible

**Severity:** High

**Resource type:**
`AWS::RDS::DBInstance`

**AWS Config rule:**
[rds-instance-subnet-igw-check](../../../config/latest/developerguide/rds-instance-subnet-igw-check.md "../../../config/latest/developerguide/rds-instance-subnet-igw-check.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an Amazon RDS DB instance is deployed in a public subnet that
has a route to an internet gateway. The control fails if the RDS DB instance is deployed
in a subnet that has a route to an internet gateway and the destination is set to
`0.0.0.0/0` or `::/0`.

By provisioning your Amazon RDS resources in private subnets, you can prevent your RDS
resources from receiving inbound traffic from the public internet, which can prevent
unintended access to your RDS DB instances. If RDS resources are provisioned in a public
subnet that is open to the internet, they might be vulnerable to risks such as data
exfiltration.

### Remediation

For information about provisioning a private subnet for an Amazon RDS DB instance, see
[Working with a DB instance in a VPC](../../../AmazonRDS/latest/UserGuide/USER_VPC.md "../../../AmazonRDS/latest/UserGuide/USER_VPC.md") in the _Amazon Relational Database Service User Guide_.

## [RDS.47] RDS for PostgreSQL DB clusters should be configured to copy tags to DB

snapshots

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[rds-pgsql-cluster-copy-tags-to-snapshot-check](../../../config/latest/developerguide/rds-pgsql-cluster-copy-tags-to-snapshot-check.md "../../../config/latest/developerguide/rds-pgsql-cluster-copy-tags-to-snapshot-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon RDS for PostgreSQL DB cluster is configured to
automatically copy tags to snapshots of the DB cluster when the snapshots are created.
The control fails if the `CopyTagsToSnapshot` parameter is set to
`false` for the RDS for PostgreSQL DB cluster.

Copying tags to DB snapshots helps maintain proper resource tracking, governance, and
cost allocation across backup resources. This enables consistent resource
identification, access control, and compliance monitoring across both active databases
and their snapshots. Properly tagged snapshots improve security operations by ensuring
backup resources inherit the same metadata as their source databases.

### Remediation

For information about configuring an Amazon RDS for PostgreSQL DB cluster to automatically
copy tags to DB snapshots, see [Tagging
Amazon RDS resources](../../../AmazonRDS/latest/UserGuide/USER_Tagging.md "../../../AmazonRDS/latest/UserGuide/USER_Tagging.md") in the _Amazon Relational Database Service User
Guide_.

## [RDS.48] RDS for MySQL DB clusters should be configured to copy tags to DB

snapshots

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::RDS::DBCluster`

**AWS Config rule:**
[rds-mysql-cluster-copy-tags-to-snapshot-check](../../../config/latest/developerguide/rds-mysql-cluster-copy-tags-to-snapshot-check.md "../../../config/latest/developerguide/rds-mysql-cluster-copy-tags-to-snapshot-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon RDS for MySQL DB cluster is configured to
automatically copy tags to snapshots of the DB cluster when the snapshots are created.
The control fails if the `CopyTagsToSnapshot` parameter is set to
`false` for the RDS for MySQL DB cluster.

Copying tags to DB snapshots helps maintain proper resource tracking, governance, and
cost allocation across backup resources. This enables consistent resource
identification, access control, and compliance monitoring across both active databases
and their snapshots. Properly tagged snapshots improve security operations by ensuring
backup resources inherit the same metadata as their source databases.

### Remediation

For information about configuring an Amazon RDS for MySQL DB cluster to automatically
copy tags to DB snapshots, see [Tagging Amazon RDS
resources](../../../AmazonRDS/latest/UserGuide/USER_Tagging.md "../../../AmazonRDS/latest/UserGuide/USER_Tagging.md") in the _Amazon Relational Database Service User
Guide_.
