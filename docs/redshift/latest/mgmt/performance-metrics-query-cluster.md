Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Viewing cluster performance as

queries run

You can monitor the performance of your clusters as queries run to identify
potential bottlenecks and optimize query execution. Viewing cluster performance as
queries run provides a real-time view of the system-level metrics, such as CPU
utilization, disk I/O, and network traffic, as well as query-level details like
execution time, data processed, and query steps. The following procedures guides you
through accessing and interpreting the performance metrics to effectively manage and
optimize your provisioned clusters.

###### To display cluster performance as queries run

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**, then choose
   the cluster name from the list to open its details. The details of the
   cluster are displayed, which can include **Cluster performance**, **Query monitoring**,
   **Databases**, **Datashares**,
   **Schedules**, **Maintenance**, and **Properties** tabs.
3. Choose the **Query monitoring** tab for more details.

For more information, see [Viewing query history
data](performance-metrics-query-history.md "performance-metrics-query-history.md").
