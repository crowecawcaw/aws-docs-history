

# How billing works in Aurora DSQL
<a name="billing-metering"></a>

With Amazon Aurora DSQL, you only pay for what you use with no upfront costs. This section explains how Aurora DSQL meters your database activity and translates it into charges on your AWS bill. For current pricing by Region, see the [Aurora DSQL pricing page](https://aws.amazon.com/rds/aurora/dsql/pricing/).

**Topics**
+ [How metering works](#billing-how-metering-works)
+ [DPU component metering explained](#billing-dpu-components)
+ [Multi-Region billing](#billing-multiregion-write-dpu)
+ [Monitoring DPU usage with CloudWatch](#billing-cloudwatch-monitoring)
+ [Using EXPLAIN ANALYZE VERBOSE for cost awareness](#billing-explain-analyze)
+ [Cost estimation best practices](#billing-best-practices)

## How metering works
<a name="billing-how-metering-works"></a>

Unlike traditional databases that charge for provisioned capacity, Aurora DSQL charges only for actual work performed. Aurora DSQL meters two primary components: database activity, measured in Distributed Processing Units (DPUs), and storage, measured in GiB-month.

DPUs measure how much work the system does to run your SQL workload and are comprised of three components for single-Region clusters: Compute DPUs, Read DPUs, and Write DPUs. Multi-Region clusters incur an additional MultiRegion Write DPU component. For more information about Multi-Region billing, see [Multi-Region billing](#billing-multiregion-write-dpu). Clusters with change data capture (CDC) enabled incur an additional Stream DPU component. For more information about CDC billing, see [Stream DPU](#billing-stream-dpu).

The following table summarizes the components that Aurora DSQL uses to meter your database activity. On your bill, you see only two line items: one for storage and one for DPU, which is the sum of each of the individual components.


| Metering unit | Activity type | Measurement | 
| --- | --- | --- | 
| Compute DPU | Query processing | CPU time | 
| Read DPU | Read data from your database | Bytes read from storage | 
| Write DPU | Write data to your database | Bytes written to storage | 
| Stream DPU | CDC streaming (when enabled) | Bytes streamed | 
| Storage | Table storage | GiB-month | 

## DPU component metering explained
<a name="billing-dpu-components"></a>

For every transaction, Aurora DSQL calculates the total DPU as the sum of three components: Compute DPU, Read DPU, and Write DPU. The following sections explain how Aurora DSQL meters each component.

```
Total DPU = ComputeDPU + ReadDPU + WriteDPU
```

### ComputeDPU
<a name="billing-compute-dpu"></a>

Compute DPUs are measured using the total processing time spent executing your query, including joins, functions, aggregations, sorting, and query planning. Because parts of your query can be processed in parallel, the Compute DPU reflects the sum of all processing time — not the wall-clock time of the query.

The following formula summarizes how to calculate Compute DPUs:

```
ComputeDPU = Total Compute time (in seconds)
```

### WriteDPU
<a name="billing-write-dpu"></a>

For every transaction, Aurora DSQL measures Write DPUs by the total bytes written to storage. Write DPUs include the total data written to your base table as well as any secondary indexes. Aurora DSQL bills each row written to your base table and secondary indexes that is smaller than 128 bytes as if it is 128 bytes. Aurora DSQL bills a write transaction that writes less than 1,024 bytes as if it wrote 1,024 bytes.

**Note**  
Write operations also incur ReadDPU charges because Aurora DSQL reads the primary key index to verify uniqueness before writing.

The following formulas show the steps to calculate Write DPUs:

**Step 1: Calculate bytes written**

```
Bytes Written = Sum of max(size of each row, 128 bytes) for all rows written
```

**Step 2: Calculate WriteDPU**

```
WriteDPU = max(Bytes Written, 1024) × 0.00004883
```

### ReadDPU
<a name="billing-read-dpu"></a>

For every transaction, Aurora DSQL measures Read DPUs by the total bytes read from storage. Read DPUs include data read from your base table as well as any secondary indexes.

**Per-partition minimum:** Aurora DSQL measures read bytes per storage partition, not per row. If a read request to a storage partition returns less than 128 bytes, Aurora DSQL rounds it up to 128 bytes. For example, if your query reads from 4 partitions—200 bytes from one partition and 50 bytes from each of the other three—the three 50-byte reads are each rounded up to 128 bytes, resulting in a total of 200 \+ 128 \+ 128 \+ 128 = 584 bytes billed.

**Transaction minimum:** Aurora DSQL bills a read transaction that reads less than 2,048 bytes in total as if it read 2,048 bytes.

The following formulas show the steps to calculate Read DPUs:

**Step 1: Calculate bytes read**

```
Bytes Read = # of rows read × size of each row
```

**Note**  
The actual bytes read depends on how your data is distributed across storage partitions, because the 128-byte per-partition minimum is applied per partition. If all of your row sizes are above 128 bytes, you can simply multiply the number of rows read by the size of each row.

**Step 2: Calculate ReadDPU**

```
ReadDPU = max(Bytes Read, 2048) × 0.00000183105
```

### Stream DPU
<a name="billing-stream-dpu"></a>

Stream DPUs apply only when you enable change data capture (CDC) on your cluster. Aurora DSQL measures Stream DPUs by the total bytes streamed to your target Amazon Kinesis Data Streams stream. When there are no changes to stream, you incur no Stream DPU charges.

The following formula shows how to calculate Stream DPUs:

```
StreamDPU = Bytes Streamed × 0.0000023283
```

Aurora DSQL bills Stream DPUs at the same rate as all other DPU components. For more information about CDC streams, see [Change data capture streams](cdc-streams.md).

### Billing examples
<a name="billing-dpu-examples"></a>

The following examples demonstrate how Aurora DSQL calculates DPUs for common operations. Cost values in these examples use the us-east-1 Region price. For pricing in other Regions, see the [Aurora DSQL pricing page](https://aws.amazon.com/rds/aurora/dsql/pricing/).

#### Example: Simple point lookup (read)
<a name="billing-read-dpu-example"></a>

This example demonstrates a point lookup ReadDPU calculation where the transaction minimum applies.

**Schema:**

```
CREATE TABLE orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id VARCHAR(50) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2),
    status VARCHAR(20)
);
-- Average row size: ~100 bytes
```

**Query:**

```
SELECT * FROM orders WHERE customer_id = 'cust-12345';
```

**Scenario:** The query returns 5 rows, each approximately 100 bytes. Assuming all rows reside in one storage partition, the total bytes read is 5 × 100 = 500 bytes. Since 500 bytes exceeds the 128-byte per-partition minimum, no per-partition minimum applies.

**Calculate ReadDPU:**

```
ReadDPU = max(500, 2048) × 0.00000183105 = 2048 × 0.00000183105 = 0.00375
```

The transaction minimum of 2,048 bytes applies since 500 < 2,048.

**Total transaction cost:**

Assuming query execution time of 3 ms (0.003 seconds):

```
ComputeDPU: 0.003
ReadDPU:    0.00375
WriteDPU:   0.0
-------------------
Total DPU:  0.00675
```

#### Example: Filtered range scan (read)
<a name="billing-read-dpu-example-filtered"></a>

**Schema:**

```
CREATE TABLE orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id VARCHAR(50) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2),
    status VARCHAR(20)
);
-- Average row size: ~100 bytes
-- Table contains 100 orders for customer 'cust-12345'
```

**Query:**

```
SELECT * FROM orders
WHERE customer_id = 'cust-12345'
  AND total_amount > 500.00;
```

**Scenario:** The query scans 100 rows for customer 'cust-12345', but the `total_amount > 500.00` filter reduces the result to only 10 rows returned. Aurora DSQL bills for all 100 rows scanned. Assuming all rows reside in one storage partition, the total bytes read is 100 × 100 = 10,000 bytes.

**Calculate ReadDPU:**

```
ReadDPU = max(10000, 2048) × 0.00000183105 = 10000 × 0.00000183105 = 0.01831
```

Since 10,000 bytes exceeds the 2,048-byte transaction minimum, the actual bytes read are used.

**Total transaction cost:**

Assuming query execution time of 8 ms (0.008 seconds):

```
ComputeDPU: 0.008
ReadDPU:    0.01831
WriteDPU:   0.0
-------------------
Total DPU:  0.02631
```

**Important**  
To minimize ReadDPU costs, design queries and indexes to scan only the rows you need. In this example, adding an index on `(customer_id, total_amount)` could allow the query to scan fewer rows.

#### Example: Single insert (read and write)
<a name="billing-write-dpu-example-single"></a>

**Schema:**

```
CREATE TABLE orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id VARCHAR(50) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2),
    status VARCHAR(20)
);
-- Average row size: ~100 bytes
```

**Query:**

```
INSERT INTO orders (customer_id, total_amount, status)
VALUES ('cust-67890', 150.00, 'pending');
```

**Scenario:** Insert 1 row, approximately 100 bytes.

**WriteDPU calculation:**

*Step 1 - Calculate bytes written:*

```
1 row × max(100 bytes, 128 bytes) = 1 × 128 = 128 bytes
```

*Step 2 - Calculate WriteDPU:*

```
WriteDPU = max(128, 1024) × 0.00004883 = 1024 × 0.00004883 = 0.05
```

The transaction minimum of 1,024 bytes applies since 128 < 1,024.

**ReadDPU (primary key check):**

Aurora DSQL reads the primary key index to verify uniqueness before writing. This incurs the transaction minimum read charge.

```
ReadDPU = 0.00375 (transaction minimum)
```

**Total transaction cost:**

Assuming query execution time of 8 ms (0.008 seconds):

```
ComputeDPU: 0.008
ReadDPU:    0.00375
WriteDPU:   0.05
-------------------
Total DPU:  0.06175
```

#### Example: Bulk insert (read and write)
<a name="billing-write-dpu-example-bulk"></a>

**Schema:**

```
CREATE TABLE orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id VARCHAR(50) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2),
    status VARCHAR(20)
);
-- Average row size: ~100 bytes
```

**Query:**

```
INSERT INTO orders (customer_id, total_amount, status)
VALUES
    ('cust-001', 100.00, 'pending'),
    ('cust-002', 150.00, 'pending'),
    ... -- 100 rows total
    ('cust-100', 200.00, 'pending');
```

**Scenario:** Insert 100 rows, each approximately 100 bytes.

**WriteDPU calculation:**

*Step 1 - Calculate bytes written:*

```
100 rows × max(100 bytes, 128 bytes) = 100 × 128 = 12,800 bytes
```

*Step 2 - Calculate WriteDPU:*

```
WriteDPU = max(12800, 1024) × 0.00004883 = 12800 × 0.00004883 = 0.625
```

**ReadDPU (primary key checks):**

Aurora DSQL reads the primary key index for each row to verify uniqueness. Assuming all 100 key lookups reside in one storage partition, the total bytes read is 100 × 16 bytes (UUID) = 1,600 bytes:

```
ReadDPU = max(1600, 2048) × 0.00000183105 = 2048 × 0.00000183105 = 0.00375
```

The transaction minimum of 2,048 bytes applies since 1,600 < 2,048.

**Total transaction cost:**

Assuming query execution time of 80 ms (0.08 seconds):

```
ComputeDPU: 0.08
ReadDPU:    0.00375
WriteDPU:   0.625
-------------------
Total DPU:  0.70875
```

## Multi-Region billing
<a name="billing-multiregion-write-dpu"></a>

Multi-Region clusters incur an additional MultiRegion Write DPU component on top of the standard Compute, Read, and Write DPUs. This section applies only to multi-Region clusters. Single-Region clusters do not incur this charge.

Multi-Region Write DPUs measure the total bytes written to the peered Region. Aurora DSQL charges this DPU in the Region where the write originated, not in the peered Region. For example, in a two-active Region and Witness peering configuration, Aurora DSQL charges the write DPU of the originating transaction for each active peered Region when calculating the `MultiRegionWriteDPU`. This means a transaction that accrues 8 `WriteDPU` incurs an additional 8 `MultiRegionWriteDPU` for this configuration. This is 8 for the originating Region, 8 for the peered Region, and no charge for the Witness Region. Aurora DSQL bills all charges to the Region that originated the transaction. 

All clusters in the multi-Region configuration incur storage size charge. Because Aurora DSQL synchronously replicates the data you write to the peered Region, the storage size charge applies to all clusters in the multi-Region configuration individually. This also applies to clusters in **Pending Delete** state. For more information about the **Pending Delete** state, see the [Aurora DSQL cluster lifecycle](cluster-lifecycle.md#dsql-cluster-statuses.title) page.

```
MultiRegionWriteDPU = WriteDPU
```

## Monitoring DPU usage with CloudWatch
<a name="billing-cloudwatch-monitoring"></a>

Aurora DSQL publishes usage metrics to Amazon CloudWatch, allowing you to monitor consumption in near real-time.

### Available DPU metrics
<a name="billing-available-dpu-metrics"></a>


**DPU metrics**  

| CloudWatch metric | Description | Dimension | 
| --- | --- | --- | 
| WriteDPU | Write usage component | ClusterId | 
| ReadDPU | Read usage component | ClusterId | 
| ComputeDPU | Query processing component | ClusterId | 
| MultiRegionWriteDPU | Multi-Region replication (multi-Region clusters only) | ClusterId | 
| StreamDPU | CDC streaming (clusters with CDC enabled only) | ClusterId, StreamId | 
| TotalDPU | Sum of all DPU components | ClusterId | 

### Viewing DPU metrics
<a name="billing-viewing-dpu-metrics"></a>

**To view DPU metrics in CloudWatch**

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch).

1. Navigate to **Metrics**, then **AuroraDSQL**, then **ClusterId**.

1. Select your cluster and the DPU metrics you want to monitor.

**Tip**  
Use the **Sum** statistic for DPU metrics to see total usage over a time period. Add the **LAST** label to see the most recent value.

### Additional observability metrics
<a name="billing-observability-metrics"></a>

For a complete list of Aurora DSQL metrics and monitoring capabilities, see [Monitoring and logging for Aurora DSQL](monitoring-overview.md).


**Observability metrics**  

| Metric | Description | 
| --- | --- | 
| ClusterStorageSize | Current storage size in bytes | 
| TotalTransactions | Total transactions executed | 
| ReadOnlyTransactions | Read-only transactions executed | 
| QueryTimeouts | Queries that exceeded time limit | 
| OccConflicts | Transactions aborted due to OCC conflicts | 
| BytesWritten | Raw bytes written to storage | 
| BytesRead | Raw bytes read from storage | 

## Using EXPLAIN ANALYZE VERBOSE for cost awareness
<a name="billing-explain-analyze"></a>

Aurora DSQL extends `EXPLAIN ANALYZE VERBOSE` to include a statement-level DPU usage estimate at the end of the output. This provides immediate visibility into query cost, helping you identify workload cost drivers, tune query performance, and better forecast resource usage.

**Note**  
You must use `EXPLAIN ANALYZE VERBOSE` (with VERBOSE) to see DPU estimates. A plain `EXPLAIN ANALYZE` without VERBOSE does not show DPU information.

### Example 1: SELECT query
<a name="billing-explain-analyze-select"></a>

```
EXPLAIN ANALYZE VERBOSE SELECT * FROM test_table;
```

```
QUERY PLAN
----------------------------------------------------
Index Only Scan using test_table_pkey on public.test_table  (cost=125100.05..171100.05 rows=1000000 width=36) (actual time=2.973..4.482 rows=120 loops=1)
  Output: id, context
  -> Storage Scan on test_table_pkey (cost=125100.05..171100.05 rows=1000000 width=36) (actual rows=120 loops=1)
      Projections: id, context
      -> B-Tree Scan on test_table_pkey (cost=125100.05..171100.05 rows=1000000 width=36) (actual rows=120 loops=1)
Query Identifier: qymgw1m77maoe
Planning Time: 11.415 ms
Execution Time: 4.528 ms
Statement DPU Estimate:
  Compute: 0.01607 DPU
  Read: 0.04312 DPU
  Write: 0.00000 DPU
  Total: 0.05919 DPU
```

In this example, the SELECT statement performs an index-only scan, so most of the cost comes from Read DPU (0.04312), representing the data retrieved from storage and Compute DPU (0.01607), which reflects the compute resources used to process and return the results. There is no Write DPU since the query does not modify data. The total DPU (0.05919) is the sum of Compute \+ Read \+ Write.

### Example 2: INSERT query
<a name="billing-explain-analyze-insert"></a>

```
EXPLAIN ANALYZE VERBOSE INSERT INTO test_table VALUES (1, 'name1'), (2, 'name2'), (3, 'name3');
```

```
QUERY PLAN
----------------------------------------------------
Insert on public.test_table  (cost=0.00..0.04 rows=0 width=0) (actual time=0.055..0.056 rows=0 loops=1)
  ->  Values Scan on "*VALUES*"  (cost=0.00..0.04 rows=3 width=122) (actual time=0.003..0.008 rows=3 loops=1)
        Output: "*VALUES*".column1, "*VALUES*".column2
Query Identifier: jtkjkexhjotbo
Planning Time: 0.068 ms
Execution Time: 0.543 ms
Statement DPU Estimate:
  Compute: 0.01550 DPU
  Read: 0.00307 DPU (Transaction minimum: 0.00375)
  Write: 0.01875 DPU (Transaction minimum: 0.05000)
  Total: 0.03732 DPU
```

This statement primarily performs writes, so most of the cost is associated with Write DPU. The Compute DPU (0.01550) represents the work done to process and insert the values. The Read DPU (0.00307) reflects minor system reads (for catalog lookups or index checks).

Notice the transaction minimums shown in parentheses next to Read and Write DPUs. These minimums apply at the transaction level, meaning the total Read or Write DPU for an entire transaction is never less than these values. If you are using `EXPLAIN ANALYZE VERBOSE` to forecast costs and this is the only statement in the transaction, use the transaction minimum values rather than the raw statement estimates. If the transaction contains multiple statements, the minimums apply to the aggregate across all statements. Because `EXPLAIN ANALYZE VERBOSE` reports statement-level estimates while billing applies transaction-level minimums, the values may not exactly match CloudWatch metrics or billing data.

### Using DPU information for optimization
<a name="billing-explain-dpu-optimization"></a>

Per-statement DPU estimates give you a powerful way to optimize queries beyond just execution time. Common use cases include:
+ **Cost awareness:** Understand how expensive a query is relative to others.
+ **Schema optimization:** Compare the impact of indexes or schema changes on both performance and resource efficiency.
+ **Budget planning:** Estimate workload cost based on observed DPU usage.
+ **Query comparison:** Evaluate alternative query approaches by their relative DPU consumption.

### Interpreting DPU information
<a name="billing-explain-dpu-interpreting"></a>

Keep the following best practices in mind when using DPU data from `EXPLAIN ANALYZE VERBOSE`:
+ **Use it directionally:** Treat the reported DPU as a way to understand the *relative* cost of a query rather than an exact match with CloudWatch metrics or billing data. Differences are expected because `EXPLAIN ANALYZE VERBOSE` reports statement-level cost, while CloudWatch aggregates transaction-level activity. CloudWatch also includes background operations (such as asynchronous ANALYZE or compactions) and transaction overhead (`BEGIN`/`COMMIT`) that `EXPLAIN ANALYZE VERBOSE` intentionally excludes.
+ **Test with representative data for proof of concepts:** When running a proof of concept to evaluate costs, ensure your tables contain data volumes and distributions similar to your expected production workload. DPU estimates — whether from `EXPLAIN ANALYZE VERBOSE` or CloudWatch metrics — that are based on empty or sparsely populated tables will not reflect real-world costs.
+ **DPU variability across runs is normal** in distributed systems and does not indicate errors. Factors such as caching, execution plan changes, concurrency, background operations like asynchronous ANALYZE, or shifts in data distribution can all cause the same query to consume different resources from one run to the next.
+ **Batch small operations:** If your workload issues many small statements, consider batching them into larger write operations within a single transaction (modifications must not exceed 10 MB per transaction, though reads are only limited by the 5-minute transaction timeout). This amortizes transaction minimums across more work and produces more meaningful cost estimates.
+ **Use for tuning, not billing:** DPU data in `EXPLAIN ANALYZE VERBOSE` is designed for cost awareness, query tuning, and optimization. It is not a billing-grade metric. Always rely on CloudWatch metrics or monthly billing reports for authoritative cost and usage data.

## Cost estimation best practices
<a name="billing-best-practices"></a>
+ **Monitor before optimizing:** Use CloudWatch metrics to understand your current usage pattern before making optimization decisions. For details, see [Monitoring DPU usage with CloudWatch](#billing-cloudwatch-monitoring).
+ **Focus on transaction efficiency:** Since minimums apply at the transaction level, batch related operations together to amortize minimum charges.
+ **Use EXPLAIN ANALYZE VERBOSE during development:** Run `EXPLAIN ANALYZE VERBOSE` on critical queries during development to understand their cost characteristics. When running a proof of concept to evaluate costs, test against tables with representative data volumes and distributions — estimates based on empty or sparsely populated tables will not reflect production costs. For details, see [Using EXPLAIN ANALYZE VERBOSE for cost awareness](#billing-explain-analyze).
+ **Set CloudWatch alarms:** Create alarms on DPU metrics to get notified of unexpected usage spikes.