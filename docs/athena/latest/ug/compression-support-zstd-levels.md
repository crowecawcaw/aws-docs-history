# Use ZSTD compression levels

The [Zstandard real-time data compression
algorithm](http://facebook.github.io/zstd/ "http://facebook.github.io/zstd/") is a fast compression algorithm that provides high compression ratios.
The Zstandard (ZSTD) library is open source software and uses a BSD license. Athena supports
reading and writing ZSTD compressed ORC, Parquet, and text file data.

You can use ZSTD compression levels to adjust the compression ratio and speed according to
your requirements. The ZSTD library supports compression levels from 1 to 22. Athena uses
ZSTD compression level 3 by default.

Compression levels provide granular trade-offs between compression speed and the amount of
compression achieved. Lower compression levels provide faster speed but larger file sizes.
For example, you can use level 1 if speed is most important and level 22 if size is most
important. Level 3 is suitable for many use cases and is the default. Use levels greater
than 19 with caution as they require more memory. The ZSTD library also offers negative
compression levels that extend the range of compression speed and ratios. For more
information, see the [Zstandard
Compression RFC](https://datatracker.ietf.org/doc/html/rfc8478 "https://datatracker.ietf.org/doc/html/rfc8478").

The abundance of compression levels offers substantial opportunities for fine tuning.
However, make sure that you measure your data and consider the tradeoffs when deciding on a
compression level. We recommend using the default level of 3 or a level in the range from 6
to 9 for a reasonable tradeoff between compression speed and compressed data size. Reserve
levels 20 and greater for cases where size is most important and compression speed is not a
concern.

## Considerations and limitations

When using ZSTD compression level in Athena, consider the following points.

- The ZSTD `compression_level` property is supported only in
  Athena engine version 3.
- The ZSTD `compression_level` property is supported for the
  `ALTER TABLE`, `CREATE TABLE`, `CREATE TABLE
AS` (CTAS), and `UNLOAD` statements.
- The `compression_level` property is optional.
- The `compression_level` property is supported only for ZSTD
  compression.
- Possible compression levels are 1 through 22.
- The default compression level is 3.

For information about Apache Hive ZSTD compression support in Athena, see [Use Hive table compression](compression-support-hive.md "compression-support-hive.md"). For
information about Apache Iceberg ZSTD compression support in Athena, see [Use Iceberg table compression](compression-support-iceberg.md "compression-support-iceberg.md").

## Specify ZSTD compression levels

To specify the ZSTD compression level for the `ALTER TABLE`, `CREATE
 TABLE`, `CREATE TABLE AS`, and `UNLOAD` statements, use
the `compression_level` property. To specify ZSTD compression itself, you
must use the individual compression property that the syntax for the statement
uses.

In the [ALTER TABLE SET TBLPROPERTIES](alter-table-set-tblproperties.md "alter-table-set-tblproperties.md") statement `SET
 TBLPROPERTIES` clause, specify ZSTD compression using
`'write.compression' = ' ZSTD'` or `'parquet.compression' =
 'ZSTD'`. Then use the `compression_level` property to specify a
value from 1 to 22 (for example, '`compression_level' = '5'`). If you do
not specify a compression level property, the compression level defaults to 3.

#### Example

The following example modifies the table `existing_table` to use
Parquet file format with ZSTD compression and ZSTD compression level 4. Note
that in the `TBLPROPERTIES` clause the compression level value must
be entered as a string rather an integer and therefore must be enclosed in
either single or double quotes.

```
ALTER TABLE existing_table
SET TBLPROPERTIES ('parquet.compression' = 'ZSTD', 'compression_level' = '4')
```

In the [CREATE TABLE](create-table.md "create-table.md") statement
`TBLPROPERTIES` clause, specify '`write.compression' =
 'ZSTD'` or `'parquet.compression' = 'ZSTD'`, and then use
`compression_level = `compression_level`` and specify a value from 1 to 22 as a string. If the`compression_level`
property is not specified, the default compression level is 3.

#### Example

The following example creates a table in Parquet file format using ZSTD
compression and ZSTD compression level 4.

```
CREATE EXTERNAL TABLE new_table (
  `col0` string COMMENT '',
  `col1` string COMMENT ''
)
STORED AS PARQUET
LOCATION 's3://amzn-s3-demo-bucket/'
TBLPROPERTIES ('write.compression' = 'ZSTD', 'compression_level' = '4')
```

In the [CREATE TABLE AS](create-table-as.md "create-table-as.md") statement
`WITH` clause, specify `write_compression = 'ZSTD'`, or
`parquet_compression = 'ZSTD'`, and then use `compression_level
 = `compression_level``and specify a value from 1
 to 22 as an integer. If the`compression_level` property is not
specified, the default compression level is 3.

#### Example

The following CTAS example specifies Parquet as the file format using ZSTD
compression with compression level 4. Note that, in the `WITH`
clause, the value for compression level must be specified as an integer, not as
a string.

```
CREATE TABLE new_table
WITH ( format = 'PARQUET', write_compression = 'ZSTD', compression_level = 4)
AS SELECT * FROM old_table
```

In the [UNLOAD](unload.md "unload.md") statement `WITH`
clause, specify `compression = 'ZSTD'`, and then use
`compression_level = `compression_level``  and specify a value from 1 to 22 as an integer. If the
 `compression_level` property is not specified, the default
compression level is 3.

#### Example

The following example unloads the query results to the specified location
using the Parquet file format, ZSTD compression, and ZSTD compression level 4.

```
UNLOAD (SELECT * FROM old_table)
TO 's3://amzn-s3-demo-bucket/'
WITH (format = 'PARQUET', compression = 'ZSTD', compression_level = 4)
```
