# Neptune Global Database API

**Actions:**

- [CreateGlobalCluster (action)](#CreateGlobalCluster "#CreateGlobalCluster")
- [DeleteGlobalCluster (action)](#DeleteGlobalCluster "#DeleteGlobalCluster")
- [ModifyGlobalCluster (action)](#ModifyGlobalCluster "#ModifyGlobalCluster")
- [DescribeGlobalClusters (action)](#DescribeGlobalClusters "#DescribeGlobalClusters")
- [FailoverGlobalCluster (action)](#FailoverGlobalCluster "#FailoverGlobalCluster")
- [RemoveFromGlobalCluster (action)](#RemoveFromGlobalCluster "#RemoveFromGlobalCluster")
  **Structures:**

- [GlobalCluster (structure)](#GlobalCluster "#GlobalCluster")
- [GlobalClusterMember (structure)](#GlobalClusterMember "#GlobalClusterMember")

## CreateGlobalCluster (action)

        The AWS CLI name for this API is: `create-global-cluster`.

Creates a Neptune global database spread across multiple Amazon Regions.
The global database contains a single primary cluster with read-write capability,
and read-only secondary clusters that receive data from the primary cluster
through high-speed replication performed by the Neptune storage subsystem.

You can create a global database that is initially empty, and then add a
primary cluster and secondary clusters to it, or you can specify an existing Neptune
cluster during the create operation to become the primary cluster of the global
database.

**Request**

- **DatabaseName**  (in the CLI: `--database-name`) –  a String, of type: `string` (a UTF-8 encoded string).

The name for the new global database (up to 64 alpha-numeric characters.

- **DeletionProtection**  (in the CLI: `--deletion-protection`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

The deletion protection setting for the new global database. The global
database can't be deleted when deletion protection is enabled.

- **Engine**  (in the CLI: `--engine`) –  a String, of type: `string` (a UTF-8 encoded string).

The name of the database engine to be used in the global database.

Valid values: `neptune`

- **EngineVersion**  (in the CLI: `--engine-version`) –  a String, of type: `string` (a UTF-8 encoded string).

The Neptune engine version to be used by the global database.

Valid values: `1.2.0.0` or above.

- **GlobalClusterIdentifier**  (in the CLI: `--global-cluster-identifier`) –  _Required:_ a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

The cluster identifier of the new global database cluster.

- **SourceDBClusterIdentifier**  (in the CLI: `--source-db-cluster-identifier`) –  a String, of type: `string` (a UTF-8 encoded string).

(_Optional_) The Amazon Resource Name (ARN) of
an existing Neptune DB cluster to use as the primary cluster of the new global database.

- **StorageEncrypted**  (in the CLI: `--storage-encrypted`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

The storage encryption setting for the new global database cluster.

**Response**

Contains the details of an Amazon Neptune global database.

This data type is used as a response element for the CreateGlobalCluster (action), [DescribeGlobalClusters (action)](#DescribeGlobalClusters "#DescribeGlobalClusters"), [ModifyGlobalCluster (action)](#ModifyGlobalCluster "#ModifyGlobalCluster"), [DeleteGlobalCluster (action)](#DeleteGlobalCluster "#DeleteGlobalCluster"), [FailoverGlobalCluster (action)](#FailoverGlobalCluster "#FailoverGlobalCluster"), and [RemoveFromGlobalCluster (action)](#RemoveFromGlobalCluster "#RemoveFromGlobalCluster") actions.

- **DeletionProtection**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

The deletion protection setting for the global database.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

The Neptune database engine used by the global database (`"neptune"`).

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

The Neptune engine version used by the global database.

- **GlobalClusterArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the global database.

- **GlobalClusterIdentifier**   – a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

Contains a user-supplied global database cluster identifier. This identifier
is the unique key that identifies a global database.

- **GlobalClusterMembers**   – An array of [GlobalClusterMember](#GlobalClusterMember "#GlobalClusterMember") objects.

A list of cluster ARNs and instance ARNs for all the DB clusters that are
part of the global database.

- **GlobalClusterResourceId**   – a String, of type: `string` (a UTF-8 encoded string).

An immutable identifier for the global database that is unique within
in all regions. This identifier is found in CloudTrail log entries whenever the
KMS key for the DB cluster is accessed.

- **Status**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this global database.

- **StorageEncrypted**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

The storage encryption setting for the global database.

###### Errors

- [GlobalClusterAlreadyExistsFault](api-faults.md#GlobalClusterAlreadyExistsFault "api-faults.md#GlobalClusterAlreadyExistsFault")
- [GlobalClusterQuotaExceededFault](api-faults.md#GlobalClusterQuotaExceededFault "api-faults.md#GlobalClusterQuotaExceededFault")
- [InvalidDBClusterStateFault](api-faults.md#InvalidDBClusterStateFault "api-faults.md#InvalidDBClusterStateFault")
- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")

## DeleteGlobalCluster (action)

        The AWS CLI name for this API is: `delete-global-cluster`.

Deletes a global database. The primary and all secondary clusters must
already be detached or deleted first.

**Request**

- **GlobalClusterIdentifier**  (in the CLI: `--global-cluster-identifier`) –  _Required:_ a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

The cluster identifier of the global database cluster being deleted.

**Response**

Contains the details of an Amazon Neptune global database.

This data type is used as a response element for the [CreateGlobalCluster (action)](#CreateGlobalCluster "#CreateGlobalCluster"), [DescribeGlobalClusters (action)](#DescribeGlobalClusters "#DescribeGlobalClusters"), [ModifyGlobalCluster (action)](#ModifyGlobalCluster "#ModifyGlobalCluster"), DeleteGlobalCluster (action), [FailoverGlobalCluster (action)](#FailoverGlobalCluster "#FailoverGlobalCluster"), and [RemoveFromGlobalCluster (action)](#RemoveFromGlobalCluster "#RemoveFromGlobalCluster") actions.

- **DeletionProtection**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

The deletion protection setting for the global database.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

The Neptune database engine used by the global database (`"neptune"`).

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

The Neptune engine version used by the global database.

- **GlobalClusterArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the global database.

- **GlobalClusterIdentifier**   – a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

Contains a user-supplied global database cluster identifier. This identifier
is the unique key that identifies a global database.

- **GlobalClusterMembers**   – An array of [GlobalClusterMember](#GlobalClusterMember "#GlobalClusterMember") objects.

A list of cluster ARNs and instance ARNs for all the DB clusters that are
part of the global database.

- **GlobalClusterResourceId**   – a String, of type: `string` (a UTF-8 encoded string).

An immutable identifier for the global database that is unique within
in all regions. This identifier is found in CloudTrail log entries whenever the
KMS key for the DB cluster is accessed.

- **Status**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this global database.

- **StorageEncrypted**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

The storage encryption setting for the global database.

###### Errors

- [GlobalClusterNotFoundFault](api-faults.md#GlobalClusterNotFoundFault "api-faults.md#GlobalClusterNotFoundFault")
- [InvalidGlobalClusterStateFault](api-faults.md#InvalidGlobalClusterStateFault "api-faults.md#InvalidGlobalClusterStateFault")

## ModifyGlobalCluster (action)

        The AWS CLI name for this API is: `modify-global-cluster`.

Modify a setting for an Amazon Neptune global cluster. You can change one
or more database configuration parameters by specifying these parameters and
their new values in the request.

**Request**

- **AllowMajorVersionUpgrade**  (in the CLI: `--allow-major-version-upgrade`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

A value that indicates whether major version upgrades are allowed.

Constraints: You must allow major version upgrades if you specify a value
for the `EngineVersion` parameter that is a different major version
than the DB cluster's current version.

If you upgrade the major version of a global database, the cluster and DB
instance parameter groups are set to the default parameter groups for the new
version, so you will need to apply any custom parameter groups after completing
the upgrade.

- **DeletionProtection**  (in the CLI: `--deletion-protection`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

Indicates whether the global database has deletion protection enabled.
The global database cannot be deleted when deletion protection is enabled.

- **EngineVersion**  (in the CLI: `--engine-version`) –  a String, of type: `string` (a UTF-8 encoded string).

The version number of the database engine to which you want to upgrade.
Changing this parameter will result in an outage. The change is applied during
the next maintenance window unless `ApplyImmediately` is enabled.

To list all of the available Neptune engine versions, use the following
command:

###### Example

```
aws neptune describe-db-engine-versions \
          --engine neptune \
          --query '*[]|[?SupportsGlobalDatabases == 'true'].[EngineVersion]'
```

- **GlobalClusterIdentifier**  (in the CLI: `--global-cluster-identifier`) –  _Required:_ a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

The DB cluster identifier for the global cluster being modified. This
parameter is not case-sensitive.

Constraints: Must match the identifier of an existing global database
cluster.

- **NewGlobalClusterIdentifier**  (in the CLI: `--new-global-cluster-identifier`) –  a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

A new cluster identifier to assign to the global database. This value is
stored as a lowercase string.

Constraints:

    + Must contain from 1 to 63 letters, numbers, or hyphens.
    + The first character must be a letter.
    + Can't end with a hyphen or contain two consecutive hyphens

Example: `my-cluster2`

**Response**

Contains the details of an Amazon Neptune global database.

This data type is used as a response element for the [CreateGlobalCluster (action)](#CreateGlobalCluster "#CreateGlobalCluster"), [DescribeGlobalClusters (action)](#DescribeGlobalClusters "#DescribeGlobalClusters"), ModifyGlobalCluster (action), [DeleteGlobalCluster (action)](#DeleteGlobalCluster "#DeleteGlobalCluster"), [FailoverGlobalCluster (action)](#FailoverGlobalCluster "#FailoverGlobalCluster"), and [RemoveFromGlobalCluster (action)](#RemoveFromGlobalCluster "#RemoveFromGlobalCluster") actions.

- **DeletionProtection**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

The deletion protection setting for the global database.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

The Neptune database engine used by the global database (`"neptune"`).

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

The Neptune engine version used by the global database.

- **GlobalClusterArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the global database.

- **GlobalClusterIdentifier**   – a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

Contains a user-supplied global database cluster identifier. This identifier
is the unique key that identifies a global database.

- **GlobalClusterMembers**   – An array of [GlobalClusterMember](#GlobalClusterMember "#GlobalClusterMember") objects.

A list of cluster ARNs and instance ARNs for all the DB clusters that are
part of the global database.

- **GlobalClusterResourceId**   – a String, of type: `string` (a UTF-8 encoded string).

An immutable identifier for the global database that is unique within
in all regions. This identifier is found in CloudTrail log entries whenever the
KMS key for the DB cluster is accessed.

- **Status**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this global database.

- **StorageEncrypted**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

The storage encryption setting for the global database.

###### Errors

- [GlobalClusterNotFoundFault](api-faults.md#GlobalClusterNotFoundFault "api-faults.md#GlobalClusterNotFoundFault")
- [InvalidGlobalClusterStateFault](api-faults.md#InvalidGlobalClusterStateFault "api-faults.md#InvalidGlobalClusterStateFault")

## DescribeGlobalClusters (action)

        The AWS CLI name for this API is: `describe-global-clusters`.

Returns information about Neptune global database clusters. This API
supports pagination.

**Request**

- **GlobalClusterIdentifier**  (in the CLI: `--global-cluster-identifier`) –  a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

The user-supplied DB cluster identifier. If this parameter is specified,
only information about the specified DB cluster is returned. This parameter
is not case-sensitive.

Constraints: If supplied, must match an existing DB cluster identifier.

- **Marker**  (in the CLI: `--marker`) –  a String, of type: `string` (a UTF-8 encoded string).

(_Optional_) A pagination token returned by a previous
call to `DescribeGlobalClusters`. If this parameter is specified,
the response will only include records beyond the marker, up to the number specified
by `MaxRecords`.

- **MaxRecords**  (in the CLI: `--max-records`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The maximum number of records to include in the response. If more records
exist than the specified `MaxRecords` value, a pagination marker
token is included in the response that you can use to retrieve the remaining results.

Default: `100`

Constraints: Minimum 20, maximum 100.

**Response**

- **GlobalClusters**   – An array of [GlobalCluster](#GlobalCluster "#GlobalCluster") objects.

The list of global clusters and instances returned by this request.

- **Marker**   – a String, of type: `string` (a UTF-8 encoded string).

A pagination token. If this parameter is returned in the response, more
records are available, which can be retrieved by one or more additional calls
to `DescribeGlobalClusters`.

###### Errors

- [GlobalClusterNotFoundFault](api-faults.md#GlobalClusterNotFoundFault "api-faults.md#GlobalClusterNotFoundFault")

## FailoverGlobalCluster (action)

        The AWS CLI name for this API is: `failover-global-cluster`.

Initiates the failover process for a Neptune global database.

A failover for a Neptune global database promotes one of secondary read-only
DB clusters to be the primary DB cluster and demotes the primary DB cluster to being
a secondary (read-only) DB cluster. In other words, the role of the current primary
DB cluster and the selected target secondary DB cluster are switched. The selected
secondary DB cluster assumes full read/write capabilities for the Neptune global
database.

###### Note

This action applies **only** to Neptune
global databases. This action is only intended for use on healthy Neptune global
databases with healthy Neptune DB clusters and no region-wide outages, to test
disaster recovery scenarios or to reconfigure the global database topology.

**Request**

- **GlobalClusterIdentifier**  (in the CLI: `--global-cluster-identifier`) –  _Required:_ a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

Identifier of the Neptune global database that should be failed over.
The identifier is the unique key assigned by the user when the Neptune global database
was created. In other words, it's the name of the global database that you want
to fail over.

Constraints: Must match the identifier of an existing Neptune global
database.

- **TargetDbClusterIdentifier**  (in the CLI: `--target-db-cluster-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) of the secondary Neptune DB cluster that
you want to promote to primary for the global database.

**Response**

Contains the details of an Amazon Neptune global database.

This data type is used as a response element for the [CreateGlobalCluster (action)](#CreateGlobalCluster "#CreateGlobalCluster"), [DescribeGlobalClusters (action)](#DescribeGlobalClusters "#DescribeGlobalClusters"), [ModifyGlobalCluster (action)](#ModifyGlobalCluster "#ModifyGlobalCluster"), [DeleteGlobalCluster (action)](#DeleteGlobalCluster "#DeleteGlobalCluster"), FailoverGlobalCluster (action), and [RemoveFromGlobalCluster (action)](#RemoveFromGlobalCluster "#RemoveFromGlobalCluster") actions.

- **DeletionProtection**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

The deletion protection setting for the global database.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

The Neptune database engine used by the global database (`"neptune"`).

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

The Neptune engine version used by the global database.

- **GlobalClusterArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the global database.

- **GlobalClusterIdentifier**   – a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

Contains a user-supplied global database cluster identifier. This identifier
is the unique key that identifies a global database.

- **GlobalClusterMembers**   – An array of [GlobalClusterMember](#GlobalClusterMember "#GlobalClusterMember") objects.

A list of cluster ARNs and instance ARNs for all the DB clusters that are
part of the global database.

- **GlobalClusterResourceId**   – a String, of type: `string` (a UTF-8 encoded string).

An immutable identifier for the global database that is unique within
in all regions. This identifier is found in CloudTrail log entries whenever the
KMS key for the DB cluster is accessed.

- **Status**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this global database.

- **StorageEncrypted**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

The storage encryption setting for the global database.

###### Errors

- [GlobalClusterNotFoundFault](api-faults.md#GlobalClusterNotFoundFault "api-faults.md#GlobalClusterNotFoundFault")
- [InvalidGlobalClusterStateFault](api-faults.md#InvalidGlobalClusterStateFault "api-faults.md#InvalidGlobalClusterStateFault")
- [InvalidDBClusterStateFault](api-faults.md#InvalidDBClusterStateFault "api-faults.md#InvalidDBClusterStateFault")
- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")

## RemoveFromGlobalCluster (action)

        The AWS CLI name for this API is: `remove-from-global-cluster`.

Detaches a Neptune DB cluster from a Neptune global database. A secondary
cluster becomes a normal standalone cluster with read-write capability instead
of being read-only, and no longer receives data from a the primary cluster.

**Request**

- **DbClusterIdentifier**  (in the CLI: `--db-cluster-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) identifying the cluster to be detached
from the Neptune global database cluster.

- **GlobalClusterIdentifier**  (in the CLI: `--global-cluster-identifier`) –  _Required:_ a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

The identifier of the Neptune global database from which to detach the
specified Neptune DB cluster.

**Response**

Contains the details of an Amazon Neptune global database.

This data type is used as a response element for the [CreateGlobalCluster (action)](#CreateGlobalCluster "#CreateGlobalCluster"), [DescribeGlobalClusters (action)](#DescribeGlobalClusters "#DescribeGlobalClusters"), [ModifyGlobalCluster (action)](#ModifyGlobalCluster "#ModifyGlobalCluster"), [DeleteGlobalCluster (action)](#DeleteGlobalCluster "#DeleteGlobalCluster"), [FailoverGlobalCluster (action)](#FailoverGlobalCluster "#FailoverGlobalCluster"), and RemoveFromGlobalCluster (action) actions.

- **DeletionProtection**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

The deletion protection setting for the global database.

- **Engine**   – a String, of type: `string` (a UTF-8 encoded string).

The Neptune database engine used by the global database (`"neptune"`).

- **EngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

The Neptune engine version used by the global database.

- **GlobalClusterArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the global database.

- **GlobalClusterIdentifier**   – a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

Contains a user-supplied global database cluster identifier. This identifier
is the unique key that identifies a global database.

- **GlobalClusterMembers**   – An array of [GlobalClusterMember](#GlobalClusterMember "#GlobalClusterMember") objects.

A list of cluster ARNs and instance ARNs for all the DB clusters that are
part of the global database.

- **GlobalClusterResourceId**   – a String, of type: `string` (a UTF-8 encoded string).

An immutable identifier for the global database that is unique within
in all regions. This identifier is found in CloudTrail log entries whenever the
KMS key for the DB cluster is accessed.

- **Status**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this global database.

- **StorageEncrypted**   – a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

The storage encryption setting for the global database.

###### Errors

- [GlobalClusterNotFoundFault](api-faults.md#GlobalClusterNotFoundFault "api-faults.md#GlobalClusterNotFoundFault")
- [InvalidGlobalClusterStateFault](api-faults.md#InvalidGlobalClusterStateFault "api-faults.md#InvalidGlobalClusterStateFault")
- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")

## _Structures:_

## GlobalCluster (structure)

Contains the details of an Amazon Neptune global database.

This data type is used as a response element for the [CreateGlobalCluster (action)](#CreateGlobalCluster "#CreateGlobalCluster"), [DescribeGlobalClusters (action)](#DescribeGlobalClusters "#DescribeGlobalClusters"), [ModifyGlobalCluster (action)](#ModifyGlobalCluster "#ModifyGlobalCluster"), [DeleteGlobalCluster (action)](#DeleteGlobalCluster "#DeleteGlobalCluster"), [FailoverGlobalCluster (action)](#FailoverGlobalCluster "#FailoverGlobalCluster"), and [RemoveFromGlobalCluster (action)](#RemoveFromGlobalCluster "#RemoveFromGlobalCluster") actions.

###### Fields

- **DeletionProtection** – This is a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

The deletion protection setting for the global database.

- **Engine** – This is a String, of type: `string` (a UTF-8 encoded string).

The Neptune database engine used by the global database (`"neptune"`).

- **EngineVersion** – This is a String, of type: `string` (a UTF-8 encoded string).

The Neptune engine version used by the global database.

- **GlobalClusterArn** – This is a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the global database.

- **GlobalClusterIdentifier** – This is a GlobalClusterIdentifier, of type: `string` (a UTF-8 encoded string), not less than 1 or more than 255 ?st?s, matching this regular expression: `[A-Za-z][0-9A-Za-z-:._]*`.

Contains a user-supplied global database cluster identifier. This identifier
is the unique key that identifies a global database.

- **GlobalClusterMembers** – This is An array of [GlobalClusterMember](#GlobalClusterMember "#GlobalClusterMember") objects.

A list of cluster ARNs and instance ARNs for all the DB clusters that are
part of the global database.

- **GlobalClusterResourceId** – This is a String, of type: `string` (a UTF-8 encoded string).

An immutable identifier for the global database that is unique within
in all regions. This identifier is found in CloudTrail log entries whenever the
KMS key for the DB cluster is accessed.

- **Status** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the current state of this global database.

- **StorageEncrypted** – This is a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

The storage encryption setting for the global database.

`GlobalCluster` is used as the response element for:

- [CreateGlobalCluster](#CreateGlobalCluster "#CreateGlobalCluster")
- [ModifyGlobalCluster](#ModifyGlobalCluster "#ModifyGlobalCluster")
- [DeleteGlobalCluster](#DeleteGlobalCluster "#DeleteGlobalCluster")
- [RemoveFromGlobalCluster](#RemoveFromGlobalCluster "#RemoveFromGlobalCluster")
- [FailoverGlobalCluster](#FailoverGlobalCluster "#FailoverGlobalCluster")

## GlobalClusterMember (structure)

A data structure with information about any primary and secondary clusters
associated with an Neptune global database.

###### Fields

- **DBClusterArn** – This is a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for each Neptune cluster.

- **IsWriter** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether the Neptune cluster is the primary cluster (that is,
has read-write capability) for the Neptune global database with which it is associated.

- **Readers** – This is a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for each read-only secondary cluster associated
with the Neptune global database.
