# Reading Aurora DSQL EXPLAIN plans

Understanding how to read EXPLAIN plans is key to optimizing query performance. In this section, we’ll walk through real examples of Aurora DSQL query plans, show how different scan types behave, explain where filters are applied, and highlight opportunities for optimization.

## Full Scan example

Aurora DSQL has both Sequential Scans, which is functionally identical to PostgreSQL, as well as Full Scans. The only difference between these two are that Full Scans can utilize extra filtering on storage. Due to this, it is almost always selected above Sequential Scans. Due to the similarity, we will only cover examples of the more interesting Full Scans.

Full Scans will mostly be used on tables with no primary key. Because Aurora DSQL primary keys are by default full covering indexes, Aurora DSQL will most likely use Index Only Scans on the primary key in many situations where PostgreSQL would use a Sequential Scan. As with most other databases, a table with no indexes on it will scale badly.

```
EXPLAIN SELECT account_id FROM transaction WHERE transaction_date > '2025-01-01' AND description LIKE '%external%';
```

```
                                                   QUERY PLAN
----------------------------------------------------------------------------------------------------------------
 Full Scan (btree-table) on transaction  (cost=125100.05..177933.38 rows=33333 width=16)
   Filter: (description ~~ '%external%'::text)
   -> Storage Scan on transaction (cost=12510.05..17793.38 rows=66666 width=16)
        Projections: account_id, description
        Filters: (transaction_date > '2025-01-01 00:00:00'::timestamp without time zone)
        -> B-Tree Scan on transaction (cost=12510.05..17793.38 rows=100000 width=30)
```

This plan shows two filters applied at different stages. The `transaction_date >
 '2025-01-01'` condition is applied at the storage layer, reducing how much data is returned. The
`description LIKE '%external%'` condition is applied later in the query processor, after data is
transferred, making it less efficient. Pushing more selective filters into the storage or index
layers generally improves performance.

## Index Only Scan example

Index Only Scans are the most optimal scan types in Aurora DSQL as they result in the fewest
round trips to the storage layer and can do the most filtering. But just because you see Index
Only Scan does not mean that you have the best plan. Because of all the different levels of
filtering that can happen, it is essential to still pay attention to the different places
filtering can happen.

```
EXPLAIN SELECT balance FROM account
WHERE customer_id = '4b18a761-5870-4d7c-95ce-0a48eca3fceb'
AND balance > 100
AND status = 'pending';
```

```
                                  QUERY PLAN
-------------------------------------------------------------------------------
 Index Only Scan using idx1 on account  (cost=725.05..1025.08 rows=8 width=18)
   Index Cond: (customer_id = '4b18a761-5870-4d7c-95ce-0a48eca3fceb'::uuid)
   Filter: (balance > '100'::numeric)
   -> Storage Scan on idx1 (cost=12510.05..17793.38 rows=9 width=16)
        Projections: balance
        Filters: ((status)::text = 'pending'::text)
        -> B-Tree Scan on idx1 (cost=12510.05..17793.38 rows=10 width=30)
            Index Cond: (customer_id = '4b18a761-5870-4d7c-95ce-0a48eca3fceb'::uuid)
```

In this plan, the index condition, `customer_id = '4b18a761-5870-4d7c-95ce-0a48eca3fceb'`), is evaluated first during the index scan, which is the most efficient stage because it limits how much data is read from storage. The storage filter, `status = 'pending'`, is applied after data is read but before it’s sent to the compute layer, reducing the amount of data transferred. Finally, the query processor filter, `balance > 100`, runs last, after the data has been moved, making it the least efficient. Of these, the index condition provides the greatest performance because it directly controls how much data is scanned.

## Index Scan example

Index Scans are similar to Index Only Scans, except they have the extra step of having to
call into the base table. Because Aurora DSQL can specify storage filters, it is able to do so on both
the index call as well as the lookup call.

To make this clear, Aurora DSQL presents the plan as two nodes. This way, you can clearly see how much adding an include column will help in terms of rows returned from storage.

```
EXPLAIN SELECT balance FROM account
WHERE customer_id = '4b18a761-5870-4d7c-95ce-0a48eca3fceb'
AND balance > 100
AND status = 'pending'
AND created_at > '2025-01-01';
```

```
                                                QUERY PLAN
----------------------------------------------------------------------------------------------------------
 Index Scan using idx1 on account  (cost=728.18..1132.20 rows=3 width=18)
   Filter: (balance > '100'::numeric)
   Index Cond: (customer_id = '4b18a761-5870-4d7c-95ce-0a48eca3fceb'::uuid)
   -> Storage Scan on idx1 (cost=12510.05..17793.38 rows=8 width=16)
        Projections: balance
        Filters: ((status)::text = 'pending'::text)
        -> B-Tree Scan on account (cost=12510.05..17793.38 rows=10 width=30)
            Index Cond: (customer_id = '4b18a761-5870-4d7c-95ce-0a48eca3fceb'::uuid)
   -> Storage Lookup on account (cost=12510.05..17793.38 rows=4 width=16)
        Filters: (created_at > '2025-01-01 00:00:00'::timestamp without time zone)
        -> B-Tree Lookup on transaction (cost=12510.05..17793.38 rows=8 width=30)
```

This plan shows how filtering happens across multiple stages:

- The index condition on `customer_id` filters data early.
- The storage filter on `status` further narrows results before they’re sent to
  compute.
- The query processor filter on `balance` is applied later, after
  transfer.
- The lookup filter on `created_at` is evaluated when fetching additional columns
  from the base table.

Adding frequently used columns as `INCLUDE` fields can often eliminate this lookup and improve
performance.

## Best Practices

- **Align filters with indexed columns** to push filtering
  earlier.
- **Use INCLUDE columns** to allow Index-Only Scans and avoid
  lookups.
- **Keep statistics up to date** to ensure cost and row
  estimates are accurate.
- **Avoid unindexed queries** on large tables to prevent
  expensive Full Scans.
