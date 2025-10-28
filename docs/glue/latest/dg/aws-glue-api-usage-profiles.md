# Usage profiles

The Usage profiles API describes the data types and API related to creating,
updating, or viewing usage profiles in AWS Glue.

## Data types

- [ProfileConfiguration structure](#aws-glue-api-usage-profiles-ProfileConfiguration "#aws-glue-api-usage-profiles-ProfileConfiguration")
- [ConfigurationObject structure](#aws-glue-api-usage-profiles-ConfigurationObject "#aws-glue-api-usage-profiles-ConfigurationObject")
- [UsageProfileDefinition structure](#aws-glue-api-usage-profiles-UsageProfileDefinition "#aws-glue-api-usage-profiles-UsageProfileDefinition")

## ProfileConfiguration structure

Specifies the job and session values that an admin configures in an AWS Glue usage profile.

###### Fields

- `SessionConfiguration` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a A [ConfigurationObject](#aws-glue-api-usage-profiles-ConfigurationObject "#aws-glue-api-usage-profiles-ConfigurationObject") object.

A key-value map of configuration parameters for AWS Glue sessions.

- `JobConfiguration` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a A [ConfigurationObject](#aws-glue-api-usage-profiles-ConfigurationObject "#aws-glue-api-usage-profiles-ConfigurationObject") object.

A key-value map of configuration parameters for AWS Glue jobs.

## ConfigurationObject structure

Specifies the values that an admin sets for each job or session parameter
configured in a AWS Glue usage profile.

###### Fields

- `DefaultValue` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #35](aws-glue-api-common.md#regex_35 "aws-glue-api-common.md#regex_35").

A default value for the parameter.

- `AllowedValues` – An array of UTF-8 strings.

A list of allowed values for the parameter.

- `MinValue` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #35](aws-glue-api-common.md#regex_35 "aws-glue-api-common.md#regex_35").

A minimum allowed value for the parameter.

- `MaxValue` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #35](aws-glue-api-common.md#regex_35 "aws-glue-api-common.md#regex_35").

A maximum allowed value for the parameter.

## UsageProfileDefinition structure

Describes an AWS Glue usage profile.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the usage profile.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the usage profile.

- `CreatedOn` – Timestamp.

The date and time when the usage profile was created.

- `LastModifiedOn` – Timestamp.

The date and time when the usage profile was last modified.

## Operations

- [CreateUsageProfile action (Python: create_usage_profile)](#aws-glue-api-usage-profiles-CreateUsageProfile "#aws-glue-api-usage-profiles-CreateUsageProfile")
- [GetUsageProfile action (Python: get_usage_profile)](#aws-glue-api-usage-profiles-GetUsageProfile "#aws-glue-api-usage-profiles-GetUsageProfile")
- [UpdateUsageProfile action (Python: update_usage_profile)](#aws-glue-api-usage-profiles-UpdateUsageProfile "#aws-glue-api-usage-profiles-UpdateUsageProfile")
- [DeleteUsageProfile action (Python: delete_usage_profile)](#aws-glue-api-usage-profiles-DeleteUsageProfile "#aws-glue-api-usage-profiles-DeleteUsageProfile")
- [ListUsageProfiles action (Python: list_usage_profiles)](#aws-glue-api-usage-profiles-ListUsageProfiles "#aws-glue-api-usage-profiles-ListUsageProfiles")

## CreateUsageProfile action (Python: create_usage_profile)

Creates an AWS Glue usage profile.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the usage profile.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the usage profile.

- `Configuration` – _Required:_ A [ProfileConfiguration](#aws-glue-api-usage-profiles-ProfileConfiguration "#aws-glue-api-usage-profiles-ProfileConfiguration") object.

A `ProfileConfiguration` object specifying the job and
session values for the profile.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

A list of tags applied to the usage profile.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the usage profile that was created.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `AlreadyExistsException`
- `OperationTimeoutException`
- `ResourceNumberLimitExceededException`
- `OperationNotSupportedException`

## GetUsageProfile action (Python: get_usage_profile)

Retrieves information about the specified AWS Glue usage
profile.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the usage profile to retrieve.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the usage profile.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the usage profile.

- `Configuration` – A [ProfileConfiguration](#aws-glue-api-usage-profiles-ProfileConfiguration "#aws-glue-api-usage-profiles-ProfileConfiguration") object.

A `ProfileConfiguration` object specifying the job and
session values for the profile.

- `CreatedOn` – Timestamp.

The date and time when the usage profile was created.

- `LastModifiedOn` – Timestamp.

The date and time when the usage profile was last modified.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `EntityNotFoundException`
- `OperationTimeoutException`
- `OperationNotSupportedException`

## UpdateUsageProfile action (Python: update_usage_profile)

Update an AWS Glue usage profile.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the usage profile.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the usage profile.

- `Configuration` – _Required:_ A [ProfileConfiguration](#aws-glue-api-usage-profiles-ProfileConfiguration "#aws-glue-api-usage-profiles-ProfileConfiguration") object.

A `ProfileConfiguration` object specifying the job and
session values for the profile.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the usage profile that was updated.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `EntityNotFoundException`
- `OperationTimeoutException`
- `OperationNotSupportedException`
- `ConcurrentModificationException`

## DeleteUsageProfile action (Python: delete_usage_profile)

Deletes the AWS Glue specified usage profile.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the usage profile to delete.

###### Response

- _No Response parameters._

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `OperationNotSupportedException`

## ListUsageProfiles action (Python: list_usage_profiles)

List all the AWS Glue usage profiles.

###### Request

- `NextToken` – UTF-8 string, not more than 400000 bytes long.

A continuation token, included if this is a continuation call.

- `MaxResults` – Number (integer), not less than 1 or more than 200.

The maximum number of usage profiles to return in a single response.

###### Response

- `Profiles` – An array of [UsageProfileDefinition](#aws-glue-api-usage-profiles-UsageProfileDefinition "#aws-glue-api-usage-profiles-UsageProfileDefinition") objects.

A list of usage profile (`UsageProfileDefinition`) objects.

- `NextToken` – UTF-8 string, not more than 400000 bytes long.

A continuation token, present if the current list segment is not the last.

###### Errors

- `InternalServiceException`
- `OperationTimeoutException`
- `InvalidInputException`
- `OperationNotSupportedException`
