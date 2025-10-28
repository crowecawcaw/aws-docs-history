# Best practice 15.5 – Optimize your data modeling and data storage for efficient data retrieval

How your data is organized in a data store, database, or ﬁle system can have an impact on the amount of resources that are required to store, process, and analyze the data. Using encoding, compression, indexes, partitioning, and similar tools we can make this more efficient and reduce the overall environmental impact of our analytics workloads.

**How can your organization reduce the
resources required to store, process, and analyze your
organization’s data in a sustainable manner?**

Reducing data that a database system scans to return a result is an eﬃcient way in reducing your organization’s analytics environmental impact. This approach requires less resources to scan the disk to retrieve the information to service the request, and reduces the amount of provisioned storage required to service the workload. There are diﬀerent methods that database engines use to optimize the amount of information scanned, such as partitioning, bucketing, and sorting.

## Suggestion 15.5.1 – Implement an efficient partitioning strategy for your data lake

Partitioning plays a crucial role when optimizing data sets for
Amazon Athena or Amazon Redshift Spectrum. By partitioning a data set, you can reduce the amount of data scanned by queries dramatically. This reduces the amount of compute power needed, and therefore the environmental impact.

When implementing a partitioning scheme for your data model, work backwards from your queries and identify the properties that would reduce the amount of data scanned the most. For example, it is common to partition data sets by date. Data sets tend to grow over time, and queries tend to look at specific windows of time, such as the last week, or last month.

For more details, refer to the following information:

- Amazon S3 and Amazon Athena:
  [Partitioning and bucketing in Athena](../../../athena/latest/ug/ctas-partitioning-and-bucketing.md "../../../athena/latest/ug/ctas-partitioning-and-bucketing.md")
- Amazon Athena:
  [Partitioning
  data in Amazon Athena](../../../athena/latest/ug/partitions.md "../../../athena/latest/ug/partitions.md")

## Suggestion 15.5.2 – Configure and sort distribution keys on your Amazon Redshift tables

Amazon Redshift sort keys determine the order in which
rows in a table are stored on the disk. When you query a data set in Redshift, it can leverage the sort order of the data to avoid reading blocks that are outside of the range of values you are looking for. By reading fewer blocks of data, this approach can result in a reduction of compute resources required.

For more details, refer to the following information:

- Amazon Redshift:
  [Choose
  the best sort key](../../../redshift/latest/dg/c_best-practices-sort-key.md "../../../redshift/latest/dg/c_best-practices-sort-key.md")

In Amazon Redshift, the distribution key, or distkey, determines how data is distributed between the nodes in a cluster. Choosing the right distribution keys can improve the performance of common analytical operations like joins and aggregations.

For more details, refer to the following information:

- Amazon Redshift:
  [Automate
  your Amazon Redshift performance tuning with automatic
  table optimization](https://aws.amazon.com/blogs/big-data/automate-your-amazon-redshift-performance-tuning-with-automatic-table-optimization/ "https://aws.amazon.com/blogs/big-data/automate-your-amazon-redshift-performance-tuning-with-automatic-table-optimization/")
- Amazon Redshift:
  [Distribution
  styles](../../../redshift/latest/dg/c_choosing_dist_sort.md "../../../redshift/latest/dg/c_choosing_dist_sort.md")

## Suggestion 15.5.3 – Enable results and query plan caching

Computing the same result over and over again is wasteful. Query engines and data warehouses often support result caching, and/or query plan caching. By enabling these you can reduce the overall amount of compute power needed for your analytics workload by eliminating recomputing results and/or query plans when the data set hasn’t changed. This saves on compute resource and reduce the environmental impact.

For more details, refer to the following information:

- Amazon Redshift:
  [Performance
  optimization](../../../redshift/latest/dg/c_challenges_achieving_high_performance_queries.md "../../../redshift/latest/dg/c_challenges_achieving_high_performance_queries.md")
- Amazon Athena: [Query result reuse](../../../athena/latest/ug/reusing-query-results.md "../../../athena/latest/ug/reusing-query-results.md")

## Suggestion 15.5.4 – Enable data compression to reduce storage resources

Your organization should consider compressing data in both
object stores, such as Amazon S3, and if supported, in
your organization’s database systems. By compressing data,
your organization is reducing the amount of storage and
networking resources required for the workload. Database
systems can decompress the data at a rate that is almost
unnoticeable to the end user or application. As the data
is compressed and then decompressed, this will also reduce
the retrieval time of the database engine to fetch all the
data from the storage array leading to a potential
reduction in compute resources.

For more details, refer to the following information:

- **Amazon Redshift compression
  and encoding:**
  [Amazon Redshift Engineering’s Advanced Table Design Playbook:
  Compression Encodings](https://aws.amazon.com/blogs/big-data/amazon-redshift-engineerings-advanced-table-design-playbook-compression-encodings/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-engineerings-advanced-table-design-playbook-compression-encodings/")
- **Amazon Redshift file
  compression parameter:**
  [File
  compression parameters](../../../redshift/latest/dg/copy-parameters-file-compression.md "../../../redshift/latest/dg/copy-parameters-file-compression.md")
- Amazon Redshift
  Compression:
  [Compression
  encodings](../../../redshift/latest/dg/c_Compression_encodings.md "../../../redshift/latest/dg/c_Compression_encodings.md")
- Amazon DynamoDB
  Compression:
  [Using
  data compression](../../../amazondynamodb/latest/developerguide/EMRforDynamoDB.CopyingData.md "../../../amazondynamodb/latest/developerguide/EMRforDynamoDB.CopyingData.md")
- Amazon Athena Compression
  Support:
  [Amazon Athena compression support](../../../athena/latest/ug/compression-formats.md "../../../athena/latest/ug/compression-formats.md")

## Suggestion 15.5.5– Use file formats that optimize storage and compute needs

There are many diﬀerent file formats that can be used to store data from the ubiquitous CSV format, through structured formats like JSON, and data lake-optimized formats like Parquet – each is designed to overcome speciﬁc technical challenges. There is no file format that meets all needs, and different formats have different uses.

For analytical workloads, columnar file formats like Parquet and ORC often perform better overall. They achieve higher compression rates, and help query engines scan less data. Through reduced storage and compute needs they can help reduce the environmental impact of your workload.

More information on how to choose the right format can be found in [Choose the best-performing file format and partitioning](design-principle-10.md "design-principle-10.md").

## Suggestion 15.5.6– Avoid using unnecessary operations in queries, use approximations where possible, and pre-compute commonly used aggregates and joins

Consider the computational requirements of the operations you use when writing queries. For example, think about how the result gets consumed. For example, avoid adding an ORDER BY clause unless the result strictly needs to be ordered.

Many compute-intensive operations can be replaced by approximations. Modern query engines and data warehouses, like Amazon Athena and Amazon Redshift, have functions that can calculate approximate distinct counts, approximate percentiles, and similar analytical functions. These often require much less compute power to run, which can lower the environmental impact of your analytical workload.

Consider pre-computing operations. When you notice that the complexity of your queries increase, or that many queries include the same joins, aggregates, or other compute intensive operations, this can be a sign that you should pre-compute these. Depending on your platform this can be in the form of adding steps to your data transformation pipeline, or by introducing a materialized view.
