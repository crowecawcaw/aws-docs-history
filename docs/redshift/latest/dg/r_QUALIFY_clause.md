Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# QUALIFY clause

The QUALIFY clause filters results of a previously computed window function according to user‑specified search conditions.
You can use the clause to apply filtering conditions to the result of a window function without using a subquery.

It is similar to the [HAVING clause](r_HAVING_clause.md "r_HAVING_clause.md"), which applies a condition to further filter rows from a WHERE clause. The difference between
QUALIFY and HAVING is that filtered results from the QUALIFY clause could be based on the result of running window
functions on the data. You can use both the QUALIFY and HAVING clauses in one query.

## Syntax

```
QUALIFY condition
```

###### Note

If you're using the QUALIFY clause directly after the FROM clause,
the FROM relation name must have an alias specified before the QUALIFY clause.

## Examples

The examples in this section use the sample data below.

```
`create table store_sales (ss_sold_date date, ss_sold_time time,
 ss_item text, ss_sales_price float);
insert into store_sales values ('2022-01-01', '09:00:00', 'Product 1', 100.0),
 ('2022-01-01', '11:00:00', 'Product 2', 500.0),
 ('2022-01-01', '15:00:00', 'Product 3', 20.0),
 ('2022-01-01', '17:00:00', 'Product 4', 1000.0),
 ('2022-01-01', '18:00:00', 'Product 5', 30.0),
 ('2022-01-02', '10:00:00', 'Product 6', 5000.0),
 ('2022-01-02', '16:00:00', 'Product 7', 5.0);`
```

The following example demonstrates how to find the two most expensive items sold after 12:00 each day.

```
`SELECT *
FROM store_sales ss
WHERE ss_sold_time > time '12:00:00'
QUALIFY row_number()
OVER (PARTITION BY ss_sold_date ORDER BY ss_sales_price DESC) <= 2`

`ss_sold_date | ss_sold_time | ss_item | ss_sales_price
--------------+--------------+-----------+----------------
 2022-01-01 | 17:00:00 | Product 4 | 1000
 2022-01-01 | 18:00:00 | Product 5 | 30
 2022-01-02 | 16:00:00 | Product 7 | 5`
```

You can then find the last item sold each day.

```
`SELECT *
FROM store_sales ss
QUALIFY last_value(ss_item)
OVER (PARTITION BY ss_sold_date ORDER BY ss_sold_time ASC
 ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) = ss_item;`

`ss_sold_date | ss_sold_time | ss_item | ss_sales_price
--------------+--------------+-----------+----------------
 2022-01-01 | 18:00:00 | Product 5 | 30
 2022-01-02 | 16:00:00 | Product 7 | 5`
```

The following example returns the same records as the previous query, the last item sold each day, but it doesn't use the QUALIFY clause.

```
`SELECT * FROM (
 SELECT *,
 last_value(ss_item)
 OVER (PARTITION BY ss_sold_date ORDER BY ss_sold_time ASC
 ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) ss_last_item
 FROM store_sales ss
)
WHERE ss_last_item = ss_item;`

 `ss_sold_date | ss_sold_time | ss_item | ss_sales_price | ss_last_item
--------------+--------------+-----------+----------------+--------------
 2022-01-02 | 16:00:00 | Product 7 | 5 | Product 7
 2022-01-01 | 18:00:00 | Product 5 | 30 | Product 5`
```
