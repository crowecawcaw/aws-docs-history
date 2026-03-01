# Synchronize Delta Lake metadata

Athena synchronizes table metadata, including schema, partition columns, and table
properties, to AWS Glue if you use Athena to create your Delta Lake table. As time passes,
this metadata can lose its synchronization with the underlying table metadata in the
transaction log. To keep your table up to date, you can choose one of the following
options:

- Use the AWS Glue crawler for Delta Lake tables. For more information, see [Introducing native Delta Lake table support with AWS Glue crawlers](https://aws.amazon.com/blogs/big-data/introducing-native-delta-lake-table-support-with-aws-glue-crawlers/ "https://aws.amazon.com/blogs/big-data/introducing-native-delta-lake-table-support-with-aws-glue-crawlers/") in
  the _AWS Big Data Blog_ and [Scheduling an AWS Glue
  crawler](../../../glue/latest/dg/schedule-crawler.md "../../../glue/latest/dg/schedule-crawler.md") in the AWS Glue Developer Guide.
- Drop and recreate the table in Athena.
- Use the SDK, CLI, or AWS Glue console to manually update the schema in
  AWS Glue.
  Note that the following features require your AWS Glue schema to always have the same
  schema as the transaction log:

- Lake Formation
- Views
- Row and column filters
  If your workflow does not require any of this functionality, and you prefer not to
  maintain this compatibility, you can use `CREATE TABLE` DDL in Athena and then
  add the Amazon S3 path as a SerDe parameter in AWS Glue.

You can use the following procedure to create a Delta Lake table with the
Athena and AWS Glue consoles.

###### To create a Delta Lake table using the Athena and AWS Glue consoles

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. In the Athena query editor, use the following DDL to create your Delta
   Lake table. Note that when using this method, the value for
   `TBLPROPERTIES` must be
   `'spark.sql.sources.provider' = 'delta'` and not
   `'table_type' = 'delta'`.

Note that this same schema (with a single of column named
`col` of type `array<string>`) is
inserted when you use Apache Spark (Athena for Apache Spark) or most
other engines to create your table.

```
CREATE EXTERNAL TABLE
   [db_name.]table_name(col array<string>)
   LOCATION 's3://amzn-s3-demo-bucket/`your-folder`/'
   TBLPROPERTIES ('spark.sql.sources.provider' = 'delta')
```

3. Open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
4. In the navigation pane, choose **Data Catalog**,
   **Tables**.
5. In the list of tables, choose the link for your table.
6. On the page for the table, choose **Actions**,
   **Edit table**.
7. In the **Serde parameters** section, add the key
   `path` with the value
   `s3://amzn-s3-demo-bucket/`your-folder`/`.
8. Choose **Save**.
   To create a Delta Lake table using the AWS CLI, enter a command like the
   following.

```
aws glue create-table --database-name dbname \
    --table-input '{"Name" : "tablename", "StorageDescriptor":{
            "Columns" : [
                {
                    "Name": "col",
                    "Type": "array<string>"
                }
            ],
            "Location" : "s3://`amzn-s3-demo-bucket`/`<prefix>`/",
            "SerdeInfo" : {
                "Parameters" : {
                    "serialization.format" : "1",
                    "path" : "s3://`amzn-s3-demo-bucket`/`<prefix>`/"
                }
            }
        },
        "PartitionKeys": [],
        "TableType": "EXTERNAL_TABLE",
        "Parameters": {
            "EXTERNAL": "TRUE",
            "spark.sql.sources.provider": "delta"
        }
    }'
```
