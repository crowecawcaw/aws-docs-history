# Best practices for Trino on Amazon EMR

Trino’s architecture is designed for fast, distributed SQL queries on large datasets across multiple data sources, following a coordinator-worker model, where each
component has a specialized role in query execution. There are a few areas or categories you can focus on in order to configure your Amazon EMR cluster running Trino for its best
performance. These include the following:

- Adjusting cluster configuration settings for memory optimization.
- Optimizing settings for data partitioning and data distribution.
- Using dynamic filtering to reduce query-result counts.
  Some of these settings are tuned automatically when you use
  Trino with Amazon EMR. Others can be set manually through the console or through CLI commands. The topics in this section help you configure your
  data and your cluster optimally.

###### Topics

- [Key areas of focus for performance improvement](emr-trino-performance-areas.md "emr-trino-performance-areas.md")
- [Collect and Utilize table statistics](emr-trino-performance-areas-collect-stats.md "emr-trino-performance-areas-collect-stats.md")
- [Common challenges when scaling Trino workloads](emr-trino-common-issues.md "emr-trino-common-issues.md")
