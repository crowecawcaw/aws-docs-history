# Table API

The Table API describes data types and operations associated with tables.

## Data types

- [Table structure](#aws-glue-api-catalog-tables-Table "#aws-glue-api-catalog-tables-Table")
- [TableInput structure](#aws-glue-api-catalog-tables-TableInput "#aws-glue-api-catalog-tables-TableInput")
- [FederatedTable structure](#aws-glue-api-catalog-tables-FederatedTable "#aws-glue-api-catalog-tables-FederatedTable")
- [Column structure](#aws-glue-api-catalog-tables-Column "#aws-glue-api-catalog-tables-Column")
- [StorageDescriptor structure](#aws-glue-api-catalog-tables-StorageDescriptor "#aws-glue-api-catalog-tables-StorageDescriptor")
- [SchemaReference structure](#aws-glue-api-catalog-tables-SchemaReference "#aws-glue-api-catalog-tables-SchemaReference")
- [SerDeInfo structure](#aws-glue-api-catalog-tables-SerDeInfo "#aws-glue-api-catalog-tables-SerDeInfo")
- [Order structure](#aws-glue-api-catalog-tables-Order "#aws-glue-api-catalog-tables-Order")
- [SkewedInfo structure](#aws-glue-api-catalog-tables-SkewedInfo "#aws-glue-api-catalog-tables-SkewedInfo")
- [TableVersion structure](#aws-glue-api-catalog-tables-TableVersion "#aws-glue-api-catalog-tables-TableVersion")
- [TableError structure](#aws-glue-api-catalog-tables-TableError "#aws-glue-api-catalog-tables-TableError")
- [TableVersionError structure](#aws-glue-api-catalog-tables-TableVersionError "#aws-glue-api-catalog-tables-TableVersionError")
- [SortCriterion structure](#aws-glue-api-catalog-tables-SortCriterion "#aws-glue-api-catalog-tables-SortCriterion")
- [TableIdentifier structure](#aws-glue-api-catalog-tables-TableIdentifier "#aws-glue-api-catalog-tables-TableIdentifier")
- [KeySchemaElement structure](#aws-glue-api-catalog-tables-KeySchemaElement "#aws-glue-api-catalog-tables-KeySchemaElement")
- [PartitionIndex structure](#aws-glue-api-catalog-tables-PartitionIndex "#aws-glue-api-catalog-tables-PartitionIndex")
- [PartitionIndexDescriptor structure](#aws-glue-api-catalog-tables-PartitionIndexDescriptor "#aws-glue-api-catalog-tables-PartitionIndexDescriptor")
- [BackfillError structure](#aws-glue-api-catalog-tables-BackfillError "#aws-glue-api-catalog-tables-BackfillError")
- [IcebergInput structure](#aws-glue-api-catalog-tables-IcebergInput "#aws-glue-api-catalog-tables-IcebergInput")
- [OpenTableFormatInput structure](#aws-glue-api-catalog-tables-OpenTableFormatInput "#aws-glue-api-catalog-tables-OpenTableFormatInput")
- [ViewDefinition structure](#aws-glue-api-catalog-tables-ViewDefinition "#aws-glue-api-catalog-tables-ViewDefinition")
- [ViewDefinitionInput structure](#aws-glue-api-catalog-tables-ViewDefinitionInput "#aws-glue-api-catalog-tables-ViewDefinitionInput")
- [ViewRepresentation structure](#aws-glue-api-catalog-tables-ViewRepresentation "#aws-glue-api-catalog-tables-ViewRepresentation")
- [ViewRepresentationInput structure](#aws-glue-api-catalog-tables-ViewRepresentationInput "#aws-glue-api-catalog-tables-ViewRepresentationInput")
- [UpdateOpenTableFormatInput structure](#aws-glue-api-catalog-tables-UpdateOpenTableFormatInput "#aws-glue-api-catalog-tables-UpdateOpenTableFormatInput")
- [UpdateIcebergInput structure](#aws-glue-api-catalog-tables-UpdateIcebergInput "#aws-glue-api-catalog-tables-UpdateIcebergInput")
- [CreateIcebergTableInput structure](#aws-glue-api-catalog-tables-CreateIcebergTableInput "#aws-glue-api-catalog-tables-CreateIcebergTableInput")
- [UpdateIcebergTableInput structure](#aws-glue-api-catalog-tables-UpdateIcebergTableInput "#aws-glue-api-catalog-tables-UpdateIcebergTableInput")
- [IcebergSortOrder structure](#aws-glue-api-catalog-tables-IcebergSortOrder "#aws-glue-api-catalog-tables-IcebergSortOrder")
- [IcebergSortField structure](#aws-glue-api-catalog-tables-IcebergSortField "#aws-glue-api-catalog-tables-IcebergSortField")
- [IcebergPartitionSpec structure](#aws-glue-api-catalog-tables-IcebergPartitionSpec "#aws-glue-api-catalog-tables-IcebergPartitionSpec")
- [IcebergPartitionField structure](#aws-glue-api-catalog-tables-IcebergPartitionField "#aws-glue-api-catalog-tables-IcebergPartitionField")
- [IcebergSchema structure](#aws-glue-api-catalog-tables-IcebergSchema "#aws-glue-api-catalog-tables-IcebergSchema")
- [IcebergStructField structure](#aws-glue-api-catalog-tables-IcebergStructField "#aws-glue-api-catalog-tables-IcebergStructField")
- [IcebergTableUpdate structure](#aws-glue-api-catalog-tables-IcebergTableUpdate "#aws-glue-api-catalog-tables-IcebergTableUpdate")
- [AuditContext structure](#aws-glue-api-catalog-tables-AuditContext "#aws-glue-api-catalog-tables-AuditContext")

## Table structure

Represents a collection of related data organized in columns and rows.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The table name. For Hive compatibility, this must be entirely lowercase.

- `DatabaseName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database where the table metadata resides. For Hive compatibility,
this must be all lowercase.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the table.

- `Owner` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The owner of the table.

- `CreateTime` – Timestamp.

The time when the table definition was created in the Data Catalog.

- `UpdateTime` – Timestamp.

The last time that the table was updated.

- `LastAccessTime` – Timestamp.

The last time that the table was accessed. This is usually taken from HDFS,
and might not be reliable.

- `LastAnalyzedTime` – Timestamp.

The last time that column statistics were computed for this table.

- `Retention` – Number (integer), not more than None.

The retention time for this table.

- `StorageDescriptor` – A [StorageDescriptor](aws-glue-api-catalog-partitions.md#aws-glue-api-catalog-partitions-StorageDescriptor "aws-glue-api-catalog-partitions.md#aws-glue-api-catalog-partitions-StorageDescriptor") object.

A storage descriptor containing information about the physical storage
of this table.

- `PartitionKeys` – An array of [Column](#aws-glue-api-catalog-tables-Column "#aws-glue-api-catalog-tables-Column") objects.

A list of columns by which the table is partitioned. Only primitive types
are supported as partition keys.

When you create a table used by Amazon Athena, and you do not specify any
`partitionKeys`, you must at least set the value of `partitionKeys`
to an empty list. For example:

`"PartitionKeys": []`

- `ViewOriginalText` – UTF-8 string, not more than 409600 bytes long.

Included for Apache Hive compatibility. Not used in the normal course
of AWS Glue operations. If the table is a `VIRTUAL_VIEW`,
certain Athena configuration encoded in base64.

- `ViewExpandedText` – UTF-8 string, not more than 409600 bytes long.

Included for Apache Hive compatibility. Not used in the normal course
of AWS Glue operations.

- `TableType` – UTF-8 string, not more than 255 bytes long.

The type of this table. AWS Glue will create tables with
the `EXTERNAL_TABLE` type. Other services, such as Athena, may create tables with additional table types.

AWS Glue related table types:

EXTERNAL_TABLE

Hive compatible attribute - indicates a non-Hive managed table.

GOVERNED

Used by AWS Lake Formation. The AWS Glue Data Catalog
understands `GOVERNED`.

- `Parameters` – A map array of key-value pairs.

Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string, not more than 512000 bytes long.

These key-value pairs define properties associated with the table.

- `CreatedBy` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The person or entity who created the table.

- `IsRegisteredWithLakeFormation` – Boolean.

Indicates whether the table has been registered with AWS Lake Formation.

- `TargetTable` – A [TableIdentifier](#aws-glue-api-catalog-tables-TableIdentifier "#aws-glue-api-catalog-tables-TableIdentifier") object.

A `TableIdentifier` structure that describes a target table
for resource linking.

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which the table resides.

- `VersionId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the table version.

- `FederatedTable` – A [FederatedTable](#aws-glue-api-catalog-tables-FederatedTable "#aws-glue-api-catalog-tables-FederatedTable") object.

A `FederatedTable` structure that references an entity
outside the AWS Glue Data Catalog.

- `ViewDefinition` – A [ViewDefinition](#aws-glue-api-catalog-tables-ViewDefinition "#aws-glue-api-catalog-tables-ViewDefinition") object.

A structure that contains all the information that defines the view, including
the dialect or dialects for the view, and the query.

- `IsMultiDialectView` – Boolean.

Specifies whether the view supports the SQL dialects of one or more different
query engines and can therefore be read by those engines.

## TableInput structure

A structure used to define a table.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The table name. For Hive compatibility, this is folded to lowercase when
it is stored.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the table.

- `Owner` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The table owner. Included for Apache Hive compatibility. Not used in the
normal course of AWS Glue operations.

- `LastAccessTime` – Timestamp.

The last time that the table was accessed.

- `LastAnalyzedTime` – Timestamp.

The last time that column statistics were computed for this table.

- `Retention` – Number (integer), not more than None.

The retention time for this table.

- `StorageDescriptor` – A [StorageDescriptor](aws-glue-api-catalog-partitions.md#aws-glue-api-catalog-partitions-StorageDescriptor "aws-glue-api-catalog-partitions.md#aws-glue-api-catalog-partitions-StorageDescriptor") object.

A storage descriptor containing information about the physical storage
of this table.

- `PartitionKeys` – An array of [Column](#aws-glue-api-catalog-tables-Column "#aws-glue-api-catalog-tables-Column") objects.

A list of columns by which the table is partitioned. Only primitive types
are supported as partition keys.

When you create a table used by Amazon Athena, and you do not specify any
`partitionKeys`, you must at least set the value of `partitionKeys`
to an empty list. For example:

`"PartitionKeys": []`

- `ViewOriginalText` – UTF-8 string, not more than 409600 bytes long.

Included for Apache Hive compatibility. Not used in the normal course
of AWS Glue operations. If the table is a `VIRTUAL_VIEW`,
certain Athena configuration encoded in base64.

- `ViewExpandedText` – UTF-8 string, not more than 409600 bytes long.

Included for Apache Hive compatibility. Not used in the normal course
of AWS Glue operations.

- `TableType` – UTF-8 string, not more than 255 bytes long.

The type of this table. AWS Glue will create tables with
the `EXTERNAL_TABLE` type. Other services, such as Athena, may create tables with additional table types.

AWS Glue related table types:

EXTERNAL_TABLE

Hive compatible attribute - indicates a non-Hive managed table.

GOVERNED

Used by AWS Lake Formation. The AWS Glue Data Catalog
understands `GOVERNED`.

- `Parameters` – A map array of key-value pairs.

Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string, not more than 512000 bytes long.

These key-value pairs define properties associated with the table.

- `TargetTable` – A [TableIdentifier](#aws-glue-api-catalog-tables-TableIdentifier "#aws-glue-api-catalog-tables-TableIdentifier") object.

A `TableIdentifier` structure that describes a target table
for resource linking.

- `ViewDefinition` – A [ViewDefinitionInput](#aws-glue-api-catalog-tables-ViewDefinitionInput "#aws-glue-api-catalog-tables-ViewDefinitionInput") object.

A structure that contains all the information that defines the view, including
the dialect or dialects for the view, and the query.

## FederatedTable structure

A table that points to an entity outside the AWS Glue Data Catalog.

###### Fields

- `Identifier` – UTF-8 string, not less than 1 or more than 512 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique identifier for the federated table.

- `DatabaseIdentifier` – UTF-8 string, not less than 1 or more than 512 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique identifier for the federated database.

- `ConnectionName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the connection to the external metastore.

- `ConnectionType` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The type of connection used to access the federated table, specifying
the protocol or method for connecting to the external data source.

## Column structure

A column in a `Table`.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the `Column`.

- `Type` – UTF-8 string, not more than 131072 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The data type of the `Column`.

- `Comment` – Comment string, not more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A free-form text comment.

- `Parameters` – A map array of key-value pairs.

Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string, not more than 512000 bytes long.

These key-value pairs define properties associated with the column.

## StorageDescriptor structure

Describes the physical storage of table data.

###### Fields

- `Columns` – An array of [Column](#aws-glue-api-catalog-tables-Column "#aws-glue-api-catalog-tables-Column") objects.

A list of the `Columns` in the table.

- `Location` – Location string, not more than 2056 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

The physical location of the table. By default, this takes the form of the
warehouse location, followed by the database location in the warehouse, followed
by the table name.

- `AdditionalLocations` – An array of UTF-8 strings.

A list of locations that point to the path where a Delta table is located.

- `InputFormat` – Format string, not more than 128 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The input format: `SequenceFileInputFormat` (binary),
or `TextInputFormat`, or a custom format.

- `OutputFormat` – Format string, not more than 128 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The output format: `SequenceFileOutputFormat` (binary),
or `IgnoreKeyTextOutputFormat`, or a custom format.

- `Compressed` – Boolean.

`True` if the data in the table is compressed, or `False`
if not.

- `NumberOfBuckets` – Number (integer).

Must be specified if the table contains any dimension columns.

- `SerdeInfo` – A [SerDeInfo](aws-glue-api-catalog-partitions.md#aws-glue-api-catalog-partitions-SerDeInfo "aws-glue-api-catalog-partitions.md#aws-glue-api-catalog-partitions-SerDeInfo") object.

The serialization/deserialization (SerDe) information.

- `BucketColumns` – An array of UTF-8 strings.

A list of reducer grouping columns, clustering columns, and bucketing
columns in the table.

- `SortColumns` – An array of [Order](#aws-glue-api-catalog-tables-Order "#aws-glue-api-catalog-tables-Order") objects.

A list specifying the sort order of each bucket in the table.

- `Parameters` – A map array of key-value pairs.

Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string, not more than 512000 bytes long.

The user-supplied properties in key-value form.

- `SkewedInfo` – A [SkewedInfo](aws-glue-api-catalog-partitions.md#aws-glue-api-catalog-partitions-SkewedInfo "aws-glue-api-catalog-partitions.md#aws-glue-api-catalog-partitions-SkewedInfo") object.

The information about values that appear frequently in a column (skewed
values).

- `StoredAsSubDirectories` – Boolean.

`True` if the table data is stored in subdirectories, or `False`
if not.

- `SchemaReference` – A [SchemaReference](aws-glue-api-catalog-partitions.md#aws-glue-api-catalog-partitions-SchemaReference "aws-glue-api-catalog-partitions.md#aws-glue-api-catalog-partitions-SchemaReference") object.

An object that references a schema stored in the AWS Glue Schema
Registry.

When creating a table, you can pass an empty list of columns for the schema,
and instead use a schema reference.

## SchemaReference structure

An object that references a schema stored in the AWS Glue Schema
Registry.

###### Fields

- `SchemaId` – A [SchemaId](aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-SchemaId "aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-SchemaId") object.

A structure that contains schema identity fields. Either this or the `SchemaVersionId`
has to be provided.

- `SchemaVersionId` – UTF-8 string, not less than 36 or more than 36 bytes long, matching the [Custom string pattern #45](aws-glue-api-common.md#regex_45 "aws-glue-api-common.md#regex_45").

The unique ID assigned to a version of the schema. Either this or the `SchemaId`
has to be provided.

- `SchemaVersionNumber` – Number (long), not less than 1 or more than 100000.

The version number of the schema.

## SerDeInfo structure

Information about a serialization/deserialization program (SerDe)
that serves as an extractor and loader.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the SerDe.

- `SerializationLibrary` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Usually the class that implements the SerDe. An example is `org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`.

- `Parameters` – A map array of key-value pairs.

Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string, not more than 512000 bytes long.

These key-value pairs define initialization parameters for the SerDe.

## Order structure

Specifies the sort order of a sorted column.

###### Fields

- `Column` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the column.

- `SortOrder` – _Required:_ Number (integer), not more than 1.

Indicates that the column is sorted in ascending order (`== 1`),
or in descending order (`==0`).

## SkewedInfo structure

Specifies skewed values in a table. Skewed values are those that occur
with very high frequency.

###### Fields

- `SkewedColumnNames` – An array of UTF-8 strings.

A list of names of columns that contain skewed values.

- `SkewedColumnValues` – An array of UTF-8 strings.

A list of values that appear so frequently as to be considered skewed.

- `SkewedColumnValueLocationMaps` – A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

A mapping of skewed values to the columns that contain them.

## TableVersion structure

Specifies a version of a table.

###### Fields

- `Table` – A [Table](#aws-glue-api-catalog-tables-Table "#aws-glue-api-catalog-tables-Table") object.

The table in question.

- `VersionId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID value that identifies this table version. A `VersionId`
is a string representation of an integer. Each version is incremented by 1.

## TableError structure

An error record for table operations.

###### Fields

- `TableName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table. For Hive compatibility, this must be entirely lowercase.

- `ErrorDetail` – An [ErrorDetail](aws-glue-api-common.md#aws-glue-api-common-ErrorDetail "aws-glue-api-common.md#aws-glue-api-common-ErrorDetail") object.

The details about the error.

## TableVersionError structure

An error record for table-version operations.

###### Fields

- `TableName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table in question.

- `VersionId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID value of the version in question. A `VersionID` is a
string representation of an integer. Each version is incremented by 1.

- `ErrorDetail` – An [ErrorDetail](aws-glue-api-common.md#aws-glue-api-common-ErrorDetail "aws-glue-api-common.md#aws-glue-api-common-ErrorDetail") object.

The details about the error.

## SortCriterion structure

Specifies a field to sort by and a sort order.

###### Fields

- `FieldName` – Value string, not less than 1 or more than 1024 bytes long.

The name of the field on which to sort.

- `Sort` – UTF-8 string (valid values: `ASC="ASCENDING"` | `DESC="DESCENDING"`).

An ascending or descending sort.

## TableIdentifier structure

A structure that describes a target table for resource linking.

###### Fields

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which the table resides.

- `DatabaseName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the catalog database that contains the target table.

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the target table.

- `Region` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Region of the target table.

## KeySchemaElement structure

A partition key pair consisting of a name and a type.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of a partition key.

- `Type` – _Required:_ UTF-8 string, not more than 131072 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The type of a partition key.

## PartitionIndex structure

A structure for a partition index.

###### Fields

- `Keys` – _Required:_ An array of UTF-8 strings, at least 1 string.

The keys for the partition index.

- `IndexName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the partition index.

## PartitionIndexDescriptor structure

A descriptor for a partition index in a table.

###### Fields

- `IndexName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the partition index.

- `Keys` – _Required:_ An array of [KeySchemaElement](#aws-glue-api-catalog-tables-KeySchemaElement "#aws-glue-api-catalog-tables-KeySchemaElement") objects, at least 1 structure.

A list of one or more keys, as `KeySchemaElement` structures,
for the partition index.

- `IndexStatus` – _Required:_ UTF-8 string (valid values: `CREATING` | `ACTIVE` | `DELETING` | `FAILED`).

The status of the partition index.

The possible statuses are:

    + CREATING: The index is being created. When an index is in a CREATING state,
     the index or its table cannot be deleted.
    + ACTIVE: The index creation succeeds.
    + FAILED: The index creation fails.
    + DELETING: The index is deleted from the list of indexes.

- `BackfillErrors` – An array of [BackfillError](#aws-glue-api-catalog-tables-BackfillError "#aws-glue-api-catalog-tables-BackfillError") objects.

A list of errors that can occur when registering partition indexes for
an existing table.

## BackfillError structure

A list of errors that can occur when registering partition indexes for
an existing table.

These errors give the details about why an index registration failed and
provide a limited number of partitions in the response, so that you can fix the
partitions at fault and try registering the index again. The most common set of
errors that can occur are categorized as follows:

- EncryptedPartitionError: The partitions are encrypted.
- InvalidPartitionTypeDataError: The partition value doesn't match
  the data type for that partition column.
- MissingPartitionValueError: The partitions are encrypted.
- UnsupportedPartitionCharacterError: Characters inside the partition
  value are not supported. For example: U+0000 , U+0001, U+0002.
- InternalError: Any error which does not belong to other error codes.

###### Fields

- `Code` – UTF-8 string (valid values: `ENCRYPTED_PARTITION_ERROR` | `INTERNAL_ERROR` | `INVALID_PARTITION_TYPE_DATA_ERROR` | `MISSING_PARTITION_VALUE_ERROR` | `UNSUPPORTED_PARTITION_CHARACTER_ERROR`).

The error code for an error that occurred when registering partition indexes
for an existing table.

- `Partitions` – An array of [PartitionValueList](aws-glue-api-catalog-partitions.md#aws-glue-api-catalog-partitions-PartitionValueList "aws-glue-api-catalog-partitions.md#aws-glue-api-catalog-partitions-PartitionValueList") objects.

A list of a limited number of partitions in the response.

## IcebergInput structure

A structure that defines an Apache Iceberg metadata table to create in
the catalog.

###### Fields

- `MetadataOperation` – _Required:_ UTF-8 string (valid values: `CREATE`).

A required metadata operation. Can only be set to `CREATE`.

- `Version` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The table version for the Iceberg table. Defaults to 2.

- `CreateIcebergTableInput` – A [CreateIcebergTableInput](#aws-glue-api-catalog-tables-CreateIcebergTableInput "#aws-glue-api-catalog-tables-CreateIcebergTableInput") object.

The configuration parameters required to create a new Iceberg table in
the AWS Glue Data Catalog, including table properties and metadata
specifications.

## OpenTableFormatInput structure

A structure representing an open format table.

###### Fields

- `IcebergInput` – An [IcebergInput](#aws-glue-api-catalog-tables-IcebergInput "#aws-glue-api-catalog-tables-IcebergInput") object.

Specifies an `IcebergInput` structure that defines an Apache
Iceberg metadata table.

## ViewDefinition structure

A structure containing details for representations.

###### Fields

- `IsProtected` – Boolean.

You can set this flag as true to instruct the engine not to push user-provided
operations into the logical plan of the view during query planning. However,
setting this flag does not guarantee that the engine will comply. Refer to the
engine's documentation to understand the guarantees provided, if any.

- `Definer` – UTF-8 string, not less than 20 or more than 2048 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The definer of a view in SQL.

- `SubObjects` – An array of UTF-8 strings, not more than 10 strings.

A list of table Amazon Resource Names (ARNs).

- `Representations` – An array of [ViewRepresentation](#aws-glue-api-catalog-tables-ViewRepresentation "#aws-glue-api-catalog-tables-ViewRepresentation") objects, not less than 1 or more than 1000 structures.

A list of representations.

## ViewDefinitionInput structure

A structure containing details for creating or updating an AWS Glue view.

###### Fields

- `IsProtected` – Boolean.

You can set this flag as true to instruct the engine not to push user-provided
operations into the logical plan of the view during query planning. However,
setting this flag does not guarantee that the engine will comply. Refer to the
engine's documentation to understand the guarantees provided, if any.

- `Definer` – UTF-8 string, not less than 20 or more than 2048 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The definer of a view in SQL.

- `Representations` – An array of [ViewRepresentationInput](#aws-glue-api-catalog-tables-ViewRepresentationInput "#aws-glue-api-catalog-tables-ViewRepresentationInput") objects, not less than 1 or more than 10 structures.

A list of structures that contains the dialect of the view, and the query
that defines the view.

- `SubObjects` – An array of UTF-8 strings, not more than 10 strings.

A list of base table ARNs that make up the view.

## ViewRepresentation structure

A structure that contains the dialect of the view, and the query that defines
the view.

###### Fields

- `Dialect` – UTF-8 string (valid values: `REDSHIFT` | `ATHENA` | `SPARK`).

The dialect of the query engine.

- `DialectVersion` – UTF-8 string, not less than 1 or more than 255 bytes long.

The version of the dialect of the query engine. For example, 3.0.0.

- `ViewOriginalText` – UTF-8 string, not more than 409600 bytes long.

The `SELECT` query provided by the customer during `CREATE
 VIEW DDL`. This SQL is not used during a query on a view (`ViewExpandedText`
is used instead). `ViewOriginalText` is used for cases like `SHOW
 CREATE VIEW` where users want to see the original DDL command that created
the view.

- `ViewExpandedText` – UTF-8 string, not more than 409600 bytes long.

The expanded SQL for the view. This SQL is used by engines while processing
a query on a view. Engines may perform operations during view creation to transform
`ViewOriginalText` to `ViewExpandedText`. For example:

    + Fully qualified identifiers: `SELECT * from table1 -> SELECT
     * from db1.table1`

- `ValidationConnection` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the connection to be used to validate the specific representation
of the view.

- `IsStale` – Boolean.

Dialects marked as stale are no longer valid and must be updated before
they can be queried in their respective query engines.

## ViewRepresentationInput structure

A structure containing details of a representation to update or create
a Lake Formation view.

###### Fields

- `Dialect` – UTF-8 string (valid values: `REDSHIFT` | `ATHENA` | `SPARK`).

A parameter that specifies the engine type of a specific representation.

- `DialectVersion` – UTF-8 string, not less than 1 or more than 255 bytes long.

A parameter that specifies the version of the engine of a specific representation.

- `ViewOriginalText` – UTF-8 string, not more than 409600 bytes long.

A string that represents the original SQL query that describes the view.

- `ValidationConnection` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the connection to be used to validate the specific representation
of the view.

- `ViewExpandedText` – UTF-8 string, not more than 409600 bytes long.

A string that represents the SQL query that describes the view with expanded
resource ARNs

## UpdateOpenTableFormatInput structure

Input parameters for updating open table format tables in AWS GlueData Catalog, serving as a wrapper for format-specific update operations
such as Apache Iceberg.

###### Fields

- `UpdateIcebergInput` – An [UpdateIcebergInput](#aws-glue-api-catalog-tables-UpdateIcebergInput "#aws-glue-api-catalog-tables-UpdateIcebergInput") object.

Apache Iceberg-specific update parameters that define the table modifications
to be applied, including schema changes, partition specifications, and table
properties.

## UpdateIcebergInput structure

Input parameters specific to updating Apache Iceberg tables in AWS Glue Data Catalog, containing the update operations to be applied to an
existing Iceberg table.

###### Fields

- `UpdateIcebergTableInput` – _Required:_ An [UpdateIcebergTableInput](#aws-glue-api-catalog-tables-UpdateIcebergTableInput "#aws-glue-api-catalog-tables-UpdateIcebergTableInput") object.

The specific update operations to be applied to the Iceberg table, containing
a list of updates that define the new state of the table including schema, partitions,
and properties.

## CreateIcebergTableInput structure

The configuration parameters required to create a new Iceberg table in
the AWS Glue Data Catalog, including table properties and metadata
specifications.

###### Fields

- `Location` – _Required:_ Location string, not more than 2056 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

The S3 location where the Iceberg table data will be stored.

- `Schema` – _Required:_ An [IcebergSchema](#aws-glue-api-catalog-tables-IcebergSchema "#aws-glue-api-catalog-tables-IcebergSchema") object.

The schema definition that specifies the structure, field types, and
metadata for the Iceberg table.

- `PartitionSpec` – An [IcebergPartitionSpec](#aws-glue-api-catalog-tables-IcebergPartitionSpec "#aws-glue-api-catalog-tables-IcebergPartitionSpec") object.

The partitioning specification that defines how the Iceberg table data
will be organized and partitioned for optimal query performance.

- `WriteOrder` – An [IcebergSortOrder](#aws-glue-api-catalog-tables-IcebergSortOrder "#aws-glue-api-catalog-tables-IcebergSortOrder") object.

The sort order specification that defines how data should be ordered within
each partition to optimize query performance.

- `Properties` –

Key-value pairs of additional table properties and configuration settings
for the Iceberg table.

## UpdateIcebergTableInput structure

Contains the update operations to be applied to an existing Iceberg table
inAWS Glue Data Catalog, defining the new state of the table metadata.

###### Fields

- `Updates` – _Required:_ An array of [IcebergTableUpdate](#aws-glue-api-catalog-tables-IcebergTableUpdate "#aws-glue-api-catalog-tables-IcebergTableUpdate") objects.

The list of table update operations that specify the changes to be made
to the Iceberg table, including schema modifications, partition specifications,
and table properties.

## IcebergSortOrder structure

Defines the sort order specification for an Iceberg table, determining
how data should be ordered within partitions to optimize query performance.

###### Fields

- `OrderId` – _Required:_ Number (integer).

The unique identifier for this sort order specification within the Iceberg
table's metadata.

- `Fields` – _Required:_ An array of [IcebergSortField](#aws-glue-api-catalog-tables-IcebergSortField "#aws-glue-api-catalog-tables-IcebergSortField") objects.

The list of fields and their sort directions that define the ordering criteria
for the Iceberg table data.

## IcebergSortField structure

Defines a single field within an Iceberg sort order specification, including
the source field, transformation, sort direction, and null value ordering.

###### Fields

- `SourceId` – _Required:_ Number (integer).

The identifier of the source field from the table schema that this sort
field is based on.

- `Transform` – _Required:_ UTF-8 string.

The transformation function applied to the source field before sorting,
such as identity, bucket, or truncate.

- `Direction` – _Required:_ UTF-8 string (valid values: `asc="ASC"` | `desc="DESC"`).

The sort direction for this field, either ascending or descending.

- `NullOrder` – _Required:_ UTF-8 string (valid values: `nulls-first="NULLS_FIRST"` | `nulls-last="NULLS_LAST"`).

The ordering behavior for null values in this field, specifying whether
nulls should appear first or last in the sort order.

## IcebergPartitionSpec structure

Defines the partitioning specification for an Iceberg table, determining
how table data will be organized and partitioned for optimal query performance.

###### Fields

- `Fields` – _Required:_ An array of [IcebergPartitionField](#aws-glue-api-catalog-tables-IcebergPartitionField "#aws-glue-api-catalog-tables-IcebergPartitionField") objects.

The list of partition fields that define how the table data should be partitioned,
including source fields and their transformations.

- `SpecId` – Number (integer).

The unique identifier for this partition specification within the Iceberg
table's metadata history.

## IcebergPartitionField structure

Defines a single partition field within an Iceberg partition specification,
including the source field, transformation function, partition name, and unique
identifier.

###### Fields

- `SourceId` – _Required:_ Number (integer).

The identifier of the source field from the table schema that this partition
field is based on.

- `Transform` – _Required:_ UTF-8 string.

The transformation function applied to the source field to create the
partition, such as identity, bucket, truncate, year, month, day, or hour.

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 1024 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the partition field as it will appear in the partitioned table
structure.

- `FieldId` – Number (integer).

The unique identifier assigned to this partition field within the Iceberg
table's partition specification.

## IcebergSchema structure

Defines the schema structure for an Iceberg table, including field definitions,
data types, and schema metadata.

###### Fields

- `SchemaId` – Number (integer).

The unique identifier for this schema version within the Iceberg table's
schema evolution history.

- `IdentifierFieldIds` – An array of signed 32-bit integers.

The list of field identifiers that uniquely identify records in the table,
used for row-level operations and deduplication.

- `Type` – UTF-8 string (valid values: `struct="STRUCT"`).

The root type of the schema structure, typically "struct" for Iceberg
table schemas.

- `Fields` – _Required:_ An array of [IcebergStructField](#aws-glue-api-catalog-tables-IcebergStructField "#aws-glue-api-catalog-tables-IcebergStructField") objects.

The list of field definitions that make up the table schema, including
field names, types, and metadata.

## IcebergStructField structure

Defines a single field within an Iceberg table schema, including its identifier,
name, data type, nullability, and documentation.

###### Fields

- `Id` – _Required:_ Number (integer).

The unique identifier assigned to this field within the Iceberg table
schema, used for schema evolution and field tracking.

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 1024 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the field as it appears in the table schema and query operations.

- `Type` – _Required:_ An empty-structure named `IcebergDocument`.

The data type definition for this field, specifying the structure and
format of the data it contains.

- `Required` – _Required:_ Boolean.

Indicates whether this field is required (non-nullable) or optional
(nullable) in the table schema.

- `Doc` – Comment string, not more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Optional documentation or description text that provides additional
context about the purpose and usage of this field.

## IcebergTableUpdate structure

Defines a complete set of updates to be applied to an Iceberg table, including
schema changes, partitioning modifications, sort order adjustments, location
updates, and property changes.

###### Fields

- `Schema` – _Required:_ An [IcebergSchema](#aws-glue-api-catalog-tables-IcebergSchema "#aws-glue-api-catalog-tables-IcebergSchema") object.

The updated schema definition for the Iceberg table, specifying any changes
to field structure, data types, or schema metadata.

- `PartitionSpec` – An [IcebergPartitionSpec](#aws-glue-api-catalog-tables-IcebergPartitionSpec "#aws-glue-api-catalog-tables-IcebergPartitionSpec") object.

The updated partitioning specification that defines how the table data
should be reorganized and partitioned.

- `SortOrder` – An [IcebergSortOrder](#aws-glue-api-catalog-tables-IcebergSortOrder "#aws-glue-api-catalog-tables-IcebergSortOrder") object.

The updated sort order specification that defines how data should be ordered
within partitions for optimal query performance.

- `Location` – _Required:_ Location string, not more than 2056 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

The updated S3 location where the Iceberg table data will be stored.

- `Properties` –

Updated key-value pairs of table properties and configuration settings
for the Iceberg table.

## AuditContext structure

A structure containing the Lake Formation audit context.

###### Fields

- `AdditionalAuditContext` – UTF-8 string, not more than 2048 bytes long.

A string containing the additional audit context information.

- `RequestedColumns` – An array of UTF-8 strings.

The requested columns for audit.

- `AllColumnsRequested` – Boolean.

All columns request for audit.

## Operations

- [CreateTable action (Python: create_table)](#aws-glue-api-catalog-tables-CreateTable "#aws-glue-api-catalog-tables-CreateTable")
- [UpdateTable action (Python: update_table)](#aws-glue-api-catalog-tables-UpdateTable "#aws-glue-api-catalog-tables-UpdateTable")
- [DeleteTable action (Python: delete_table)](#aws-glue-api-catalog-tables-DeleteTable "#aws-glue-api-catalog-tables-DeleteTable")
- [BatchDeleteTable action (Python: batch_delete_table)](#aws-glue-api-catalog-tables-BatchDeleteTable "#aws-glue-api-catalog-tables-BatchDeleteTable")
- [GetTable action (Python: get_table)](#aws-glue-api-catalog-tables-GetTable "#aws-glue-api-catalog-tables-GetTable")
- [GetTables action (Python: get_tables)](#aws-glue-api-catalog-tables-GetTables "#aws-glue-api-catalog-tables-GetTables")
- [GetTableVersion action (Python: get_table_version)](#aws-glue-api-catalog-tables-GetTableVersion "#aws-glue-api-catalog-tables-GetTableVersion")
- [GetTableVersions action (Python: get_table_versions)](#aws-glue-api-catalog-tables-GetTableVersions "#aws-glue-api-catalog-tables-GetTableVersions")
- [DeleteTableVersion action (Python: delete_table_version)](#aws-glue-api-catalog-tables-DeleteTableVersion "#aws-glue-api-catalog-tables-DeleteTableVersion")
- [BatchDeleteTableVersion action (Python: batch_delete_table_version)](#aws-glue-api-catalog-tables-BatchDeleteTableVersion "#aws-glue-api-catalog-tables-BatchDeleteTableVersion")
- [SearchTables action (Python: search_tables)](#aws-glue-api-catalog-tables-SearchTables "#aws-glue-api-catalog-tables-SearchTables")
- [GetPartitionIndexes action (Python: get_partition_indexes)](#aws-glue-api-catalog-tables-GetPartitionIndexes "#aws-glue-api-catalog-tables-GetPartitionIndexes")
- [CreatePartitionIndex action (Python: create_partition_index)](#aws-glue-api-catalog-tables-CreatePartitionIndex "#aws-glue-api-catalog-tables-CreatePartitionIndex")
- [DeletePartitionIndex action (Python: delete_partition_index)](#aws-glue-api-catalog-tables-DeletePartitionIndex "#aws-glue-api-catalog-tables-DeletePartitionIndex")
- [GetColumnStatisticsForTable action (Python: get_column_statistics_for_table)](#aws-glue-api-catalog-tables-GetColumnStatisticsForTable "#aws-glue-api-catalog-tables-GetColumnStatisticsForTable")
- [UpdateColumnStatisticsForTable action (Python: update_column_statistics_for_table)](#aws-glue-api-catalog-tables-UpdateColumnStatisticsForTable "#aws-glue-api-catalog-tables-UpdateColumnStatisticsForTable")
- [DeleteColumnStatisticsForTable action (Python: delete_column_statistics_for_table)](#aws-glue-api-catalog-tables-DeleteColumnStatisticsForTable "#aws-glue-api-catalog-tables-DeleteColumnStatisticsForTable")

## CreateTable action (Python: create_table)

Creates a new table definition in the Data Catalog.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog in which to create the `Table`. If
none is supplied, the AWS account ID is used by default.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The catalog database in which to create the new table. For Hive compatibility,
this name is entirely lowercase.

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier for the table within the specified database that
will be created in the AWS Glue Data Catalog.

- `TableInput` – A [TableInput](#aws-glue-api-catalog-tables-TableInput "#aws-glue-api-catalog-tables-TableInput") object.

The `TableInput` object that defines the metadata table
to create in the catalog.

- `PartitionIndexes` – An array of [PartitionIndex](#aws-glue-api-catalog-tables-PartitionIndex "#aws-glue-api-catalog-tables-PartitionIndex") objects, not more than 3 structures.

A list of partition indexes, `PartitionIndex` structures,
to create in the table.

- `TransactionId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #44](aws-glue-api-common.md#regex_44 "aws-glue-api-common.md#regex_44").

The ID of the transaction.

- `OpenTableFormatInput` – An [OpenTableFormatInput](#aws-glue-api-catalog-tables-OpenTableFormatInput "#aws-glue-api-catalog-tables-OpenTableFormatInput") object.

Specifies an `OpenTableFormatInput` structure when creating
an open format table.

###### Response

- _No Response parameters._

###### Errors

- `AlreadyExistsException`
- `InvalidInputException`
- `EntityNotFoundException`
- `ResourceNumberLimitExceededException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`
- `ConcurrentModificationException`
- `ResourceNotReadyException`
- `FederationSourceException`
- `FederationSourceRetryableException`

## UpdateTable action (Python: update_table)

Updates a metadata table in the Data Catalog.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog where the table resides. If none is provided,
the AWS account ID is used by default.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the catalog database in which the table resides. For Hive compatibility,
this name is entirely lowercase.

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique identifier for the table within the specified database that
will be created in the AWS Glue Data Catalog.

- `TableInput` – A [TableInput](#aws-glue-api-catalog-tables-TableInput "#aws-glue-api-catalog-tables-TableInput") object.

An updated `TableInput` object to define the metadata table
in the catalog.

- `SkipArchive` – Boolean.

By default, `UpdateTable` always creates an archived version
of the table before updating it. However, if `skipArchive` is set
to true, `UpdateTable` does not create the archived version.

- `TransactionId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #44](aws-glue-api-common.md#regex_44 "aws-glue-api-common.md#regex_44").

The transaction ID at which to update the table contents.

- `VersionId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The version ID at which to update the table contents.

- `ViewUpdateAction` – UTF-8 string (valid values: `ADD` | `REPLACE` | `ADD_OR_REPLACE` | `DROP`).

The operation to be performed when updating the view.

- `Force` – Boolean.

A flag that can be set to true to ignore matching storage descriptor and
subobject matching requirements.

- `UpdateOpenTableFormatInput` – An [UpdateOpenTableFormatInput](#aws-glue-api-catalog-tables-UpdateOpenTableFormatInput "#aws-glue-api-catalog-tables-UpdateOpenTableFormatInput") object.

Input parameters for updating open table format tables in AWS GlueData Catalog, serving as a wrapper for format-specific update operations
such as Apache Iceberg.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `ConcurrentModificationException`
- `ResourceNumberLimitExceededException`
- `GlueEncryptionException`
- `ResourceNotReadyException`
- `FederationSourceException`
- `FederationSourceRetryableException`
- `AlreadyExistsException`

## DeleteTable action (Python: delete_table)

Removes a table definition from the Data Catalog.

###### Note

After completing this operation, you no longer have access to the table
versions and partitions that belong to the deleted table. AWS Glue
deletes these "orphaned" resources asynchronously in a timely manner, at the
discretion of the service.

To ensure the immediate deletion of all related resources, before calling
`DeleteTable`, use `DeleteTableVersion` or `BatchDeleteTableVersion`,
and `DeletePartition` or `BatchDeletePartition`,
to delete any resources that belong to the table.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog where the table resides. If none is provided,
the AWS account ID is used by default.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the catalog database in which the table resides. For Hive compatibility,
this name is entirely lowercase.

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table to be deleted. For Hive compatibility, this name is
entirely lowercase.

- `TransactionId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #44](aws-glue-api-common.md#regex_44 "aws-glue-api-common.md#regex_44").

The transaction ID at which to delete the table contents.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `ConcurrentModificationException`
- `ResourceNotReadyException`
- `FederationSourceException`
- `FederationSourceRetryableException`

## BatchDeleteTable action (Python: batch_delete_table)

Deletes multiple tables at once.

###### Note

After completing this operation, you no longer have access to the table
versions and partitions that belong to the deleted table. AWS Glue
deletes these "orphaned" resources asynchronously in a timely manner, at the
discretion of the service.

To ensure the immediate deletion of all related resources, before calling
`BatchDeleteTable`, use `DeleteTableVersion` or
`BatchDeleteTableVersion`, and `DeletePartition`
or `BatchDeletePartition`, to delete any resources that belong
to the table.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog where the table resides. If none is provided,
the AWS account ID is used by default.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the catalog database in which the tables to delete reside. For
Hive compatibility, this name is entirely lowercase.

- `TablesToDelete` – _Required:_ An array of UTF-8 strings, not more than 100 strings.

A list of the table to delete.

- `TransactionId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #44](aws-glue-api-common.md#regex_44 "aws-glue-api-common.md#regex_44").

The transaction ID at which to delete the table contents.

###### Response

- `Errors` – An array of [TableError](#aws-glue-api-catalog-tables-TableError "#aws-glue-api-catalog-tables-TableError") objects.

A list of errors encountered in attempting to delete the specified tables.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`
- `ResourceNotReadyException`

## GetTable action (Python: get_table)

Retrieves the `Table` definition in a Data Catalog for a specified
table.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog where the table resides. If none is provided,
the AWS account ID is used by default.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the database in the catalog in which the table resides. For Hive
compatibility, this name is entirely lowercase.

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table for which to retrieve the definition. For Hive compatibility,
this name is entirely lowercase.

- `TransactionId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #44](aws-glue-api-common.md#regex_44 "aws-glue-api-common.md#regex_44").

The transaction ID at which to read the table contents.

- `QueryAsOfTime` – Timestamp.

The time as of when to read the table contents. If not set, the most recent
transaction commit time will be used. Cannot be specified along with `TransactionId`.

- `AuditContext` – An [AuditContext](#aws-glue-api-catalog-tables-AuditContext "#aws-glue-api-catalog-tables-AuditContext") object.

A structure containing the Lake Formation [audit
context](../webapi/API_AuditContext.md "../webapi/API_AuditContext.md").

- `IncludeStatusDetails` – Boolean.

Specifies whether to include status details related to a request to create
or update an AWS Glue Data Catalog view.

###### Response

- `Table` – A [Table](#aws-glue-api-catalog-tables-Table "#aws-glue-api-catalog-tables-Table") object.

The `Table` object that defines the specified table.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`
- `ResourceNotReadyException`
- `FederationSourceException`
- `FederationSourceRetryableException`

## GetTables action (Python: get_tables)

Retrieves the definitions of some or all of the tables in a given `Database`.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog where the tables reside. If none is provided,
the AWS account ID is used by default.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The database in the catalog whose tables to list. For Hive compatibility,
this name is entirely lowercase.

- `Expression` – UTF-8 string, not more than 2048 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A regular expression pattern. If present, only those tables whose names
match the pattern are returned.

- `NextToken` – UTF-8 string.

A continuation token, included if this is a continuation call.

- `MaxResults` – Number (integer), not less than 1 or more than 100.

The maximum number of tables to return in a single response.

- `TransactionId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #44](aws-glue-api-common.md#regex_44 "aws-glue-api-common.md#regex_44").

The transaction ID at which to read the table contents.

- `QueryAsOfTime` – Timestamp.

The time as of when to read the table contents. If not set, the most recent
transaction commit time will be used. Cannot be specified along with `TransactionId`.

- `AuditContext` – An [AuditContext](#aws-glue-api-catalog-tables-AuditContext "#aws-glue-api-catalog-tables-AuditContext") object.

A structure containing the Lake Formation [audit
context](../webapi/API_AuditContext.md "../webapi/API_AuditContext.md").

- `IncludeStatusDetails` – Boolean.

Specifies whether to include status details related to a request to create
or update an AWS Glue Data Catalog view.

- `AttributesToGet` – An array of UTF-8 strings.

Specifies the table fields returned by the `GetTables` call.
This parameter doesn't accept an empty list. The request must include `NAME`.

The following are the valid combinations of values:

    + `NAME` - Names of all tables in the database.
    + `NAME`, `TABLE_TYPE` - Names of all tables and
     the table types.

###### Response

- `TableList` – An array of [Table](#aws-glue-api-catalog-tables-Table "#aws-glue-api-catalog-tables-Table") objects.

A list of the requested `Table` objects.

- `NextToken` – UTF-8 string.

A continuation token, present if the current list segment is not the last.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`
- `GlueEncryptionException`
- `FederationSourceException`
- `FederationSourceRetryableException`

## GetTableVersion action (Python: get_table_version)

Retrieves a specified version of a table.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog where the tables reside. If none is provided,
the AWS account ID is used by default.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The database in the catalog in which the table resides. For Hive compatibility,
this name is entirely lowercase.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table. For Hive compatibility, this name is entirely lowercase.

- `VersionId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID value of the table version to be retrieved. A `VersionID`
is a string representation of an integer. Each version is incremented by 1.

###### Response

- `TableVersion` – A [TableVersion](#aws-glue-api-catalog-tables-TableVersion "#aws-glue-api-catalog-tables-TableVersion") object.

The requested table version.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`

## GetTableVersions action (Python: get_table_versions)

Retrieves a list of strings that identify available versions of a specified
table.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog where the tables reside. If none is provided,
the AWS account ID is used by default.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The database in the catalog in which the table resides. For Hive compatibility,
this name is entirely lowercase.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table. For Hive compatibility, this name is entirely lowercase.

- `NextToken` – UTF-8 string.

A continuation token, if this is not the first call.

- `MaxResults` – Number (integer), not less than 1 or more than 100.

The maximum number of table versions to return in one response.

###### Response

- `TableVersions` – An array of [TableVersion](#aws-glue-api-catalog-tables-TableVersion "#aws-glue-api-catalog-tables-TableVersion") objects.

A list of strings identifying available versions of the specified table.

- `NextToken` – UTF-8 string.

A continuation token, if the list of available versions does not include
the last one.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`

## DeleteTableVersion action (Python: delete_table_version)

Deletes a specified version of a table.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog where the tables reside. If none is provided,
the AWS account ID is used by default.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The database in the catalog in which the table resides. For Hive compatibility,
this name is entirely lowercase.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table. For Hive compatibility, this name is entirely lowercase.

- `VersionId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the table version to be deleted. A `VersionID` is
a string representation of an integer. Each version is incremented by 1.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`

## BatchDeleteTableVersion action (Python: batch_delete_table_version)

Deletes a specified batch of versions of a table.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog where the tables reside. If none is provided,
the AWS account ID is used by default.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The database in the catalog in which the table resides. For Hive compatibility,
this name is entirely lowercase.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the table. For Hive compatibility, this name is entirely lowercase.

- `VersionIds` – _Required:_ An array of UTF-8 strings, not more than 100 strings.

A list of the IDs of versions to be deleted. A `VersionId` is
a string representation of an integer. Each version is incremented by 1.

###### Response

- `Errors` – An array of [TableVersionError](#aws-glue-api-catalog-tables-TableVersionError "#aws-glue-api-catalog-tables-TableVersionError") objects.

A list of errors encountered while trying to delete the specified table
versions.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`

## SearchTables action (Python: search_tables)

Searches a set of tables based on properties in the table metadata as well
as on the parent database. You can search against text or filter conditions.

You can only get tables that you have access to based on the security policies
defined in Lake Formation. You need at least a read-only access to the table for
it to be returned. If you do not have access to all the columns in the table, these
columns will not be searched against when returning the list of tables back to
you. If you have access to the columns but not the data in the columns, those columns
and the associated metadata for those columns will be included in the search.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

A unique identifier, consisting of `*account\_id*`.

- `NextToken` – UTF-8 string.

A continuation token, included if this is a continuation call.

- `Filters` – An array of [PropertyPredicate](aws-glue-api-common.md#aws-glue-api-common-PropertyPredicate "aws-glue-api-common.md#aws-glue-api-common-PropertyPredicate") objects.

A list of key-value pairs, and a comparator used to filter the search results.
Returns all entities matching the predicate.

The `Comparator` member of the `PropertyPredicate`
struct is used only for time fields, and can be omitted for other field types. Also,
when comparing string values, such as when `Key=Name`, a fuzzy match
algorithm is used. The `Key` field (for example, the value of the
`Name` field) is split on certain punctuation characters, for example,
-, :, #, etc. into tokens. Then each token is exact-match compared with the `Value`
member of `PropertyPredicate`. For example, if `Key=Name`
and `Value=link`, tables named `customer-link` and
`xx-link-yy` are returned, but `xxlinkyy` is not returned.

- `SearchText` – Value string, not less than 1 or more than 1024 bytes long.

A string used for a text search.

Specifying a value in quotes filters based on an exact match to the value.

- `SortCriteria` – An array of [SortCriterion](#aws-glue-api-catalog-tables-SortCriterion "#aws-glue-api-catalog-tables-SortCriterion") objects, not more than 1 structures.

A list of criteria for sorting the results by a field name, in an ascending
or descending order.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum number of tables to return in a single response.

- `ResourceShareType` – UTF-8 string (valid values: `FOREIGN` | `ALL` | `FEDERATED`).

Allows you to specify that you want to search the tables shared with your
account. The allowable values are `FOREIGN` or `ALL`.

    + If set to `FOREIGN`, will search the tables shared with your
     account.
    + If set to `ALL`, will search the tables shared with your account,
     as well as the tables in yor local account.

- `IncludeStatusDetails` – Boolean.

Specifies whether to include status details related to a request to create
or update an AWS Glue Data Catalog view.

###### Response

- `NextToken` – UTF-8 string.

A continuation token, present if the current list segment is not the last.

- `TableList` – An array of [Table](#aws-glue-api-catalog-tables-Table "#aws-glue-api-catalog-tables-Table") objects.

A list of the requested `Table` objects. The `SearchTables`
response returns only the tables that you have access to.

###### Errors

- `InternalServiceException`
- `InvalidInputException`
- `OperationTimeoutException`

## GetPartitionIndexes action (Python: get_partition_indexes)

Retrieves the partition indexes associated with a table.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The catalog ID where the table resides.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Specifies the name of a database from which you want to retrieve partition
indexes.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Specifies the name of a table for which you want to retrieve the partition
indexes.

- `NextToken` – UTF-8 string.

A continuation token, included if this is a continuation call.

###### Response

- `PartitionIndexDescriptorList` – An array of [PartitionIndexDescriptor](#aws-glue-api-catalog-tables-PartitionIndexDescriptor "#aws-glue-api-catalog-tables-PartitionIndexDescriptor") objects.

A list of index descriptors.

- `NextToken` – UTF-8 string.

A continuation token, present if the current list segment is not the last.

###### Errors

- `InternalServiceException`
- `OperationTimeoutException`
- `InvalidInputException`
- `EntityNotFoundException`
- `ConflictException`

## CreatePartitionIndex action (Python: create_partition_index)

Creates a specified partition index in an existing table.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The catalog ID where the table resides.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Specifies the name of a database in which you want to create a partition
index.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Specifies the name of a table in which you want to create a partition index.

- `PartitionIndex` – _Required:_ A [PartitionIndex](#aws-glue-api-catalog-tables-PartitionIndex "#aws-glue-api-catalog-tables-PartitionIndex") object.

Specifies a `PartitionIndex` structure to create a partition
index in an existing table.

###### Response

- _No Response parameters._

###### Errors

- `AlreadyExistsException`
- `InvalidInputException`
- `EntityNotFoundException`
- `ResourceNumberLimitExceededException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`

## DeletePartitionIndex action (Python: delete_partition_index)

Deletes a specified partition index from an existing table.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The catalog ID where the table resides.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Specifies the name of a database from which you want to delete a partition
index.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Specifies the name of a table from which you want to delete a partition index.

- `IndexName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the partition index to be deleted.

###### Response

- _No Response parameters._

###### Errors

- `InternalServiceException`
- `OperationTimeoutException`
- `InvalidInputException`
- `EntityNotFoundException`
- `ConflictException`
- `GlueEncryptionException`

## GetColumnStatisticsForTable action (Python: get_column_statistics_for_table)

Retrieves table statistics of columns.

The Identity and Access Management (IAM) permission required for this
operation is `GetTable`.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog where the partitions in question reside. If none
is supplied, the AWS account ID is used by default.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the catalog database where the partitions reside.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the partitions' table.

- `ColumnNames` – _Required:_ An array of UTF-8 strings, not more than 100 strings.

A list of the column names.

###### Response

- `ColumnStatisticsList` – An array of [ColumnStatistics](aws-glue-api-common.md#aws-glue-api-common-ColumnStatistics "aws-glue-api-common.md#aws-glue-api-common-ColumnStatistics") objects.

List of ColumnStatistics.

- `Errors` – An array of [ColumnError](aws-glue-api-common.md#aws-glue-api-common-ColumnError "aws-glue-api-common.md#aws-glue-api-common-ColumnError") objects.

List of ColumnStatistics that failed to be retrieved.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`

## UpdateColumnStatisticsForTable action (Python: update_column_statistics_for_table)

Creates or updates table statistics of columns.

The Identity and Access Management (IAM) permission required for this
operation is `UpdateTable`.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog where the partitions in question reside. If none
is supplied, the AWS account ID is used by default.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the catalog database where the partitions reside.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the partitions' table.

- `ColumnStatisticsList` – _Required:_ An array of [ColumnStatistics](aws-glue-api-common.md#aws-glue-api-common-ColumnStatistics "aws-glue-api-common.md#aws-glue-api-common-ColumnStatistics") objects, not more than 25 structures.

A list of the column statistics.

###### Response

- `Errors` – An array of [ColumnStatisticsError](aws-glue-api-common.md#aws-glue-api-common-ColumnStatisticsError "aws-glue-api-common.md#aws-glue-api-common-ColumnStatisticsError") objects.

List of ColumnStatisticsErrors.

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`

## DeleteColumnStatisticsForTable action (Python: delete_column_statistics_for_table)

Retrieves table statistics of columns.

The Identity and Access Management (IAM) permission required for this
operation is `DeleteTable`.

###### Request

- `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the Data Catalog where the partitions in question reside. If none
is supplied, the AWS account ID is used by default.

- `DatabaseName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the catalog database where the partitions reside.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the partitions' table.

- `ColumnName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the column.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `GlueEncryptionException`
