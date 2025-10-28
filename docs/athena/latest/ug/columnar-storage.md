# Use columnar storage formats

[Apache Parquet](https://parquet.apache.org "https://parquet.apache.org") and [ORC](https://orc.apache.org/ "https://orc.apache.org/") are columnar storage formats that are
optimized for fast retrieval of data and used in AWS analytical applications.

Columnar storage formats have the following characteristics that make them suitable for
using with Athena:

- _Compression by column, with compression algorithm selected for the
  column data type_ to save storage space in Amazon S3 and reduce disk space
  and I/O during query processing.
- _Predicate pushdown_ in Parquet and ORC enables Athena queries
  to fetch only the blocks it needs, improving query performance. When an Athena query
  obtains specific column values from your data, it uses statistics from data block
  predicates, such as max/min values, to determine whether to read or skip the block.
- _Splitting of data_ in Parquet and ORC allows Athena to split
  the reading of data to multiple readers and increase parallelism during its query
  processing.
  To convert your existing raw data from other storage formats to Parquet or ORC, you can
  run [CREATE TABLE AS SELECT (CTAS)](ctas.md "ctas.md") queries in Athena and specify a
  data storage format as Parquet or ORC, or use the AWS Glue Crawler.

## Choose between Parquet and ORC

The choice between ORC (Optimized Row Columnar) and Parquet depends on your specific
usage requirements.

Apache Parquet provides efficient data compression and encoding schemes and is ideal
for running complex queries and processing large amounts of data. Parquet is optimized
for use with [Apache Arrow](https://arrow.apache.org/ "https://arrow.apache.org/"), which can be
advantageous if you use tools that are Arrow related.

ORC provides an efficient way to store Hive data. ORC files are often smaller than
Parquet files, and ORC indexes can make querying faster. In addition, ORC supports
complex types such as structs, maps, and lists.

When choosing between Parquet and ORC, consider the following:

Query performance – Because Parquet supports a
wider range of query types, Parquet might be a better choice if you plan to perform
complex queries.

Complex data types – If you are using complex
data types, ORC might be a better choice as it supports a wider range of complex data
types.

File size – If disk space is a concern, ORC
usually results in smaller files, which can reduce storage costs.

Compression – Both Parquet and ORC provide good
compression, but the best format for you can depend on your specific use case.

Evolution – Both Parquet and ORC support schema
evolution, which means you can add, remove, or modify columns over time.

Both Parquet and ORC are good choices for big data applications, but consider the
requirements of your scenario before choosing. You might want to perform benchmarks on
your data and queries to see which format performs better for your use case.

## Convert to columnar formats

Options for easily converting source data such as JSON or CSV into a columnar format
include using [CREATE TABLE AS](ctas.md "ctas.md") queries
or running jobs in AWS Glue.

- You can use `CREATE TABLE AS` (CTAS) queries to convert data into
  Parquet or ORC in one step. For an example, see [Example:
  Writing query results to a different format](ctas-examples.md#ctas-example-format "ctas-examples.md#ctas-example-format") on the [Examples of CTAS queries](ctas-examples.md "ctas-examples.md") page.
- For information about using Athena for ETL to transform data from CSV to
  Parquet, see [Use CTAS and INSERT INTO for ETL and data
  analysis](ctas-insert-into-etl.md "ctas-insert-into-etl.md").
- For information about running an AWS Glue job to transform CSV data to Parquet,
  see the section "Transform the data from CSV to Parquet format" in the AWS Big
  Data blog post [Build a data lake foundation with AWS Glue and Amazon S3](https://aws.amazon.com/blogs/big-data/build-a-data-lake-foundation-with-aws-glue-and-amazon-s3/ "https://aws.amazon.com/blogs/big-data/build-a-data-lake-foundation-with-aws-glue-and-amazon-s3/"). AWS Glue supports
  using the same technique to convert CSV data to ORC, or JSON data to either
  Parquet or ORC.
