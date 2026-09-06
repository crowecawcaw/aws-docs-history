

# aurora\_stat\_activity
<a name="aurora_stat_activity"></a>

Returns one row per server process, showing information related to the current activity of that process.

## Syntax
<a name="aurora_stat_activity-syntax"></a>

 

```
aurora_stat_activity();
```

## Arguments
<a name="aurora_stat_activity-arguments"></a>

None

## Return type
<a name="aurora_stat_activity-return-type"></a>

Returns one row per server process. In additional to `pg_stat_activity` columns, the following field is added:
+ planid – plan identifier

## Usage notes
<a name="aurora_stat_activity-usage-notes"></a>

A supplementary view to `pg_stat_activity` returning the same columns with an additional `plan_id` column which shows the current query execution plan.

`aurora_compute_plan_id` must be enabled for the view to return a plan\_id.

This function is available from Aurora PostgreSQL versions 14.10, 15.5, and for all other later versions.

## Examples
<a name="aurora_stat_activity-examples"></a>

The example query below aggregates the top load by query\_id and plan\_id.

```
db1=# select count(*), query_id, plan_id
db1-# from aurora_stat_activity() where state = 'active'
db1-# and pid <> pg_backend_pid()
db1-# group by query_id, plan_id
db1-# order by 1 desc;   

count |  query_id             |  plan_id 
-------+----------------------+-------------
 11    | -5471422286312252535 | -2054628807
 3     | -6907107586630739258 | -815866029
 1     | 5213711845501580017  |  300482084
(3 rows)
```

If the plan used for query\_id changes, a new plan\_id will be reported by aurora\_stat\_activity.

```
count  |  query_id            |  plan_id 
-------+----------------------+-------------
 10    | -5471422286312252535 | 1602979607
 1     | -6907107586630739258 | -1809935983
 1     | -2446282393000597155 | -207532066
(3 rows)
```