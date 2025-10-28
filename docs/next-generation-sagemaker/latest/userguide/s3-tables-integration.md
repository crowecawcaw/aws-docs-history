# Get started with Amazon S3 Tables in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio provides integrated support for S3 Tables, allowing you to create S3 table buckets and Apache Iceberg tables in those buckets.

Amazon S3 Tables provide S3 storage that’s optimized for analytics workloads, with built-in Apache Iceberg support and features designed to continuously improve query performance and reduce storage costs for tables. Data in S3 Tables is stored in table buckets, which are specialized buckets for storing tabular data. For more information, see [Working with Amazon S3 Tables and table buckets](../../../AmazonS3/latest/userguide/s3-tables.md "../../../AmazonS3/latest/userguide/s3-tables.md").

You can begin working with S3 Tables directly by creating an S3 table bucket as a new data source within Amazon SageMaker Unified Studio.

## Integrating S3 with AWS analytics services through Amazon SageMaker Unified Studio

Amazon S3 table buckets integrate with AWS Glue Data Catalog and AWS Lake Formation to allow AWS analytics services to automatically discover and access your table data. For more information, see [Integrating Amazon S3 Tables with AWS analytics services](../../../AmazonS3/latest/userguide/s3-tables-integrating-aws.md "../../../AmazonS3/latest/userguide/s3-tables-integrating-aws.md").

If you've never used S3 Tables before in the current Region, you can allow Amazon SageMaker to enable the S3 Tables analytics integration when you create a new S3 Tables catalog in the Amazon SageMaker Unified Studio console.

When you allow Amazon SageMaker Unified Studio to perform the integration, Amazon SageMaker takes the following actions on your behalf in your account:

- Creates a new AWS AWS Identity and Access Management (IAM) [service role](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") that gives Lake Formation access to all your tables and table buckets in your current Region. This allows Lake Formation to manage access, permissions, and governance for all current and future table buckets in that Region.
- Creates the `S3tablescatalog` in the AWS Glue Data Catalog in your current Region without privileged access.
- Adds the Amazon Redshift service role (`AWSServiceRoleForRedshift`) as a [Lake Formation Read-only administrator](../../../lake-formation/latest/dg/permissions-reference.md#persona-read-only-admin "../../../lake-formation/latest/dg/permissions-reference.md#persona-read-only-admin"). This allows Amazon Redshift to automatically mount all tables in S3 table buckets in the Region.

###### Note

Integration will be performed in the current Region only.

## Prerequisites

- Create a Amazon SageMaker domain and project. For more information, see [Setting up Amazon SageMaker](setting-up.md "setting-up.md").

## Creating S3 Tables catalogs in Amazon SageMaker Unified Studio

To get started using S3 Tables in Amazon SageMaker Unified Studio you create a new Lakehouse catalog with S3 table bucket source using the following steps.

1. Open the Amazon SageMaker at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/") and use the Region selector in the top navigation bar to choose the appropriate AWS Region.
2. Select your Amazon SageMaker domain.
3. Select the project you want to create a table bucket in.
4. In the navigation menu select **Data**, then select **+** to add a new data source.
5. select **Create Lakehouse catalog**.
6. In the add catalog menu, choose **S3 Tables** as the source.
7. Enter a name for the catalog, and a database name.
8. Choose **Create catalog**. This creates the following resources in your account:
   1. A new S3 Table bucket and the corresponding AWS Glue child catalog under the parent catalog `s3tablescatalog`.
   2. A new database within that AWS Glue child catalog. The database name will match the database name you provided. In S3 tables, this is the table namespace.

9. Begin creating tables in your database and querying them using query editor or Jupyter notebook.

## Creating and Querying S3 Tables

After you add an S3 Tables catalog it can be queried as `s3tablescatalog/`your-bucket-name``. You can begin creating S3 tables in the catalog and querying them in Amazon SageMaker Unified Studio with the Query editor and Jupyterlab.

###### Note

You can only create S3 tables in Amazon SageMaker Unified Studio with Athena engine or Spark. Once created, you can query tables with Athena, Amazon Redshift, or Spark.

Using the Query Editor

1. Navigate to the project you created in the top center menu of the Amazon SageMaker Unified Studio home page.
2. Expand the **Build** menu in the top navigation bar, then choose **Query editor**.
3. Create a new querybook tab. A querybook is a kind of SQL notebook where you can draw from multiple engines to design and visualize data analytics solutions.
4. Select a data source for your queries by using the menu in the upper-right corner of the querybook.
   1. Under **Connections**, choose **Lakehouse (Athena)** to connect to your Lakehouse resources.
   2. Under **Catalogs**, choose `s3tablescatalog/{your-table-bucket}`
   3. Under **Databases**, choose the name of the database for your S3 tables.

5. Select **Choose** to connect to the database and query engine.
6. Enter SQL to create your first table, the following is an example SQL query:

```
CREATE TABLE `daily_sales` (
    sale_date date,
    product_category string,
    sales_price double
)
PARTITIONED BY (month(sale_date))
TBLPROPERTIES ('table_type' = 'iceberg')
```

    1. After you create the table you can browse to it in the **Data explorer** by choosing **S3tablescatalog** → `your-bucket-name` → `example_database` → `example_table`

7. Insert data into a table with the following query.

```
INSERT INTO daily_sales
VALUES (DATE '2024-01-15', 'Monitor', 900.00),
(DATE '2024-01-14', 'Keyboard', 250.00),
(DATE '2024-01-16', 'CPU', 1350.00)
;
```

8. Select data from a table with the following query.

```
SELECT *
FROM daily_sales
WHERE sale_date BETWEEN DATE '2024-01-14' AND DATE '2024-01-16' ORDER BY sale_date;
```

To learn more about the query editor and see more SQL examples, see: [Get started with the query editor in Amazon SageMaker Unified Studio](../../../sagemaker-unified-studio/latest/userguide/getting-started-querying.md "../../../sagemaker-unified-studio/latest/userguide/getting-started-querying.md")

Using JupyterLab

1. Navigate to the project you created in the top center menu of the Amazon SageMaker Unified Studio home page.
2. Expand the **Build** menu in the top navigation bar, then choose **JupyterLab**.
3. Create a new notebook.
4. Select engine you want to use
5. Select your table bucket and namespace as the data source for your queries:
   1. For Spark engine, execute query `USE s3tablescatalog_`example-table-bucket``
   2. For Athena or Amazon Redshift engine, use the following configure magic. For more information, see [Configure compute resources in JupyterLab](../../../sagemaker-unified-studio/latest/userguide/jupyterlab-compute-configure.md "../../../sagemaker-unified-studio/latest/userguide/jupyterlab-compute-configure.md") in the _SageMaker AI Unified Studio User Guide_.

   ```
   %%configure -n project.athena -f
   {
       "catalog_name": "s3tablescatalog/`examples-table-bucket`",
       "schema_name": "`example-namespace`"
   }
   ```

6. Enter SQL queries into the notebook cell to create a table in the database.

###### Important

When using the Spark engine through a Spark connection, the [`S3TableFullAccess`](../../../aws-managed-policy/latest/reference/AmazonS3TablesFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonS3TablesFullAccess.md") permission is required for table creation. For more information, refer to [Considerations for enabling Lake Formation permissions](../../../glue/latest/dg/security-lf-enable-considerations.md "../../../glue/latest/dg/security-lf-enable-considerations.md") in the _AWS Glue Developer Guide_.

The following are examples of basic SQL queries you can use to start working with tables.

Create a new table

```
CREATE TABLE `daily_sales` (
    sale_date date,
    product_category string,
    sales_price double
)
PARTITIONED BY (month(sale_date))
TBLPROPERTIES ('table_type' = 'iceberg')
```

After you create the table you can browse to it in the **Data explorer** by choosing **S3tablescatalog** → **`your-bucket-name`** → **`your-database-name`** → **`daily_sales`**

Insert data into a table

```
INSERT INTO `daily_sales`
VALUES
(DATE '2024-01-15', 'Monitor', 900.00),
(DATE '2024-01-14', 'Keyboard', 250.00),
(DATE '2024-01-16', 'CPU', 1350.00)
;
```

Select data from a table

```
SELECT * FROM `daily_sales`
WHERE sale_date BETWEEN DATE '2024-01-14' AND DATE '2024-01-16'
ORDER BY sale_date;
```

Drop a table

```
DROP TABLE IF EXISTS `sample_table`;
```
