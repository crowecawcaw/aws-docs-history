# Get started with Delta Lake tables

To be queryable, your Delta Lake table must exist in AWS Glue. If your table is in Amazon S3
but not in AWS Glue, run a `CREATE EXTERNAL TABLE` statement using the following
syntax. If your table already exists in AWS Glue (for example, because you are using Apache
Spark or another engine with AWS Glue), you can skip this step. Note the omission of column
definitions, SerDe library, and other table properties. Unlike traditional Hive tables,
Delta Lake table metadata are inferred from the Delta Lake transaction log and
synchronized directly to AWS Glue.

```
CREATE EXTERNAL TABLE
  [`db_name`.]`table_name`
  LOCATION 's3://amzn-s3-demo-bucket/`your-folder`/'
  TBLPROPERTIES ('table_type' = 'DELTA')
```

###### Note

- This statement is not compatible with S3 buckets that have requester pays enabled. If you want
  to create a Delta Lake table against an S3 bucket with requester pays
  enabled, follow the instructions and DDL statement in [Synchronize Delta Lake metadata](delta-lake-tables-syncing-metadata.md "delta-lake-tables-syncing-metadata.md").
- For Delta Lake tables, `CREATE TABLE` statements that
  include more than the `LOCATION` and `table_type`
  property are not allowed.
