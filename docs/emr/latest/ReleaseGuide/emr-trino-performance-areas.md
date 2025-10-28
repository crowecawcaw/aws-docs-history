# Key areas of focus for performance improvement

Trino maximizes query parallelism and memory optimization. This architecture provides flexibility by enabling it to query multiple, varied
data sources while efficiently scaling. Key areas of performance improvement in Trino include those listed below.

## Memory optimization

Memory management in Trino is critical for achieving high performance and
stability, especially when you run large, complex queries. Trino uses a distributed memory model. In this model, memory is allocated across worker nodes for processing
tasks, aggregations, joins, and other operations. The following list introduces a collection of these settings:

- **query.max-memory** – Sets the maximum memory available for a single query across the entire
  cluster. This is a hard limit; if a query exceeds this memory, it will fail.
- **query.max-memory-per-node** – Defines the maximum memory a query can consume on each worker
  node. Setting this ensures no single query monopolizes resources on any worker.
- **JVM Heap Size** – Configured at the JVM level, it sets the maximum heap size for the Trino server
  process on each node. This value should generally be larger than the memory-related configurations (this is the sum
  of **query.max-memory-per-node** and **memory.heap-headroom-per-node**) in
  Trino to avoid the system running out of memory at the JVM level.
- **memory.heap-headroom-per-node** – Specifies a buffer amount of memory to leave out of the JVM heap size for non-query operations. This
  is crucial for ensuring enough overhead for internal operations and garbage collection.

## Dynamic Filtering

Dynamic filtering in Trino is an optimization technique that improves
query performance by reducing the amount of data processed, particularly during joins. It dynamically applies filter conditions to limit the
data scanned by one side of a join, based on the data seen on the other side, which is especially useful in queries where one side of the join
is highly selective (meaning that it contains a small subset of data). It is enabled by default on Amazon EMR. The following is an example query:

```
SELECT orders.order_id, orders.total_amount
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
WHERE customers.country = 'France';
```

Without dynamic filtering, Trino scans the entire orders table in a join, even though only a small subset of customers (those from France) is
relevant. This approach reads all rows in the **orders** table, resulting in high I/O and processing costs. With dynamic filtering, Trino initially scans the
smaller **customers** table, retrieves customer_id values for only customers from France, and then applies this subset as a filter on
orders. This means only relevant rows from **orders** — those with a customer_id matching the filtered subset — are scanned, significantly
reducing the records processed.

## Spill to Disk

In Trino, disk spilling allows intermediate query results to be offloaded to disk, enabling memory-intensive queries to complete,
even if they exceed memory limits set by `query_max_memory` or `query_max_memory_per_node`. By default, Trino enforces these limits to ensure
fair memory allocation and to prevent cluster deadlock. However, when a large query surpasses these limits, it risks termination. Disk spilling addresses
this by using `revocable memory`, allowing a query to borrow additional memory that can be revoked if resources are needed elsewhere. When memory is
revoked, intermediate data spills to disk, enabling queries to continue processing without exceeding memory limits. Please note
that a query that is forced to spill to disk may have longer execution time, hence it is disabled by default. To enable spill
on Amazon EMR, use following configuration:

- `spill-enabled=true` – Enables disk spilling when memory usage exceeds available thresholds.
- `spill-paths` – Defines the directories where spilled data is stored, `spill-paths=/mnt/spill`.
