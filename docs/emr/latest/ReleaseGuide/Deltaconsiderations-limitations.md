# Considerations and

limitations

- Delta Lake is supported for use with Amazon EMR releases 6.9.0 and higher. You can use
  [Apache Spark](https://aws.amazon.com/emr/features/spark/ "https://aws.amazon.com/emr/features/spark/") 3.x on Amazon EMR clusters with Delta tables.
- We recommend that you use s3 URI scheme for S3 location paths instead of s3a
  for best performance, security and reliability. For more information see [Working with
  storage and file systems](../ManagementGuide/emr-plan-file-systems.md "../ManagementGuide/emr-plan-file-systems.md").
- With Amazon EMR 7.0, Delta Universal Format (UniForm) and
  convert-to-Iceberg statements aren't supported.
- With Amazon EMR 6.9 and 6.10, when you store Delta Lake table data in Amazon S3, column
  data becomes `NULL` after column rename operation. This issue is
  resolved with Amazon EMR 6.11. For more information about the experimental column
  rename operation, see [Column
  rename operation](https://docs.delta.io/latest/delta-batch.html#rename-columns "https://docs.delta.io/latest/delta-batch.html#rename-columns") in the Delta Lake User Guide.
- When using EMR Delta with Glue in the Beijing (cn-north-1) region, set
  `hive.s3.endpoint` to `https://s3.cn-north-1.amazonaws.com.cn`.
- If you create a database in the AWS Glue Data Catalog outside of Apache Spark, the
  database could have an empty `LOCATION` field. Because Spark doesn't
  allow databases to be created with an empty location property, you'll get the
  following error if you use Spark in Amazon EMR to create a Delta table in a Glue
  database and the database has an empty `LOCATION` property:

```
IllegalArgumentException: Can not create a Path from an empty string
```

To resolve this issue, create the database in the Data Catalog with a valid,
non-empty path for the `LOCATION` field. For steps to implement this
solution, see [Illegal argument exception when creating a table](../../../athena/latest/ug/notebooks-spark-known-issues.md#notebooks-spark-known-issues-illegal-argument-exception "../../../athena/latest/ug/notebooks-spark-known-issues.md#notebooks-spark-known-issues-illegal-argument-exception") in the
_Amazon Athena User Guide_.
