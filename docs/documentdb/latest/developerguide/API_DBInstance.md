# DBInstance

Detailed information about an instance.

## Contents

###### Note

In the following list, the required parameters are described first.

**AutoMinorVersionUpgrade**

Does not apply. This parameter does not apply to Amazon DocumentDB. Amazon DocumentDB does not perform minor version upgrades regardless of the value set.

Type: Boolean

Required: No

**AvailabilityZone**

Specifies the name of the Availability Zone that the instance is located in.

Type: String

Required: No

**BackupRetentionPeriod**

Specifies the number of days for which automatic snapshots are retained.

Type: Integer

Required: No

**CACertificateIdentifier**

The identifier of the CA certificate for this DB instance.

Type: String

Required: No

**CertificateDetails**

The details of the DB instance's server certificate.

Type: [CertificateDetails](API_CertificateDetails.md "API_CertificateDetails.md") object

Required: No

**CopyTagsToSnapshot**

A value that indicates whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.

Type: Boolean

Required: No

**DBClusterIdentifier**

Contains the name of the cluster that the instance is a member of if the
instance is a member of a cluster.

Type: String

Required: No

**DBInstanceArn**

The Amazon Resource Name (ARN) for the instance.

Type: String

Required: No

**DBInstanceClass**

Contains the name of the compute and memory capacity class of the instance.

Type: String

Required: No

**DBInstanceIdentifier**

Contains a user-provided database identifier. This identifier is the unique key that
identifies an instance.

Type: String

Required: No

**DBInstanceStatus**

Specifies the current state of this database.

Type: String

Required: No

**DbiResourceId**

The AWS Region-unique, immutable identifier for the instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the instance is
accessed.

Type: String

Required: No

**DBSubnetGroup**

Specifies information on the subnet group that is associated with the instance, including the name, description, and subnets in the subnet group.

Type: [DBSubnetGroup](API_DBSubnetGroup.md "API_DBSubnetGroup.md") object

Required: No

**EnabledCloudwatchLogsExports.member.N**

A list of log types that this instance is configured to export to CloudWatch Logs.

Type: Array of strings

Required: No

**Endpoint**

Specifies the connection endpoint.

Type: [Endpoint](API_Endpoint.md "API_Endpoint.md") object

Required: No

**Engine**

Provides the name of the database engine to be used for this instance.

Type: String

Required: No

**EngineVersion**

Indicates the database engine version.

Type: String

Required: No

**InstanceCreateTime**

Provides the date and time that the instance was created.

Type: Timestamp

Required: No

**KmsKeyId**

If `StorageEncrypted` is `true`, the AWS KMS key identifier for
the encrypted instance.

Type: String

Required: No

**LatestRestorableTime**

Specifies the latest time to which a database can be restored with point-in-time
restore.

Type: Timestamp

Required: No

**PendingModifiedValues**

Specifies that changes to the instance are pending. This element is included only when changes are pending. Specific changes are identified by subelements.

Type: [PendingModifiedValues](API_PendingModifiedValues.md "API_PendingModifiedValues.md") object

Required: No

**PerformanceInsightsEnabled**

Set to `true` if Amazon RDS Performance Insights is enabled for the DB instance, and otherwise `false`.

Type: Boolean

Required: No

**PerformanceInsightsKMSKeyId**

The AWS KMS key identifier for encryption of Performance Insights data. The AWS KMS key ID is the Amazon Resource Name (ARN), AWS KMS key identifier, or the AWS KMS key alias for the AWS KMS encryption key.

Type: String

Required: No

**PreferredBackupWindow**

Specifies the daily time range during which automated backups are created if
automated backups are enabled, as determined by the `BackupRetentionPeriod`.

Type: String

Required: No

**PreferredMaintenanceWindow**

Specifies the weekly time range during which system maintenance can occur, in
Universal Coordinated Time (UTC).

Type: String

Required: No

**PromotionTier**

A value that specifies the order in which an Amazon DocumentDB replica is promoted to the
primary instance after a failure of the existing primary instance.

Type: Integer

Required: No

**PubliclyAccessible**

Not supported. Amazon DocumentDB does not currently support public endpoints. The value
of `PubliclyAccessible` is always `false`.

Type: Boolean

Required: No

**StatusInfos.DBInstanceStatusInfo.N**

The status of a read replica. If the instance is not a read replica, this is
blank.

Type: Array of [DBInstanceStatusInfo](API_DBInstanceStatusInfo.md "API_DBInstanceStatusInfo.md") objects

Required: No

**StorageEncrypted**

Specifies whether or not the instance is encrypted.

Type: Boolean

Required: No

**VpcSecurityGroups.VpcSecurityGroupMembership.N**

Provides a list of VPC security group elements that the instance belongs to.

Type: Array of [VpcSecurityGroupMembership](API_VpcSecurityGroupMembership.md "API_VpcSecurityGroupMembership.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DBInstance.md "../../../goto/SdkForCpp/docdb-2014-10-31/DBInstance.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DBInstance.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DBInstance.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DBInstance.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DBInstance.md")
