

# Tuning query\_mem for your workload
<a name="aurora-analytics-tuning-query-mem"></a>

`query_mem` trades per-query speed against concurrency: a higher value lets each query use more memory and run faster, but fewer queries can run at once before they compete for memory. Raise it when only a few large queries run at a time and you want each to finish quickly. Lower it as concurrency rises, so more queries fit without exhausting memory.

On an instance shared with other workloads, keep `query_mem` low so foreign table queries reserve capacity for the other work, or move them to a dedicated reader. For more information, see [Using a dedicated reader instance for analytics](aurora-analytics-dedicated-reader.md).

Because `query_mem` is a per-query ceiling rather than memory reserved up front, concurrency depends on how much memory your queries actually use. To learn how `query_mem` shares instance memory with `shared_buffers` and how to budget it across concurrent sessions, see [Memory budget across concurrent sessions](aurora-analytics-resource-management.md#aurora-analytics-query-memory-concurrent).

You can set `query_mem` at several scope levels: the cluster parameter group, a database (`ALTER DATABASE`), a role (`ALTER ROLE`), or the current session (`SET`). We recommend the lowest level that solves the problem, so a change does not over-allocate memory for queries that do not need it.

For targeted tuning, set it per session so the change applies only to the current connection and only to the queries you run there.

```
SET aurora_analytics.query_mem = 'XXGB';
```

For stable defaults tied to a role, set it per role. This approach suits mixed workloads where different user types consistently need different amounts.

```
ALTER ROLE dashboard_user SET aurora_analytics.query_mem = 'XXGB';
```

Setting `query_mem` in the cluster parameter group changes it for every session on every database, so reserve that for a cluster-wide baseline rather than workload-specific tuning.