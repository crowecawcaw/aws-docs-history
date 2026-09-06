

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Referencing Iceberg tables in Amazon Redshift
<a name="referencing-iceberg-tables"></a>

Amazon Redshift provides multiple ways to reference Apache Iceberg tables stored in your data lake. You can use external schemas to create references to Data Catalog databases containing Iceberg tables, or use three-part notation for direct access to auto-mounted catalogs.

## Using external schemas to reference Iceberg tables
<a name="referencing-iceberg-external-schemas"></a>

External schemas provide a way to reference tables in your Data Catalog from within Amazon Redshift. When you create an external schema, you establish a connection between your Amazon Redshift database and a specific Data Catalog database that contains your Iceberg tables.

To create an external schema for Iceberg tables:

```
CREATE EXTERNAL SCHEMA {{schema_name}}
FROM DATA CATALOG
DATABASE '{{glue_database_name}}'
IAM_ROLE '{{arn:aws:iam::account-id:role/role-name}}';
```

After creating the external schema, you can query Iceberg tables using two-part notation:

```
SELECT * FROM {{schema_name}}.{{iceberg_table_name}};
```

You can also join Iceberg tables with local Amazon Redshift tables:

```
SELECT r.customer_id, i.order_date, r.customer_name
FROM local_customers r
JOIN {{schema_name}}.{{iceberg_orders}} i 
ON r.customer_id = i.customer_id;
```

## Using three-part notation with auto-mounted catalogs
<a name="referencing-iceberg-three-part-notation"></a>

With three-part notation, you can directly reference tables in auto-mounted catalogs without creating external schemas. This method is particularly useful when working with Amazon S3 table buckets federated with AWS Lake Formation. For information about setting up automatic mounting of the Data Catalog, see [Simplify external object access in Amazon Redshift using automatic mounting of the AWS Glue Data Catalog](https://aws.amazon.com/blogs/big-data/simplify-external-object-access-in-amazon-redshift-using-automatic-mounting-of-the-aws-glue-data-catalog/).

The syntax for three-part notation is:

```
{{"catalog_name"}}.{{database_name}}.{{table_name}}
```

For example, to query an Iceberg table in an auto-mounted Amazon S3 table catalog:

```
SELECT * FROM "{{my_table_bucket}}@s3tablescatalog".{{my_database}}.{{my_iceberg_table}};
```

For more information about integrating Amazon S3 table buckets with Amazon Redshift, see [Integrating S3 Tables with Amazon Redshift](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-redshift.html) in the *Amazon S3 User Guide*.

You can also reference tables under the auto-mounted root catalog `awsdatacatalog`, which provides direct access to databases and tables registered in the AWS Glue Data Catalog:

```
SELECT * FROM awsdatacatalog.{{my_database}}.{{my_iceberg_table}};
```

For more information about using the `awsdatacatalog` root catalog, see [Querying the AWS Glue Data Catalog](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-glue.html) in the *Amazon Redshift Management Guide* and [Managing Data Catalog namespaces](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-namespaces-datacatalog.html) in the *AWS Lake Formation Developer Guide*.

You can also use the `USE` statement to set a default catalog and database for Amazon S3 table buckets:

```
USE "{{my_table_bucket}}@s3tablescatalog".{{my_database}};
SELECT * FROM {{my_iceberg_table}};
```

To set a search path for schema resolution with Amazon S3 table buckets:

```
USE "{{my_table_bucket}}@s3tablescatalog";
SET search_path TO {{my_database}};
SELECT * FROM {{my_iceberg_table}};
```

**Note**  
The `USE` statement and `search_path` are only supported for `s3tablescatalog`. They can't be used with `awsdatacatalog`. To reference tables in `awsdatacatalog`, use the full three-part notation.

## Best practices for referencing Iceberg tables
<a name="referencing-iceberg-best-practices"></a>

An Apache Iceberg table is a single logical entity composed of multiple files: a root metadata file (metadata.json), manifest lists, manifest files, and data files (typically .parquet). The root metadata file serves as the entry point and contains references to all other files that make up the table. When you grant Amazon Redshift access to an Iceberg table, Amazon Redshift uses the root metadata file to discover and read all referenced data files. If Amazon Redshift has access to the root metadata file, it assumes and requires access to all underlying data files as well. This is consistent with Iceberg's design, where table-level access is the intended unit of authorization.

To improve query performance, Amazon Redshift caches Iceberg metadata files (including the root metadata file, manifest lists, and manifest files) in memory. The root metadata file (metadata.json) is revalidated against Amazon S3 at a configurable interval (TTL). After the TTL expires, Amazon Redshift performs an Amazon S3 HEAD request on the root metadata file to verify that the IAM role still has access and that the file has not been modified. If the permission check fails or the file has changed, the cached entry is evicted and the metadata is re-fetched from Amazon S3. Because the root metadata file is the entry point for all table access, this revalidation serves as the permission gate for the entire table. Manifest lists and manifest files are cached without independent TTL revalidation — their access validity is derived from the root metadata permission check. This means that if you revoke Amazon S3 permissions on an Iceberg table, queries may continue to succeed for a maximum of 2 minutes while using cached metadata.

**Important**  
Amazon S3 allows you to set permissions at the individual object level, which means it is technically possible to grant access to an Iceberg table's metadata while restricting access to some of its underlying data files. This creates a permission inconsistency that can lead to query failures or unexpected access errors in Amazon Redshift.

Amazon Redshift validates access to the cached root metadata file periodically but does not validate or enforce consistency between metadata-level and data-file-level permissions within your Amazon S3 bucket. It is the customer's responsibility to make sure that permissions are applied consistently across all files that constitute an Iceberg table.

To avoid this, consider the following best practices when referencing Iceberg tables in Amazon Redshift:
+ **Use descriptive schema names** – When creating external schemas, use names that clearly indicate the source and purpose of the data, such as `sales_data_lake` or `customer_analytics`.
+ **Leverage table statistics** – Make sure that column statistics are generated for your Iceberg tables using AWS Glue to optimize query performance. Amazon Redshift uses these statistics for query planning and optimization.
+ **Consider data freshness** – Iceberg tables may be updated by other services while you're querying them. Amazon Redshift provides transactional consistency, ensuring you see a consistent snapshot of the data during your query execution.
+ **Use appropriate IAM permissions** – Make sure that your Amazon Redshift cluster or workgroup has the necessary IAM permissions to access the Amazon S3 locations where your Iceberg tables are stored, as well as the Data Catalog metadata.
+ **Table level permissions** – Grant permissions at the table level, not at the individual file level.
+ **Uniform permissions** – Maintain uniform access across the entire Amazon S3 path for your Iceberg table, including all metadata, manifest, and data files.
+ **Avoid restrictive object-level policies** – Do not set restrictive object-level policies on individual Parquet files within an Iceberg table's prefix.
+ **Understand caching TTL for permission changes** – When you revoke Amazon S3 permissions on an Iceberg table, queries may continue to succeed using cached root metadata for up to the configured TTL duration (default: 2 minutes).
+ **Monitor query performance** – Use Amazon Redshift query monitoring features to track the performance of queries against Iceberg tables and optimize as needed.

## Common referencing patterns
<a name="referencing-iceberg-examples"></a>

The following examples demonstrate common patterns for referencing Iceberg tables:

**Aggregating data across multiple Iceberg tables:**

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

**Joining Iceberg tables with local Amazon Redshift tables:**

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

**Using three-part notation with complex queries:**

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