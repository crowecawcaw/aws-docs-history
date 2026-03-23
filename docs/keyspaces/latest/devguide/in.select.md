# Use the `IN` operator with the `SELECT` statement in a query in Amazon Keyspaces

SELECT IN

You can query data from tables using the `SELECT` statement, which reads
one or more columns for one or more rows in a table and returns a result-set containing
the rows matching the request. A `SELECT` statement contains a
`select_clause` that determines which columns to read and to return in
the result-set. The clause can contain instructions to transform the data before
returning it. The optional `WHERE` clause specifies which rows must be
queried and is composed of relations on the columns that are part of the primary key.
Amazon Keyspaces supports the `IN` keyword in the `WHERE` clause.
This section uses examples to show how Amazon Keyspaces processes `SELECT` statements with the
`IN` keyword.

This examples demonstrates how Amazon Keyspaces breaks down the `SELECT` statement with the `IN` keyword
into _subqueries_. In this example we use a table with the name `my_keyspace.customers`.
The table has one primary key column `department_id`, two clustering columns `sales_region_id` and `sales_representative_id`, and one column
that contains the name of the customer in the `customer_name` column.

```
`SELECT * FROM my_keyspace.customers;

 department_id | sales_region_id | sales_representative_id | customer_name
 ---------------+-----------------+-------------------------+--------------
 0 | 0 | 0 | a
 0 | 0 | 1 | b
 0 | 1 | 0 | c
 0 | 1 | 1 | d
 1 | 0 | 0 | e
 1 | 0 | 1 | f
 1 | 1 | 0 | g
 1 | 1 | 1 | h`
```

Using this table, you can run the following `SELECT` statement to find the customers in the departments and
sales regions that you are interested in with the `IN` keyword in the `WHERE`
clause. The following statement is an example of this.

```
SELECT * FROM my_keyspace.customers WHERE department_id IN (0, 1) AND sales_region_id IN (0, 1);
```

Amazon Keyspaces divides this statement into four subqueries as shown in the following
output.

```
`SELECT * FROM my_keyspace.customers WHERE department_id = 0 AND sales_region_id = 0;

 department_id | sales_region_id | sales_representative_id | customer_name
---------------+-----------------+-------------------------+--------------
 0 | 0 | 0 | a
 0 | 0 | 1 | b

SELECT * FROM my_keyspace.customers WHERE department_id = 0 AND sales_region_id = 1;

 department_id | sales_region_id | sales_representative_id | customer_name
---------------+-----------------+-------------------------+--------------
 0 | 1 | 0 | c
 0 | 1 | 1 | d

SELECT * FROM my_keyspace.customers WHERE department_id = 1 AND sales_region_id = 0;

 department_id | sales_region_id | sales_representative_id | customer_name
---------------+-----------------+-------------------------+--------------
 1 | 0 | 0 | e
 1 | 0 | 1 | f

SELECT * FROM my_keyspace.customers WHERE department_id = 1 AND sales_region_id = 1;

 department_id | sales_region_id | sales_representative_id | customer_name
---------------+-----------------+-------------------------+--------------
 1 | 1 | 0 | g
 1 | 1 | 1 | h`
```

When the `IN` keyword is used, Amazon Keyspaces automatically paginates the results in any of the following cases:

- After every 10th subquery is processed.
- After processing 1MB of logical IO.
- If you configured a `PAGE SIZE`, Amazon Keyspaces paginates after reading the number of queries
  for processing based on the set `PAGE SIZE`.
- When you use the `LIMIT` keyword to reduce the number of rows returned,
  Amazon Keyspaces paginates after reading the number of queries
  for processing based on the set `LIMIT`.
  The following table is used to illustrate this with an example.

For more information about pagination, see [Paginate results in Amazon Keyspaces](paginating-results.md "paginating-results.md").

```
`SELECT * FROM my_keyspace.customers;

 department_id | sales_region_id | sales_representative_id | customer_name
 ---------------+-----------------+-------------------------+--------------
 2 | 0 | 0 | g
 2 | 1 | 1 | h
 2 | 2 | 2 | i
 0 | 0 | 0 | a
 0 | 1 | 1 | b
 0 | 2 | 2 | c
 1 | 0 | 0 | d
 1 | 1 | 1 | e
 1 | 2 | 2 | f
 3 | 0 | 0 | j
 3 | 1 | 1 | k
 3 | 2 | 2 | l`
```

You can run the following statement on this table to see how pagination works.

```
SELECT * FROM my_keyspace.customers WHERE department_id IN (0, 1, 2, 3) AND sales_region_id IN (0, 1, 2) AND sales_representative_id IN (0, 1);
```

Amazon Keyspaces processes this statement as 24 subqueries, because the cardinality of the
Cartesian product of all the `IN` terms contained in this query is 24.

```
 `department_id | sales_region_id | sales_representative_id | customer_name
---------------+-----------------+-------------------------+--------------
 0 | 0 | 0 | a
 0 | 1 | 1 | b
 1 | 0 | 0 | d
 1 | 1 | 1 | e

---MORE---
 department_id | sales_region_id | sales_representative_id | customer_name
---------------+-----------------+-------------------------+--------------
 2 | 0 | 0 | g
 2 | 1 | 1 | h
 3 | 0 | 0 | j

---MORE---
 department_id | sales_region_id | sales_representative_id | customer_name
---------------+-----------------+-------------------------+--------------
 3 | 1 | 1 | k`
```

This example shows how you can use the `ORDER BY` clause in a `SELECT` statement
with the `IN` keyword.

```
`SELECT * FROM my_keyspace.customers WHERE department_id IN (3, 2, 1) ORDER BY sales_region_id DESC;

 department_id | sales_region_id | sales_representative_id | customer_name
 ---------------+-----------------+-------------------------+--------------
 3 | 2 | 2 | l
 3 | 1 | 1 | k
 3 | 0 | 0 | j
 2 | 2 | 2 | i
 2 | 1 | 1 | h
 2 | 0 | 0 | g
 1 | 2 | 2 | f
 1 | 1 | 1 | e
 1 | 0 | 0 | d`
```

Subqueries are processed in the order in which the partition key and clustering key
columns are presented in the query. In the example below, subqueries for partition key
value ”2“ are processed first, followed by subqueries for partition key value ”3“ and
”1“. Results of a given subquery are ordered according to the query's ordering clause,
if present, or the table's clustering order defined during table creation.

```
`SELECT * FROM my_keyspace.customers WHERE department_id IN (2, 3, 1) ORDER BY sales_region_id DESC;

 department_id | sales_region_id | sales_representative_id | customer_name
 ---------------+-----------------+-------------------------+--------------
 2 | 2 | 2 | i
 2 | 1 | 1 | h
 2 | 0 | 0 | g
 3 | 2 | 2 | l
 3 | 1 | 1 | k
 3 | 0 | 0 | j
 1 | 2 | 2 | f
 1 | 1 | 1 | e
 1 | 0 | 0 | d`
```
