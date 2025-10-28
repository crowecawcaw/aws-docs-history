# Create tables using AWS Glue or the Athena

console

You can create tables in Athena by using AWS Glue, the add table form, or by running a DDL
statement in the Athena query editor.

## To create a

table using the AWS Glue crawler

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. In the query editor, next to **Tables and views**, choose
   **Create**, and then choose **AWS Glue
   crawler**.
3. Follow the steps on the **Add crawler** page of the AWS Glue
   console to add a crawler.

For more information, see [Use a crawler to add a table](schema-crawlers.md "schema-crawlers.md").

## To create a table using the

Athena create table form

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. In the query editor, next to **Tables and views**, choose
   **Create**, and then choose **S3 bucket
   data.**
3. In the **Create Table From S3 bucket data** form, enter
   the information to create your table, and then choose **Create
   table**. For more information about the fields in the form, see
   [Use a form in the Athena console to add an
   AWS Glue table](data-sources-glue-manual-table.md "data-sources-glue-manual-table.md").

## To create a table using a CREATE

TABLE statement in the Athena query editor

1. From the **Database** menu, choose the database for which
   you want to create a table. If you don't specify a database in your
   `CREATE TABLE` statement, the table is created in the
   database that is currently selected in the query editor.
2. In the query editor, enter a statement as shown in the following example
   and then choose **Run**.

```
CREATE EXTERNAL TABLE `myopencsvtable` (
   firstname string,
   lastname string,
   job string,
   country string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
   'separatorChar' = ',',
   'quoteChar' = '"',
   'escapeChar' = '\\'
   )
STORED AS TEXTFILE
LOCATION 's3://`amzn-s3-demo-bucket`/`mycsv`/';
```
