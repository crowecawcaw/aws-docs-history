# Sensitive data detection API

The Sensitive data detection API describes the APIs used to detect sensitive
data across the columns and rows of your structured data.

## Data types

- [CustomEntityType structure](#aws-glue-api-sensitive-data-api-CustomEntityType "#aws-glue-api-sensitive-data-api-CustomEntityType")

## CustomEntityType structure

An object representing a custom pattern for detecting sensitive data
across the columns and rows of your structured data.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A name for the custom pattern that allows it to be retrieved or deleted later.
This name must be unique per AWS account.

- `RegexString` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A regular expression string that is used for detecting sensitive data
in a custom pattern.

- `ContextWords` – An array of UTF-8 strings, not less than 1 or more than 20 strings.

A list of context words. If none of these context words are found within
the vicinity of the regular expression the data will not be detected as sensitive
data.

If no context words are passed only a regular expression is checked.

## Operations

- [CreateCustomEntityType action (Python: create_custom_entity_type)](#aws-glue-api-sensitive-data-api-CreateCustomEntityType "#aws-glue-api-sensitive-data-api-CreateCustomEntityType")
- [DeleteCustomEntityType action (Python: delete_custom_entity_type)](#aws-glue-api-sensitive-data-api-DeleteCustomEntityType "#aws-glue-api-sensitive-data-api-DeleteCustomEntityType")
- [GetCustomEntityType action (Python: get_custom_entity_type)](#aws-glue-api-sensitive-data-api-GetCustomEntityType "#aws-glue-api-sensitive-data-api-GetCustomEntityType")
- [BatchGetCustomEntityTypes action (Python: batch_get_custom_entity_types)](#aws-glue-api-sensitive-data-api-BatchGetCustomEntityTypes "#aws-glue-api-sensitive-data-api-BatchGetCustomEntityTypes")
- [ListCustomEntityTypes action (Python: list_custom_entity_types)](#aws-glue-api-sensitive-data-api-ListCustomEntityTypes "#aws-glue-api-sensitive-data-api-ListCustomEntityTypes")

## CreateCustomEntityType action (Python: create_custom_entity_type)

Creates a custom pattern that is used to detect sensitive data across the
columns and rows of your structured data.

Each custom pattern you create specifies a regular expression and an optional
list of context words. If no context words are passed only a regular expression
is checked.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A name for the custom pattern that allows it to be retrieved or deleted later.
This name must be unique per AWS account.

- `RegexString` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A regular expression string that is used for detecting sensitive data
in a custom pattern.

- `ContextWords` – An array of UTF-8 strings, not less than 1 or more than 20 strings.

A list of context words. If none of these context words are found within
the vicinity of the regular expression the data will not be detected as sensitive
data.

If no context words are passed only a regular expression is checked.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

A list of tags applied to the custom entity type.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the custom pattern you created.

###### Errors

- `AccessDeniedException`
- `AlreadyExistsException`
- `IdempotentParameterMismatchException`
- `InternalServiceException`
- `InvalidInputException`
- `OperationTimeoutException`
- `ResourceNumberLimitExceededException`

## DeleteCustomEntityType action (Python: delete_custom_entity_type)

Deletes a custom pattern by specifying its name.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the custom pattern that you want to delete.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the custom pattern you deleted.

###### Errors

- `EntityNotFoundException`
- `AccessDeniedException`
- `InternalServiceException`
- `InvalidInputException`
- `OperationTimeoutException`

## GetCustomEntityType action (Python: get_custom_entity_type)

Retrieves the details of a custom pattern by specifying its name.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the custom pattern that you want to retrieve.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the custom pattern that you retrieved.

- `RegexString` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A regular expression string that is used for detecting sensitive data
in a custom pattern.

- `ContextWords` – An array of UTF-8 strings, not less than 1 or more than 20 strings.

A list of context words if specified when you created the custom pattern.
If none of these context words are found within the vicinity of the regular expression
the data will not be detected as sensitive data.

###### Errors

- `EntityNotFoundException`
- `AccessDeniedException`
- `InternalServiceException`
- `InvalidInputException`
- `OperationTimeoutException`

## BatchGetCustomEntityTypes action (Python: batch_get_custom_entity_types)

Retrieves the details for the custom patterns specified by a list of names.

###### Request

- `Names` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 50 strings.

A list of names of the custom patterns that you want to retrieve.

###### Response

- `CustomEntityTypes` – An array of [CustomEntityType](#aws-glue-api-sensitive-data-api-CustomEntityType "#aws-glue-api-sensitive-data-api-CustomEntityType") objects.

A list of `CustomEntityType` objects representing the custom
patterns that have been created.

- `CustomEntityTypesNotFound` – An array of UTF-8 strings, not less than 1 or more than 50 strings.

A list of the names of custom patterns that were not found.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`

## ListCustomEntityTypes action (Python: list_custom_entity_types)

Lists all the custom patterns that have been created.

###### Request

- `NextToken` – UTF-8 string.

A paginated token to offset the results.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum number of results to return.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

A list of key-value pair tags.

###### Response

- `CustomEntityTypes` – An array of [CustomEntityType](#aws-glue-api-sensitive-data-api-CustomEntityType "#aws-glue-api-sensitive-data-api-CustomEntityType") objects.

A list of `CustomEntityType` objects representing custom
patterns.

- `NextToken` – UTF-8 string.

A pagination token, if more results are available.

###### Errors

- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`
