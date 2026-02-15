# Query AWS Glue Data Catalog materialized views

Athena allows you to query AWS Glue Data Catalog materialized views. Glue Data Catalog materialized views store pre-computed results of SQL queries as Apache Iceberg tables.

When you create Glue Data Catalog materialized views using Apache Spark in Amazon EMR or AWS Glue, the view definitions and metadata are stored in the AWS Glue Data Catalog. The pre-computed results are stored as Apache Iceberg tables in Amazon S3. You can query these materialized views from Athena using standard SQL `SELECT` statements, just as you would query regular Iceberg tables.

## Prerequisites

Before you query materialized views in Athena, ensure the following:

- The materialized view exists in the AWS Glue Data Catalog and was created using Apache Spark (Amazon EMR release 7.12.0 or later, or AWS Glue version 5.1 or later)
- To query materialized views in Athena, you need the following AWS Lake Formation permissions:
  - `SELECT` permission on the materialized view
  - `DESCRIBE` permission on the materialized view
  - Access to the underlying Amazon S3 location where the materialized view data is stored

- The materialized view's underlying data is stored in Amazon S3 Table buckets or Amazon S3 general purpose buckets
- You have access to the AWS Glue Data Catalog database containing the materialized view
- For materialized views stored in Amazon S3 Tables buckets, ensure your IAM role has the necessary permissions to access the S3 Tables catalog.

## Considerations and limitations

- Athena does not support the following operations on materialized views: `ALTER`, `CREATE MATERIALIZED VIEW`, `REFRESH MATERIALIZED VIEW`, `DROP`, `INSERT`, `UPDATE`, `MERGE`, `DELETE`, `OPTIMIZE`, `VACUUM`. To create materialized views, use Apache Spark in Amazon EMR or AWS Glue. Refresh operations must be performed through the AWS Glue Data Catalog API or Apache Spark. Modify materialized views using Apache Spark.

## Querying materialized views

Athena treats materialized views as standard Iceberg tables for read operations, allowing you to access the pre-computed data without requiring special syntax or configuration changes.

To query a materialized view in Athena, use standard `SELECT` statements:

```
SELECT * FROM my_database.sales_summary_mv;
```

You can apply filters, aggregations, and joins just as you would with regular tables:

```
SELECT
  region,
  SUM(total_sales) as sales_total
FROM my_database.sales_summary_mv
WHERE year = 2025
GROUP BY region
ORDER BY sales_total DESC;
```

## Supported operations

Athena supports the following operations on materialized views:

- `SELECT` queries - Read data from materialized views using standard SQL `SELECT` statements
- `DESCRIBE` - View the schema and metadata of materialized views
- `SHOW TABLES` - List materialized views along with other tables in a database
- `JOIN` operations - Join materialized views with other tables or views
- Filtering and aggregation - Apply `WHERE` clauses, `GROUP BY`, and aggregate functions
