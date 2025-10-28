# Neptune Subnet API

**Actions:**

- [CreateDBSubnetGroup (action)](#CreateDBSubnetGroup "#CreateDBSubnetGroup")
- [DeleteDBSubnetGroup (action)](#DeleteDBSubnetGroup "#DeleteDBSubnetGroup")
- [ModifyDBSubnetGroup (action)](#ModifyDBSubnetGroup "#ModifyDBSubnetGroup")
- [DescribeDBSubnetGroups (action)](#DescribeDBSubnetGroups "#DescribeDBSubnetGroups")
  **Structures:**

- [Subnet (structure)](#Subnet "#Subnet")
- [DBSubnetGroup (structure)](#DBSubnetGroup "#DBSubnetGroup")

## CreateDBSubnetGroup (action)

        The AWS CLI name for this API is: `create-db-subnet-group`.

Creates a new DB subnet group. DB subnet groups must contain at least one
subnet in at least two AZs in the Amazon Region.

**Request**

- **DBSubnetGroupDescription**  (in the CLI: `--db-subnet-group-description`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The description for the DB subnet group.

- **DBSubnetGroupName**  (in the CLI: `--db-subnet-group-name`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name for the DB subnet group. This value is stored as a lowercase string.

Constraints: Must contain no more than 255 letters, numbers, periods,
underscores, spaces, or hyphens. Must not be default.

Example: `mySubnetgroup`

- **SubnetIds**  (in the CLI: `--subnet-ids`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The EC2 Subnet IDs for the DB subnet group.

- **Tags**  (in the CLI: `--tags`) –  An array of [Tag](api-other-apis.md#Tag "api-other-apis.md#Tag") objects.

The tags to be assigned to the new DB subnet group.

**Response**

Contains the details of an Amazon Neptune DB subnet group.

This data type is used as a response element in the [DescribeDBSubnetGroups (action)](#DescribeDBSubnetGroups "#DescribeDBSubnetGroups") action.

- **DBSubnetGroupArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB subnet group.

- **DBSubnetGroupDescription**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the description of the DB subnet group.

- **DBSubnetGroupName**   – a String, of type: `string` (a UTF-8 encoded string).

The name of the DB subnet group.

- **SubnetGroupStatus**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the status of the DB subnet group.

- **Subnets**   – An array of [Subnet](#Subnet "#Subnet") objects.

Contains a list of [Subnet (structure)](#Subnet "#Subnet") elements.

- **VpcId**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the VpcId of the DB subnet group.

###### Errors

- [DBSubnetGroupAlreadyExistsFault](api-faults.md#DBSubnetGroupAlreadyExistsFault "api-faults.md#DBSubnetGroupAlreadyExistsFault")
- [DBSubnetGroupQuotaExceededFault](api-faults.md#DBSubnetGroupQuotaExceededFault "api-faults.md#DBSubnetGroupQuotaExceededFault")
- [DBSubnetQuotaExceededFault](api-faults.md#DBSubnetQuotaExceededFault "api-faults.md#DBSubnetQuotaExceededFault")
- [DBSubnetGroupDoesNotCoverEnoughAZs](api-faults.md#DBSubnetGroupDoesNotCoverEnoughAZs "api-faults.md#DBSubnetGroupDoesNotCoverEnoughAZs")
- [InvalidSubnet](api-faults.md#InvalidSubnet "api-faults.md#InvalidSubnet")

## DeleteDBSubnetGroup (action)

        The AWS CLI name for this API is: `delete-db-subnet-group`.

Deletes a DB subnet group.

###### Note

The specified database subnet group must not be associated with any DB
instances.

**Request**

- **DBSubnetGroupName**  (in the CLI: `--db-subnet-group-name`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name of the database subnet group to delete.

###### Note

You can't delete the default subnet group.

Constraints:

Constraints: Must match the name of an existing DBSubnetGroup. Must not
be default.

Example: `mySubnetgroup`

###### Response

- _No Response parameters._

###### Errors

- [InvalidDBSubnetGroupStateFault](api-faults.md#InvalidDBSubnetGroupStateFault "api-faults.md#InvalidDBSubnetGroupStateFault")
- [InvalidDBSubnetStateFault](api-faults.md#InvalidDBSubnetStateFault "api-faults.md#InvalidDBSubnetStateFault")
- [DBSubnetGroupNotFoundFault](api-faults.md#DBSubnetGroupNotFoundFault "api-faults.md#DBSubnetGroupNotFoundFault")

## ModifyDBSubnetGroup (action)

        The AWS CLI name for this API is: `modify-db-subnet-group`.

Modifies an existing DB subnet group. DB subnet groups must contain at
least one subnet in at least two AZs in the Amazon Region.

**Request**

- **DBSubnetGroupDescription**  (in the CLI: `--db-subnet-group-description`) –  a String, of type: `string` (a UTF-8 encoded string).

The description for the DB subnet group.

- **DBSubnetGroupName**  (in the CLI: `--db-subnet-group-name`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The name for the DB subnet group. This value is stored as a lowercase string.
You can't modify the default subnet group.

Constraints: Must match the name of an existing DBSubnetGroup. Must not
be default.

Example: `mySubnetgroup`

- **SubnetIds**  (in the CLI: `--subnet-ids`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The EC2 subnet IDs for the DB subnet group.

**Response**

Contains the details of an Amazon Neptune DB subnet group.

This data type is used as a response element in the [DescribeDBSubnetGroups (action)](#DescribeDBSubnetGroups "#DescribeDBSubnetGroups") action.

- **DBSubnetGroupArn**   – a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB subnet group.

- **DBSubnetGroupDescription**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the description of the DB subnet group.

- **DBSubnetGroupName**   – a String, of type: `string` (a UTF-8 encoded string).

The name of the DB subnet group.

- **SubnetGroupStatus**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the status of the DB subnet group.

- **Subnets**   – An array of [Subnet](#Subnet "#Subnet") objects.

Contains a list of [Subnet (structure)](#Subnet "#Subnet") elements.

- **VpcId**   – a String, of type: `string` (a UTF-8 encoded string).

Provides the VpcId of the DB subnet group.

###### Errors

- [DBSubnetGroupNotFoundFault](api-faults.md#DBSubnetGroupNotFoundFault "api-faults.md#DBSubnetGroupNotFoundFault")
- [DBSubnetQuotaExceededFault](api-faults.md#DBSubnetQuotaExceededFault "api-faults.md#DBSubnetQuotaExceededFault")
- [SubnetAlreadyInUse](api-faults.md#SubnetAlreadyInUse "api-faults.md#SubnetAlreadyInUse")
- [DBSubnetGroupDoesNotCoverEnoughAZs](api-faults.md#DBSubnetGroupDoesNotCoverEnoughAZs "api-faults.md#DBSubnetGroupDoesNotCoverEnoughAZs")
- [InvalidSubnet](api-faults.md#InvalidSubnet "api-faults.md#InvalidSubnet")

## DescribeDBSubnetGroups (action)

        The AWS CLI name for this API is: `describe-db-subnet-groups`.

Returns a list of DBSubnetGroup descriptions. If a DBSubnetGroupName
is specified, the list will contain only the descriptions of the specified DBSubnetGroup.

For an overview of CIDR ranges, go to the [Wikipedia
Tutorial](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing "http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing").

**Request**

- **DBSubnetGroupName**  (in the CLI: `--db-subnet-group-name`) –  a String, of type: `string` (a UTF-8 encoded string).

The name of the DB subnet group to return details for.

- **Filters**  (in the CLI: `--filters`) –  An array of [Filter](api-datatypes.md#Filter "api-datatypes.md#Filter") objects.

This parameter is not currently supported.

- **Marker**  (in the CLI: `--marker`) –  a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous DescribeDBSubnetGroups
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

- **DBSubnetGroups**   – An array of [DBSubnetGroup](#DBSubnetGroup "#DBSubnetGroup") objects.

A list of [DBSubnetGroup (structure)](#DBSubnetGroup "#DBSubnetGroup") instances.

- **Marker**   – a String, of type: `string` (a UTF-8 encoded string).

An optional pagination token provided by a previous request. If this parameter
is specified, the response includes only records beyond the marker, up to the
value specified by `MaxRecords`.

###### Errors

- [DBSubnetGroupNotFoundFault](api-faults.md#DBSubnetGroupNotFoundFault "api-faults.md#DBSubnetGroupNotFoundFault")

## _Structures:_

## Subnet (structure)

Specifies a subnet.

This data type is used as a response element in the [DescribeDBSubnetGroups (action)](#DescribeDBSubnetGroups "#DescribeDBSubnetGroups") action.

###### Fields

- **SubnetAvailabilityZone** – This is An [AvailabilityZone](api-datatypes.md#AvailabilityZone "api-datatypes.md#AvailabilityZone") object.

Specifies the EC2 Availability Zone that the subnet is in.

- **SubnetIdentifier** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the identifier of the subnet.

- **SubnetStatus** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the status of the subnet.

## DBSubnetGroup (structure)

Contains the details of an Amazon Neptune DB subnet group.

This data type is used as a response element in the [DescribeDBSubnetGroups (action)](#DescribeDBSubnetGroups "#DescribeDBSubnetGroups") action.

###### Fields

- **DBSubnetGroupArn** – This is a String, of type: `string` (a UTF-8 encoded string).

The Amazon Resource Name (ARN) for the DB subnet group.

- **DBSubnetGroupDescription** – This is a String, of type: `string` (a UTF-8 encoded string).

Provides the description of the DB subnet group.

- **DBSubnetGroupName** – This is a String, of type: `string` (a UTF-8 encoded string).

The name of the DB subnet group.

- **SubnetGroupStatus** – This is a String, of type: `string` (a UTF-8 encoded string).

Provides the status of the DB subnet group.

- **Subnets** – This is An array of [Subnet](#Subnet "#Subnet") objects.

Contains a list of [Subnet (structure)](#Subnet "#Subnet") elements.

- **VpcId** – This is a String, of type: `string` (a UTF-8 encoded string).

Provides the VpcId of the DB subnet group.

`DBSubnetGroup` is used as the response element for:

- [CreateDBSubnetGroup](#CreateDBSubnetGroup "#CreateDBSubnetGroup")
- [ModifyDBSubnetGroup](#ModifyDBSubnetGroup "#ModifyDBSubnetGroup")
