# Considerations and limitations for SQL queries

in Amazon Athena

When running queries in Athena, keep in mind the following considerations and
limitations:

- Stored procedures – Stored procedures are
  not supported.
- Maximum number of partitions – The maximum
  number of partitions you can create with `CREATE TABLE AS SELECT` (CTAS)
  statements is 100. For information, see [CREATE TABLE
  AS](create-table-as.md "create-table-as.md"). For a workaround, see [Use CTAS and INSERT INTO to work around the 100 partition
  limit](ctas-insert-into.md "ctas-insert-into.md").
- Unsupported statements – Unsupported
  statements include the following. For a complete list of unsupported DDL statements
  in Athena, see [Unsupported DDL](unsupported-ddl.md "unsupported-ddl.md").
  - `CREATE TABLE LIKE` is not supported.
  - `DESCRIBE INPUT` and `DESCRIBE OUTPUT` are not
    supported.
  - The `MERGE` statement is supported only for transactional table
    formats. For more information, see [MERGE INTO](merge-into-statement.md "merge-into-statement.md").
  - `UPDATE` statements are not supported.
  - `DELETE FROM` is not supported.

- Trino and Presto connectors – Neither [Trino](https://trino.io/docs/current/connector.html "https://trino.io/docs/current/connector.html") nor [Presto](https://prestodb.io/docs/current/connector.html "https://prestodb.io/docs/current/connector.html") connectors
  are supported. Use Amazon Athena Federated Query to connect data sources. For more information, see
  [Use Amazon Athena Federated Query](federated-queries.md "federated-queries.md").
- Timeouts on tables with many partitions –
  Athena may time out when querying a table that has many thousands of partitions. This
  can happen when the table has many partitions that are not of type
  `string`. When you use type `string`, Athena prunes
  partitions at the metastore level. However, when you use other data types, Athena
  prunes partitions on the server side. The more partitions you have, the longer this
  process takes and the more likely your queries are to time out. To resolve this
  issue, set your partition type to `string` so that Athena prunes
  partitions at the metastore level. This reduces overhead and prevents queries from
  timing out.
- Amazon Glacier support – For information about
  querying restored Amazon Glacier objects, see [Query restored Amazon Glacier objects](querying-glacier.md "querying-glacier.md").
- Files treated as hidden – Athena treats
  source files that start with an underscore (`_`) or a dot
  (`.`) as hidden. To work around this limitation, rename the
  files.
- Row or column size limitation – The size
  of a single row or its columns cannot exceed 32 MB. This limit can be exceeded when,
  for example, a row contains a single column of 35 MB. This is a hard limit of the
  service and cannot be changed.
- Max line length in a text file – The size of
  single line in a text file has an upper limit of 200 MB. Exceeding this limit can
  produce the error message **`TextLineLengthLimitExceededException: Too many
bytes before newline`**. To work around this limitation, make sure that
  you don't have a single line in a text file exceeding 200 MB.
- LIMIT clause maximum – The maximum number of
  rows that can be specified for the `LIMIT` clause is

9223372036854776000. When using `ORDER BY`, the maximum number of
                     supported rows for the LIMIT clause is 2147483647. Exceeding this limit results in
                     the error message **`NOT_SUPPORTED: ORDER BY LIMIT > 2147483647 is not
supported`**.

- information_schema – Querying
  `information_schema` is most performant if you have a small to
  moderate amount of AWS Glue metadata. If you have a large amount of metadata, errors
  can occur. For information about querying the `information_schema`
  database for AWS Glue metadata, see [Query the AWS Glue Data Catalog](querying-glue-catalog.md "querying-glue-catalog.md").
- Array initializations – Due to a limitation in
  Java, it is not possible to initialize an array in Athena that has more than 254
  arguments.
- Hidden metadata columns – The Hive or
  Iceberg hidden metadata columns `$bucket`,
  `$file_modified_time`, `$file_size`, and
  `$partition` are not supported for views. For information about using
  the `$path` metadata column in Athena, see [Getting the file locations for source data in Amazon S3](select.md#select-path "select.md#select-path") .
  For information about maximum query string length, quotas for query timeouts, and quotas
  for the active number of DML queries, see [Service Quotas](service-limits.md "service-limits.md").
