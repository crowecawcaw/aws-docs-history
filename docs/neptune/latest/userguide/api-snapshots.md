# Neptune Snapshots API

**Actions:**

- [CreateDBClusterSnapshot (action)](#CreateDBClusterSnapshot "#CreateDBClusterSnapshot")
- [DeleteDBClusterSnapshot (action)](#DeleteDBClusterSnapshot "#DeleteDBClusterSnapshot")
- [CopyDBClusterSnapshot (action)](#CopyDBClusterSnapshot "#CopyDBClusterSnapshot")
- [ModifyDBClusterSnapshotAttribute (action)](#ModifyDBClusterSnapshotAttribute "#ModifyDBClusterSnapshotAttribute")
- [RestoreDBClusterFromSnapshot (action)](#RestoreDBClusterFromSnapshot "#RestoreDBClusterFromSnapshot")
- [RestoreDBClusterToPointInTime (action)](#RestoreDBClusterToPointInTime "#RestoreDBClusterToPointInTime")
- [DescribeDBClusterSnapshots (action)](#DescribeDBClusterSnapshots "#DescribeDBClusterSnapshots")
- [DescribeDBClusterSnapshotAttributes (action)](#DescribeDBClusterSnapshotAttributes "#DescribeDBClusterSnapshotAttributes")
  **Structures:**

- [DBClusterSnapshot (structure)](#DBClusterSnapshot "#DBClusterSnapshot")
- [DBClusterSnapshotAttribute (structure)](#DBClusterSnapshotAttribute "#DBClusterSnapshotAttribute")
- [DBClusterSnapshotAttributesResult (structure)](#DBClusterSnapshotAttributesResult "#DBClusterSnapshotAttributesResult")

## CreateDBClusterSnapshot (action)

        The AWS CLI name for this API is: `create-db-cluster-snapshot`.

Creates a snapshot of a DB cluster.

**Request**

- **DBClusterIdentifier**  (in the CLI: `--db-cluster-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The identifier of the DB cluster to create a snapshot for. This parameter
is not case-sensitive.

Constraints:

    + Must match the identifier of an existing DBCluster.

Example: `my-cluster1`

- **DBClusterSnapshotIdentifier**  (in the CLI: `--db-cluster-snapshot-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The identifier of the DB cluster snapshot. This parameter is stored as
a lowercase string.

Constraints:

    + Must contain from 1 to 63 letters, numbers, or hyphens.
    + First character must be a letter.
    + Cannot end with a hyphen or contain two consecutive hyphens.

Example: `my-cluster1-snapshot1`

- **Tags**  (in the CLI: `--tags`) –  An array of [Tag](api-other-apis.md#Tag "api-other-apis.md#Tag") objects.

The tags to be assigned to the DB cluster snapshot.

**Response**

Contains the details for an Amazon Neptune DB cluster snapshot

This data type is used as a response element in the [DescribeDBClusterSnapshots (action)](#DescribeDBClusterSnapshots "#DescribeDBClusterSnapshots") action.

- **AllocatedStorage**   – an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the allocated storage size in gibibytes (GiB).

- **AvailabilityZones**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the list of EC2 Availability Zones that instances in the DB cluster
snapshot can be restored in.

- **ClusterCreateTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the time when the DB cluster was created, in Universal Coordinated
Time (UTC).

- **DBClusterIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the DB cluster identifier of the DB cluster that this DB cluster
snapshot was created from.

- **DBClusterSnapshotArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB cluster snapshot.

- **DBClusterSnapshotIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the identifier for a DB cluster snapshot. Must match the identifier
of an existing snapshot.

After you restore a DB cluster using a `DBClusterSnapshotIdentifier`,
you must specify the same `DBClusterSnapshotIdentifier` for any
future updates to the DB cluster. When you specify this property for an update,
the DB cluster is not restored from the snapshot again, and the data in the database
is not changed.

However, if you don't specify the `DBClusterSnapshotIdentifier`,
an empty DB cluster is created, and the original DB cluster is deleted. If you specify
a property that is different from the previous snapshot restore property, the
DB cluster is restored from the snapshot specified by the `DBClusterSnapshotIdentifier`,
and the original DB cluster is deleted.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the database engine.

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the version of the database engine for this DB cluster snapshot.

- **IAMDatabaseAuthenticationEnabled**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

True if mapping of Amazon Identity and Access Management (IAM) accounts
to database accounts is enabled, and otherwise false.

- **KmsKeyId**   – a String, of type: `string` (a UTF-8 encoded string).

If `StorageEncrypted` is true, the Amazon KMS key identifier
for the encrypted DB cluster snapshot.

- **LicenseModel**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the license model information for this DB cluster snapshot.

- **PercentProgress**   – an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the percentage of the estimated data that has been transferred.

- **Port**   – an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the port that the DB cluster was listening on at the time of the
snapshot.

- **SnapshotCreateTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Provides the time when the snapshot was taken, in Universal Coordinated
Time (UTC).

- **SnapshotType**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the type of the DB cluster snapshot.

- **SourceDBClusterSnapshotArn**   – a String, of type: `string` (a UTF-8 encoded string).

If the DB cluster snapshot was copied from a source DB cluster snapshot,
the Amazon Resource Name (ARN) for the source DB cluster snapshot, otherwise,
a null value.

- **Status**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the status of this DB cluster snapshot.

- **StorageEncrypted**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster snapshot is encrypted.

- **StorageType**   – a String, of type: `string` (a UTF-8 encoded string).

The storage type associated with the DB cluster snapshot.

- **VpcId**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the VPC ID associated with the DB cluster snapshot.

###### Errors

- [DBClusterSnapshotAlreadyExistsFault](api-faults.md#DBClusterSnapshotAlreadyExistsFault "api-faults.md#DBClusterSnapshotAlreadyExistsFault")
- [InvalidDBClusterStateFault](api-faults.md#InvalidDBClusterStateFault "api-faults.md#InvalidDBClusterStateFault")
- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")
- [SnapshotQuotaExceededFault](api-faults.md#SnapshotQuotaExceededFault "api-faults.md#SnapshotQuotaExceededFault")
- [InvalidDBClusterSnapshotStateFault](api-faults.md#InvalidDBClusterSnapshotStateFault "api-faults.md#InvalidDBClusterSnapshotStateFault")

## DeleteDBClusterSnapshot (action)

        The AWS CLI name for this API is: `delete-db-cluster-snapshot`.

Deletes a DB cluster snapshot. If the snapshot is being copied, the copy
operation is terminated.

###### Note

The DB cluster snapshot must be in the `available` state to
be deleted.

**Request**

- **DBClusterSnapshotIdentifier**  (in the CLI: `--db-cluster-snapshot-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The identifier of the DB cluster snapshot to delete.

Constraints: Must be the name of an existing DB cluster snapshot in the
`available` state.

**Response**

Contains the details for an Amazon Neptune DB cluster snapshot

This data type is used as a response element in the [DescribeDBClusterSnapshots (action)](#DescribeDBClusterSnapshots "#DescribeDBClusterSnapshots") action.

- **AllocatedStorage**   – an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the allocated storage size in gibibytes (GiB).

- **AvailabilityZones**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the list of EC2 Availability Zones that instances in the DB cluster
snapshot can be restored in.

- **ClusterCreateTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the time when the DB cluster was created, in Universal Coordinated
Time (UTC).

- **DBClusterIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the DB cluster identifier of the DB cluster that this DB cluster
snapshot was created from.

- **DBClusterSnapshotArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB cluster snapshot.

- **DBClusterSnapshotIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the identifier for a DB cluster snapshot. Must match the identifier
of an existing snapshot.

After you restore a DB cluster using a `DBClusterSnapshotIdentifier`,
you must specify the same `DBClusterSnapshotIdentifier` for any
future updates to the DB cluster. When you specify this property for an update,
the DB cluster is not restored from the snapshot again, and the data in the database
is not changed.

However, if you don't specify the `DBClusterSnapshotIdentifier`,
an empty DB cluster is created, and the original DB cluster is deleted. If you specify
a property that is different from the previous snapshot restore property, the
DB cluster is restored from the snapshot specified by the `DBClusterSnapshotIdentifier`,
and the original DB cluster is deleted.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the database engine.

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the version of the database engine for this DB cluster snapshot.

- **IAMDatabaseAuthenticationEnabled**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

True if mapping of Amazon Identity and Access Management (IAM) accounts
to database accounts is enabled, and otherwise false.

- **KmsKeyId**   – a String, of type: `string` (a UTF-8 encoded string).

If `StorageEncrypted` is true, the Amazon KMS key identifier
for the encrypted DB cluster snapshot.

- **LicenseModel**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the license model information for this DB cluster snapshot.

- **PercentProgress**   – an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the percentage of the estimated data that has been transferred.

- **Port**   – an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the port that the DB cluster was listening on at the time of the
snapshot.

- **SnapshotCreateTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Provides the time when the snapshot was taken, in Universal Coordinated
Time (UTC).

- **SnapshotType**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the type of the DB cluster snapshot.

- **SourceDBClusterSnapshotArn**   – a String, of type: `string` (a UTF-8 encoded string).

If the DB cluster snapshot was copied from a source DB cluster snapshot,
the Amazon Resource Name (ARN) for the source DB cluster snapshot, otherwise,
a null value.

- **Status**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the status of this DB cluster snapshot.

- **StorageEncrypted**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster snapshot is encrypted.

- **StorageType**   – a String, of type: `string` (a UTF-8 encoded string).

The storage type associated with the DB cluster snapshot.

- **VpcId**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the VPC ID associated with the DB cluster snapshot.

###### Errors

- [InvalidDBClusterSnapshotStateFault](api-faults.md#InvalidDBClusterSnapshotStateFault "api-faults.md#InvalidDBClusterSnapshotStateFault")
- [DBClusterSnapshotNotFoundFault](api-faults.md#DBClusterSnapshotNotFoundFault "api-faults.md#DBClusterSnapshotNotFoundFault")

## CopyDBClusterSnapshot (action)

        The AWS CLI name for this API is: `copy-db-cluster-snapshot`.

Copies a snapshot of a DB cluster.

To copy a DB cluster snapshot from a shared manual DB cluster snapshot,
`SourceDBClusterSnapshotIdentifier` must be the Amazon Resource
Name (ARN) of the shared DB cluster snapshot.

**Request**

- **CopyTags**  (in the CLI: `--copy-tags`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

True to copy all tags from the source DB cluster snapshot to the target DB
cluster snapshot, and otherwise false. The default is false.

- **KmsKeyId**  (in the CLI: `--kms-key-id`) –  a String, of type: `string` (a UTF-8 encoded string).

The Amazon Amazon KMS key ID for an encrypted DB cluster snapshot. The KMS
key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias
for the KMS encryption key.

If you copy an encrypted DB cluster snapshot from your Amazon account,
you can specify a value for `KmsKeyId` to encrypt the copy with a new
KMS encryption key. If you don't specify a value for `KmsKeyId`,
then the copy of the DB cluster snapshot is encrypted with the same KMS key as the
source DB cluster snapshot.

If you copy an encrypted DB cluster snapshot that is shared from another
Amazon account, then you must specify a value for `KmsKeyId`.

KMS encryption keys are specific to the Amazon Region that they are created
in, and you can't use encryption keys from one Amazon Region in another Amazon
Region.

You cannot encrypt an unencrypted DB cluster snapshot when you copy it.
If you try to copy an unencrypted DB cluster snapshot and specify a value for the
KmsKeyId parameter, an error is returned.

- **PreSignedUrl**  (in the CLI: `--pre-signed-url`) –  a String, of type: `string` (a UTF-8 encoded string).

Not currently supported.

- **SourceDBClusterSnapshotIdentifier**  (in the CLI: `--source-db-cluster-snapshot-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The identifier of the DB cluster snapshot to copy. This parameter is not
case-sensitive.

Constraints:

    + Must specify a valid system snapshot in the "available" state.
    + Specify a valid DB snapshot identifier.

Example: `my-cluster-snapshot1`

- **Tags**  (in the CLI: `--tags`) –  An array of [Tag](api-other-apis.md#Tag "api-other-apis.md#Tag") objects.

The tags to assign to the new DB cluster snapshot copy.

- **TargetDBClusterSnapshotIdentifier**  (in the CLI: `--target-db-cluster-snapshot-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The identifier of the new DB cluster snapshot to create from the source
DB cluster snapshot. This parameter is not case-sensitive.

Constraints:

    + Must contain from 1 to 63 letters, numbers, or hyphens.
    + First character must be a letter.
    + Cannot end with a hyphen or contain two consecutive hyphens.

Example: `my-cluster-snapshot2`

**Response**

Contains the details for an Amazon Neptune DB cluster snapshot

This data type is used as a response element in the [DescribeDBClusterSnapshots (action)](#DescribeDBClusterSnapshots "#DescribeDBClusterSnapshots") action.

- **AllocatedStorage**   – an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the allocated storage size in gibibytes (GiB).

- **AvailabilityZones**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the list of EC2 Availability Zones that instances in the DB cluster
snapshot can be restored in.

- **ClusterCreateTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the time when the DB cluster was created, in Universal Coordinated
Time (UTC).

- **DBClusterIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the DB cluster identifier of the DB cluster that this DB cluster
snapshot was created from.

- **DBClusterSnapshotArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB cluster snapshot.

- **DBClusterSnapshotIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the identifier for a DB cluster snapshot. Must match the identifier
of an existing snapshot.

After you restore a DB cluster using a `DBClusterSnapshotIdentifier`,
you must specify the same `DBClusterSnapshotIdentifier` for any
future updates to the DB cluster. When you specify this property for an update,
the DB cluster is not restored from the snapshot again, and the data in the database
is not changed.

However, if you don't specify the `DBClusterSnapshotIdentifier`,
an empty DB cluster is created, and the original DB cluster is deleted. If you specify
a property that is different from the previous snapshot restore property, the
DB cluster is restored from the snapshot specified by the `DBClusterSnapshotIdentifier`,
and the original DB cluster is deleted.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the database engine.

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the version of the database engine for this DB cluster snapshot.

- **IAMDatabaseAuthenticationEnabled**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

True if mapping of Amazon Identity and Access Management (IAM) accounts
to database accounts is enabled, and otherwise false.

- **KmsKeyId**   – a String, of type: `string` (a UTF-8 encoded string).

If `StorageEncrypted` is true, the Amazon KMS key identifier
for the encrypted DB cluster snapshot.

- **LicenseModel**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the license model information for this DB cluster snapshot.

- **PercentProgress**   – an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the percentage of the estimated data that has been transferred.

- **Port**   – an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the port that the DB cluster was listening on at the time of the
snapshot.

- **SnapshotCreateTime**   – a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Provides the time when the snapshot was taken, in Universal Coordinated
Time (UTC).

- **SnapshotType**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the type of the DB cluster snapshot.

- **SourceDBClusterSnapshotArn**   – a String, of type: `string` (a UTF-8 encoded string).

If the DB cluster snapshot was copied from a source DB cluster snapshot,
the Amazon Resource Name (ARN) for the source DB cluster snapshot, otherwise,
a null value.

- **Status**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the status of this DB cluster snapshot.

- **StorageEncrypted**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster snapshot is encrypted.

- **StorageType**   – a String, of type: `string` (a UTF-8 encoded string).

The storage type associated with the DB cluster snapshot.

- **VpcId**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the VPC ID associated with the DB cluster snapshot.

###### Errors

- [DBClusterSnapshotAlreadyExistsFault](api-faults.md#DBClusterSnapshotAlreadyExistsFault "api-faults.md#DBClusterSnapshotAlreadyExistsFault")
- [DBClusterSnapshotNotFoundFault](api-faults.md#DBClusterSnapshotNotFoundFault "api-faults.md#DBClusterSnapshotNotFoundFault")
- [InvalidDBClusterStateFault](api-faults.md#InvalidDBClusterStateFault "api-faults.md#InvalidDBClusterStateFault")
- [InvalidDBClusterSnapshotStateFault](api-faults.md#InvalidDBClusterSnapshotStateFault "api-faults.md#InvalidDBClusterSnapshotStateFault")
- [SnapshotQuotaExceededFault](api-faults.md#SnapshotQuotaExceededFault "api-faults.md#SnapshotQuotaExceededFault")
- [KMSKeyNotAccessibleFault](api-faults.md#KMSKeyNotAccessibleFault "api-faults.md#KMSKeyNotAccessibleFault")

## ModifyDBClusterSnapshotAttribute (action)

        The AWS CLI name for this API is: `modify-db-cluster-snapshot-attribute`.

Adds an attribute and values to, or removes an attribute and values from,
a manual DB cluster snapshot.

To share a manual DB cluster snapshot with other Amazon accounts, specify
`restore` as the `AttributeName` and use the `ValuesToAdd`
parameter to add a list of IDs of the Amazon accounts that are authorized to restore
the manual DB cluster snapshot. Use the value `all` to make the manual
DB cluster snapshot public, which means that it can be copied or restored by all
Amazon accounts. Do not add the `all` value for any manual DB cluster
snapshots that contain private information that you don't want available to
all Amazon accounts. If a manual DB cluster snapshot is encrypted, it can be shared,
but only by specifying a list of authorized Amazon account IDs for the `ValuesToAdd`
parameter. You can't use `all` as a value for that parameter in this
case.

To view which Amazon accounts have access to copy or restore a manual DB
cluster snapshot, or whether a manual DB cluster snapshot public or private,
use the [DescribeDBClusterSnapshotAttributes (action)](#DescribeDBClusterSnapshotAttributes "#DescribeDBClusterSnapshotAttributes") API action.

**Request**

- **AttributeName**  (in the CLI: `--attribute-name`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the DB cluster snapshot attribute to modify.

To manage authorization for other Amazon accounts to copy or restore a
manual DB cluster snapshot, set this value to `restore`.

- **DBClusterSnapshotIdentifier**  (in the CLI: `--db-cluster-snapshot-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The identifier for the DB cluster snapshot to modify the attributes for.

- **ValuesToAdd**  (in the CLI: `--values-to-add`) –  a String, of type: `string` (a UTF-8 encoded string).

A list of DB cluster snapshot attributes to add to the attribute specified
by `AttributeName`.

To authorize other Amazon accounts to copy or restore a manual DB cluster
snapshot, set this list to include one or more Amazon account IDs, or `all`
to make the manual DB cluster snapshot restorable by any Amazon account. Do not
add the `all` value for any manual DB cluster snapshots that contain
private information that you don't want available to all Amazon accounts.

- **ValuesToRemove**  (in the CLI: `--values-to-remove`) –  a String, of type: `string` (a UTF-8 encoded string).

A list of DB cluster snapshot attributes to remove from the attribute specified
by `AttributeName`.

To remove authorization for other Amazon accounts to copy or restore a
manual DB cluster snapshot, set this list to include one or more Amazon account
identifiers, or `all` to remove authorization for any Amazon account
to copy or restore the DB cluster snapshot. If you specify `all`,
an Amazon account whose account ID is explicitly added to the `restore`
attribute can still copy or restore a manual DB cluster snapshot.

**Response**

Contains the results of a successful call to the [DescribeDBClusterSnapshotAttributes (action)](#DescribeDBClusterSnapshotAttributes "#DescribeDBClusterSnapshotAttributes") API action.

Manual DB cluster snapshot attributes are used to authorize other Amazon
accounts to copy or restore a manual DB cluster snapshot. For more information,
see the ModifyDBClusterSnapshotAttribute (action) API action.

- **DBClusterSnapshotAttributes**   – An array of [DBClusterSnapshotAttribute](#DBClusterSnapshotAttribute "#DBClusterSnapshotAttribute") objects.

The list of attributes and values for the manual DB cluster snapshot.

- **DBClusterSnapshotIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

The identifier of the manual DB cluster snapshot that the attributes apply
to.

###### Errors

- [DBClusterSnapshotNotFoundFault](api-faults.md#DBClusterSnapshotNotFoundFault "api-faults.md#DBClusterSnapshotNotFoundFault")
- [InvalidDBClusterSnapshotStateFault](api-faults.md#InvalidDBClusterSnapshotStateFault "api-faults.md#InvalidDBClusterSnapshotStateFault")
- [SharedSnapshotQuotaExceededFault](api-faults.md#SharedSnapshotQuotaExceededFault "api-faults.md#SharedSnapshotQuotaExceededFault")

## RestoreDBClusterFromSnapshot (action)

        The AWS CLI name for this API is: `restore-db-cluster-from-snapshot`.

Creates a new DB cluster from a DB snapshot or DB cluster snapshot.

If a DB snapshot is specified, the target DB cluster is created from the
source DB snapshot with a default configuration and default security group.

If a DB cluster snapshot is specified, the target DB cluster is created
from the source DB cluster restore point with the same configuration as the original
source DB cluster, except that the new DB cluster is created with the default security
group.

**Request**

- **AvailabilityZones**  (in the CLI: `--availability-zones`) –  a String, of type: `string` (a UTF-8 encoded string).

Provides the list of EC2 Availability Zones that instances in the restored
DB cluster can be created in.

- **CopyTagsToSnapshot**  (in the CLI: `--copy-tags-to-snapshot`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

_If set to `true`, tags are copied to any snapshot
of the restored DB cluster that is created._

- **DatabaseName**  (in the CLI: `--database-name`) –  a String, of type: `string` (a UTF-8 encoded string).

Not supported.

- **DBClusterIdentifier**  (in the CLI: `--db-cluster-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the DB cluster to create from the DB snapshot or DB cluster snapshot.
This parameter isn't case-sensitive.

Constraints:

    + Must contain from 1 to 63 letters, numbers, or hyphens
    + First character must be a letter
    + Cannot end with a hyphen or contain two consecutive hyphens

Example: `my-snapshot-id`

- **DBClusterParameterGroupName**  (in the CLI: `--db-cluster-parameter-group-name`) –  a String, of type: `string` (a UTF-8 encoded string).

The name of the DB cluster parameter group to associate with the new DB cluster.

Constraints:

    + If supplied, must match the name of an existing DBClusterParameterGroup.

- **DBSubnetGroupName**  (in the CLI: `--db-subnet-group-name`) –  a String, of type: `string` (a UTF-8 encoded string).

The name of the DB subnet group to use for the new DB cluster.

Constraints: If supplied, must match the name of an existing DBSubnetGroup.

Example: `mySubnetgroup`

- **DeletionProtection**  (in the CLI: `--deletion-protection`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

A value that indicates whether the DB cluster has deletion protection
enabled. The database can't be deleted when deletion protection is enabled.
By default, deletion protection is disabled.

- **EnableCloudwatchLogsExports**  (in the CLI: `--enable-cloudwatch-logs-exports`) –  a String, of type: `string` (a UTF-8 encoded string).

The list of logs that the restored DB cluster is to export to Amazon CloudWatch
Logs.

- **EnableIAMDatabaseAuthentication**  (in the CLI: `--enable-iam-database-authentication`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

True to enable mapping of Amazon Identity and Access Management (IAM)
accounts to database accounts, and otherwise false.

Default: `false`

- **Engine**  (in the CLI: `--engine`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The database engine to use for the new DB cluster.

Default: The same as source

Constraint: Must be compatible with the engine of the source

- **EngineVersion**  (in the CLI: `--engine-version`) –  a String, of type: `string` (a UTF-8 encoded string).

The version of the database engine to use for the new DB cluster.

- **KmsKeyId**  (in the CLI: `--kms-key-id`) –  a String, of type: `string` (a UTF-8 encoded string).

The Amazon KMS key identifier to use when restoring an encrypted DB cluster
from a DB snapshot or DB cluster snapshot.

The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption
key. If you are restoring a DB cluster with the same Amazon account that owns the
KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key
alias instead of the ARN for the KMS encryption key.

If you do not specify a value for the `KmsKeyId` parameter,
then the following will occur:

    + If the DB snapshot or DB cluster snapshot in `SnapshotIdentifier`
     is encrypted, then the restored DB cluster is encrypted using the KMS key that
     was used to encrypt the DB snapshot or DB cluster snapshot.
    + If the DB snapshot or DB cluster snapshot in `SnapshotIdentifier`
     is not encrypted, then the restored DB cluster is not encrypted.

- **Port**  (in the CLI: `--port`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The port number on which the new DB cluster accepts connections.

Constraints: Value must be `1150-65535`

Default: The same port as the original DB cluster.

- **ServerlessV2ScalingConfiguration**  (in the CLI: `--serverless-v2-scaling-configuration`) –  A [ServerlessV2ScalingConfiguration](api-datatypes.md#ServerlessV2ScalingConfiguration "api-datatypes.md#ServerlessV2ScalingConfiguration") object.

Contains the scaling configuration of a Neptune Serverless DB cluster.

For more information, see [Using
Amazon Neptune Serverless](neptune-serverless-using.md "neptune-serverless-using.md") in the _Amazon Neptune User Guide_.

- **SnapshotIdentifier**  (in the CLI: `--snapshot-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The identifier for the DB snapshot or DB cluster snapshot to restore from.

You can use either the name or the Amazon Resource Name (ARN) to specify
a DB cluster snapshot. However, you can use only the ARN to specify a DB snapshot.

Constraints:

    + Must match the identifier of an existing Snapshot.

- **StorageType**  (in the CLI: `--storage-type`) –  a String, of type: `string` (a UTF-8 encoded string).

Specifies the storage type to be associated with the DB cluster.

Valid values: `standard`, `iopt1`

Default: `standard`

- **Tags**  (in the CLI: `--tags`) –  An array of [Tag](api-other-apis.md#Tag "api-other-apis.md#Tag") objects.

The tags to be assigned to the restored DB cluster.

- **VpcSecurityGroupIds**  (in the CLI: `--vpc-security-group-ids`) –  a String, of type: `string` (a UTF-8 encoded string).

A list of VPC security groups that the new DB cluster will belong to.

**Response**

Contains the details of an Amazon Neptune DB cluster.

This data type is used as a response element in the [DescribeDBClusters (action)](api-clusters.md#DescribeDBClusters "api-clusters.md#DescribeDBClusters").

- **AllocatedStorage**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

`AllocatedStorage` always returns 1, because Neptune DB
cluster storage size is not fixed, but instead automatically adjusts as needed.

- **AssociatedRoles**   – An array of [DBClusterRole](api-clusters.md#DBClusterRole "api-clusters.md#DBClusterRole") objects.

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

- **DBClusterMembers**   – An array of [DBClusterMember](api-clusters.md#DBClusterMember "api-clusters.md#DBClusterMember") objects.

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

- **PendingModifiedValues**   – A [ClusterPendingModifiedValues](api-clusters.md#ClusterPendingModifiedValues "api-clusters.md#ClusterPendingModifiedValues") object.

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
- [DBClusterQuotaExceededFault](api-faults.md#DBClusterQuotaExceededFault "api-faults.md#DBClusterQuotaExceededFault")
- [StorageQuotaExceededFault](api-faults.md#StorageQuotaExceededFault "api-faults.md#StorageQuotaExceededFault")
- [DBSubnetGroupNotFoundFault](api-faults.md#DBSubnetGroupNotFoundFault "api-faults.md#DBSubnetGroupNotFoundFault")
- [DBSnapshotNotFoundFault](api-faults.md#DBSnapshotNotFoundFault "api-faults.md#DBSnapshotNotFoundFault")
- [DBClusterSnapshotNotFoundFault](api-faults.md#DBClusterSnapshotNotFoundFault "api-faults.md#DBClusterSnapshotNotFoundFault")
- [InsufficientDBClusterCapacityFault](api-faults.md#InsufficientDBClusterCapacityFault "api-faults.md#InsufficientDBClusterCapacityFault")
- [InsufficientStorageClusterCapacityFault](api-faults.md#InsufficientStorageClusterCapacityFault "api-faults.md#InsufficientStorageClusterCapacityFault")
- [InvalidDBSnapshotStateFault](api-faults.md#InvalidDBSnapshotStateFault "api-faults.md#InvalidDBSnapshotStateFault")
- [InvalidDBClusterSnapshotStateFault](api-faults.md#InvalidDBClusterSnapshotStateFault "api-faults.md#InvalidDBClusterSnapshotStateFault")
- [StorageQuotaExceededFault](api-faults.md#StorageQuotaExceededFault "api-faults.md#StorageQuotaExceededFault")
- [InvalidVPCNetworkStateFault](api-faults.md#InvalidVPCNetworkStateFault "api-faults.md#InvalidVPCNetworkStateFault")
- [InvalidRestoreFault](api-faults.md#InvalidRestoreFault "api-faults.md#InvalidRestoreFault")
- [DBSubnetGroupNotFoundFault](api-faults.md#DBSubnetGroupNotFoundFault "api-faults.md#DBSubnetGroupNotFoundFault")
- [InvalidSubnet](api-faults.md#InvalidSubnet "api-faults.md#InvalidSubnet")
- [OptionGroupNotFoundFault](api-faults.md#OptionGroupNotFoundFault "api-faults.md#OptionGroupNotFoundFault")
- [KMSKeyNotAccessibleFault](api-faults.md#KMSKeyNotAccessibleFault "api-faults.md#KMSKeyNotAccessibleFault")
- [DBClusterParameterGroupNotFoundFault](api-faults.md#DBClusterParameterGroupNotFoundFault "api-faults.md#DBClusterParameterGroupNotFoundFault")

## RestoreDBClusterToPointInTime (action)

        The AWS CLI name for this API is: `restore-db-cluster-to-point-in-time`.

Restores a DB cluster to an arbitrary point in time. Users can restore to
any point in time before `LatestRestorableTime` for up to `BackupRetentionPeriod`
days. The target DB cluster is created from the source DB cluster with the same
configuration as the original DB cluster, except that the new DB cluster is created
with the default DB security group.

###### Note

This action only restores the DB cluster, not the DB instances for that
DB cluster. You must invoke the [CreateDBInstance (action)](api-instances.md#CreateDBInstance "api-instances.md#CreateDBInstance") action
to create DB instances for the restored DB cluster, specifying the identifier
of the restored DB cluster in `DBClusterIdentifier`. You can create
DB instances only after the `RestoreDBClusterToPointInTime`
action has completed and the DB cluster is available.

**Request**

- **DBClusterIdentifier**  (in the CLI: `--db-cluster-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the new DB cluster to be created.

Constraints:

    + Must contain from 1 to 63 letters, numbers, or hyphens
    + First character must be a letter
    + Cannot end with a hyphen or contain two consecutive hyphens

- **DBClusterParameterGroupName**  (in the CLI: `--db-cluster-parameter-group-name`) –  a String, of type: `string` (a UTF-8 encoded string).

The name of the DB cluster parameter group to associate with the new DB cluster.

Constraints:

    + If supplied, must match the name of an existing DBClusterParameterGroup.

- **DBSubnetGroupName**  (in the CLI: `--db-subnet-group-name`) –  a String, of type: `string` (a UTF-8 encoded string).

The DB subnet group name to use for the new DB cluster.

Constraints: If supplied, must match the name of an existing DBSubnetGroup.

Example: `mySubnetgroup`

- **DeletionProtection**  (in the CLI: `--deletion-protection`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

A value that indicates whether the DB cluster has deletion protection
enabled. The database can't be deleted when deletion protection is enabled.
By default, deletion protection is disabled.

- **EnableCloudwatchLogsExports**  (in the CLI: `--enable-cloudwatch-logs-exports`) –  a String, of type: `string` (a UTF-8 encoded string).

The list of logs that the restored DB cluster is to export to CloudWatch
Logs.

- **EnableIAMDatabaseAuthentication**  (in the CLI: `--enable-iam-database-authentication`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

True to enable mapping of Amazon Identity and Access Management (IAM)
accounts to database accounts, and otherwise false.

Default: `false`

- **KmsKeyId**  (in the CLI: `--kms-key-id`) –  a String, of type: `string` (a UTF-8 encoded string).

The Amazon KMS key identifier to use when restoring an encrypted DB cluster
from an encrypted DB cluster.

The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption
key. If you are restoring a DB cluster with the same Amazon account that owns the
KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key
alias instead of the ARN for the KMS encryption key.

You can restore to a new DB cluster and encrypt the new DB cluster with a KMS
key that is different than the KMS key used to encrypt the source DB cluster. The
new DB cluster is encrypted with the KMS key identified by the `KmsKeyId`
parameter.

If you do not specify a value for the `KmsKeyId` parameter,
then the following will occur:

    + If the DB cluster is encrypted, then the restored DB cluster is encrypted
     using the KMS key that was used to encrypt the source DB cluster.
    + If the DB cluster is not encrypted, then the restored DB cluster is not encrypted.

If `DBClusterIdentifier` refers to a DB cluster that is not
encrypted, then the restore request is rejected.

- **Port**  (in the CLI: `--port`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The port number on which the new DB cluster accepts connections.

Constraints: Value must be `1150-65535`

Default: The same port as the original DB cluster.

- **RestoreToTime**  (in the CLI: `--restore-to-time`) –  a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

The date and time to restore the DB cluster to.

Valid Values: Value must be a time in Universal Coordinated Time (UTC)
format

Constraints:

    + Must be before the latest restorable time for the DB instance
    + Must be specified if `UseLatestRestorableTime` parameter
     is not provided
    + Cannot be specified if `UseLatestRestorableTime` parameter
     is true
    + Cannot be specified if `RestoreType` parameter is `copy-on-write`

Example: `2015-03-07T23:45:00Z`

- **RestoreType**  (in the CLI: `--restore-type`) –  a String, of type: `string` (a UTF-8 encoded string).

The type of restore to be performed. You can specify one of the following
values:

    + `full-copy` - The new DB cluster is restored as a full copy
     of the source DB cluster.
    + `copy-on-write` - The new DB cluster is restored as a clone
     of the source DB cluster.

If you don't specify a `RestoreType` value, then the new DB
cluster is restored as a full copy of the source DB cluster.

- **ServerlessV2ScalingConfiguration**  (in the CLI: `--serverless-v2-scaling-configuration`) –  A [ServerlessV2ScalingConfiguration](api-datatypes.md#ServerlessV2ScalingConfiguration "api-datatypes.md#ServerlessV2ScalingConfiguration") object.

Contains the scaling configuration of a Neptune Serverless DB cluster.

For more information, see [Using
Amazon Neptune Serverless](neptune-serverless-using.md "neptune-serverless-using.md") in the _Amazon Neptune User Guide_.

- **SourceDBClusterIdentifier**  (in the CLI: `--source-db-cluster-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The identifier of the source DB cluster from which to restore.

Constraints:

    + Must match the identifier of an existing DBCluster.

- **StorageType**  (in the CLI: `--storage-type`) –  a String, of type: `string` (a UTF-8 encoded string).

Specifies the storage type to be associated with the DB cluster.

Valid values: `standard`, `iopt1`

Default: `standard`

- **Tags**  (in the CLI: `--tags`) –  An array of [Tag](api-other-apis.md#Tag "api-other-apis.md#Tag") objects.

The tags to be applied to the restored DB cluster.

- **UseLatestRestorableTime**  (in the CLI: `--use-latest-restorable-time`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

A value that is set to `true` to restore the DB cluster to the
latest restorable backup time, and `false` otherwise.

Default: `false`

Constraints: Cannot be specified if `RestoreToTime` parameter
is provided.

- **VpcSecurityGroupIds**  (in the CLI: `--vpc-security-group-ids`) –  a String, of type: `string` (a UTF-8 encoded string).

A list of VPC security groups that the new DB cluster belongs to.

**Response**

Contains the details of an Amazon Neptune DB cluster.

This data type is used as a response element in the [DescribeDBClusters (action)](api-clusters.md#DescribeDBClusters "api-clusters.md#DescribeDBClusters").

- **AllocatedStorage**   – an IntegerOptional, of type: `integer` (a signed 32-bit integer).

`AllocatedStorage` always returns 1, because Neptune DB
cluster storage size is not fixed, but instead automatically adjusts as needed.

- **AssociatedRoles**   – An array of [DBClusterRole](api-clusters.md#DBClusterRole "api-clusters.md#DBClusterRole") objects.

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

- **DBClusterMembers**   – An array of [DBClusterMember](api-clusters.md#DBClusterMember "api-clusters.md#DBClusterMember") objects.

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

- **PendingModifiedValues**   – A [ClusterPendingModifiedValues](api-clusters.md#ClusterPendingModifiedValues "api-clusters.md#ClusterPendingModifiedValues") object.

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
- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")
- [DBClusterQuotaExceededFault](api-faults.md#DBClusterQuotaExceededFault "api-faults.md#DBClusterQuotaExceededFault")
- [DBClusterSnapshotNotFoundFault](api-faults.md#DBClusterSnapshotNotFoundFault "api-faults.md#DBClusterSnapshotNotFoundFault")
- [DBSubnetGroupNotFoundFault](api-faults.md#DBSubnetGroupNotFoundFault "api-faults.md#DBSubnetGroupNotFoundFault")
- [InsufficientDBClusterCapacityFault](api-faults.md#InsufficientDBClusterCapacityFault "api-faults.md#InsufficientDBClusterCapacityFault")
- [InsufficientStorageClusterCapacityFault](api-faults.md#InsufficientStorageClusterCapacityFault "api-faults.md#InsufficientStorageClusterCapacityFault")
- [InvalidDBClusterSnapshotStateFault](api-faults.md#InvalidDBClusterSnapshotStateFault "api-faults.md#InvalidDBClusterSnapshotStateFault")
- [InvalidDBClusterStateFault](api-faults.md#InvalidDBClusterStateFault "api-faults.md#InvalidDBClusterStateFault")
- [InvalidDBSnapshotStateFault](api-faults.md#InvalidDBSnapshotStateFault "api-faults.md#InvalidDBSnapshotStateFault")
- [InvalidRestoreFault](api-faults.md#InvalidRestoreFault "api-faults.md#InvalidRestoreFault")
- [InvalidSubnet](api-faults.md#InvalidSubnet "api-faults.md#InvalidSubnet")
- [InvalidVPCNetworkStateFault](api-faults.md#InvalidVPCNetworkStateFault "api-faults.md#InvalidVPCNetworkStateFault")
- [KMSKeyNotAccessibleFault](api-faults.md#KMSKeyNotAccessibleFault "api-faults.md#KMSKeyNotAccessibleFault")
- [OptionGroupNotFoundFault](api-faults.md#OptionGroupNotFoundFault "api-faults.md#OptionGroupNotFoundFault")
- [StorageQuotaExceededFault](api-faults.md#StorageQuotaExceededFault "api-faults.md#StorageQuotaExceededFault")
- [DBClusterParameterGroupNotFoundFault](api-faults.md#DBClusterParameterGroupNotFoundFault "api-faults.md#DBClusterParameterGroupNotFoundFault")

## DescribeDBClusterSnapshots (action)

        The AWS CLI name for this API is: `describe-db-cluster-snapshots`.

Returns information about DB cluster snapshots. This API action supports
pagination.

**Request**

- **DBClusterIdentifier**  (in the CLI: `--db-cluster-identifier`) –  a String, of type: `string` (a UTF-8 encoded string).

The ID of the DB cluster to retrieve the list of DB cluster snapshots for.
This parameter can't be used in conjunction with the `DBClusterSnapshotIdentifier`
parameter. This parameter is not case-sensitive.

Constraints:

    + If supplied, must match the identifier of an existing DBCluster.

- **DBClusterSnapshotIdentifier**  (in the CLI: `--db-cluster-snapshot-identifier`) –  a String, of type: `string` (a UTF-8 encoded string).

A specific DB cluster snapshot identifier to describe. This parameter
can't be used in conjunction with the `DBClusterIdentifier` parameter.
This value is stored as a lowercase string.

Constraints:

    + If supplied, must match the identifier of an existing DBClusterSnapshot.
    + If this identifier is for an automated snapshot, the `SnapshotType`
     parameter must also be specified.

- **Filters**  (in the CLI: `--filters`) –  An array of [Filter](api-datatypes.md#Filter "api-datatypes.md#Filter") objects.

This parameter is not currently supported.

- **IncludePublic**  (in the CLI: `--include-public`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

True to include manual DB cluster snapshots that are public and can be copied
or restored by any Amazon account, and otherwise false. The default is `false`.
The default is false.

You can share a manual DB cluster snapshot as public by using the [ModifyDBClusterSnapshotAttribute (action)](#ModifyDBClusterSnapshotAttribute "#ModifyDBClusterSnapshotAttribute") API action.

- **IncludeShared**  (in the CLI: `--include-shared`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

True to include shared manual DB cluster snapshots from other Amazon accounts
that this Amazon account has been given permission to copy or restore, and otherwise
false. The default is `false`.

You can give an Amazon account permission to restore a manual DB cluster
snapshot from another Amazon account by the [ModifyDBClusterSnapshotAttribute (action)](#ModifyDBClusterSnapshotAttribute "#ModifyDBClusterSnapshotAttribute") API action.

- **Marker**  (in the CLI: `--marker`) –  a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous `DescribeDBClusterSnapshots`
request. If this parameter is specified, the response includes only records
beyond the marker, up to the value specified by `MaxRecords`.

- **MaxRecords**  (in the CLI: `--max-records`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The maximum number of records to include in the response. If more records
exist than the specified `MaxRecords` value, a pagination token
called a marker is included in the response so that the remaining results can be
retrieved.

Default: 100

Constraints: Minimum 20, maximum 100.

- **SnapshotType**  (in the CLI: `--snapshot-type`) –  a String, of type: `string` (a UTF-8 encoded string).

The type of DB cluster snapshots to be returned. You can specify one of the
following values:

    + `automated` - Return all DB cluster snapshots that have been
     automatically taken by Amazon Neptune for my Amazon account.
    + `manual` - Return all DB cluster snapshots that have been
     taken by my Amazon account.
    + `shared` - Return all manual DB cluster snapshots that have
     been shared to my Amazon account.
    + `public` - Return all DB cluster snapshots that have been
     marked as public.

If you don't specify a `SnapshotType` value, then both automated
and manual DB cluster snapshots are returned. You can include shared DB cluster
snapshots with these results by setting the `IncludeShared` parameter
to `true`. You can include public DB cluster snapshots with these
results by setting the `IncludePublic` parameter to `true`.

The `IncludeShared` and `IncludePublic` parameters
don't apply for `SnapshotType` values of `manual`
or `automated`. The `IncludePublic` parameter doesn't
apply when `SnapshotType` is set to `shared`. The `IncludeShared`
parameter doesn't apply when `SnapshotType` is set to `public`.

**Response**

- **DBClusterSnapshots**   – An array of [DBClusterSnapshot](#DBClusterSnapshot "#DBClusterSnapshot") objects.

Provides a list of DB cluster snapshots for the user.

- **Marker**   – a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous DescribeDBClusterSnapshots (action) request. If this parameter is specified, the response includes only records
beyond the marker, up to the value specified by `MaxRecords`.

###### Errors

- [DBClusterSnapshotNotFoundFault](api-faults.md#DBClusterSnapshotNotFoundFault "api-faults.md#DBClusterSnapshotNotFoundFault")

## DescribeDBClusterSnapshotAttributes (action)

        The AWS CLI name for this API is: `describe-db-cluster-snapshot-attributes`.

Returns a list of DB cluster snapshot attribute names and values for a manual
DB cluster snapshot.

When sharing snapshots with other Amazon accounts, `DescribeDBClusterSnapshotAttributes`
returns the `restore` attribute and a list of IDs for the Amazon accounts
that are authorized to copy or restore the manual DB cluster snapshot. If `all`
is included in the list of values for the `restore` attribute, then
the manual DB cluster snapshot is public and can be copied or restored by all Amazon
accounts.

To add or remove access for an Amazon account to copy or restore a manual
DB cluster snapshot, or to make the manual DB cluster snapshot public or private,
use the [ModifyDBClusterSnapshotAttribute (action)](#ModifyDBClusterSnapshotAttribute "#ModifyDBClusterSnapshotAttribute") API action.

**Request**

- **DBClusterSnapshotIdentifier**  (in the CLI: `--db-cluster-snapshot-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The identifier for the DB cluster snapshot to describe the attributes
for.

**Response**

Contains the results of a successful call to the DescribeDBClusterSnapshotAttributes (action) API action.

Manual DB cluster snapshot attributes are used to authorize other Amazon
accounts to copy or restore a manual DB cluster snapshot. For more information,
see the [ModifyDBClusterSnapshotAttribute (action)](#ModifyDBClusterSnapshotAttribute "#ModifyDBClusterSnapshotAttribute") API action.

- **DBClusterSnapshotAttributes**   – An array of [DBClusterSnapshotAttribute](#DBClusterSnapshotAttribute "#DBClusterSnapshotAttribute") objects.

The list of attributes and values for the manual DB cluster snapshot.

- **DBClusterSnapshotIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

The identifier of the manual DB cluster snapshot that the attributes apply
to.

###### Errors

- [DBClusterSnapshotNotFoundFault](api-faults.md#DBClusterSnapshotNotFoundFault "api-faults.md#DBClusterSnapshotNotFoundFault")

## _Structures:_

## DBClusterSnapshot (structure)

Contains the details for an Amazon Neptune DB cluster snapshot

This data type is used as a response element in the [DescribeDBClusterSnapshots (action)](#DescribeDBClusterSnapshots "#DescribeDBClusterSnapshots") action.

###### Fields

- **AllocatedStorage** – This is an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the allocated storage size in gibibytes (GiB).

- **AvailabilityZones** – This is a String, of type: `string` (a UTF-8 encoded string).

Provides the list of EC2 Availability Zones that instances in the DB cluster
snapshot can be restored in.

- **ClusterCreateTime** – This is a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Specifies the time when the DB cluster was created, in Universal Coordinated
Time (UTC).

- **DBClusterIdentifier** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the DB cluster identifier of the DB cluster that this DB cluster
snapshot was created from.

- **DBClusterSnapshotArn** – This is a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB cluster snapshot.

- **DBClusterSnapshotIdentifier** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the identifier for a DB cluster snapshot. Must match the identifier
of an existing snapshot.

After you restore a DB cluster using a `DBClusterSnapshotIdentifier`,
you must specify the same `DBClusterSnapshotIdentifier` for any
future updates to the DB cluster. When you specify this property for an update,
the DB cluster is not restored from the snapshot again, and the data in the database
is not changed.

However, if you don't specify the `DBClusterSnapshotIdentifier`,
an empty DB cluster is created, and the original DB cluster is deleted. If you specify
a property that is different from the previous snapshot restore property, the
DB cluster is restored from the snapshot specified by the `DBClusterSnapshotIdentifier`,
and the original DB cluster is deleted.

- **Engine** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the database engine.

- **EngineVersion** – This is a String, of type: `string` (a UTF-8 encoded string).

Provides the version of the database engine for this DB cluster snapshot.

- **IAMDatabaseAuthenticationEnabled** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

True if mapping of Amazon Identity and Access Management (IAM) accounts
to database accounts is enabled, and otherwise false.

- **KmsKeyId** – This is a String, of type: `string` (a UTF-8 encoded string).

If `StorageEncrypted` is true, the Amazon KMS key identifier
for the encrypted DB cluster snapshot.

- **LicenseModel** – This is a String, of type: `string` (a UTF-8 encoded string).

Provides the license model information for this DB cluster snapshot.

- **PercentProgress** – This is an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the percentage of the estimated data that has been transferred.

- **Port** – This is an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the port that the DB cluster was listening on at the time of the
snapshot.

- **SnapshotCreateTime** – This is a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

Provides the time when the snapshot was taken, in Universal Coordinated
Time (UTC).

- **SnapshotType** – This is a String, of type: `string` (a UTF-8 encoded string).

Provides the type of the DB cluster snapshot.

- **SourceDBClusterSnapshotArn** – This is a String, of type: `string` (a UTF-8 encoded string).

If the DB cluster snapshot was copied from a source DB cluster snapshot,
the Amazon Resource Name (ARN) for the source DB cluster snapshot, otherwise,
a null value.

- **Status** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the status of this DB cluster snapshot.

- **StorageEncrypted** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the DB cluster snapshot is encrypted.

- **StorageType** – This is a String, of type: `string` (a UTF-8 encoded string).

The storage type associated with the DB cluster snapshot.

- **VpcId** – This is a String, of type: `string` (a UTF-8 encoded string).

Provides the VPC ID associated with the DB cluster snapshot.

`DBClusterSnapshot` is used as the response element for:

- [CreateDBClusterSnapshot](#CreateDBClusterSnapshot "#CreateDBClusterSnapshot")
- [CopyDBClusterSnapshot](#CopyDBClusterSnapshot "#CopyDBClusterSnapshot")
- [DeleteDBClusterSnapshot](#DeleteDBClusterSnapshot "#DeleteDBClusterSnapshot")

## DBClusterSnapshotAttribute (structure)

Contains the name and values of a manual DB cluster snapshot attribute.

Manual DB cluster snapshot attributes are used to authorize other Amazon
accounts to restore a manual DB cluster snapshot. For more information, see the
[ModifyDBClusterSnapshotAttribute (action)](#ModifyDBClusterSnapshotAttribute "#ModifyDBClusterSnapshotAttribute") API action.

###### Fields

- **AttributeName** – This is a String, of type: `string` (a UTF-8 encoded string).

The name of the manual DB cluster snapshot attribute.

The attribute named `restore` refers to the list of Amazon
accounts that have permission to copy or restore the manual DB cluster snapshot.
For more information, see the [ModifyDBClusterSnapshotAttribute (action)](#ModifyDBClusterSnapshotAttribute "#ModifyDBClusterSnapshotAttribute") API action.

- **AttributeValues** – This is a String, of type: `string` (a UTF-8 encoded string).

The value(s) for the manual DB cluster snapshot attribute.

If the `AttributeName` field is set to `restore`,
then this element returns a list of IDs of the Amazon accounts that are authorized
to copy or restore the manual DB cluster snapshot. If a value of `all`
is in the list, then the manual DB cluster snapshot is public and available for
any Amazon account to copy or restore.

## DBClusterSnapshotAttributesResult (structure)

Contains the results of a successful call to the [DescribeDBClusterSnapshotAttributes (action)](#DescribeDBClusterSnapshotAttributes "#DescribeDBClusterSnapshotAttributes") API action.

Manual DB cluster snapshot attributes are used to authorize other Amazon
accounts to copy or restore a manual DB cluster snapshot. For more information,
see the [ModifyDBClusterSnapshotAttribute (action)](#ModifyDBClusterSnapshotAttribute "#ModifyDBClusterSnapshotAttribute") API action.

###### Fields

- **DBClusterSnapshotAttributes** – This is An array of [DBClusterSnapshotAttribute](#DBClusterSnapshotAttribute "#DBClusterSnapshotAttribute") objects.

The list of attributes and values for the manual DB cluster snapshot.

- **DBClusterSnapshotIdentifier** – This is a String, of type: `string` (a UTF-8 encoded string).

The identifier of the manual DB cluster snapshot that the attributes apply
to.

`DBClusterSnapshotAttributesResult` is used as the response element for:

- [DescribeDBClusterSnapshotAttributes](#DescribeDBClusterSnapshotAttributes "#DescribeDBClusterSnapshotAttributes")
- [ModifyDBClusterSnapshotAttribute](#ModifyDBClusterSnapshotAttribute "#ModifyDBClusterSnapshotAttribute")
