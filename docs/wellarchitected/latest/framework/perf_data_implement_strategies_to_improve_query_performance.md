# PERF03-BP04 Implement strategies to improve query performance

in data store

Implement strategies to optimize data and improve data query to
enable more scalability and efficient performance for your workload.

**Common anti-patterns:**

- You do not partition data in your data store.
- You store data in only one file format in your data store.
- You do not use indexes in your data store.

**Benefits of establishing this best
practice:** Optimizing data and query performance
results in more efficiency, lower cost, and improved user
experience.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Data optimization and query tuning are critical aspects of performance efficiency in a data store, as they impact the performance and responsiveness of the entire cloud workload. Unoptimized queries can result in greater resource usage and bottlenecks, which reduce the overall efficiency of a data store.

Data optimization includes several techniques to ensure efficient data storage and access. This also help to improve the query performance in a data store. Key strategies include data partitioning, data compression, and data denormalization, which help data to be optimized for both storage and access.

### Implementation steps

- Understand and analyze the critical data queries which are
  performed in your data store.
- Identify the slow-running queries in your data store and use query
  plans to understand their current state.
  - [Analyzing
    the query plan in Amazon Redshift](../../../redshift/latest/dg/c-analyzing-the-query-plan.md "../../../redshift/latest/dg/c-analyzing-the-query-plan.md")
  - [Using
    EXPLAIN and EXPLAIN ANALYZE in Athena](../../../athena/latest/ug/athena-explain-statement.md "../../../athena/latest/ug/athena-explain-statement.md")

- Implement strategies to improve the query performance. Some
  of the key strategies include:
  - Using a [columnar file format](../../../athena/latest/ug/columnar-storage.md "../../../athena/latest/ug/columnar-storage.md") (like Parquet or ORC).
  - Compressing data in the data store to reduce storage space and I/O operation.
  - Data partitioning to split data into smaller parts and
    reduce data scanning time.
    - [Partitioning data in Athena](../../../athena/latest/ug/partitions.md "../../../athena/latest/ug/partitions.md")
    - [Partitions and data distribution](../../../amazondynamodb/latest/developerguide/HowItWorks.md "../../../amazondynamodb/latest/developerguide/HowItWorks.md")

  - Data indexing on the common columns in the query.
  - Use materialized views for frequent queries.
    - [Understanding materialized views](../../../prescriptive-guidance/latest/materialized-views-redshift/understanding-materialized-views.md "../../../prescriptive-guidance/latest/materialized-views-redshift/understanding-materialized-views.md")
    - [Creating materialized views in Amazon Redshift](../../../redshift/latest/dg/materialized-view-overview.md "../../../redshift/latest/dg/materialized-view-overview.md")

  - Choose the right join operation for the query. When you join two tables, specify the larger table on the left side of join and the smaller table on the right side of the join.
  - Distributed caching solution to improve latency and reduce
    the number of database I/O operation.
  - Regular maintenance such as [vacuuming](../../../prescriptive-guidance/latest/postgresql-maintenance-rds-aurora/autovacuum.md "../../../prescriptive-guidance/latest/postgresql-maintenance-rds-aurora/autovacuum.md"), reindexing, and [running statistics](../../../redshift/latest/dg/t_Analyzing_tables.md "../../../redshift/latest/dg/t_Analyzing_tables.md").

- Experiment and test strategies in a non-production
  environment.

## Resources

**Related documents:**

- [Amazon Aurora best practices](../../../AmazonRDS/latest/UserGuide/Aurora.md "../../../AmazonRDS/latest/UserGuide/Aurora.md")
- [Amazon Redshift performance](../../../redshift/latest/dg/c_challenges_achieving_high_performance_queries.md "../../../redshift/latest/dg/c_challenges_achieving_high_performance_queries.md")
- [Amazon Athena top 10 performance tips](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/?ref=wellarchitected "https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/?ref=wellarchitected")
- [AWS Database Caching](https://aws.amazon.com/caching/database-caching/?ref=wellarchitected "https://aws.amazon.com/caching/database-caching/?ref=wellarchitected")
- [Best
  Practices for Implementing Amazon ElastiCache](../../../AmazonElastiCache/latest/UserGuide/BestPractices.md "../../../AmazonElastiCache/latest/UserGuide/BestPractices.md")
- [Partitioning
  data in Athena](../../../athena/latest/ug/partitions.md "../../../athena/latest/ug/partitions.md")

**Related videos:**

- [AWS re:Invent 2023 - AWS storage cost-optimization best practices](https://www.youtube.com/watch?v=8LVKNHcA6RY "https://www.youtube.com/watch?v=8LVKNHcA6RY")
- [AWS re:Invent 2022 - Performance monitoring with Amazon RDS and Aurora, featuring Autodesk](https://www.youtube.com/watch?v=wokRbwK4YLo "https://www.youtube.com/watch?v=wokRbwK4YLo")
- [Optimize
  Amazon Athena Queries with New Query Analysis Tools](https://www.youtube.com/watch?v=7JUyTqglmNU&ab_channel=AmazonWebServices "https://www.youtube.com/watch?v=7JUyTqglmNU&ab_channel=AmazonWebServices")

**Related examples:**

- [AWS Purpose Built Databases Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US")
