# JOIN clause

A SQL JOIN clause is used to combine the data from two or more tables based on common
fields. The results might or might not change depending on the join method specified. Left and
right outer joins retain values from one of the joined tables when no match is found in the other
table.

The combination of the JOIN type and the join condition determines which rows are included
in the final result set. The SELECT and WHERE clauses then control which columns are returned and
how the rows are filtered. Understanding the different JOIN types and how to use them effectively
is a crucial skill in SQL, because it allows you to combine data from multiple tables in a
flexible and powerful way.

## Syntax

```
SELECT column1, column2, ..., columnn
FROM table1
join_type table2
ON table1.column = table2.column;

```

## Parameters

_SELECT column1, column2, ..., columnN_

The columns you want to include in the result set. You can select columns from either or
both of the tables involved in the JOIN.

_FROM table1_

The first (left) table in the JOIN operation.

_[JOIN | INNER JOIN | LEFT [OUTER] JOIN | RIGHT [OUTER] JOIN | FULL [OUTER] JOIN]
table2:_

The type of JOIN to be performed. JOIN or INNER JOIN returns only the rows with matching
values in both tables.

LEFT [OUTER] JOIN returns all rows from the left table, with matching rows from the
right table.

RIGHT [OUTER] JOIN returns all rows from the right table, with matching rows from the
left table.

FULL [OUTER] JOIN returns all rows from both tables, regardless of whether there is a
match or not.

CROSS JOIN creates a Cartesian product of the rows from the two tables.

_ON table1.column = table2.column_

The join condition, which specifies how the rows in the two tables are matched. The join
condition can be based on one or more columns.

_WHERE condition:_

An optional clause that can be used to filter the result set further, based on a
specified condition.

## Example

The following example is a join between two tables with the USING clause. In this case, the
columns listid and eventid are used as the join columns. The results are limited to five
rows.

```
select listid, listing.sellerid, eventid, listing.dateid, numtickets
from listing join sales
using (listid, eventid)
order by 1
limit 5;

listid | sellerid | eventid | dateid | numtickets
-------+----------+---------+--------+-----------
1      | 36861    | 7872    | 1850   | 10
4      | 8117     | 4337    | 1970   | 8
5      | 1616     | 8647    | 1963   | 4
5      | 1616     | 8647    | 1963   | 4
6      | 47402    | 8240    | 2053   | 18

```
