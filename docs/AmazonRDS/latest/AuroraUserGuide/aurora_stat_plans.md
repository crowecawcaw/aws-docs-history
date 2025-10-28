# aurora_stat_plans

Returns a row for every tracked execution plan.

## Syntax

```
aurora_stat_plans(
    showtext
)
```

## Arguments

- showtext – Show the query and plan text. Valid values are NULL,
  true or false. True will show the query and plan text.

## Return type

Returns a row for each tracked plan that contains all the columns from
`aurora_stat_statements` and the following additional columns.

- planid – plan identifier
- explain_plan – explain plan text
- plan_type:
  - `no plan` - no plan was captured
  - `estimate` - plan captured with estimated costs
  - `actual` - plan captured with EXPLAIN ANALYZE

- plan_captured_time – last time a plan was captured

## Usage notes

`aurora_compute_plan_id` must be enabled and
`pg_stat_statements` must be in `shared_preload_libraries`
for the plans to be tracked.

The number of plans available is controlled by the value set in the
`pg_stat_statements.max` parameter. When
`aurora_compute_plan_id` is enabled, you can track the plans up to
this specified value in `aurora_stat_plans`.

This function is available from Aurora PostgreSQL versions 14.10, 15.5, and for all
other later versions.

## Examples

In the example below, the two plans that are for the query identifier
-5471422286312252535 are captured and the statements statistics are tracked by the
planid.

````
`db1=# select calls, total_exec_time, planid, plan_captured_time, explain_plan
db1-# from aurora_stat_plans(true)
db1-# where queryid = '-5471422286312252535'`
`calls | total_exec_time | planid | plan_captured_time | explain_plan
---------+--------------------+-------------+-------------------------------+------------------------------------------------------------------
 1532632 | 3209846.097107853 | 1602979607 | 2023-10-31 03:27:16.925497+00 | Update on pgbench_branches +
| | | | -> Bitmap Heap Scan on pgbench_branches +
| | | | Recheck Cond: (bid = 76) +
| | | | -> Bitmap Index Scan on pgbench_branches_pkey +
| | | | Index Cond: (bid = 76) 61365 | 124078.18012200127 | -2054628807 | 2023-10-31 03:20:09.85429+00 | Update on pgbench_branches +
| | | | -> Index Scan using pgbench_branches_pkey on pgbench_branches+
| | | | Index Cond: (bid = 17)` ```
````
