

# Partition API
<a name="aws-glue-api-catalog-partitions"></a>

The Partition API describes data types and operations used to work with partitions.

## Data types
<a name="aws-glue-api-catalog-partitions-objects"></a>
+ [Partition structure](#aws-glue-api-catalog-partitions-Partition)
+ [PartitionInput structure](#aws-glue-api-catalog-partitions-PartitionInput)
+ [PartitionSpecWithSharedStorageDescriptor structure](#aws-glue-api-catalog-partitions-PartitionSpecWithSharedStorageDescriptor)
+ [PartitionListComposingSpec structure](#aws-glue-api-catalog-partitions-PartitionListComposingSpec)
+ [PartitionSpecProxy structure](#aws-glue-api-catalog-partitions-PartitionSpecProxy)
+ [PartitionValueList structure](#aws-glue-api-catalog-partitions-PartitionValueList)
+ [Segment structure](#aws-glue-api-catalog-partitions-Segment)
+ [PartitionError structure](#aws-glue-api-catalog-partitions-PartitionError)
+ [BatchUpdatePartitionFailureEntry structure](#aws-glue-api-catalog-partitions-BatchUpdatePartitionFailureEntry)
+ [BatchUpdatePartitionRequestEntry structure](#aws-glue-api-catalog-partitions-BatchUpdatePartitionRequestEntry)
+ [StorageDescriptor structure](#aws-glue-api-catalog-partitions-StorageDescriptor)
+ [SchemaReference structure](#aws-glue-api-catalog-partitions-SchemaReference)
+ [SerDeInfo structure](#aws-glue-api-catalog-partitions-SerDeInfo)
+ [SkewedInfo structure](#aws-glue-api-catalog-partitions-SkewedInfo)

## Partition structure
<a name="aws-glue-api-catalog-partitions-Partition"></a>

Represents a slice of table data.

**Fields**
+ `Values` – An array of UTF-8 strings.

  The values of the partition.
+ `DatabaseName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the catalog database in which to create the partition.
+ `TableName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the database table in which to create the partition.
+ `CreationTime` – Timestamp.

  The time at which the partition was created.
+ `LastAccessTime` – Timestamp.

  The last time at which the partition was accessed.
+ `StorageDescriptor` – A [StorageDescriptor](#aws-glue-api-catalog-partitions-StorageDescriptor) object.

  Provides information about the physical location where the partition is stored.
+ `Parameters` – A map array of key-value pairs.

  Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  Each value is a UTF-8 string, not more than 512000 bytes long.

  These key-value pairs define partition parameters.
+ `LastAnalyzedTime` – Timestamp.

  The last time at which column statistics were computed for this partition.
+ `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The ID of the Data Catalog in which the partition resides.

## PartitionInput structure
<a name="aws-glue-api-catalog-partitions-PartitionInput"></a>

The structure used to create and update a partition.

**Fields**
+ `Values` – An array of UTF-8 strings.

  The values of the partition. Although this parameter is not required by the SDK, you must specify this parameter for a valid input.

  The values for the keys for the new partition must be passed as an array of String objects that must be ordered in the same order as the partition keys appearing in the Amazon S3 prefix. Otherwise AWS Glue will add the values to the wrong keys.
+ `LastAccessTime` – Timestamp.

  The last time at which the partition was accessed.
+ `StorageDescriptor` – A [StorageDescriptor](#aws-glue-api-catalog-partitions-StorageDescriptor) object.

  Provides information about the physical location where the partition is stored.
+ `Parameters` – A map array of key-value pairs.

  Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  Each value is a UTF-8 string, not more than 512000 bytes long.

  These key-value pairs define partition parameters.
+ `LastAnalyzedTime` – Timestamp.

  The last time at which column statistics were computed for this partition.

## PartitionSpecWithSharedStorageDescriptor structure
<a name="aws-glue-api-catalog-partitions-PartitionSpecWithSharedStorageDescriptor"></a>

A partition specification for partitions that share a physical location.

**Fields**
+ `StorageDescriptor` – A [StorageDescriptor](#aws-glue-api-catalog-partitions-StorageDescriptor) object.

  The shared physical storage information.
+ `Partitions` – An array of [Partition](#aws-glue-api-catalog-partitions-Partition) objects.

  A list of the partitions that share this physical location.

## PartitionListComposingSpec structure
<a name="aws-glue-api-catalog-partitions-PartitionListComposingSpec"></a>

Lists the related partitions.

**Fields**
+ `Partitions` – An array of [Partition](#aws-glue-api-catalog-partitions-Partition) objects.

  A list of the partitions in the composing specification.

## PartitionSpecProxy structure
<a name="aws-glue-api-catalog-partitions-PartitionSpecProxy"></a>

Provides a root path to specified partitions.

**Fields**
+ `DatabaseName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The catalog database in which the partitions reside.
+ `TableName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the table that contains the partitions.
+ `RootPath` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The root path of the proxy for addressing the partitions.
+ `PartitionSpecWithSharedSD` – A [PartitionSpecWithSharedStorageDescriptor](#aws-glue-api-catalog-partitions-PartitionSpecWithSharedStorageDescriptor) object.

  A specification of partitions that share the same physical storage location.
+ `PartitionListComposingSpec` – A [PartitionListComposingSpec](#aws-glue-api-catalog-partitions-PartitionListComposingSpec) object.

  Specifies a list of partitions.

## PartitionValueList structure
<a name="aws-glue-api-catalog-partitions-PartitionValueList"></a>

Contains a list of values defining partitions.

**Fields**
+ `Values` – *Required:* An array of UTF-8 strings.

  The list of values.

## Segment structure
<a name="aws-glue-api-catalog-partitions-Segment"></a>

Defines a non-overlapping region of a table's partitions, allowing multiple requests to be run in parallel.

**Fields**
+ `SegmentNumber` – *Required:* Number (integer).

  The zero-based index number of the segment. For example, if the total number of segments is 4, `SegmentNumber` values range from 0 through 3.
+ `TotalSegments` – *Required:* Number (integer), not less than 1 or more than 10.

  The total number of segments.

## PartitionError structure
<a name="aws-glue-api-catalog-partitions-PartitionError"></a>

Contains information about a partition error.

**Fields**
+ `PartitionValues` – An array of UTF-8 strings.

  The values that define the partition.
+ `ErrorDetail` – An [ErrorDetail](aws-glue-api-common.md#aws-glue-api-common-ErrorDetail) object.

  The details about the partition error.

## BatchUpdatePartitionFailureEntry structure
<a name="aws-glue-api-catalog-partitions-BatchUpdatePartitionFailureEntry"></a>

Contains information about a batch update partition error.

**Fields**
+ `PartitionValueList` – An array of UTF-8 strings, not more than 100 strings.

  A list of values defining the partitions.
+ `ErrorDetail` – An [ErrorDetail](aws-glue-api-common.md#aws-glue-api-common-ErrorDetail) object.

  The details about the batch update partition error.

## BatchUpdatePartitionRequestEntry structure
<a name="aws-glue-api-catalog-partitions-BatchUpdatePartitionRequestEntry"></a>

A structure that contains the values and structure used to update a partition.

**Fields**
+ `PartitionValueList` – *Required:* An array of UTF-8 strings, not more than 100 strings.

  A list of values defining the partitions.
+ `PartitionInput` – *Required:* A [PartitionInput](#aws-glue-api-catalog-partitions-PartitionInput) object.

  The structure used to update a partition.

## StorageDescriptor structure
<a name="aws-glue-api-catalog-partitions-StorageDescriptor"></a>

Describes the physical storage of table data.

**Fields**
+ `Columns` – An array of [Column](aws-glue-api-catalog-tables.md#aws-glue-api-catalog-tables-Column) objects.

  A list of the `Columns` in the table.
+ `Location` – Location string, not more than 2056 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri).

  The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
+ `AdditionalLocations` – An array of UTF-8 strings.

  A list of locations that point to the path where a Delta table is located.
+ `InputFormat` – Format string, not more than 128 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The input format: `SequenceFileInputFormat` (binary), or `TextInputFormat`, or a custom format.
+ `OutputFormat` – Format string, not more than 128 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The output format: `SequenceFileOutputFormat` (binary), or `IgnoreKeyTextOutputFormat`, or a custom format.
+ `Compressed` – Boolean.

  `True` if the data in the table is compressed, or `False` if not.
+ `NumberOfBuckets` – Number (integer).

  Must be specified if the table contains any dimension columns.
+ `SerdeInfo` – A [SerDeInfo](#aws-glue-api-catalog-partitions-SerDeInfo) object.

  The serialization/deserialization (SerDe) information.
+ `BucketColumns` – An array of UTF-8 strings.

  A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
+ `SortColumns` – An array of [Order](aws-glue-api-catalog-tables.md#aws-glue-api-catalog-tables-Order) objects.

  A list specifying the sort order of each bucket in the table.
+ `Parameters` – A map array of key-value pairs.

  Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  Each value is a UTF-8 string, not more than 512000 bytes long.

  The user-supplied properties in key-value form.
+ `SkewedInfo` – A [SkewedInfo](#aws-glue-api-catalog-partitions-SkewedInfo) object.

  The information about values that appear frequently in a column (skewed values).
+ `StoredAsSubDirectories` – Boolean.

  `True` if the table data is stored in subdirectories, or `False` if not.
+ `SchemaReference` – A [SchemaReference](#aws-glue-api-catalog-partitions-SchemaReference) object.

  An object that references a schema stored in the AWS Glue Schema Registry.

  When creating a table, you can pass an empty list of columns for the schema, and instead use a schema reference.

## SchemaReference structure
<a name="aws-glue-api-catalog-partitions-SchemaReference"></a>

An object that references a schema stored in the AWS Glue Schema Registry.

**Fields**
+ `SchemaId` – A [SchemaId](aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-SchemaId) object.

  A structure that contains schema identity fields. Either this or the `SchemaVersionId` has to be provided.
+ `SchemaVersionId` – UTF-8 string, not less than 36 or more than 36 bytes long, matching the [Custom string pattern #42](aws-glue-api-common.md#regex_42).

  The unique ID assigned to a version of the schema. Either this or the `SchemaId` has to be provided.
+ `SchemaVersionNumber` – Number (long), not less than 1 or more than 100000.

  The version number of the schema.

## SerDeInfo structure
<a name="aws-glue-api-catalog-partitions-SerDeInfo"></a>

Information about a serialization/deserialization program (SerDe) that serves as an extractor and loader.

**Fields**
+ `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  Name of the SerDe.
+ `SerializationLibrary` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  Usually the class that implements the SerDe. An example is `org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`.
+ `Parameters` – A map array of key-value pairs.

  Each key is a Key string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  Each value is a UTF-8 string, not more than 512000 bytes long.

  These key-value pairs define initialization parameters for the SerDe.

## SkewedInfo structure
<a name="aws-glue-api-catalog-partitions-SkewedInfo"></a>

Specifies skewed values in a table. Skewed values are those that occur with very high frequency.

**Fields**
+ `SkewedColumnNames` – An array of UTF-8 strings.

  A list of names of columns that contain skewed values.
+ `SkewedColumnValues` – An array of UTF-8 strings.

  A list of values that appear so frequently as to be considered skewed.
+ `SkewedColumnValueLocationMaps` – A map array of key-value pairs.

  Each key is a UTF-8 string.

  Each value is a UTF-8 string.

  A mapping of skewed values to the columns that contain them.

## Operations
<a name="aws-glue-api-catalog-partitions-actions"></a>
+ [CreatePartition action (Python: create\_partition)](#aws-glue-api-catalog-partitions-CreatePartition)
+ [BatchCreatePartition action (Python: batch\_create\_partition)](#aws-glue-api-catalog-partitions-BatchCreatePartition)
+ [UpdatePartition action (Python: update\_partition)](#aws-glue-api-catalog-partitions-UpdatePartition)
+ [DeletePartition action (Python: delete\_partition)](#aws-glue-api-catalog-partitions-DeletePartition)
+ [BatchDeletePartition action (Python: batch\_delete\_partition)](#aws-glue-api-catalog-partitions-BatchDeletePartition)
+ [GetPartition action (Python: get\_partition)](#aws-glue-api-catalog-partitions-GetPartition)
+ [GetPartitions action (Python: get\_partitions)](#aws-glue-api-catalog-partitions-GetPartitions)
+ [BatchGetPartition action (Python: batch\_get\_partition)](#aws-glue-api-catalog-partitions-BatchGetPartition)
+ [BatchUpdatePartition action (Python: batch\_update\_partition)](#aws-glue-api-catalog-partitions-BatchUpdatePartition)
+ [GetColumnStatisticsForPartition action (Python: get\_column\_statistics\_for\_partition)](#aws-glue-api-catalog-partitions-GetColumnStatisticsForPartition)
+ [UpdateColumnStatisticsForPartition action (Python: update\_column\_statistics\_for\_partition)](#aws-glue-api-catalog-partitions-UpdateColumnStatisticsForPartition)
+ [DeleteColumnStatisticsForPartition action (Python: delete\_column\_statistics\_for\_partition)](#aws-glue-api-catalog-partitions-DeleteColumnStatisticsForPartition)

## CreatePartition action (Python: create\_partition)
<a name="aws-glue-api-catalog-partitions-CreatePartition"></a>

Creates a new partition.

**Request**
+ `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The AWS account ID of the catalog in which the partition is to be created.
+ `DatabaseName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the metadata database in which the partition is to be created.
+ `TableName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the metadata table in which the partition is to be created.
+ `PartitionInput` – *Required:* A [PartitionInput](#aws-glue-api-catalog-partitions-PartitionInput) object.

  A `PartitionInput` structure defining the partition to be created.

**Response**
+ *No Response parameters.*

**Errors**
+ `InvalidInputException`
+ `AlreadyExistsException`
+ `ResourceNumberLimitExceededException`
+ `InternalServiceException`
+ `EntityNotFoundException`
+ `OperationTimeoutException`
+ `GlueEncryptionException`

## BatchCreatePartition action (Python: batch\_create\_partition)
<a name="aws-glue-api-catalog-partitions-BatchCreatePartition"></a>

Creates one or more partitions in a batch operation.

**Request**
+ `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The ID of the catalog in which the partition is to be created. Currently, this should be the AWS account ID.
+ `DatabaseName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the metadata database in which the partition is to be created.
+ `TableName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the metadata table in which the partition is to be created.
+ `PartitionInputList` – *Required:* An array of [PartitionInput](#aws-glue-api-catalog-partitions-PartitionInput) objects, not more than 100 structures.

  A list of `PartitionInput` structures that define the partitions to be created.

**Response**
+ `Errors` – An array of [PartitionError](#aws-glue-api-catalog-partitions-PartitionError) objects.

  The errors encountered when trying to create the requested partitions.

**Errors**
+ `InvalidInputException`
+ `AlreadyExistsException`
+ `ResourceNumberLimitExceededException`
+ `InternalServiceException`
+ `EntityNotFoundException`
+ `OperationTimeoutException`
+ `GlueEncryptionException`

## UpdatePartition action (Python: update\_partition)
<a name="aws-glue-api-catalog-partitions-UpdatePartition"></a>

Updates a partition.

**Request**
+ `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The ID of the Data Catalog where the partition to be updated resides. If none is provided, the AWS account ID is used by default.
+ `DatabaseName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the catalog database in which the table in question resides.
+ `TableName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the table in which the partition to be updated is located.
+ `PartitionValueList` – *Required:* An array of UTF-8 strings, not more than 100 strings.

  List of partition key values that define the partition to update.
+ `PartitionInput` – *Required:* A [PartitionInput](#aws-glue-api-catalog-partitions-PartitionInput) object.

  The new partition object to update the partition to.

  The `Values` property can't be changed. If you want to change the partition key values for a partition, delete and recreate the partition.

**Response**
+ *No Response parameters.*

**Errors**
+ `EntityNotFoundException`
+ `InvalidInputException`
+ `InternalServiceException`
+ `OperationTimeoutException`
+ `GlueEncryptionException`

## DeletePartition action (Python: delete\_partition)
<a name="aws-glue-api-catalog-partitions-DeletePartition"></a>

Deletes a specified partition.

**Request**
+ `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The ID of the Data Catalog where the partition to be deleted resides. If none is provided, the AWS account ID is used by default.
+ `DatabaseName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the catalog database in which the table in question resides.
+ `TableName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the table that contains the partition to be deleted.
+ `PartitionValues` – *Required:* An array of UTF-8 strings.

  The values that define the partition.

**Response**
+ *No Response parameters.*

**Errors**
+ `EntityNotFoundException`
+ `InvalidInputException`
+ `InternalServiceException`
+ `OperationTimeoutException`

## BatchDeletePartition action (Python: batch\_delete\_partition)
<a name="aws-glue-api-catalog-partitions-BatchDeletePartition"></a>

Deletes one or more partitions in a batch operation.

**Request**
+ `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The ID of the Data Catalog where the partition to be deleted resides. If none is provided, the AWS account ID is used by default.
+ `DatabaseName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the catalog database in which the table in question resides.
+ `TableName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the table that contains the partitions to be deleted.
+ `PartitionsToDelete` – *Required:* An array of [PartitionValueList](#aws-glue-api-catalog-partitions-PartitionValueList) objects, not more than 25 structures.

  A list of `PartitionInput` structures that define the partitions to be deleted.

**Response**
+ `Errors` – An array of [PartitionError](#aws-glue-api-catalog-partitions-PartitionError) objects.

  The errors encountered when trying to delete the requested partitions.

**Errors**
+ `InvalidInputException`
+ `EntityNotFoundException`
+ `InternalServiceException`
+ `OperationTimeoutException`

## GetPartition action (Python: get\_partition)
<a name="aws-glue-api-catalog-partitions-GetPartition"></a>

Retrieves information about a specified partition.

**Request**
+ `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The ID of the Data Catalog where the partition in question resides. If none is provided, the AWS account ID is used by default.
+ `DatabaseName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the catalog database where the partition resides.
+ `TableName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the partition's table.
+ `PartitionValues` – *Required:* An array of UTF-8 strings.

  The values that define the partition.

**Response**
+ `Partition` – A [Partition](#aws-glue-api-catalog-partitions-Partition) object.

  The requested information, in the form of a `Partition` object.

**Errors**
+ `EntityNotFoundException`
+ `InvalidInputException`
+ `InternalServiceException`
+ `OperationTimeoutException`
+ `GlueEncryptionException`
+ `FederationSourceException`
+ `FederationSourceRetryableException`

## GetPartitions action (Python: get\_partitions)
<a name="aws-glue-api-catalog-partitions-GetPartitions"></a>

Retrieves information about the partitions in a table.

**Request**
+ `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The ID of the Data Catalog where the partitions in question reside. If none is provided, the AWS account ID is used by default.
+ `DatabaseName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the catalog database where the partitions reside.
+ `TableName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the partitions' table.
+ `Expression` – Predicate string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri).

  An expression that filters the partitions to be returned.

  The expression uses SQL syntax similar to the SQL `WHERE` filter clause. The SQL statement parser [JSQLParser](http://jsqlparser.sourceforge.net/home.php) parses the expression. 

  *Operators*: The following are the operators that you can use in the `Expression` API call:  
=  
Checks whether the values of the two operands are equal; if yes, then the condition becomes true.  
Example: Assume 'variable a' holds 10 and 'variable b' holds 20.   
(a = b) is not true.  
< >  
Checks whether the values of two operands are equal; if the values are not equal, then the condition becomes true.  
Example: (a < > b) is true.  
>  
Checks whether the value of the left operand is greater than the value of the right operand; if yes, then the condition becomes true.  
Example: (a > b) is not true.  
<  
Checks whether the value of the left operand is less than the value of the right operand; if yes, then the condition becomes true.  
Example: (a < b) is true.  
>=  
Checks whether the value of the left operand is greater than or equal to the value of the right operand; if yes, then the condition becomes true.  
Example: (a >= b) is not true.  
<=  
Checks whether the value of the left operand is less than or equal to the value of the right operand; if yes, then the condition becomes true.  
Example: (a <= b) is true.  
AND, OR, IN, BETWEEN, LIKE, NOT, IS NULL  
Logical operators.

  *Supported Partition Key Types*: The following are the supported partition keys.
  + `string`
  + `date`
  + `timestamp`
  + `int`
  + `bigint`
  + `long`
  + `tinyint`
  + `smallint`
  + `decimal`

  If an type is encountered that is not valid, an exception is thrown. 

  The following list shows the valid operators on each type. When you define a crawler, the `partitionKey` type is created as a `STRING`, to be compatible with the catalog partitions. 

  *Sample API Call*:   
**Example**  

  The table `twitter_partition` has three partitions:

  ```
  year = 2015
          year = 2016
          year = 2017
  ```  
**Example**  

  Get partition `year` equal to 2015

  ```
  aws glue get-partitions --database-name dbname --table-name twitter_partition 
          --expression "year*=*'2015'"
  ```  
**Example**  

  Get partition `year` between 2016 and 2018 (exclusive)

  ```
  aws glue get-partitions --database-name dbname --table-name twitter_partition 
          --expression "year>'2016' AND year<'2018'"
  ```  
**Example**  

  Get partition `year` between 2015 and 2018 (inclusive). The following API calls are equivalent to each other:

  ```
  aws glue get-partitions --database-name dbname --table-name twitter_partition 
          --expression "year>='2015' AND year<='2018'"
          
          aws glue get-partitions --database-name dbname --table-name twitter_partition 
          --expression "year BETWEEN 2015 AND 2018"
          
          aws glue get-partitions --database-name dbname --table-name twitter_partition 
          --expression "year IN (2015,2016,2017,2018)"
  ```  
**Example**  

  A wildcard partition filter, where the following call output is partition year=2017. A regular expression is not supported in `LIKE`.

  ```
  aws glue get-partitions --database-name dbname --table-name twitter_partition 
          --expression "year LIKE '%7'"
  ```
+ `NextToken` – UTF-8 string.

  A continuation token, if this is not the first call to retrieve these partitions.
+ `Segment` – A [Segment](#aws-glue-api-catalog-partitions-Segment) object.

  The segment of the table's partitions to scan in this request.
+ `MaxResults` – Number (integer), not less than 1 or more than 1000.

  The maximum number of partitions to return in a single response.
+ `ExcludeColumnSchema` – Boolean.

  When true, specifies not returning the partition column schema. Useful when you are interested only in other partition attributes such as partition values or location. This approach avoids the problem of a large response by not returning duplicate data.
+ `TransactionId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #41](aws-glue-api-common.md#regex_41).

  The transaction ID at which to read the partition contents.
+ `QueryAsOfTime` – Timestamp.

  The time as of when to read the partition contents. If not set, the most recent transaction commit time will be used. Cannot be specified along with `TransactionId`.

**Response**
+ `Partitions` – An array of [Partition](#aws-glue-api-catalog-partitions-Partition) objects.

  A list of requested partitions.
+ `NextToken` – UTF-8 string.

  A continuation token, if the returned list of partitions does not include the last one.

**Errors**
+ `EntityNotFoundException`
+ `InvalidInputException`
+ `OperationTimeoutException`
+ `InternalServiceException`
+ `GlueEncryptionException`
+ `InvalidStateException`
+ `ResourceNotReadyException`
+ `FederationSourceException`
+ `FederationSourceRetryableException`

## BatchGetPartition action (Python: batch\_get\_partition)
<a name="aws-glue-api-catalog-partitions-BatchGetPartition"></a>

Retrieves partitions in a batch request.

**Request**
+ `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The ID of the Data Catalog where the partitions in question reside. If none is supplied, the AWS account ID is used by default.
+ `DatabaseName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the catalog database where the partitions reside.
+ `TableName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the partitions' table.
+ `PartitionsToGet` – *Required:* An array of [PartitionValueList](#aws-glue-api-catalog-partitions-PartitionValueList) objects, not more than 1000 structures.

  A list of partition values identifying the partitions to retrieve.

**Response**
+ `Partitions` – An array of [Partition](#aws-glue-api-catalog-partitions-Partition) objects.

  A list of the requested partitions.
+ `UnprocessedKeys` – An array of [PartitionValueList](#aws-glue-api-catalog-partitions-PartitionValueList) objects, not more than 1000 structures.

  A list of the partition values in the request for which partitions were not returned.

**Errors**
+ `InvalidInputException`
+ `EntityNotFoundException`
+ `OperationTimeoutException`
+ `InternalServiceException`
+ `GlueEncryptionException`
+ `InvalidStateException`
+ `FederationSourceException`
+ `FederationSourceRetryableException`

## BatchUpdatePartition action (Python: batch\_update\_partition)
<a name="aws-glue-api-catalog-partitions-BatchUpdatePartition"></a>

Updates one or more partitions in a batch operation.

**Request**
+ `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The ID of the catalog in which the partition is to be updated. Currently, this should be the AWS account ID.
+ `DatabaseName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the metadata database in which the partition is to be updated.
+ `TableName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the metadata table in which the partition is to be updated.
+ `Entries` – *Required:* An array of [BatchUpdatePartitionRequestEntry](#aws-glue-api-catalog-partitions-BatchUpdatePartitionRequestEntry) objects, not less than 1 or more than 100 structures.

  A list of up to 100 `BatchUpdatePartitionRequestEntry` objects to update.

**Response**
+ `Errors` – An array of [BatchUpdatePartitionFailureEntry](#aws-glue-api-catalog-partitions-BatchUpdatePartitionFailureEntry) objects.

  The errors encountered when trying to update the requested partitions. A list of `BatchUpdatePartitionFailureEntry` objects.

**Errors**
+ `InvalidInputException`
+ `EntityNotFoundException`
+ `OperationTimeoutException`
+ `InternalServiceException`
+ `GlueEncryptionException`

## GetColumnStatisticsForPartition action (Python: get\_column\_statistics\_for\_partition)
<a name="aws-glue-api-catalog-partitions-GetColumnStatisticsForPartition"></a>

Retrieves partition statistics of columns.

The Identity and Access Management (IAM) permission required for this operation is `GetPartition`.

**Request**
+ `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The ID of the Data Catalog where the partitions in question reside. If none is supplied, the AWS account ID is used by default.
+ `DatabaseName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the catalog database where the partitions reside.
+ `TableName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the partitions' table.
+ `PartitionValues` – *Required:* An array of UTF-8 strings.

  A list of partition values identifying the partition.
+ `ColumnNames` – *Required:* An array of UTF-8 strings, not more than 100 strings.

  A list of the column names.

**Response**
+ `ColumnStatisticsList` – An array of [ColumnStatistics](aws-glue-api-common.md#aws-glue-api-common-ColumnStatistics) objects.

  List of ColumnStatistics that failed to be retrieved.
+ `Errors` – An array of [ColumnError](aws-glue-api-common.md#aws-glue-api-common-ColumnError) objects.

  Error occurred during retrieving column statistics data.

**Errors**
+ `EntityNotFoundException`
+ `InvalidInputException`
+ `InternalServiceException`
+ `OperationTimeoutException`
+ `GlueEncryptionException`

## UpdateColumnStatisticsForPartition action (Python: update\_column\_statistics\_for\_partition)
<a name="aws-glue-api-catalog-partitions-UpdateColumnStatisticsForPartition"></a>

Creates or updates partition statistics of columns.

The Identity and Access Management (IAM) permission required for this operation is `UpdatePartition`.

**Request**
+ `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The ID of the Data Catalog where the partitions in question reside. If none is supplied, the AWS account ID is used by default.
+ `DatabaseName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the catalog database where the partitions reside.
+ `TableName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the partitions' table.
+ `PartitionValues` – *Required:* An array of UTF-8 strings.

  A list of partition values identifying the partition.
+ `ColumnStatisticsList` – *Required:* An array of [ColumnStatistics](aws-glue-api-common.md#aws-glue-api-common-ColumnStatistics) objects, not more than 25 structures.

  A list of the column statistics.

**Response**
+ `Errors` – An array of [ColumnStatisticsError](aws-glue-api-common.md#aws-glue-api-common-ColumnStatisticsError) objects.

  Error occurred during updating column statistics data.

**Errors**
+ `EntityNotFoundException`
+ `InvalidInputException`
+ `InternalServiceException`
+ `OperationTimeoutException`
+ `GlueEncryptionException`

## DeleteColumnStatisticsForPartition action (Python: delete\_column\_statistics\_for\_partition)
<a name="aws-glue-api-catalog-partitions-DeleteColumnStatisticsForPartition"></a>

Delete the partition column statistics of a column.

The Identity and Access Management (IAM) permission required for this operation is `DeletePartition`.

**Request**
+ `CatalogId` – Catalog id string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The ID of the Data Catalog where the partitions in question reside. If none is supplied, the AWS account ID is used by default.
+ `DatabaseName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the catalog database where the partitions reside.
+ `TableName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the partitions' table.
+ `PartitionValues` – *Required:* An array of UTF-8 strings.

  A list of partition values identifying the partition.
+ `ColumnName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  Name of the column.

**Response**
+ *No Response parameters.*

**Errors**
+ `EntityNotFoundException`
+ `InvalidInputException`
+ `InternalServiceException`
+ `OperationTimeoutException`
+ `GlueEncryptionException`