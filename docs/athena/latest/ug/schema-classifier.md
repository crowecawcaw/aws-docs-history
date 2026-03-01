# Create tables for ETL jobs

You can use Athena to create tables that AWS Glue can use for ETL jobs. AWS Glue jobs perform ETL
operations. An AWS Glue job runs a script that extracts data from sources, transforms the
data, and loads it into targets. For more information, see [Authoring Jobs in AWS Glue](../../../glue/latest/dg/author-job-glue.md "../../../glue/latest/dg/author-job-glue.md") in the
_AWS Glue Developer Guide_.

## Creating Athena tables for AWS Glue ETL jobs

Tables that you create in Athena must have a table property added to them called a
`classification`, which identifies the format of the data. This allows
AWS Glue to use the tables for ETL jobs. The classification values can be
`avro`, `csv`, `json`, `orc`,
`parquet`, or `xml`. An example `CREATE TABLE`
statement in Athena follows:

```
CREATE EXTERNAL TABLE sampleTable (
  column1 INT,
  column2 INT
  ) STORED AS PARQUET
  TBLPROPERTIES (
  'classification'='parquet')
```

If the `classification` table property was not added when the table was
created, you can add it using the AWS Glue console.

###### To add the classification table property using the AWS Glue console

1. Sign in to the AWS Management Console and open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. In the console navigation pane, choose **Tables**.
3. Choose the link for the table that you want to edit, and then choose
   **Actions**, **Edit table**.
4. Scroll down to the **Table properties** section.
5. Choose **Add**.
6. For **Key**, enter `classification`.
7. For **Value**, enter a data type (for example,
   `json`).
8. Choose **Save**.

In the **Table details** section, the data type that you entered
appears in the **Classification** field for the table.
For more information, see [Working with tables](../../../glue/latest/dg/console-tables.md "../../../glue/latest/dg/console-tables.md") in the _AWS Glue Developer Guide_.

## Use ETL jobs to optimize query performance

AWS Glue jobs can help you transform data to a format that optimizes query
performance in Athena. Data formats have a large impact on query performance and query
costs in Athena.

AWS Glue supports writing to the Parquet and ORC data formats. You can use this
feature to transform your data for use in Athena. For more information about using
Parquet and ORC, and other ways to improve performance in Athena, see [Top 10 performance tuning tips for Amazon Athena](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/ "https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/").

###### Note

To reduce the likelihood that Athena is unable to read the `SMALLINT`
and `TINYINT` data types produced by an AWS Glue ETL job, convert
`SMALLINT` and `TINYINT` to `INT` when you
create an ETL job that converts data to ORC.

## Automate AWS Glue jobs for ETL

You can configure AWS Glue ETL jobs to run automatically based on triggers. This
feature is ideal when data from outside AWS is being pushed to an Amazon S3 bucket in an
otherwise suboptimal format for querying in Athena. For more information, see [Triggering AWS Glue jobs](../../../glue/latest/dg/trigger-job.md "../../../glue/latest/dg/trigger-job.md")
in the _AWS Glue Developer Guide_.
