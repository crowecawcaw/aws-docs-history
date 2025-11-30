# Considerations for DB cluster snapshot exports

## Limitations

Exporting DB snapshot data to Amazon S3 has the following limitations:

- You can't run multiple export tasks for the same DB cluster snapshot simultaneously. This applies to both full and
  partial exports.
- You can have up to five concurrent DB snapshot export tasks in progress per AWS account.
- You can't export snapshot data from Aurora Serverless v1 DB clusters to S3.
- Exports to S3 don't support S3 prefixes containing a colon (:).
- The following characters in the S3 file path are converted to underscores (\_) during export:

```
\ ` " (space)
```

- If a database, schema, or table has characters in its name other than the following, partial export isn't
  supported. However, you can export the entire DB snapshot.
  - Latin letters (A–Z)
  - Digits (0–9)
  - Dollar symbol ($)
  - Underscore (\_)

- Spaces ( ) and certain characters aren't supported in database table column names. Tables with the following
  characters in column names are skipped during export:

```
, ; { } ( ) \n \t = (space)
```

- Tables with slashes (/) in their names are skipped during export.
- Aurora PostgreSQL temporary and unlogged tables are skipped during export.
- If the data contains a large object, such as a BLOB or CLOB, that is close to
  or greater than 500 MB, then the export fails.
- If a table contains a large row that is close to or greater than 2 GB, then
  the table is skipped during export.
- For partial exports, the `ExportOnly` list has a maximum size of
  200 KB.
- We strongly recommend that you use a unique name for each export task. If you don't use a unique task name, you might
  receive the following error message:

**`ExportTaskAlreadyExistsFault: An error occurred (ExportTaskAlreadyExists) when calling the StartExportTask
 operation: The export task with the ID `xxxxx` already exists.`**

- You can delete a snapshot while you're exporting its data to S3, but you're still charged for the storage
  costs for that snapshot until the export task has completed.
- You can't restore exported snapshot data from S3 to a new DB cluster.

## File naming convention

Exported data for specific tables is stored in the format ``base_prefix`/`files``, where the base prefix is
the following:

```
`export_identifier`/`database_name`/`schema_name`.`table_name`/
```

For example:

```
export-1234567890123-459/rdststdb/rdststdb.DataInsert_7ADB5D19965123A2/
```

There are two conventions for how files are named.

- Current convention:

```
`batch_index`/part-`partition_index`-`random_uuid`.`format-based_extension`
```

The batch index is a sequence number that represents a batch of data read from the table. If we can't partition your
table into small chunks to be exported in parallel, there will be multiple batch indexes. The same thing happens if your
table is partitioned into multiple tables. There will be multiple batch indexes, one for each of the table partitions of
your main table.

If we can partition your table into small chunks to be read in parallel, there will be only the batch index
`1` folder.

Inside the batch index folder, there are one or more Parquet files that contain your table's data. The prefix of the
Parquet filename is `part-`partition_index``. If your table is partitioned,
 there will be multiple files starting with the partition index `00000`.

There can be gaps in the partition index sequence. This happens because each partition is obtained from a ranged query
in your table. If there is no data in the range of that partition, then that sequence number is skipped.

For example, suppose that the `id` column is the table's primary key, and its minimum and maximum values
are `100` and `1000`. When we try to export this table with nine partitions, we read it with
parallel queries such as the following:

```
SELECT * FROM table WHERE id <= 100 AND id < 200
	SELECT * FROM table WHERE id <= 200 AND id < 300
```

This should generate nine files, from
`part-00000-`random_uuid`.gz.parquet` to
`part-00008-`random_uuid`.gz.parquet`. However, if there are no rows
with IDs between `200` and `350`, one of the completed partitions is empty, and no file is created
for it. In the previous example, `part-00001-`random_uuid`.gz.parquet` isn't
created.

- Older convention:

```
part-`partition_index`-`random_uuid`.`format-based_extension`
```

This is the same as the current convention, but without the `batch_index`
prefix, for example:

```
part-00000-c5a881bb-58ff-4ee6-1111-b41ecff340a3-c000.gz.parquet
	part-00001-d7a881cc-88cc-5ab7-2222-c41ecab340a4-c000.gz.parquet
	part-00002-f5a991ab-59aa-7fa6-3333-d41eccd340a7-c000.gz.parquet

```

The file naming convention is subject to change. Therefore, when reading target
tables, we recommend that you read everything inside the base prefix for the
table.

## Data conversion when exporting to an Amazon S3

bucket

When you export a DB snapshot to an Amazon S3 bucket, Amazon Aurora converts data to,
exports data in, and stores data in the Parquet format. For more information about
Parquet, see the [Apache
Parquet](https://parquet.apache.org/docs/ "https://parquet.apache.org/docs/") website.

Parquet stores all data as one of the following primitive types:

- BOOLEAN
- INT32
- INT64
- INT96
- FLOAT
- DOUBLE
- BYTE_ARRAY – A variable-length byte array, also known as binary
- FIXED_LEN_BYTE_ARRAY – A fixed-length byte array used when the values have a
  constant size

The Parquet data types are few to reduce the complexity of reading and writing the format.
Parquet provides logical types for extending primitive types. A _logical type_ is implemented as an annotation with the data in a
`LogicalType` metadata field. The logical type annotation explains how to
interpret the primitive type.

When the `STRING` logical type annotates a `BYTE_ARRAY` type, it
indicates that the byte array should be interpreted as a UTF-8 encoded character string.
After an export task completes, Amazon Aurora notifies you if any string conversion occurred.
The underlying data exported is always the same as the data from the source. However,
due to the encoding difference in UTF-8, some characters might appear different from the
source when read in tools such as Athena.

For more information, see [Parquet
logical type definitions](https://github.com/apache/parquet-format/blob/master/LogicalTypes.md "https://github.com/apache/parquet-format/blob/master/LogicalTypes.md") in the Parquet documentation.

###### Topics

- [MySQL data type mapping to Parquet](#aurora-export-snapshot.data-types.MySQL "#aurora-export-snapshot.data-types.MySQL")
- [PostgreSQL data type mapping to Parquet](#aurora-export-snapshot.data-types.PostgreSQL "#aurora-export-snapshot.data-types.PostgreSQL")

### MySQL data type mapping to Parquet

The following table shows the mapping from MySQL data types to Parquet data types when data is converted and
exported to Amazon S3.

| Source data type             | Parquet primitive type  | Logical type annotation                                                                                                                                | Conversion notes                                                                                                                   |
| ---------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Numeric data types**       |
| BIGINT                       | INT64                   |                                                                                                                                                        |                                                                                                                                    |
| BIGINT UNSIGNED              | FIXED_LEN_BYTE_ARRAY(9) | DECIMAL(20,0)                                                                                                                                          | Parquet supports only signed types, so the mapping requires an<br>additional byte (8 plus 1) to store the BIGINT_UNSIGNED<br>type. |
| BIT                          | BYTE_ARRAY              |                                                                                                                                                        |                                                                                                                                    |
| DECIMAL                      | INT32                   | DECIMAL(p,s)                                                                                                                                           | If the source value is less than 231,<br>it's stored as INT32.                                                                     |
| INT64                        | DECIMAL(p,s)            | If the source value is 231 or greater,<br>but less than 263, it's stored as<br>INT64.                                                                  |
| FIXED_LEN_BYTE_ARRAY(N)      | DECIMAL(p,s)            | If the source value is 263 or greater,<br>it's stored as FIXED_LEN_BYTE_ARRAY(N).                                                                      |
| BYTE_ARRAY                   | STRING                  | Parquet doesn't support Decimal precision greater than 38.<br>The Decimal value is converted to a string in a BYTE_ARRAY type and<br>encoded as UTF8.  |
| DOUBLE                       | DOUBLE                  |                                                                                                                                                        |                                                                                                                                    |
| FLOAT                        | DOUBLE                  |                                                                                                                                                        |                                                                                                                                    |
| INT                          | INT32                   |                                                                                                                                                        |                                                                                                                                    |
| INT UNSIGNED                 | INT64                   |                                                                                                                                                        |                                                                                                                                    |
| MEDIUMINT                    | INT32                   |                                                                                                                                                        |                                                                                                                                    |
| MEDIUMINT UNSIGNED           | INT64                   |                                                                                                                                                        |                                                                                                                                    |
| NUMERIC                      | INT32                   | DECIMAL(p,s)                                                                                                                                           | If the source value is less than<br>231, it's stored as<br>INT32.                                                                  |
| INT64                        | DECIMAL(p,s)            | If the source value is 231 or greater,<br>but less than 263, it's stored as<br>INT64.                                                                  |
| FIXED_LEN_ARRAY(N)           | DECIMAL(p,s)            | If the source value is 263 or greater,<br>it's stored as FIXED_LEN_BYTE_ARRAY(N).                                                                      |
| BYTE_ARRAY                   | STRING                  | Parquet doesn't support Numeric precision greater than 38. This<br>Numeric value is converted to a string in a BYTE_ARRAY type and<br>encoded as UTF8. |
| SMALLINT                     | INT32                   |                                                                                                                                                        |                                                                                                                                    |
| SMALLINT UNSIGNED            | INT32                   |                                                                                                                                                        |                                                                                                                                    |
| TINYINT                      | INT32                   |                                                                                                                                                        |                                                                                                                                    |
| TINYINT UNSIGNED             | INT32                   | INT(16, true)                                                                                                                                          |                                                                                                                                    |
| **String data types**        |
| BINARY                       | BYTE_ARRAY              |                                                                                                                                                        |                                                                                                                                    |
| BLOB                         | BYTE_ARRAY              |                                                                                                                                                        |                                                                                                                                    |
| CHAR                         | BYTE_ARRAY              |                                                                                                                                                        |                                                                                                                                    |
| ENUM                         | BYTE_ARRAY              | STRING                                                                                                                                                 |                                                                                                                                    |
| LINESTRING                   | BYTE_ARRAY              |                                                                                                                                                        |                                                                                                                                    |
| LONGBLOB                     | BYTE_ARRAY              |                                                                                                                                                        |                                                                                                                                    |
| LONGTEXT                     | BYTE_ARRAY              | STRING                                                                                                                                                 |                                                                                                                                    |
| MEDIUMBLOB                   | BYTE_ARRAY              |                                                                                                                                                        |                                                                                                                                    |
| MEDIUMTEXT                   | BYTE_ARRAY              | STRING                                                                                                                                                 |                                                                                                                                    |
| MULTILINESTRING              | BYTE_ARRAY              |                                                                                                                                                        |                                                                                                                                    |
| SET                          | BYTE_ARRAY              | STRING                                                                                                                                                 |                                                                                                                                    |
| TEXT                         | BYTE_ARRAY              | STRING                                                                                                                                                 |                                                                                                                                    |
| TINYBLOB                     | BYTE_ARRAY              |                                                                                                                                                        |                                                                                                                                    |
| TINYTEXT                     | BYTE_ARRAY              | STRING                                                                                                                                                 |                                                                                                                                    |
| VARBINARY                    | BYTE_ARRAY              |                                                                                                                                                        |                                                                                                                                    |
| VARCHAR                      | BYTE_ARRAY              | STRING                                                                                                                                                 |                                                                                                                                    |
| **Date and time data types** |
| DATE                         | BYTE_ARRAY              | STRING                                                                                                                                                 | A date is converted to a string in a BYTE_ARRAY type and encoded<br>as UTF8.                                                       |
| DATETIME                     | INT64                   | TIMESTAMP_MICROS                                                                                                                                       |                                                                                                                                    |
| TIME                         | BYTE_ARRAY              | STRING                                                                                                                                                 | A TIME type is converted to a string in a BYTE_ARRAY and encoded<br>as UTF8.                                                       |
| TIMESTAMP                    | INT64                   | TIMESTAMP_MICROS                                                                                                                                       |                                                                                                                                    |
| YEAR                         | INT32                   |                                                                                                                                                        |                                                                                                                                    |
| **Geometric data types**     |
| GEOMETRY                     | BYTE_ARRAY              |                                                                                                                                                        |                                                                                                                                    |
| GEOMETRYCOLLECTION           | BYTE_ARRAY              |                                                                                                                                                        |                                                                                                                                    |
| MULTIPOINT                   | BYTE_ARRAY              |                                                                                                                                                        |                                                                                                                                    |
| MULTIPOLYGON                 | BYTE_ARRAY              |                                                                                                                                                        |                                                                                                                                    |
| POINT                        | BYTE_ARRAY              |                                                                                                                                                        |                                                                                                                                    |
| POLYGON                      | BYTE_ARRAY              |                                                                                                                                                        |                                                                                                                                    |
| **JSON data type**           |
| JSON                         | BYTE_ARRAY              | STRING                                                                                                                                                 |                                                                                                                                    |

###

PostgreSQL data type mapping to Parquet

The following table shows the mapping from PostgreSQL data types to Parquet data types when
data is converted and exported to Amazon S3.

| PostgreSQL data type              | Parquet primitive type | Logical type annotation | Mapping notes                                                                                                                                                                                               |
| --------------------------------- | ---------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Numeric data types**            |
| BIGINT                            | INT64                  |                         |                                                                                                                                                                                                             |
| BIGSERIAL                         | INT64                  |                         |                                                                                                                                                                                                             |
| DECIMAL                           | BYTE_ARRAY             | STRING                  | A DECIMAL type is converted to a string in a BYTE_ARRAY type and<br>encoded as UTF8.This conversion is to avoid complications due<br>to data precision and data values that are not a number<br>(NaN).      |
| DOUBLE PRECISION                  | DOUBLE                 |                         |                                                                                                                                                                                                             |
| INTEGER                           | INT32                  |                         |                                                                                                                                                                                                             |
| MONEY                             | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| REAL                              | FLOAT                  |                         |                                                                                                                                                                                                             |
| SERIAL                            | INT32                  |                         |                                                                                                                                                                                                             |
| SMALLINT                          | INT32                  | INT(16, true)           |                                                                                                                                                                                                             |
| SMALLSERIAL                       | INT32                  | INT(16, true)           |                                                                                                                                                                                                             |
| **String and related data types** |
| ARRAY                             | BYTE_ARRAY             | STRING                  | An array is converted to a string and encoded as BINARY<br>(UTF8).<br>This conversion is to avoid complications due to data<br>precision, data values that are not a number (NaN), and time<br>data values. |
| BIT                               | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| BIT VARYING                       | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| BYTEA                             | BINARY                 |                         |                                                                                                                                                                                                             |
| CHAR                              | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| CHAR(N)                           | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| ENUM                              | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| NAME                              | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| TEXT                              | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| TEXT SEARCH                       | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| VARCHAR(N)                        | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| XML                               | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| **Date and time data types**      |
| DATE                              | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| INTERVAL                          | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| TIME                              | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| TIME WITH TIME ZONE               | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| TIMESTAMP                         | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| TIMESTAMP WITH TIME ZONE          | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| **Geometric data types**          |
| BOX                               | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| CIRCLE                            | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| LINE                              | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| LINESEGMENT                       | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| PATH                              | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| POINT                             | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| POLYGON                           | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| **JSON data types**               |
| JSON                              | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| JSONB                             | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| **Other data types**              |
| BOOLEAN                           | BOOLEAN                |                         |                                                                                                                                                                                                             |
| CIDR                              | BYTE_ARRAY             | STRING                  | Network data type                                                                                                                                                                                           |
| COMPOSITE                         | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| DOMAIN                            | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| INET                              | BYTE_ARRAY             | STRING                  | Network data type                                                                                                                                                                                           |
| MACADDR                           | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| OBJECT IDENTIFIER                 | N/A                    |                         |                                                                                                                                                                                                             |
| PG_LSN                            | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| RANGE                             | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
| UUID                              | BYTE_ARRAY             | STRING                  |                                                                                                                                                                                                             |
