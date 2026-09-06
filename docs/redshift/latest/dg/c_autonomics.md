

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Automatic database optimization
<a name="c_autonomics"></a>

Amazon Redshift hosts a set of automated features, termed collectively as autonomics, that enhance performance, reduce manual maintenance, and optimize resource usage. Autonomics leverage machine learning and background processes to manage database operations efficiently, automating many routine maintenance tasks to reduce database administrator workload.

The following table details Amazon Redshift's autonomics features:


| Autonomics feature | Description | 
| --- | --- | 
| Automatic vacuum sort | Amazon Redshift automatically reorganizes table data based on observed query patterns for optimal sort order. This feature is enabled by default for tables with specified sort keys. For more information, see [Automatic table sort](t_Reclaiming_storage_space202.md#automatic-table-sort). | 
| Automatic vacuum delete | Amazon Redshift automatically runs vacuum operations to reclaim space from deleted rows and sort data. For more information on automatic vacuum delete operations, see [Automatic vacuum delete](t_Reclaiming_storage_space202.md#automatic-table-delete). | 
| Automatic table optimization | Amazon Redshift monitors query performance and table metadata to automatically determine the best sort and distribution keys for tables, and chooses the type of compression that is applied to a column of data values as rows are added to a table. For more information, see [Automatic table optimization](t_Creating_tables.md) and [Compression encodings](c_Compression_encodings.md). | 
| Automatic analyze | Amazon Redshift automatically analyzes tables as the data within them changes, ensuring that the query planner has up-to-date information for optimal execution plans. For more information on automatic analyze operations, see [Automatic analyze](t_Analyzing_tables.md#t_Analyzing_tables-auto-analyze). | 
| Automated materialized views | Amazon Redshift automatically creates and refreshes materialized views based on observed query patterns. This reduces the need for users to manually create or refresh views to benefit from faster query responses. For more information on materialized views, see [Materialized views in Amazon Redshift](materialized-view-overview.md). | 

These autonomics features are enabled by default and run automatically in the background during low-traffic periods to optimize your cluster's performance. You can refer to the [Default parameter values](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html#default-param-group-values) in the *Amazon Redshift Management Guide* to configure automatic features.

For clusters or workgroups with sustained high traffic, we recommend enabling extra compute resources for continuous optimization. For more information, see [Allocating extra compute resources for automatic database optimization](t_extra-compute-autonomics.md).

**Topics**
+ [Allocating extra compute resources for automatic database optimization](t_extra-compute-autonomics.md)
+ [Billing for autonomics operations](t_autonomics-billing.md)
+ [Usage metrics for autonomics operations](t_autonomics-usage-metrics.md)