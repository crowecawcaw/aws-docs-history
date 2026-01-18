Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Automatic database optimization

Amazon Redshift hosts a set of automated features, termed collectively as autonomics,
that enhance performance, reduce manual maintenance, and optimize resource usage. Autonomics
leverage machine learning and background processes to manage database operations efficiently,
automating many routine maintenance tasks to reduce database administrator workload.

The following table details Amazon Redshift's autonomics features:

| Autonomics feature           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Automatic vacuum sort        | Amazon Redshift automatically reorganizes table data<br>based on observed query patterns to ensure optimal<br>sort order. This feature is enabled by default for<br>tables with specified sort keys. For more information,<br>see [Automatic table sort](t_Reclaiming_storage_space202.md#automatic-table-sort "t_Reclaiming_storage_space202.md#automatic-table-sort").                                                                                            |
| Automatic vacuum delete      | Amazon Redshift automatically runs vacuum operations to<br>reclaim space from deleted rows and sort data. For<br>more information on automatic vacuum delete operations,<br>see [Automatic vacuum delete](t_Reclaiming_storage_space202.md#automatic-table-delete "t_Reclaiming_storage_space202.md#automatic-table-delete").                                                                                                                                       |
| Automatic table optimization | Amazon Redshift monitors query performance and table metadata<br>to automatically determine the best sort and distribution keys<br>for tables, and chooses the type of compression that is applied<br>to a column of data values as rows are added to a table.<br>For more information, see<br>[Automatic table optimization](t_Creating_tables.md "t_Creating_tables.md") and<br>[Compression encodings](c_Compression_encodings.md "c_Compression_encodings.md"). |
| Automatic analyze            | Amazon Redshift automatically analyzes tables as the data within them changes,<br>ensuring that the query planner has up-to-date information for optimal<br>execution plans. For more information on automatic analyze operations, see<br>[Automatic analyze](t_Analyzing_tables.md#t_Analyzing_tables-auto-analyze "t_Analyzing_tables.md#t_Analyzing_tables-auto-analyze").                                                                                       |
| Automated materialized views | Amazon Redshift automatically creates and refreshes materialized views based<br>on observed query patterns. This reduces the need for users to manually create<br>or refresh views to benefit from faster query responses. For more information<br>on materialized views, see<br>[Materialized views in Amazon Redshift](materialized-view-overview.md "materialized-view-overview.md").                                                                            |

These autonomics features are enabled by default and run automatically in the background during low-traffic
periods to optimize your cluster's performance. You can refer to the
[Default parameter values](../mgmt/working-with-parameter-groups.md#default-param-group-values "../mgmt/working-with-parameter-groups.md#default-param-group-values")
in the _Amazon Redshift Management Guide_
to configure automatic features.

For clusters or workgroups with sustained high traffic, we recommend enabling extra compute
resources to ensure continuous optimization. For more information, see
[Allocating extra compute resources for automatic database optimization](t_extra-compute-autonomics.md "t_extra-compute-autonomics.md").

###### Topics

- [Allocating extra compute resources for automatic database optimization](t_extra-compute-autonomics.md "t_extra-compute-autonomics.md")
- [Billing for autonomics operations](t_autonomics-billing.md "t_autonomics-billing.md")
- [Usage metrics for autonomics operations](t_autonomics-usage-metrics.md "t_autonomics-usage-metrics.md")
