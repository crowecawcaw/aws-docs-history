# Common Neptune Datatypes

**Structures:**

- [AvailabilityZone (structure)](#AvailabilityZone "#AvailabilityZone")
- [DBSecurityGroupMembership (structure)](#DBSecurityGroupMembership "#DBSecurityGroupMembership")
- [DomainMembership (structure)](#DomainMembership "#DomainMembership")
- [DoubleRange (structure)](#DoubleRange "#DoubleRange")
- [Endpoint (structure)](#Endpoint "#Endpoint")
- [Filter (structure)](#Filter "#Filter")
- [Range (structure)](#Range "#Range")
- [ServerlessV2ScalingConfiguration (structure)](#ServerlessV2ScalingConfiguration "#ServerlessV2ScalingConfiguration")
- [ServerlessV2ScalingConfigurationInfo (structure)](#ServerlessV2ScalingConfigurationInfo "#ServerlessV2ScalingConfigurationInfo")
- [Timezone (structure)](#Timezone "#Timezone")
- [VpcSecurityGroupMembership (structure)](#VpcSecurityGroupMembership "#VpcSecurityGroupMembership")

## AvailabilityZone (structure)

Specifies an Availability Zone.

###### Fields

- **Name** – This is a String, of type: `string` (a UTF-8 encoded string).

The name of the availability zone.

## DBSecurityGroupMembership (structure)

Specifies membership in a designated DB security group.

###### Fields

- **DBSecurityGroupName** – This is a String, of type: `string` (a UTF-8 encoded string).

The name of the DB security group.

- **Status** – This is a String, of type: `string` (a UTF-8 encoded string).

The status of the DB security group.

## DomainMembership (structure)

An Active Directory Domain membership record associated with a DB instance.

###### Fields

- **Domain** – This is a String, of type: `string` (a UTF-8 encoded string).

The identifier of the Active Directory Domain.

- **FQDN** – This is a String, of type: `string` (a UTF-8 encoded string).

The fully qualified domain name of the Active Directory Domain.

- **IAMRoleName** – This is a String, of type: `string` (a UTF-8 encoded string).

The name of the IAM role to be used when making API calls to the Directory
Service.

- **Status** – This is a String, of type: `string` (a UTF-8 encoded string).

The status of the DB instance's Active Directory Domain membership, such
as joined, pending-join, failed etc).

## DoubleRange (structure)

A range of double values.

###### Fields

- **From** – This is a Double, of type: `double` (a double-precisionn IEEE 754 floating-point number).

The minimum value in the range.

- **To** – This is a Double, of type: `double` (a double-precisionn IEEE 754 floating-point number).

The maximum value in the range.

## Endpoint (structure)

Specifies a connection endpoint.

For the data structure that represents Amazon Neptune DB cluster endpoints,
see `DBClusterEndpoint`.

###### Fields

- **Address** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the DNS address of the DB instance.

- **HostedZoneId** – This is a String, of type: `string` (a UTF-8 encoded string).

Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

- **Port** – This is an Integer, of type: `integer` (a signed 32-bit integer).

Specifies the port that the database engine is listening on.

## Filter (structure)

This type is not currently supported.

###### Fields

- **Name** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

This parameter is not currently supported.

- **Values** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

This parameter is not currently supported.

## Range (structure)

A range of integer values.

###### Fields

- **From** – This is an Integer, of type: `integer` (a signed 32-bit integer).

The minimum value in the range.

- **Step** – This is an IntegerOptional, of type: `integer` (a signed 32-bit integer).

The step value for the range. For example, if you have a range of 5,000 to
10,000, with a step value of 1,000, the valid values start at 5,000 and step up by
1,000. Even though 7,500 is within the range, it isn't a valid value for the range.
The valid values are 5,000, 6,000, 7,000, 8,000...

- **To** – This is an Integer, of type: `integer` (a signed 32-bit integer).

The maximum value in the range.

## ServerlessV2ScalingConfiguration (structure)

Contains the scaling configuration of a Neptune Serverless DB cluster.

For more information, see [Using
Amazon Neptune Serverless](neptune-serverless-using.md "neptune-serverless-using.md") in the _Amazon Neptune User Guide_.

###### Fields

- **MaxCapacity** – This is a DoubleOptional, of type: `double` (a double-precisionn IEEE 754 floating-point number).

The maximum number of Neptune capacity units (NCUs) for a DB instance in
a Neptune Serverless cluster. You can specify NCU values in half-step increments,
such as 40, 40.5, 41, and so on.

- **MinCapacity** – This is a DoubleOptional, of type: `double` (a double-precisionn IEEE 754 floating-point number).

The minimum number of Neptune capacity units (NCUs) for a DB instance in
a Neptune Serverless cluster. You can specify NCU values in half-step increments,
such as 8, 8.5, 9, and so on.

## ServerlessV2ScalingConfigurationInfo (structure)

Shows the scaling configuration for a Neptune Serverless DB cluster.

For more information, see [Using
Amazon Neptune Serverless](neptune-serverless-using.md "neptune-serverless-using.md") in the _Amazon Neptune User Guide_.

###### Fields

- **MaxCapacity** – This is a DoubleOptional, of type: `double` (a double-precisionn IEEE 754 floating-point number).

The maximum number of Neptune capacity units (NCUs) for a DB instance in
a Neptune Serverless cluster. You can specify NCU values in half-step increments,
such as 40, 40.5, 41, and so on.

- **MinCapacity** – This is a DoubleOptional, of type: `double` (a double-precisionn IEEE 754 floating-point number).

The minimum number of Neptune capacity units (NCUs) for a DB instance in
a Neptune Serverless cluster. You can specify NCU values in half-step increments,
such as 8, 8.5, 9, and so on.

## Timezone (structure)

A time zone associated with a [DBInstance (structure)](api-instances.md#DBInstance "api-instances.md#DBInstance").

###### Fields

- **TimezoneName** – This is a String, of type: `string` (a UTF-8 encoded string).

The name of the time zone.

## VpcSecurityGroupMembership (structure)

This data type is used as a response element for queries on VPC security
group membership.

###### Fields

- **Status** – This is a String, of type: `string` (a UTF-8 encoded string).

The status of the VPC security group.

- **VpcSecurityGroupId** – This is a String, of type: `string` (a UTF-8 encoded string).

The name of the VPC security group.
