

# Data type mappings for table migration
<a name="s3-tables-migrate-data-type-mappings"></a>

## What migration transforms
<a name="s3-tables-migrate-transforms"></a>

A migration job applies the following transformations as it copies your data. It doesn't change your source table or its objects.


| Transformation | What the migration job does | 
| --- | --- | 
| Data types | Converts each source column data type to an Iceberg-compatible data type. | 
| Column matching | Matches source columns to destination columns by name, ignoring case, at every nesting level. If two source columns match the same destination column, the migration fails during planning. | 
| Partitioning | Represents your Hive partitions as an Iceberg partition spec that uses identity transforms. The migration job writes the partition values into each data file. | 
| File format and compression | Writes Apache Parquet files and recompresses your data. | 
| File size and layout | Combines small files and splits large ones toward a target file size. | 

## Iceberg version support
<a name="s3-tables-migrate-format-v3"></a>

Migration creates Iceberg format version 2 tables by default. Of the data types that Iceberg version 3 adds, migration supports nanosecond timestamps (`timestamp_ns` and `timestamptz_ns`). Choose version 3 if your source has nanosecond timestamps and every engine that reads the table supports version 3.

## How column data types change
<a name="s3-tables-migrate-type-changes"></a>

Migration identifies the level of fidelity with which it can convert data from the source schema and destination schema. Migration classifies the transformations of columns and values as follows.
+ **Lossless** – The data type stays the same and every value is represented exactly.
+ **Widened** – The column moves to a larger data type of the same kind, and every value is represented exactly. For example, `int` becomes `long`.
+ **Converted** – The column moves to a different data type that keeps every value, but some information about the data type is lost. For example, a `tinyint` column becomes `decimal(5,2)`, which keeps every value but loses the information that the column only ever held whole numbers.
+ **Incompatible** – The destination data type can't hold every value of the source type. For example, `bigint` becomes `int`. Your `incompatibleValuesPolicy` determines whether the migration job fails or the column is written as null.
+ **Unsupported** – The source data type has no equivalent Iceberg data type, or migration doesn't support the requested data type conversion. The migration fails under every migration policy. Migration checks data types during planning, using the AWS Glue table and a sample data file. To migrate the table, leave the column out of your destination schema and set `unmatchedSourceFieldsPolicy` to `drop`. You can't leave out a partition column.

The table compatibility report lists each column's data type change. For more information on the table compatibility report, see [Migration reports and statistics](s3-tables-migrate-reports.md).

## Data type mapping for an inferred schema
<a name="s3-tables-migrate-inferred-schema"></a>

If you don't specify a destination schema, migration infers one from the AWS Glue table definition, and every column is optional. The following table shows the Iceberg data type for each AWS Glue data type.


| AWS Glue data type | Iceberg data type | Data type change | 
| --- | --- | --- | 
| boolean | boolean | Lossless | 
| tinyint, smallint | int | Widened | 
| int | int | Lossless | 
| bigint | long | Lossless | 
| float | float | Lossless | 
| double | double | Lossless | 
| decimal(p,s) | decimal(p,s) | Lossless | 
| string | string | Lossless | 
| varchar(n) | string | Widened (the length limit isn't preserved) | 
| char(n) | string | Converted (the length limit and trailing-space padding aren't kept) | 
| binary | binary | Lossless | 
| date | date | Lossless | 
| timestamp | timestamp or timestamptz, based on the sample object | Lossless for microseconds. Widened for milliseconds. Converted for INT96. See [Timestamps](#s3-tables-migrate-timestamps). | 
| timestamp with local time zone | timestamptz | Lossless | 
| array<T>, map<K,V>, struct | list<T>, map<K,V>, struct | Each nested field is classified on its own. | 
| uniontype, void, interval\_year\_month, interval\_day\_time, decimal with precision above 38 | None | Unsupported | 

## Data type changes in a destination schema
<a name="s3-tables-migrate-requested-type-changes"></a>

If you specify a destination schema, you can request the data type changes in the following table. Changes that narrow a data type (for example, `bigint` to `int`), parse text (for example, `string` to a number), or drop part of a date or timestamp are incompatible and follow your `incompatibleValuesPolicy`. Other changes aren't supported. The same rules apply when a source object stores a different data type than its AWS Glue column.


| Source data type | Destination data type | Result | 
| --- | --- | --- | 
| int | long | Widened | 
| float | double | Widened | 
| decimal | A wider decimal | Widened | 
| int | double | Converted | 
| tinyint, smallint | float, double | Converted | 
| An integer type | A decimal that holds every digit | Converted | 
| decimal(p,0) | int, long, float, double | Converted, if the digits fit (9 for int, 18 for long, 7 for float, 15 for double) | 
| string | binary | Converted | 
| A number, boolean, or date | string | Converted | 

## Timestamps
<a name="s3-tables-migrate-timestamps"></a>

An AWS Glue `timestamp` column can store a local date and time (Iceberg `timestamp`) or an instant in UTC (Iceberg `timestamptz`). The migration job reads a sample object to choose the data type, as the following table shows.


| How the sample object stores the column | Iceberg data type | Example writers | 
| --- | --- | --- | 
| Parquet TIMESTAMP adjusted to UTC (isAdjustedToUTC is true), or the older TIMESTAMP\_MILLIS or TIMESTAMP\_MICROS type | timestamptz | Apache Spark with spark.sql.parquet.outputTimestampType set to TIMESTAMP\_MICROS or TIMESTAMP\_MILLIS | 
| Parquet TIMESTAMP not adjusted to UTC (isAdjustedToUTC is false) | timestamp | Apache Spark TIMESTAMP\_NTZ columns | 
| INT96 | timestamptz | Apache Hive, and Apache Spark by default | 
| The sample object doesn't contain the column (for example, the column was added after the migration job sampled it) | timestamp | None | 

You can't change a column data type between `timestamp` and `timestamptz`, except for a column stored as INT96. If a later source object stores the column differently, that object fails. Migration widens millisecond timestamps to microseconds and drops the digits below a microsecond in INT96 timestamps. Nanosecond timestamps require Iceberg format version 3.

## Nested data types
<a name="s3-tables-migrate-nested-types"></a>

Migration maps `struct`, `array`, and `map` types to Iceberg `struct`, `list`, and `map` types, and classifies each nested field on its own.