# Run federated queries

After you have configured one or more data connectors and deployed them to your account,
you can use them in your Athena queries.

## Query a single data

source

The examples in this section assume that you have configured and deployed the [Amazon Athena CloudWatch connector](connectors-cloudwatch.md "connectors-cloudwatch.md") to your
account. Use the same approach to query when you use other connectors.

###### To create an Athena query that uses the CloudWatch connector

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. In the Athena query editor, create a SQL query that uses the following syntax
   in the `FROM` clause.

```
`MyCloudwatchCatalog`.`database_name`.`table_name`
```

### Examples

The following example uses the Athena CloudWatch connector to connect to the
`all_log_streams` view in the
`/var/ecommerce-engine/order-processor` CloudWatch Logs [Log group](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md").
The `all_log_streams` view is a view of all the log streams in the log
group. The example query limits the number of rows returned to 100.

```
SELECT *
FROM "MyCloudwatchCatalog"."/var/ecommerce-engine/order-processor".all_log_streams
LIMIT 100;
```

The following example parses information from the same view as the previous
example. The example extracts the order ID and log level and filters out any message
that has the level `INFO`.

```
SELECT
    log_stream as ec2_instance,
    Regexp_extract(message '.*orderId=(\d+) .*', 1) AS orderId,
    message AS order_processor_log,
    Regexp_extract(message, '(.*):.*', 1) AS log_level
FROM MyCloudwatchCatalog."/var/ecommerce-engine/order-processor".all_log_streams
WHERE Regexp_extract(message, '(.*):.*', 1) != 'INFO'
```

## Query multiple data

sources

As a more complex example, imagine an e-commerce company that uses the following data
sources to store data related to customer purchases:

- [Amazon RDS for MySQL](https://aws.amazon.com/rds/mysql/ "https://aws.amazon.com/rds/mysql/") to store
  product catalog data
- [Amazon DocumentDB](https://aws.amazon.com/documentdb/ "https://aws.amazon.com/documentdb/") to store customer
  account data such as email and shipping addresses
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") to store order
  shipment and tracking data

Imagine that a data analyst for this e-commerce application learns that shipping time
in some regions has been impacted by local weather conditions. The analyst wants to know
how many orders are delayed, where the affected customers are located, and which
products are most affected. Instead of investigating the sources of information
separately, the analyst uses Athena to join the data together in a single federated
query.

```
SELECT
     t2.product_name AS product,
     t2.product_category AS category,
     t3.customer_region AS region,
     count(t1.order_id) AS impacted_orders
FROM my_dynamodb.default.orders t1
JOIN my_mysql.products.catalog t2 ON t1.product_id = t2.product_id
JOIN my_documentdb.default.customers t3 ON t1.customer_id = t3.customer_id
WHERE
     t1.order_status = 'PENDING'
     AND t1.order_date between '2022-01-01' AND '2022-01-05'
GROUP BY 1, 2, 3
ORDER BY 4 DESC
```

## Query federated

views

When querying federated sources, you can use views to obfuscate the underlying data
sources or hide complex joins from other analysts who query the data.

### Considerations and limitations

- Federated views require Athena engine version 3.
- Federated views are stored in AWS Glue, not with the underlying data
  source.
- Federated views are not supported on data sources that are [registered as a
  Glue Data Catalog](register-connection-as-gdc.md "register-connection-as-gdc.md").
- Views created with federated catalogs must use fully qualified name
  syntax, as in the following example:

```
"ddbcatalog"."default"."customers"
```

- Users who run queries on federated sources must have permission to query
  the federated sources.
- The `athena:GetDataCatalog` permission is required for
  federated views. For more information, see [Allow access to Athena Federated Query: Example policies](federated-query-iam-access.md "federated-query-iam-access.md") .

### Examples

The following example creates a view called `customers` on data stored
in a federated data source.

```
CREATE VIEW customers AS
SELECT *
FROM my_federated_source.default.table
```

The following example query shows a query that references the
`customers` view instead of the underlying federated data
source.

```
SELECT id, SUM(order_amount)
FROM customers
GROUP by 1
ORDER by 2 DESC
LIMIT 50
```

The following example creates a view called `order_summary` that
combines data from a federated data source and from an Amazon S3 data source. From the
federated source, which has already been created in Athena, the view uses the
`person` and `profile` tables. From Amazon S3, the view uses
the `purchase` and `payment` tables. To refer to Amazon S3, the
statement uses the keyword `awsdatacatalog`. Note that the federated data
source uses the fully qualified name syntax
`federated_source_name`.`federated_source_database`.`federated_source_table`.

```
CREATE VIEW default.order_summary AS
SELECT *
FROM `federated_source_name`.`federated_source_database`."person" p
    JOIN `federated_source_name`.`federated_source_database`."profile" pr ON pr.id = p.id
    JOIN awsdatacatalog.default.purchase i ON p.id = i.id
    JOIN awsdatacatalog.default.payment pay ON pay.id = p.id
```

### Additional resources

- For an example of a federated view that is decoupled from its originating
  source and is available for on-demand analysis in a multi-user model, see
  [Extend your data mesh with Amazon Athena and federated views](https://aws.amazon.com/blogs/big-data/extend-your-data-mesh-with-amazon-athena-and-federated-views/ "https://aws.amazon.com/blogs/big-data/extend-your-data-mesh-with-amazon-athena-and-federated-views/") in the
  _AWS Big Data Blog_.
- For more information about working with views in Athena, see [Work with views](views.md "views.md").
