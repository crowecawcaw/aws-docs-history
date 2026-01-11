# Amazon Aurora Parallel Query

Amazon Aurora Parallel Query is a feature of the Amazon Aurora database that provides faster analytical queries over your current data, without having to copy the data into a separate system. It can speed up queries by up to two orders of magnitude, while maintaining high throughput for your core transactional workload.

While some databases can parallelize query processing across CPUs in one or a handful of servers, Parallel Query takes advantage of Aurora unique architecture to push down and parallelize query processing across thousands of CPUs in the Aurora storage layer. By offloading analytical query processing to the Aurora storage layer, Parallel Query reduces network, CPU, and buffer pool contention with the transactional workload.

## Features

**Accelerate your analytical queries**

In a traditional database, running analytical queries directly on the database means accepting slower query performance and risking a slowdown of your transactional workload, even when running light queries. Queries can run for several minutes to hours, depending on the size of the tables and database server instances. Queries are also slowed down by network latency, since the storage layer may have to transfer entire tables to the database server for processing.

With Amazon Aurora Parallel Query, query processing is pushed down to the Aurora storage layer. The query gains a large amount of computing power, and it needs to transfer far less data over the network. In the meantime, the Amazon Aurora database instance can continue serving transactions with much less interruption. This way, you can run transactional and analytical workloads alongside each other in the same Aurora database, while maintaining high performance.

**Query on fresh data**

Many analytical workloads require both fresh data and good query performance. For example, operational systems such as network monitoring, cyber-security or fraud detection rely on fresh, real-time data from a transactional database, and can’t wait for it to be extracted to a analytics system.

By running your queries in the same database that you use for transaction processing, without degrading transaction performance, Amazon Aurora Parallel Query enables smarter operational decisions with no additional software and no changes to your queries.

## Benefits of Using Parallel Query

`AURlong` Parallel Query feature provides the following benefits:

- Improved I/O performance, due to parallelizing physical read requests across multiple storage nodes.
- Reduced network traffic. Amazon Aurora doesn’t transmit entire data pages from storage nodes to the head node and then filter out unnecessary rows and columns afterward. Instead, Aurora transmits compact tuples containing only the column values needed for the result set.
- Reduced CPU usage on the head node, due to pushing down function processing, row filtering, and column projection for the WHERE clause.
- Reduced memory pressure on the buffer pool. The pages processed by Parallel Query aren’t added to the buffer pool. This approach reduces the chance of a data-intensive scan evicting frequently used data from the buffer pool.
- Potentially reduced data duplication in your extract, transform, and load (ETL) pipeline, by making it practical to perform long-running analytic queries on existing data.

## Important notes

Consider the following when using the `AURlong` Parallel Query feature:

- **Table formats** — The table row format must be `COMPACT`; partitioned tables aren’t supported.
- **Data types** — The `TEXT`, `BLOB`, and `GEOMETRY` data types aren’t supported.
- **DDL** — The table can’t have any pending fast online DDL operations.
- **Cost** — You can make use of Parallel Query at no extra charge. However, because it makes direct access to storage, there is a possibility that your IO cost will increase.

For more information, see [Amazon Aurora Parallel Query](https://aws.amazon.com/rds/aurora/parallel-query/ "https://aws.amazon.com/rds/aurora/parallel-query/").
