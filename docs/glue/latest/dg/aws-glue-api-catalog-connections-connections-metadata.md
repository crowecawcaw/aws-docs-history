# Connection Metadata and Preview API

The following connection APIs describe operations for describing connection
metadata.

## Data types

- [Entity structure](#aws-glue-api-catalog-connections-connections-metadata-Entity "#aws-glue-api-catalog-connections-connections-metadata-Entity")
- [Field structure](#aws-glue-api-catalog-connections-connections-metadata-Field "#aws-glue-api-catalog-connections-connections-metadata-Field")

## Entity structure

An entity supported by a given `ConnectionType`.

###### Fields

- `EntityName` – UTF-8 string.

The name of the entity.

- `Label` – UTF-8 string.

Label used for the entity.

- `IsParentEntity` – Boolean.

A Boolean value which helps to determine whether there are sub objects
that can be listed.

- `Description` – UTF-8 string.

A description of the entity.

- `Category` – UTF-8 string.

The type of entities that are present in the response. This value depends
on the source connection. For example this is `SObjects` for Salesforce
and `databases` or `schemas` or `tables`
for sources like Amazon Redshift.

- `CustomProperties` –

An optional map of keys which may be returned for an entity by a connector.

## Field structure

The `Field` object has information about the different properties
associated with a field in the connector.

###### Fields

- `FieldName` – UTF-8 string.

A unique identifier for the field.

- `Label` – UTF-8 string.

A readable label used for the field.

- `Description` – UTF-8 string.

A description of the field.

- `FieldType` – UTF-8 string (valid values: `INT` | `SMALLINT` | `BIGINT` | `FLOAT` | `LONG` | `DATE` | `BOOLEAN` | `MAP` | `ARRAY` | `STRING` | `TIMESTAMP` | `DECIMAL` | `BYTE` | `SHORT` | `DOUBLE` | `STRUCT`).

The type of data in the field.

- `IsPrimaryKey` – Boolean.

Indicates whether this field can used as a primary key for the given entity.

- `IsNullable` – Boolean.

Indicates whether this field can be nullable or not.

- `IsRetrievable` – Boolean.

Indicates whether this field can be added in Select clause of SQL query
or whether it is retrievable or not.

- `IsFilterable` – Boolean.

Indicates whether this field can used in a filter clause (`WHERE`
clause) of a SQL statement when querying data.

- `IsPartitionable` – Boolean.

Indicates whether a given field can be used in partitioning the query made
to SaaS.

- `IsCreateable` – Boolean.

Indicates whether this field can be created as part of a destination write.

- `IsUpdateable` – Boolean.

Indicates whether this field can be updated as part of a destination write.

- `IsUpsertable` – Boolean.

Indicates whether this field can be upserted as part of a destination write.

- `IsDefaultOnCreate` – Boolean.

Indicates whether this field is populated automatically when the object
is created, such as a created at timestamp.

- `SupportedValues` – .

A list of supported values for the field.

- `SupportedFilterOperators` – An array of UTF-8 strings.

Indicates the support filter operators for this field.

- `CustomProperties` –

Optional map of keys which may be returned.

## Operations

- [ListEntities action (Python: list_entities)](#aws-glue-api-catalog-connections-connections-metadata-ListEntities "#aws-glue-api-catalog-connections-connections-metadata-ListEntities")
- [DescribeEntity action (Python: describe_entity)](#aws-glue-api-catalog-connections-connections-metadata-DescribeEntity "#aws-glue-api-catalog-connections-connections-metadata-DescribeEntity")
- [GetEntityRecords action (Python: get_entity_records)](#aws-glue-api-catalog-connections-connections-metadata-GetEntityRecords "#aws-glue-api-catalog-connections-connections-metadata-GetEntityRecords")

## ListEntities action (Python: list_entities)

Returns the available entities supported by the connection type.

###### Request

- `ConnectionName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A name for the connection that has required credentials to query any connection
type.

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The catalog ID of the catalog that contains the connection. This can be
null, By default, the AWS Account ID is the catalog ID.

- `ParentEntityName` – UTF-8 string.

Name of the parent entity for which you want to list the children. This parameter
takes a fully-qualified path of the entity in order to list the child entities.

- `NextToken` – UTF-8 string, not less than 1 or more than 2048 bytes long, matching the [Custom string pattern #11](aws-glue-api-common.md#regex_11 "aws-glue-api-common.md#regex_11").

A continuation token, included if this is a continuation call.

- `DataStoreApiVersion` – UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #23](aws-glue-api-common.md#regex_23 "aws-glue-api-common.md#regex_23").

The API version of the SaaS connector.

###### Response

- `Entities` – An array of [Entity](#aws-glue-api-catalog-connections-connections-metadata-Entity "#aws-glue-api-catalog-connections-connections-metadata-Entity") objects.

A list of `Entity` objects.

- `NextToken` – UTF-8 string, not less than 1 or more than 2048 bytes long, matching the [Custom string pattern #11](aws-glue-api-common.md#regex_11 "aws-glue-api-common.md#regex_11").

A continuation token, present if the current segment is not the last.

###### Errors

- `EntityNotFoundException`
- `OperationTimeoutException`
- `InvalidInputException`
- `GlueEncryptionException`
- `ValidationException`
- `FederationSourceException`
- `AccessDeniedException`

## DescribeEntity action (Python: describe_entity)

Provides details regarding the entity used with the connection type,
with a description of the data model for each field in the selected entity.

The response includes all the fields which make up the entity.

###### Request

- `ConnectionName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the connection that contains the connection type credentials.

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The catalog ID of the catalog that contains the connection. This can be
null, By default, the AWS Account ID is the catalog ID.

- `EntityName` – _Required:_ UTF-8 string.

The name of the entity that you want to describe from the connection type.

- `NextToken` – UTF-8 string, not less than 1 or more than 2048 bytes long, matching the [Custom string pattern #11](aws-glue-api-common.md#regex_11 "aws-glue-api-common.md#regex_11").

A continuation token, included if this is a continuation call.

- `DataStoreApiVersion` – UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #23](aws-glue-api-common.md#regex_23 "aws-glue-api-common.md#regex_23").

The version of the API used for the data store.

###### Response

- `Fields` – An array of [Field](#aws-glue-api-catalog-connections-connections-metadata-Field "#aws-glue-api-catalog-connections-connections-metadata-Field") objects.

Describes the fields for that connector entity. This is the list of `Field`
objects. `Field` is very similar to column in a database. The `Field`
object has information about different properties associated with fields in
the connector.

- `NextToken` – UTF-8 string, not less than 1 or more than 2048 bytes long, matching the [Custom string pattern #11](aws-glue-api-common.md#regex_11 "aws-glue-api-common.md#regex_11").

A continuation token, present if the current segment is not the last.

###### Errors

- `EntityNotFoundException`
- `OperationTimeoutException`
- `InvalidInputException`
- `GlueEncryptionException`
- `ValidationException`
- `FederationSourceException`
- `AccessDeniedException`

## GetEntityRecords action (Python: get_entity_records)

This API is used to query preview data from a given connection type or from
a native Amazon S3 based AWS Glue Data Catalog.

Returns records as an array of JSON blobs. Each record is formatted using
Jackson JsonNode based on the field type defined by the `DescribeEntity`
API.

Spark connectors generate schemas according to the same data type mapping
as in the `DescribeEntity` API. Spark connectors convert data to
the appropriate data types matching the schema when returning rows.

###### Request

- `ConnectionName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the connection that contains the connection type credentials.

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The catalog ID of the catalog that contains the connection. This can be
null, By default, the AWS Account ID is the catalog ID.

- `EntityName` – _Required:_ UTF-8 string.

Name of the entity that we want to query the preview data from the given connection
type.

- `NextToken` – UTF-8 string, not less than 1 or more than 2048 bytes long, matching the [Custom string pattern #11](aws-glue-api-common.md#regex_11 "aws-glue-api-common.md#regex_11").

A continuation token, included if this is a continuation call.

- `DataStoreApiVersion` – UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #23](aws-glue-api-common.md#regex_23 "aws-glue-api-common.md#regex_23").

The API version of the SaaS connector.

- `ConnectionOptions` – A map array of key-value pairs, not more than 100 pairs.

Each key is a UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #18](aws-glue-api-common.md#regex_18 "aws-glue-api-common.md#regex_18").

Each value is a UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #17](aws-glue-api-common.md#regex_17 "aws-glue-api-common.md#regex_17").

Connector options that are required to query the data.

- `FilterPredicate` – UTF-8 string, not less than 1 or more than 100000 bytes long.

A filter predicate that you can apply in the query request.

- `Limit` – _Required:_ Number (long), not less than 1 or more than 1000.

Limits the number of records fetched with the request.

- `SelectedFields` – An array of UTF-8 strings, not less than 1 or more than 1000 strings.

List of fields that we want to fetch as part of preview data.

###### Response

- `Records` – An array of a structures.

A list of the requested objects.

- `NextToken` – UTF-8 string, not less than 1 or more than 2048 bytes long, matching the [Custom string pattern #11](aws-glue-api-common.md#regex_11 "aws-glue-api-common.md#regex_11").

A continuation token, present if the current segment is not the last.

###### Errors

- `EntityNotFoundException`
- `OperationTimeoutException`
- `InvalidInputException`
- `GlueEncryptionException`
- `ValidationException`
- `FederationSourceException`
- `AccessDeniedException`
