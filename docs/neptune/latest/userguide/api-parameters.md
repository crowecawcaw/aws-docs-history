# Neptune Parameters API

**Actions:**

- [CopyDBParameterGroup (action)](#CopyDBParameterGroup "#CopyDBParameterGroup")
- [CopyDBClusterParameterGroup (action)](#CopyDBClusterParameterGroup "#CopyDBClusterParameterGroup")
- [CreateDBParameterGroup (action)](#CreateDBParameterGroup "#CreateDBParameterGroup")
- [CreateDBClusterParameterGroup (action)](#CreateDBClusterParameterGroup "#CreateDBClusterParameterGroup")
- [DeleteDBParameterGroup (action)](#DeleteDBParameterGroup "#DeleteDBParameterGroup")
- [DeleteDBClusterParameterGroup (action)](#DeleteDBClusterParameterGroup "#DeleteDBClusterParameterGroup")
- [ModifyDBParameterGroup (action)](#ModifyDBParameterGroup "#ModifyDBParameterGroup")
- [ModifyDBClusterParameterGroup (action)](#ModifyDBClusterParameterGroup "#ModifyDBClusterParameterGroup")
- [ResetDBParameterGroup (action)](#ResetDBParameterGroup "#ResetDBParameterGroup")
- [ResetDBClusterParameterGroup (action)](#ResetDBClusterParameterGroup "#ResetDBClusterParameterGroup")
- [DescribeDBParameters (action)](#DescribeDBParameters "#DescribeDBParameters")
- [DescribeDBParameterGroups (action)](#DescribeDBParameterGroups "#DescribeDBParameterGroups")
- [DescribeDBClusterParameters (action)](#DescribeDBClusterParameters "#DescribeDBClusterParameters")
- [DescribeDBClusterParameterGroups (action)](#DescribeDBClusterParameterGroups "#DescribeDBClusterParameterGroups")
- [DescribeEngineDefaultParameters (action)](#DescribeEngineDefaultParameters "#DescribeEngineDefaultParameters")
- [DescribeEngineDefaultClusterParameters (action)](#DescribeEngineDefaultClusterParameters "#DescribeEngineDefaultClusterParameters")
  **Structures:**

- [Parameter (structure)](#Parameter "#Parameter")
- [DBParameterGroup (structure)](#DBParameterGroup "#DBParameterGroup")
- [DBClusterParameterGroup (structure)](#DBClusterParameterGroup "#DBClusterParameterGroup")
- [DBParameterGroupStatus (structure)](#DBParameterGroupStatus "#DBParameterGroupStatus")

## CopyDBParameterGroup (action)

        The AWS CLI name for this API is: `copy-db-parameter-group`.

Copies the specified DB parameter group.

**Request**

- **SourceDBParameterGroupIdentifier**  (in the CLI: `--source-db-parameter-group-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The identifier or ARN for the source DB parameter group. For information
about creating an ARN, see [Constructing an Amazon Resource Name (ARN)](../UserGuide/tagging.md#tagging.ARN.Constructing "../UserGuide/tagging.md#tagging.ARN.Constructing").

Constraints:

    + Must specify a valid DB parameter group.
    + Must specify a valid DB parameter group identifier, for example `my-db-param-group`,
     or a valid ARN.

- **Tags**  (in the CLI: `--tags`) –  An array of [Tag](api-other-apis.md#Tag "api-other-apis.md#Tag") objects.

The tags to be assigned to the copied DB parameter group.

- **TargetDBParameterGroupDescription**  (in the CLI: `--target-db-parameter-group-description`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A description for the copied DB parameter group.

- **TargetDBParameterGroupIdentifier**  (in the CLI: `--target-db-parameter-group-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The identifier for the copied DB parameter group.

Constraints:

    + Cannot be null, empty, or blank.
    + Must contain from 1 to 255 letters, numbers, or hyphens.
    + First character must be a letter.
    + Cannot end with a hyphen or contain two consecutive hyphens.

Example: `my-db-parameter-group`

**Response**

Contains the details of an Amazon Neptune DB parameter group.

This data type is used as a response element in the [DescribeDBParameterGroups (action)](#DescribeDBParameterGroups "#DescribeDBParameterGroups") action.

- **DBParameterGroupArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB parameter group.

- **DBParameterGroupFamily**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the DB parameter group family that this DB parameter
group is compatible with.

- **DBParameterGroupName**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the DB parameter group.

- **Description**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the customer-specified description for this DB parameter group.

###### Errors

- [DBParameterGroupNotFoundFault](api-faults.md#DBParameterGroupNotFoundFault "api-faults.md#DBParameterGroupNotFoundFault")
- [DBParameterGroupAlreadyExistsFault](api-faults.md#DBParameterGroupAlreadyExistsFault "api-faults.md#DBParameterGroupAlreadyExistsFault")
- [DBParameterGroupQuotaExceededFault](api-faults.md#DBParameterGroupQuotaExceededFault "api-faults.md#DBParameterGroupQuotaExceededFault")

## CopyDBClusterParameterGroup (action)

        The AWS CLI name for this API is: `copy-db-cluster-parameter-group`.

Copies the specified DB cluster parameter group.

**Request**

- **SourceDBClusterParameterGroupIdentifier**  (in the CLI: `--source-db-cluster-parameter-group-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The identifier or Amazon Resource Name (ARN) for the source DB cluster
parameter group. For information about creating an ARN, see [Constructing an Amazon Resource Name (ARN)](../UserGuide/tagging.md#tagging.ARN.Constructing "../UserGuide/tagging.md#tagging.ARN.Constructing").

Constraints:

    + Must specify a valid DB cluster parameter group.
    + If the source DB cluster parameter group is in the same Amazon Region as
     the copy, specify a valid DB parameter group identifier, for example `my-db-cluster-param-group`,
     or a valid ARN.
    + If the source DB parameter group is in a different Amazon Region than the
     copy, specify a valid DB cluster parameter group ARN, for example `arn:aws:rds:us-east-1:123456789012:cluster-pg:custom-cluster-group1`.

- **Tags**  (in the CLI: `--tags`) –  An array of [Tag](api-other-apis.md#Tag "api-other-apis.md#Tag") objects.

The tags to be assigned to the copied DB cluster parameter group.

- **TargetDBClusterParameterGroupDescription**  (in the CLI: `--target-db-cluster-parameter-group-description`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

A description for the copied DB cluster parameter group.

- **TargetDBClusterParameterGroupIdentifier**  (in the CLI: `--target-db-cluster-parameter-group-identifier`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The identifier for the copied DB cluster parameter group.

Constraints:

    + Cannot be null, empty, or blank
    + Must contain from 1 to 255 letters, numbers, or hyphens
    + First character must be a letter
    + Cannot end with a hyphen or contain two consecutive hyphens

Example: `my-cluster-param-group1`

**Response**

Contains the details of an Amazon Neptune DB cluster parameter group.

This data type is used as a response element in the [DescribeDBClusterParameterGroups (action)](#DescribeDBClusterParameterGroups "#DescribeDBClusterParameterGroups") action.

- **DBClusterParameterGroupArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB cluster parameter group.

- **DBClusterParameterGroupName**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the DB cluster parameter group.

- **DBParameterGroupFamily**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the DB parameter group family that this DB cluster
parameter group is compatible with.

- **Description**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the customer-specified description for this DB cluster parameter
group.

###### Errors

- [DBParameterGroupNotFoundFault](api-faults.md#DBParameterGroupNotFoundFault "api-faults.md#DBParameterGroupNotFoundFault")
- [DBParameterGroupQuotaExceededFault](api-faults.md#DBParameterGroupQuotaExceededFault "api-faults.md#DBParameterGroupQuotaExceededFault")
- [DBParameterGroupAlreadyExistsFault](api-faults.md#DBParameterGroupAlreadyExistsFault "api-faults.md#DBParameterGroupAlreadyExistsFault")

## CreateDBParameterGroup (action)

        The AWS CLI name for this API is: `create-db-parameter-group`.

Creates a new DB parameter group.

A DB parameter group is initially created with the default parameters
for the database engine used by the DB instance. To provide custom values for any
of the parameters, you must modify the group after creating it using _ModifyDBParameterGroup_.
Once you've created a DB parameter group, you need to associate it with your DB
instance using _ModifyDBInstance_. When you associate
a new DB parameter group with a running DB instance, you need to reboot the DB instance
without failover for the new DB parameter group and associated settings to take
effect.

###### Important

After you create a DB parameter group, you should wait at least 5 minutes
before creating your first DB instance that uses that DB parameter group as the
default parameter group. This allows Amazon Neptune to fully complete the create
action before the parameter group is used as the default for a new DB instance.
This is especially important for parameters that are critical when creating
the default database for a DB instance, such as the character set for the default
database defined by the `character_set_database` parameter.
You can use the _Parameter Groups_ option of the Amazon
Neptune console or the _DescribeDBParameters_ command
to verify that your DB parameter group has been created or modified.

**Request**

- **DBParameterGroupFamily**  (in the CLI: `--db-parameter-group-family`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The DB parameter group family name. A DB parameter group can be associated
with one and only one DB parameter group family, and can be applied only to a DB instance
running a database engine and engine version compatible with that DB parameter
group family.

- **DBParameterGroupName**  (in the CLI: `--db-parameter-group-name`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the DB parameter group.

Constraints:

    + Must be 1 to 255 letters, numbers, or hyphens.
    + First character must be a letter
    + Cannot end with a hyphen or contain two consecutive hyphens

###### Note

This value is stored as a lowercase string.

- **Description**  (in the CLI: `--description`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The description for the DB parameter group.

- **Tags**  (in the CLI: `--tags`) –  An array of [Tag](api-other-apis.md#Tag "api-other-apis.md#Tag") objects.

The tags to be assigned to the new DB parameter group.

**Response**

Contains the details of an Amazon Neptune DB parameter group.

This data type is used as a response element in the [DescribeDBParameterGroups (action)](#DescribeDBParameterGroups "#DescribeDBParameterGroups") action.

- **DBParameterGroupArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB parameter group.

- **DBParameterGroupFamily**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the DB parameter group family that this DB parameter
group is compatible with.

- **DBParameterGroupName**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the DB parameter group.

- **Description**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the customer-specified description for this DB parameter group.

###### Errors

- [DBParameterGroupQuotaExceededFault](api-faults.md#DBParameterGroupQuotaExceededFault "api-faults.md#DBParameterGroupQuotaExceededFault")
- [DBParameterGroupAlreadyExistsFault](api-faults.md#DBParameterGroupAlreadyExistsFault "api-faults.md#DBParameterGroupAlreadyExistsFault")

## CreateDBClusterParameterGroup (action)

        The AWS CLI name for this API is: `create-db-cluster-parameter-group`.

Creates a new DB cluster parameter group.

Parameters in a DB cluster parameter group apply to all of the instances
in a DB cluster.

A DB cluster parameter group is initially created with the default parameters
for the database engine used by instances in the DB cluster. To provide custom
values for any of the parameters, you must modify the group after creating it using
[ModifyDBClusterParameterGroup (action)](#ModifyDBClusterParameterGroup "#ModifyDBClusterParameterGroup"). Once you've created a
DB cluster parameter group, you need to associate it with your DB cluster using
[ModifyDBCluster (action)](api-clusters.md#ModifyDBCluster "api-clusters.md#ModifyDBCluster"). When you associate a new DB cluster parameter
group with a running DB cluster, you need to reboot the DB instances in the DB cluster
without failover for the new DB cluster parameter group and associated settings
to take effect.

###### Important

After you create a DB cluster parameter group, you should wait at least
5 minutes before creating your first DB cluster that uses that DB cluster parameter
group as the default parameter group. This allows Amazon Neptune to fully complete
the create action before the DB cluster parameter group is used as the default
for a new DB cluster. This is especially important for parameters that are critical
when creating the default database for a DB cluster, such as the character set
for the default database defined by the `character_set_database`
parameter. You can use the _Parameter Groups_ option of
the [Amazon Neptune console](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/") or the
[DescribeDBClusterParameters (action)](#DescribeDBClusterParameters "#DescribeDBClusterParameters") command to verify that your
DB cluster parameter group has been created or modified.

**Request**

- **DBClusterParameterGroupName**  (in the CLI: `--db-cluster-parameter-group-name`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the DB cluster parameter group.

Constraints:

    + Must match the name of an existing DBClusterParameterGroup.

###### Note

This value is stored as a lowercase string.

- **DBParameterGroupFamily**  (in the CLI: `--db-parameter-group-family`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The DB cluster parameter group family name. A DB cluster parameter group
can be associated with one and only one DB cluster parameter group family, and
can be applied only to a DB cluster running a database engine and engine version
compatible with that DB cluster parameter group family.

- **Description**  (in the CLI: `--description`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The description for the DB cluster parameter group.

- **Tags**  (in the CLI: `--tags`) –  An array of [Tag](api-other-apis.md#Tag "api-other-apis.md#Tag") objects.

The tags to be assigned to the new DB cluster parameter group.

**Response**

Contains the details of an Amazon Neptune DB cluster parameter group.

This data type is used as a response element in the [DescribeDBClusterParameterGroups (action)](#DescribeDBClusterParameterGroups "#DescribeDBClusterParameterGroups") action.

- **DBClusterParameterGroupArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB cluster parameter group.

- **DBClusterParameterGroupName**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the DB cluster parameter group.

- **DBParameterGroupFamily**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the DB parameter group family that this DB cluster
parameter group is compatible with.

- **Description**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the customer-specified description for this DB cluster parameter
group.

###### Errors

- [DBParameterGroupQuotaExceededFault](api-faults.md#DBParameterGroupQuotaExceededFault "api-faults.md#DBParameterGroupQuotaExceededFault")
- [DBParameterGroupAlreadyExistsFault](api-faults.md#DBParameterGroupAlreadyExistsFault "api-faults.md#DBParameterGroupAlreadyExistsFault")

## DeleteDBParameterGroup (action)

        The AWS CLI name for this API is: `delete-db-parameter-group`.

Deletes a specified DBParameterGroup. The DBParameterGroup to be deleted
can't be associated with any DB instances.

**Request**

- **DBParameterGroupName**  (in the CLI: `--db-parameter-group-name`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the DB parameter group.

Constraints:

    + Must be the name of an existing DB parameter group
    + You can't delete a default DB parameter group
    + Cannot be associated with any DB instances

###### Response

- _No Response parameters._

###### Errors

- [InvalidDBParameterGroupStateFault](api-faults.md#InvalidDBParameterGroupStateFault "api-faults.md#InvalidDBParameterGroupStateFault")
- [DBParameterGroupNotFoundFault](api-faults.md#DBParameterGroupNotFoundFault "api-faults.md#DBParameterGroupNotFoundFault")

## DeleteDBClusterParameterGroup (action)

        The AWS CLI name for this API is: `delete-db-cluster-parameter-group`.

Deletes a specified DB cluster parameter group. The DB cluster parameter
group to be deleted can't be associated with any DB clusters.

**Request**

- **DBClusterParameterGroupName**  (in the CLI: `--db-cluster-parameter-group-name`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the DB cluster parameter group.

Constraints:

    + Must be the name of an existing DB cluster parameter group.
    + You can't delete a default DB cluster parameter group.
    + Cannot be associated with any DB clusters.

###### Response

- _No Response parameters._

###### Errors

- [InvalidDBParameterGroupStateFault](api-faults.md#InvalidDBParameterGroupStateFault "api-faults.md#InvalidDBParameterGroupStateFault")
- [DBParameterGroupNotFoundFault](api-faults.md#DBParameterGroupNotFoundFault "api-faults.md#DBParameterGroupNotFoundFault")

## ModifyDBParameterGroup (action)

        The AWS CLI name for this API is: `modify-db-parameter-group`.

Modifies the parameters of a DB parameter group. To modify more than one
parameter, submit a list of the following: `ParameterName`, `ParameterValue`,
and `ApplyMethod`. A maximum of 20 parameters can be modified in
a single request.

###### Note

Changes to dynamic parameters are applied immediately. Changes to static
parameters require a reboot without failover to the DB instance associated with
the parameter group before the change can take effect.

###### Important

After you modify a DB parameter group, you should wait at least 5 minutes
before creating your first DB instance that uses that DB parameter group as the
default parameter group. This allows Amazon Neptune to fully complete the modify
action before the parameter group is used as the default for a new DB instance.
This is especially important for parameters that are critical when creating
the default database for a DB instance, such as the character set for the default
database defined by the `character_set_database` parameter.
You can use the _Parameter Groups_ option of the Amazon
Neptune console or the _DescribeDBParameters_ command
to verify that your DB parameter group has been created or modified.

**Request**

- **DBParameterGroupName**  (in the CLI: `--db-parameter-group-name`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the DB parameter group.

Constraints:

    + If supplied, must match the name of an existing DBParameterGroup.

- **Parameters**  (in the CLI: `--parameters`) –  _Required:_ An array of [Parameter](#Parameter "#Parameter") objects.

An array of parameter names, values, and the apply method for the parameter
update. At least one parameter name, value, and apply method must be supplied;
subsequent arguments are optional. A maximum of 20 parameters can be modified
in a single request.

Valid Values (for the application method): `immediate | pending-reboot`

###### Note

You can use the immediate value with dynamic parameters only. You can use
the pending-reboot value for both dynamic and static parameters, and changes
are applied when you reboot the DB instance without failover.

**Response**

- **DBParameterGroupName**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the DB parameter group.

###### Errors

- [DBParameterGroupNotFoundFault](api-faults.md#DBParameterGroupNotFoundFault "api-faults.md#DBParameterGroupNotFoundFault")
- [InvalidDBParameterGroupStateFault](api-faults.md#InvalidDBParameterGroupStateFault "api-faults.md#InvalidDBParameterGroupStateFault")

## ModifyDBClusterParameterGroup (action)

        The AWS CLI name for this API is: `modify-db-cluster-parameter-group`.

Modifies the parameters of a DB cluster parameter group. To modify more
than one parameter, submit a list of the following: `ParameterName`,
`ParameterValue`, and `ApplyMethod`. A maximum of
20 parameters can be modified in a single request.

###### Note

Changes to dynamic parameters are applied immediately. Changes to static
parameters require a reboot without failover to the DB cluster associated with
the parameter group before the change can take effect.

###### Important

After you create a DB cluster parameter group, you should wait at least
5 minutes before creating your first DB cluster that uses that DB cluster parameter
group as the default parameter group. This allows Amazon Neptune to fully complete
the create action before the parameter group is used as the default for a new DB
cluster. This is especially important for parameters that are critical when
creating the default database for a DB cluster, such as the character set for the
default database defined by the `character_set_database` parameter.
You can use the _Parameter Groups_ option of the Amazon
Neptune console or the [DescribeDBClusterParameters (action)](#DescribeDBClusterParameters "#DescribeDBClusterParameters") command
to verify that your DB cluster parameter group has been created or modified.

**Request**

- **DBClusterParameterGroupName**  (in the CLI: `--db-cluster-parameter-group-name`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the DB cluster parameter group to modify.

- **Parameters**  (in the CLI: `--parameters`) –  _Required:_ An array of [Parameter](#Parameter "#Parameter") objects.

A list of parameters in the DB cluster parameter group to modify.

**Response**

- **DBClusterParameterGroupName**   – a String, of type: `string` (a UTF-8 encoded string).

The name of the DB cluster parameter group.

Constraints:

    + Must be 1 to 255 letters or numbers.
    + First character must be a letter
    + Cannot end with a hyphen or contain two consecutive hyphens

###### Note

This value is stored as a lowercase string.

###### Errors

- [DBParameterGroupNotFoundFault](api-faults.md#DBParameterGroupNotFoundFault "api-faults.md#DBParameterGroupNotFoundFault")
- [InvalidDBParameterGroupStateFault](api-faults.md#InvalidDBParameterGroupStateFault "api-faults.md#InvalidDBParameterGroupStateFault")

## ResetDBParameterGroup (action)

        The AWS CLI name for this API is: `reset-db-parameter-group`.

Modifies the parameters of a DB parameter group to the engine/system default
value. To reset specific parameters, provide a list of the following: `ParameterName`
and `ApplyMethod`. To reset the entire DB parameter group, specify
the `DBParameterGroup` name and `ResetAllParameters`
parameters. When resetting the entire group, dynamic parameters are updated
immediately and static parameters are set to `pending-reboot`
to take effect on the next DB instance restart or `RebootDBInstance`
request.

**Request**

- **DBParameterGroupName**  (in the CLI: `--db-parameter-group-name`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the DB parameter group.

Constraints:

    + Must match the name of an existing DBParameterGroup.

- **Parameters**  (in the CLI: `--parameters`) –  An array of [Parameter](#Parameter "#Parameter") objects.

To reset the entire DB parameter group, specify the `DBParameterGroup`
name and `ResetAllParameters` parameters. To reset specific parameters,
provide a list of the following: `ParameterName` and `ApplyMethod`.
A maximum of 20 parameters can be modified in a single request.

Valid Values (for Apply method): `pending-reboot`

- **ResetAllParameters**  (in the CLI: `--reset-all-parameters`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

Specifies whether (`true`) or not (`false`)
to reset all parameters in the DB parameter group to default values.

Default: `true`

**Response**

- **DBParameterGroupName**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the DB parameter group.

###### Errors

- [InvalidDBParameterGroupStateFault](api-faults.md#InvalidDBParameterGroupStateFault "api-faults.md#InvalidDBParameterGroupStateFault")
- [DBParameterGroupNotFoundFault](api-faults.md#DBParameterGroupNotFoundFault "api-faults.md#DBParameterGroupNotFoundFault")

## ResetDBClusterParameterGroup (action)

        The AWS CLI name for this API is: `reset-db-cluster-parameter-group`.

Modifies the parameters of a DB cluster parameter group to the default
value. To reset specific parameters submit a list of the following: `ParameterName`
and `ApplyMethod`. To reset the entire DB cluster parameter group,
specify the `DBClusterParameterGroupName` and `ResetAllParameters`
parameters.

When resetting the entire group, dynamic parameters are updated immediately
and static parameters are set to `pending-reboot` to take effect
on the next DB instance restart or [RebootDBInstance (action)](api-instances.md#RebootDBInstance "api-instances.md#RebootDBInstance") request.
You must call [RebootDBInstance (action)](api-instances.md#RebootDBInstance "api-instances.md#RebootDBInstance") for every DB instance in your
DB cluster that you want the updated static parameter to apply to.

**Request**

- **DBClusterParameterGroupName**  (in the CLI: `--db-cluster-parameter-group-name`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the DB cluster parameter group to reset.

- **Parameters**  (in the CLI: `--parameters`) –  An array of [Parameter](#Parameter "#Parameter") objects.

A list of parameter names in the DB cluster parameter group to reset to the
default values. You can't use this parameter if the `ResetAllParameters`
parameter is set to `true`.

- **ResetAllParameters**  (in the CLI: `--reset-all-parameters`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

A value that is set to `true` to reset all parameters in the
DB cluster parameter group to their default values, and `false`
otherwise. You can't use this parameter if there is a list of parameter names specified
for the `Parameters` parameter.

**Response**

- **DBClusterParameterGroupName**   – a String, of type: `string` (a UTF-8 encoded string).

The name of the DB cluster parameter group.

Constraints:

    + Must be 1 to 255 letters or numbers.
    + First character must be a letter
    + Cannot end with a hyphen or contain two consecutive hyphens

###### Note

This value is stored as a lowercase string.

###### Errors

- [InvalidDBParameterGroupStateFault](api-faults.md#InvalidDBParameterGroupStateFault "api-faults.md#InvalidDBParameterGroupStateFault")
- [DBParameterGroupNotFoundFault](api-faults.md#DBParameterGroupNotFoundFault "api-faults.md#DBParameterGroupNotFoundFault")

## DescribeDBParameters (action)

        The AWS CLI name for this API is: `describe-db-parameters`.

Returns the detailed parameter list for a particular DB parameter group.

**Request**

- **DBParameterGroupName**  (in the CLI: `--db-parameter-group-name`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of a specific DB parameter group to return details for.

Constraints:

    + If supplied, must match the name of an existing DBParameterGroup.

- **Filters**  (in the CLI: `--filters`) –  An array of [Filter](api-datatypes.md#Filter "api-datatypes.md#Filter") objects.

This parameter is not currently supported.

- **Marker**  (in the CLI: `--marker`) –  a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous `DescribeDBParameters`
request. If this parameter is specified, the response includes only records
beyond the marker, up to the value specified by `MaxRecords`.

- **MaxRecords**  (in the CLI: `--max-records`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The maximum number of records to include in the response. If more records
exist than the specified `MaxRecords` value, a pagination token
called a marker is included in the response so that the remaining results can be
retrieved.

Default: 100

Constraints: Minimum 20, maximum 100.

- **Source**  (in the CLI: `--source`) –  a String, of type: `string` (a UTF-8 encoded string).

The parameter types to return.

Default: All parameter types returned

Valid Values: `user | system | engine-default`

**Response**

- **Marker**   – a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous request. If this parameter
is specified, the response includes only records beyond the marker, up to the
value specified by `MaxRecords`.

- **Parameters**   – An array of [Parameter](#Parameter "#Parameter") objects.

A list of [Parameter (structure)](#Parameter "#Parameter") values.

###### Errors

- [DBParameterGroupNotFoundFault](api-faults.md#DBParameterGroupNotFoundFault "api-faults.md#DBParameterGroupNotFoundFault")

## DescribeDBParameterGroups (action)

        The AWS CLI name for this API is: `describe-db-parameter-groups`.

Returns a list of `DBParameterGroup` descriptions. If a
`DBParameterGroupName` is specified, the list will contain only
the description of the specified DB parameter group.

**Request**

- **DBParameterGroupName**  (in the CLI: `--db-parameter-group-name`) –  a String, of type: `string` (a UTF-8 encoded string).

The name of a specific DB parameter group to return details for.

Constraints:

    + If supplied, must match the name of an existing DBClusterParameterGroup.

- **Filters**  (in the CLI: `--filters`) –  An array of [Filter](api-datatypes.md#Filter "api-datatypes.md#Filter") objects.

This parameter is not currently supported.

- **Marker**  (in the CLI: `--marker`) –  a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous `DescribeDBParameterGroups`
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

- **DBParameterGroups**   – An array of [DBParameterGroup](#DBParameterGroup "#DBParameterGroup") objects.

A list of [DBParameterGroup (structure)](#DBParameterGroup "#DBParameterGroup") instances.

- **Marker**   – a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous request. If this parameter
is specified, the response includes only records beyond the marker, up to the
value specified by `MaxRecords`.

###### Errors

- [DBParameterGroupNotFoundFault](api-faults.md#DBParameterGroupNotFoundFault "api-faults.md#DBParameterGroupNotFoundFault")

## DescribeDBClusterParameters (action)

        The AWS CLI name for this API is: `describe-db-cluster-parameters`.

Returns the detailed parameter list for a particular DB cluster parameter
group.

**Request**

- **DBClusterParameterGroupName**  (in the CLI: `--db-cluster-parameter-group-name`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of a specific DB cluster parameter group to return parameter details
for.

Constraints:

    + If supplied, must match the name of an existing DBClusterParameterGroup.

- **Filters**  (in the CLI: `--filters`) –  An array of [Filter](api-datatypes.md#Filter "api-datatypes.md#Filter") objects.

This parameter is not currently supported.

- **Marker**  (in the CLI: `--marker`) –  a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous `DescribeDBClusterParameters`
request. If this parameter is specified, the response includes only records
beyond the marker, up to the value specified by `MaxRecords`.

- **MaxRecords**  (in the CLI: `--max-records`) –  an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The maximum number of records to include in the response. If more records
exist than the specified `MaxRecords` value, a pagination token
called a marker is included in the response so that the remaining results can be
retrieved.

Default: 100

Constraints: Minimum 20, maximum 100.

- **Source**  (in the CLI: `--source`) –  a String, of type: `string` (a UTF-8 encoded string).

A value that indicates to return only parameters for a specific source.
Parameter sources can be `engine`, `service`, or `customer`.

**Response**

- **Marker**   – a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous DescribeDBClusterParameters
request. If this parameter is specified, the response includes only records
beyond the marker, up to the value specified by `MaxRecords` .

- **Parameters**   – An array of [Parameter](#Parameter "#Parameter") objects.

Provides a list of parameters for the DB cluster parameter group.

###### Errors

- [DBParameterGroupNotFoundFault](api-faults.md#DBParameterGroupNotFoundFault "api-faults.md#DBParameterGroupNotFoundFault")

## DescribeDBClusterParameterGroups (action)

        The AWS CLI name for this API is: `describe-db-cluster-parameter-groups`.

Returns a list of `DBClusterParameterGroup` descriptions.
If a `DBClusterParameterGroupName` parameter is specified, the
list will contain only the description of the specified DB cluster parameter
group.

**Request**

- **DBClusterParameterGroupName**  (in the CLI: `--db-cluster-parameter-group-name`) –  a String, of type: `string` (a UTF-8 encoded string).

The name of a specific DB cluster parameter group to return details for.

Constraints:

    + If supplied, must match the name of an existing DBClusterParameterGroup.

- **Filters**  (in the CLI: `--filters`) –  An array of [Filter](api-datatypes.md#Filter "api-datatypes.md#Filter") objects.

This parameter is not currently supported.

- **Marker**  (in the CLI: `--marker`) –  a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous `DescribeDBClusterParameterGroups`
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

- **DBClusterParameterGroups**   – An array of [DBClusterParameterGroup](#DBClusterParameterGroup "#DBClusterParameterGroup") objects.

A list of DB cluster parameter groups.

- **Marker**   – a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous `DescribeDBClusterParameterGroups`
request. If this parameter is specified, the response includes only records
beyond the marker, up to the value specified by `MaxRecords`.

###### Errors

- [DBParameterGroupNotFoundFault](api-faults.md#DBParameterGroupNotFoundFault "api-faults.md#DBParameterGroupNotFoundFault")

## DescribeEngineDefaultParameters (action)

        The AWS CLI name for this API is: `describe-engine-default-parameters`.

Returns the default engine and system parameter information for the specified
database engine.

**Request**

- **DBParameterGroupFamily**  (in the CLI: `--db-parameter-group-family`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the DB parameter group family.

- **Filters**  (in the CLI: `--filters`) –  An array of [Filter](api-datatypes.md#Filter "api-datatypes.md#Filter") objects.

Not currently supported.

- **Marker**  (in the CLI: `--marker`) –  a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous `DescribeEngineDefaultParameters`
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

Contains the result of a successful invocation of the DescribeEngineDefaultParameters (action) action.

- **DBParameterGroupFamily**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the DB parameter group family that the engine default
parameters apply to.

- **Marker**   – a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous EngineDefaults request.
If this parameter is specified, the response includes only records beyond the
marker, up to the value specified by `MaxRecords` .

- **Parameters**   – An array of [Parameter](#Parameter "#Parameter") objects.

Contains a list of engine default parameters.

## DescribeEngineDefaultClusterParameters (action)

        The AWS CLI name for this API is: `describe-engine-default-cluster-parameters`.

Returns the default engine and system parameter information for the cluster
database engine.

**Request**

- **DBParameterGroupFamily**  (in the CLI: `--db-parameter-group-family`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the DB cluster parameter group family to return engine parameter
information for.

- **Filters**  (in the CLI: `--filters`) –  An array of [Filter](api-datatypes.md#Filter "api-datatypes.md#Filter") objects.

This parameter is not currently supported.

- **Marker**  (in the CLI: `--marker`) –  a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous `DescribeEngineDefaultClusterParameters`
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

Contains the result of a successful invocation of the [DescribeEngineDefaultParameters (action)](#DescribeEngineDefaultParameters "#DescribeEngineDefaultParameters") action.

- **DBParameterGroupFamily**   – a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the DB parameter group family that the engine default
parameters apply to.

- **Marker**   – a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous EngineDefaults request.
If this parameter is specified, the response includes only records beyond the
marker, up to the value specified by `MaxRecords` .

- **Parameters**   – An array of [Parameter](#Parameter "#Parameter") objects.

Contains a list of engine default parameters.

## _Structures:_

## Parameter (structure)

Specifies a parameter.

###### Fields

- **AllowedValues** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the valid range of values for the parameter.

- **ApplyMethod** – This is an ApplyMethod, of type: `string` (a UTF-8 encoded string).

Indicates when to apply parameter updates.

- **ApplyType** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the engine specific parameters type.

- **DataType** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the valid data type for the parameter.

- **Description** – This is a String, of type: `string` (a UTF-8 encoded string).

Provides a description of the parameter.

- **IsModifiable** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Indicates whether (`true`) or not (`false`)
the parameter can be modified. Some parameters have security or operational
implications that prevent them from being changed.

- **MinimumEngineVersion** – This is a String, of type: `string` (a UTF-8 encoded string).

The earliest engine version to which the parameter can apply.

- **ParameterName** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the name of the parameter.

- **ParameterValue** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the value of the parameter.

- **Source** – This is a String, of type: `string` (a UTF-8 encoded string).

Indicates the source of the parameter value.

## DBParameterGroup (structure)

Contains the details of an Amazon Neptune DB parameter group.

This data type is used as a response element in the [DescribeDBParameterGroups (action)](#DescribeDBParameterGroups "#DescribeDBParameterGroups") action.

###### Fields

- **DBParameterGroupArn** – This is a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB parameter group.

- **DBParameterGroupFamily** – This is a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the DB parameter group family that this DB parameter
group is compatible with.

- **DBParameterGroupName** – This is a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the DB parameter group.

- **Description** – This is a String, of type: `string` (a UTF-8 encoded string).

Provides the customer-specified description for this DB parameter group.

`DBParameterGroup` is used as the response element for:

- [CopyDBParameterGroup](#CopyDBParameterGroup "#CopyDBParameterGroup")
- [CreateDBParameterGroup](#CreateDBParameterGroup "#CreateDBParameterGroup")

## DBClusterParameterGroup (structure)

Contains the details of an Amazon Neptune DB cluster parameter group.

This data type is used as a response element in the [DescribeDBClusterParameterGroups (action)](#DescribeDBClusterParameterGroups "#DescribeDBClusterParameterGroups") action.

###### Fields

- **DBClusterParameterGroupArn** – This is a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB cluster parameter group.

- **DBClusterParameterGroupName** – This is a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the DB cluster parameter group.

- **DBParameterGroupFamily** – This is a String, of type: `string` (a UTF-8 encoded string).

Provides the name of the DB parameter group family that this DB cluster
parameter group is compatible with.

- **Description** – This is a String, of type: `string` (a UTF-8 encoded string).

Provides the customer-specified description for this DB cluster parameter
group.

`DBClusterParameterGroup` is used as the response element for:

- [CopyDBClusterParameterGroup](#CopyDBClusterParameterGroup "#CopyDBClusterParameterGroup")
- [CreateDBClusterParameterGroup](#CreateDBClusterParameterGroup "#CreateDBClusterParameterGroup")

## DBParameterGroupStatus (structure)

The status of the DB parameter group.

This data type is used as a response element in the following actions:

- [CreateDBInstance (action)](api-instances.md#CreateDBInstance "api-instances.md#CreateDBInstance")
- [DeleteDBInstance (action)](api-instances.md#DeleteDBInstance "api-instances.md#DeleteDBInstance")
- [ModifyDBInstance (action)](api-instances.md#ModifyDBInstance "api-instances.md#ModifyDBInstance")
- [RebootDBInstance (action)](api-instances.md#RebootDBInstance "api-instances.md#RebootDBInstance")

###### Fields

- **DBParameterGroupName** – This is a String, of type: `string` (a UTF-8 encoded string).

The name of the DP parameter group.

- **ParameterApplyStatus** – This is a String, of type: `string` (a UTF-8 encoded string).

The status of parameter updates.
