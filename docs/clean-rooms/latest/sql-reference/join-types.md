# Join types

## INNER

This is the default join type. Returns the rows that have matching values in both table
references.

The INNER JOIN is the most common type of join used in SQL. It's a powerful way to combine
data from multiple tables based on a common column or set of columns.

**Syntax:**

```
SELECT column1, column2, ..., columnn
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```

The following query will return all the rows where there is a matching customer_id value
between the customers and orders tables. The result set will contain the customer_id, name,
order_id, and order_date columns.

```
SELECT customers.customer_id, customers.name, orders.order_id, orders.order_date
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;
```

The following query is an inner join (without the JOIN keyword) between the LISTING table
and SALES table, where the LISTID from the LISTING table is between 1 and 5. This query matches
LISTID column values in the LISTING table (the left table) and SALES table (the right table).
The results show that LISTID 1, 4, and 5 match the criteria.

```
select listing.listid, sum(pricepaid) as price, sum(commission) as comm
from listing, sales
where listing.listid = sales.listid
and listing.listid between 1 and 5
group by 1
order by 1;

listid | price  |  comm
-------+--------+--------
     1 | 728.00 | 109.20
     4 |  76.00 |  11.40
     5 | 525.00 |  78.75

```

The following example is an inner join with the ON clause. In this case, NULL rows are not
returned.

```
select listing.listid, sum(pricepaid) as price, sum(commission) as comm
from sales join listing
on sales.listid=listing.listid and sales.eventid=listing.eventid
where listing.listid between 1 and 5
group by 1
order by 1;

listid | price  |  comm
-------+--------+--------
     1 | 728.00 | 109.20
     4 |  76.00 |  11.40
     5 | 525.00 |  78.75

```

The following query is an inner join of two subqueries in the FROM clause. The query finds
the number of sold and unsold tickets for different categories of events (concerts and shows).
The FROM clause subqueries are _table_ subqueries; they can return multiple
columns and rows.

```
select catgroup1, sold, unsold
from
(select catgroup, sum(qtysold) as sold
from category c, event e, sales s
where c.catid = e.catid and e.eventid = s.eventid
group by catgroup) as a(catgroup1, sold)
join
(select catgroup, sum(numtickets)-sum(qtysold) as unsold
from category c, event e, sales s, listing l
where c.catid = e.catid and e.eventid = s.eventid
and s.listid = l.listid
group by catgroup) as b(catgroup2, unsold)

on a.catgroup1 = b.catgroup2
order by 1;

catgroup1 |  sold  | unsold
----------+--------+--------
Concerts  | 195444 |1067199
Shows     | 149905 | 817736

```

## LEFT [ OUTER ]

Returns all values from the left table reference and the matched values from the right
table reference, or appends NULL if there is no match. It's also referred to as a _left outer join_.

It returns all the rows from the left (first) table, and the matching rows from the right
(second) table. If there is no match in the right table, the result set will contain NULL
values for the columns from the right table. The OUTER keyword can be omitted, and the join can
be written as simply LEFT JOIN. The opposite of a LEFT OUTER JOIN is a RIGHT OUTER JOIN, which
returns all the rows from the right table and the matching rows from the left table.

**Syntax:**

```
SELECT column1, column2, ..., columnn
FROM table1
LEFT [OUTER] JOIN table2
ON table1.column = table2.column;
```

The following query will return all the rows from the customers table, along with the
matching rows from the orders table. If a customer has no orders, the result set will still
include that customer's information, with NULL values for the order_id and order_date
columns.

```
SELECT customers.customer_id, customers.name, orders.order_id, orders.order_date
FROM customers
LEFT OUTER JOIN orders
ON customers.customer_id = orders.customer_id;
```

The following query is a left outer join. Left and right outer joins retain values from
one of the joined tables when no match is found in the other table. The left and right tables
are the first and second tables listed in the syntax. NULL values are used to fill the "gaps"
in the result set. This query matches LISTID column values in the LISTING table (the left
table) and the SALES table (the right table). The results show that LISTIDs 2 and 3 didn't
result in any sales.

```
select listing.listid, sum(pricepaid) as price, sum(commission) as comm
from listing left outer join sales on sales.listid = listing.listid
where listing.listid between 1 and 5
group by 1
order by 1;

listid | price  |  comm
-------+--------+--------
     1 | 728.00 | 109.20
     2 | NULL   | NULL
     3 | NULL   | NULL
     4 |  76.00 |  11.40
     5 | 525.00 |  78.75

```

## RIGHT [ OUTER ]

Returns all values from the right table reference and the matched values from the left
table reference, or appends NULL if there is no match. It's also referred to as a _right outer join_.

It returns all the rows from the right (second) table, and the matching rows from the left
(first) table. If there is no match in the left table, the result set will contain NULL values
for the columns from the left table. The OUTER keyword can be omitted, and the join can be
written as simply RIGHT JOIN. The opposite of a RIGHT OUTER JOIN is a LEFT OUTER JOIN, which
returns all the rows from the left table and the matching rows from the right table.

**Syntax:**

```
SELECT column1, column2, ..., columnn
FROM table1
RIGHT [OUTER] JOIN table2
ON table1.column = table2.column;
```

The following query will return all the rows from the customers table, along with the
matching rows from the orders table. If a customer has no orders, the result set will still
include that customer's information, with NULL values for the order_id and order_date
columns.

```
SELECT orders.order_id, orders.order_date, customers.customer_id, customers.name
FROM orders
RIGHT OUTER JOIN customers
ON orders.customer_id = customers.customer_id;
```

The following query is a right outer join. This query matches LISTID column values in the
LISTING table (the left table) and the SALES table (the right table). The results show that
LISTIDs 1, 4, and 5 match the criteria.

```
select listing.listid, sum(pricepaid) as price, sum(commission) as comm
from listing right outer join sales on sales.listid = listing.listid
where listing.listid between 1 and 5
group by 1
order by 1;

listid | price  |  comm
-------+--------+--------
     1 | 728.00 | 109.20
     4 |  76.00 |  11.40
     5 | 525.00 |  78.75

```

## FULL [OUTER]

Returns all values from both relations, appending NULL values on the side that doesn't
have a match. It's also referred to as a _full outer join_.

It returns all the rows from both the left and right tables, regardless of whether there
is a match or not. If there is no match, the result set will contain NULL values for the
columns from the table that doesn't have a matching row. The OUTER keyword can be omitted, and
the join can be written as simply FULL JOIN. The FULL OUTER JOIN is less commonly used than the
LEFT OUTER JOIN or RIGHT OUTER JOIN, but it can be useful in certain scenarios where you need
to see all the data from both tables, even if there are no matches.

**Syntax:**

```
SELECT column1, column2, ..., columnn
FROM table1
FULL [OUTER] JOIN table2
ON table1.column = table2.column;
```

The following query will return all the rows from both the customers and orders tables. If
a customer has no orders, the result set will still include that customer's information, with
NULL values for the order_id and order_date columns. If an order has no associated customer,
the result set will include that order, with NULL values for the customer_id and name
columns.

```
SELECT customers.customer_id, customers.name, orders.order_id, orders.order_date
FROM customers
FULL OUTER JOIN orders
ON customers.customer_id = orders.customer_id;
```

The following query is a full join. Full joins retain values from the joined tables when
no match is found in the other table. The left and right tables are the first and second tables
listed in the syntax. NULL values are used to fill the "gaps" in the result set. This query
matches LISTID column values in the LISTING table (the left table) and the SALES table (the
right table). The results show that LISTIDs 2 and 3 didn't result in any sales.

```
select listing.listid, sum(pricepaid) as price, sum(commission) as comm
from listing full join sales on sales.listid = listing.listid
where listing.listid between 1 and 5
group by 1
order by 1;

listid | price  |  comm
-------+--------+--------
     1 | 728.00 | 109.20
     2 | NULL   | NULL
     3 | NULL   | NULL
     4 |  76.00 |  11.40
     5 | 525.00 |  78.75

```

The following query is a full join. This query matches LISTID column values in the LISTING
table (the left table) and the SALES table (the right table). Only rows that do not result in
any sales (LISTIDs 2 and 3) are in the results.

```
select listing.listid, sum(pricepaid) as price, sum(commission) as comm
from listing full join sales on sales.listid = listing.listid
where listing.listid between 1 and 5
and (listing.listid IS NULL or sales.listid IS NULL)
group by 1
order by 1;

listid | price  |  comm
-------+--------+--------
     2 | NULL   | NULL
     3 | NULL   | NULL

```

## [ LEFT ] SEMI

Returns values from the left side of the table reference that has a match with the right.
It's also referred to as a _left semi join_.

It returns only the rows from the left (first) table that have a matching row in the right
(second) table. It does not return any columns from the right table - only the columns from the
left table. The LEFT SEMI JOIN is useful when you want to find the rows in one table that have
a match in another table, without needing to return any data from the second table. The LEFT
SEMI JOIN is a more efficient alternative to using a subquery with an IN or EXISTS
clause.

**Syntax:**

```
SELECT column1, column2, ..., columnn
FROM table1
LEFT SEMI JOIN table2
ON table1.column = table2.column;
```

The following query will return only the customer_id and name columns from the customers
table, for the customers who have at least one order in the orders table. The result set won't
include any columns from the orders table.

```
SELECT customers.customer_id, customers.name
FROM customers
LEFT SEMI JOIN orders
ON customers.customer_id = orders.customer_id;
```

## CROSS JOIN

Returns the Cartesian product of two relations. This means that the result set will
contain all possible combinations of rows from the two tables, without any condition or filter
applied.

The CROSS JOIN is useful when you need to generate all possible combinations of data from
two tables, such as in the case of creating a report that displays all possible combinations of
customer and product information. The CROSS JOIN is different from other join types (INNER
JOIN, LEFT JOIN, etc.) because it doesn't have a join condition in the ON clause. The join
condition isn't required for a CROSS JOIN.

**Syntax:**

```
SELECT column1, column2, ..., columnn
FROM table1
CROSS JOIN table2;
```

The following query will return a result set that contains all possible combinations of
customer_id, customer_name, product_id, and product_name from the customers and products
tables. If the customers table has 10 rows and the products table has 20 rows, the result set
of the CROSS JOIN will contain 10 x 20 = 200 rows.

```
SELECT customers.customer_id, customers.name, products.product_id, products.product_name
FROM customers
CROSS JOIN products;
```

The following query is a cross join or Cartesian join of the LISTING table and the SALES
table with a predicate to limit the results. This query matches LISTID column values in the
SALES table and the LISTING table for LISTIDs 1, 2, 3, 4, and 5 in both tables. The results
show that 20 rows match the criteria.

```
select sales.listid as sales_listid, listing.listid as listing_listid
from sales cross join listing
where sales.listid between 1 and 5
and listing.listid between 1 and 5
order by 1,2;

sales_listid | listing_listid
-------------+---------------
1            | 1
1            | 2
1            | 3
1            | 4
1            | 5
4            | 1
4            | 2
4            | 3
4            | 4
4            | 5
5            | 1
5            | 1
5            | 2
5            | 2
5            | 3
5            | 3
5            | 4
5            | 4
5            | 5
5            | 5

```

## ANTI JOIN

Returns the values from the left table reference that have no match with the right table
reference. It's also referred to as a _left anti join_.

The ANTI JOIN is a useful operation when you want to find the rows in one table that don't
have a match in another table.

**Syntax:**

```
SELECT column1, column2, ..., columnn
FROM table1
LEFT ANTI JOIN table2
ON table1.column = table2.column;
```

The following query will return all the customers who haven't placed any orders.

```
SELECT customers.customer_id, customers.name
FROM customers
LEFT ANTI JOIN orders
ON customers.customer_id = orders.customer_id
WHERE orders.order_id IS NULL;
```

## NATURAL

Specifies that the rows from the two relations will implicitly be matched on equality for
all columns with matching names.

It automatically matches columns with the same name and data type between the two tables.
It doesn't require you to explicitly specify the join condition in the ON clause. It combines
all the matching columns between the two tables into the result set.

The NATURAL JOIN is a convenient shorthand when the tables you're joining have columns
with the same names and data types. However, it's generally recommended to use the more
explicit INNER JOIN ... ON syntax to make the join conditions more explicit and easier to
understand.

**Syntax:**

```
SELECT column1, column2, ..., columnn
FROM table1
NATURAL JOIN table2;
```

The following example is a natural join between two tables, `employees` and
`departments`, with the following columns:

- `employees` table: `employee_id`, `first_name`,
  `last_name`, `department_id`
- `departments` table: `department_id`, `department_name`

The following query will return a result set that includes the first name, last name, and
department name for all matching rows between the two tables, based on the
`department_id` column.

```
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
NATURAL JOIN departments d;
```

The following example is a natural join between two tables. In this case, the columns
listid, sellerid, eventid, and dateid have identical names and data types in both tables and so
are used as the join columns. The results are limited to five rows.

```
select listid, sellerid, eventid, dateid, numtickets
from listing natural join sales
order by 1
limit 5;

listid | sellerid  | eventid | dateid | numtickets
-------+-----------+---------+--------+-----------
113    | 29704     | 4699    | 2075   | 22
115    | 39115     | 3513    | 2062   | 14
116    | 43314     | 8675    | 1910   | 28
118    | 6079      | 1611    | 1862   | 9
163    | 24880     | 8253    | 1888   | 14

```
