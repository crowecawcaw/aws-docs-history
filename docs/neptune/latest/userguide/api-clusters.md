# Neptune DB Clusters API

**Actions:**

- [CreateDBCluster (action)](#CreateDBCluster "#CreateDBCluster")
- [DeleteDBCluster (action)](#DeleteDBCluster "#DeleteDBCluster")
- [ModifyDBCluster (action)](#ModifyDBCluster "#ModifyDBCluster")
- [StartDBCluster (action)](#StartDBCluster "#StartDBCluster")
- [StopDBCluster (action)](#StopDBCluster "#StopDBCluster")
- [AddRoleToDBCluster (action)](#AddRoleToDBCluster "#AddRoleToDBCluster")
- [RemoveRoleFromDBCluster (action)](#RemoveRoleFromDBCluster "#RemoveRoleFromDBCluster")
- [FailoverDBCluster (action)](#FailoverDBCluster "#FailoverDBCluster")
- [PromoteReadReplicaDBCluster (action)](#PromoteReadReplicaDBCluster "#PromoteReadReplicaDBCluster")
- [DescribeDBClusters (action)](#DescribeDBClusters "#DescribeDBClusters")
  **Structures:**

- [DBCluster (structure)](#DBCluster "#DBCluster")
- [DBClusterMember (structure)](#DBClusterMember "#DBClusterMember")
- [DBClusterRole (structure)](#DBClusterRole "#DBClusterRole")
- [CloudwatchLogsExportConfiguration (structure)](#CloudwatchLogsExportConfiguration "#CloudwatchLogsExportConfiguration")
- [PendingCloudwatchLogsExports (structure)](#PendingCloudwatchLogsExports "#PendingCloudwatchLogsExports")
- [ClusterPendingModifiedValues (structure)](#ClusterPendingModifiedValues "#ClusterPendingModifiedValues")

## CreateDBCluster (action)

        The AWS CLI name for this API is: `create-db-cluster`.

Creates a new Amazon Neptune DB cluster.

You can use the `ReplicationSourceIdentifier` parameter
to create the DB cluster as a Read Replica of another DB cluster or Amazon Neptune
DB instance.

Note that when you create a new cluster using `CreateDBCluster`
directly, deletion protection is disabled by default (when you create a new production
cluster in the console, deletion protection is enabled by default). You can only
delete a DB cluster if its `DeletionProtection` field is set to `false`.

**Request**

- **AvailabilityZones**  (in the CLI: `--availability-zones`) –  a String, of type: `string` (a UTF-8 encoded string).

A list of EC2 Availability Zones that instances in the DB cluster can be
created in.

- **BackupRetentionPeriod**  (in the CLI: `--backup-retention-period`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The number of days for which automated backups are retained. You must specify
a minimum value of 1.

Default: 1

Constraints:

    + Must be a value from 1 to 35

- **CopyTagsToSnapshot**  (in the CLI: `--copy-tags-to-snapshot`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

_If set to `true`, tags are copied to any snapshot
of the DB cluster that is created._

- **DatabaseName**  (in the CLI: `--database-name`) –  a String, of type: `string` (a UTF-8 encoded string).

The name for your database of up to 64 alpha-numeric characters. If you
do not provide a name, Amazon Neptune will not create a database in the DB cluster
you are creating.

- **DBClusterIdentifier**  (in the CLI: `--db-cluster-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The DB cluster identifier. This parameter is stored as a lowercase string.

Constraints:

    + Must contain from 1 to 63 letters, numbers, or hyphens.
    + First character must be a letter.
    + Cannot end with a hyphen or contain two consecutive hyphens.

Example: `my-cluster1`

- **DBClusterParameterGroupName**  (in the CLI: `--db-cluster-parameter-group-name`) –  a String, of type: `string` (a UTF-8 encoded string).

The name of the DB cluster parameter group to associate with this DB cluster.
If this argument is omitted, the default is used.

Constraints:

    + If supplied, must match the name of an existing DBClusterParameterGroup.

- **DBSubnetGroupName**  (in the CLI: `--db-subnet-group-name`) –  a String, of type: `string` (a UTF-8 encoded string).

A DB subnet group to associate with this DB cluster.

Constraints: Must match the name of an existing DBSubnetGroup. Must not
be default.

Example: `mySubnetgroup`

- **DeletionProtection**  (in the CLI: `--deletion-protection`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

A value that indicates whether the DB cluster has deletion protection
enabled. The database can't be deleted when deletion protection is enabled.
By default, deletion protection is enabled.

- **EnableCloudwatchLogsExports**  (in the CLI: `--enable-cloudwatch-logs-exports`) –  a String, of type: `string` (a UTF-8 encoded string).

A list of the log types that this DB cluster should export to CloudWatch
Logs. Valid log types are: `audit` (to publish audit logs) and `slowquery`
(to publish slow-query logs). See [Publishing
Neptune logs to Amazon CloudWatch logs](cloudwatch-logs.md "cloudwatch-logs.md").

- **EnableIAMDatabaseAuthentication**  (in the CLI: `--enable-iam-database-authentication`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

If set to `true`, enables Amazon Identity and Access Management
(IAM) authentication for the entire DB cluster (this cannot be set at an instance
level).

Default: `false`.

- **Engine**  (in the CLI: `--engine`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the database engine to be used for this DB cluster.

Valid Values: `neptune`

- **EngineVersion**  (in the CLI: `--engine-version`) –  a String, of type: `string` (a UTF-8 encoded string).

The version number of the database engine to use for the new DB cluster.

Example: `1.2.1.0`

- **GlobalClusterIdentifier**  (in the CLI: `--global-cluster-identifier`) –  a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

The ID of the Neptune global database to which this new DB cluster should
be added.

- **KmsKeyId**  (in the CLI: `--kms-key-id`) –  a String, of type: `string` (a UTF-8 encoded string).

The Amazon KMS key identifier for an encrypted DB cluster.

The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption
key. If you are creating a DB cluster with the same Amazon account that owns the
KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key
alias instead of the ARN for the KMS encryption key.

If an encryption key is not specified in `KmsKeyId`:

    + If `ReplicationSourceIdentifier` identifies an encrypted
     source, then Amazon Neptune will use the encryption key used to encrypt the source.
     Otherwise, Amazon Neptune will use your default encryption key.
    + If the `StorageEncrypted` parameter is true and `ReplicationSourceIdentifier`
     is not specified, then Amazon Neptune will use your default encryption key.

Amazon KMS creates the default encryption key for your Amazon account.
Your Amazon account has a different default encryption key for each Amazon Region.

If you create a Read Replica of an encrypted DB cluster in another Amazon
Region, you must set `KmsKeyId` to a KMS key ID that is valid in the
destination Amazon Region. This key is used to encrypt the Read Replica in that
Amazon Region.

- **Port**  (in the CLI: `--port`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The port number on which the instances in the DB cluster accept connections.

Default: `8182`

- **PreferredBackupWindow**  (in the CLI: `--preferred-backup-window`) –  a String, of type: `string` (a UTF-8 encoded string).

The daily time range during which automated backups are created if automated
backups are enabled using the `BackupRetentionPeriod` parameter.

The default is a 30-minute window selected at random from an 8-hour block
of time for each Amazon Region. To see the time blocks available, see [Neptune
Maintenance Window](manage-console-maintaining.md#manage-console-maintaining-window "manage-console-maintaining.md#manage-console-maintaining-window") in the _Amazon Neptune User Guide._

Constraints:

    + Must be in the format `hh24:mi-hh24:mi`.
    + Must be in Universal Coordinated Time (UTC).
    + Must not conflict with the preferred maintenance window.
    + Must be at least 30 minutes.

- **PreferredMaintenanceWindow**  (in the CLI: `--preferred-maintenance-window`) –  a String, of type: `string` (a UTF-8 encoded string).

The weekly time range during which system maintenance can occur, in Universal
Coordinated Time (UTC).

Format: `ddd:hh24:mi-ddd:hh24:mi`

The default is a 30-minute window selected at random from an 8-hour block
of time for each Amazon Region, occurring on a random day of the week. To see the
time blocks available, see [Neptune
Maintenance Window](manage-console-maintaining.md#manage-console-maintaining-window "manage-console-maintaining.md#manage-console-maintaining-window") in the _Amazon Neptune User Guide._

Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.

Constraints: Minimum 30-minute window.

- **PreSignedUrl**  (in the CLI: `--pre-signed-url`) –  a String, of type: `string` (a UTF-8 encoded string).

This parameter is not currently supported.

- **ReplicationSourceIdentifier**  (in the CLI: `--replication-source-identifier`) –  a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) of the source DB instance or DB cluster if
this DB cluster is created as a Read Replica.

- **ServerlessV2ScalingConfiguration**  (in the CLI: `--serverless-v2-scaling-configuration`) –  A [ServerlessV2ScalingConfiguration](api-datatypes.md#ServerlessV2ScalingConfiguration "api-datatypes.md#ServerlessV2ScalingConfiguration") object.

Contains the scaling configuration of a Neptune Serverless DB cluster.

For more information, see [Using
Amazon Neptune Serverless](neptune-serverless-using.md "neptune-serverless-using.md") in the _Amazon Neptune User Guide_.

- **StorageEncrypted**  (in the CLI: `--storage-encrypted`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster is encrypted.

- **StorageType**  (in the CLI: `--storage-type`) –  a String, of type: `string` (a UTF-8 encoded string).

The storage type for the new DB cluster.

Valid Values:

    + **`standard`**  
     –   ( *the default* ) Configures cost-effective
     database storage for applications with moderate to small I/O usage. When set
     to `standard`, the storage type is not returned in the response.
    + **`iopt1`**   –
       Enables [I/O-Optimized
     storage](storage-types.md#provisioned-iops-storage "storage-types.md#provisioned-iops-storage") that's designed to meet the needs of I/O-intensive graph workloads
     that require predictable pricing with low I/O latency and consistent I/O throughput.


    Neptune I/O-Optimized storage is only available starting with engine
     release 1.3.0.0.

- **Tags**  (in the CLI: `--tags`) –  An array of [Tag](api-other-apis.md#Tag "api-other-apis.md#Tag") objects.

The tags to assign to the new DB cluster.

- **VpcSecurityGroupIds**  (in the CLI: `--vpc-security-group-ids`) –  a String, of type: `string` (a UTF-8 encoded string).

A list of EC2 VPC security groups to associate with this DB cluster.

**Response**

Contains the details of an Amazon Neptune DB cluster.

This data type is used as a response element in the [DescribeDBClusters (action)](#DescribeDBClusters "#DescribeDBClusters").

- **AllocatedStorage**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

`AllocatedStorage` always returns 1, because Neptune DB
cluster storage size is not fixed, but instead automatically adjusts as needed.

- **AssociatedRoles**   – An array of [DBClusterRole](#DBClusterRole "#DBClusterRole") objects.

Provides a list of the Amazon Identity and Access Management (IAM) roles
that are associated with the DB cluster. IAM roles that are associated with a DB
cluster grant permission for the DB cluster to access other Amazon services on
your behalf.

- **AutomaticRestartTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Time at which the DB cluster will be automatically restarted.

- **AvailabilityZones**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the list of EC2 Availability Zones that instances in the DB cluster
can be created in.

- **BacktrackConsumedChangeRecords**   – a LongOptional, of type: `long` (a signed 64-bit integer).

Not supported by Neptune.

- **BacktrackWindow**   – a LongOptional, of type: `long` (a signed 64-bit integer).

Not supported by Neptune.

- **BackupRetentionPeriod**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the number of days for which automatic DB snapshots are retained.

- **Capacity**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Not supported by Neptune.

- **CloneGroupId**   – a String, of type: `string` (a UTF-8 encoded string).

Identifies the clone group to which the DB cluster is associated.

- **ClusterCreateTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the time when the DB cluster was created, in Universal Coordinated
Time (UTC).

- **CopyTagsToSnapshot**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

_If set to `true`, tags are copied to any snapshot
of the DB cluster that is created._

- **CrossAccountClone**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

If set to `true`, the DB cluster can be cloned across accounts.

- **DatabaseName**   – a String, of type: `string` (a UTF-8 encoded string).

Contains the name of the initial database of this DB cluster that was provided
at create time, if one was specified when the DB cluster was created. This same
name is returned for the life of the DB cluster.

- **DBClusterArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB cluster.

- **DBClusterIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Contains a user-supplied DB cluster identifier. This identifier is the
unique key that identifies a DB cluster.

- **DBClusterMembers**   – An array of [DBClusterMember](#DBClusterMember "#DBClusterMember") objects.

Provides the list of instances that make up the DB cluster.

- **DBClusterParameterGroup**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the DB cluster parameter group for the DB cluster.

- **DbClusterResourceId**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Region-unique, immutable identifier for the DB cluster. This
identifier is found in Amazon CloudTrail log entries whenever the Amazon KMS
key for the DB cluster is accessed.

- **DBSubnetGroup**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies information on the subnet group associated with the DB cluster,
including the name, description, and subnets in the subnet group.

- **DeletionProtection**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Indicates whether or not the DB cluster has deletion protection enabled.
The database can't be deleted when deletion protection is enabled.

- **EarliestBacktrackTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Not supported by Neptune.

- **EarliestRestorableTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the earliest time to which a database can be restored with point-in-time
restore.

- **EnabledCloudwatchLogsExports**   – a String, of type: `string` (a UTF-8 encoded string).

A list of the log types that this DB cluster is configured to export to CloudWatch
Logs. Valid log types are: `audit` (to publish audit logs to CloudWatch)
and slowquery (to publish slow-query logs to CloudWatch). See [Publishing Neptune
logs to Amazon CloudWatch logs](cloudwatch-logs.md "cloudwatch-logs.md").

- **Endpoint**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the connection endpoint for the primary instance of the DB cluster.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the database engine to be used for this DB cluster.

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

Indicates the database engine version.

- **GlobalClusterIdentifier**   – a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

Contains a user-supplied global database cluster identifier. This identifier
is the unique key that identifies a global database.

- **HostedZoneId**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

- **IAMDatabaseAuthenticationEnabled**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

True if mapping of Amazon Identity and Access Management (IAM) accounts
to database accounts is enabled, and otherwise false.

- **IOOptimizedNextAllowedModificationTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

The next time you can modify the DB cluster to use the `iopt1`
storage type.

- **KmsKeyId**   – a String, of type: `string` (a UTF-8 encoded string).

If `StorageEncrypted` is true, the Amazon KMS key identifier
for the encrypted DB cluster.

- **LatestRestorableTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the latest time to which a database can be restored with point-in-time
restore.

- **MultiAZ**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster has instances in multiple Availability
Zones.

- **PendingModifiedValues**   – A [ClusterPendingModifiedValues](#ClusterPendingModifiedValues "#ClusterPendingModifiedValues") object.

This data type is used as a response element in the `ModifyDBCluster`
operation and contains changes that will be applied during the next maintenance
window.

- **PercentProgress**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the progress of the operation as a percentage.

- **Port**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the port that the database engine is listening on.

- **PreferredBackupWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the daily time range during which automated backups are created
if automated backups are enabled, as determined by the `BackupRetentionPeriod`.

- **PreferredMaintenanceWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the weekly time range during which system maintenance can occur,
in Universal Coordinated Time (UTC).

- **ReaderEndpoint**   – a String, of type: `string` (a UTF-8 encoded string).

The reader endpoint for the DB cluster. The reader endpoint for a DB cluster
load-balances connections across the Read Replicas that are available in a DB
cluster. As clients request new connections to the reader endpoint, Neptune
distributes the connection requests among the Read Replicas in the DB cluster.
This functionality can help balance your read workload across multiple Read
Replicas in your DB cluster.

If a failover occurs, and the Read Replica that you are connected to is promoted
to be the primary instance, your connection is dropped. To continue sending your
read workload to other Read Replicas in the cluster, you can then reconnect to
the reader endpoint.

- **ReadReplicaIdentifiers**   – a String, of type: `string` (a UTF-8 encoded string).

Contains one or more identifiers of the Read Replicas associated with
this DB cluster.

- **ReplicationSourceIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported by Neptune.

- **ReplicationType**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported by Neptune.

- **ServerlessV2ScalingConfiguration**   – A [ServerlessV2ScalingConfigurationInfo](api-datatypes.md#ServerlessV2ScalingConfigurationInfo "api-datatypes.md#ServerlessV2ScalingConfigurationInfo") object.

Shows the scaling configuration for a Neptune Serverless DB cluster.

For more information, see [Using
Amazon Neptune Serverless](neptune-serverless-using.md "neptune-serverless-using.md") in the _Amazon Neptune User Guide_.

- **Status**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this DB cluster.

- **StorageEncrypted**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster is encrypted.

- **StorageType**   – a String, of type: `string` (a UTF-8 encoded string).

The storage type used by the DB cluster.

Valid Values:

    + **`standard`**  
     –   ( *the default* ) Provides cost-effective
     database storage for applications with moderate to small I/O usage.
    + **`iopt1`**   –
       Enables [I/O-Optimized
     storage](storage-types.md#provisioned-iops-storage "storage-types.md#provisioned-iops-storage") that's designed to meet the needs of I/O-intensive graph workloads
     that require predictable pricing with low I/O latency and consistent I/O throughput.


    Neptune I/O-Optimized storage is only available starting with engine
     release 1.3.0.0.

- **VpcSecurityGroups**   – An array of [VpcSecurityGroupMembership](api-datatypes.md#VpcSecurityGroupMembership "api-datatypes.md#VpcSecurityGroupMembership") objects.

Provides a list of VPC security groups that the DB cluster belongs to.

###### Errors

- [DBClusterAlreadyExistsFault](api-faults.md#DBClusterAlreadyExistsFault "api-faults.md#DBClusterAlreadyExistsFault")
- [InsufficientStorageClusterCapacityFault](api-faults.md#InsufficientStorageClusterCapacityFault "api-faults.md#InsufficientStorageClusterCapacityFault")
- [DBClusterQuotaExceededFault](api-faults.md#DBClusterQuotaExceededFault "api-faults.md#DBClusterQuotaExceededFault")
- [StorageQuotaExceededFault](api-faults.md#StorageQuotaExceededFault "api-faults.md#StorageQuotaExceededFault")
- [DBSubnetGroupNotFoundFault](api-faults.md#DBSubnetGroupNotFoundFault "api-faults.md#DBSubnetGroupNotFoundFault")
- [InvalidVPCNetworkStateFault](api-faults.md#InvalidVPCNetworkStateFault "api-faults.md#InvalidVPCNetworkStateFault")
- [InvalidDBClusterStateFault](api-faults.md#InvalidDBClusterStateFault "api-faults.md#InvalidDBClusterStateFault")
- [InvalidDBSubnetGroupStateFault](api-faults.md#InvalidDBSubnetGroupStateFault "api-faults.md#InvalidDBSubnetGroupStateFault")
- [InvalidSubnet](api-faults.md#InvalidSubnet "api-faults.md#InvalidSubnet")
- [InvalidDBInstanceStateFault](api-faults.md#InvalidDBInstanceStateFault "api-faults.md#InvalidDBInstanceStateFault")
- [DBClusterParameterGroupNotFoundFault](api-faults.md#DBClusterParameterGroupNotFoundFault "api-faults.md#DBClusterParameterGroupNotFoundFault")
- [KMSKeyNotAccessibleFault](api-faults.md#KMSKeyNotAccessibleFault "api-faults.md#KMSKeyNotAccessibleFault")
- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")
- [DBInstanceNotFoundFault](api-faults.md#DBInstanceNotFoundFault "api-faults.md#DBInstanceNotFoundFault")
- [DBSubnetGroupDoesNotCoverEnoughAZs](api-faults.md#DBSubnetGroupDoesNotCoverEnoughAZs "api-faults.md#DBSubnetGroupDoesNotCoverEnoughAZs")
- [GlobalClusterNotFoundFault](api-faults.md#GlobalClusterNotFoundFault "api-faults.md#GlobalClusterNotFoundFault")
- [InvalidGlobalClusterStateFault](api-faults.md#InvalidGlobalClusterStateFault "api-faults.md#InvalidGlobalClusterStateFault")

## DeleteDBCluster (action)

        The AWS CLI name for this API is: `delete-db-cluster`.

The DeleteDBCluster action deletes a previously provisioned DB cluster.
When you delete a DB cluster, all automated backups for that DB cluster are deleted
and can't be recovered. Manual DB cluster snapshots of the specified DB cluster
are not deleted.

Note that the DB Cluster cannot be deleted if deletion protection is enabled.
To delete it, you must first set its `DeletionProtection` field
to `False`.

**Request**

- **DBClusterIdentifier**  (in the CLI: `--db-cluster-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The DB cluster identifier for the DB cluster to be deleted. This parameter
isn't case-sensitive.

Constraints:

    + Must match an existing DBClusterIdentifier.

- **FinalDBSnapshotIdentifier**  (in the CLI: `--final-db-snapshot-identifier`) –  a String, of type: `string` (a UTF-8 encoded string).

The DB cluster snapshot identifier of the new DB cluster snapshot created
when `SkipFinalSnapshot` is set to `false`.

###### Note

Specifying this parameter and also setting the `SkipFinalShapshot`
parameter to true results in an error.

Constraints:

    + Must be 1 to 255 letters, numbers, or hyphens.
    + First character must be a letter
    + Cannot end with a hyphen or contain two consecutive hyphens

- **SkipFinalSnapshot**  (in the CLI: `--skip-final-snapshot`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

Determines whether a final DB cluster snapshot is created before the DB
cluster is deleted. If `true` is specified, no DB cluster snapshot
is created. If `false` is specified, a DB cluster snapshot is created
before the DB cluster is deleted.

###### Note

You must specify a `FinalDBSnapshotIdentifier` parameter
if `SkipFinalSnapshot` is `false`.

Default: `false`

**Response**

Contains the details of an Amazon Neptune DB cluster.

This data type is used as a response element in the [DescribeDBClusters (action)](#DescribeDBClusters "#DescribeDBClusters").

- **AllocatedStorage**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

`AllocatedStorage` always returns 1, because Neptune DB
cluster storage size is not fixed, but instead automatically adjusts as needed.

- **AssociatedRoles**   – An array of [DBClusterRole](#DBClusterRole "#DBClusterRole") objects.

Provides a list of the Amazon Identity and Access Management (IAM) roles
that are associated with the DB cluster. IAM roles that are associated with a DB
cluster grant permission for the DB cluster to access other Amazon services on
your behalf.

- **AutomaticRestartTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Time at which the DB cluster will be automatically restarted.

- **AvailabilityZones**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the list of EC2 Availability Zones that instances in the DB cluster
can be created in.

- **BacktrackConsumedChangeRecords**   – a LongOptional, of type: `long` (a signed 64-bit integer).

Not supported by Neptune.

- **BacktrackWindow**   – a LongOptional, of type: `long` (a signed 64-bit integer).

Not supported by Neptune.

- **BackupRetentionPeriod**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the number of days for which automatic DB snapshots are retained.

- **Capacity**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Not supported by Neptune.

- **CloneGroupId**   – a String, of type: `string` (a UTF-8 encoded string).

Identifies the clone group to which the DB cluster is associated.

- **ClusterCreateTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the time when the DB cluster was created, in Universal Coordinated
Time (UTC).

- **CopyTagsToSnapshot**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

_If set to `true`, tags are copied to any snapshot
of the DB cluster that is created._

- **CrossAccountClone**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

If set to `true`, the DB cluster can be cloned across accounts.

- **DatabaseName**   – a String, of type: `string` (a UTF-8 encoded string).

Contains the name of the initial database of this DB cluster that was provided
at create time, if one was specified when the DB cluster was created. This same
name is returned for the life of the DB cluster.

- **DBClusterArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB cluster.

- **DBClusterIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Contains a user-supplied DB cluster identifier. This identifier is the
unique key that identifies a DB cluster.

- **DBClusterMembers**   – An array of [DBClusterMember](#DBClusterMember "#DBClusterMember") objects.

Provides the list of instances that make up the DB cluster.

- **DBClusterParameterGroup**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the DB cluster parameter group for the DB cluster.

- **DbClusterResourceId**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Region-unique, immutable identifier for the DB cluster. This
identifier is found in Amazon CloudTrail log entries whenever the Amazon KMS
key for the DB cluster is accessed.

- **DBSubnetGroup**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies information on the subnet group associated with the DB cluster,
including the name, description, and subnets in the subnet group.

- **DeletionProtection**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Indicates whether or not the DB cluster has deletion protection enabled.
The database can't be deleted when deletion protection is enabled.

- **EarliestBacktrackTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Not supported by Neptune.

- **EarliestRestorableTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the earliest time to which a database can be restored with point-in-time
restore.

- **EnabledCloudwatchLogsExports**   – a String, of type: `string` (a UTF-8 encoded string).

A list of the log types that this DB cluster is configured to export to CloudWatch
Logs. Valid log types are: `audit` (to publish audit logs to CloudWatch)
and slowquery (to publish slow-query logs to CloudWatch). See [Publishing Neptune
logs to Amazon CloudWatch logs](cloudwatch-logs.md "cloudwatch-logs.md").

- **Endpoint**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the connection endpoint for the primary instance of the DB cluster.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the database engine to be used for this DB cluster.

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

Indicates the database engine version.

- **GlobalClusterIdentifier**   – a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

Contains a user-supplied global database cluster identifier. This identifier
is the unique key that identifies a global database.

- **HostedZoneId**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

- **IAMDatabaseAuthenticationEnabled**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

True if mapping of Amazon Identity and Access Management (IAM) accounts
to database accounts is enabled, and otherwise false.

- **IOOptimizedNextAllowedModificationTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

The next time you can modify the DB cluster to use the `iopt1`
storage type.

- **KmsKeyId**   – a String, of type: `string` (a UTF-8 encoded string).

If `StorageEncrypted` is true, the Amazon KMS key identifier
for the encrypted DB cluster.

- **LatestRestorableTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the latest time to which a database can be restored with point-in-time
restore.

- **MultiAZ**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster has instances in multiple Availability
Zones.

- **PendingModifiedValues**   – A [ClusterPendingModifiedValues](#ClusterPendingModifiedValues "#ClusterPendingModifiedValues") object.

This data type is used as a response element in the `ModifyDBCluster`
operation and contains changes that will be applied during the next maintenance
window.

- **PercentProgress**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the progress of the operation as a percentage.

- **Port**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the port that the database engine is listening on.

- **PreferredBackupWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the daily time range during which automated backups are created
if automated backups are enabled, as determined by the `BackupRetentionPeriod`.

- **PreferredMaintenanceWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the weekly time range during which system maintenance can occur,
in Universal Coordinated Time (UTC).

- **ReaderEndpoint**   – a String, of type: `string` (a UTF-8 encoded string).

The reader endpoint for the DB cluster. The reader endpoint for a DB cluster
load-balances connections across the Read Replicas that are available in a DB
cluster. As clients request new connections to the reader endpoint, Neptune
distributes the connection requests among the Read Replicas in the DB cluster.
This functionality can help balance your read workload across multiple Read
Replicas in your DB cluster.

If a failover occurs, and the Read Replica that you are connected to is promoted
to be the primary instance, your connection is dropped. To continue sending your
read workload to other Read Replicas in the cluster, you can then reconnect to
the reader endpoint.

- **ReadReplicaIdentifiers**   – a String, of type: `string` (a UTF-8 encoded string).

Contains one or more identifiers of the Read Replicas associated with
this DB cluster.

- **ReplicationSourceIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported by Neptune.

- **ReplicationType**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported by Neptune.

- **ServerlessV2ScalingConfiguration**   – A [ServerlessV2ScalingConfigurationInfo](api-datatypes.md#ServerlessV2ScalingConfigurationInfo "api-datatypes.md#ServerlessV2ScalingConfigurationInfo") object.

Shows the scaling configuration for a Neptune Serverless DB cluster.

For more information, see [Using
Amazon Neptune Serverless](neptune-serverless-using.md "neptune-serverless-using.md") in the _Amazon Neptune User Guide_.

- **Status**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this DB cluster.

- **StorageEncrypted**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster is encrypted.

- **StorageType**   – a String, of type: `string` (a UTF-8 encoded string).

The storage type used by the DB cluster.

Valid Values:

    + **`standard`**  
     –   ( *the default* ) Provides cost-effective
     database storage for applications with moderate to small I/O usage.
    + **`iopt1`**   –
       Enables [I/O-Optimized
     storage](storage-types.md#provisioned-iops-storage "storage-types.md#provisioned-iops-storage") that's designed to meet the needs of I/O-intensive graph workloads
     that require predictable pricing with low I/O latency and consistent I/O throughput.


    Neptune I/O-Optimized storage is only available starting with engine
     release 1.3.0.0.

- **VpcSecurityGroups**   – An array of [VpcSecurityGroupMembership](api-datatypes.md#VpcSecurityGroupMembership "api-datatypes.md#VpcSecurityGroupMembership") objects.

Provides a list of VPC security groups that the DB cluster belongs to.

###### Errors

- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")
- [InvalidDBClusterStateFault](api-faults.md#InvalidDBClusterStateFault "api-faults.md#InvalidDBClusterStateFault")
- [DBClusterSnapshotAlreadyExistsFault](api-faults.md#DBClusterSnapshotAlreadyExistsFault "api-faults.md#DBClusterSnapshotAlreadyExistsFault")
- [SnapshotQuotaExceededFault](api-faults.md#SnapshotQuotaExceededFault "api-faults.md#SnapshotQuotaExceededFault")
- [InvalidDBClusterSnapshotStateFault](api-faults.md#InvalidDBClusterSnapshotStateFault "api-faults.md#InvalidDBClusterSnapshotStateFault")

## ModifyDBCluster (action)

        The AWS CLI name for this API is: `modify-db-cluster`.

Modify a setting for a DB cluster. You can change one or more database configuration
parameters by specifying these parameters and the new values in the request.

**Request**

- **AllowMajorVersionUpgrade**  (in the CLI: `--allow-major-version-upgrade`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

A value that indicates whether upgrades between different major versions
are allowed.

Constraints: You must set the allow-major-version-upgrade flag when
providing an `EngineVersion` parameter that uses a different major
version than the DB cluster's current version.

- **ApplyImmediately**  (in the CLI: `--apply-immediately`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

A value that specifies whether the modifications in this request and any
pending modifications are asynchronously applied as soon as possible, regardless
of the `PreferredMaintenanceWindow` setting for the DB cluster.
If this parameter is set to `false`, changes to the DB cluster are
applied during the next maintenance window.

The `ApplyImmediately` parameter only affects `NewDBClusterIdentifier`
values. If you set the `ApplyImmediately` parameter value to false,
then changes to `NewDBClusterIdentifier` values are applied during
the next maintenance window. All other changes are applied immediately, regardless
of the value of the `ApplyImmediately` parameter.

Default: `false`

- **BackupRetentionPeriod**  (in the CLI: `--backup-retention-period`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The number of days for which automated backups are retained. You must specify
a minimum value of 1.

Default: 1

Constraints:

    + Must be a value from 1 to 35

- **CloudwatchLogsExportConfiguration**  (in the CLI: `--cloudwatch-logs-export-configuration`) –  A [CloudwatchLogsExportConfiguration](#CloudwatchLogsExportConfiguration "#CloudwatchLogsExportConfiguration") object.

The configuration setting for the log types to be enabled for export to
CloudWatch Logs for a specific DB cluster. See [Using
the CLI to publish Neptune audit logs to CloudWatch Logs](cloudwatch-logs.md#cloudwatch-logs-cli "cloudwatch-logs.md#cloudwatch-logs-cli").

- **CopyTagsToSnapshot**  (in the CLI: `--copy-tags-to-snapshot`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

_If set to `true`, tags are copied to any snapshot
of the DB cluster that is created._

- **DBClusterIdentifier**  (in the CLI: `--db-cluster-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The DB cluster identifier for the cluster being modified. This parameter
is not case-sensitive.

Constraints:

    + Must match the identifier of an existing DBCluster.

- **DBClusterParameterGroupName**  (in the CLI: `--db-cluster-parameter-group-name`) –  a String, of type: `string` (a UTF-8 encoded string).

The name of the DB cluster parameter group to use for the DB cluster.

- **DBInstanceParameterGroupName**  (in the CLI: `--db-instance-parameter-group-name`) –  a String, of type: `string` (a UTF-8 encoded string).

The name of the DB parameter group to apply to all instances of the DB cluster.

###### Note

When you apply a parameter group using `DBInstanceParameterGroupName`,
parameter changes aren't applied during the next maintenance window but instead
are applied immediately.

Default: The existing name setting

Constraints:

    + The DB parameter group must be in the same DB parameter group family as the
     target DB cluster version.
    + The `DBInstanceParameterGroupName` parameter is only
     valid in combination with the `AllowMajorVersionUpgrade` parameter.

- **DeletionProtection**  (in the CLI: `--deletion-protection`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

A value that indicates whether the DB cluster has deletion protection
enabled. The database can't be deleted when deletion protection is enabled.
By default, deletion protection is disabled.

- **EnableIAMDatabaseAuthentication**  (in the CLI: `--enable-iam-database-authentication`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

True to enable mapping of Amazon Identity and Access Management (IAM)
accounts to database accounts, and otherwise false.

Default: `false`

- **EngineVersion**  (in the CLI: `--engine-version`) –  a String, of type: `string` (a UTF-8 encoded string).

The version number of the database engine to which you want to upgrade.
Changing this parameter results in an outage. The change is applied during the
next maintenance window unless the `ApplyImmediately` parameter
is set to true.

For a list of valid engine versions, see [Engine Releases
for Amazon Neptune](engine-releases.md "engine-releases.md"), or call [DescribeDBEngineVersions (action)](api-other-apis.md#DescribeDBEngineVersions "api-other-apis.md#DescribeDBEngineVersions").

- **NewDBClusterIdentifier**  (in the CLI: `--new-db-cluster-identifier`) –  a String, of type: `string` (a UTF-8 encoded string).

The new DB cluster identifier for the DB cluster when renaming a DB cluster.
This value is stored as a lowercase string.

Constraints:

    + Must contain from 1 to 63 letters, numbers, or hyphens
    + The first character must be a letter
    + Cannot end with a hyphen or contain two consecutive hyphens

Example: `my-cluster2`

- **Port**  (in the CLI: `--port`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The port number on which the DB cluster accepts connections.

Constraints: Value must be `1150-65535`

Default: The same port as the original DB cluster.

- **PreferredBackupWindow**  (in the CLI: `--preferred-backup-window`) –  a String, of type: `string` (a UTF-8 encoded string).

The daily time range during which automated backups are created if automated
backups are enabled, using the `BackupRetentionPeriod` parameter.

The default is a 30-minute window selected at random from an 8-hour block
of time for each Amazon Region.

Constraints:

    + Must be in the format `hh24:mi-hh24:mi`.
    + Must be in Universal Coordinated Time (UTC).
    + Must not conflict with the preferred maintenance window.
    + Must be at least 30 minutes.

- **PreferredMaintenanceWindow**  (in the CLI: `--preferred-maintenance-window`) –  a String, of type: `string` (a UTF-8 encoded string).

The weekly time range during which system maintenance can occur, in Universal
Coordinated Time (UTC).

Format: `ddd:hh24:mi-ddd:hh24:mi`

The default is a 30-minute window selected at random from an 8-hour block
of time for each Amazon Region, occurring on a random day of the week.

Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.

Constraints: Minimum 30-minute window.

- **ServerlessV2ScalingConfiguration**  (in the CLI: `--serverless-v2-scaling-configuration`) –  A [ServerlessV2ScalingConfiguration](api-datatypes.md#ServerlessV2ScalingConfiguration "api-datatypes.md#ServerlessV2ScalingConfiguration") object.

Contains the scaling configuration of a Neptune Serverless DB cluster.

For more information, see [Using
Amazon Neptune Serverless](neptune-serverless-using.md "neptune-serverless-using.md") in the _Amazon Neptune User Guide_.

- **StorageType**  (in the CLI: `--storage-type`) –  a String, of type: `string` (a UTF-8 encoded string).

The storage type to associate with the DB cluster.

Valid Values:

    + **`standard`**  
     –   ( *the default* ) Configures cost-effective
     database storage for applications with moderate to small I/O usage.
    + **`iopt1`**   –
       Enables [I/O-Optimized
     storage](storage-types.md#provisioned-iops-storage "storage-types.md#provisioned-iops-storage") that's designed to meet the needs of I/O-intensive graph workloads
     that require predictable pricing with low I/O latency and consistent I/O throughput.


    Neptune I/O-Optimized storage is only available starting with engine
     release 1.3.0.0.

- **VpcSecurityGroupIds**  (in the CLI: `--vpc-security-group-ids`) –  a String, of type: `string` (a UTF-8 encoded string).

A list of VPC security groups that the DB cluster will belong to.

**Response**

Contains the details of an Amazon Neptune DB cluster.

This data type is used as a response element in the [DescribeDBClusters (action)](#DescribeDBClusters "#DescribeDBClusters").

- **AllocatedStorage**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

`AllocatedStorage` always returns 1, because Neptune DB
cluster storage size is not fixed, but instead automatically adjusts as needed.

- **AssociatedRoles**   – An array of [DBClusterRole](#DBClusterRole "#DBClusterRole") objects.

Provides a list of the Amazon Identity and Access Management (IAM) roles
that are associated with the DB cluster. IAM roles that are associated with a DB
cluster grant permission for the DB cluster to access other Amazon services on
your behalf.

- **AutomaticRestartTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Time at which the DB cluster will be automatically restarted.

- **AvailabilityZones**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the list of EC2 Availability Zones that instances in the DB cluster
can be created in.

- **BacktrackConsumedChangeRecords**   – a LongOptional, of type: `long` (a signed 64-bit integer).

Not supported by Neptune.

- **BacktrackWindow**   – a LongOptional, of type: `long` (a signed 64-bit integer).

Not supported by Neptune.

- **BackupRetentionPeriod**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the number of days for which automatic DB snapshots are retained.

- **Capacity**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Not supported by Neptune.

- **CloneGroupId**   – a String, of type: `string` (a UTF-8 encoded string).

Identifies the clone group to which the DB cluster is associated.

- **ClusterCreateTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the time when the DB cluster was created, in Universal Coordinated
Time (UTC).

- **CopyTagsToSnapshot**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

_If set to `true`, tags are copied to any snapshot
of the DB cluster that is created._

- **CrossAccountClone**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

If set to `true`, the DB cluster can be cloned across accounts.

- **DatabaseName**   – a String, of type: `string` (a UTF-8 encoded string).

Contains the name of the initial database of this DB cluster that was provided
at create time, if one was specified when the DB cluster was created. This same
name is returned for the life of the DB cluster.

- **DBClusterArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB cluster.

- **DBClusterIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Contains a user-supplied DB cluster identifier. This identifier is the
unique key that identifies a DB cluster.

- **DBClusterMembers**   – An array of [DBClusterMember](#DBClusterMember "#DBClusterMember") objects.

Provides the list of instances that make up the DB cluster.

- **DBClusterParameterGroup**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the DB cluster parameter group for the DB cluster.

- **DbClusterResourceId**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Region-unique, immutable identifier for the DB cluster. This
identifier is found in Amazon CloudTrail log entries whenever the Amazon KMS
key for the DB cluster is accessed.

- **DBSubnetGroup**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies information on the subnet group associated with the DB cluster,
including the name, description, and subnets in the subnet group.

- **DeletionProtection**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Indicates whether or not the DB cluster has deletion protection enabled.
The database can't be deleted when deletion protection is enabled.

- **EarliestBacktrackTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Not supported by Neptune.

- **EarliestRestorableTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the earliest time to which a database can be restored with point-in-time
restore.

- **EnabledCloudwatchLogsExports**   – a String, of type: `string` (a UTF-8 encoded string).

A list of the log types that this DB cluster is configured to export to CloudWatch
Logs. Valid log types are: `audit` (to publish audit logs to CloudWatch)
and slowquery (to publish slow-query logs to CloudWatch). See [Publishing Neptune
logs to Amazon CloudWatch logs](cloudwatch-logs.md "cloudwatch-logs.md").

- **Endpoint**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the connection endpoint for the primary instance of the DB cluster.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the database engine to be used for this DB cluster.

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

Indicates the database engine version.

- **GlobalClusterIdentifier**   – a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

Contains a user-supplied global database cluster identifier. This identifier
is the unique key that identifies a global database.

- **HostedZoneId**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

- **IAMDatabaseAuthenticationEnabled**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

True if mapping of Amazon Identity and Access Management (IAM) accounts
to database accounts is enabled, and otherwise false.

- **IOOptimizedNextAllowedModificationTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

The next time you can modify the DB cluster to use the `iopt1`
storage type.

- **KmsKeyId**   – a String, of type: `string` (a UTF-8 encoded string).

If `StorageEncrypted` is true, the Amazon KMS key identifier
for the encrypted DB cluster.

- **LatestRestorableTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the latest time to which a database can be restored with point-in-time
restore.

- **MultiAZ**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster has instances in multiple Availability
Zones.

- **PendingModifiedValues**   – A [ClusterPendingModifiedValues](#ClusterPendingModifiedValues "#ClusterPendingModifiedValues") object.

This data type is used as a response element in the `ModifyDBCluster`
operation and contains changes that will be applied during the next maintenance
window.

- **PercentProgress**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the progress of the operation as a percentage.

- **Port**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the port that the database engine is listening on.

- **PreferredBackupWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the daily time range during which automated backups are created
if automated backups are enabled, as determined by the `BackupRetentionPeriod`.

- **PreferredMaintenanceWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the weekly time range during which system maintenance can occur,
in Universal Coordinated Time (UTC).

- **ReaderEndpoint**   – a String, of type: `string` (a UTF-8 encoded string).

The reader endpoint for the DB cluster. The reader endpoint for a DB cluster
load-balances connections across the Read Replicas that are available in a DB
cluster. As clients request new connections to the reader endpoint, Neptune
distributes the connection requests among the Read Replicas in the DB cluster.
This functionality can help balance your read workload across multiple Read
Replicas in your DB cluster.

If a failover occurs, and the Read Replica that you are connected to is promoted
to be the primary instance, your connection is dropped. To continue sending your
read workload to other Read Replicas in the cluster, you can then reconnect to
the reader endpoint.

- **ReadReplicaIdentifiers**   – a String, of type: `string` (a UTF-8 encoded string).

Contains one or more identifiers of the Read Replicas associated with
this DB cluster.

- **ReplicationSourceIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported by Neptune.

- **ReplicationType**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported by Neptune.

- **ServerlessV2ScalingConfiguration**   – A [ServerlessV2ScalingConfigurationInfo](api-datatypes.md#ServerlessV2ScalingConfigurationInfo "api-datatypes.md#ServerlessV2ScalingConfigurationInfo") object.

Shows the scaling configuration for a Neptune Serverless DB cluster.

For more information, see [Using
Amazon Neptune Serverless](neptune-serverless-using.md "neptune-serverless-using.md") in the _Amazon Neptune User Guide_.

- **Status**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this DB cluster.

- **StorageEncrypted**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster is encrypted.

- **StorageType**   – a String, of type: `string` (a UTF-8 encoded string).

The storage type used by the DB cluster.

Valid Values:

    + **`standard`**  
     –   ( *the default* ) Provides cost-effective
     database storage for applications with moderate to small I/O usage.
    + **`iopt1`**   –
       Enables [I/O-Optimized
     storage](storage-types.md#provisioned-iops-storage "storage-types.md#provisioned-iops-storage") that's designed to meet the needs of I/O-intensive graph workloads
     that require predictable pricing with low I/O latency and consistent I/O throughput.


    Neptune I/O-Optimized storage is only available starting with engine
     release 1.3.0.0.

- **VpcSecurityGroups**   – An array of [VpcSecurityGroupMembership](api-datatypes.md#VpcSecurityGroupMembership "api-datatypes.md#VpcSecurityGroupMembership") objects.

Provides a list of VPC security groups that the DB cluster belongs to.

###### Errors

- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")
- [InvalidDBClusterStateFault](api-faults.md#InvalidDBClusterStateFault "api-faults.md#InvalidDBClusterStateFault")
- [StorageQuotaExceededFault](api-faults.md#StorageQuotaExceededFault "api-faults.md#StorageQuotaExceededFault")
- [DBSubnetGroupNotFoundFault](api-faults.md#DBSubnetGroupNotFoundFault "api-faults.md#DBSubnetGroupNotFoundFault")
- [InvalidVPCNetworkStateFault](api-faults.md#InvalidVPCNetworkStateFault "api-faults.md#InvalidVPCNetworkStateFault")
- [InvalidDBSubnetGroupStateFault](api-faults.md#InvalidDBSubnetGroupStateFault "api-faults.md#InvalidDBSubnetGroupStateFault")
- [InvalidSubnet](api-faults.md#InvalidSubnet "api-faults.md#InvalidSubnet")
- [DBClusterParameterGroupNotFoundFault](api-faults.md#DBClusterParameterGroupNotFoundFault "api-faults.md#DBClusterParameterGroupNotFoundFault")
- [InvalidDBSecurityGroupStateFault](api-faults.md#InvalidDBSecurityGroupStateFault "api-faults.md#InvalidDBSecurityGroupStateFault")
- [InvalidDBInstanceStateFault](api-faults.md#InvalidDBInstanceStateFault "api-faults.md#InvalidDBInstanceStateFault")
- [DBClusterAlreadyExistsFault](api-faults.md#DBClusterAlreadyExistsFault "api-faults.md#DBClusterAlreadyExistsFault")
- [StorageTypeNotSupportedFault](api-faults.md#StorageTypeNotSupportedFault "api-faults.md#StorageTypeNotSupportedFault")

## StartDBCluster (action)

        The AWS CLI name for this API is: `start-db-cluster`.

Starts an Amazon Neptune DB cluster that was stopped using the Amazon console,
the Amazon CLI stop-db-cluster command, or the StopDBCluster API.

**Request**

- **DBClusterIdentifier**  (in the CLI: `--db-cluster-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The DB cluster identifier of the Neptune DB cluster to be started. This
parameter is stored as a lowercase string.

**Response**

Contains the details of an Amazon Neptune DB cluster.

This data type is used as a response element in the [DescribeDBClusters (action)](#DescribeDBClusters "#DescribeDBClusters").

- **AllocatedStorage**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

`AllocatedStorage` always returns 1, because Neptune DB
cluster storage size is not fixed, but instead automatically adjusts as needed.

- **AssociatedRoles**   – An array of [DBClusterRole](#DBClusterRole "#DBClusterRole") objects.

Provides a list of the Amazon Identity and Access Management (IAM) roles
that are associated with the DB cluster. IAM roles that are associated with a DB
cluster grant permission for the DB cluster to access other Amazon services on
your behalf.

- **AutomaticRestartTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Time at which the DB cluster will be automatically restarted.

- **AvailabilityZones**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the list of EC2 Availability Zones that instances in the DB cluster
can be created in.

- **BacktrackConsumedChangeRecords**   – a LongOptional, of type: `long` (a signed 64-bit integer).

Not supported by Neptune.

- **BacktrackWindow**   – a LongOptional, of type: `long` (a signed 64-bit integer).

Not supported by Neptune.

- **BackupRetentionPeriod**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the number of days for which automatic DB snapshots are retained.

- **Capacity**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Not supported by Neptune.

- **CloneGroupId**   – a String, of type: `string` (a UTF-8 encoded string).

Identifies the clone group to which the DB cluster is associated.

- **ClusterCreateTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the time when the DB cluster was created, in Universal Coordinated
Time (UTC).

- **CopyTagsToSnapshot**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

_If set to `true`, tags are copied to any snapshot
of the DB cluster that is created._

- **CrossAccountClone**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

If set to `true`, the DB cluster can be cloned across accounts.

- **DatabaseName**   – a String, of type: `string` (a UTF-8 encoded string).

Contains the name of the initial database of this DB cluster that was provided
at create time, if one was specified when the DB cluster was created. This same
name is returned for the life of the DB cluster.

- **DBClusterArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB cluster.

- **DBClusterIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Contains a user-supplied DB cluster identifier. This identifier is the
unique key that identifies a DB cluster.

- **DBClusterMembers**   – An array of [DBClusterMember](#DBClusterMember "#DBClusterMember") objects.

Provides the list of instances that make up the DB cluster.

- **DBClusterParameterGroup**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the DB cluster parameter group for the DB cluster.

- **DbClusterResourceId**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Region-unique, immutable identifier for the DB cluster. This
identifier is found in Amazon CloudTrail log entries whenever the Amazon KMS
key for the DB cluster is accessed.

- **DBSubnetGroup**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies information on the subnet group associated with the DB cluster,
including the name, description, and subnets in the subnet group.

- **DeletionProtection**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Indicates whether or not the DB cluster has deletion protection enabled.
The database can't be deleted when deletion protection is enabled.

- **EarliestBacktrackTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Not supported by Neptune.

- **EarliestRestorableTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the earliest time to which a database can be restored with point-in-time
restore.

- **EnabledCloudwatchLogsExports**   – a String, of type: `string` (a UTF-8 encoded string).

A list of the log types that this DB cluster is configured to export to CloudWatch
Logs. Valid log types are: `audit` (to publish audit logs to CloudWatch)
and slowquery (to publish slow-query logs to CloudWatch). See [Publishing Neptune
logs to Amazon CloudWatch logs](cloudwatch-logs.md "cloudwatch-logs.md").

- **Endpoint**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the connection endpoint for the primary instance of the DB cluster.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the database engine to be used for this DB cluster.

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

Indicates the database engine version.

- **GlobalClusterIdentifier**   – a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

Contains a user-supplied global database cluster identifier. This identifier
is the unique key that identifies a global database.

- **HostedZoneId**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

- **IAMDatabaseAuthenticationEnabled**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

True if mapping of Amazon Identity and Access Management (IAM) accounts
to database accounts is enabled, and otherwise false.

- **IOOptimizedNextAllowedModificationTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

The next time you can modify the DB cluster to use the `iopt1`
storage type.

- **KmsKeyId**   – a String, of type: `string` (a UTF-8 encoded string).

If `StorageEncrypted` is true, the Amazon KMS key identifier
for the encrypted DB cluster.

- **LatestRestorableTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the latest time to which a database can be restored with point-in-time
restore.

- **MultiAZ**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster has instances in multiple Availability
Zones.

- **PendingModifiedValues**   – A [ClusterPendingModifiedValues](#ClusterPendingModifiedValues "#ClusterPendingModifiedValues") object.

This data type is used as a response element in the `ModifyDBCluster`
operation and contains changes that will be applied during the next maintenance
window.

- **PercentProgress**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the progress of the operation as a percentage.

- **Port**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the port that the database engine is listening on.

- **PreferredBackupWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the daily time range during which automated backups are created
if automated backups are enabled, as determined by the `BackupRetentionPeriod`.

- **PreferredMaintenanceWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the weekly time range during which system maintenance can occur,
in Universal Coordinated Time (UTC).

- **ReaderEndpoint**   – a String, of type: `string` (a UTF-8 encoded string).

The reader endpoint for the DB cluster. The reader endpoint for a DB cluster
load-balances connections across the Read Replicas that are available in a DB
cluster. As clients request new connections to the reader endpoint, Neptune
distributes the connection requests among the Read Replicas in the DB cluster.
This functionality can help balance your read workload across multiple Read
Replicas in your DB cluster.

If a failover occurs, and the Read Replica that you are connected to is promoted
to be the primary instance, your connection is dropped. To continue sending your
read workload to other Read Replicas in the cluster, you can then reconnect to
the reader endpoint.

- **ReadReplicaIdentifiers**   – a String, of type: `string` (a UTF-8 encoded string).

Contains one or more identifiers of the Read Replicas associated with
this DB cluster.

- **ReplicationSourceIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported by Neptune.

- **ReplicationType**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported by Neptune.

- **ServerlessV2ScalingConfiguration**   – A [ServerlessV2ScalingConfigurationInfo](api-datatypes.md#ServerlessV2ScalingConfigurationInfo "api-datatypes.md#ServerlessV2ScalingConfigurationInfo") object.

Shows the scaling configuration for a Neptune Serverless DB cluster.

For more information, see [Using
Amazon Neptune Serverless](neptune-serverless-using.md "neptune-serverless-using.md") in the _Amazon Neptune User Guide_.

- **Status**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this DB cluster.

- **StorageEncrypted**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster is encrypted.

- **StorageType**   – a String, of type: `string` (a UTF-8 encoded string).

The storage type used by the DB cluster.

Valid Values:

    + **`standard`**  
     –   ( *the default* ) Provides cost-effective
     database storage for applications with moderate to small I/O usage.
    + **`iopt1`**   –
       Enables [I/O-Optimized
     storage](storage-types.md#provisioned-iops-storage "storage-types.md#provisioned-iops-storage") that's designed to meet the needs of I/O-intensive graph workloads
     that require predictable pricing with low I/O latency and consistent I/O throughput.


    Neptune I/O-Optimized storage is only available starting with engine
     release 1.3.0.0.

- **VpcSecurityGroups**   – An array of [VpcSecurityGroupMembership](api-datatypes.md#VpcSecurityGroupMembership "api-datatypes.md#VpcSecurityGroupMembership") objects.

Provides a list of VPC security groups that the DB cluster belongs to.

###### Errors

- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")
- [InvalidDBClusterStateFault](api-faults.md#InvalidDBClusterStateFault "api-faults.md#InvalidDBClusterStateFault")
- [InvalidDBInstanceStateFault](api-faults.md#InvalidDBInstanceStateFault "api-faults.md#InvalidDBInstanceStateFault")

## StopDBCluster (action)

        The AWS CLI name for this API is: `stop-db-cluster`.

Stops an Amazon Neptune DB cluster. When you stop a DB cluster, Neptune
retains the DB cluster's metadata, including its endpoints and DB parameter
groups.

Neptune also retains the transaction logs so you can do a point-in-time
restore if necessary.

**Request**

- **DBClusterIdentifier**  (in the CLI: `--db-cluster-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The DB cluster identifier of the Neptune DB cluster to be stopped. This
parameter is stored as a lowercase string.

**Response**

Contains the details of an Amazon Neptune DB cluster.

This data type is used as a response element in the [DescribeDBClusters (action)](#DescribeDBClusters "#DescribeDBClusters").

- **AllocatedStorage**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

`AllocatedStorage` always returns 1, because Neptune DB
cluster storage size is not fixed, but instead automatically adjusts as needed.

- **AssociatedRoles**   – An array of [DBClusterRole](#DBClusterRole "#DBClusterRole") objects.

Provides a list of the Amazon Identity and Access Management (IAM) roles
that are associated with the DB cluster. IAM roles that are associated with a DB
cluster grant permission for the DB cluster to access other Amazon services on
your behalf.

- **AutomaticRestartTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Time at which the DB cluster will be automatically restarted.

- **AvailabilityZones**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the list of EC2 Availability Zones that instances in the DB cluster
can be created in.

- **BacktrackConsumedChangeRecords**   – a LongOptional, of type: `long` (a signed 64-bit integer).

Not supported by Neptune.

- **BacktrackWindow**   – a LongOptional, of type: `long` (a signed 64-bit integer).

Not supported by Neptune.

- **BackupRetentionPeriod**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the number of days for which automatic DB snapshots are retained.

- **Capacity**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Not supported by Neptune.

- **CloneGroupId**   – a String, of type: `string` (a UTF-8 encoded string).

Identifies the clone group to which the DB cluster is associated.

- **ClusterCreateTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the time when the DB cluster was created, in Universal Coordinated
Time (UTC).

- **CopyTagsToSnapshot**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

_If set to `true`, tags are copied to any snapshot
of the DB cluster that is created._

- **CrossAccountClone**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

If set to `true`, the DB cluster can be cloned across accounts.

- **DatabaseName**   – a String, of type: `string` (a UTF-8 encoded string).

Contains the name of the initial database of this DB cluster that was provided
at create time, if one was specified when the DB cluster was created. This same
name is returned for the life of the DB cluster.

- **DBClusterArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB cluster.

- **DBClusterIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Contains a user-supplied DB cluster identifier. This identifier is the
unique key that identifies a DB cluster.

- **DBClusterMembers**   – An array of [DBClusterMember](#DBClusterMember "#DBClusterMember") objects.

Provides the list of instances that make up the DB cluster.

- **DBClusterParameterGroup**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the DB cluster parameter group for the DB cluster.

- **DbClusterResourceId**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Region-unique, immutable identifier for the DB cluster. This
identifier is found in Amazon CloudTrail log entries whenever the Amazon KMS
key for the DB cluster is accessed.

- **DBSubnetGroup**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies information on the subnet group associated with the DB cluster,
including the name, description, and subnets in the subnet group.

- **DeletionProtection**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Indicates whether or not the DB cluster has deletion protection enabled.
The database can't be deleted when deletion protection is enabled.

- **EarliestBacktrackTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Not supported by Neptune.

- **EarliestRestorableTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the earliest time to which a database can be restored with point-in-time
restore.

- **EnabledCloudwatchLogsExports**   – a String, of type: `string` (a UTF-8 encoded string).

A list of the log types that this DB cluster is configured to export to CloudWatch
Logs. Valid log types are: `audit` (to publish audit logs to CloudWatch)
and slowquery (to publish slow-query logs to CloudWatch). See [Publishing Neptune
logs to Amazon CloudWatch logs](cloudwatch-logs.md "cloudwatch-logs.md").

- **Endpoint**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the connection endpoint for the primary instance of the DB cluster.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the database engine to be used for this DB cluster.

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

Indicates the database engine version.

- **GlobalClusterIdentifier**   – a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

Contains a user-supplied global database cluster identifier. This identifier
is the unique key that identifies a global database.

- **HostedZoneId**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

- **IAMDatabaseAuthenticationEnabled**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

True if mapping of Amazon Identity and Access Management (IAM) accounts
to database accounts is enabled, and otherwise false.

- **IOOptimizedNextAllowedModificationTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

The next time you can modify the DB cluster to use the `iopt1`
storage type.

- **KmsKeyId**   – a String, of type: `string` (a UTF-8 encoded string).

If `StorageEncrypted` is true, the Amazon KMS key identifier
for the encrypted DB cluster.

- **LatestRestorableTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the latest time to which a database can be restored with point-in-time
restore.

- **MultiAZ**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster has instances in multiple Availability
Zones.

- **PendingModifiedValues**   – A [ClusterPendingModifiedValues](#ClusterPendingModifiedValues "#ClusterPendingModifiedValues") object.

This data type is used as a response element in the `ModifyDBCluster`
operation and contains changes that will be applied during the next maintenance
window.

- **PercentProgress**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the progress of the operation as a percentage.

- **Port**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the port that the database engine is listening on.

- **PreferredBackupWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the daily time range during which automated backups are created
if automated backups are enabled, as determined by the `BackupRetentionPeriod`.

- **PreferredMaintenanceWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the weekly time range during which system maintenance can occur,
in Universal Coordinated Time (UTC).

- **ReaderEndpoint**   – a String, of type: `string` (a UTF-8 encoded string).

The reader endpoint for the DB cluster. The reader endpoint for a DB cluster
load-balances connections across the Read Replicas that are available in a DB
cluster. As clients request new connections to the reader endpoint, Neptune
distributes the connection requests among the Read Replicas in the DB cluster.
This functionality can help balance your read workload across multiple Read
Replicas in your DB cluster.

If a failover occurs, and the Read Replica that you are connected to is promoted
to be the primary instance, your connection is dropped. To continue sending your
read workload to other Read Replicas in the cluster, you can then reconnect to
the reader endpoint.

- **ReadReplicaIdentifiers**   – a String, of type: `string` (a UTF-8 encoded string).

Contains one or more identifiers of the Read Replicas associated with
this DB cluster.

- **ReplicationSourceIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported by Neptune.

- **ReplicationType**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported by Neptune.

- **ServerlessV2ScalingConfiguration**   – A [ServerlessV2ScalingConfigurationInfo](api-datatypes.md#ServerlessV2ScalingConfigurationInfo "api-datatypes.md#ServerlessV2ScalingConfigurationInfo") object.

Shows the scaling configuration for a Neptune Serverless DB cluster.

For more information, see [Using
Amazon Neptune Serverless](neptune-serverless-using.md "neptune-serverless-using.md") in the _Amazon Neptune User Guide_.

- **Status**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this DB cluster.

- **StorageEncrypted**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster is encrypted.

- **StorageType**   – a String, of type: `string` (a UTF-8 encoded string).

The storage type used by the DB cluster.

Valid Values:

    + **`standard`**  
     –   ( *the default* ) Provides cost-effective
     database storage for applications with moderate to small I/O usage.
    + **`iopt1`**   –
       Enables [I/O-Optimized
     storage](storage-types.md#provisioned-iops-storage "storage-types.md#provisioned-iops-storage") that's designed to meet the needs of I/O-intensive graph workloads
     that require predictable pricing with low I/O latency and consistent I/O throughput.


    Neptune I/O-Optimized storage is only available starting with engine
     release 1.3.0.0.

- **VpcSecurityGroups**   – An array of [VpcSecurityGroupMembership](api-datatypes.md#VpcSecurityGroupMembership "api-datatypes.md#VpcSecurityGroupMembership") objects.

Provides a list of VPC security groups that the DB cluster belongs to.

###### Errors

- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")
- [InvalidDBClusterStateFault](api-faults.md#InvalidDBClusterStateFault "api-faults.md#InvalidDBClusterStateFault")
- [InvalidDBInstanceStateFault](api-faults.md#InvalidDBInstanceStateFault "api-faults.md#InvalidDBInstanceStateFault")

## AddRoleToDBCluster (action)

        The AWS CLI name for this API is: `add-role-to-db-cluster`.

Associates an Identity and Access Management (IAM) role with an Neptune
DB cluster.

**Request**

- **DBClusterIdentifier**  (in the CLI: `--db-cluster-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the DB cluster to associate the IAM role with.

- **FeatureName**  (in the CLI: `--feature-name`) –  a String, of type: `string` (a UTF-8 encoded string).

The name of the feature for the Neptune DB cluster that the IAM role is to
be associated with. For the list of supported feature names, see [DBEngineVersion (structure)](api-other-apis.md#DBEngineVersion "api-other-apis.md#DBEngineVersion").

- **RoleArn**  (in the CLI: `--role-arn`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) of the IAM role to associate with the Neptune
DB cluster, for example `arn:aws:iam::123456789012:role/NeptuneAccessRole`.

###### Response

- _No Response parameters._

###### Errors

- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")
- [DBClusterRoleAlreadyExistsFault](api-faults.md#DBClusterRoleAlreadyExistsFault "api-faults.md#DBClusterRoleAlreadyExistsFault")
- [InvalidDBClusterStateFault](api-faults.md#InvalidDBClusterStateFault "api-faults.md#InvalidDBClusterStateFault")
- [DBClusterRoleQuotaExceededFault](api-faults.md#DBClusterRoleQuotaExceededFault "api-faults.md#DBClusterRoleQuotaExceededFault")

## RemoveRoleFromDBCluster (action)

        The AWS CLI name for this API is: `remove-role-from-db-cluster`.

Disassociates an Identity and Access Management (IAM) role from a DB cluster.

**Request**

- **DBClusterIdentifier**  (in the CLI: `--db-cluster-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the DB cluster to disassociate the IAM role from.

- **FeatureName**  (in the CLI: `--feature-name`) –  a String, of type: `string` (a UTF-8 encoded string).

The name of the feature for the DB cluster that the IAM role is to be disassociated
from. For the list of supported feature names, see [DescribeDBEngineVersions (action)](api-other-apis.md#DescribeDBEngineVersions "api-other-apis.md#DescribeDBEngineVersions").

- **RoleArn**  (in the CLI: `--role-arn`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) of the IAM role to disassociate from the
DB cluster, for example `arn:aws:iam::123456789012:role/NeptuneAccessRole`.

###### Response

- _No Response parameters._

###### Errors

- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")
- [DBClusterRoleNotFoundFault](api-faults.md#DBClusterRoleNotFoundFault "api-faults.md#DBClusterRoleNotFoundFault")
- [InvalidDBClusterStateFault](api-faults.md#InvalidDBClusterStateFault "api-faults.md#InvalidDBClusterStateFault")

## FailoverDBCluster (action)

        The AWS CLI name for this API is: `failover-db-cluster`.

Forces a failover for a DB cluster.

A failover for a DB cluster promotes one of the Read Replicas (read-only
instances) in the DB cluster to be the primary instance (the cluster writer).

Amazon Neptune will automatically fail over to a Read Replica, if one exists,
when the primary instance fails. You can force a failover when you want to simulate
a failure of a primary instance for testing. Because each instance in a DB cluster
has its own endpoint address, you will need to clean up and re-establish any existing
connections that use those endpoint addresses when the failover is complete.

**Request**

- **DBClusterIdentifier**  (in the CLI: `--db-cluster-identifier`) –  a String, of type: `string` (a UTF-8 encoded string).

A DB cluster identifier to force a failover for. This parameter is not case-sensitive.

Constraints:

    + Must match the identifier of an existing DBCluster.

- **TargetDBInstanceIdentifier**  (in the CLI: `--target-db-instance-identifier`) –  a String, of type: `string` (a UTF-8 encoded string).

The name of the instance to promote to the primary instance.

You must specify the instance identifier for an Read Replica in the DB cluster.
For example, `mydbcluster-replica1`.

**Response**

Contains the details of an Amazon Neptune DB cluster.

This data type is used as a response element in the [DescribeDBClusters (action)](#DescribeDBClusters "#DescribeDBClusters").

- **AllocatedStorage**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

`AllocatedStorage` always returns 1, because Neptune DB
cluster storage size is not fixed, but instead automatically adjusts as needed.

- **AssociatedRoles**   – An array of [DBClusterRole](#DBClusterRole "#DBClusterRole") objects.

Provides a list of the Amazon Identity and Access Management (IAM) roles
that are associated with the DB cluster. IAM roles that are associated with a DB
cluster grant permission for the DB cluster to access other Amazon services on
your behalf.

- **AutomaticRestartTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Time at which the DB cluster will be automatically restarted.

- **AvailabilityZones**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the list of EC2 Availability Zones that instances in the DB cluster
can be created in.

- **BacktrackConsumedChangeRecords**   – a LongOptional, of type: `long` (a signed 64-bit integer).

Not supported by Neptune.

- **BacktrackWindow**   – a LongOptional, of type: `long` (a signed 64-bit integer).

Not supported by Neptune.

- **BackupRetentionPeriod**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the number of days for which automatic DB snapshots are retained.

- **Capacity**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Not supported by Neptune.

- **CloneGroupId**   – a String, of type: `string` (a UTF-8 encoded string).

Identifies the clone group to which the DB cluster is associated.

- **ClusterCreateTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the time when the DB cluster was created, in Universal Coordinated
Time (UTC).

- **CopyTagsToSnapshot**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

_If set to `true`, tags are copied to any snapshot
of the DB cluster that is created._

- **CrossAccountClone**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

If set to `true`, the DB cluster can be cloned across accounts.

- **DatabaseName**   – a String, of type: `string` (a UTF-8 encoded string).

Contains the name of the initial database of this DB cluster that was provided
at create time, if one was specified when the DB cluster was created. This same
name is returned for the life of the DB cluster.

- **DBClusterArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB cluster.

- **DBClusterIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Contains a user-supplied DB cluster identifier. This identifier is the
unique key that identifies a DB cluster.

- **DBClusterMembers**   – An array of [DBClusterMember](#DBClusterMember "#DBClusterMember") objects.

Provides the list of instances that make up the DB cluster.

- **DBClusterParameterGroup**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the DB cluster parameter group for the DB cluster.

- **DbClusterResourceId**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Region-unique, immutable identifier for the DB cluster. This
identifier is found in Amazon CloudTrail log entries whenever the Amazon KMS
key for the DB cluster is accessed.

- **DBSubnetGroup**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies information on the subnet group associated with the DB cluster,
including the name, description, and subnets in the subnet group.

- **DeletionProtection**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Indicates whether or not the DB cluster has deletion protection enabled.
The database can't be deleted when deletion protection is enabled.

- **EarliestBacktrackTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Not supported by Neptune.

- **EarliestRestorableTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the earliest time to which a database can be restored with point-in-time
restore.

- **EnabledCloudwatchLogsExports**   – a String, of type: `string` (a UTF-8 encoded string).

A list of the log types that this DB cluster is configured to export to CloudWatch
Logs. Valid log types are: `audit` (to publish audit logs to CloudWatch)
and slowquery (to publish slow-query logs to CloudWatch). See [Publishing Neptune
logs to Amazon CloudWatch logs](cloudwatch-logs.md "cloudwatch-logs.md").

- **Endpoint**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the connection endpoint for the primary instance of the DB cluster.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the database engine to be used for this DB cluster.

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

Indicates the database engine version.

- **GlobalClusterIdentifier**   – a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

Contains a user-supplied global database cluster identifier. This identifier
is the unique key that identifies a global database.

- **HostedZoneId**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

- **IAMDatabaseAuthenticationEnabled**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

True if mapping of Amazon Identity and Access Management (IAM) accounts
to database accounts is enabled, and otherwise false.

- **IOOptimizedNextAllowedModificationTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

The next time you can modify the DB cluster to use the `iopt1`
storage type.

- **KmsKeyId**   – a String, of type: `string` (a UTF-8 encoded string).

If `StorageEncrypted` is true, the Amazon KMS key identifier
for the encrypted DB cluster.

- **LatestRestorableTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the latest time to which a database can be restored with point-in-time
restore.

- **MultiAZ**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster has instances in multiple Availability
Zones.

- **PendingModifiedValues**   – A [ClusterPendingModifiedValues](#ClusterPendingModifiedValues "#ClusterPendingModifiedValues") object.

This data type is used as a response element in the `ModifyDBCluster`
operation and contains changes that will be applied during the next maintenance
window.

- **PercentProgress**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the progress of the operation as a percentage.

- **Port**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the port that the database engine is listening on.

- **PreferredBackupWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the daily time range during which automated backups are created
if automated backups are enabled, as determined by the `BackupRetentionPeriod`.

- **PreferredMaintenanceWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the weekly time range during which system maintenance can occur,
in Universal Coordinated Time (UTC).

- **ReaderEndpoint**   – a String, of type: `string` (a UTF-8 encoded string).

The reader endpoint for the DB cluster. The reader endpoint for a DB cluster
load-balances connections across the Read Replicas that are available in a DB
cluster. As clients request new connections to the reader endpoint, Neptune
distributes the connection requests among the Read Replicas in the DB cluster.
This functionality can help balance your read workload across multiple Read
Replicas in your DB cluster.

If a failover occurs, and the Read Replica that you are connected to is promoted
to be the primary instance, your connection is dropped. To continue sending your
read workload to other Read Replicas in the cluster, you can then reconnect to
the reader endpoint.

- **ReadReplicaIdentifiers**   – a String, of type: `string` (a UTF-8 encoded string).

Contains one or more identifiers of the Read Replicas associated with
this DB cluster.

- **ReplicationSourceIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported by Neptune.

- **ReplicationType**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported by Neptune.

- **ServerlessV2ScalingConfiguration**   – A [ServerlessV2ScalingConfigurationInfo](api-datatypes.md#ServerlessV2ScalingConfigurationInfo "api-datatypes.md#ServerlessV2ScalingConfigurationInfo") object.

Shows the scaling configuration for a Neptune Serverless DB cluster.

For more information, see [Using
Amazon Neptune Serverless](neptune-serverless-using.md "neptune-serverless-using.md") in the _Amazon Neptune User Guide_.

- **Status**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this DB cluster.

- **StorageEncrypted**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster is encrypted.

- **StorageType**   – a String, of type: `string` (a UTF-8 encoded string).

The storage type used by the DB cluster.

Valid Values:

    + **`standard`**  
     –   ( *the default* ) Provides cost-effective
     database storage for applications with moderate to small I/O usage.
    + **`iopt1`**   –
       Enables [I/O-Optimized
     storage](storage-types.md#provisioned-iops-storage "storage-types.md#provisioned-iops-storage") that's designed to meet the needs of I/O-intensive graph workloads
     that require predictable pricing with low I/O latency and consistent I/O throughput.


    Neptune I/O-Optimized storage is only available starting with engine
     release 1.3.0.0.

- **VpcSecurityGroups**   – An array of [VpcSecurityGroupMembership](api-datatypes.md#VpcSecurityGroupMembership "api-datatypes.md#VpcSecurityGroupMembership") objects.

Provides a list of VPC security groups that the DB cluster belongs to.

###### Errors

- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")
- [InvalidDBClusterStateFault](api-faults.md#InvalidDBClusterStateFault "api-faults.md#InvalidDBClusterStateFault")
- [InvalidDBInstanceStateFault](api-faults.md#InvalidDBInstanceStateFault "api-faults.md#InvalidDBInstanceStateFault")

## PromoteReadReplicaDBCluster (action)

        The AWS CLI name for this API is: `promote-read-replica-db-cluster`.

Not supported.

**Request**

- **DBClusterIdentifier**  (in the CLI: `--db-cluster-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

Not supported.

**Response**

Contains the details of an Amazon Neptune DB cluster.

This data type is used as a response element in the [DescribeDBClusters (action)](#DescribeDBClusters "#DescribeDBClusters").

- **AllocatedStorage**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

`AllocatedStorage` always returns 1, because Neptune DB
cluster storage size is not fixed, but instead automatically adjusts as needed.

- **AssociatedRoles**   – An array of [DBClusterRole](#DBClusterRole "#DBClusterRole") objects.

Provides a list of the Amazon Identity and Access Management (IAM) roles
that are associated with the DB cluster. IAM roles that are associated with a DB
cluster grant permission for the DB cluster to access other Amazon services on
your behalf.

- **AutomaticRestartTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Time at which the DB cluster will be automatically restarted.

- **AvailabilityZones**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the list of EC2 Availability Zones that instances in the DB cluster
can be created in.

- **BacktrackConsumedChangeRecords**   – a LongOptional, of type: `long` (a signed 64-bit integer).

Not supported by Neptune.

- **BacktrackWindow**   – a LongOptional, of type: `long` (a signed 64-bit integer).

Not supported by Neptune.

- **BackupRetentionPeriod**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the number of days for which automatic DB snapshots are retained.

- **Capacity**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Not supported by Neptune.

- **CloneGroupId**   – a String, of type: `string` (a UTF-8 encoded string).

Identifies the clone group to which the DB cluster is associated.

- **ClusterCreateTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the time when the DB cluster was created, in Universal Coordinated
Time (UTC).

- **CopyTagsToSnapshot**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

_If set to `true`, tags are copied to any snapshot
of the DB cluster that is created._

- **CrossAccountClone**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

If set to `true`, the DB cluster can be cloned across accounts.

- **DatabaseName**   – a String, of type: `string` (a UTF-8 encoded string).

Contains the name of the initial database of this DB cluster that was provided
at create time, if one was specified when the DB cluster was created. This same
name is returned for the life of the DB cluster.

- **DBClusterArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB cluster.

- **DBClusterIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Contains a user-supplied DB cluster identifier. This identifier is the
unique key that identifies a DB cluster.

- **DBClusterMembers**   – An array of [DBClusterMember](#DBClusterMember "#DBClusterMember") objects.

Provides the list of instances that make up the DB cluster.

- **DBClusterParameterGroup**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the DB cluster parameter group for the DB cluster.

- **DbClusterResourceId**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Region-unique, immutable identifier for the DB cluster. This
identifier is found in Amazon CloudTrail log entries whenever the Amazon KMS
key for the DB cluster is accessed.

- **DBSubnetGroup**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies information on the subnet group associated with the DB cluster,
including the name, description, and subnets in the subnet group.

- **DeletionProtection**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Indicates whether or not the DB cluster has deletion protection enabled.
The database can't be deleted when deletion protection is enabled.

- **EarliestBacktrackTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Not supported by Neptune.

- **EarliestRestorableTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the earliest time to which a database can be restored with point-in-time
restore.

- **EnabledCloudwatchLogsExports**   – a String, of type: `string` (a UTF-8 encoded string).

A list of the log types that this DB cluster is configured to export to CloudWatch
Logs. Valid log types are: `audit` (to publish audit logs to CloudWatch)
and slowquery (to publish slow-query logs to CloudWatch). See [Publishing Neptune
logs to Amazon CloudWatch logs](cloudwatch-logs.md "cloudwatch-logs.md").

- **Endpoint**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the connection endpoint for the primary instance of the DB cluster.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the database engine to be used for this DB cluster.

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

Indicates the database engine version.

- **GlobalClusterIdentifier**   – a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

Contains a user-supplied global database cluster identifier. This identifier
is the unique key that identifies a global database.

- **HostedZoneId**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

- **IAMDatabaseAuthenticationEnabled**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

True if mapping of Amazon Identity and Access Management (IAM) accounts
to database accounts is enabled, and otherwise false.

- **IOOptimizedNextAllowedModificationTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

The next time you can modify the DB cluster to use the `iopt1`
storage type.

- **KmsKeyId**   – a String, of type: `string` (a UTF-8 encoded string).

If `StorageEncrypted` is true, the Amazon KMS key identifier
for the encrypted DB cluster.

- **LatestRestorableTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the latest time to which a database can be restored with point-in-time
restore.

- **MultiAZ**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster has instances in multiple Availability
Zones.

- **PendingModifiedValues**   – A [ClusterPendingModifiedValues](#ClusterPendingModifiedValues "#ClusterPendingModifiedValues") object.

This data type is used as a response element in the `ModifyDBCluster`
operation and contains changes that will be applied during the next maintenance
window.

- **PercentProgress**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the progress of the operation as a percentage.

- **Port**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the port that the database engine is listening on.

- **PreferredBackupWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the daily time range during which automated backups are created
if automated backups are enabled, as determined by the `BackupRetentionPeriod`.

- **PreferredMaintenanceWindow**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the weekly time range during which system maintenance can occur,
in Universal Coordinated Time (UTC).

- **ReaderEndpoint**   – a String, of type: `string` (a UTF-8 encoded string).

The reader endpoint for the DB cluster. The reader endpoint for a DB cluster
load-balances connections across the Read Replicas that are available in a DB
cluster. As clients request new connections to the reader endpoint, Neptune
distributes the connection requests among the Read Replicas in the DB cluster.
This functionality can help balance your read workload across multiple Read
Replicas in your DB cluster.

If a failover occurs, and the Read Replica that you are connected to is promoted
to be the primary instance, your connection is dropped. To continue sending your
read workload to other Read Replicas in the cluster, you can then reconnect to
the reader endpoint.

- **ReadReplicaIdentifiers**   – a String, of type: `string` (a UTF-8 encoded string).

Contains one or more identifiers of the Read Replicas associated with
this DB cluster.

- **ReplicationSourceIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported by Neptune.

- **ReplicationType**   – a String, of type: `string` (a UTF-8 encoded string).

Not supported by Neptune.

- **ServerlessV2ScalingConfiguration**   – A [ServerlessV2ScalingConfigurationInfo](api-datatypes.md#ServerlessV2ScalingConfigurationInfo "api-datatypes.md#ServerlessV2ScalingConfigurationInfo") object.

Shows the scaling configuration for a Neptune Serverless DB cluster.

For more information, see [Using
Amazon Neptune Serverless](neptune-serverless-using.md "neptune-serverless-using.md") in the _Amazon Neptune User Guide_.

- **Status**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this DB cluster.

- **StorageEncrypted**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster is encrypted.

- **StorageType**   – a String, of type: `string` (a UTF-8 encoded string).

The storage type used by the DB cluster.

Valid Values:

    + **`standard`**  
     –   ( *the default* ) Provides cost-effective
     database storage for applications with moderate to small I/O usage.
    + **`iopt1`**   –
       Enables [I/O-Optimized
     storage](storage-types.md#provisioned-iops-storage "storage-types.md#provisioned-iops-storage") that's designed to meet the needs of I/O-intensive graph workloads
     that require predictable pricing with low I/O latency and consistent I/O throughput.


    Neptune I/O-Optimized storage is only available starting with engine
     release 1.3.0.0.

- **VpcSecurityGroups**   – An array of [VpcSecurityGroupMembership](api-datatypes.md#VpcSecurityGroupMembership "api-datatypes.md#VpcSecurityGroupMembership") objects.

Provides a list of VPC security groups that the DB cluster belongs to.

###### Errors

- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")
- [InvalidDBClusterStateFault](api-faults.md#InvalidDBClusterStateFault "api-faults.md#InvalidDBClusterStateFault")

## DescribeDBClusters (action)

        The AWS CLI name for this API is: `describe-db-clusters`.

Returns information about provisioned DB clusters, and supports pagination.

###### Note

This operation can also return information for Amazon RDS clusters and
Amazon DocDB clusters.

**Request**

- **DBClusterIdentifier**  (in the CLI: `--db-cluster-identifier`) –  a String, of type: `string` (a UTF-8 encoded string).

The user-supplied DB cluster identifier. If this parameter is specified,
information from only the specific DB cluster is returned. This parameter isn't
case-sensitive.

Constraints:

    + If supplied, must match an existing DBClusterIdentifier.

- **Filters**  (in the CLI: `--filters`) –  An array of [Filter](api-datatypes.md#Filter "api-datatypes.md#Filter") objects.

A filter that specifies one or more DB clusters to describe.

Supported filters:

    + `db-cluster-id` - Accepts DB cluster identifiers and DB
     cluster Amazon Resource Names (ARNs). The results list will only include information
     about the DB clusters identified by these ARNs.
    + `engine` - Accepts an engine name (such as `neptune`),
     and restricts the results list to DB clusters created by that engine.

For example, to invoke this API from the Amazon CLI and filter so that only
Neptune DB clusters are returned, you could use the following command:

###### Example

```
aws neptune describe-db-clusters \
            --filters  Name=engine,Values=neptune
```

- **Marker**  (in the CLI: `--marker`) –  a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous DescribeDBClusters (action) request. If this parameter is specified, the response includes only records
beyond the marker, up to the value specified by `MaxRecords`.

- **MaxRecords**  (in the CLI: `--max-records`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The maximum number of records to include in the response. If more records
exist than the specified `MaxRecords` value, a pagination token
called a marker is included in the response so that the remaining results can be
retrieved.

Default: 100

Constraints: Minimum 20, maximum 100.

**Response**

- **DBClusters**   – An array of [DBCluster](#DBCluster "#DBCluster") objects.

Contains a list of DB clusters for the user.

- **Marker**   – a String, of type: `string` (a UTF-8 encoded string).

A pagination token that can be used in a subsequent DescribeDBClusters
request.

###### Errors

- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")

## _Structures:_

## DBCluster (structure)

Contains the details of an Amazon Neptune DB cluster.

This data type is used as a response element in the [DescribeDBClusters (action)](#DescribeDBClusters "#DescribeDBClusters").

###### Fields

- **AllocatedStorage** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

`AllocatedStorage` always returns 1, because Neptune DB
cluster storage size is not fixed, but instead automatically adjusts as needed.

- **AssociatedRoles** – This is An array of [DBClusterRole](#DBClusterRole "#DBClusterRole") objects.

Provides a list of the Amazon Identity and Access Management (IAM) roles
that are associated with the DB cluster. IAM roles that are associated with a DB
cluster grant permission for the DB cluster to access other Amazon services on
your behalf.

- **AutomaticRestartTime** – This is a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Time at which the DB cluster will be automatically restarted.

- **AvailabilityZones** – This is a String, of type: `string` (a UTF-8 encoded string).

Provides the list of EC2 Availability Zones that instances in the DB cluster
can be created in.

- **BacktrackConsumedChangeRecords** – This is a LongOptional, of type: `long` (a signed 64-bit integer).

Not supported by Neptune.

- **BacktrackWindow** – This is a LongOptional, of type: `long` (a signed 64-bit integer).

Not supported by Neptune.

- **BackupRetentionPeriod** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the number of days for which automatic DB snapshots are retained.

- **Capacity** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Not supported by Neptune.

- **CloneGroupId** – This is a String, of type: `string` (a UTF-8 encoded string).

Identifies the clone group to which the DB cluster is associated.

- **ClusterCreateTime** – This is a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the time when the DB cluster was created, in Universal Coordinated
Time (UTC).

- **CopyTagsToSnapshot** – This is a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

_If set to `true`, tags are copied to any snapshot
of the DB cluster that is created._

- **CrossAccountClone** – This is a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

If set to `true`, the DB cluster can be cloned across accounts.

- **DatabaseName** – This is a String, of type: `string` (a UTF-8 encoded string).

Contains the name of the initial database of this DB cluster that was provided
at create time, if one was specified when the DB cluster was created. This same
name is returned for the life of the DB cluster.

- **DBClusterArn** – This is a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB cluster.

- **DBClusterIdentifier** – This is a String, of type: `string` (a UTF-8 encoded string).

Contains a user-supplied DB cluster identifier. This identifier is the
unique key that identifies a DB cluster.

- **DBClusterMembers** – This is An array of [DBClusterMember](#DBClusterMember "#DBClusterMember") objects.

Provides the list of instances that make up the DB cluster.

- **DBClusterParameterGroup** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the DB cluster parameter group for the DB cluster.

- **DbClusterResourceId** – This is a String, of type: `string` (a UTF-8 encoded string).

The Amazon Region-unique, immutable identifier for the DB cluster. This
identifier is found in Amazon CloudTrail log entries whenever the Amazon KMS
key for the DB cluster is accessed.

- **DBSubnetGroup** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies information on the subnet group associated with the DB cluster,
including the name, description, and subnets in the subnet group.

- **DeletionProtection** – This is a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Indicates whether or not the DB cluster has deletion protection enabled.
The database can't be deleted when deletion protection is enabled.

- **EarliestBacktrackTime** – This is a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Not supported by Neptune.

- **EarliestRestorableTime** – This is a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the earliest time to which a database can be restored with point-in-time
restore.

- **EnabledCloudwatchLogsExports** – This is a String, of type: `string` (a UTF-8 encoded string).

A list of the log types that this DB cluster is configured to export to CloudWatch
Logs. Valid log types are: `audit` (to publish audit logs to CloudWatch)
and slowquery (to publish slow-query logs to CloudWatch). See [Publishing Neptune
logs to Amazon CloudWatch logs](cloudwatch-logs.md "cloudwatch-logs.md").

- **Endpoint** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the connection endpoint for the primary instance of the DB cluster.

- **Engine** – This is a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the database engine to be used for this DB cluster.

- **EngineVersion** – This is a String, of type: `string` (a UTF-8 encoded string).

Indicates the database engine version.

- **GlobalClusterIdentifier** – This is a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

Contains a user-supplied global database cluster identifier. This identifier
is the unique key that identifies a global database.

- **HostedZoneId** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

- **IAMDatabaseAuthenticationEnabled** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

True if mapping of Amazon Identity and Access Management (IAM) accounts
to database accounts is enabled, and otherwise false.

- **IOOptimizedNextAllowedModificationTime** – This is a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

The next time you can modify the DB cluster to use the `iopt1`
storage type.

- **KmsKeyId** – This is a String, of type: `string` (a UTF-8 encoded string).

If `StorageEncrypted` is true, the Amazon KMS key identifier
for the encrypted DB cluster.

- **LatestRestorableTime** – This is a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the latest time to which a database can be restored with point-in-time
restore.

- **MultiAZ** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster has instances in multiple Availability
Zones.

- **PendingModifiedValues** – This is A [ClusterPendingModifiedValues](#ClusterPendingModifiedValues "#ClusterPendingModifiedValues") object.

This data type is used as a response element in the `ModifyDBCluster`
operation and contains changes that will be applied during the next maintenance
window.

- **PercentProgress** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the progress of the operation as a percentage.

- **Port** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

Specifies the port that the database engine is listening on.

- **PreferredBackupWindow** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the daily time range during which automated backups are created
if automated backups are enabled, as determined by the `BackupRetentionPeriod`.

- **PreferredMaintenanceWindow** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the weekly time range during which system maintenance can occur,
in Universal Coordinated Time (UTC).

- **ReaderEndpoint** – This is a String, of type: `string` (a UTF-8 encoded string).

The reader endpoint for the DB cluster. The reader endpoint for a DB cluster
load-balances connections across the Read Replicas that are available in a DB
cluster. As clients request new connections to the reader endpoint, Neptune
distributes the connection requests among the Read Replicas in the DB cluster.
This functionality can help balance your read workload across multiple Read
Replicas in your DB cluster.

If a failover occurs, and the Read Replica that you are connected to is promoted
to be the primary instance, your connection is dropped. To continue sending your
read workload to other Read Replicas in the cluster, you can then reconnect to
the reader endpoint.

- **ReadReplicaIdentifiers** – This is a String, of type: `string` (a UTF-8 encoded string).

Contains one or more identifiers of the Read Replicas associated with
this DB cluster.

- **ReplicationSourceIdentifier** – This is a String, of type: `string` (a UTF-8 encoded string).

Not supported by Neptune.

- **ReplicationType** – This is a String, of type: `string` (a UTF-8 encoded string).

Not supported by Neptune.

- **ServerlessV2ScalingConfiguration** – This is A [ServerlessV2ScalingConfigurationInfo](api-datatypes.md#ServerlessV2ScalingConfigurationInfo "api-datatypes.md#ServerlessV2ScalingConfigurationInfo") object.

Shows the scaling configuration for a Neptune Serverless DB cluster.

For more information, see [Using
Amazon Neptune Serverless](neptune-serverless-using.md "neptune-serverless-using.md") in the _Amazon Neptune User Guide_.

- **Status** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this DB cluster.

- **StorageEncrypted** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster is encrypted.

- **StorageType** – This is a String, of type: `string` (a UTF-8 encoded string).

The storage type used by the DB cluster.

Valid Values:

    + **`standard`**  
     –   ( *the default* ) Provides cost-effective
     database storage for applications with moderate to small I/O usage.
    + **`iopt1`**   –
       Enables [I/O-Optimized
     storage](storage-types.md#provisioned-iops-storage "storage-types.md#provisioned-iops-storage") that's designed to meet the needs of I/O-intensive graph workloads
     that require predictable pricing with low I/O latency and consistent I/O throughput.


    Neptune I/O-Optimized storage is only available starting with engine
     release 1.3.0.0.

- **VpcSecurityGroups** – This is An array of [VpcSecurityGroupMembership](api-datatypes.md#VpcSecurityGroupMembership "api-datatypes.md#VpcSecurityGroupMembership") objects.

Provides a list of VPC security groups that the DB cluster belongs to.

`DBCluster` is used as the response element for:

- [CreateDBCluster](#CreateDBCluster "#CreateDBCluster")
- [DeleteDBCluster](#DeleteDBCluster "#DeleteDBCluster")
- [FailoverDBCluster](#FailoverDBCluster "#FailoverDBCluster")
- [ModifyDBCluster](#ModifyDBCluster "#ModifyDBCluster")
- [PromoteReadReplicaDBCluster](#PromoteReadReplicaDBCluster "#PromoteReadReplicaDBCluster")
- [RestoreDBClusterFromSnapshot](api-snapshots.md#RestoreDBClusterFromSnapshot "api-snapshots.md#RestoreDBClusterFromSnapshot")
- [RestoreDBClusterToPointInTime](api-snapshots.md#RestoreDBClusterToPointInTime "api-snapshots.md#RestoreDBClusterToPointInTime")
- [StartDBCluster](#StartDBCluster "#StartDBCluster")
- [StopDBCluster](#StopDBCluster "#StopDBCluster")

## DBClusterMember (structure)

Contains information about an instance that is part of a DB cluster.

###### Fields

- **DBClusterParameterGroupStatus** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the status of the DB cluster parameter group for this member
of the DB cluster.

- **DBInstanceIdentifier** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the instance identifier for this member of the DB cluster.

- **IsClusterWriter** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Value that is `true` if the cluster member is the primary instance
for the DB cluster and `false` otherwise.

- **PromotionTier** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

A value that specifies the order in which a Read Replica is promoted to the
primary instance after a failure of the existing primary instance.

## DBClusterRole (structure)

Describes an Amazon Identity and Access Management (IAM) role that is
associated with a DB cluster.

###### Fields

- **FeatureName** – This is a String, of type: `string` (a UTF-8 encoded string).

The name of the feature associated with the Amazon Identity and Access
Management (IAM) role. For the list of supported feature names, see [DescribeDBEngineVersions (action)](api-other-apis.md#DescribeDBEngineVersions "api-other-apis.md#DescribeDBEngineVersions").

- **RoleArn** – This is a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) of the IAM role that is associated with the
DB cluster.

- **Status** – This is a String, of type: `string` (a UTF-8 encoded string).

Describes the state of association between the IAM role and the DB cluster.
The Status property returns one of the following values:

    + `ACTIVE` - the IAM role ARN is associated with the DB cluster
     and can be used to access other Amazon services on your behalf.
    + `PENDING` - the IAM role ARN is being associated with the DB
     cluster.
    + `INVALID` - the IAM role ARN is associated with the DB cluster,
     but the DB cluster is unable to assume the IAM role in order to access other Amazon
     services on your behalf.

## CloudwatchLogsExportConfiguration (structure)

The configuration setting for the log types to be enabled for export to
CloudWatch Logs for a specific DB instance or DB cluster.

The `EnableLogTypes` and `DisableLogTypes`
arrays determine which logs will be exported (or not exported) to CloudWatch
Logs.

Valid log types are: `audit` (to publish audit logs) and `slowquery`
(to publish slow-query logs). See [Publishing
Neptune logs to Amazon CloudWatch logs](cloudwatch-logs.md "cloudwatch-logs.md").

###### Fields

- **DisableLogTypes** – This is a String, of type: `string` (a UTF-8 encoded string).

The list of log types to disable.

- **EnableLogTypes** – This is a String, of type: `string` (a UTF-8 encoded string).

The list of log types to enable.

## PendingCloudwatchLogsExports (structure)

A list of the log types whose configuration is still pending. In other words,
these log types are in the process of being activated or deactivated.

Valid log types are: `audit` (to publish audit logs) and `slowquery`
(to publish slow-query logs). See [Publishing
Neptune logs to Amazon CloudWatch logs](cloudwatch-logs.md "cloudwatch-logs.md").

###### Fields

- **LogTypesToDisable** – This is a String, of type: `string` (a UTF-8 encoded string).

Log types that are in the process of being enabled. After they are enabled,
these log types are exported to CloudWatch Logs.

- **LogTypesToEnable** – This is a String, of type: `string` (a UTF-8 encoded string).

Log types that are in the process of being deactivated. After they are deactivated,
these log types aren't exported to CloudWatch Logs.

## ClusterPendingModifiedValues (structure)

This data type is used as a response element in the `ModifyDBCluster`
operation and contains changes that will be applied during the next maintenance
window.

###### Fields

- **AllocatedStorage** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The allocated storage size in gibibytes (GiB) for database engines. For
Neptune, `AllocatedStorage` always returns 1, because Neptune
DB cluster storage size isn't fixed, but instead automatically adjusts as needed.

- **BackupRetentionPeriod** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The number of days for which automatic DB snapshots are retained.

- **DBClusterIdentifier** – This is a String, of type: `string` (a UTF-8 encoded string).

The DBClusterIdentifier value for the DB cluster.

- **EngineVersion** – This is a String, of type: `string` (a UTF-8 encoded string).

The database engine version.

- **IAMDatabaseAuthenticationEnabled** – This is a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

A value that indicates whether mapping of AWS Identity
and Access Management (IAM) accounts to database accounts is enabled.

- **Iops** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The Provisioned IOPS (I/O operations per second) value. This setting
is only for Multi-AZ DB clusters.

- **PendingCloudwatchLogsExports** – This is A [PendingCloudwatchLogsExports](#PendingCloudwatchLogsExports "#PendingCloudwatchLogsExports") object.

This `PendingCloudwatchLogsExports` structure specifies
pending changes to which CloudWatch logs are enabled and which are disabled.

- **StorageType** – This is a String, of type: `string` (a UTF-8 encoded string).

The pending change in storage type for the DB cluster.   Valid Values:

    + **`standard`**  
     –   ( *the default* ) Configures cost-effective
     database storage for applications with moderate to small I/O usage.
    + **`iopt1`**   –
       Enables [I/O-Optimized
     storage](storage-types.md#provisioned-iops-storage "storage-types.md#provisioned-iops-storage") that's designed to meet the needs of I/O-intensive graph workloads
     that require predictable pricing with low I/O latency and consistent I/O throughput.


    Neptune I/O-Optimized storage is only available starting with engine
     release 1.3.0.0.
