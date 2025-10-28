# aurora_stat_activity

Returns one row per server process, showing information related to the current
activity of that process.

## Syntax

```
aurora_stat_activity();
```

## Arguments

None

## Return type

Returns one row per server process. In additional to `pg_stat_activity`
columns, the following field is added:

- planid – plan identifier

## Usage notes

A supplementary view to `pg_stat_activity` returning the same columns
with an additional `plan_id` column which shows the current query
execution plan.

`aurora_compute_plan_id` must be enabled for the view to return a
plan_id.

This function is available from Aurora PostgreSQL versions 14.10, 15.5, and for all
other later versions.

## Examples

The example query below aggregates the top load by query_id and plan_id.

```
`db1=# select count(*), query_id, plan_id
db1-# from aurora_stat_activity() where state = 'active'
db1-# and pid <> pg_backend_pid()
db1-# group by query_id, plan_id
db1-# order by 1 desc;`
`count | query_id | plan_id
-------+----------------------+-------------
 11 | -5471422286312252535 | -2054628807
 3 | -6907107586630739258 | -815866029
 1 | 5213711845501580017 | 300482084
(3 rows)`

```

If the plan used for query_id changes, a new plan_id will be reported by
aurora_stat_activity.

```

`count | query_id | plan_id
-------+----------------------+-------------
 10 | -5471422286312252535 | 1602979607
 1 | -6907107586630739258 | -1809935983
 1 | -2446282393000597155 | -207532066
(3 rows)`

```
