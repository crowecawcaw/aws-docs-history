# UNLOAD

Writes query results from a `SELECT` statement to the specified data format.
Supported formats for `UNLOAD` include Apache Parquet, ORC, Apache Avro, and
JSON. CSV is the only output format supported by the Athena `SELECT` command, but
you can use the `UNLOAD` command, which supports a variety of output formats, to
enclose your `SELECT` query and rewrite its output to one of the formats that
`UNLOAD` supports.

Although you can use the `CREATE TABLE AS` (CTAS) statement to output data in
formats other than CSV, CTAS statements require the creation of a table in Athena. The
`UNLOAD` statement is useful when you want to output the results of a
`SELECT` query in a non-CSV format but do not want the associated table. For
example, a downstream application might require the results of a `SELECT` query
to be in JSON format, and Parquet or ORC might provide a performance advantage over CSV if
you intend to use the results of the `SELECT` query for additional
analysis.

## Considerations and

limitations

When you use the `UNLOAD` statement in Athena, keep in mind the following
points:

- No global ordering of files –
  `UNLOAD` results are written to multiple files in parallel. If
  the `SELECT` query in the `UNLOAD` statement specifies a
  sort order, each file's contents are in sorted order, but the files are not
  sorted relative to each other.
- Orphaned data not deleted – In the case
  of a failure, Athena does not attempt to delete orphaned data. This behavior is
  the same as that for CTAS and `INSERT INTO` statements.
- Maximum partitions – The maximum number
  of partitions that can be used with `UNLOAD` is 100.
- Metadata and manifest files – Athena
  generates a metadata file and data manifest file for each `UNLOAD`
  query. The manifest tracks the files that the query wrote. Both files are saved
  to your Athena query result location in Amazon S3. For more information, see [Identify query output
  files](querying-finding-output-files.md#querying-identifying-output-files "querying-finding-output-files.md#querying-identifying-output-files").
- Encryption – `UNLOAD` output
  files are encrypted according to the encryption configuration used for Amazon S3. To
  set up encryption configuration to encrypt your `UNLOAD` result, you
  can use the [EncryptionConfiguration API](../APIReference/API_EncryptionConfiguration.md "../APIReference/API_EncryptionConfiguration.md").
- Prepared statements –
  `UNLOAD` can be used with prepared statements. For information
  about prepared statements in Athena, see [Use parameterized queries](querying-with-prepared-statements.md "querying-with-prepared-statements.md").
- Service quotas – `UNLOAD`
  uses DML query quotas. For quota information, see [Service Quotas](service-limits.md "service-limits.md").
- Expected bucket owner – The expected
  bucket owner setting does not apply to the destination Amazon S3 location specfied in
  the `UNLOAD` query. The expected bucket owner setting applies only to the Amazon S3
  output location that you specify for Athena query results. For more information, see
  [Specify a query result
  location using the Athena console](query-results-specify-location-console.md "query-results-specify-location-console.md").

## Syntax

The `UNLOAD` statement uses the following syntax.

```
UNLOAD (SELECT `col_name`[, ...] FROM `old_table`)
TO 's3://amzn-s3-demo-bucket/`my_folder`/'
WITH ( `property_name` = '`expression`' [, ...] )
```

Except when writing to partitions, the `TO` destination must specify a
location in Amazon S3 that has no data. Before the `UNLOAD` query writes to the
location specified, it verifies that the bucket location is empty. Because
`UNLOAD` does not write data to the specified location if the location
already has data in it, `UNLOAD` does not overwrite existing data. To reuse a
bucket location as a destination for `UNLOAD`, delete the data in the bucket
location, and then run the query again.

Note that when `UNLOAD` writes to partitions, this behavior is different.
If you run the same `UNLOAD` query multiple times that has the same
`SELECT` statement, the same `TO` location and the same
partitions, each `UNLOAD` query unloads the data into Amazon S3 at the location
and partitions specified.

### Parameters

Possible values for `property_name` are as
follows.

**format = '`file_format`'**

Required. Specifies the file format of the output. Possible values for
`file_format` are `ORC`,
`PARQUET`, `AVRO`, `JSON`, or
`TEXTFILE`.

**compression = '`compression_format`'**

Optional. This option is specific to the ORC and Parquet formats. For
ORC, the default is `zlib`, and for Parquet, the default is
`gzip`. For information about supported compression
formats, see [Athena compression
support](compression-formats.md "compression-formats.md").

###### Note

This option does not apply to the `AVRO` format. Athena
uses `gzip` for the `JSON` and
`TEXTFILE` formats.

**compression_level = `compression_level`**

Optional. The compression level to use for ZSTD compression. This
property applies only to ZSTD compression. For more information, see
[Use ZSTD compression levels](compression-support-zstd-levels.md "compression-support-zstd-levels.md").

**field_delimiter = '`delimiter`'**

Optional. Specifies a single-character field delimiter for files in
CSV, TSV, and other text formats. The following example specifies a
comma delimiter.

```
WITH (field_delimiter = ',')
```

Currently, multicharacter field delimiters are not supported. If you
do not specify a field delimiter, the octal character `\001`
(^A) is used.

**partitioned_by = ARRAY[ `col_name`[,...] ]**

Optional. An array list of columns by which the output is
partitioned.

###### Note

In your `SELECT` statement, make sure that the names of
the partitioned columns are last in your list of columns.

## Examples

The following example writes the output of a `SELECT` query to the Amazon S3
location `s3://amzn-s3-demo-bucket/unload_test_1/` using JSON
format.

```
UNLOAD (SELECT * FROM old_table)
TO 's3://amzn-s3-demo-bucket/unload_test_1/'
WITH (format = 'JSON')
```

The following example writes the output of a `SELECT` query in Parquet
format using Snappy compression.

```
UNLOAD (SELECT * FROM old_table)
TO 's3://amzn-s3-demo-bucket/'
WITH (format = 'PARQUET',compression = 'SNAPPY')
```

The following example writes four columns in text format, with the output partitioned
by the last column.

```
UNLOAD (SELECT name1, address1, comment1, key1 FROM table1)
TO 's3://amzn-s3-demo-bucket/ partitioned/'
WITH (format = 'TEXTFILE', partitioned_by = ARRAY['key1'])
```

The following example unloads the query results to the specified location using the
Parquet file format, ZSTD compression, and ZSTD compression level 4.

```
UNLOAD (SELECT * FROM old_table)
TO 's3://amzn-s3-demo-bucket/'
WITH (format = 'PARQUET', compression = 'ZSTD', compression_level = 4)
```

## Additional resources

- [Simplify your ETL and ML pipelines using the Amazon Athena UNLOAD
  feature](https://aws.amazon.com/blogs/big-data/simplify-your-etl-and-ml-pipelines-using-the-amazon-athena-unload-feature/ "https://aws.amazon.com/blogs/big-data/simplify-your-etl-and-ml-pipelines-using-the-amazon-athena-unload-feature/") in the _AWS Big Data Blog_.
