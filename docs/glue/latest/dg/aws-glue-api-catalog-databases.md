# Database API

The Database API describes database data types, and includes the API for
creating, deleting, locating, updating, and listing databases.

## Data types

- [Database structure](#aws-glue-api-catalog-databases-Database "#aws-glue-api-catalog-databases-Database")
- [DatabaseInput structure](#aws-glue-api-catalog-databases-DatabaseInput "#aws-glue-api-catalog-databases-DatabaseInput")
- [PrincipalPermissions structure](#aws-glue-api-catalog-databases-PrincipalPermissions "#aws-glue-api-catalog-databases-PrincipalPermissions")
- [DataLakePrincipal structure](#aws-glue-api-catalog-databases-DataLakePrincipal "#aws-glue-api-catalog-databases-DataLakePrincipal")
- [DatabaseIdentifier structure](#aws-glue-api-catalog-databases-DatabaseIdentifier "#aws-glue-api-catalog-databases-DatabaseIdentifier")
- [FederatedDatabase structure](#aws-glue-api-catalog-databases-FederatedDatabase "#aws-glue-api-catalog-databases-FederatedDatabase")

## Database structure

The `Database` object represents a logical grouping of tables
that might reside in a Hive metastore or an RDBMS.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database. For Hive compatibility, this is folded to lowercase
when it is stored.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the database.

- `LocationUri` – Uniform resource identifier (uri), not less than 1 or more than 1024 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

The location of the database (for example, an HDFS path).

- `Parameters` – A map array of key-value pairs.

Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string, not more than 512000 bytes long.

These key-value pairs define parameters and properties of the database.

- `CreateTime` – Timestamp.

The time at which the metadata database was created in the catalog.

- `CreateTableDefaultPermissions` – An array of [PrincipalPermissions](#aws-glue-api-catalog-databases-PrincipalPermissions "#aws-glue-api-catalog-databases-PrincipalPermissions") objects.

Creates a set of default permissions on the table for principals. Used
by AWS Lake Formation. Not used in the normal course of AWS Glue operations.

- `TargetDatabase` – A [DatabaseIdentifier](#aws-glue-api-catalog-databases-DatabaseIdentifier "#aws-glue-api-catalog-databases-DatabaseIdentifier") object.

A `DatabaseIdentifier` structure that describes a target
database for resource linking.

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which the database resides.

- `FederatedDatabase` – A [FederatedDatabase](#aws-glue-api-catalog-databases-FederatedDatabase "#aws-glue-api-catalog-databases-FederatedDatabase") object.

A `FederatedDatabase` structure that references an entity
outside the AWS Glue Data Catalog.

## DatabaseInput structure

The structure used to create or update a database.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database. For Hive compatibility, this is folded to lowercase
when it is stored.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the database.

- `LocationUri` – Uniform resource identifier (uri), not less than 1 or more than 1024 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

The location of the database (for example, an HDFS path).

- `Parameters` – A map array of key-value pairs.

Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string, not more than 512000 bytes long.

These key-value pairs define parameters and properties of the database.

These key-value pairs define parameters and properties of the database.

- `CreateTableDefaultPermissions` – An array of [PrincipalPermissions](#aws-glue-api-catalog-databases-PrincipalPermissions "#aws-glue-api-catalog-databases-PrincipalPermissions") objects.

Creates a set of default permissions on the table for principals. Used
by AWS Lake Formation. Not used in the normal course of AWS Glue operations.

- `TargetDatabase` – A [DatabaseIdentifier](#aws-glue-api-catalog-databases-DatabaseIdentifier "#aws-glue-api-catalog-databases-DatabaseIdentifier") object.

A `DatabaseIdentifier` structure that describes a target
database for resource linking.

- `FederatedDatabase` – A [FederatedDatabase](#aws-glue-api-catalog-databases-FederatedDatabase "#aws-glue-api-catalog-databases-FederatedDatabase") object.

A `FederatedDatabase` structure that references an entity
outside the AWS Glue Data Catalog.

## PrincipalPermissions structure

Permissions granted to a principal.

###### Fields

- `Principal` – A [DataLakePrincipal](#aws-glue-api-catalog-databases-DataLakePrincipal "#aws-glue-api-catalog-databases-DataLakePrincipal") object.

The principal who is granted permissions.

- `Permissions` – An array of UTF-8 strings.

The permissions that are granted to the principal.

## DataLakePrincipal structure

The AWS Lake Formation principal.

###### Fields

- `DataLakePrincipalIdentifier` – UTF-8 string, not less than 1 or more than 255 bytes long.

An identifier for the AWS Lake Formation principal.

## DatabaseIdentifier structure

A structure that describes a target database for resource linking.

###### Fields

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which the database resides.

- `DatabaseName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the catalog database.

- `Region` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Region of the target database.

## FederatedDatabase structure

A database that points to an entity outside the AWS Glue Data Catalog.

###### Fields

- `Identifier` – UTF-8 string, not less than 1 or more than 512 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique identifier for the federated database.

- `ConnectionName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the connection to the external metastore.

- `ConnectionType` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The type of connection used to access the federated database, such as JDBC,
ODBC, or other supported connection protocols.

## Operations

- [CreateDatabase action (Python: create_database)](#aws-glue-api-catalog-databases-CreateDatabase "#aws-glue-api-catalog-databases-CreateDatabase")
- [UpdateDatabase action (Python: update_database)](#aws-glue-api-catalog-databases-UpdateDatabase "#aws-glue-api-catalog-databases-UpdateDatabase")
- [DeleteDatabase action (Python: delete_database)](#aws-glue-api-catalog-databases-DeleteDatabase "#aws-glue-api-catalog-databases-DeleteDatabase")
- [GetDatabase action (Python: get_database)](#aws-glue-api-catalog-databases-GetDatabase "#aws-glue-api-catalog-databases-GetDatabase")
- [GetDatabases action (Python: get_databases)](#aws-glue-api-catalog-databases-GetDatabases "#aws-glue-api-catalog-databases-GetDatabases")

## CreateDatabase action (Python: create_database)

Creates a new database in a Data Catalog.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which to create the database. If none is provided,
the AWS account ID is used by default.

- `DatabaseInput` – _Required:_ A [DatabaseInput](#aws-glue-api-catalog-databases-DatabaseInput "#aws-glue-api-catalog-databases-DatabaseInput") object.

The metadata for the database.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

The tags you assign to the database.

###### Response

- _No Response parameters._

###### Errors

- `InvalidInputException`
- `AlreadyExistsException`
- `ResourceNumberLimitExceededException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`
- `ConcurrentModificationException`
- `FederatedResourceAlreadyExistsException`
- `FederationSourceException`
- `FederationSourceRetryableException`

## UpdateDatabase action (Python: update_database)

Updates an existing database definition in a Data Catalog.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which the metadata database resides. If none
is provided, the AWS account ID is used by default.

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database to update in the catalog. For Hive compatibility,
this is folded to lowercase.

- `DatabaseInput` – _Required:_ A [DatabaseInput](#aws-glue-api-catalog-databases-DatabaseInput "#aws-glue-api-catalog-databases-DatabaseInput") object.

A `DatabaseInput` object specifying the new definition
of the metadata database in the catalog.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`
- `ConcurrentModificationException`
- `FederationSourceException`
- `FederationSourceRetryableException`
- `AlreadyExistsException`

## DeleteDatabase action (Python: delete_database)

Removes a specified database from a Data Catalog.

###### Note

After completing this operation, you no longer have access to the tables
(and all table versions and partitions that might belong to the tables) and the
user-defined functions in the deleted database. AWS Glue deletes
these "orphaned" resources asynchronously in a timely manner, at the discretion
of the service.

To ensure the immediate deletion of all related resources, before calling
`DeleteDatabase`, use `DeleteTableVersion` or `BatchDeleteTableVersion`,
`DeletePartition` or `BatchDeletePartition`, `DeleteUserDefinedFunction`,
and `DeleteTable` or `BatchDeleteTable`, to delete
any resources that belong to the database.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which the database resides. If none is provided,
the AWS account ID is used by default.

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database to delete. For Hive compatibility, this must be
all lowercase.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `ConcurrentModificationException`
- `FederationSourceException`
- `FederationSourceRetryableException`

## GetDatabase action (Python: get_database)

Retrieves the definition of a specified database.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which the database resides. If none is provided,
the AWS account ID is used by default.

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database to retrieve. For Hive compatibility, this should
be all lowercase.

###### Response

- `Database` – A [Database](#aws-glue-api-catalog-databases-Database "#aws-glue-api-catalog-databases-Database") object.

The definition of the specified database in the Data Catalog.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`
- `FederationSourceException`
- `FederationSourceRetryableException`

## GetDatabases action (Python: get_databases)

Retrieves all databases defined in a given Data Catalog.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog from which to retrieve `Databases`.
If none is provided, the AWS account ID is used by default.

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation call.

- `MaxResults` – Number (integer), not less than 1 or more than 100.

The maximum number of databases to return in one response.

- `ResourceShareType` – UTF-8 string (valid values: `FOREIGN` | `ALL` | `FEDERATED`).

Allows you to specify that you want to list the databases shared with your
account. The allowable values are `FEDERATED`, `FOREIGN`
or `ALL`.

    + If set to `FEDERATED`, will list the federated databases
     (referencing an external entity) shared with your account.
    + If set to `FOREIGN`, will list the databases shared with your
     account.
    + If set to `ALL`, will list the databases shared with your account,
     as well as the databases in yor local account.

- `AttributesToGet` – An array of UTF-8 strings.

Specifies the database fields returned by the `GetDatabases`
call. This parameter doesn't accept an empty list. The request must include the
`NAME`.

###### Response

- `DatabaseList` – _Required:_ An array of [Database](#aws-glue-api-catalog-databases-Database "#aws-glue-api-catalog-databases-Database") objects.

A list of `Database` objects from the specified catalog.

- `NextToken` – UTF-8 string.

A continuation token for paginating the returned list of tokens, returned
if the current segment of the list is not the last.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`
- `EntityNotFoundException`
- `FederationSourceException`
- `FederationSourceRetryableException`
