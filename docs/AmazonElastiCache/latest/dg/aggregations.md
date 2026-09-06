

# Getting started with data aggregations
<a name="aggregations"></a>

Amazon ElastiCache for Valkey supports aggregation queries, enabling you to filter, group, transform, and summarize data stored in your cache with a single query. Aggregations run server-side in memory, performing computations directly on indexed data and returning only the final results to the client. This eliminates the need to transfer large datasets to the application layer for processing, reducing network overhead and enabling response latencies as low as microseconds over terabytes of data.

Aggregation queries are built as pipelines of chained stages, where the output of each stage feeds into the next. Available stages include `GROUPBY` for grouping results by field values, `REDUCE` for applying functions such as COUNT, SUM, AVG, MIN, and MAX to each group, `APPLY` for computing derived values using expressions, `FILTER` for pruning intermediate results, `SORTBY` for ordering output, `LIMIT` for controlling result set size, and `LOAD` for pulling additional hash fields into the pipeline at query time. You can combine these stages in any order and repeat them to construct multi-step analytical workflows within a single command.

Common use cases include:
+ **Faceted search** - Group matching catalog items by attributes such as category, brand, or rating and return counts per group to power dynamic filter UIs.
+ **Real-time rankings and trends** - Compute top performers by engagement metrics such as views, scores, or sales across categories, with results that reflect the latest data without scheduled recomputation.
+ **Operational reporting and analytics** - Generate summary metrics such as averages, totals, and distributions over session, order, or transaction data on demand or on a schedule, without a separate analytics layer.

For more details on the command syntax, see [FT.AGGREGATE](https://valkey.io/commands/ft.aggregate/) on the Valkey documentation.

For more details related to aggregation expressions, see [Valkey search expressions](https://valkey.io/topics/search-expressions/).