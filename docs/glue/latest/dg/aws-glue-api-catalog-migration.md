# Importing an Athena catalog to AWS Glue

The Migration API describes AWS Glue data types and operations
having to do with migrating an Athena Data catalog to AWS Glue.

## Data types

- [CatalogImportStatus structure](#aws-glue-api-catalog-migration-CatalogImportStatus "#aws-glue-api-catalog-migration-CatalogImportStatus")

## CatalogImportStatus structure

A structure containing migration status information.

###### Fields

- `ImportCompleted` – Boolean.

`True` if the migration has completed, or `False`
otherwise.

- `ImportTime` – Timestamp.

The time that the migration was started.

- `ImportedBy` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the person who initiated the migration.

## Operations

- [ImportCatalogToGlue action (Python: import_catalog_to_glue)](#aws-glue-api-catalog-migration-ImportCatalogToGlue "#aws-glue-api-catalog-migration-ImportCatalogToGlue")
- [GetCatalogImportStatus action (Python: get_catalog_import_status)](#aws-glue-api-catalog-migration-GetCatalogImportStatus "#aws-glue-api-catalog-migration-GetCatalogImportStatus")

## ImportCatalogToGlue action (Python: import_catalog_to_glue)

Imports an existing Amazon Athena Data Catalog to AWS Glue.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the catalog to import. Currently, this should be the AWS account ID.

###### Response

- _No Response parameters._

###### Errors

- `InternalServiceException`
- `OperationTimeoutException`

## GetCatalogImportStatus action (Python: get_catalog_import_status)

Retrieves the status of a migration operation.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the catalog to migrate. Currently, this should be the AWS account ID.

###### Response

- `ImportStatus` – A [CatalogImportStatus](#aws-glue-api-catalog-migration-CatalogImportStatus "#aws-glue-api-catalog-migration-CatalogImportStatus") object.

The status of the specified catalog migration.

###### Errors

- `InternalServiceException`
- `OperationTimeoutException`
