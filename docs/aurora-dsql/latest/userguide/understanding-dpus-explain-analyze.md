# Understanding DPUs in EXPLAIN ANALYZE

Aurora DSQL provides **statement-level** Distributed Processing Unit (DPU) information in `EXPLAIN ANALYZE VERBOSE` plan output, giving you deeper visibility into query cost during development. This section explains what DPUs are and how to interpret them in the `EXPLAIN ANALYZE VERBOSE` output.

## What is a DPU?

A Distributed Processing Unit (DPU) is the normalized measure of work done by Aurora DSQL. It is composed of:

- **ComputeDPU** – Time spent executing SQL queries
- **ReadDPU** – Resources used to read data from storage
- **WriteDPU** - Resources used to write data to storage
- **MultiRegionWriteDPU** – Resources used to replicate writes to peered clusters in multi-Region configurations.

## DPU usage in EXPLAIN ANALYZE VERBOSE

Aurora DSQL extends `EXPLAIN ANALYZE VERBOSE` to include a statement-level DPU usage estimate to the end of the output. This provides immediate visibility into query cost, helping you identify workload cost drivers, tune query performance, and better forecast resource usage.

The following examples show how to interpret the statement-level DPU estimates included in EXPLAIN ANALYZE VERBOSE output.

### Example 1: SELECT Query

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

In this example, the SELECT statement performs an index-only scan, so most of the cost comes from Read DPU (0.04312), representing the data retrieved from storage and Compute DPU (0.01607), which reflects the compute resources used to process and return the results. There is no Write DPU since the query doesn't modify data. The total DPU (0.05919) is the sum of Compute + Read + Write.

### Example 2: INSERT Query

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

Notice the Transaction minimums shown next to Read and Write DPUs. These indicate the baseline per-transaction costs that apply _only when the operation includes reads or writes_. They do not mean that every transaction automatically incurs a 0.00375 Read DPU or 0.05 Write DPU charge. Instead, these minimums are applied at the transaction level during cost aggregation and only if reads or writes occur within that transaction. Because of this difference in scope, statement-level estimates in `EXPLAIN ANALYZE VERBOSE` may not exactly match the transaction-level metrics reported in CloudWatch or billing data.

## Using DPU Information for Optimization

Per-statement DPU estimates give you a powerful way to optimize queries beyond just execution time. Common use cases include:

- **Cost Awareness:** Understand how expensive a query is relative to others.
- **Schema Optimization:** Compare the impact of indexes or schema changes on both performance and resource efficiency.
- **Budget Planning:** Estimate workload cost based on observed DPU usage.
- **Query Comparison:** Evaluate alternative query approaches by their relative DPU consumption.

## Interpreting DPU Information

Keep the following best practices in mind when using DPU data from `EXPLAIN ANALYZE VERBOSE`:

- **Use it directionally:** Treat the reported DPU as a way to understand the _relative_ cost of a query rather than an exact match with CloudWatch metrics or billing data. Differences are expected because `EXPLAIN ANALYZE VERBOSE` reports statement-level cost, while CloudWatch aggregates transaction-level activity. CloudWatch also includes background operations (such as ANALYZE or compactions) and transaction overhead (`BEGIN`/`COMMIT`) that `EXPLAIN ANALYZE VERBOSE` intentionally excludes.
- **DPU variability across runs is normal** in distributed systems and does not indicate errors. Factors such as caching, execution plan changes, concurrency, or shifts in data distribution can all cause the same query to consume different resources from one run to the next.
- **Batch small operations:** If your workload issues many small statements, consider batching them into larger operations (not to exceed 10MB). This reduces rounding overhead and produces more meaningful cost estimates.
- **Use for tuning, not billing:** DPU data in `EXPLAIN ANALYZE VERBOSE` is designed for cost awareness, query tuning, and optimization. It is not a billing-grade metric. Always rely on CloudWatch metrics or monthly billing reports for authoritative cost and usage data.
