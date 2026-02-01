Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Referencing Iceberg tables in Amazon Redshift

Amazon Redshift provides multiple ways to reference Apache Iceberg tables stored in your data lake. You can use external schemas to create references to Data Catalog databases containing Iceberg tables, or use three-part notation for direct access to auto-mounted catalogs.

## Using external schemas to reference Iceberg tables

External schemas provide a way to reference tables in your Data Catalog from within Amazon Redshift. When you create an external schema, you establish a connection between your Amazon Redshift database and a specific Data Catalog database that contains your Iceberg tables.

To create an external schema for Iceberg tables:

```
CREATE EXTERNAL SCHEMA `schema_name`
FROM DATA CATALOG
DATABASE '`glue_database_name`'
IAM_ROLE '`arn:aws:iam::account-id:role/role-name`';
```

After creating the external schema, you can query Iceberg tables using two-part notation:

```
SELECT * FROM `schema_name`.`iceberg_table_name`;
```

You can also join Iceberg tables with local Amazon Redshift tables:

```
SELECT r.customer_id, i.order_date, r.customer_name
FROM local_customers r
JOIN `schema_name`.`iceberg_orders` i
ON r.customer_id = i.customer_id;
```

## Using three-part notation with auto-mounted catalogs

Three-part notation allows you to directly reference tables in auto-mounted catalogs without creating external schemas. This method is particularly useful when working with Amazon S3 table buckets federated with AWS Lake Formation. For information about setting up automatic mounting of the Data Catalog, see [Simplify external object access in Amazon Redshift using automatic mounting of the AWS Glue Data Catalog](https://aws.amazon.com/blogs/big-data/simplify-external-object-access-in-amazon-redshift-using-automatic-mounting-of-the-aws-glue-data-catalog/ "https://aws.amazon.com/blogs/big-data/simplify-external-object-access-in-amazon-redshift-using-automatic-mounting-of-the-aws-glue-data-catalog/").

The syntax for three-part notation is:

```
`"catalog_name"`.`database_name`.`table_name`
```

For example, to query an Iceberg table in an auto-mounted Amazon S3 table catalog:

```
SELECT * FROM "`my_table_bucket`@s3tablescatalog".`my_database`.`my_iceberg_table`;
```

For more information about integrating Amazon S3 table buckets with Amazon Redshift, see [Integrating S3 Tables with Amazon Redshift](../../../s3/latest/userguide/s3-tables-integrating-redshift.md "../../../s3/latest/userguide/s3-tables-integrating-redshift.md") in the _Amazon S3 User Guide_.

You can also use the `USE` statement to set a default catalog and database:

```
USE "`my_table_bucket`@s3tablescatalog".`my_database`;
SELECT * FROM `my_iceberg_table`;
```

To set a search path for schema resolution:

```
USE "`my_table_bucket`@s3tablescatalog";
SET search_path TO `my_database`;
SELECT * FROM `my_iceberg_table`;
```

## Best practices for referencing Iceberg tables

Consider the following best practices when referencing Iceberg tables in Amazon Redshift:

- Use descriptive schema names – When creating external schemas, use names that clearly indicate the source and purpose of the data, such as `sales_data_lake` or `customer_analytics`.
- Leverage table statistics – Ensure that column statistics are generated for your Iceberg tables using AWS Glue to optimize query performance. Amazon Redshift uses these statistics for query planning and optimization.
- Consider data freshness – Iceberg tables may be updated by other services while you're querying them. Amazon Redshift provides transactional consistency, ensuring you see a consistent snapshot of the data during your query execution.
- Use appropriate IAM permissions – Ensure that your Amazon Redshift cluster or workgroup has the necessary IAM permissions to access the Amazon S3 locations where your Iceberg tables are stored, as well as the Data Catalog metadata.
- Monitor query performance – Use Amazon Redshift query monitoring features to track the performance of queries against Iceberg tables and optimize as needed.

## Common referencing patterns

The following examples demonstrate common patterns for referencing Iceberg tables:

Aggregating data across multiple Iceberg tables:

```
SELECT
    region,
    SUM(sales_amount) as total_sales,
    COUNT(*) as transaction_count
FROM data_lake.sales_transactions
WHERE transaction_date >= '2024-01-01'
GROUP BY region
ORDER BY total_sales DESC;
```

Joining Iceberg tables with local Amazon Redshift tables:

```
SELECT
    c.customer_name,
    c.customer_tier,
    SUM(o.order_amount) as total_orders
FROM customers c
JOIN data_lake.order_history o ON c.customer_id = o.customer_id
WHERE o.order_date >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY c.customer_name, c.customer_tier;
```

Using three-part notation with complex queries:

```
WITH recent_orders AS (
    SELECT customer_id, order_date, order_amount
    FROM "analytics_bucket@s3tablescatalog".ecommerce.orders
    WHERE order_date >= CURRENT_DATE - INTERVAL '7 days'
)
SELECT
    customer_id,
    COUNT(*) as order_count,
    AVG(order_amount) as avg_order_value
FROM recent_orders
GROUP BY customer_id
HAVING COUNT(*) > 1;
```
