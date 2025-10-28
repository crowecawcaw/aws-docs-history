# Register S3 table bucket catalogs and

query Tables from Athena

Amazon S3 table buckets are a bucket type in Amazon S3 that is purpose-built to store tabular
data in Apache Iceberg tables. Table buckets automate table management tasks such as
compaction, snapshot management, and garbage collection to continuously optimize query
performance and minimize cost. Whether you're just starting out, or have thousands of
tables in your Iceberg environment, table buckets simplify data lakes at any scale. For
more information, see [Table buckets](../../../AmazonS3/latest/userguide/s3-tables-buckets.md "../../../AmazonS3/latest/userguide/s3-tables-buckets.md").

## Considerations and

limitations

- All DDL operations supported for Iceberg tables are supported for S3
  Tables with the following exceptions:
  - `ALTER TABLE RENAME`, `CREATE VIEW`, and
    `ALTER DATABASE` are not supported.
  - `OPTIMIZE` and `VACUUM` – You can
    manage compaction and snapshot management in S3. For more
    information, see [S3
    Tables maintenance documentation](../../../AmazonS3/latest/userguide/s3-tables-maintenance.md "../../../AmazonS3/latest/userguide/s3-tables-maintenance.md").

- DDL queries on S3 Tables registered as Athena data sources are not
  supported.
- Query result reuse is not supported.
- In workgroups with SSE-KMS, CSE-KMS encryption enabled, you can't run write
  operations like `INSERT`, `UPDATE`,
  `DELETE`, or `MERGE` on S3 Tables.
- In workgroups with S3 Requester Pays option enabled, you can't run DML
  operations on S3 Tables.

## Query S3 Tables from Athena

###### Complete these prerequisite steps before you query S3 Tables in Athena

1. Create an S3 table bucket. For more information, see [Creating a
   table bucket](../../../AmazonS3/latest/userguide/s3-tables-buckets-create.md "../../../AmazonS3/latest/userguide/s3-tables-buckets-create.md") in Amazon Simple Storage Service User Guide.
2. Make sure that the integration of your table buckets with AWS Glue Data Catalog and
   AWS Lake Formation is successful by following [Prerequisites for integration](../../../AmazonS3/latest/userguide/s3-tables-integrating-aws.md#table-integration-prerequisites "../../../AmazonS3/latest/userguide/s3-tables-integrating-aws.md#table-integration-prerequisites") and [Integrating table buckets with AWS analytics services](../../../AmazonS3/latest/userguide/s3-tables-integrating-aws.md#table-integration-procedures "../../../AmazonS3/latest/userguide/s3-tables-integrating-aws.md#table-integration-procedures") in
   Amazon Simple Storage Service User Guide.

###### Note

If you enabled the integration while creating an S3 table bucket from
the S3 console in Step 1, then you can skip this step. 3. For the principal you use to run queries with Athena, grant Lake Formation permissions on the S3 Table
catalog, either through the Lake Formation console or AWS CLI.

AWS Management Console

    1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/") and sign in as a data lake
     administrator. For more information on how to create a
     data lake administrator, see [Create a data lake administrator](../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin "../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin").
    2. In the navigation pane, choose **Data
     permissions** and then choose
     **Grant**.
    3. On the **Grant Permissions** page,
     under **Principals**, choose the
     principal that you want to use to submit query from
     Athena.
    4. Under **LF-Tags or catalog
     resources**, choose **Named Data
     Catalog resources**.
    5. For **Catalogs**, choose a glue data
     catalog that you created from the integration of your
     table bucket. For example,
     `<accoundID>`:s3tablescatalog/`amzn-s3-demo-bucket`.
    6. For **Catalog permissions**, choose
     **Super**.
    7. Choose **Grant**.

AWS CLI
Run the following command with Lake Formation data lake administrator
role to grant access to the principal that you use to submit
query from Athena.

```
aws lakeformation grant-permissions \
--region `<region (Example,us-east-1)>` \
--cli-input-json \
'{
    "Principal": {
        "DataLakePrincipalIdentifier": "`<user or role ARN (Example, arn:aws:iam::<Account ID>:role/ExampleRole>`"
    },
    "Resource": {
        "Catalog": {
            "Id":"`<Account ID>`:s3tablescatalog/`amzn-s3-demo-bucket`"
        }
    },
    "Permissions": ["ALL"]
}'
```

###### Submit queries for S3 Tables

1. Submit a `CREATE DATABASE` query from Athena with the above granted user/role. In
   this example, `s3tablescatalog` is the parent Glue Data Catalog
   created from the integration and `s3tablescatalog/`amzn-s3-demo-bucket``
   is the child Glue Data Catalog created for each S3 table bucket. There are
   two ways in which you can query.

Option 1 Specify the child Glue Data Catalog
(`s3tablescatalog/`amzn-s3-demo-bucket``)
directly from console or AWS CLI.

**Using AWS Management Console**

    1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/ "https://console.aws.amazon.com/athena/").
    2. In the left navigation, for **Data source
     name**, choose
     **AwsDataCatalog**.
    3. For **Catalog**, choose
     **s3tablescatalog/`amzn-s3-demo-bucket`**.
    4. In the query editor, enter a query like
     `CREATE DATABASE
     `test_namespace``.

**Using AWS CLI**

Run the following command.

```
aws athena start-query-execution \
--query-string 'CREATE DATABASE ``test_namespace``' \
--query-execution-context '{"Catalog": "s3tablescatalog/`amzn-s3-demo-bucket`"}' \
--work-group "primary"
```

Option 2 Create Athena data catalog from the child Glue Data Catalog in the Athena console and specify
it as a catalog in the query. For more information, see [Register S3 table bucket catalogs as
Athena data sources](#gdc-register-s3-table-console-steps "#gdc-register-s3-table-console-steps"). 2. With the database that you created in previous step, use `CREATE
 TABLE` to create a table. The following example creates a table in
the `test_namespace` database that you
previously created in the
`s3tablescatalog/`amzn-s3-demo-bucket``
Glue catalog.

AWS Management Console

    1. In the left navigation, for **Data source
     name**, choose
     **AwsDataCatalog**.
    2. For **Catalog**, choose
     **s3tablescatalog/`amzn-s3-demo-bucket`**.
    3. For **Database**, choose
     **test\_namespace**.
    4. In the query editor, run the following query.



    ```
    CREATE TABLE `daily_sales` (
            sale_date date,
            product_category
            string, sales_amount double)
    PARTITIONED BY (month(sale_date))
    TBLPROPERTIES ('table_type' = 'iceberg')
    ```

AWS CLI
Run the following command.

```
aws athena start-query-execution \
--query-string "CREATE TABLE `daily_sales` (
        sale_date date,
        product_category
        string, sales_amount double)
PARTITIONED BY (month(sale_date))
TBLPROPERTIES ('table_type' = 'iceberg')" \
--query-execution-context '{"Catalog": "s3tablescatalog/`amzn-s3-demo-bucket`", "Database":"`test_namespace`"}' \
--work-group "primary"
```

3. Insert data into the table that you created in the previous step.

AWS Management Console

    1. In the left navigation, for **Data source
     name**, choose
     **AwsDataCatalog**.
    2. For **Catalog**, choose
     **s3tablescatalog/`amzn-s3-demo-bucket`**.
    3. For **Database**, choose
     **test\_namespace**.
    4. In the query editor, run the following query.



    ```
    INSERT INTO `daily_sales`
    VALUES
        (DATE '`2024-01-15`', '`Laptop`', `900.00`),
        (DATE '`2024-01-15`', '`Monitor`', `250.00`),
        (DATE '`2024-01-16`', '`Laptop`', `1350.00`),
        (DATE '`2024-02-01`', '`Monitor`', `300.00`);
    ```

AWS CLI
Run the following command.

```
aws athena start-query-execution \
--query-string "INSERT INTO \"s3tablescatalog/`amzn-s3-demo-bucket`\".`test_namespace`.`daily_sales`
VALUES
(DATE '2024-01-15', 'Laptop', 900.00),
(DATE '2024-01-15', 'Monitor', 250.00),
(DATE '2024-01-16', 'Laptop', 1350.00),
(DATE '2024-02-01', 'Monitor', 300.00)"\
--work-group "primary"
```

4. After inserting data into the table, you can query it.

AWS Management Console

    1. In the left navigation, for **Data source
     name**, choose
     **AwsDataCatalog**.
    2. For **Catalog**, choose
     **s3tablescatalog/`amzn-s3-demo-bucket`**.
    3. For **Database**, choose
     **test\_namespace**.
    4. In the query editor, run the following query.



    ```
    SELECT
        product_category,
        COUNT(*) AS units_sold,
        SUM(sales_amount) AS total_revenue,
        AVG(sales_amount) AS average_price
    FROM
        `daily_sales`
    WHERE
        sale_date BETWEEN DATE '`2024-02-01`'
                     AND DATE '`2024-02-29`'
    GROUP BY
        product_category
    ORDER BY
        total_revenue DESC
    ```

AWS CLI Run the following command.

```
aws athena start-query-execution \
--query-string "SELECT product_category,
    COUNT(*) AS units_sold,
    SUM(sales_amount) AS total_revenue,
    AVG(sales_amount) AS average_price
FROM \"s3tablescatalog/`amzn-s3-demo-bucket`\".`test_namespace`.`daily_sales`
WHERE sale_date BETWEEN DATE '2024-02-01' AND DATE '2024-02-29'
GROUP BY product_category
ORDER BY total_revenue DESC"\
--work-group "primary"
```

## Create S3 Tables in Athena

Athena supports creating tables in existing S3 Table namespaces or namespaces
created in Athena with `CREATE DATABASE` statements. To create an S3 Table
from Athena, the syntax is the same as when you [create a regular Iceberg table](querying-iceberg-creating-tables.md "querying-iceberg-creating-tables.md")
except you don't specify the `LOCATION`, as shown in the following
example.

```
CREATE TABLE
[db_name.]table_name (col_name data_type [COMMENT col_comment] [, ...] )
[PARTITIONED BY (col_name | transform, ... )]
[TBLPROPERTIES ([, property_name=property_value] )]
```

You can also create S3 Tables using CREATE TABLE AS SELECT (CTAS) statements. For
more information, see [CTAS for S3 Tables](#ctas-s3-tables "#ctas-s3-tables").

## Register S3 table bucket catalogs as

Athena data sources

To register S3 table bucket catalogs with the Athena console, perform the following
steps.

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/ "https://console.aws.amazon.com/athena/").
2. In the navigation pane, choose **Data sources and catalogs**.
3. On the **Data sources and catalogs** page, choose **Create data
   source**.
4. For **Choose a data source**, choose **Amazon S3 -
   AWS Glue Data Catalog**.
5. In the **AWS Glue Data Catalog** section, for **Data source
   account**, choose **AWS Glue Data Catalog in this
   account**.
6. For **Create a table or register a catalog**, choose
   **Register a new AWS Glue Catalog**.
7. In the **Data source details** section, for **Data
   source name**, enter the name that you want to use to specify the
   data source in your SQL queries or use the default name that is
   generated.
8. For **Catalog**, choose **Browse** to search
   for a list of AWS Glue catalogs in the same account. If you don't see any existing
   catalogs, create one in [AWS Glue console](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
9. In the **Browse AWS Glue catalogs** dialog box, select the
   catalog that you want to use, and then choose
   **Choose**.
10. (Optional) For **Tags**, enter any key/value pairs that you
    want to associate with the data source.
11. Choose **Next**.
12. On the **Review and create** page, verify that the
    information that you entered is correct, and then choose **Create data
    source**.

## CTAS for S3 Tables

Amazon Athena now supports CREATE TABLE AS SELECT (CTAS) operations for S3 Tables. This
feature enables you to create new S3 Tables based on the results of a SELECT query.

When creating a CTAS query for an S3 Table, there are a few important differences compared
to standard Athena tables:

- You must omit the location property because S3 Tables automatically manage their
  own storage locations.
- The `table_type` property defaults to `ICEBERG`, so you
  don't need to explicitly specify it in your query.
- If you don't specify a format, the system automatically uses `PARQUET`
  as the default format for your data.
- All other properties follow the same syntax as regular Iceberg tables.

Before you create S3 Tables using CTAS, ensure that you have the necessary
permissions configured in AWS Lake Formation. Specifically, you need permissions to create
tables in the S3 Tables catalog. Without these permissions, your CTAS operations
will fail.

###### Note

If your CTAS query fails, you might have to delete your table using the [S3
Tables API](../../../AmazonS3/latest/userguide/s3-tables-delete.md "../../../AmazonS3/latest/userguide/s3-tables-delete.md") before attempting to re-run your query. you cannot use the Athena
`DROP TABLE` statements to remove the table that was partially created by
the query.

**Example**

```
CREATE TABLE "s3tablescatalog/`amzn-s3-demo-bucket`"."`namespace`"."`s3-table-name`"
WITH (
    format = 'PARQUET'
)
AS SELECT *
FROM `source_table`;
```
