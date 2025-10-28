# Optimizing reads with pushdown in AWS Glue ETL

Pushdown is an optimization technique that pushes logic about retrieving data closer to the source of your
data. The source could be a database or a file system such as Amazon S3. When executing certain operations directly
on the source, you can save time and processing power by not bringing all the data over the network to the Spark
engine managed by AWS Glue.

Another way of saying this is that pushdown reduces data scan. For more information
about the process of identifying when this technique is appropriate, consult [Reduce the amount of data scan](../../../prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/reduce-data-scan.md "../../../prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/reduce-data-scan.md") in the _Best practices for performance tuning
AWS Glue for Apache Spark jobs_ guide on AWS Prescriptive Guidance.

## Predicate pushdown on files stored on Amazon S3

When working with files on Amazon S3 that have been organized by prefix, you can filter your target Amazon S3 paths by defining a
pushdown predicate. Rather than reading the complete dataset and applying filters within a
`DynamicFrame`, you can directly apply the filter to the partition metadata stored in the
AWS Glue Data Catalog. This approach allows you to selectively list and read only the necessary data. For more information
about this process, including writing to a bucket by partitions, see [Managing partitions for ETL output in AWS Glue](aws-glue-programming-etl-partitions.md "aws-glue-programming-etl-partitions.md").

You achieve predicate pushdown in Amazon S3 by using the `push_down_predicate` parameter. Consider a bucket in
Amazon S3 you've partitioned by year, month and day. If you want to retrieve customer data for June of 2022, you
can instruct AWS Glue to read only relevant Amazon S3 paths. The `push_down_predicate` in this case is
`year='2022' and month='06'`. Putting it all together, the read operation can be achieved as
below:

Python

```
customer_records = glueContext.create_dynamic_frame.from_catalog(
    database = "customer_db",
    table_name = "customer_tbl",
    push_down_predicate = "year='2022' and month='06'"
)
```

Scala

```
val customer_records = glueContext.getCatalogSource(
database="customer_db",
tableName="customer_tbl",
pushDownPredicate="year='2022' and month='06'"
).getDynamicFrame()
```

In the previous scenario, `push_down_predicate` retrieves a list of all partitions from the
AWS Glue Data Catalog and filters them before reading the underlying Amazon S3 files. Though this helps in most cases, when
working with datasets that have millions of partitions, the process of listing partitions can be time
consuming. To address this issue, server-side pruning of partitions can be used to improve performance. This
is done by building a **Partition index** for your data in the AWS Glue Data Catalog. For more
information about partition indices, see [Creating partition indexes](partition-indexes.md "partition-indexes.md") . You can then use the
`catalogPartitionPredicate` option to reference the index. For an example retrieving partitions
with `catalogPartitionPredicate`, see [Server-side filtering using catalog partition predicates](aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-cat-predicates "aws-glue-programming-etl-partitions.md#aws-glue-programming-etl-partitions-cat-predicates").

## Pushdown when working with JDBC sources

The AWS Glue JDBC reader used in the `GlueContext` supports pushdown on supported databases by providing
custom SQL queries that can run directly on the source. This can be achieved by setting the `sampleQuery` parameter.
Your sample query can specify which columns to select as well as provide a pushdown predicate to limit the data transferred to the Spark engine.

By default, sample queries operate on a single node, which can result in job failures when dealing with large
data volumes. To use this feature to query data at scale, you should configure query partitioning by setting `enablePartitioningForSampleQuery` to true, which
will distribute the query to multiple nodes across a key of your choice. Query partitioning also requires a few other necessary configuration parameters.
For more information about query partitioning, see [Reading from JDBC tables in parallel](run-jdbc-parallel-read-job.md "run-jdbc-parallel-read-job.md").

When setting `enablePartitioningForSampleQuery`, AWS Glue will combine your pushdown predicate
with a partitioning predicate when querying your database. Your `sampleQuery` must end with an
`AND` for AWS Glue to append partitioning conditions. (If you do not provide a pushdown predicate,
`sampleQuery` must end with an `WHERE`). See an example below, where we push down a
predicate to only retrieve rows whose `id` is greater than 1000. This `sampleQuery`
will only return the name and location columns for rows where `id` is greater than the specified
value:

Python

```
sample_query = "select name, location from customer_tbl WHERE id>=1000 AND"
customer_records = glueContext.create_dynamic_frame.from_catalog(
    database="customer_db",
    table_name="customer_tbl",
    sample_query = "select name, location from customer_tbl WHERE id>=1000 AND",

    additional_options = {
                           "hashpartitions": 36 ,
                           "hashfield":"id",
                           "enablePartitioningForSampleQuery":True,
                           "sampleQuery":sample_query
                          }
)
```

Scala

```
val additionalOptions = Map(
        "hashpartitions" -> "36",
        "hashfield" -> "id",
        "enablePartitioningForSampleQuery" -> "true",
        "sampleQuery" -> "select name, location from customer_tbl WHERE id >= 1000 AND"
        )

    val customer_records = glueContext.getCatalogSource(
        database="customer_db",
        tableName="customer_tbl").getDynamicFrame()

```

###### Note

If `customer_tbl` has a different name in your Data Catalog and underlying datastore, you must provide the underlying table name in sample_query, since the query
is passed to the underlying datastore.

You can also query against JDBC tables without integrating with the AWS Glue Data Catalog. Instead of providing username and password as parameters to the method, you can reuse
credentials from a preexisting connection by providing `useConnectionProperties` and `connectionName`. In this example, we retrieve credentials from
a connection called `my_postgre_connection`.

Python

```
connection_options_dict = {
    "useConnectionProperties": True,
    "connectionName": "my_postgre_connection",
    "dbtable":"customer_tbl",
    "sampleQuery":"select name, location from customer_tbl WHERE id>=1000 AND",
    "enablePartitioningForSampleQuery":True,
    "hashfield":"id",
    "hashpartitions":36
    }

customer_records = glueContext.create_dynamic_frame.from_options(
    connection_type="postgresql",
    connection_options=connection_options_dict
    )
```

Scala

```
val connectionOptionsJson = """
      {
        "useConnectionProperties": true,
        "connectionName": "my_postgre_connection",
        "dbtable": "customer_tbl",
        "sampleQuery": "select name, location from customer_tbl WHERE id>=1000 AND",
        "enablePartitioningForSampleQuery" : true,
        "hashfield" : "id",
        "hashpartitions" : 36
      }
    """

    val connectionOptions = new JsonOptions(connectionOptionsJson)

    val dyf = glueContext.getSource("postgresql", connectionOptions).getDynamicFrame()
```

## Notes and limitations for pushdown in AWS Glue

Pushdown, as a concept, is applicable when reading from non-streaming sources. AWS Glue supports a variety of
sources - the ability to pushdown depends on the source and connector.

- When connecting to Snowflake, you can use the `query` option. Similar functionality exists in
  the Redshift connector in AWS Glue 4.0 and later versions. For more information about reading from Snowflake
  with `query`, see [Reading from Snowflake tables](aws-glue-programming-etl-connect-snowflake-home.md#aws-glue-programming-etl-connect-snowflake-read "aws-glue-programming-etl-connect-snowflake-home.md#aws-glue-programming-etl-connect-snowflake-read").
- The DynamoDB ETL reader does not support filters or pushdown predicates. MongoDB and DocumentDB also do not
  support this sort of functionality.
- When reading from data stored in Amazon S3 in open table formats, the partitioning method for files in Amazon S3 is no longer sufficient.
  To read and write from partitions using open table formats, consult documentation for the format.
- DynamicFrame methods do not perform Amazon S3 projection pushdown. All columns will be read from files
  that pass the predicate filter.
- When working with `custom.jdbc` connectors in AWS Glue, the ability to pushdown depends on the source and connector.
  Please review the appropriate connector documentation to confirm if and how it supports pushdown in AWS Glue.
