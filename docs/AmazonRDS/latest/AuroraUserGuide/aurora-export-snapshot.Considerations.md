

# Considerations for DB cluster snapshot exports
<a name="aurora-export-snapshot.Considerations"></a>

## Limitations
<a name="aurora-export-snapshot.Limits"></a>

Exporting DB snapshot data to Amazon S3 has the following limitations:
+ You can't run multiple export tasks for the same DB cluster snapshot simultaneously. This applies to both full and partial exports.
+ You can have up to five concurrent DB snapshot export tasks in progress per AWS account.
+ Exports to S3 don't support S3 prefixes containing a colon (:).
+ The following characters in the S3 file path are converted to underscores (\_) during export:

  ```
  \ ` " (space)
  ```
+ If a database, schema, or table has characters in its name other than the following, partial export isn't supported. However, you can export the entire DB snapshot.
  + Latin letters (A–Z)
  + Digits (0–9)
  + Dollar symbol ($)
  + Underscore (\_)
+ Spaces ( ) and certain characters aren't supported in database table column names. Tables with the following characters in column names are skipped during export:

  ```
  , ; { } ( ) \n \t = (space)
  ```
+ Tables with slashes (/) in their names are skipped during export.
+ Aurora PostgreSQL temporary and unlogged tables are skipped during export.
+ If the data contains a large object, such as a BLOB or CLOB, that is close to or greater than 500 MB, then the export fails.
+ If a table contains a large row that is close to or greater than 2 GB, then the table is skipped during export.
+ For partial exports, the `ExportOnly` list has a maximum size of 200 KB.
+ We strongly recommend that you use a unique name for each export task. If you don't use a unique task name, you might receive the following error message:

  ExportTaskAlreadyExistsFault: An error occurred (ExportTaskAlreadyExists) when calling the StartExportTask operation: The export task with the ID {{xxxxx}} already exists.
+ You can delete a snapshot while you're exporting its data to S3, but you're still charged for the storage costs for that snapshot until the export task has completed.
+ You can't restore exported snapshot data from S3 to a new DB cluster.

## File naming convention
<a name="aurora-export-snapshot.FileNames"></a>

Exported data for specific tables is stored in the format `{{base_prefix}}/{{files}}`, where the base prefix is the following:

```
{{export_identifier}}/{{database_name}}/{{schema_name}}.{{table_name}}/
```

For example:

```
export-1234567890123-459/rdststdb/rdststdb.DataInsert_7ADB5D19965123A2/
```

There are two conventions for how files are named.
+ Current convention:

  ```
  {{batch_index}}/part-{{partition_index}}-{{random_uuid}}.{{format-based_extension}}
  ```

  The batch index is a sequence number that represents a batch of data read from the table. If we can't partition your table into small chunks to be exported in parallel, there will be multiple batch indexes. The same thing happens if your table is partitioned into multiple tables. There will be multiple batch indexes, one for each of the table partitions of your main table.

  If we can partition your table into small chunks to be read in parallel, there will be only the batch index `1` folder.

  Inside the batch index folder, there are one or more Parquet files that contain your table's data. The prefix of the Parquet filename is `part-{{partition_index}}`. If your table is partitioned, there will be multiple files starting with the partition index `00000`.

  There can be gaps in the partition index sequence. This happens because each partition is obtained from a ranged query in your table. If there is no data in the range of that partition, then that sequence number is skipped.

  For example, suppose that the `id` column is the table's primary key, and its minimum and maximum values are `100` and `1000`. When we try to export this table with nine partitions, we read it with parallel queries such as the following:

  ```
  SELECT * FROM table WHERE id <= 100 AND id < 200
  	SELECT * FROM table WHERE id <= 200 AND id < 300
  ```

  This should generate nine files, from `part-00000-{{random_uuid}}.gz.parquet` to `part-00008-{{random_uuid}}.gz.parquet`. However, if there are no rows with IDs between `200` and `350`, one of the completed partitions is empty, and no file is created for it. In the previous example, `part-00001-{{random_uuid}}.gz.parquet` isn't created.
+ Older convention:

  ```
  part-{{partition_index}}-{{random_uuid}}.{{format-based_extension}}
  ```

  This is the same as the current convention, but without the `{{batch_index}}` prefix, for example:

  ```
  part-00000-c5a881bb-58ff-4ee6-1111-b41ecff340a3-c000.gz.parquet
  	part-00001-d7a881cc-88cc-5ab7-2222-c41ecab340a4-c000.gz.parquet
  	part-00002-f5a991ab-59aa-7fa6-3333-d41eccd340a7-c000.gz.parquet
  ```

The file naming convention is subject to change. Therefore, when reading target tables, we recommend that you read everything inside the base prefix for the table.

## Data conversion when exporting to an Amazon S3 bucket
<a name="aurora-export-snapshot.data-types"></a>

When you export a DB snapshot to an Amazon S3 bucket, Amazon Aurora converts data to, exports data in, and stores data in the Parquet format. For more information about Parquet, see the [Apache Parquet](https://parquet.apache.org/docs/) website.

Parquet stores all data as one of the following primitive types:
+ BOOLEAN
+ INT32
+ INT64
+ INT96
+ FLOAT
+ DOUBLE
+ BYTE\_ARRAY – A variable-length byte array, also known as binary
+ FIXED\_LEN\_BYTE\_ARRAY – A fixed-length byte array used when the values have a constant size

The Parquet data types are few to reduce the complexity of reading and writing the format. Parquet provides logical types for extending primitive types. A *logical type* is implemented as an annotation with the data in a `LogicalType` metadata field. The logical type annotation explains how to interpret the primitive type. 

When the `STRING` logical type annotates a `BYTE_ARRAY` type, it indicates that the byte array should be interpreted as a UTF-8 encoded character string. After an export task completes, Amazon Aurora notifies you if any string conversion occurred. The underlying data exported is always the same as the data from the source. However, due to the encoding difference in UTF-8, some characters might appear different from the source when read in tools such as Athena.

For more information, see [Parquet logical type definitions](https://github.com/apache/parquet-format/blob/master/LogicalTypes.md) in the Parquet documentation.

**Topics**
+ [MySQL data type mapping to Parquet](#aurora-export-snapshot.data-types.MySQL)
+ [PostgreSQL data type mapping to Parquet](#aurora-export-snapshot.data-types.PostgreSQL)

### MySQL data type mapping to Parquet
<a name="aurora-export-snapshot.data-types.MySQL"></a>

The following table shows the mapping from MySQL data types to Parquet data types when data is converted and exported to Amazon S3.


<table>
<thead>
  <tr><th>Source data type</th><th>Parquet primitive type</th><th>Logical type annotation</th><th>Conversion notes</th></tr>
</thead>
<tbody>
  <tr><td colspan="4"><b>Numeric data types</b></td></tr>
  <tr><td>BIGINT</td><td>INT64</td><td></td><td> </td></tr>
  <tr><td>BIGINT UNSIGNED</td><td>FIXED_LEN_BYTE_ARRAY(9) </td><td>DECIMAL(20,0)</td><td>Parquet supports only signed types, so the mapping requires an additional byte (8 plus 1) to store the BIGINT_UNSIGNED type.</td></tr>
  <tr><td>BIT</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td rowspan="4">DECIMAL</td><td>INT32</td><td>DECIMAL(p,s)</td><td>If the source value is less than 231, it's stored as INT32. </td></tr>
  <tr><td>INT64</td><td>DECIMAL(p,s)</td><td>If the source value is 231 or greater, but less than 263, it's stored as INT64.</td></tr>
  <tr><td>FIXED_LEN_BYTE_ARRAY(N)</td><td>DECIMAL(p,s)</td><td>If the source value is 263 or greater, it's stored as FIXED_LEN_BYTE_ARRAY(N).</td></tr>
  <tr><td>BYTE_ARRAY</td><td>STRING</td><td>Parquet doesn't support Decimal precision greater than 38. The Decimal value is converted to a string in a BYTE_ARRAY type and encoded as UTF8.</td></tr>
  <tr><td>DOUBLE</td><td>DOUBLE</td><td></td><td> </td></tr>
  <tr><td>FLOAT</td><td>DOUBLE</td><td></td><td> </td></tr>
  <tr><td>INT</td><td>INT32</td><td></td><td> </td></tr>
  <tr><td>INT UNSIGNED</td><td>INT64</td><td></td><td> </td></tr>
  <tr><td>MEDIUMINT</td><td>INT32</td><td></td><td> </td></tr>
  <tr><td>MEDIUMINT UNSIGNED</td><td>INT64</td><td></td><td> </td></tr>
  <tr><td rowspan="4"> NUMERIC</td><td>INT32</td><td>DECIMAL(p,s)</td><td>If the source value is less than 231, it's stored as INT32.</td></tr>
  <tr><td>INT64</td><td>DECIMAL(p,s)</td><td>If the source value is 231 or greater, but less than 263, it's stored as INT64.</td></tr>
  <tr><td>FIXED_LEN_ARRAY(N)</td><td>DECIMAL(p,s)</td><td>If the source value is 263 or greater, it's stored as FIXED_LEN_BYTE_ARRAY(N).</td></tr>
  <tr><td>BYTE_ARRAY</td><td>STRING</td><td>Parquet doesn't support Numeric precision greater than 38. This Numeric value is converted to a string in a BYTE_ARRAY type and encoded as UTF8.</td></tr>
  <tr><td>SMALLINT</td><td>INT32</td><td></td><td> </td></tr>
  <tr><td>SMALLINT UNSIGNED</td><td>INT32</td><td></td><td> </td></tr>
  <tr><td>TINYINT</td><td>INT32</td><td></td><td> </td></tr>
  <tr><td>TINYINT UNSIGNED</td><td>INT32</td><td>INT(16, true)</td><td> </td></tr>
  <tr><td colspan="4"><b>String data types</b></td></tr>
  <tr><td>BINARY</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>BLOB</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>CHAR</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>ENUM</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>LINESTRING</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>LONGBLOB</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>LONGTEXT</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>MEDIUMBLOB</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>MEDIUMTEXT</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>MULTILINESTRING</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>SET</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>TEXT</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>TINYBLOB</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>TINYTEXT</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>VARBINARY</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>VARCHAR</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td colspan="4"><b>Date and time data types</b></td></tr>
  <tr><td>DATE</td><td>BYTE_ARRAY</td><td>STRING</td><td>A date is converted to a string in a BYTE_ARRAY type and encoded as UTF8.</td></tr>
  <tr><td>DATETIME</td><td>INT64 </td><td>TIMESTAMP_MICROS</td><td> </td></tr>
  <tr><td>TIME</td><td>BYTE_ARRAY</td><td>STRING</td><td>A TIME type is converted to a string in a BYTE_ARRAY and encoded as UTF8.</td></tr>
  <tr><td>TIMESTAMP</td><td>INT64 </td><td>TIMESTAMP_MICROS</td><td> </td></tr>
  <tr><td>YEAR</td><td>INT32</td><td></td><td> </td></tr>
  <tr><td colspan="4"><b>Geometric data types</b></td></tr>
  <tr><td>GEOMETRY</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>GEOMETRYCOLLECTION</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>MULTIPOINT</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>MULTIPOLYGON</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>POINT</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td>POLYGON</td><td>BYTE_ARRAY</td><td></td><td> </td></tr>
  <tr><td colspan="4"><b>JSON data type</b></td></tr>
  <tr><td>JSON </td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
</tbody>
</table>


### PostgreSQL data type mapping to Parquet
<a name="aurora-export-snapshot.data-types.PostgreSQL"></a>

The following table shows the mapping from PostgreSQL data types to Parquet data types when data is converted and exported to Amazon S3.


<table>
<thead>
  <tr><th>PostgreSQL data type</th><th>Parquet primitive type</th><th>Logical type annotation</th><th>Mapping notes</th></tr>
</thead>
<tbody>
  <tr><td colspan="4"><b>Numeric data types</b></td></tr>
  <tr><td>BIGINT</td><td>INT64</td><td></td><td> </td></tr>
  <tr><td>BIGSERIAL</td><td>INT64</td><td></td><td> </td></tr>
  <tr><td>DECIMAL</td><td>BYTE_ARRAY</td><td>STRING</td><td>A DECIMAL type is converted to a string in a BYTE_ARRAY type and encoded as UTF8.This conversion is to avoid complications due to data precision and data values that are not a number (NaN).</td></tr>
  <tr><td>DOUBLE PRECISION</td><td>DOUBLE</td><td></td><td> </td></tr>
  <tr><td>INTEGER</td><td>INT32</td><td></td><td> </td></tr>
  <tr><td>MONEY</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>REAL</td><td>FLOAT</td><td></td><td> </td></tr>
  <tr><td>SERIAL</td><td>INT32</td><td></td><td> </td></tr>
  <tr><td>SMALLINT</td><td>INT32</td><td>INT(16, true)</td><td> </td></tr>
  <tr><td>SMALLSERIAL</td><td>INT32</td><td>INT(16, true)</td><td> </td></tr>
  <tr><td colspan="3"><b>String and related data types</b></td><td></td></tr>
  <tr><td>ARRAY</td><td>BYTE_ARRAY</td><td>STRING</td><td>An array is converted to a string and encoded as BINARY (UTF8).<br />This conversion is to avoid complications due to data precision, data values that are not a number (NaN), and time data values.</td></tr>
  <tr><td>BIT</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>BIT VARYING</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>BYTEA</td><td>BINARY</td><td></td><td> </td></tr>
  <tr><td>CHAR</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>CHAR(N)</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>ENUM</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>NAME</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>TEXT</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>TEXT SEARCH</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>VARCHAR(N)</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>XML</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td colspan="4"><b>Date and time data types</b></td></tr>
  <tr><td>DATE</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>INTERVAL</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>TIME</td><td>BYTE_ARRAY</td><td>STRING</td><td></td></tr>
  <tr><td>TIME WITH TIME ZONE</td><td>BYTE_ARRAY</td><td>STRING</td><td></td></tr>
  <tr><td>TIMESTAMP</td><td>BYTE_ARRAY</td><td>STRING</td><td></td></tr>
  <tr><td>TIMESTAMP WITH TIME ZONE</td><td>BYTE_ARRAY</td><td>STRING</td><td></td></tr>
  <tr><td colspan="4"><b>Geometric data types</b></td></tr>
  <tr><td>BOX</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>CIRCLE</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>LINE</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>LINESEGMENT</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>PATH</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>POINT</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>POLYGON</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td colspan="4"><b>JSON data types</b></td></tr>
  <tr><td>JSON</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>JSONB</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td colspan="4"><b>Other data types</b></td></tr>
  <tr><td>BOOLEAN</td><td>BOOLEAN</td><td></td><td> </td></tr>
  <tr><td>CIDR</td><td>BYTE_ARRAY</td><td>STRING</td><td> Network data type</td></tr>
  <tr><td>COMPOSITE</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>DOMAIN</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>INET</td><td>BYTE_ARRAY</td><td>STRING</td><td> Network data type</td></tr>
  <tr><td>MACADDR</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>OBJECT IDENTIFIER</td><td>N/A</td><td></td><td></td></tr>
  <tr><td>PG_LSN</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>RANGE</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
  <tr><td>UUID</td><td>BYTE_ARRAY</td><td>STRING</td><td> </td></tr>
</tbody>
</table>
