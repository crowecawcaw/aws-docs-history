# Troubleshooting AWS Clean Rooms

This section describes some common issues that might arise when using AWS Clean Rooms and how to fix them.

###### Issues

- [One or more tables referenced by the query is not accessible by its associated service role. The table/role owner must grant the service role access to the table.](#table-not-accessible "#table-not-accessible")
- [One of the underlying datasets has an unsupported file format.](#dataset-has-unsupported-file-format "#dataset-has-unsupported-file-format")
- [Query results are not as expected when
  using Cryptographic Computing for Clean Rooms.](#troubleshoot-query-results-c3r "#troubleshoot-query-results-c3r")
- [AWS Clean Rooms Spark SQL: Missing
  partition data](#troubleshoot-missing-partition-data "#troubleshoot-missing-partition-data")

## One or more tables referenced by the query is not accessible by its associated service role. The table/role owner must grant the service role access to the table.

- Verify that the permissions for the service role are set up as required. For
  more information, see [Setting up AWS Clean Rooms](setting-up.md "setting-up.md"). ​
  ​

## One of the underlying datasets has an unsupported file format.

- Ensure that your dataset is in one of the supported file formats:

      + Parquet
      + RCFile
      + TextFile
      + SequenceFile
      + RegexSerde
      + OpenCSV
      + AVRO
      + JSON

  For more information, see [Data formats for AWS Clean Rooms](data-formats.md "data-formats.md").

## Query results are not as expected when

using Cryptographic Computing for Clean Rooms.

If you are using Cryptographic Computing for Clean Rooms (C3R), verify that your query uses encrypted
columns correctly:

- The sealed columns are only used in SELECT
  clauses.
- The fingerprint columns are only used in JOIN
  clauses (and GROUP BY clauses under certain conditions).
- That you are only JOINing
  fingerprint columns with the same name if the collaboration
  settings require it.

For more information, see [Cryptographic Computing for Clean Rooms](crypto-computing.md "crypto-computing.md") and [Column types in Cryptographic Computing for Clean Rooms](crypto-computing-column-types.md "crypto-computing-column-types.md").

## AWS Clean Rooms Spark SQL: Missing

partition data

All
partitions in the AWS Glue Data Catalog must also have data in S3. The engine uses the Spark
setting `spark.sql.files.ignoreMissingFiles=False`

For more information, see [https://spark.apache.org/docs/latest/sql-data-sources-generic-options.html#ignore-missing-files](https://spark.apache.org/docs/latest/sql-data-sources-generic-options.html#ignore-missing-files "https://spark.apache.org/docs/latest/sql-data-sources-generic-options.html#ignore-missing-files") .

If you encounter this error you will get the following error message: `"Missing
 partition data: One of the configured tables is partitioned and one or more of the
 partitions does not have data".`

Compare your data present in Amazon S3 with the partitions listed in the AWS Glue Data Catalog for
the table. Delete partitions that don't have corresponding data in S3.
