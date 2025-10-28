# User-defined Function API

The User-defined Function API describes AWS Glue data types
and operations used in working with functions.

## Data types

- [UserDefinedFunction structure](#aws-glue-api-catalog-functions-UserDefinedFunction "#aws-glue-api-catalog-functions-UserDefinedFunction")
- [UserDefinedFunctionInput structure](#aws-glue-api-catalog-functions-UserDefinedFunctionInput "#aws-glue-api-catalog-functions-UserDefinedFunctionInput")

## UserDefinedFunction structure

Represents the equivalent of a Hive user-defined function (`UDF`)
definition.

###### Fields

- `FunctionName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the function.

- `DatabaseName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the catalog database that contains the function.

- `ClassName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Java class that contains the function code.

- `OwnerName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The owner of the function.

- `OwnerType` – UTF-8 string (valid values: `USER` | `ROLE` | `GROUP`).

The owner type.

- `CreateTime` – Timestamp.

The time at which the function was created.

- `ResourceUris` – An array of [ResourceUri](aws-glue-api-common.md#aws-glue-api-common-ResourceUri "aws-glue-api-common.md#aws-glue-api-common-ResourceUri") objects, not more than 1000 structures.

The resource URIs for the function.

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which the function resides.

## UserDefinedFunctionInput structure

A structure used to create or update a user-defined function.

###### Fields

- `FunctionName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the function.

- `ClassName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The Java class that contains the function code.

- `OwnerName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The owner of the function.

- `OwnerType` – UTF-8 string (valid values: `USER` | `ROLE` | `GROUP`).

The owner type.

- `ResourceUris` – An array of [ResourceUri](aws-glue-api-common.md#aws-glue-api-common-ResourceUri "aws-glue-api-common.md#aws-glue-api-common-ResourceUri") objects, not more than 1000 structures.

The resource URIs for the function.

## Operations

- [CreateUserDefinedFunction action (Python: create_user_defined_function)](#aws-glue-api-catalog-functions-CreateUserDefinedFunction "#aws-glue-api-catalog-functions-CreateUserDefinedFunction")
- [UpdateUserDefinedFunction action (Python: update_user_defined_function)](#aws-glue-api-catalog-functions-UpdateUserDefinedFunction "#aws-glue-api-catalog-functions-UpdateUserDefinedFunction")
- [DeleteUserDefinedFunction action (Python: delete_user_defined_function)](#aws-glue-api-catalog-functions-DeleteUserDefinedFunction "#aws-glue-api-catalog-functions-DeleteUserDefinedFunction")
- [GetUserDefinedFunction action (Python: get_user_defined_function)](#aws-glue-api-catalog-functions-GetUserDefinedFunction "#aws-glue-api-catalog-functions-GetUserDefinedFunction")
- [GetUserDefinedFunctions action (Python: get_user_defined_functions)](#aws-glue-api-catalog-functions-GetUserDefinedFunctions "#aws-glue-api-catalog-functions-GetUserDefinedFunctions")

## CreateUserDefinedFunction action (Python: create_user_defined_function)

Creates a new function definition in the Data Catalog.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which to create the function. If none is provided,
the AWS account ID is used by default.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the catalog database in which to create the function.

- `FunctionInput` – _Required:_ An [UserDefinedFunctionInput](#aws-glue-api-catalog-functions-UserDefinedFunctionInput "#aws-glue-api-catalog-functions-UserDefinedFunctionInput") object.

A `FunctionInput` object that defines the function to create
in the Data Catalog.

###### Response

- _No Response parameters._

###### Errors

- `AlreadyExistsException`
- `InvalidInputException`
- `InternalServiceException`
- `EntityNotFoundException`
- `OperationTimeoutException`
- `ResourceNumberLimitExceededException`
- `GlueEncryptionException`

## UpdateUserDefinedFunction action (Python: update_user_defined_function)

Updates an existing function definition in the Data Catalog.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog where the function to be updated is located. If
none is provided, the AWS account ID is used by default.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the catalog database where the function to be updated is located.

- `FunctionName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the function.

- `FunctionInput` – _Required:_ An [UserDefinedFunctionInput](#aws-glue-api-catalog-functions-UserDefinedFunctionInput "#aws-glue-api-catalog-functions-UserDefinedFunctionInput") object.

A `FunctionInput` object that redefines the function in
the Data Catalog.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`

## DeleteUserDefinedFunction action (Python: delete_user_defined_function)

Deletes an existing function definition from the Data Catalog.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog where the function to be deleted is located. If
none is supplied, the AWS account ID is used by default.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the catalog database where the function is located.

- `FunctionName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the function definition to be deleted.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`

## GetUserDefinedFunction action (Python: get_user_defined_function)

Retrieves a specified function definition from the Data Catalog.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog where the function to be retrieved is located.
If none is provided, the AWS account ID is used by default.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the catalog database where the function is located.

- `FunctionName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the function.

###### Response

- `UserDefinedFunction` – An [UserDefinedFunction](#aws-glue-api-catalog-functions-UserDefinedFunction "#aws-glue-api-catalog-functions-UserDefinedFunction") object.

The requested function definition.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`

## GetUserDefinedFunctions action (Python: get_user_defined_functions)

Retrieves multiple function definitions from the Data Catalog.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog where the functions to be retrieved are located.
If none is provided, the AWS account ID is used by default.

- `DatabaseName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the catalog database where the functions are located. If none
is provided, functions from all the databases across the catalog will be returned.

- `Pattern` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

An optional function-name pattern string that filters the function definitions
returned.

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation call.

- `MaxResults` – Number (integer), not less than 1 or more than 100.

The maximum number of functions to return in one response.

###### Response

- `UserDefinedFunctions` – An array of [UserDefinedFunction](#aws-glue-api-catalog-functions-UserDefinedFunction "#aws-glue-api-catalog-functions-UserDefinedFunction") objects.

A list of requested function definitions.

- `NextToken` – UTF-8 string.

A continuation token, if the list of functions returned does not include
the last requested function.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`
- `GlueEncryptionException`
