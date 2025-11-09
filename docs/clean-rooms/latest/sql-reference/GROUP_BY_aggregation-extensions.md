# Aggregation extensions

AWS Clean Rooms supports aggregation extensions to do the work of multiple GROUP BY operations in a
single statement.

## _GROUPING SETS_

Computes one or more grouping sets in a single statement. A grouping set is the set of a
single GROUP BY clause, a set of 0 or more columns by which you can group a query's result set.
GROUP BY GROUPING SETS is equivalent to running a UNION ALL query on one result set grouped by
different columns. For example, GROUP BY GROUPING SETS((a), (b)) is equivalent to GROUP BY a
UNION ALL GROUP BY b.

The following example returns the cost of the order table's products grouped according to
both the products' categories and the kind of products sold.

```

SELECT category, product, sum(cost) as total
FROM orders
GROUP BY GROUPING SETS(category, product);

       category       |       product        | total
----------------------+----------------------+-------
 computers            |                      |  2100
 cellphones           |                      |  1610
                      | laptop               |  2050
                      | smartphone           |  1610
                      | mouse                |    50

(5 rows)
```

## _ROLLUP_

Assumes a hierarchy where preceding columns are considered the parents of subsequent
columns. ROLLUP groups data by the provided columns, returning extra subtotal rows representing
the totals throughout all levels of grouping columns, in addition to the grouped rows. For
example, you can use GROUP BY ROLLUP((a), (b)) to return a result set grouped first by a, then
by b while assuming that b is a subsection of a. ROLLUP also returns a row with the whole
result set without grouping columns.

GROUP BY ROLLUP((a), (b)) is equivalent to GROUP BY GROUPING SETS((a,b), (a), ()).

The following example returns the cost of the order table's products grouped first by
category and then product, with product as a subdivision of category.

```
SELECT category, product, sum(cost) as total
FROM orders
GROUP BY ROLLUP(category, product) ORDER BY 1,2;

       category       |       product        | total
----------------------+----------------------+-------
 cellphones           | smartphone           |  1610
 cellphones           |                      |  1610
 computers            | laptop               |  2050
 computers            | mouse                |    50
 computers            |                      |  2100
                      |                      |  3710
(6 rows)
```

## _CUBE_

Groups data by the provided columns, returning extra subtotal rows representing the
totals throughout all levels of grouping columns, in addition to the grouped rows. CUBE returns
the same rows as ROLLUP, while adding additional subtotal rows for every combination of
grouping column not covered by ROLLUP. For example, you can use GROUP BY CUBE ((a), (b)) to
return a result set grouped first by a, then by b while assuming that b is a subsection of a,
then by b alone. CUBE also returns a row with the whole result set without grouping
columns.

GROUP BY CUBE((a), (b)) is equivalent to GROUP BY GROUPING SETS((a, b), (a), (b), ()).

The following example returns the cost of the order table's products grouped first by
category and then product, with product as a subdivision of category. Unlike the preceding
example for ROLLUP, the statement returns results for every combination of grouping column.

```
SELECT category, product, sum(cost) as total
FROM orders
GROUP BY CUBE(category, product) ORDER BY 1,2;

       category       |       product        | total
----------------------+----------------------+-------
 cellphones           | smartphone           |  1610
 cellphones           |                      |  1610
 computers            | laptop               |  2050
 computers            | mouse                |    50
 computers            |                      |  2100
                      | laptop               |  2050
                      | mouse                |    50
                      | smartphone           |  1610
                      |                      |  3710
(9 rows)
```
