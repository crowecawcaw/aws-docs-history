

# Batched nested-loop joins in Aurora DSQL EXPLAIN plans
<a name="batched-nested-loop-joins"></a>

When a query joins a small outer input to an inner input that Aurora DSQL can scan efficiently from storage, Aurora DSQL can choose a `Nested Loop (Batched Join)` plan. This join type reduces round trips between the compute and storage layers by grouping multiple outer rows together before probing the inner side.

A standard nested loop processes one outer row at a time and runs the inner scan again for every row. A batched nested-loop join collects a batch of outer rows, builds the inner scan work for the entire batch, and then joins the returned inner rows back to the matching outer rows.

## How batched nested-loop joins work
<a name="batched-nested-loop-joins-how-it-works"></a>

1. Aurora DSQL reads a batch of rows from the outer side of the join.

1. If the inner side is an `Index Scan` or `Index Only Scan` with an `Index Cond` parameterized on the outer side, Aurora DSQL binds the condition for each outer row and combines the resulting index scan keys into one batched inner scan. Other join predicates don't drive the inner scan.

1. An `Index Scan` or `Index Only Scan` without an outer-parameterized `Index Cond` behaves like a `Full Scan` or `Sequential Scan`. Aurora DSQL has no parameterized index scan keys to combine and runs one inner scan per outer batch instead of one inner scan per outer row.

1. Aurora DSQL streams rows from the inner side as they arrive for the batch. It doesn't materialize the entire inner result for the batch before joining.

1. When the inner `Index Scan` or `Index Only Scan` has an outer-parameterized `Index Cond`, Aurora DSQL uses the `Recheck Cond` to match each returned inner row back to the applicable outer rows in the batch. Aurora DSQL then applies any remaining join predicates. Without an outer-parameterized `Index Cond`, Aurora DSQL applies the join predicates directly as it matches each streamed inner row against the outer batch.

1. For left and anti joins, Aurora DSQL tracks which outer rows matched and emits unmatched rows after the inner scan for the batch finishes.

This approach is most useful when the inner side is an index scan with a parameterized `Index Cond`, because the combined scan keys provide targeted storage access for the entire outer batch.

## When Aurora DSQL uses this join
<a name="batched-nested-loop-joins-when-used"></a>

Aurora DSQL considers batched nested-loop joins when the inner side of the join is a physical scan node, meaning an `Index Scan`, `Index Only Scan`, `Full Scan`, or `Sequential Scan`, and batching is expected to cost less than running the inner scan for each outer row. In practice, the greatest benefit typically comes from a smaller outer input and an inner index scan with an `Index Cond` parameterized on the outer side.

If another plan shape is cheaper, such as a hash join or merge join, Aurora DSQL chooses that plan instead. To compare plan shapes during tuning, you can disable batched nested-loop joins for the current session:

```
SET dsql.enable_batched_nestloop = off;
```

## How to read batched nested-loop join output
<a name="batched-nested-loop-joins-reading-output"></a>

The following query uses the sample `transaction` and `account` tables from [Reading Aurora DSQL EXPLAIN plans](reading-dsql-explain-plans.md):

```
EXPLAIN
SELECT t.account_id, a.balance
FROM transaction t
LEFT JOIN account a
  ON t.account_id = a.customer_id
 AND a.balance > CASE
                    WHEN t.description LIKE 'fee%' THEN 0
                    ELSE 100
                  END
WHERE t.transaction_date >= '2025-01-01'
  AND (a.status = 'active' OR a.customer_id IS NULL)
ORDER BY t.account_id;
```

An EXPLAIN plan can include output similar to the following:

```
Sort
  Sort Key: t.account_id
  -> Nested Loop (Batched Join)
       Filter: (((status)::text = 'active'::text) OR (customer_id IS NULL))
       Join Type: Left
       Recheck Cond: (customer_id = t.account_id)
       Join Filter: (balance > CASE WHEN (t.description ~~ 'fee%'::text) THEN '0'::numeric ELSE '100'::numeric END)
       -> Full Scan (btree-table) on transaction t
            -> Storage Scan on transaction t
                 Filters: (transaction_date >= '2025-01-01 00:00:00'::timestamp without time zone)
                 -> B-Tree Scan on transaction t
       -> Index Only Scan using idx1 on account a
            Index Cond: (customer_id = t.account_id)
```

`Nested Loop (Batched Join)`  
Shows that Aurora DSQL is batching outer rows before probing the inner side of the join.

`Index Cond`  
Shows the predicate used to probe the inner side for the current batch. When the inner side is an `Index Scan` or `Index Only Scan`, this predicate often references columns from the outer side of the join.

`Filter`  
Shows a condition applied to the result of the join. In this example, the `WHERE (a.status = 'active' OR a.customer_id IS NULL)` condition appears here. Under standard SQL left join semantics, this condition can't be pushed into the inner scan because doing so would change the query results. Aurora DSQL displays it as a filter on the join node. By contrast, the condition on `t.transaction_date` references only the outer table, so it appears under the outer physical scan.

`Join Type`  
Shows the join semantics for the batched join, such as `Left`, `Semi`, or `Anti`.

`Recheck Cond`  
Appears only when the inner side is an `Index Scan` or `Index Only Scan` with at least one `Index Cond` parameterized on the outer side of the join. For each returned inner row, Aurora DSQL runs the recheck against every outer row in the batch to determine which outer rows produced that probe and should join with that inner row.

`Join Filter`  
Shows join predicates that Aurora DSQL evaluates after it has matched an inner row back to candidate outer rows in the batch. These predicates affect which row pairs join, but they don't drive the storage probe the way `Index Cond` does.

A preceding sort node  
Can appear when the query needs ordered output. Batched nested-loop joins don't preserve the same output order guarantees as a standard nested loop, so Aurora DSQL can add an explicit sort before returning the final result set.