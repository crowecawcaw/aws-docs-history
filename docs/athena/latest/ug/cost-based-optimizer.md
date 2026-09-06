

# Use the cost-based optimizer
<a name="cost-based-optimizer"></a>

You can use the cost-based optimizer (CBO) feature in Athena SQL to optimize your queries. You can optionally request that Athena gather table or column-level statistics for one of your tables in AWS Glue. If all of the tables in your query have statistics, Athena uses the statistics to create an execution plan that it determines to be the most performant. The query optimizer calculates alternative plans based on a statistical model and then selects the one that will likely be the fastest to run the query.

Statistics on AWS Glue tables are collected and stored in the AWS Glue Data Catalog and made available to Athena for improved query planning and execution. These statistics are column-level statistics such as number of distinct, number of null, max, and min values on file types such as Parquet, ORC, JSON, ION, CSV, and XML. Amazon Athena uses these statistics to optimize queries by applying the most restrictive filters as early as possible in query processing. This filtering limits memory usage and the number of records that must be read to deliver the query results.

In conjunction with CBO, Athena uses a feature called the rule-based optimizer (RBO). RBO mechanically applies rules that are expected to improve query performance. RBO is generally beneficial because its transformations aim to simplify the query plan. However, because RBO does not perform cost calculations or plan comparisons, more complicated queries make it difficult for RBO to create an optimal plan.

For this reason, Athena uses both RBO and CBO to optimize your queries. After Athena identifies opportunities to improve query execution, it creates an optimal plan. For information about execution plan details, see [View execution plans for SQL queries](query-plans.md). For a detailed discussion of how CBO works, see [Speed up queries with the cost-based optimizer in Amazon Athena](https://aws.amazon.com/blogs/big-data/speed-up-queries-with-cost-based-optimizer-in-amazon-athena/) in the the AWS Big Data Blog.

To generate statistics for AWS Glue Catalog tables, you can use the Athena console, the AWS Glue Console, or AWS Glue APIs. Because Athena is integrated with AWS Glue Catalog, you automatically get the corresponding query performance improvements when you run queries from Amazon Athena.

## Considerations and limitations
<a name="cost-based-optimizer-considerations-and-limitations"></a>
+ **Table types** – Currently, the CBO feature in Athena supports only Hive and Iceberg tables that are in the AWS Glue Data Catalog.
+ **Athena for Spark** – The CBO feature is not available in Athena for Spark.
+ **Pricing** – For pricing information, visit the [AWS Glue pricing page](https://aws.amazon.com/glue/pricing).

## Generate table statistics using the Athena console
<a name="cost-based-optimizer-generating-table-statistics-using-the-athena-console"></a>

This section describes how to use the Athena console to generate table or column-level statistics for a table in AWS Glue. For information on using AWS Glue to generate table statistics, see [Working with column statistics](https://docs.aws.amazon.com/glue/latest/dg/column-statistics.html) in the *AWS Glue Developer Guide*.

**To generate statistics for a table using the Athena console**

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. In the Athena query editor **Tables** list, choose the three vertical dots for the table that you want, and then choose **Generate statistics**.  
![Context menu for a table in the Athena query editor.](http://docs.aws.amazon.com/athena/latest/ug/images/cost-based-optimizer-1.png)

1. In the **Generate statistics** dialog box, choose **All columns** to generate statistics for all columns in the table, or choose **Selected columns** to select specific columns. **All columns** is the default setting.  
![The generate statistics dialog box.](http://docs.aws.amazon.com/athena/latest/ug/images/cost-based-optimizer-2.png)

1. For **AWS Glue service role**, create or select an existing service role to give permission to AWS Glue to generate statistics. The AWS Glue service role also requires [`S3:GetObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) permissions to the Amazon S3 bucket that contains the table's data.  
![Choosing a AWS Glue service role.](http://docs.aws.amazon.com/athena/latest/ug/images/cost-based-optimizer-3.png)

1. Choose **Generate statistics**. A **Generating statistics for {{table\_name}}** notification banner displays the task status.  
![The Generating statistics notification banner.](http://docs.aws.amazon.com/athena/latest/ug/images/cost-based-optimizer-4.png)

1. To view details in the AWS Glue console, choose **View in Glue**. 

   For information about viewing statistics in the AWS Glue console, see [Viewing column statistics](https://docs.aws.amazon.com/glue/latest/dg/view-column-stats.html) in the *AWS Glue Developer Guide*. 

1. After statistics have been generated, the tables and columns that have statistics show the word **Statistics** in parentheses, as in the following image.  
![A table showing statistics icons in the Athena query editor.](http://docs.aws.amazon.com/athena/latest/ug/images/cost-based-optimizer-5.png)

Now when you run your queries, Athena will perform cost-based optimization on the tables and columns for which statistics were generated.

## Enable and disable the table statistics
<a name="cost-based-optimizer-enabling-iceberg-table-statistics"></a>

When you generate table statistics for an Iceberg table following the steps in previous section, a Glue table property called `use_iceberg_statistics` is automatically added to the Iceberg table in AWS Glue Data Catalog and set to **true** by default. If you remove this property or set it to **false**, CBO will not use the Iceberg table statistics when trying to optimize the query plan during query execution, even if the statistics were generated by Glue. For more information onhow to generate table statistics, see [Generate table statistics using the Athena console](#cost-based-optimizer-generating-table-statistics-using-the-athena-console).

In contrast, Hive tables in the Glue Data Catalog do not have a similar table property to enable or disable the use of table statistics for CBO. As a result, CBO always uses the table statistics generated by Glue when trying to optimize the query plan for Hive tables. 

## Additional resources
<a name="cost-based-optimizer-additional-resources"></a>

For additional information, see the following resource.

[![AWS Videos](http://img.youtube.com/vi/zUHEXJdHUxs?si=rMAhJj3I5IlhN-1R/0.jpg)](http://www.youtube.com/watch?v=zUHEXJdHUxs?si=rMAhJj3I5IlhN-1R)
