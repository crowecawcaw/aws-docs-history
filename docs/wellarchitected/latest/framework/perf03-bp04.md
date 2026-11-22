

# PERF03-BP04 Implement strategies to improve query performance in data store

 To keep a data store efficient and scalable as demand grows, optimize both data layout and query execution. 

 **Desired outcome:** 
+  Your queries are optimized for your workload's access patterns. 
+  Your data layout, including partitioning, file format, and indexing, supports the queries you run most. 
+  You identify and remediate slow queries using query plans and metrics. 
+  You validate optimization strategies before applying them in production. 

 **Common anti-patterns:** 
+  Teams do not partition data in the data store. 
+  Teams store data in a single file format regardless of the query pattern. 
+  Teams run without indexes, or maintain indexes that collide too often. 
+  Teams do not use query result caching where it would help. 
+  Teams write broad queries, such as selecting all columns or filtering inefficiently. 
+  Teams distribute tables without regard to join patterns, which moves data between nodes on every query. 

 **Benefits of establishing this best practice:** 
+  Queries return faster, which improves user experience. 
+  Resource use and cost fall because queries scan less data. 
+  The data store scales further before it needs larger instances. 
+  Bottlenecks from contention and full scans become rare. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Query performance depends on data layout and query execution. Data layout covers partitioning, file format, compression, and denormalization. Query execution covers indexes, join strategy, materialized views, and caching. Use the query plan to see where time and I/O go, then decide which to tune. 

 Data layout trade-offs depend on whether the workload is analytical or transactional. Columnar formats, such as Parquet and ORC, read only the columns a query needs, which suits large analytical scans. Row-based formats suit transactional access that touches whole records. Partitioning reduces the data a query scans. Denormalization speeds frequent joins, but it duplicates data and complicates writes, so use it deliberately for hot paths. 

 Indexes speed reads on the columns a query filters, but each index slows writes and adds maintenance overhead. Materialized views precompute a frequent query's result. They trade storage and refresh work for fast reads, and help only when the underlying data changes less often than the query runs. For repeated queries against slowly changing data, use query result caching. Weigh cache freshness against the workload's staleness tolerance. 

 Query planners use statistics to choose execution paths. When statistics drift, plans degrade even though nothing else changed. Keep plans accurate with regular maintenance, such as vacuuming, reindexing, and refreshing statistics. Test changes in a non-production environment against representative load before you apply them. AWS provides diagnostic tools, including query plan analysis in [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/c-analyzing-the-query-plan.html), [EXPLAIN and EXPLAIN ANALYZE in Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/athena-explain-statement.html), and query analysis in [Amazon RDS Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DatabaseInsights.html). 

 If your data store distributes data across nodes, choose the distribution key from your most frequent joins. An even distribution avoids skew but can force rows to move between nodes for each join. A key-based distribution keeps matching rows together and avoids that movement, but a key with few distinct values creates skew. In Amazon Redshift, see [distribution styles](https://docs.aws.amazon.com/redshift/latest/dg/c_choosing_dist_sort.html), and check the query plan and skew before you adopt a key. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Analyze your critical queries and access patterns:** Identify the queries that run most often or matter most to users, and document the access patterns behind them. This focuses optimization on the queries that affect performance rather than on every statement. 

1.  **Identify slow queries using query plans:** Find slow-running queries and read their execution plans to see where time and I/O go. 

1.  **Optimize data layout:** Choose a [columnar file format](https://docs.aws.amazon.com/athena/latest/ug/columnar-storage.html) for analytical workloads and a row-based format for transactional ones. Compress data to reduce I/O while monitoring compression ratios, and [partition data](https://docs.aws.amazon.com/athena/latest/ug/partitions.html) by frequently filtered columns while avoiding over-partitioning. For key-value stores, design keys around [partitions and data distribution](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.Partitions.html). 

1.  **Optimize indexes and materialized views:** Index the columns your common queries filter on, monitor index usage, and remove unused indexes that only add write overhead. Use [materialized views](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-overview.html) for frequent queries whose underlying data changes less often than the query runs. 

1.  **Optimize query structure and joins:** Select only the columns a query needs, and write precise filter conditions. When joining tables, choose the join type that fits the requirement. Consider denormalization for tables that are joined on hot paths. 

1.  **Add query result caching:** For repeated queries against slowly changing data, enable result caching with features, such as the [Amazon Athena query result cache](https://docs.aws.amazon.com/athena/latest/ug/) or [Amazon Redshift result caching](https://docs.aws.amazon.com/redshift/latest/dg/), and set freshness limits the workload can tolerate. 

1.  **Run regular maintenance:** Schedule [vacuuming](https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-maintenance-rds-aurora/autovacuum.html), reindexing, and [statistics refresh](https://docs.aws.amazon.com/redshift/latest/dg/t_Analyzing_tables.html) so the query planner works from accurate information and continues to choose good plans. 

1.  **Test strategies in a non-production environment:** Apply each optimization against representative data and load before promoting it, and confirm the change improves the target queries without harming others. 

1.  **Align the distribution key with join patterns:** Where your data store uses a distribution key, base it on your most frequent joins, and confirm in the query plan that data movement between nodes drops. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF03-BP02 Evaluate available configuration options for data store](perf03-bp02.md) 
+  [PERF03-BP05 Implement data access patterns that utilize caching](perf03-bp05.md) 
+  [PERF03-BP03 Collect and record data store performance metrics](perf03-bp03.md) 

 **Related documents:** 
+  [Amazon Aurora best practices](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.BestPractices.html) 
+  [Amazon Redshift performance](https://docs.aws.amazon.com/redshift/latest/dg/c_challenges_achieving_high_performance_queries.html) 
+  [Amazon RDS for PostgreSQL query performance guidelines](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.html#CHAP_BestPractices.PostgreSQL) 
+  [Amazon DynamoDB best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html) 
+  [Amazon Athena performance guide](https://docs.aws.amazon.com/athena/latest/ug/) 
+  [Understanding materialized views](https://docs.aws.amazon.com/prescriptive-guidance/latest/materialized-views-redshift/understanding-materialized-views.html) 
+  [Best practices for implementing Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html) 
+  [AWS database caching](https://aws.amazon.com/caching/database-caching/) 

 **Related workshops:** 
+  [AWS purpose-built databases workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US) 