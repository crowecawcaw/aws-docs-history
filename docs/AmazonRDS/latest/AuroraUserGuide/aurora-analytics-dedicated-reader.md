

# Using a dedicated reader instance for analytics
<a name="aurora-analytics-dedicated-reader"></a>

For analytics-heavy workloads, run your foreign table queries on a dedicated Aurora reader instance so they do not interrupt the OLTP workload on your writer. When you set up this reader, consider the following.
+ **Adjust `shared_buffers`**: Queries against foreign tables do not use `shared_buffers`, so on the reader you can reduce `shared_buffers` and increase `query_mem` to make more memory available per query.
+ **Failover priority**: Because the reader is tuned for analytics rather than transactional traffic, it is a poor writer if it is promoted during a failover. Assign it promotion tier 15 (the lowest priority) so Aurora promotes a transaction-tuned reader first. Aurora can still promote it as a last resort if no other instance is available.
+ **Instance endpoint**: Connect analytics clients to the reader's instance endpoint or a custom endpoint rather than the cluster reader endpoint, which load-balances across all readers and sends foreign table queries to instances tuned for other workloads.

## Managing long-running queries on readers
<a name="aurora-analytics-long-running-readers"></a>

Long-running foreign table queries on a reader affect both the writer and the reader.
+ **Impact on the writer**: A long-running foreign table query on a reader holds back dead tuple cleanup on the writer. While the query runs, the writer cannot reclaim the dead tuples that its vacuum normally removes, so they accumulate and degrade performance on the writer. Because foreign table queries can run for minutes or hours, this effect is more pronounced on an analytics reader.
+ **Impact on the reader**: A foreign table query also accesses local catalog tables and might join with regular PostgreSQL tables, so it pins page buffers on the reader like any other query. While those buffers are pinned, DDL or vacuum operations on the writer can trigger replication conflicts (snapshot, lock, or buffer pin) that cancel the query or restart the reader. Because foreign table queries tend to run longer, they are more likely to encounter these conflicts.

To limit this effect, set `statement_timeout` on the analytics reader to bound how long a single query can run, and monitor `oldest_reader_feedback_xid_age` on the writer in Database Insights or Amazon CloudWatch. For a guided version of this diagnosis and how to stop the blocking query, see [Resolving identifiable vacuum blockers in Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Maintenance.html) in the *Amazon Aurora User Guide*.