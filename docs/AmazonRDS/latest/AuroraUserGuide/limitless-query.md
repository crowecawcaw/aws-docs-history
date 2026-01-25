# Single-shard queries in Aurora PostgreSQL Limitless Database

A _single-shard query_ is a query that can be run directly on a shard while maintaining SQL [ACID](https://en.wikipedia.org/wiki/ACID "https://en.wikipedia.org/wiki/ACID") semantics. When such a query is encountered by the query planner on the router, the
planner detects it and proceeds to push down the entire SQL query to the corresponding shard.

This optimization reduces the number of network round trips from the router to the shard, improving the performance. Currently this optimization
is performed for `INSERT`, `SELECT`, `UPDATE`, and `DELETE` queries.

###### Topics

- [Single-shard query examples](#limitless-query.single-shard.examples "#limitless-query.single-shard.examples")
- [Restrictions for single-shard queries](#limitless-query.single-shard.restrictions "#limitless-query.single-shard.restrictions")
- [Fully qualified (explicit) joins](#limitless-query.single-shard.fq "#limitless-query.single-shard.fq")
- [Setting an active shard key](#limitless-query.single-shard.active "#limitless-query.single-shard.active")

## Single-shard query examples

In the following examples, we have the sharded table `customers`, with the shard key `customer_id`, and the reference
table `zipcodes`.

**SELECT**

```
postgres_limitless=> EXPLAIN (VERBOSE, COSTS OFF) SELECT * FROM customers WHERE customer_id = 100;

                       QUERY PLAN
---------------------------------------------------------
 Foreign Scan
   Output: customer_id, other_id, customer_name, balance
   Remote SQL:  SELECT customer_id,
     other_id,
     customer_name,
     balance
    FROM public.customers
   WHERE (customer_id = 100)
 Single Shard Optimized
(9 rows)
```

```
postgres_limitless=> EXPLAIN (VERBOSE, COSTS OFF) SELECT * FROM orders
    LEFT JOIN zipcodes ON orders.zipcode_id = zipcodes.zipcode_id
    WHERE customer_id = 11;

                                               QUERY PLAN
---------------------------------------------------------------------------------------------------------
 Foreign Scan
   Output: customer_id, order_id, zipcode_id, customer_name, balance, zipcodes.zipcode_id, zipcodes.city
   Remote SQL:  SELECT orders.customer_id,
     orders.order_id,
     orders.zipcode_id,
     orders.customer_name,
     orders.balance,
     zipcodes.zipcode_id,
     zipcodes.city
    FROM (public.orders
      LEFT JOIN public.zipcodes ON ((orders.zipcode_id = zipcodes.zipcode_id)))
   WHERE (orders.customer_id = 11)
 Single Shard Optimized
(13 rows)
```

**INSERT**

```
postgres_limitless=> EXPLAIN (VERBOSE, COSTS OFF) INSERT INTO customers
    (customer_id, other_id, customer_name, balance)
    VALUES (1, 10, 'saikiran', 1000);

                      QUERY PLAN
-------------------------------------------------------
 Insert on public.customers
   ->  Result
         Output: 1, 10, 'saikiran'::text, '1000'::real
 Single Shard Optimized
(4 rows)
```

**UPDATE**

```
postgres_limitless=> EXPLAIN (VERBOSE, COSTS OFF) UPDATE orders SET balance = balance + 100
    WHERE customer_id = 100;

                                         QUERY PLAN
---------------------------------------------------------------------------------------------
 Update on public.orders
   Foreign Update on public.orders_fs00002 orders_1
   ->  Foreign Update
         Remote SQL:  UPDATE public.orders SET balance = (balance + (100)::double precision)
   WHERE (customer_id = 100)
 Single Shard Optimized
(6 rows)
```

**DELETE**

```
postgres_limitless=> EXPLAIN (VERBOSE, COSTS OFF) DELETE FROM orders
    WHERE customer_id = 100 and balance = 0;

                             QUERY PLAN
---------------------------------------------------------------------
 Delete on public.orders
   Foreign Delete on public.orders_fs00002 orders_1
   ->  Foreign Delete
         Remote SQL:  DELETE FROM public.orders
   WHERE ((customer_id = 100) AND (balance = (0)::double precision))
 Single Shard Optimized
(6 rows)
```

## Restrictions for single-shard queries

Single-shard queries have the following restrictions:

**Functions**

If a single-shard query contains a function, the query qualifies for single-shard optimization only if one of the following
conditions applies:

- The function is immutable. For more information, see [Function volatility](limitless-reference.md#limitless-function-volatility "limitless-reference.md#limitless-function-volatility").
- The function is mutable, but is registered in the `rds_aurora.limitless_distributed_functions` view. For more
  information, see [Function distribution](limitless-reference.md#limitless-function-distribution "limitless-reference.md#limitless-function-distribution").

**Views**

If a query contains one or more views, single-shard optimization is disabled for the query if it has one of the following
conditions:

- Any view has the `security_barrier` attribute.
- Objects used in the query require multiple user privileges. For example, a query contains two views, and the views are run
  under two different users.

```
CREATE VIEW v1 AS SELECT customer_name FROM customers c WHERE c.customer_id =  1;
CREATE VIEW v2 WITH (security_barrier) AS SELECT customer_name FROM customers c WHERE c.customer_id =  1;

postgres_limitless=> EXPLAIN VERBOSE SELECT * FROM v1;
                                     QUERY PLAN
------------------------------------------------------------------------------------
 Foreign Scan  (cost=100.00..101.00 rows=100 width=0)
   Output: customer_name
   Remote Plans from Shard postgres_s3:
         Seq Scan on public.customers_ts00001 c  (cost=0.00..24.12 rows=6 width=32)
           Output: c.customer_name
           Filter: (c.customer_id = 1)
         Query Identifier: -6005737533846718506
   Remote SQL:  SELECT customer_name
    FROM ( SELECT c.customer_name
            FROM public.customers c
           WHERE (c.customer_id = 1)) v1
 Query Identifier: -5754424854414896228
(12 rows)


postgres_limitless=> EXPLAIN VERBOSE SELECT * FROM v2;
                                         QUERY PLAN
--------------------------------------------------------------------------------------------
 Foreign Scan on public.customers_fs00001 c  (cost=100.00..128.41 rows=7 width=32)
   Output: c.customer_name
   Remote Plans from Shard postgres_s3:
         Seq Scan on public.customers_ts00001 customers  (cost=0.00..24.12 rows=6 width=32)
           Output: customers.customer_name
           Filter: (customers.customer_id = 1)
         Query Identifier: 4136563775490008117
   Remote SQL: SELECT customer_name FROM public.customers WHERE ((customer_id = 1))
 Query Identifier: 5056054318010163757
(9 rows)
```

**PREPARE and EXECUTE statements**

Aurora PostgreSQL Limitless Database supports single-shard optimization for prepared
`SELECT`, `UPDATE`, and `DELETE`
statements.

However, if you use prepared statements for `PREPARE` and
`EXECUTE` with `plan_cache_mode` set to
`'force_generic_plan'`, the query planner rejects
single-shard optimization for that query.

**PL/pgSQL**

Queries with PL/pgSQL variables are run as implicitly prepared statements. If a query contains any PL/pgSQL variables, the query
planner rejects single-shard optimization.

Optimization is supported in the PL/pgSQL block if the statement doesn't contain any PL/pgSQL variables.

## Fully qualified (explicit) joins

Single-shard optimization is based on partition eliminations. The PostgreSQL optimizer eliminates partitions based on constant conditions. If
Aurora PostgreSQL Limitless Database finds that all of the remaining partitions and tables are on the same shard, it marks the query eligible for single-shard optimization.
All filter conditions must be explicit for partition elimination to work. Aurora PostgreSQL Limitless Database can't eliminate partitions without one or more join
predicates or filter predicates on the shard keys of every sharded table in the statement.

Assume that we've partitioned the `customers`, `orders`, and `order_details` tables based on the
`customer_id` column. In this schema, the application tries to keep all of the data for a customer on a single shard.

Consider the following query:

```
SELECT * FROM
    customers c, orders o, order_details od
WHERE c.customer_id = o.customer_id
    AND od.order_id = o.order_id
    AND c.customer_id = 1;
```

This query retrieves all of the data for a customer (`c.customer_id = 1`). Data for this customer is on a single shard, but
Aurora PostgreSQL Limitless Database doesn't qualify this query as a single-shard query. The optimizer process for the query is as follows:

1. The optimizer can eliminate partitions for `customers` and `orders` based on the following condition:

```
c.customer_id = 1
c.customer_id = o.customer_id
o.customer_id =  1 (transitive implicit condition)
```

2. The optimizer can't eliminate any partitions for `order_details`, because there's no constant condition on the
   table.
3. The optimizer concludes that it has read all of the partitions from `order_details`. Therefore, the query can't be
   qualified for single-shard optimization.

To make this a single-shard query, we add the following explicit join condition:

```
o.customer_id = od.customer_id
```

The changed query looks like this:

```
SELECT * FROM
    customers c, orders o,  order_details od
WHERE c.customer_id = o.customer_id
     AND o.customer_id = od.customer_id
     AND od. order_id = o. order_id
 AND c.customer_id =  1;

```

Now the optimizer can eliminate partitions for `order_details`. The new query becomes a single-shard query and qualifies for
optimization.

## Setting an active shard key

This feature allows you to set a single shard key while querying the database, causing all `SELECT` and DML queries to be appended
with the shard key as a constant predicate. This feature is useful if you've migrated to Aurora PostgreSQL Limitless Database and have denormalized the schema by adding
shard keys to tables.

You can append a shard key predicate automatically to the existing SQL logic, without changing the semantics of the queries. Appending an
active shard key predicate is done only for [compatible tables](#active-shard-key-compatible-tables "#active-shard-key-compatible-tables").

The active shard key feature uses the `rds_aurora.limitless_active_shard_key` variable, which has the following syntax:

```
SET [session | local] rds_aurora.limitless_active_shard_key = '{"col1_value", "col2_value", ...}';
```

Some considerations about active shard keys and foreign keys:

- A sharded table can have a foreign key constraint if the parent and child tables
  are collocated and the foreign key is a superset of the shard key.
- A sharded table can have a foreign key constraint to a reference table.
- A reference table can have a foreign key constraint to another reference table.

Assume that we have a `customers` table that is sharded on the `customer_id` column.

```
BEGIN;
SET local rds_aurora.limitless_create_table_mode='sharded';
SET local rds_aurora.limitless_create_table_shard_key='{"customer_id"}';
CREATE TABLE customers(customer_id int PRIMARY KEY, name text , email text);
COMMIT;
```

With an active shard key set, queries have the following transformations.

**SELECT**

```
SET rds_aurora.limitless_active_shard_key = '{"123"}';
SELECT * FROM customers;

-- This statement is changed to:
SELECT * FROM customers WHERE customer_id = '123'::int;
```

**INSERT**

```
SET rds_aurora.limitless_active_shard_key = '{"123"}';
INSERT INTO customers(name, email) VALUES('Alex', 'alex@example.com');

-- This statement is changed to:
INSERT INTO customers(customer_id, name, email) VALUES('123'::int, 'Alex', 'alex@example.com');
```

**UPDATE**

```
SET rds_aurora.limitless_active_shard_key = '{"123"}';
UPDATE customers SET email = 'alex_new_email@example.com';

-- This statement is changed to:
UPDATE customers SET email = 'alex_new_email@example.com' WHERE customer_id = '123'::int;
```

**DELETE**

```
SET rds_aurora.limitless_active_shard_key = '{"123"}';
DELETE FROM customers;

-- This statement is changed to:
DELETE FROM customers WHERE customer_id = '123'::int;
```

**Joins**

When performing join operations on tables with an active shard key, the shard key predicate is automatically added to all tables
involved in the join. This automatic addition of the shard key predicate occurs only when all tables in the query belong to the same
collocation group. If the query involves tables from different collocation groups, an error is raised instead.

Assume that we also have `orders` and `order_details` tables that are collocated with the
`customers` table.

```
SET local rds_aurora.limitless_create_table_mode='sharded';
SET local rds_aurora.limitless_create_table_collocate_with='customers';
SET local rds_aurora.limitless_create_table_shard_key='{"customer_id"}';
CREATE TABLE orders (id int , customer_id int, total_amount int, date date);
CREATE TABLE order_details (id int , order_id int, customer_id int, product_name VARCHAR(100), price int);
COMMIT;
```

Retrieve the last 10 order invoices for a customer whose customer ID is 10.

```
SET rds_aurora.limitless_active_shard_key = '{"10"}';
SELECT * FROM customers, orders, order_details WHERE
    orders.customer_id = customers.customer_id AND
    order_details.order_id = orders.order_id AND
    customers.customer_id = 10
    order by order_date limit 10;
```

This query is transformed into the following:

```
SELECT * FROM customers, orders, order_details WHERE
    orders.customer_id = customers.customer_id AND
    orders.order_id = order_details.order_id AND
    customers.customer_id = 10 AND
    order_details.customer_id = 10 AND
    orders.customer_id = 10 AND
    ORDER BY "order_date" LIMIT 10;
```

**Active shard key compatible tables**

The shard key predicate is added only to tables that are compatible with the active shard key. A table is considered compatible if
it has the same number of columns in its shard key as specified in the `rds_aurora.limitless_active_shard_key` variable.
If the query involves tables that are incompatible with the active shard key, the system raises an error instead of proceeding with
the query.

For example:

```
-- Compatible table
SET rds_aurora.limitless_active_shard_key = '{"10"}';

-- The following query works because the customers table is sharded on one column.
SELECT * FROM customers;

-- Incompatible table
SET rds_aurora.limitless_active_shard_key = '{"10","20"}';

-- The following query raises a error because the customers table isn't sharded on two columns.
 SELECT * FROM customers;
```
