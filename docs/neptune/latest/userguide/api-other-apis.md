# Other Neptune APIs

**Actions:**

- [AddTagsToResource (action)](#AddTagsToResource "#AddTagsToResource")
- [ListTagsForResource (action)](#ListTagsForResource "#ListTagsForResource")
- [RemoveTagsFromResource (action)](#RemoveTagsFromResource "#RemoveTagsFromResource")
- [ApplyPendingMaintenanceAction (action)](#ApplyPendingMaintenanceAction "#ApplyPendingMaintenanceAction")
- [DescribePendingMaintenanceActions (action)](#DescribePendingMaintenanceActions "#DescribePendingMaintenanceActions")
- [DescribeDBEngineVersions (action)](#DescribeDBEngineVersions "#DescribeDBEngineVersions")
  **Structures:**

- [DBEngineVersion (structure)](#DBEngineVersion "#DBEngineVersion")
- [EngineDefaults (structure)](#EngineDefaults "#EngineDefaults")
- [PendingMaintenanceAction (structure)](#PendingMaintenanceAction "#PendingMaintenanceAction")
- [ResourcePendingMaintenanceActions (structure)](#ResourcePendingMaintenanceActions "#ResourcePendingMaintenanceActions")
- [UpgradeTarget (structure)](#UpgradeTarget "#UpgradeTarget")
- [Tag (structure)](#Tag "#Tag")

## AddTagsToResource (action)

        The AWS CLI name for this API is: `add-tags-to-resource`.

Adds metadata tags to an Amazon Neptune resource. These tags can also be
used with cost allocation reporting to track cost associated with Amazon Neptune
resources, or used in a Condition statement in an IAM policy for Amazon Neptune.

**Request**

- **ResourceName**  (in the CLI: `--resource-name`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The Amazon Neptune resource that the tags are added to. This value is an
Amazon Resource Name (ARN). For information about creating an ARN, see [Constructing an Amazon Resource Name (ARN)](../UserGuide/tagging.md#tagging.ARN.Constructing "../UserGuide/tagging.md#tagging.ARN.Constructing").

- **Tags**  (in the CLI: `--tags`) –  _Required:_ An array of [Tag](#Tag "#Tag") objects.

The tags to be assigned to the Amazon Neptune resource.

###### Response

- _No Response parameters._

###### Errors

- [DBInstanceNotFoundFault](api-faults.md#DBInstanceNotFoundFault "api-faults.md#DBInstanceNotFoundFault")
- [DBSnapshotNotFoundFault](api-faults.md#DBSnapshotNotFoundFault "api-faults.md#DBSnapshotNotFoundFault")
- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")

## ListTagsForResource (action)

        The AWS CLI name for this API is: `list-tags-for-resource`.

Lists all tags on an Amazon Neptune resource.

**Request**

- **Filters**  (in the CLI: `--filters`) –  An array of [Filter](api-datatypes.md#Filter "api-datatypes.md#Filter") objects.

This parameter is not currently supported.

- **ResourceName**  (in the CLI: `--resource-name`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The Amazon Neptune resource with tags to be listed. This value is an Amazon
Resource Name (ARN). For information about creating an ARN, see [Constructing an Amazon Resource Name (ARN)](../UserGuide/tagging.md#tagging.ARN.Constructing "../UserGuide/tagging.md#tagging.ARN.Constructing").

**Response**

- **TagList**   – An array of [Tag](#Tag "#Tag") objects.

List of tags returned by the ListTagsForResource operation.

###### Errors

- [DBInstanceNotFoundFault](api-faults.md#DBInstanceNotFoundFault "api-faults.md#DBInstanceNotFoundFault")
- [DBSnapshotNotFoundFault](api-faults.md#DBSnapshotNotFoundFault "api-faults.md#DBSnapshotNotFoundFault")
- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")

## RemoveTagsFromResource (action)

        The AWS CLI name for this API is: `remove-tags-from-resource`.

Removes metadata tags from an Amazon Neptune resource.

**Request**

- **ResourceName**  (in the CLI: `--resource-name`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The Amazon Neptune resource that the tags are removed from. This value
is an Amazon Resource Name (ARN). For information about creating an ARN, see [Constructing an Amazon Resource Name (ARN)](../UserGuide/tagging.md#tagging.ARN.Constructing "../UserGuide/tagging.md#tagging.ARN.Constructing").

- **TagKeys**  (in the CLI: `--tag-keys`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The tag key (name) of the tag to be removed.

###### Response

- _No Response parameters._

###### Errors

- [DBInstanceNotFoundFault](api-faults.md#DBInstanceNotFoundFault "api-faults.md#DBInstanceNotFoundFault")
- [DBSnapshotNotFoundFault](api-faults.md#DBSnapshotNotFoundFault "api-faults.md#DBSnapshotNotFoundFault")
- [DBClusterNotFoundFault](api-faults.md#DBClusterNotFoundFault "api-faults.md#DBClusterNotFoundFault")

## ApplyPendingMaintenanceAction (action)

        The AWS CLI name for this API is: `apply-pending-maintenance-action`.

Applies a pending maintenance action to a resource (for example, to a DB
instance).

**Request**

- **ApplyAction**  (in the CLI: `--apply-action`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The pending maintenance action to apply to this resource.

Valid values: `system-update`, `db-upgrade`

- **OptInType**  (in the CLI: `--opt-in-type`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A value that specifies the type of opt-in request, or undoes an opt-in request.
An opt-in request of type `immediate` can't be undone.

Valid values:

    + `immediate` - Apply the maintenance action immediately.
    + `next-maintenance` - Apply the maintenance action during
     the next maintenance window for the resource.
    + `undo-opt-in` - Cancel any existing `next-maintenance`
     opt-in requests.

- **ResourceIdentifier**  (in the CLI: `--resource-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) of the resource that the pending maintenance
action applies to. For information about creating an ARN, see [Constructing an Amazon Resource Name (ARN)](../UserGuide/tagging.md#tagging.ARN.Constructing "../UserGuide/tagging.md#tagging.ARN.Constructing").

**Response**

Describes the pending maintenance actions for a resource.

- **PendingMaintenanceActionDetails**   – An array of [PendingMaintenanceAction](#PendingMaintenanceAction "#PendingMaintenanceAction") objects.

A list that provides details about the pending maintenance actions for
the resource.

- **ResourceIdentifier**   – a String, of type: `string` (a UTF-8 encoded string).

The ARN of the resource that has pending maintenance actions.

###### Errors

- [ResourceNotFoundFault](api-faults.md#ResourceNotFoundFault "api-faults.md#ResourceNotFoundFault")

## DescribePendingMaintenanceActions (action)

        The AWS CLI name for this API is: `describe-pending-maintenance-actions`.

Returns a list of resources (for example, DB instances) that have at least
one pending maintenance action.

**Request**

- **Filters**  (in the CLI: `--filters`) –  An array of [Filter](api-datatypes.md#Filter "api-datatypes.md#Filter") objects.

A filter that specifies one or more resources to return pending maintenance
actions for.

Supported filters:

    + `db-cluster-id` - Accepts DB cluster identifiers and DB
     cluster Amazon Resource Names (ARNs). The results list will only include pending
     maintenance actions for the DB clusters identified by these ARNs.
    + `db-instance-id` - Accepts DB instance identifiers and
     DB instance ARNs. The results list will only include pending maintenance actions
     for the DB instances identified by these ARNs.

- **Marker**  (in the CLI: `--marker`) –  a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous `DescribePendingMaintenanceActions`
request. If this parameter is specified, the response includes only records
beyond the marker, up to a number of records specified by `MaxRecords`.

- **MaxRecords**  (in the CLI: `--max-records`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The maximum number of records to include in the response. If more records
exist than the specified `MaxRecords` value, a pagination token
called a marker is included in the response so that the remaining results can be
retrieved.

Default: 100

Constraints: Minimum 20, maximum 100.

- **ResourceIdentifier**  (in the CLI: `--resource-identifier`) –  a String, of type: `string` (a UTF-8 encoded string).

The ARN of a resource to return pending maintenance actions for.

**Response**

- **Marker**   – a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous `DescribePendingMaintenanceActions`
request. If this parameter is specified, the response includes only records
beyond the marker, up to a number of records specified by `MaxRecords`.

- **PendingMaintenanceActions**   – An array of [ResourcePendingMaintenanceActions](#ResourcePendingMaintenanceActions "#ResourcePendingMaintenanceActions") objects.

A list of the pending maintenance actions for the resource.

###### Errors

- [ResourceNotFoundFault](api-faults.md#ResourceNotFoundFault "api-faults.md#ResourceNotFoundFault")

## DescribeDBEngineVersions (action)

        The AWS CLI name for this API is: `describe-db-engine-versions`.

Returns a list of the available DB engines.

**Request**

- **DBParameterGroupFamily**  (in the CLI: `--db-parameter-group-family`) –  a String, of type: `string` (a UTF-8 encoded string).

The name of a specific DB parameter group family to return details for.

Constraints:

    + If supplied, must match an existing DBParameterGroupFamily.

- **DefaultOnly**  (in the CLI: `--default-only`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

Indicates that only the default version of the specified engine or engine
and major version combination is returned.

- **Engine**  (in the CLI: `--engine`) –  a String, of type: `string` (a UTF-8 encoded string).

The database engine to return.

- **EngineVersion**  (in the CLI: `--engine-version`) –  a String, of type: `string` (a UTF-8 encoded string).

The database engine version to return.

Example: `5.1.49`

- **Filters**  (in the CLI: `--filters`) –  An array of [Filter](api-datatypes.md#Filter "api-datatypes.md#Filter") objects.

Not currently supported.

- **ListSupportedCharacterSets**  (in the CLI: `--list-supported-character-sets`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

If this parameter is specified and the requested engine supports the `CharacterSetName`
parameter for `CreateDBInstance`, the response includes a list
of supported character sets for each engine version.

- **ListSupportedTimezones**  (in the CLI: `--list-supported-timezones`) –  a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

If this parameter is specified and the requested engine supports the `TimeZone`
parameter for `CreateDBInstance`, the response includes a list
of supported time zones for each engine version.

- **Marker**  (in the CLI: `--marker`) –  a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous request. If this parameter
is specified, the response includes only records beyond the marker, up to the
value specified by `MaxRecords`.

- **MaxRecords**  (in the CLI: `--max-records`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The maximum number of records to include in the response. If more than the
`MaxRecords` value is available, a pagination token called a marker
is included in the response so that the following results can be retrieved.

Default: 100

Constraints: Minimum 20, maximum 100.

**Response**

- **DBEngineVersions**   – An array of [DBEngineVersion](#DBEngineVersion "#DBEngineVersion") objects.

A list of `DBEngineVersion` elements.

- **Marker**   – a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous request. If this parameter
is specified, the response includes only records beyond the marker, up to the
value specified by `MaxRecords`.

## _Structures:_

## DBEngineVersion (structure)

This data type is used as a response element in the action [DescribeDBEngineVersions (action)](#DescribeDBEngineVersions "#DescribeDBEngineVersions").

###### Fields

- **DBEngineDescription** – This is a String, of type: `string` (a UTF-8 encoded string).

The description of the database engine.

- **DBEngineVersionDescription** – This is a String, of type: `string` (a UTF-8 encoded string).

The description of the database engine version.

- **DBParameterGroupFamily** – This is a String, of type: `string` (a UTF-8 encoded string).

The name of the DB parameter group family for the database engine.

- **Engine** – This is a String, of type: `string` (a UTF-8 encoded string).

The name of the database engine.

- **EngineVersion** – This is a String, of type: `string` (a UTF-8 encoded string).

The version number of the database engine.

- **ExportableLogTypes** – This is a String, of type: `string` (a UTF-8 encoded string).

The types of logs that the database engine has available for export to CloudWatch
Logs.

- **SupportedTimezones** – This is An array of [Timezone](api-datatypes.md#Timezone "api-datatypes.md#Timezone") objects.

A list of the time zones supported by this engine for the `Timezone`
parameter of the `CreateDBInstance` action.

- **SupportsGlobalDatabases** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

A value that indicates whether you can use Aurora global databases with
a specific DB engine version.

- **SupportsLogExportsToCloudwatchLogs** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

A value that indicates whether the engine version supports exporting
the log types specified by ExportableLogTypes to CloudWatch Logs.

- **SupportsReadReplica** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Indicates whether the database engine version supports read replicas.

- **ValidUpgradeTarget** – This is An array of [UpgradeTarget](#UpgradeTarget "#UpgradeTarget") objects.

A list of engine versions that this database engine version can be upgraded
to.

## EngineDefaults (structure)

Contains the result of a successful invocation of the [DescribeEngineDefaultParameters (action)](api-parameters.md#DescribeEngineDefaultParameters "api-parameters.md#DescribeEngineDefaultParameters") action.

###### Fields

- **DBParameterGroupFamily** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the DB parameter group family that the engine default
parameters apply to.

- **Marker** – This is a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous EngineDefaults request.
If this parameter is specified, the response includes only records beyond the
marker, up to the value specified by `MaxRecords` .

- **Parameters** – This is An array of [Parameter](api-parameters.md#Parameter "api-parameters.md#Parameter") objects.

Contains a list of engine default parameters.

`EngineDefaults` is used as the response element for:

- [DescribeEngineDefaultParameters](api-parameters.md#DescribeEngineDefaultParameters "api-parameters.md#DescribeEngineDefaultParameters")
- [DescribeEngineDefaultClusterParameters](api-parameters.md#DescribeEngineDefaultClusterParameters "api-parameters.md#DescribeEngineDefaultClusterParameters")

## PendingMaintenanceAction (structure)

Provides information about a pending maintenance action for a resource.

###### Fields

- **Action** – This is a String, of type: `string` (a UTF-8 encoded string).

The type of pending maintenance action that is available for the resource.

- **AutoAppliedAfterDate** – This is a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

The date of the maintenance window when the action is applied. The maintenance
action is applied to the resource during its first maintenance window after this
date. If this date is specified, any `next-maintenance` opt-in
requests are ignored.

- **CurrentApplyDate** – This is a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

The effective date when the pending maintenance action is applied to the
resource. This date takes into account opt-in requests received from the [ApplyPendingMaintenanceAction (action)](#ApplyPendingMaintenanceAction "#ApplyPendingMaintenanceAction") API, the `AutoAppliedAfterDate`,
and the `ForcedApplyDate`. This value is blank if an opt-in request
has not been received and nothing has been specified as `AutoAppliedAfterDate`
or `ForcedApplyDate`.

- **Description** – This is a String, of type: `string` (a UTF-8 encoded string).

A description providing more detail about the maintenance action.

- **ForcedApplyDate** – This is a TStamp, of type: `timestamp` (a point in time, generally defined as an offset from midnight 1970-01-01).

The date when the maintenance action is automatically applied. The maintenance
action is applied to the resource on this date regardless of the maintenance window
for the resource. If this date is specified, any `immediate` opt-in
requests are ignored.

- **OptInStatus** – This is a String, of type: `string` (a UTF-8 encoded string).

Indicates the type of opt-in request that has been received for the resource.

## ResourcePendingMaintenanceActions (structure)

Describes the pending maintenance actions for a resource.

###### Fields

- **PendingMaintenanceActionDetails** – This is An array of [PendingMaintenanceAction](#PendingMaintenanceAction "#PendingMaintenanceAction") objects.

A list that provides details about the pending maintenance actions for
the resource.

- **ResourceIdentifier** – This is a String, of type: `string` (a UTF-8 encoded string).

The ARN of the resource that has pending maintenance actions.

`ResourcePendingMaintenanceActions` is used as the response element for:

- [ApplyPendingMaintenanceAction](#ApplyPendingMaintenanceAction "#ApplyPendingMaintenanceAction")

## UpgradeTarget (structure)

The version of the database engine that a DB instance can be upgraded to.

###### Fields

- **AutoUpgrade** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

A value that indicates whether the target version is applied to any source
DB instances that have AutoMinorVersionUpgrade set to true.

- **Description** – This is a String, of type: `string` (a UTF-8 encoded string).

The version of the database engine that a DB instance can be upgraded to.

- **Engine** – This is a String, of type: `string` (a UTF-8 encoded string).

The name of the upgrade target database engine.

- **EngineVersion** – This is a String, of type: `string` (a UTF-8 encoded string).

The version number of the upgrade target database engine.

- **IsMajorVersionUpgrade** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

A value that indicates whether a database engine is upgraded to a major
version.

- **SupportsGlobalDatabases** – This is a BooleanOptional, of type: `boolean` (a Boolean (true or false) value).

A value that indicates whether you can use Neptune global databases with
the target engine version.

## Tag (structure)

Metadata assigned to an Amazon Neptune resource consisting of a key-value
pair.

###### Fields

- **Key** – This is a String, of type: `string` (a UTF-8 encoded string).

A key is the required name of the tag. The string value can be from 1 to 128
Unicode characters in length and can't be prefixed with `aws:` or
`rds:`. The string can only contain the set of Unicode letters, digits,
white-space, '\_', '.', '/', '=', '+', '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}\_.:/=+\\-]\*)$").

- **Value** – This is a String, of type: `string` (a UTF-8 encoded string).

A value is the optional value of the tag. The string value can be from 1 to
256 Unicode characters in length and can't be prefixed with `aws:`
or `rds:`. The string can only contain the set of Unicode letters,
digits, white-space, '\_', '.', '/', '=', '+', '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}\_.:/=+\\-]\*)$").
