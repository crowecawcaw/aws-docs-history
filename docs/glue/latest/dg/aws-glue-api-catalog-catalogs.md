# Catalogs API

The Catalogs API describes the APIs for creating, deleting, locating,
updating, and listing catalogs.

## Data types

- [Catalog structure](#aws-glue-api-catalog-catalogs-Catalog "#aws-glue-api-catalog-catalogs-Catalog")
- [CatalogInput structure](#aws-glue-api-catalog-catalogs-CatalogInput "#aws-glue-api-catalog-catalogs-CatalogInput")
- [TargetRedshiftCatalog structure](#aws-glue-api-catalog-catalogs-TargetRedshiftCatalog "#aws-glue-api-catalog-catalogs-TargetRedshiftCatalog")
- [CatalogProperties structure](#aws-glue-api-catalog-catalogs-CatalogProperties "#aws-glue-api-catalog-catalogs-CatalogProperties")
- [CatalogPropertiesOutput structure](#aws-glue-api-catalog-catalogs-CatalogPropertiesOutput "#aws-glue-api-catalog-catalogs-CatalogPropertiesOutput")
- [DataLakeAccessProperties structure](#aws-glue-api-catalog-catalogs-DataLakeAccessProperties "#aws-glue-api-catalog-catalogs-DataLakeAccessProperties")
- [IcebergOptimizationProperties structure](#aws-glue-api-catalog-catalogs-IcebergOptimizationProperties "#aws-glue-api-catalog-catalogs-IcebergOptimizationProperties")
- [DataLakeAccessPropertiesOutput structure](#aws-glue-api-catalog-catalogs-DataLakeAccessPropertiesOutput "#aws-glue-api-catalog-catalogs-DataLakeAccessPropertiesOutput")
- [IcebergOptimizationPropertiesOutput structure](#aws-glue-api-catalog-catalogs-IcebergOptimizationPropertiesOutput "#aws-glue-api-catalog-catalogs-IcebergOptimizationPropertiesOutput")
- [FederatedCatalog structure](#aws-glue-api-catalog-catalogs-FederatedCatalog "#aws-glue-api-catalog-catalogs-FederatedCatalog")

## Catalog structure

The catalog object represents a logical grouping of databases in the AWS Glue Data Catalog or a federated source. You can now create a Redshift-federated
catalog or a catalog containing resource links to Redshift databases in another
account or region.

###### Fields

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the catalog. To grant access to the default catalog, this field
should not be provided.

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 64 bytes long, matching the [Custom string pattern #25](aws-glue-api-common.md#regex_25 "aws-glue-api-common.md#regex_25").

The name of the catalog. Cannot be the same as the account ID.

- `ResourceArn` – UTF-8 string.

The Amazon Resource Name (ARN) assigned to the catalog resource.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

Description string, not more than 2048 bytes long, matching the URI address
multi-line string pattern. A description of the catalog.

- `Parameters` – A map array of key-value pairs.

Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string, not more than 512000 bytes long.

A map array of key-value pairs that define parameters and properties of
the catalog.

- `CreateTime` – Timestamp.

The time at which the catalog was created.

- `UpdateTime` – Timestamp.

The time at which the catalog was last updated.

- `TargetRedshiftCatalog` – A [TargetRedshiftCatalog](#aws-glue-api-catalog-catalogs-TargetRedshiftCatalog "#aws-glue-api-catalog-catalogs-TargetRedshiftCatalog") object.

A `TargetRedshiftCatalog` object that describes a target
catalog for database resource linking.

- `FederatedCatalog` – A [FederatedCatalog](#aws-glue-api-catalog-catalogs-FederatedCatalog "#aws-glue-api-catalog-catalogs-FederatedCatalog") object.

A `FederatedCatalog` object that points to an entity outside
the AWS Glue Data Catalog.

- `CatalogProperties` – A [CatalogPropertiesOutput](#aws-glue-api-catalog-catalogs-CatalogPropertiesOutput "#aws-glue-api-catalog-catalogs-CatalogPropertiesOutput") object.

A `CatalogProperties` object that specifies data lake access
properties and other custom properties.

- `CreateTableDefaultPermissions` – An array of [PrincipalPermissions](aws-glue-api-catalog-databases.md#aws-glue-api-catalog-databases-PrincipalPermissions "aws-glue-api-catalog-databases.md#aws-glue-api-catalog-databases-PrincipalPermissions") objects.

An array of `PrincipalPermissions` objects. Creates a set
of default permissions on the table(s) for principals. Used by AWS Lake Formation. Not used in the normal course of AWS Glue operations.

- `CreateDatabaseDefaultPermissions` – An array of [PrincipalPermissions](aws-glue-api-catalog-databases.md#aws-glue-api-catalog-databases-PrincipalPermissions "aws-glue-api-catalog-databases.md#aws-glue-api-catalog-databases-PrincipalPermissions") objects.

An array of `PrincipalPermissions` objects. Creates a set
of default permissions on the database(s) for principals. Used by AWS Lake Formation. Not used in the normal course of AWS Glue operations.

- `AllowFullTableExternalDataAccess` – UTF-8 string (valid values: `True` | `False`).

Allows third-party engines to access data in Amazon S3 locations
that are registered with Lake Formation.

## CatalogInput structure

A structure that describes catalog properties.

###### Fields

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

Description string, not more than 2048 bytes long, matching the URI address
multi-line string pattern. A description of the catalog.

- `FederatedCatalog` – A [FederatedCatalog](#aws-glue-api-catalog-catalogs-FederatedCatalog "#aws-glue-api-catalog-catalogs-FederatedCatalog") object.

A `FederatedCatalog` object. A `FederatedCatalog`
structure that references an entity outside the AWS Glue Data Catalog,
for example a Redshift database.

- `Parameters` – A map array of key-value pairs.

Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string, not more than 512000 bytes long.

A map array of key-value pairs that define the parameters and properties
of the catalog.

- `TargetRedshiftCatalog` – A [TargetRedshiftCatalog](#aws-glue-api-catalog-catalogs-TargetRedshiftCatalog "#aws-glue-api-catalog-catalogs-TargetRedshiftCatalog") object.

A `TargetRedshiftCatalog` object that describes a target
catalog for resource linking.

- `CatalogProperties` – A [CatalogProperties](#aws-glue-api-catalog-catalogs-CatalogProperties "#aws-glue-api-catalog-catalogs-CatalogProperties") object.

A `CatalogProperties` object that specifies data lake access
properties and other custom properties.

- `CreateTableDefaultPermissions` – An array of [PrincipalPermissions](aws-glue-api-catalog-databases.md#aws-glue-api-catalog-databases-PrincipalPermissions "aws-glue-api-catalog-databases.md#aws-glue-api-catalog-databases-PrincipalPermissions") objects.

An array of `PrincipalPermissions` objects. Creates a set
of default permissions on the table(s) for principals. Used by AWS Lake Formation. Typically should be explicitly set as an empty list.

- `CreateDatabaseDefaultPermissions` – An array of [PrincipalPermissions](aws-glue-api-catalog-databases.md#aws-glue-api-catalog-databases-PrincipalPermissions "aws-glue-api-catalog-databases.md#aws-glue-api-catalog-databases-PrincipalPermissions") objects.

An array of `PrincipalPermissions` objects. Creates a set
of default permissions on the database(s) for principals. Used by AWS Lake Formation. Typically should be explicitly set as an empty list.

- `AllowFullTableExternalDataAccess` – UTF-8 string (valid values: `True` | `False`).

Allows third-party engines to access data in Amazon S3 locations
that are registered with Lake Formation.

## TargetRedshiftCatalog structure

A structure that describes a target catalog for resource linking.

###### Fields

- `CatalogArn` – _Required:_ UTF-8 string.

The Amazon Resource Name (ARN) of the catalog resource.

## CatalogProperties structure

A structure that specifies data lake access properties and other custom
properties.

###### Fields

- `DataLakeAccessProperties` – A [DataLakeAccessProperties](#aws-glue-api-catalog-catalogs-DataLakeAccessProperties "#aws-glue-api-catalog-catalogs-DataLakeAccessProperties") object.

A `DataLakeAccessProperties` object that specifies properties
to configure data lake access for your catalog resource in the AWS Glue Data Catalog.

- `IcebergOptimizationProperties` – An [IcebergOptimizationProperties](#aws-glue-api-catalog-catalogs-IcebergOptimizationProperties "#aws-glue-api-catalog-catalogs-IcebergOptimizationProperties") object.

A structure that specifies Iceberg table optimization properties for
the catalog. This includes configuration for compaction, retention, and orphan
file deletion operations that can be applied to Iceberg tables in this catalog.

- `CustomProperties` – A map array of key-value pairs.

Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string, not more than 512000 bytes long.

Additional key-value properties for the catalog, such as column statistics
optimizations.

## CatalogPropertiesOutput structure

Property attributes that include configuration properties for the catalog
resource.

###### Fields

- `DataLakeAccessProperties` – A [DataLakeAccessPropertiesOutput](#aws-glue-api-catalog-catalogs-DataLakeAccessPropertiesOutput "#aws-glue-api-catalog-catalogs-DataLakeAccessPropertiesOutput") object.

A `DataLakeAccessProperties` object with input properties
to configure data lake access for your catalog resource in the AWS Glue Data Catalog.

- `IcebergOptimizationProperties` – An [IcebergOptimizationPropertiesOutput](#aws-glue-api-catalog-catalogs-IcebergOptimizationPropertiesOutput "#aws-glue-api-catalog-catalogs-IcebergOptimizationPropertiesOutput") object.

An `IcebergOptimizationPropertiesOutput` object that
specifies Iceberg table optimization settings for the catalog, including configurations
for compaction, retention, and orphan file deletion operations.

- `CustomProperties` – A map array of key-value pairs.

Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string, not more than 512000 bytes long.

Additional key-value properties for the catalog, such as column statistics
optimizations.

## DataLakeAccessProperties structure

Input properties to configure data lake access for your catalog resource
in the AWS Glue Data Catalog.

###### Fields

- `DataLakeAccess` – Boolean.

Turns on or off data lake access for Apache Spark applications that access
Amazon Redshift databases in the Data Catalog from any non-Redshift engine,
such as Amazon Athena, Amazon EMR, or AWS Glue ETL.

- `DataTransferRole` – UTF-8 string, matching the [Custom string pattern #53](aws-glue-api-common.md#regex_53 "aws-glue-api-common.md#regex_53").

A role that will be assumed by AWS Glue for transferring data
into/out of the staging bucket during a query.

- `KmsKey` – UTF-8 string.

An encryption key that will be used for the staging bucket that will be created
along with the catalog.

- `CatalogType` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Specifies a federated catalog type for the native catalog resource. The
currently supported type is `aws:redshift`.

## IcebergOptimizationProperties structure

A structure that specifies Iceberg table optimization properties for
the catalog, including configurations for compaction, retention, and orphan
file deletion operations.

###### Fields

- `RoleArn` – UTF-8 string, matching the [Custom string pattern #53](aws-glue-api-common.md#regex_53 "aws-glue-api-common.md#regex_53").

The Amazon Resource Name (ARN) of the IAM role that will be assumed to perform
Iceberg table optimization operations.

- `Compaction` – A map array of key-value pairs.

Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string, not more than 512000 bytes long.

A map of key-value pairs that specify configuration parameters for Iceberg
table compaction operations, which optimize the layout of data files to improve
query performance.

- `Retention` – A map array of key-value pairs.

Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string, not more than 512000 bytes long.

A map of key-value pairs that specify configuration parameters for Iceberg
table retention operations, which manage the lifecycle of table snapshots to
control storage costs.

- `OrphanFileDeletion` – A map array of key-value pairs.

Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string, not more than 512000 bytes long.

A map of key-value pairs that specify configuration parameters for Iceberg
orphan file deletion operations, which identify and remove files that are no
longer referenced by the table metadata.

## DataLakeAccessPropertiesOutput structure

The output properties of the data lake access configuration for your catalog
resource in the AWS Glue Data Catalog.

###### Fields

- `DataLakeAccess` – Boolean.

Turns on or off data lake access for Apache Spark applications that access
Amazon Redshift databases in the Data Catalog.

- `DataTransferRole` – UTF-8 string, matching the [Custom string pattern #53](aws-glue-api-common.md#regex_53 "aws-glue-api-common.md#regex_53").

A role that will be assumed by AWS Glue for transferring data
into/out of the staging bucket during a query.

- `KmsKey` – UTF-8 string.

An encryption key that will be used for the staging bucket that will be created
along with the catalog.

- `ManagedWorkgroupName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The managed Redshift Serverless compute name that is created for your
catalog resource.

- `ManagedWorkgroupStatus` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The managed Redshift Serverless compute status.

- `RedshiftDatabaseName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The default Redshift database resource name in the managed compute.

- `StatusMessage` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A message that gives more detailed information about the managed workgroup
status.

- `CatalogType` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Specifies a federated catalog type for the native catalog resource. The
currently supported type is `aws:redshift`.

## IcebergOptimizationPropertiesOutput structure

A structure that contains the output properties of Iceberg table optimization
configuration for your catalog resource in the AWS Glue Data Catalog.

###### Fields

- `RoleArn` – UTF-8 string, matching the [Custom string pattern #53](aws-glue-api-common.md#regex_53 "aws-glue-api-common.md#regex_53").

The Amazon Resource Name (ARN) of the IAM role that is used to perform Iceberg
table optimization operations.

- `Compaction` – A map array of key-value pairs.

Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string, not more than 512000 bytes long.

A map of key-value pairs that specify configuration parameters for Iceberg
table compaction operations, which optimize the layout of data files to improve
query performance.

- `Retention` – A map array of key-value pairs.

Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string, not more than 512000 bytes long.

A map of key-value pairs that specify configuration parameters for Iceberg
table retention operations, which manage the lifecycle of table snapshots to
control storage costs.

- `OrphanFileDeletion` – A map array of key-value pairs.

Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string, not more than 512000 bytes long.

A map of key-value pairs that specify configuration parameters for Iceberg
orphan file deletion operations, which identify and remove files that are no
longer referenced by the table metadata.

- `LastUpdatedTime` – Timestamp.

The timestamp when the Iceberg optimization properties were last updated.

## FederatedCatalog structure

A catalog that points to an entity outside the AWS Glue Data
Catalog.

###### Fields

- `Identifier` – UTF-8 string, not less than 1 or more than 512 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique identifier for the federated catalog.

- `ConnectionName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the connection to an external data source, for example a Redshift-federated
catalog.

- `ConnectionType` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The type of connection used to access the federated catalog, specifying
the protocol or method for connection to the external data source.

## Operations

- [CreateCatalog action (Python: create_catalog)](#aws-glue-api-catalog-catalogs-CreateCatalog "#aws-glue-api-catalog-catalogs-CreateCatalog")
- [UpdateCatalog action (Python: update_catalog)](#aws-glue-api-catalog-catalogs-UpdateCatalog "#aws-glue-api-catalog-catalogs-UpdateCatalog")
- [DeleteCatalog action (Python: delete_catalog)](#aws-glue-api-catalog-catalogs-DeleteCatalog "#aws-glue-api-catalog-catalogs-DeleteCatalog")
- [GetCatalog action (Python: get_catalog)](#aws-glue-api-catalog-catalogs-GetCatalog "#aws-glue-api-catalog-catalogs-GetCatalog")
- [GetCatalogs action (Python: get_catalogs)](#aws-glue-api-catalog-catalogs-GetCatalogs "#aws-glue-api-catalog-catalogs-GetCatalogs")

## CreateCatalog action (Python: create_catalog)

Creates a new catalog in the AWS Glue Data Catalog.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 64 bytes long, matching the [Custom string pattern #25](aws-glue-api-common.md#regex_25 "aws-glue-api-common.md#regex_25").

The name of the catalog to create.

- `CatalogInput` – _Required:_ A [CatalogInput](#aws-glue-api-catalog-catalogs-CatalogInput "#aws-glue-api-catalog-catalogs-CatalogInput") object.

A `CatalogInput` object that defines the metadata for the
catalog.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

A map array of key-value pairs, not more than 50 pairs. Each key is a UTF-8
string, not less than 1 or more than 128 bytes long. Each value is a UTF-8 string,
not more than 256 bytes long. The tags you assign to the catalog.

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
- `AccessDeniedException`
- `EntityNotFoundException`
- `FederatedResourceAlreadyExistsException`
- `FederationSourceException`

## UpdateCatalog action (Python: update_catalog)

Updates an existing catalog's properties in the AWS Glue Data
Catalog.

###### Request

- `CatalogId` – _Required:_ Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the catalog.

- `CatalogInput` – _Required:_ A [CatalogInput](#aws-glue-api-catalog-catalogs-CatalogInput "#aws-glue-api-catalog-catalogs-CatalogInput") object.

A `CatalogInput` object specifying the new properties of
an existing catalog.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`
- `ConcurrentModificationException`
- `AccessDeniedException`
- `FederationSourceException`

## DeleteCatalog action (Python: delete_catalog)

Removes the specified catalog from the AWS Glue Data Catalog.

After completing this operation, you no longer have access to the databases,
tables (and all table versions and partitions that might belong to the tables)
and the user-defined functions in the deleted catalog. AWS Glue deletes
these "orphaned" resources asynchronously in a timely manner, at the discretion
of the service.

To ensure the immediate deletion of all related resources before calling
the `DeleteCatalog` operation, use `DeleteTableVersion`
(or `BatchDeleteTableVersion`), `DeletePartition`
(or `BatchDeletePartition`), `DeleteTable` (or
`BatchDeleteTable`), `DeleteUserDefinedFunction`
and `DeleteDatabase` to delete any resources that belong to the
catalog.

###### Request

- `CatalogId` – _Required:_ Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the catalog.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`
- `ConcurrentModificationException`
- `AccessDeniedException`
- `FederationSourceException`

## GetCatalog action (Python: get_catalog)

The name of the Catalog to retrieve. This should be all lowercase.

###### Request

- `CatalogId` – _Required:_ Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the parent catalog in which the catalog resides. If none is provided,
the AWS Account Number is used by default.

###### Response

- `Catalog` – A [Catalog](#aws-glue-api-catalog-catalogs-Catalog "#aws-glue-api-catalog-catalogs-Catalog") object.

A `Catalog` object. The definition of the specified catalog
in the AWS Glue Data Catalog.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`
- `AccessDeniedException`
- `EntityNotFoundException`
- `FederationSourceException`
- `FederationSourceRetryableException`

## GetCatalogs action (Python: get_catalogs)

Retrieves all catalogs defined in a catalog in the AWS Glue
Data Catalog. For a Redshift-federated catalog use case, this operation returns
the list of catalogs mapped to Redshift databases in the Redshift namespace catalog.

###### Request

- `ParentCatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the parent catalog in which the catalog resides. If none is provided,
the AWS Account Number is used by default.

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation call.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum number of catalogs to return in one response.

- `Recursive` – Boolean.

Whether to list all catalogs across the catalog hierarchy, starting from
the `ParentCatalogId`. Defaults to `false` . When
`true`, all catalog objects in the `ParentCatalogID`
hierarchy are enumerated in the response.

- `IncludeRoot` – Boolean.

Whether to list the default catalog in the account and region in the response.
Defaults to `false`. When `true` and `ParentCatalogId
 = NULL | AWS Account ID`, all catalogs and the default catalog
are enumerated in the response.

When the `ParentCatalogId` is not equal to null, and this
attribute is passed as `false` or `true`, an `InvalidInputException`
is thrown.

###### Response

- `CatalogList` – _Required:_ An array of [Catalog](#aws-glue-api-catalog-catalogs-Catalog "#aws-glue-api-catalog-catalogs-Catalog") objects.

An array of `Catalog` objects. A list of `Catalog`
objects from the specified parent catalog.

- `NextToken` – UTF-8 string.

A continuation token for paginating the returned list of tokens, returned
if the current segment of the list is not the last.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`
- `AccessDeniedException`
- `EntityNotFoundException`
- `FederationSourceException`
- `FederationSourceRetryableException`
