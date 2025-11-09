# Neptune Instances API

**Actions:**

- [CreateDBInstance (action)](#CreateDBInstance "#CreateDBInstance")
- [DeleteDBInstance (action)](#DeleteDBInstance "#DeleteDBInstance")
- [ModifyDBInstance (action)](#ModifyDBInstance "#ModifyDBInstance")
- [RebootDBInstance (action)](#RebootDBInstance "#RebootDBInstance")
- [DescribeDBInstances (action)](#DescribeDBInstances "#DescribeDBInstances")
- [DescribeOrderableDBInstanceOptions (action)](#DescribeOrderableDBInstanceOptions "#DescribeOrderableDBInstanceOptions")
- [DescribeValidDBInstanceModifications (action)](#DescribeValidDBInstanceModifications "#DescribeValidDBInstanceModifications")
  **Structures:**

- [DBInstance (structure)](#DBInstance "#DBInstance")
- [DBInstanceStatusInfo (structure)](#DBInstanceStatusInfo "#DBInstanceStatusInfo")
- [OrderableDBInstanceOption (structure)](#OrderableDBInstanceOption "#OrderableDBInstanceOption")
- [PendingModifiedValues (structure)](#PendingModifiedValues "#PendingModifiedValues")
- [ValidStorageOptions (structure)](#ValidStorageOptions "#ValidStorageOptions")
- [ValidDBInstanceModificationsMessage (structure)](#ValidDBInstanceModificationsMessage "#ValidDBInstanceModificationsMessage")

## CreateDBInstance (action)

        The AWS CLI name for this API is: `create-db-instance`.

Creates a new DB instance.

**Request**

- **AutoMinorVersionUpgrade**  (in the CLI: `--auto-minor-version-upgrade`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Indicates that minor engine upgrades are applied automatically to the
DB instance during the maintenance window.

Default: `true`

- **AvailabilityZone**  (in the CLI: `--availability-zone`) –  a String, of type: `string` (a UTF-8 encoded string).

The EC2 Availability Zone that the DB instance is created in

Default: A random, system-chosen Availability Zone in the endpoint's
Amazon Region.

Example: `us-east-1d`

Constraint: The AvailabilityZone parameter can't be specified if the
MultiAZ parameter is set to `true`. The specified Availability
Zone must be in the same Amazon Region as the current endpoint.

- **BackupRetentionPeriod**  (in the CLI: `--backup-retention-period`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The number of days for which automated backups are retained.

Not applicable. The retention period for automated backups is managed
by the DB cluster. For more information, see [CreateDBCluster (action)](api-clusters.md#CreateDBCluster "api-clusters.md#CreateDBCluster").

Default: 1

Constraints:

    + Must be a value from 0 to 35
    + Cannot be set to 0 if the DB instance is a source to Read Replicas

- **CopyTagsToSnapshot**  (in the CLI: `--copy-tags-to-snapshot`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

True to copy all tags from the DB instance to snapshots of the DB instance,
and otherwise false. The default is false.

- **DBClusterIdentifier**  (in the CLI: `--db-cluster-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The identifier of the DB cluster that the instance will belong to.

For information on creating a DB cluster, see [CreateDBCluster (action)](api-clusters.md#CreateDBCluster "api-clusters.md#CreateDBCluster").

Type: String

- **DBInstanceClass**  (in the CLI: `--db-instance-class`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The compute and memory capacity of the DB instance, for example, `db.m4.large`.
Not all DB instance classes are available in all Amazon Regions.

- **DBInstanceIdentifier**  (in the CLI: `--db-instance-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The DB instance identifier. This parameter is stored as a lowercase string.

Constraints:

    + Must contain from 1 to 63 letters, numbers, or hyphens.
    + First character must be a letter.
    + Cannot end with a hyphen or contain two consecutive hyphens.

Example: `mydbinstance`

- **DBName**  (in the CLI: `--db-name`) –  a String, of type: `string` (a UTF-8 encoded string).

Not supported.

- **DBParameterGroupName**  (in the CLI: `--db-parameter-group-name`) –  a String, of type: `string` (a UTF-8 encoded string).

The name of the DB parameter group to associate with this DB instance. If
this argument is omitted, the default DBParameterGroup for the specified engine
is used.

Constraints:

    + Must be 1 to 255 letters, numbers, or hyphens.
    + First character must be a letter
    + Cannot end with a hyphen or contain two consecutive hyphens

- **DBSecurityGroups**  (in the CLI: `--db-security-groups`) –  a String, of type: `string` (a UTF-8 encoded string).

A list of DB security groups to associate with this DB instance.

Default: The default DB security group for the database engine.

- **DBSubnetGroupName**  (in the CLI: `--db-subnet-group-name`) –  a String, of type: `string` (a UTF-8 encoded string).

A DB subnet group to associate with this DB instance.

If there is no DB subnet group, then it is a non-VPC DB instance.

- **DeletionProtection**  (in the CLI: `--deletion-protection`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

A value that indicates whether the DB instance has deletion protection
enabled. The database can't be deleted when deletion protection is enabled.
By default, deletion protection is disabled. See [Deleting
a DB Instance](manage-console-instances-delete.md "manage-console-instances-delete.md").

DB instances in a DB cluster can be deleted even when deletion protection
is enabled in their parent DB cluster.

- **Domain**  (in the CLI: `--domain`) –  a String, of type: `string` (a UTF-8 encoded string).

Specify the Active Directory Domain to create the instance in.

- **DomainIAMRoleName**  (in the CLI: `--domain-iam-role-name`) –  a String, of type: `string` (a UTF-8 encoded string).

Specify the name of the IAM role to be used when making API calls to the Directory
Service.

- **EnableCloudwatchLogsExports**  (in the CLI: `--enable-cloudwatch-logs-exports`) –  a String, of type: `string` (a UTF-8 encoded string).

The list of log types that need to be enabled for exporting to CloudWatch
Logs.

- **EnableIAMDatabaseAuthentication**  (in the CLI: `--enable-iam-database-authentication`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Not supported by Neptune (ignored).

- **Engine**  (in the CLI: `--engine`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the database engine to be used for this instance.

Valid Values: `neptune`

- **EngineVersion**  (in the CLI: `--engine-version`) –  a String, of type: `string` (a UTF-8 encoded string).

The version number of the database engine to use. Currently, setting this
parameter has no effect.

- **Iops**  (in the CLI: `--iops`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The amount of Provisioned IOPS (input/output operations per second)
to be initially allocated for the DB instance.

- **KmsKeyId**  (in the CLI: `--kms-key-id`) –  a String, of type: `string` (a UTF-8 encoded string).

The Amazon KMS key identifier for an encrypted DB instance.

The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption
key. If you are creating a DB instance with the same Amazon account that owns the
KMS encryption key used to encrypt the new DB instance, then you can use the KMS
key alias instead of the ARN for the KM encryption key.

Not applicable. The KMS key identifier is managed by the DB cluster. For
more information, see [CreateDBCluster (action)](api-clusters.md#CreateDBCluster "api-clusters.md#CreateDBCluster").

If the `StorageEncrypted` parameter is true, and you do not
specify a value for the `KmsKeyId` parameter, then Amazon Neptune
will use your default encryption key. Amazon KMS creates the default encryption
key for your Amazon account. Your Amazon account has a different default encryption
key for each Amazon Region.

- **LicenseModel**  (in the CLI: `--license-model`) –  a String, of type: `string` (a UTF-8 encoded string).

License model information for this DB instance.

Valid values: `license-included` | `bring-your-own-license`
| `general-public-license`

- **MonitoringInterval**  (in the CLI: `--monitoring-interval`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The interval, in seconds, between points when Enhanced Monitoring metrics
are collected for the DB instance. To disable collecting Enhanced Monitoring
metrics, specify 0. The default is 0.

If `MonitoringRoleArn` is specified, then you must also
set `MonitoringInterval` to a value other than 0.

Valid Values: `0, 1, 5, 10, 15, 30, 60`

- **MonitoringRoleArn**  (in the CLI: `--monitoring-role-arn`) –  a String, of type: `string` (a UTF-8 encoded string).

The ARN for the IAM role that permits Neptune to send enhanced monitoring
metrics to Amazon CloudWatch Logs. For example, `arn:aws:iam:123456789012:role/emaccess`.

If `MonitoringInterval` is set to a value other than 0, then
you must supply a `MonitoringRoleArn` value.

- **MultiAZ**  (in the CLI: `--multi-az`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Specifies if the DB instance is a Multi-AZ deployment. You can't set the
AvailabilityZone parameter if the MultiAZ parameter is set to true.

- **Port**  (in the CLI: `--port`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The port number on which the database accepts connections.

Not applicable. The port is managed by the DB cluster. For more information,
see [CreateDBCluster (action)](api-clusters.md#CreateDBCluster "api-clusters.md#CreateDBCluster").

Default: `8182`

Type: Integer

- **PreferredBackupWindow**  (in the CLI: `--preferred-backup-window`) –  a String, of type: `string` (a UTF-8 encoded string).

The daily time range during which automated backups are created.

Not applicable. The daily time range for creating automated backups is
managed by the DB cluster. For more information, see [CreateDBCluster (action)](api-clusters.md#CreateDBCluster "api-clusters.md#CreateDBCluster").

- **PreferredMaintenanceWindow**  (in the CLI: `--preferred-maintenance-window`) –  a String, of type: `string` (a UTF-8 encoded string).

The time range each week during which system maintenance can occur, in
Universal Coordinated Time (UTC).

Format: `ddd:hh24:mi-ddd:hh24:mi`

The default is a 30-minute window selected at random from an 8-hour block
of time for each Amazon Region, occurring on a random day of the week.

Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.

Constraints: Minimum 30-minute window.

- **PromotionTier**  (in the CLI: `--promotion-tier`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

A value that specifies the order in which an Read Replica is promoted to
the primary instance after a failure of the existing primary instance.

Default: 1

Valid Values: 0 - 15

- **PubliclyAccessible**  (in the CLI: `--publicly-accessible`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

This flag should no longer be used.

- **StorageEncrypted**  (in the CLI: `--storage-encrypted`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB instance is encrypted.

Not applicable. The encryption for DB instances is managed by the DB cluster.
For more information, see [CreateDBCluster (action)](api-clusters.md#CreateDBCluster "api-clusters.md#CreateDBCluster").

Default: false

- **StorageType**  (in the CLI: `--storage-type`) –  a String, of type: `string` (a UTF-8 encoded string).

Not applicable. In Neptune the storage type is managed at the DB Cluster
level.

- **Tags**  (in the CLI: `--tags`) –  An array of [Tag](api-other-apis.md#Tag "api-other-apis.md#Tag") objects.

The tags to assign to the new instance.

- **TdeCredentialArn**  (in the CLI: `--tde-credential-arn`) –  a String, of type: `string` (a UTF-8 encoded string).

The ARN from the key store with which to associate the instance for TDE encryption.

- **TdeCredentialPassword**  (in the CLI: `--tde-credential-password`) –  a SensitiveString, of type: `string` (a UTF-8 encoded string).

The password for the given ARN from the key store in order to access the device.

- **Timezone**  (in the CLI: `--timezone`) –  a String, of type: `string` (a UTF-8 encoded string).

The time zone of the DB instance.

- **VpcSecurityGroupIds**  (in the CLI: `--vpc-security-group-ids`) –  a String, of type: `string` (a UTF-8 encoded string).

A list of EC2 VPC security groups to associate with this DB instance.

Not applicable. The associated list of EC2 VPC security groups is managed
by the DB cluster. For more information, see [CreateDBCluster (action)](api-clusters.md#CreateDBCluster "api-clusters.md#CreateDBCluster").

Default: The default EC2 VPC security group for the DB subnet group's VPC.

**Response**

Contains the details of an Amazon Neptune DB instance.

This data type is used as a response element in the [DescribeDBInstances (action)](#DescribeDBInstances "#DescribeDBInstances") action.

- **AutoMinorVersionUpgrade**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Indicates that minor version patches are applied automatically.

- **AvailabilityZone**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the Availability Zone the DB instance is located
in.

- **BackupRetentionPeriod**   – an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the number of days for which automatic DB snapshots are retained.

- **CACertificateIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

The identifier of the CA certificate for this DB instance.

- **CopyTagsToSnapshot**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether tags are copied from the DB instance to snapshots of
the DB instance.

- **DBClusterIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

If the DB instance is a member of a DB cluster, contains the name of the DB
cluster that the DB instance is a member of.

- **DBInstanceArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB instance.

- **DBInstanceClass**   – a String, of type: `string` (a UTF-8 encoded string).

Contains the name of the compute and memory capacity class of the DB instance.

- **DBInstanceIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Contains a user-supplied database identifier. This identifier is the
unique key that identifies a DB instance.

- **DbInstancePort**   – an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the port that the DB instance listens on. If the DB instance is
part of a DB cluster, this can be a different port than the DB cluster port.

- **DBInstanceStatus**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this database.

- **DbiResourceId**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Region-unique, immutable identifier for the DB instance.
This identifier is found in Amazon CloudTrail log entries whenever the Amazon
KMS key for the DB instance is accessed.

- **DBName**   – a String, of type: `string` (a UTF-8 encoded string).

The database name.

- **DBParameterGroups**   – An array of [DBParameterGroupStatus](api-parameters.md#DBParameterGroupStatus "api-parameters.md#DBParameterGroupStatus") objects.

Provides the list of DB parameter groups applied to this DB instance.

- **DBSecurityGroups**   – An array of [DBSecurityGroupMembership](api-datatypes.md#DBSecurityGroupMembership "api-datatypes.md#DBSecurityGroupMembership") objects.

Provides List of DB security group elements containing only `DBSecurityGroup.Name`
and `DBSecurityGroup.Status` subelements.

- **DBSubnetGroup**   – A [DBSubnetGroup](api-subnets.md#DBSubnetGroup "api-subnets.md#DBSubnetGroup") object.

Specifies information on the subnet group associated with the DB instance,
including the name, description, and subnets in the subnet group.

- **DeletionProtection**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Indicates whether or not the DB instance has deletion protection enabled.
The instance can't be deleted when deletion protection is enabled. See [Deleting
a DB Instance](manage-console-instances-delete.md "manage-console-instances-delete.md").

- **DomainMemberships**   – An array of [DomainMembership](api-datatypes.md#DomainMembership "api-datatypes.md#DomainMembership") objects.

Not supported

- **EnabledCloudwatchLogsExports**   – a String, of type: `string` (a UTF-8 encoded string).

A list of log types that this DB instance is configured to export to CloudWatch
Logs.

- **Endpoint**   – An [Endpoint](api-datatypes.md#Endpoint "api-datatypes.md#Endpoint") object.

Specifies the connection endpoint.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the database engine to be used for this DB instance.

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

Indicates the database engine version.

- **EnhancedMonitoringResourceArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream
that receives the Enhanced Monitoring metrics data for the DB instance.

- **IAMDatabaseAuthenticationEnabled**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

True if Amazon Identity and Access Management (IAM) authentication is
enabled, and otherwise false.

- **InstanceCreateTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Provides the date and time the DB instance was created.

- **Iops**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the Provisioned IOPS (I/O operations per second) value.

- **KmsKeyId**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported: The encryption for DB instances is managed by the DB cluster.

- **LatestRestorableTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the latest time to which a database can be restored with point-in-time
restore.

- **LicenseModel**   – a String, of type: `string` (a UTF-8 encoded string).

License model information for this DB instance.

- **MonitoringInterval**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The interval, in seconds, between points when Enhanced Monitoring metrics
are collected for the DB instance.

- **MonitoringRoleArn**   – a String, of type: `string` (a UTF-8 encoded string).

The ARN for the IAM role that permits Neptune to send Enhanced Monitoring
metrics to Amazon CloudWatch Logs.

- **MultiAZ**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies if the DB instance is a Multi-AZ deployment.

- **PendingModifiedValues**   – A [PendingModifiedValues](#PendingModifiedValues "#PendingModifiedValues") object.

Specifies that changes to the DB instance are pending. This element is
only included when changes are pending. Specific changes are identified by subelements.

- **PreferredBackupWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the daily time range during which automated backups are created
if automated backups are enabled, as determined by the `BackupRetentionPeriod`.

- **PreferredMaintenanceWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the weekly time range during which system maintenance can occur,
in Universal Coordinated Time (UTC).

- **PromotionTier**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

A value that specifies the order in which a Read Replica is promoted to the
primary instance after a failure of the existing primary instance.

- **PubliclyAccessible**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

This flag should no longer be used.

- **ReadReplicaDBClusterIdentifiers**   – a String, of type: `string` (a UTF-8 encoded string).

Contains one or more identifiers of DB clusters that are Read Replicas
of this DB instance.

- **ReadReplicaDBInstanceIdentifiers**   – a String, of type: `string` (a UTF-8 encoded string).

Contains one or more identifiers of the Read Replicas associated with
this DB instance.

- **ReadReplicaSourceDBInstanceIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Contains the identifier of the source DB instance if this DB instance is
a Read Replica.

- **SecondaryAvailabilityZone**   – a String, of type: `string` (a UTF-8 encoded string).

If present, specifies the name of the secondary Availability Zone for
a DB instance with multi-AZ support.

- **StatusInfos**   – An array of [DBInstanceStatusInfo](#DBInstanceStatusInfo "#DBInstanceStatusInfo") objects.

The status of a Read Replica. If the instance is not a Read Replica, this
is blank.

- **StorageEncrypted**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Not supported: The encryption for DB instances is managed by the DB cluster.

- **StorageType**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the storage type associated with the DB instance.

- **TdeCredentialArn**   – a String, of type: `string` (a UTF-8 encoded string).

The ARN from the key store with which the instance is associated for TDE
encryption.

- **Timezone**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported.

- **VpcSecurityGroups**   – An array of [VpcSecurityGroupMembership](api-datatypes.md#VpcSecurityGroupMembership "api-datatypes.md#VpcSecurityGroupMembership") objects.

Provides a list of VPC security group elements that the DB instance belongs
to.

###### Errors

- [DBInstanceAlreadyExistsFault](api-faults.md#DBInstanceAlreadyExistsFault "api-faults.md#DBInstanceAlreadyExistsFault")
- [InsufficientDBInstanceCapacityFault](api-faults.md#InsufficientDBInstanceCapacityFault "api-faults.md#InsufficientDBInstanceCapacityFault")
- [DBParameterGroupNotFoundFault](api-faults.md#DBParameterGroupNotFoundFault "api-faults.md#DBParameterGroupNotFoundFault")
- [DBSecurityGroupNotFoundFault](api-faults.md#DBSecurityGroupNotFoundFault "api-faults.md#DBSecurityGroupNotFoundFault")
- [InstanceQuotaExceededFault](api-faults.md#InstanceQuotaExceededFault "api-faults.md#InstanceQuotaExceededFault")
- [StorageQuotaExceededFault](api-faults.md#StorageQuotaExceededFault "api-faults.md#StorageQuotaExceededFault")
- [DBSubnetGroupNotFoundFault](api-faults.md#DBSubnetGroupNotFoundFault "api-faults.md#DBSubnetGroupNotFoundFault")
- [DBSubnetGroupDoesNotCoverEnoughAZs](api-faults.md#DBSubnetGroupDoesNotCoverEnoughAZs "api-faults.md#DBSubnetGroupDoesNotCoverEnoughAZs")
- [InvalidDBClusterStateFault](api-faults.md#InvalidDBClusterStateFault "api-faults.md#InvalidDBClusterStateFault")
- [InvalidSubnet](api-faults.md#InvalidSubnet "api-faults.md#InvalidSubnet")
- [InvalidVPCNetworkStateFault](api-faults.md#InvalidVPCNetworkStateFault "api-faults.md#InvalidVPCNetworkStateFault")
- [ProvisionedIopsNotAvailableInAZFault](api-faults.md#ProvisionedIopsNotAvailableInAZFault "api-faults.md#ProvisionedIopsNotAvailableInAZFault")
- [OptionGroupNotFoundFault](api-faults.md#OptionGroupNotFoundFault "api-faults.md#OptionGroupNotFoundFault")
- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")
- [StorageTypeNotSupportedFault](api-faults.md#StorageTypeNotSupportedFault "api-faults.md#StorageTypeNotSupportedFault")
- [AuthorizationNotFoundFault](api-faults.md#AuthorizationNotFoundFault "api-faults.md#AuthorizationNotFoundFault")
- [KMSKeyNotAccessibleFault](api-faults.md#KMSKeyNotAccessibleFault "api-faults.md#KMSKeyNotAccessibleFault")
- [DomainNotFoundFault](api-faults.md#DomainNotFoundFault "api-faults.md#DomainNotFoundFault")

## DeleteDBInstance (action)

        The AWS CLI name for this API is: `delete-db-instance`.

The DeleteDBInstance action deletes a previously provisioned DB instance.
When you delete a DB instance, all automated backups for that instance are deleted
and can't be recovered. Manual DB snapshots of the DB instance to be deleted by
`DeleteDBInstance` are not deleted.

If you request a final DB snapshot the status of the Amazon Neptune DB instance
is `deleting` until the DB snapshot is created. The API action `DescribeDBInstance`
is used to monitor the status of this operation. The action can't be canceled or
reverted once submitted.

Note that when a DB instance is in a failure state and has a status of `failed`,
`incompatible-restore`, or `incompatible-network`,
you can only delete it when the `SkipFinalSnapshot` parameter is
set to `true`.

You can't delete a DB instance if it is the only instance in the DB cluster,
or if it has deletion protection enabled.

**Request**

- **DBInstanceIdentifier**  (in the CLI: `--db-instance-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The DB instance identifier for the DB instance to be deleted. This parameter
isn't case-sensitive.

Constraints:

    + Must match the name of an existing DB instance.

- **FinalDBSnapshotIdentifier**  (in the CLI: `--final-db-snapshot-identifier`) –  a String, of type: `string` (a UTF-8 encoded string).

The DBSnapshotIdentifier of the new DBSnapshot created when SkipFinalSnapshot
is set to `false`.

###### Note

Specifying this parameter and also setting the SkipFinalShapshot parameter
to true results in an error.

Constraints:

    + Must be 1 to 255 letters or numbers.
    + First character must be a letter
    + Cannot end with a hyphen or contain two consecutive hyphens
    + Cannot be specified when deleting a Read Replica.

- **SkipFinalSnapshot**  (in the CLI: `--skip-final-snapshot`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

Determines whether a final DB snapshot is created before the DB instance
is deleted. If `true` is specified, no DBSnapshot is created. If
`false` is specified, a DB snapshot is created before the DB instance
is deleted.

Note that when a DB instance is in a failure state and has a status of 'failed',
'incompatible-restore', or 'incompatible-network', it can only be deleted
when the SkipFinalSnapshot parameter is set to "true".

Specify `true` when deleting a Read Replica.

###### Note

The FinalDBSnapshotIdentifier parameter must be specified if SkipFinalSnapshot
is `false`.

Default: `false`

**Response**

Contains the details of an Amazon Neptune DB instance.

This data type is used as a response element in the [DescribeDBInstances (action)](#DescribeDBInstances "#DescribeDBInstances") action.

- **AutoMinorVersionUpgrade**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Indicates that minor version patches are applied automatically.

- **AvailabilityZone**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the Availability Zone the DB instance is located
in.

- **BackupRetentionPeriod**   – an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the number of days for which automatic DB snapshots are retained.

- **CACertificateIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

The identifier of the CA certificate for this DB instance.

- **CopyTagsToSnapshot**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether tags are copied from the DB instance to snapshots of
the DB instance.

- **DBClusterIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

If the DB instance is a member of a DB cluster, contains the name of the DB
cluster that the DB instance is a member of.

- **DBInstanceArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB instance.

- **DBInstanceClass**   – a String, of type: `string` (a UTF-8 encoded string).

Contains the name of the compute and memory capacity class of the DB instance.

- **DBInstanceIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Contains a user-supplied database identifier. This identifier is the
unique key that identifies a DB instance.

- **DbInstancePort**   – an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the port that the DB instance listens on. If the DB instance is
part of a DB cluster, this can be a different port than the DB cluster port.

- **DBInstanceStatus**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this database.

- **DbiResourceId**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Region-unique, immutable identifier for the DB instance.
This identifier is found in Amazon CloudTrail log entries whenever the Amazon
KMS key for the DB instance is accessed.

- **DBName**   – a String, of type: `string` (a UTF-8 encoded string).

The database name.

- **DBParameterGroups**   – An array of [DBParameterGroupStatus](api-parameters.md#DBParameterGroupStatus "api-parameters.md#DBParameterGroupStatus") objects.

Provides the list of DB parameter groups applied to this DB instance.

- **DBSecurityGroups**   – An array of [DBSecurityGroupMembership](api-datatypes.md#DBSecurityGroupMembership "api-datatypes.md#DBSecurityGroupMembership") objects.

Provides List of DB security group elements containing only `DBSecurityGroup.Name`
and `DBSecurityGroup.Status` subelements.

- **DBSubnetGroup**   – A [DBSubnetGroup](api-subnets.md#DBSubnetGroup "api-subnets.md#DBSubnetGroup") object.

Specifies information on the subnet group associated with the DB instance,
including the name, description, and subnets in the subnet group.

- **DeletionProtection**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Indicates whether or not the DB instance has deletion protection enabled.
The instance can't be deleted when deletion protection is enabled. See [Deleting
a DB Instance](manage-console-instances-delete.md "manage-console-instances-delete.md").

- **DomainMemberships**   – An array of [DomainMembership](api-datatypes.md#DomainMembership "api-datatypes.md#DomainMembership") objects.

Not supported

- **EnabledCloudwatchLogsExports**   – a String, of type: `string` (a UTF-8 encoded string).

A list of log types that this DB instance is configured to export to CloudWatch
Logs.

- **Endpoint**   – An [Endpoint](api-datatypes.md#Endpoint "api-datatypes.md#Endpoint") object.

Specifies the connection endpoint.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the database engine to be used for this DB instance.

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

Indicates the database engine version.

- **EnhancedMonitoringResourceArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream
that receives the Enhanced Monitoring metrics data for the DB instance.

- **IAMDatabaseAuthenticationEnabled**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

True if Amazon Identity and Access Management (IAM) authentication is
enabled, and otherwise false.

- **InstanceCreateTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Provides the date and time the DB instance was created.

- **Iops**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the Provisioned IOPS (I/O operations per second) value.

- **KmsKeyId**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported: The encryption for DB instances is managed by the DB cluster.

- **LatestRestorableTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the latest time to which a database can be restored with point-in-time
restore.

- **LicenseModel**   – a String, of type: `string` (a UTF-8 encoded string).

License model information for this DB instance.

- **MonitoringInterval**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The interval, in seconds, between points when Enhanced Monitoring metrics
are collected for the DB instance.

- **MonitoringRoleArn**   – a String, of type: `string` (a UTF-8 encoded string).

The ARN for the IAM role that permits Neptune to send Enhanced Monitoring
metrics to Amazon CloudWatch Logs.

- **MultiAZ**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies if the DB instance is a Multi-AZ deployment.

- **PendingModifiedValues**   – A [PendingModifiedValues](#PendingModifiedValues "#PendingModifiedValues") object.

Specifies that changes to the DB instance are pending. This element is
only included when changes are pending. Specific changes are identified by subelements.

- **PreferredBackupWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the daily time range during which automated backups are created
if automated backups are enabled, as determined by the `BackupRetentionPeriod`.

- **PreferredMaintenanceWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the weekly time range during which system maintenance can occur,
in Universal Coordinated Time (UTC).

- **PromotionTier**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

A value that specifies the order in which a Read Replica is promoted to the
primary instance after a failure of the existing primary instance.

- **PubliclyAccessible**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

This flag should no longer be used.

- **ReadReplicaDBClusterIdentifiers**   – a String, of type: `string` (a UTF-8 encoded string).

Contains one or more identifiers of DB clusters that are Read Replicas
of this DB instance.

- **ReadReplicaDBInstanceIdentifiers**   – a String, of type: `string` (a UTF-8 encoded string).

Contains one or more identifiers of the Read Replicas associated with
this DB instance.

- **ReadReplicaSourceDBInstanceIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Contains the identifier of the source DB instance if this DB instance is
a Read Replica.

- **SecondaryAvailabilityZone**   – a String, of type: `string` (a UTF-8 encoded string).

If present, specifies the name of the secondary Availability Zone for
a DB instance with multi-AZ support.

- **StatusInfos**   – An array of [DBInstanceStatusInfo](#DBInstanceStatusInfo "#DBInstanceStatusInfo") objects.

The status of a Read Replica. If the instance is not a Read Replica, this
is blank.

- **StorageEncrypted**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Not supported: The encryption for DB instances is managed by the DB cluster.

- **StorageType**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the storage type associated with the DB instance.

- **TdeCredentialArn**   – a String, of type: `string` (a UTF-8 encoded string).

The ARN from the key store with which the instance is associated for TDE
encryption.

- **Timezone**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported.

- **VpcSecurityGroups**   – An array of [VpcSecurityGroupMembership](api-datatypes.md#VpcSecurityGroupMembership "api-datatypes.md#VpcSecurityGroupMembership") objects.

Provides a list of VPC security group elements that the DB instance belongs
to.

###### Errors

- [DBInstanceNotFoundFault](api-faults.md#DBInstanceNotFoundFault "api-faults.md#DBInstanceNotFoundFault")
- [InvalidDBInstanceStateFault](api-faults.md#InvalidDBInstanceStateFault "api-faults.md#InvalidDBInstanceStateFault")
- [DBSnapshotAlreadyExistsFault](api-faults.md#DBSnapshotAlreadyExistsFault "api-faults.md#DBSnapshotAlreadyExistsFault")
- [SnapshotQuotaExceededFault](api-faults.md#SnapshotQuotaExceededFault "api-faults.md#SnapshotQuotaExceededFault")
- [InvalidDBClusterStateFault](api-faults.md#InvalidDBClusterStateFault "api-faults.md#InvalidDBClusterStateFault")

## ModifyDBInstance (action)

        The AWS CLI name for this API is: `modify-db-instance`.

Modifies settings for a DB instance. You can change one or more database
configuration parameters by specifying these parameters and the new values
in the request. To learn what modifications you can make to your DB instance, call
[DescribeValidDBInstanceModifications (action)](#DescribeValidDBInstanceModifications "#DescribeValidDBInstanceModifications") before you call
ModifyDBInstance (action).

**Request**

- **AllowMajorVersionUpgrade**  (in the CLI: `--allow-major-version-upgrade`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

Indicates that major version upgrades are allowed. Changing this parameter
doesn't result in an outage and the change is asynchronously applied as soon as
possible.

- **ApplyImmediately**  (in the CLI: `--apply-immediately`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the modifications in this request and any pending modifications
are asynchronously applied as soon as possible, regardless of the `PreferredMaintenanceWindow`
setting for the DB instance.

If this parameter is set to `false`, changes to the DB instance
are applied during the next maintenance window. Some parameter changes can cause
an outage and are applied on the next call to [RebootDBInstance (action)](#RebootDBInstance "#RebootDBInstance"), or the next failure reboot.

Default: `false`

- **AutoMinorVersionUpgrade**  (in the CLI: `--auto-minor-version-upgrade`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Indicates that minor version upgrades are applied automatically to the
DB instance during the maintenance window. Changing this parameter doesn't
result in an outage except in the following case and the change is asynchronously
applied as soon as possible. An outage will result if this parameter is set to `true`
during the maintenance window, and a newer minor version is available, and Neptune
has enabled auto patching for that engine version.

- **BackupRetentionPeriod**  (in the CLI: `--backup-retention-period`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Not applicable. The retention period for automated backups is managed
by the DB cluster. For more information, see [ModifyDBCluster (action)](api-clusters.md#ModifyDBCluster "api-clusters.md#ModifyDBCluster").

Default: Uses existing setting

- **CACertificateIdentifier**  (in the CLI: `--ca-certificate-identifier`) –  a String, of type: `string` (a UTF-8 encoded string).

Indicates the certificate that needs to be associated with the instance.

- **CloudwatchLogsExportConfiguration**  (in the CLI: `--cloudwatch-logs-export-configuration`) –  A [CloudwatchLogsExportConfiguration](api-clusters.md#CloudwatchLogsExportConfiguration "api-clusters.md#CloudwatchLogsExportConfiguration") object.

The configuration setting for the log types to be enabled for export to
CloudWatch Logs for a specific DB instance or DB cluster.

- **CopyTagsToSnapshot**  (in the CLI: `--copy-tags-to-snapshot`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

True to copy all tags from the DB instance to snapshots of the DB instance,
and otherwise false. The default is false.

- **DBInstanceClass**  (in the CLI: `--db-instance-class`) –  a String, of type: `string` (a UTF-8 encoded string).

The new compute and memory capacity of the DB instance, for example, `db.m4.large`.
Not all DB instance classes are available in all Amazon Regions.

If you modify the DB instance class, an outage occurs during the change.
The change is applied during the next maintenance window, unless `ApplyImmediately`
is specified as `true` for this request.

Default: Uses existing setting

- **DBInstanceIdentifier**  (in the CLI: `--db-instance-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The DB instance identifier. This value is stored as a lowercase string.

Constraints:

    + Must match the identifier of an existing DBInstance.

- **DBParameterGroupName**  (in the CLI: `--db-parameter-group-name`) –  a String, of type: `string` (a UTF-8 encoded string).

The name of the DB parameter group to apply to the DB instance. Changing
this setting doesn't result in an outage. The parameter group name itself is changed
immediately, but the actual parameter changes are not applied until you reboot
the instance without failover. The db instance will NOT be rebooted automatically
and the parameter changes will NOT be applied during the next maintenance window.

Default: Uses existing setting

Constraints: The DB parameter group must be in the same DB parameter group
family as this DB instance.

- **DBPortNumber**  (in the CLI: `--db-port-number`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The port number on which the database accepts connections.

The value of the `DBPortNumber` parameter must not match
any of the port values specified for options in the option group for the DB instance.

Your database will restart when you change the `DBPortNumber`
value regardless of the value of the `ApplyImmediately` parameter.

Default: `8182`

- **DBSecurityGroups**  (in the CLI: `--db-security-groups`) –  a String, of type: `string` (a UTF-8 encoded string).

A list of DB security groups to authorize on this DB instance. Changing
this setting doesn't result in an outage and the change is asynchronously applied
as soon as possible.

Constraints:

    + If supplied, must match existing DBSecurityGroups.

- **DBSubnetGroupName**  (in the CLI: `--db-subnet-group-name`) –  a String, of type: `string` (a UTF-8 encoded string).

The new DB subnet group for the DB instance. You can use this parameter to
move your DB instance to a different VPC.

Changing the subnet group causes an outage during the change. The change
is applied during the next maintenance window, unless you specify `true`
for the `ApplyImmediately` parameter.

Constraints: If supplied, must match the name of an existing DBSubnetGroup.

Example: `mySubnetGroup`

- **DeletionProtection**  (in the CLI: `--deletion-protection`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

A value that indicates whether the DB instance has deletion protection
enabled. The database can't be deleted when deletion protection is enabled.
By default, deletion protection is disabled. See [Deleting
a DB Instance](manage-console-instances-delete.md "manage-console-instances-delete.md").

- **Domain**  (in the CLI: `--domain`) –  a String, of type: `string` (a UTF-8 encoded string).

Not supported.

- **DomainIAMRoleName**  (in the CLI: `--domain-iam-role-name`) –  a String, of type: `string` (a UTF-8 encoded string).

Not supported

- **EnableIAMDatabaseAuthentication**  (in the CLI: `--enable-iam-database-authentication`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

True to enable mapping of Amazon Identity and Access Management (IAM)
accounts to database accounts, and otherwise false.

You can enable IAM database authentication for the following database
engines

Not applicable. Mapping Amazon IAM accounts to database accounts is managed
by the DB cluster. For more information, see [ModifyDBCluster (action)](api-clusters.md#ModifyDBCluster "api-clusters.md#ModifyDBCluster").

Default: `false`

- **EngineVersion**  (in the CLI: `--engine-version`) –  a String, of type: `string` (a UTF-8 encoded string).

The version number of the database engine to upgrade to. Currently, setting
this parameter has no effect. To upgrade your database engine to the most recent
release, use the [ApplyPendingMaintenanceAction (action)](api-other-apis.md#ApplyPendingMaintenanceAction "api-other-apis.md#ApplyPendingMaintenanceAction") API.

- **Iops**  (in the CLI: `--iops`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The new Provisioned IOPS (I/O operations per second) value for the instance.

Changing this setting doesn't result in an outage and the change is applied
during the next maintenance window unless the `ApplyImmediately`
parameter is set to `true` for this request.

Default: Uses existing setting

- **MonitoringInterval**  (in the CLI: `--monitoring-interval`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The interval, in seconds, between points when Enhanced Monitoring metrics
are collected for the DB instance. To disable collecting Enhanced Monitoring
metrics, specify 0. The default is 0.

If `MonitoringRoleArn` is specified, then you must also
set `MonitoringInterval` to a value other than 0.

Valid Values: `0, 1, 5, 10, 15, 30, 60`

- **MonitoringRoleArn**  (in the CLI: `--monitoring-role-arn`) –  a String, of type: `string` (a UTF-8 encoded string).

The ARN for the IAM role that permits Neptune to send enhanced monitoring
metrics to Amazon CloudWatch Logs. For example, `arn:aws:iam:123456789012:role/emaccess`.

If `MonitoringInterval` is set to a value other than 0, then
you must supply a `MonitoringRoleArn` value.

- **MultiAZ**  (in the CLI: `--multi-az`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Specifies if the DB instance is a Multi-AZ deployment. Changing this parameter
doesn't result in an outage and the change is applied during the next maintenance
window unless the `ApplyImmediately` parameter is set to `true`
for this request.

- **NewDBInstanceIdentifier**  (in the CLI: `--new-db-instance-identifier`) –  a String, of type: `string` (a UTF-8 encoded string).

The new DB instance identifier for the DB instance when renaming a DB instance.
When you change the DB instance identifier, an instance reboot will occur immediately
if you set `Apply Immediately` to true, or will occur during the next
maintenance window if `Apply Immediately` to false. This value
is stored as a lowercase string.

Constraints:

    + Must contain from 1 to 63 letters, numbers, or hyphens.
    + The first character must be a letter.
    + Cannot end with a hyphen or contain two consecutive hyphens.

Example: `mydbinstance`

- **PreferredBackupWindow**  (in the CLI: `--preferred-backup-window`) –  a String, of type: `string` (a UTF-8 encoded string).

The daily time range during which automated backups are created if automated
backups are enabled.

Not applicable. The daily time range for creating automated backups is
managed by the DB cluster. For more information, see [ModifyDBCluster (action)](api-clusters.md#ModifyDBCluster "api-clusters.md#ModifyDBCluster").

Constraints:

    + Must be in the format hh24:mi-hh24:mi
    + Must be in Universal Time Coordinated (UTC)
    + Must not conflict with the preferred maintenance window
    + Must be at least 30 minutes

- **PreferredMaintenanceWindow**  (in the CLI: `--preferred-maintenance-window`) –  a String, of type: `string` (a UTF-8 encoded string).

The weekly time range (in UTC) during which system maintenance can occur,
which might result in an outage. Changing this parameter doesn't result in an
outage, except in the following situation, and the change is asynchronously
applied as soon as possible. If there are pending actions that cause a reboot,
and the maintenance window is changed to include the current time, then changing
this parameter will cause a reboot of the DB instance. If moving this window to
the current time, there must be at least 30 minutes between the current time and
end of the window to ensure pending changes are applied.

Default: Uses existing setting

Format: ddd:hh24:mi-ddd:hh24:mi

Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun

Constraints: Must be at least 30 minutes

- **PromotionTier**  (in the CLI: `--promotion-tier`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

A value that specifies the order in which a Read Replica is promoted to the
primary instance after a failure of the existing primary instance.

Default: 1

Valid Values: 0 - 15

- **PubliclyAccessible**  (in the CLI: `--publicly-accessible`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

This flag should no longer be used.

- **StorageType**  (in the CLI: `--storage-type`) –  a String, of type: `string` (a UTF-8 encoded string).

Not applicable. In Neptune the storage type is managed at the DB Cluster
level.

- **TdeCredentialArn**  (in the CLI: `--tde-credential-arn`) –  a String, of type: `string` (a UTF-8 encoded string).

The ARN from the key store with which to associate the instance for TDE encryption.

- **TdeCredentialPassword**  (in the CLI: `--tde-credential-password`) –  a SensitiveString, of type: `string` (a UTF-8 encoded string).

The password for the given ARN from the key store in order to access the device.

- **VpcSecurityGroupIds**  (in the CLI: `--vpc-security-group-ids`) –  a String, of type: `string` (a UTF-8 encoded string).

A list of EC2 VPC security groups to authorize on this DB instance. This
change is asynchronously applied as soon as possible.

Not applicable. The associated list of EC2 VPC security groups is managed
by the DB cluster. For more information, see [ModifyDBCluster (action)](api-clusters.md#ModifyDBCluster "api-clusters.md#ModifyDBCluster").

Constraints:

    + If supplied, must match existing VpcSecurityGroupIds.

**Response**

Contains the details of an Amazon Neptune DB instance.

This data type is used as a response element in the [DescribeDBInstances (action)](#DescribeDBInstances "#DescribeDBInstances") action.

- **AutoMinorVersionUpgrade**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Indicates that minor version patches are applied automatically.

- **AvailabilityZone**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the Availability Zone the DB instance is located
in.

- **BackupRetentionPeriod**   – an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the number of days for which automatic DB snapshots are retained.

- **CACertificateIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

The identifier of the CA certificate for this DB instance.

- **CopyTagsToSnapshot**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether tags are copied from the DB instance to snapshots of
the DB instance.

- **DBClusterIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

If the DB instance is a member of a DB cluster, contains the name of the DB
cluster that the DB instance is a member of.

- **DBInstanceArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB instance.

- **DBInstanceClass**   – a String, of type: `string` (a UTF-8 encoded string).

Contains the name of the compute and memory capacity class of the DB instance.

- **DBInstanceIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Contains a user-supplied database identifier. This identifier is the
unique key that identifies a DB instance.

- **DbInstancePort**   – an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the port that the DB instance listens on. If the DB instance is
part of a DB cluster, this can be a different port than the DB cluster port.

- **DBInstanceStatus**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this database.

- **DbiResourceId**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Region-unique, immutable identifier for the DB instance.
This identifier is found in Amazon CloudTrail log entries whenever the Amazon
KMS key for the DB instance is accessed.

- **DBName**   – a String, of type: `string` (a UTF-8 encoded string).

The database name.

- **DBParameterGroups**   – An array of [DBParameterGroupStatus](api-parameters.md#DBParameterGroupStatus "api-parameters.md#DBParameterGroupStatus") objects.

Provides the list of DB parameter groups applied to this DB instance.

- **DBSecurityGroups**   – An array of [DBSecurityGroupMembership](api-datatypes.md#DBSecurityGroupMembership "api-datatypes.md#DBSecurityGroupMembership") objects.

Provides List of DB security group elements containing only `DBSecurityGroup.Name`
and `DBSecurityGroup.Status` subelements.

- **DBSubnetGroup**   – A [DBSubnetGroup](api-subnets.md#DBSubnetGroup "api-subnets.md#DBSubnetGroup") object.

Specifies information on the subnet group associated with the DB instance,
including the name, description, and subnets in the subnet group.

- **DeletionProtection**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Indicates whether or not the DB instance has deletion protection enabled.
The instance can't be deleted when deletion protection is enabled. See [Deleting
a DB Instance](manage-console-instances-delete.md "manage-console-instances-delete.md").

- **DomainMemberships**   – An array of [DomainMembership](api-datatypes.md#DomainMembership "api-datatypes.md#DomainMembership") objects.

Not supported

- **EnabledCloudwatchLogsExports**   – a String, of type: `string` (a UTF-8 encoded string).

A list of log types that this DB instance is configured to export to CloudWatch
Logs.

- **Endpoint**   – An [Endpoint](api-datatypes.md#Endpoint "api-datatypes.md#Endpoint") object.

Specifies the connection endpoint.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the database engine to be used for this DB instance.

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

Indicates the database engine version.

- **EnhancedMonitoringResourceArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream
that receives the Enhanced Monitoring metrics data for the DB instance.

- **IAMDatabaseAuthenticationEnabled**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

True if Amazon Identity and Access Management (IAM) authentication is
enabled, and otherwise false.

- **InstanceCreateTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Provides the date and time the DB instance was created.

- **Iops**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the Provisioned IOPS (I/O operations per second) value.

- **KmsKeyId**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported: The encryption for DB instances is managed by the DB cluster.

- **LatestRestorableTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the latest time to which a database can be restored with point-in-time
restore.

- **LicenseModel**   – a String, of type: `string` (a UTF-8 encoded string).

License model information for this DB instance.

- **MonitoringInterval**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The interval, in seconds, between points when Enhanced Monitoring metrics
are collected for the DB instance.

- **MonitoringRoleArn**   – a String, of type: `string` (a UTF-8 encoded string).

The ARN for the IAM role that permits Neptune to send Enhanced Monitoring
metrics to Amazon CloudWatch Logs.

- **MultiAZ**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies if the DB instance is a Multi-AZ deployment.

- **PendingModifiedValues**   – A [PendingModifiedValues](#PendingModifiedValues "#PendingModifiedValues") object.

Specifies that changes to the DB instance are pending. This element is
only included when changes are pending. Specific changes are identified by subelements.

- **PreferredBackupWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the daily time range during which automated backups are created
if automated backups are enabled, as determined by the `BackupRetentionPeriod`.

- **PreferredMaintenanceWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the weekly time range during which system maintenance can occur,
in Universal Coordinated Time (UTC).

- **PromotionTier**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

A value that specifies the order in which a Read Replica is promoted to the
primary instance after a failure of the existing primary instance.

- **PubliclyAccessible**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

This flag should no longer be used.

- **ReadReplicaDBClusterIdentifiers**   – a String, of type: `string` (a UTF-8 encoded string).

Contains one or more identifiers of DB clusters that are Read Replicas
of this DB instance.

- **ReadReplicaDBInstanceIdentifiers**   – a String, of type: `string` (a UTF-8 encoded string).

Contains one or more identifiers of the Read Replicas associated with
this DB instance.

- **ReadReplicaSourceDBInstanceIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Contains the identifier of the source DB instance if this DB instance is
a Read Replica.

- **SecondaryAvailabilityZone**   – a String, of type: `string` (a UTF-8 encoded string).

If present, specifies the name of the secondary Availability Zone for
a DB instance with multi-AZ support.

- **StatusInfos**   – An array of [DBInstanceStatusInfo](#DBInstanceStatusInfo "#DBInstanceStatusInfo") objects.

The status of a Read Replica. If the instance is not a Read Replica, this
is blank.

- **StorageEncrypted**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Not supported: The encryption for DB instances is managed by the DB cluster.

- **StorageType**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the storage type associated with the DB instance.

- **TdeCredentialArn**   – a String, of type: `string` (a UTF-8 encoded string).

The ARN from the key store with which the instance is associated for TDE
encryption.

- **Timezone**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported.

- **VpcSecurityGroups**   – An array of [VpcSecurityGroupMembership](api-datatypes.md#VpcSecurityGroupMembership "api-datatypes.md#VpcSecurityGroupMembership") objects.

Provides a list of VPC security group elements that the DB instance belongs
to.

###### Errors

- [InvalidDBInstanceStateFault](api-faults.md#InvalidDBInstanceStateFault "api-faults.md#InvalidDBInstanceStateFault")
- [InvalidDBSecurityGroupStateFault](api-faults.md#InvalidDBSecurityGroupStateFault "api-faults.md#InvalidDBSecurityGroupStateFault")
- [DBInstanceAlreadyExistsFault](api-faults.md#DBInstanceAlreadyExistsFault "api-faults.md#DBInstanceAlreadyExistsFault")
- [DBInstanceNotFoundFault](api-faults.md#DBInstanceNotFoundFault "api-faults.md#DBInstanceNotFoundFault")
- [DBSecurityGroupNotFoundFault](api-faults.md#DBSecurityGroupNotFoundFault "api-faults.md#DBSecurityGroupNotFoundFault")
- [DBParameterGroupNotFoundFault](api-faults.md#DBParameterGroupNotFoundFault "api-faults.md#DBParameterGroupNotFoundFault")
- [InsufficientDBInstanceCapacityFault](api-faults.md#InsufficientDBInstanceCapacityFault "api-faults.md#InsufficientDBInstanceCapacityFault")
- [StorageQuotaExceededFault](api-faults.md#StorageQuotaExceededFault "api-faults.md#StorageQuotaExceededFault")
- [InvalidVPCNetworkStateFault](api-faults.md#InvalidVPCNetworkStateFault "api-faults.md#InvalidVPCNetworkStateFault")
- [ProvisionedIopsNotAvailableInAZFault](api-faults.md#ProvisionedIopsNotAvailableInAZFault "api-faults.md#ProvisionedIopsNotAvailableInAZFault")
- [OptionGroupNotFoundFault](api-faults.md#OptionGroupNotFoundFault "api-faults.md#OptionGroupNotFoundFault")
- [DBUpgradeDependencyFailureFault](api-faults.md#DBUpgradeDependencyFailureFault "api-faults.md#DBUpgradeDependencyFailureFault")
- [StorageTypeNotSupportedFault](api-faults.md#StorageTypeNotSupportedFault "api-faults.md#StorageTypeNotSupportedFault")
- [AuthorizationNotFoundFault](api-faults.md#AuthorizationNotFoundFault "api-faults.md#AuthorizationNotFoundFault")
- [CertificateNotFoundFault](api-faults.md#CertificateNotFoundFault "api-faults.md#CertificateNotFoundFault")
- [DomainNotFoundFault](api-faults.md#DomainNotFoundFault "api-faults.md#DomainNotFoundFault")

## RebootDBInstance (action)

        The AWS CLI name for this API is: `reboot-db-instance`.

You might need to reboot your DB instance, usually for maintenance reasons.
For example, if you make certain modifications, or if you change the DB parameter
group associated with the DB instance, you must reboot the instance for the changes
to take effect.

Rebooting a DB instance restarts the database engine service. Rebooting
a DB instance results in a momentary outage, during which the DB instance status
is set to rebooting.

**Request**

- **DBInstanceIdentifier**  (in the CLI: `--db-instance-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The DB instance identifier. This parameter is stored as a lowercase string.

Constraints:

    + Must match the identifier of an existing DBInstance.

- **ForceFailover**  (in the CLI: `--force-failover`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

When `true`, the reboot is conducted through a MultiAZ failover.

Constraint: You can't specify `true` if the instance is not
configured for MultiAZ.

**Response**

Contains the details of an Amazon Neptune DB instance.

This data type is used as a response element in the [DescribeDBInstances (action)](#DescribeDBInstances "#DescribeDBInstances") action.

- **AutoMinorVersionUpgrade**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Indicates that minor version patches are applied automatically.

- **AvailabilityZone**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the Availability Zone the DB instance is located
in.

- **BackupRetentionPeriod**   – an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the number of days for which automatic DB snapshots are retained.

- **CACertificateIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

The identifier of the CA certificate for this DB instance.

- **CopyTagsToSnapshot**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether tags are copied from the DB instance to snapshots of
the DB instance.

- **DBClusterIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

If the DB instance is a member of a DB cluster, contains the name of the DB
cluster that the DB instance is a member of.

- **DBInstanceArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB instance.

- **DBInstanceClass**   – a String, of type: `string` (a UTF-8 encoded string).

Contains the name of the compute and memory capacity class of the DB instance.

- **DBInstanceIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Contains a user-supplied database identifier. This identifier is the
unique key that identifies a DB instance.

- **DbInstancePort**   – an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the port that the DB instance listens on. If the DB instance is
part of a DB cluster, this can be a different port than the DB cluster port.

- **DBInstanceStatus**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this database.

- **DbiResourceId**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Region-unique, immutable identifier for the DB instance.
This identifier is found in Amazon CloudTrail log entries whenever the Amazon
KMS key for the DB instance is accessed.

- **DBName**   – a String, of type: `string` (a UTF-8 encoded string).

The database name.

- **DBParameterGroups**   – An array of [DBParameterGroupStatus](api-parameters.md#DBParameterGroupStatus "api-parameters.md#DBParameterGroupStatus") objects.

Provides the list of DB parameter groups applied to this DB instance.

- **DBSecurityGroups**   – An array of [DBSecurityGroupMembership](api-datatypes.md#DBSecurityGroupMembership "api-datatypes.md#DBSecurityGroupMembership") objects.

Provides List of DB security group elements containing only `DBSecurityGroup.Name`
and `DBSecurityGroup.Status` subelements.

- **DBSubnetGroup**   – A [DBSubnetGroup](api-subnets.md#DBSubnetGroup "api-subnets.md#DBSubnetGroup") object.

Specifies information on the subnet group associated with the DB instance,
including the name, description, and subnets in the subnet group.

- **DeletionProtection**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Indicates whether or not the DB instance has deletion protection enabled.
The instance can't be deleted when deletion protection is enabled. See [Deleting
a DB Instance](manage-console-instances-delete.md "manage-console-instances-delete.md").

- **DomainMemberships**   – An array of [DomainMembership](api-datatypes.md#DomainMembership "api-datatypes.md#DomainMembership") objects.

Not supported

- **EnabledCloudwatchLogsExports**   – a String, of type: `string` (a UTF-8 encoded string).

A list of log types that this DB instance is configured to export to CloudWatch
Logs.

- **Endpoint**   – An [Endpoint](api-datatypes.md#Endpoint "api-datatypes.md#Endpoint") object.

Specifies the connection endpoint.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the database engine to be used for this DB instance.

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

Indicates the database engine version.

- **EnhancedMonitoringResourceArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream
that receives the Enhanced Monitoring metrics data for the DB instance.

- **IAMDatabaseAuthenticationEnabled**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

True if Amazon Identity and Access Management (IAM) authentication is
enabled, and otherwise false.

- **InstanceCreateTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Provides the date and time the DB instance was created.

- **Iops**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the Provisioned IOPS (I/O operations per second) value.

- **KmsKeyId**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported: The encryption for DB instances is managed by the DB cluster.

- **LatestRestorableTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the latest time to which a database can be restored with point-in-time
restore.

- **LicenseModel**   – a String, of type: `string` (a UTF-8 encoded string).

License model information for this DB instance.

- **MonitoringInterval**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The interval, in seconds, between points when Enhanced Monitoring metrics
are collected for the DB instance.

- **MonitoringRoleArn**   – a String, of type: `string` (a UTF-8 encoded string).

The ARN for the IAM role that permits Neptune to send Enhanced Monitoring
metrics to Amazon CloudWatch Logs.

- **MultiAZ**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies if the DB instance is a Multi-AZ deployment.

- **PendingModifiedValues**   – A [PendingModifiedValues](#PendingModifiedValues "#PendingModifiedValues") object.

Specifies that changes to the DB instance are pending. This element is
only included when changes are pending. Specific changes are identified by subelements.

- **PreferredBackupWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the daily time range during which automated backups are created
if automated backups are enabled, as determined by the `BackupRetentionPeriod`.

- **PreferredMaintenanceWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the weekly time range during which system maintenance can occur,
in Universal Coordinated Time (UTC).

- **PromotionTier**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

A value that specifies the order in which a Read Replica is promoted to the
primary instance after a failure of the existing primary instance.

- **PubliclyAccessible**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

This flag should no longer be used.

- **ReadReplicaDBClusterIdentifiers**   – a String, of type: `string` (a UTF-8 encoded string).

Contains one or more identifiers of DB clusters that are Read Replicas
of this DB instance.

- **ReadReplicaDBInstanceIdentifiers**   – a String, of type: `string` (a UTF-8 encoded string).

Contains one or more identifiers of the Read Replicas associated with
this DB instance.

- **ReadReplicaSourceDBInstanceIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Contains the identifier of the source DB instance if this DB instance is
a Read Replica.

- **SecondaryAvailabilityZone**   – a String, of type: `string` (a UTF-8 encoded string).

If present, specifies the name of the secondary Availability Zone for
a DB instance with multi-AZ support.

- **StatusInfos**   – An array of [DBInstanceStatusInfo](#DBInstanceStatusInfo "#DBInstanceStatusInfo") objects.

The status of a Read Replica. If the instance is not a Read Replica, this
is blank.

- **StorageEncrypted**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Not supported: The encryption for DB instances is managed by the DB cluster.

- **StorageType**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the storage type associated with the DB instance.

- **TdeCredentialArn**   – a String, of type: `string` (a UTF-8 encoded string).

The ARN from the key store with which the instance is associated for TDE
encryption.

- **Timezone**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported.

- **VpcSecurityGroups**   – An array of [VpcSecurityGroupMembership](api-datatypes.md#VpcSecurityGroupMembership "api-datatypes.md#VpcSecurityGroupMembership") objects.

Provides a list of VPC security group elements that the DB instance belongs
to.

###### Errors

- [InvalidDBInstanceStateFault](api-faults.md#InvalidDBInstanceStateFault "api-faults.md#InvalidDBInstanceStateFault")
- [DBInstanceNotFoundFault](api-faults.md#DBInstanceNotFoundFault "api-faults.md#DBInstanceNotFoundFault")

## DescribeDBInstances (action)

        The AWS CLI name for this API is: `describe-db-instances`.

Returns information about provisioned instances, and supports pagination.

###### Note

This operation can also return information for Amazon RDS instances and
Amazon DocDB instances.

**Request**

- **DBInstanceIdentifier**  (in the CLI: `--db-instance-identifier`) –  a String, of type: `string` (a UTF-8 encoded string).

The user-supplied instance identifier. If this parameter is specified,
information from only the specific DB instance is returned. This parameter isn't
case-sensitive.

Constraints:

    + If supplied, must match the identifier of an existing DBInstance.

- **Filters**  (in the CLI: `--filters`) –  An array of [Filter](api-datatypes.md#Filter "api-datatypes.md#Filter") objects.

A filter that specifies one or more DB instances to describe.

Supported filters:

    + `db-cluster-id` - Accepts DB cluster identifiers and DB
     cluster Amazon Resource Names (ARNs). The results list will only include information
     about the DB instances associated with the DB clusters identified by these ARNs.
    + `engine` - Accepts an engine name (such as `neptune`),
     and restricts the results list to DB instances created by that engine.

For example, to invoke this API from the Amazon CLI and filter so that only
Neptune DB instances are returned, you could use the following command:

```
aws neptune describe-db-instances \
            --filters  Name=engine,Values=neptune
```

- **Marker**  (in the CLI: `--marker`) –  a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous `DescribeDBInstances`
request. If this parameter is specified, the response includes only records
beyond the marker, up to the value specified by `MaxRecords`.

- **MaxRecords**  (in the CLI: `--max-records`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The maximum number of records to include in the response. If more records
exist than the specified `MaxRecords` value, a pagination token
called a marker is included in the response so that the remaining results can be
retrieved.

Default: 100

Constraints: Minimum 20, maximum 100.

**Response**

- **DBInstances**   – An array of [DBInstance](#DBInstance "#DBInstance") objects.

A list of [DBInstance (structure)](#DBInstance "#DBInstance") instances.

- **Marker**   – a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous request. If this parameter
is specified, the response includes only records beyond the marker, up to the
value specified by `MaxRecords` .

###### Errors

- [DBInstanceNotFoundFault](api-faults.md#DBInstanceNotFoundFault "api-faults.md#DBInstanceNotFoundFault")

## DescribeOrderableDBInstanceOptions (action)

        The AWS CLI name for this API is: `describe-orderable-db-instance-options`.

Returns a list of orderable DB instance options for the specified engine.

**Request**

- **DBInstanceClass**  (in the CLI: `--db-instance-class`) –  a String, of type: `string` (a UTF-8 encoded string).

The DB instance class filter value. Specify this parameter to show only
the available offerings matching the specified DB instance class.

- **Engine**  (in the CLI: `--engine`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the engine to retrieve DB instance options for.

- **EngineVersion**  (in the CLI: `--engine-version`) –  a String, of type: `string` (a UTF-8 encoded string).

The engine version filter value. Specify this parameter to show only the
available offerings matching the specified engine version.

- **Filters**  (in the CLI: `--filters`) –  An array of [Filter](api-datatypes.md#Filter "api-datatypes.md#Filter") objects.

This parameter is not currently supported.

- **LicenseModel**  (in the CLI: `--license-model`) –  a String, of type: `string` (a UTF-8 encoded string).

The license model filter value. Specify this parameter to show only the
available offerings matching the specified license model.

- **Marker**  (in the CLI: `--marker`) –  a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions
request. If this parameter is specified, the response includes only records
beyond the marker, up to the value specified by `MaxRecords` .

- **MaxRecords**  (in the CLI: `--max-records`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The maximum number of records to include in the response. If more records
exist than the specified `MaxRecords` value, a pagination token
called a marker is included in the response so that the remaining results can be
retrieved.

Default: 100

Constraints: Minimum 20, maximum 100.

- **Vpc**  (in the CLI: `--vpc`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

The VPC filter value. Specify this parameter to show only the available
VPC or non-VPC offerings.

**Response**

- **Marker**   – a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous OrderableDBInstanceOptions
request. If this parameter is specified, the response includes only records
beyond the marker, up to the value specified by `MaxRecords` .

- **OrderableDBInstanceOptions**   – An array of [OrderableDBInstanceOption](#OrderableDBInstanceOption "#OrderableDBInstanceOption") objects.

An [OrderableDBInstanceOption (structure)](#OrderableDBInstanceOption "#OrderableDBInstanceOption") structure containing
information about orderable options for the DB instance.

## DescribeValidDBInstanceModifications (action)

        The AWS CLI name for this API is: `describe-valid-db-instance-modifications`.

You can call DescribeValidDBInstanceModifications (action) to learn what modifications you can make to your DB instance. You can use this
information when you call [ModifyDBInstance (action)](#ModifyDBInstance "#ModifyDBInstance").

**Request**

- **DBInstanceIdentifier**  (in the CLI: `--db-instance-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The customer identifier or the ARN of your DB instance.

**Response**

Information about valid modifications that you can make to your DB instance.
Contains the result of a successful call to the DescribeValidDBInstanceModifications (action) action. You can use this information when you call [ModifyDBInstance (action)](#ModifyDBInstance "#ModifyDBInstance").

- **Storage**   – An array of [ValidStorageOptions](#ValidStorageOptions "#ValidStorageOptions") objects.

Valid storage options for your DB instance.

###### Errors

- [DBInstanceNotFoundFault](api-faults.md#DBInstanceNotFoundFault "api-faults.md#DBInstanceNotFoundFault")
- [InvalidDBInstanceStateFault](api-faults.md#InvalidDBInstanceStateFault "api-faults.md#InvalidDBInstanceStateFault")

## _Structures:_

## DBInstance (structure)

Contains the details of an Amazon Neptune DB instance.

This data type is used as a response element in the [DescribeDBInstances (action)](#DescribeDBInstances "#DescribeDBInstances") action.

###### Fields

- **AutoMinorVersionUpgrade** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Indicates that minor version patches are applied automatically.

- **AvailabilityZone** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the Availability Zone the DB instance is located
in.

- **BackupRetentionPeriod** – This is an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the number of days for which automatic DB snapshots are retained.

- **CACertificateIdentifier** – This is a String, of type: `string` (a UTF-8 encoded string).

The identifier of the CA certificate for this DB instance.

- **CopyTagsToSnapshot** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether tags are copied from the DB instance to snapshots of
the DB instance.

- **DBClusterIdentifier** – This is a String, of type: `string` (a UTF-8 encoded string).

If the DB instance is a member of a DB cluster, contains the name of the DB
cluster that the DB instance is a member of.

- **DBInstanceArn** – This is a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB instance.

- **DBInstanceClass** – This is a String, of type: `string` (a UTF-8 encoded string).

Contains the name of the compute and memory capacity class of the DB instance.

- **DBInstanceIdentifier** – This is a String, of type: `string` (a UTF-8 encoded string).

Contains a user-supplied database identifier. This identifier is the
unique key that identifies a DB instance.

- **DbInstancePort** – This is an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the port that the DB instance listens on. If the DB instance is
part of a DB cluster, this can be a different port than the DB cluster port.

- **DBInstanceStatus** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this database.

- **DbiResourceId** – This is a String, of type: `string` (a UTF-8 encoded string).

The Amazon Region-unique, immutable identifier for the DB instance.
This identifier is found in Amazon CloudTrail log entries whenever the Amazon
KMS key for the DB instance is accessed.

- **DBName** – This is a String, of type: `string` (a UTF-8 encoded string).

The database name.

- **DBParameterGroups** – This is An array of [DBParameterGroupStatus](api-parameters.md#DBParameterGroupStatus "api-parameters.md#DBParameterGroupStatus") objects.

Provides the list of DB parameter groups applied to this DB instance.

- **DBSecurityGroups** – This is An array of [DBSecurityGroupMembership](api-datatypes.md#DBSecurityGroupMembership "api-datatypes.md#DBSecurityGroupMembership") objects.

Provides List of DB security group elements containing only `DBSecurityGroup.Name`
and `DBSecurityGroup.Status` subelements.

- **DBSubnetGroup** – This is A [DBSubnetGroup](api-subnets.md#DBSubnetGroup "api-subnets.md#DBSubnetGroup") object.

Specifies information on the subnet group associated with the DB instance,
including the name, description, and subnets in the subnet group.

- **DeletionProtection** – This is a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Indicates whether or not the DB instance has deletion protection enabled.
The instance can't be deleted when deletion protection is enabled. See [Deleting
a DB Instance](manage-console-instances-delete.md "manage-console-instances-delete.md").

- **DomainMemberships** – This is An array of [DomainMembership](api-datatypes.md#DomainMembership "api-datatypes.md#DomainMembership") objects.

Not supported

- **EnabledCloudwatchLogsExports** – This is a String, of type: `string` (a UTF-8 encoded string).

A list of log types that this DB instance is configured to export to CloudWatch
Logs.

- **Endpoint** – This is An [Endpoint](api-datatypes.md#Endpoint "api-datatypes.md#Endpoint") object.

Specifies the connection endpoint.

- **Engine** – This is a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the database engine to be used for this DB instance.

- **EngineVersion** – This is a String, of type: `string` (a UTF-8 encoded string).

Indicates the database engine version.

- **EnhancedMonitoringResourceArn** – This is a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream
that receives the Enhanced Monitoring metrics data for the DB instance.

- **IAMDatabaseAuthenticationEnabled** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

True if Amazon Identity and Access Management (IAM) authentication is
enabled, and otherwise false.

- **InstanceCreateTime** – This is a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Provides the date and time the DB instance was created.

- **Iops** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the Provisioned IOPS (I/O operations per second) value.

- **KmsKeyId** – This is a String, of type: `string` (a UTF-8 encoded string).

Not supported: The encryption for DB instances is managed by the DB cluster.

- **LatestRestorableTime** – This is a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the latest time to which a database can be restored with point-in-time
restore.

- **LicenseModel** – This is a String, of type: `string` (a UTF-8 encoded string).

License model information for this DB instance.

- **MonitoringInterval** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The interval, in seconds, between points when Enhanced Monitoring metrics
are collected for the DB instance.

- **MonitoringRoleArn** – This is a String, of type: `string` (a UTF-8 encoded string).

The ARN for the IAM role that permits Neptune to send Enhanced Monitoring
metrics to Amazon CloudWatch Logs.

- **MultiAZ** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies if the DB instance is a Multi-AZ deployment.

- **PendingModifiedValues** – This is A [PendingModifiedValues](#PendingModifiedValues "#PendingModifiedValues") object.

Specifies that changes to the DB instance are pending. This element is
only included when changes are pending. Specific changes are identified by subelements.

- **PreferredBackupWindow** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the daily time range during which automated backups are created
if automated backups are enabled, as determined by the `BackupRetentionPeriod`.

- **PreferredMaintenanceWindow** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the weekly time range during which system maintenance can occur,
in Universal Coordinated Time (UTC).

- **PromotionTier** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

A value that specifies the order in which a Read Replica is promoted to the
primary instance after a failure of the existing primary instance.

- **PubliclyAccessible** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

This flag should no longer be used.

- **ReadReplicaDBClusterIdentifiers** – This is a String, of type: `string` (a UTF-8 encoded string).

Contains one or more identifiers of DB clusters that are Read Replicas
of this DB instance.

- **ReadReplicaDBInstanceIdentifiers** – This is a String, of type: `string` (a UTF-8 encoded string).

Contains one or more identifiers of the Read Replicas associated with
this DB instance.

- **ReadReplicaSourceDBInstanceIdentifier** – This is a String, of type: `string` (a UTF-8 encoded string).

Contains the identifier of the source DB instance if this DB instance is
a Read Replica.

- **SecondaryAvailabilityZone** – This is a String, of type: `string` (a UTF-8 encoded string).

If present, specifies the name of the secondary Availability Zone for
a DB instance with multi-AZ support.

- **StatusInfos** – This is An array of [DBInstanceStatusInfo](#DBInstanceStatusInfo "#DBInstanceStatusInfo") objects.

The status of a Read Replica. If the instance is not a Read Replica, this
is blank.

- **StorageEncrypted** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Not supported: The encryption for DB instances is managed by the DB cluster.

- **StorageType** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the storage type associated with the DB instance.

- **TdeCredentialArn** – This is a String, of type: `string` (a UTF-8 encoded string).

The ARN from the key store with which the instance is associated for TDE
encryption.

- **Timezone** – This is a String, of type: `string` (a UTF-8 encoded string).

Not supported.

- **VpcSecurityGroups** – This is An array of [VpcSecurityGroupMembership](api-datatypes.md#VpcSecurityGroupMembership "api-datatypes.md#VpcSecurityGroupMembership") objects.

Provides a list of VPC security group elements that the DB instance belongs
to.

`DBInstance` is used as the response element for:

- [CreateDBInstance](#CreateDBInstance "#CreateDBInstance")
- [DeleteDBInstance](#DeleteDBInstance "#DeleteDBInstance")
- [ModifyDBInstance](#ModifyDBInstance "#ModifyDBInstance")
- [RebootDBInstance](#RebootDBInstance "#RebootDBInstance")

## DBInstanceStatusInfo (structure)

Provides a list of status information for a DB instance.

###### Fields

- **Message** – This is a String, of type: `string` (a UTF-8 encoded string).

Details of the error if there is an error for the instance. If the instance
is not in an error state, this value is blank.

- **Normal** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Boolean value that is true if the instance is operating normally, or false
if the instance is in an error state.

- **Status** – This is a String, of type: `string` (a UTF-8 encoded string).

Status of the DB instance. For a StatusType of read replica, the values
can be replicating, error, stopped, or terminated.

- **StatusType** – This is a String, of type: `string` (a UTF-8 encoded string).

This value is currently "read replication."

## OrderableDBInstanceOption (structure)

Contains a list of available options for a DB instance.

This data type is used as a response element in the [DescribeOrderableDBInstanceOptions (action)](#DescribeOrderableDBInstanceOptions "#DescribeOrderableDBInstanceOptions") action.

###### Fields

- **AvailabilityZones** – This is An array of [AvailabilityZone](api-datatypes.md#AvailabilityZone "api-datatypes.md#AvailabilityZone") objects.

A list of Availability Zones for a DB instance.

- **DBInstanceClass** – This is a String, of type: `string` (a UTF-8 encoded string).

The DB instance class for a DB instance.

- **Engine** – This is a String, of type: `string` (a UTF-8 encoded string).

The engine type of a DB instance.

- **EngineVersion** – This is a String, of type: `string` (a UTF-8 encoded string).

The engine version of a DB instance.

- **LicenseModel** – This is a String, of type: `string` (a UTF-8 encoded string).

The license model for a DB instance.

- **MaxIopsPerDbInstance** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Maximum total provisioned IOPS for a DB instance.

- **MaxIopsPerGib** – This is a DoubleOptional, of type: `double` (a double-precisionn IEEE 754 floating-point number).

Maximum provisioned IOPS per GiB for a DB instance.

- **MaxStorageSize** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Maximum storage size for a DB instance.

- **MinIopsPerDbInstance** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Minimum total provisioned IOPS for a DB instance.

- **MinIopsPerGib** – This is a DoubleOptional, of type: `double` (a double-precisionn IEEE 754 floating-point number).

Minimum provisioned IOPS per GiB for a DB instance.

- **MinStorageSize** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Minimum storage size for a DB instance.

- **MultiAZCapable** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Indicates whether a DB instance is Multi-AZ capable.

- **ReadReplicaCapable** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Indicates whether a DB instance can have a Read Replica.

- **StorageType** – This is a String, of type: `string` (a UTF-8 encoded string).

Not applicable. In Neptune the storage type is managed at the DB Cluster
level.

- **SupportsEnhancedMonitoring** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Indicates whether a DB instance supports Enhanced Monitoring at intervals
from 1 to 60 seconds.

- **SupportsGlobalDatabases** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

A value that indicates whether you can use Neptune global databases with
a specific combination of other DB engine attributes.

- **SupportsIAMDatabaseAuthentication** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Indicates whether a DB instance supports IAM database authentication.

- **SupportsIops** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Indicates whether a DB instance supports provisioned IOPS.

- **SupportsStorageEncryption** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Indicates whether a DB instance supports encrypted storage.

- **Vpc** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Indicates whether a DB instance is in a VPC.

## PendingModifiedValues (structure)

This data type is used as a response element in the [ModifyDBInstance (action)](#ModifyDBInstance "#ModifyDBInstance") action.

###### Fields

- **AllocatedStorage** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Contains the new `AllocatedStorage` size for the DB instance
that will be applied or is currently being applied.

- **BackupRetentionPeriod** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the pending number of days for which automated backups are retained.

- **CACertificateIdentifier** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the identifier of the CA certificate for the DB instance.

- **DBInstanceClass** – This is a String, of type: `string` (a UTF-8 encoded string).

Contains the new `DBInstanceClass` for the DB instance that
will be applied or is currently being applied.

- **DBInstanceIdentifier** – This is a String, of type: `string` (a UTF-8 encoded string).

Contains the new `DBInstanceIdentifier` for the DB instance
that will be applied or is currently being applied.

- **DBSubnetGroupName** – This is a String, of type: `string` (a UTF-8 encoded string).

The new DB subnet group for the DB instance.

- **EngineVersion** – This is a String, of type: `string` (a UTF-8 encoded string).

Indicates the database engine version.

- **Iops** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the new Provisioned IOPS value for the DB instance that will
be applied or is currently being applied.

- **MultiAZ** – This is a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

- **PendingCloudwatchLogsExports** – This is A [PendingCloudwatchLogsExports](api-clusters.md#PendingCloudwatchLogsExports "api-clusters.md#PendingCloudwatchLogsExports") object.

This `PendingCloudwatchLogsExports` structure specifies
pending changes to which CloudWatch logs are enabled and which are disabled.

- **Port** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the pending port for the DB instance.

- **StorageType** – This is a String, of type: `string` (a UTF-8 encoded string).

Not applicable. In Neptune the storage type is managed at the DB Cluster
level.

## ValidStorageOptions (structure)

Not applicable. In Neptune the storage type is managed at the DB Cluster
level.

###### Fields

- **IopsToStorageRatio** – This is An array of [DoubleRange](api-datatypes.md#DoubleRange "api-datatypes.md#DoubleRange") objects.

Not applicable. In Neptune the storage type is managed at the DB Cluster
level.

- **ProvisionedIops** – This is An array of [Range](api-datatypes.md#Range "api-datatypes.md#Range") objects.

Not applicable. In Neptune the storage type is managed at the DB Cluster
level.

- **StorageSize** – This is An array of [Range](api-datatypes.md#Range "api-datatypes.md#Range") objects.

Not applicable. In Neptune the storage type is managed at the DB Cluster
level.

- **StorageType** – This is a String, of type: `string` (a UTF-8 encoded string).

Not applicable. In Neptune the storage type is managed at the DB Cluster
level.

## ValidDBInstanceModificationsMessage (structure)

Information about valid modifications that you can make to your DB instance.
Contains the result of a successful call to the [DescribeValidDBInstanceModifications (action)](#DescribeValidDBInstanceModifications "#DescribeValidDBInstanceModifications") action. You can use this information when you call [ModifyDBInstance (action)](#ModifyDBInstance "#ModifyDBInstance").

###### Fields

- **Storage** – This is An array of [ValidStorageOptions](#ValidStorageOptions "#ValidStorageOptions") objects.

Valid storage options for your DB instance.

`ValidDBInstanceModificationsMessage` is used as the response element for:

- [DescribeValidDBInstanceModifications](#DescribeValidDBInstanceModifications "#DescribeValidDBInstanceModifications")
