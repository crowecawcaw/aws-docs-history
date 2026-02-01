Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Examples

This section contains examples for using HyperLogLog with Amazon Redshift.

###### Topics

- [Example: Return cardinality in a
  subquery](#hll-examples-subquery "#hll-examples-subquery")
- [Example: Return an HLLSKETCH type from
  combined sketches in a subquery](#hll-examples-combined-subquery "#hll-examples-combined-subquery")
- [Example: Return a HyperLogLog sketch
  from combining multiple sketches](#hll-examples-multiple-sketches "#hll-examples-multiple-sketches")
- [Example: Generate HyperLogLog sketches over S3 data using external tables](#hll-examples-cache-sketches "#hll-examples-cache-sketches")

## Example: Return cardinality in a

subquery

The following example returns the cardinality for each sketch in a subquery for a table
named _Sales_.

```
CREATE TABLE Sales (customer VARCHAR, country VARCHAR, amount BIGINT);
INSERT INTO Sales VALUES ('David Joe', 'Greece', 14.5),  ('David Joe', 'Greece', 19.95), ('John Doe', 'USA', 29.95), ('John Doe', 'USA', 19.95), ('George Spanos', 'Greece', 9.95), ('George Spanos', 'Greece', 2.95);
```

The following query generates an HLL sketch for the customers of each country and extracts the cardinality. This shows unique customers from each country.

```
SELECT hll_cardinality(sketch), country
FROM (SELECT hll_create_sketch(customer) AS sketch, country
        FROM Sales
        GROUP BY country) AS hll_subquery;

hll_cardinality | country
----------------+---------
            1   | USA
            2   | Greece
 ...
```

## Example: Return an HLLSKETCH type from

combined sketches in a subquery

The following example returns a single HLLSKETCH type that represents the combination
of individual sketches from a subquery. The sketches are combined by using the
HLL_COMBINE aggregate function.

```
SELECT hll_combine(sketch)
FROM (SELECT hll_create_sketch(customer) AS sketch
        FROM Sales
        GROUP BY country) AS hll_subquery

                                        hll_combine
--------------------------------------------------------------------------------------------
 {"version":1,"logm":15,"sparse":{"indices":[29808639,35021072,47612452],"values":[1,1,1]}}
(1 row)

```

## Example: Return a HyperLogLog sketch

from combining multiple sketches

For the following example, suppose that the table `page-users` stores
preaggregated sketches for each page that users visited on a given website. Each row
in this table contains a HyperLogLog sketch that represents all user IDs that show
the visited pages.

```
page_users
-- +----------------+-------------+--------------+
-- | _PARTITIONTIME | page         | sketch |
-- +----------------+-------------+--------------+
-- | 2019-07-28     | homepage     | CHAQkAQYA... |
-- | 2019-07-28     | Product A    | CHAQxPnYB... |
-- +----------------+-------------+--------------+
```

The following example unions the preaggregated multiple sketches and generates a single
sketch. This sketch encapsulates the collective cardinality that each sketch
encapsulates.

```
SELECT hll_combine(sketch) as sketch
FROM page_users
```

The output looks similar to the following.

```
-- +-----------------------------------------+
-- | sketch |
-- +-----------------------------------------+
-- | CHAQ3sGoCxgCIAuCB4iAIBgTIBgqgIAgAwY.... |
-- +-----------------------------------------+
```

When a new sketch is created, you can use the HLL_CARDINALITY function to get the
collective distinct values, as shown following.

```
SELECT hll_cardinality(sketch)
FROM (
  SELECT
  hll_combine(sketch) as sketch
  FROM page_users
) AS hll_subquery

```

The output looks similar to the following.

```
-- +-------+
-- | count |
-- +-------+
-- | 54356 |
-- +-------+
```

## Example: Generate HyperLogLog sketches over S3 data using external tables

The following examples cache HyperLogLog sketches to avoid directly accessing Amazon S3
for cardinality estimation.

You can preaggregate and cache HyperLogLog sketches in external tables defined to
hold Amazon S3 data. By doing this, you can extract cardinality estimates without
accessing the underlying base data.

For example, suppose that you have unloaded a set of tab-delimited text files into
Amazon S3. You run the following query to define an external table named
`sales` in the Amazon Redshift external schema named `spectrum`.
The Amazon S3 bucket for this example is in the US East (N. Virginia) AWS Region.

```
create external table spectrum.sales(
salesid integer,
listid integer,
sellerid smallint,
buyerid smallint,
eventid integer,
dateid integer,
qtysold integer,
pricepaid decimal(8,2),
commission decimal(8,2),
saletime timestamp)
row format delimited
fields terminated by '\t' stored as textfile
location 's3://redshift-downloads/tickit/spectrum/sales/';
```

Suppose that you want to compute the distinct buyers who purchased an item on
arbitrary dates. To do so, the following example generates sketches for the buyer IDs
for each day of the year and stores the result in the Amazon Redshift table
`hll_sales`.

```
CREATE TABLE hll_sales AS
SELECT saletime, hll_create_sketch(buyerid) AS sketch
FROM spectrum.sales
GROUP BY saletime;

SELECT TOP 5 * FROM hll_sales;
```

The output looks similar to the following.

```
-- hll_sales

-- | saletime        | sketch                                                              |
-- +-----------------+---------------------------------------------------------------------+
-- | 7/22/2008 8:30  | {"version":1,"logm":15,"sparse":{"indices":[9281416],"values":[1]}}
-- | 2/19/2008 0:38  | {"version":1,"logm":15,"sparse":{"indices":[48735497],"values":[3]}}
-- | 11/5/2008 4:49  | {"version":1,"logm":15,"sparse":{"indices":[27858661],"values":[1]}}
-- | 10/27/2008 4:08 | {"version":1,"logm":15,"sparse":{"indices":[65295430],"values":[2]}}
-- | 2/16/2008 9:37  | {"version":1,"logm":15,"sparse":{"indices":[56869618],"values":[2]}}
-- +---------------- +---------------------------------------------------------------------+
```

The following query shows the estimated number of distinct buyers that purchased
an item during the Friday after Thanksgiving in 2008.

```
SELECT hll_cardinality(hll_combine(sketch)) as distinct_buyers
FROM hll_sales
WHERE trunc(saletime) = '2008-11-28';
```

The output looks similar to the following.

```
distinct_buyers
---------------
386
```

Suppose that you want the number of distinct users who bought an item on a certain
range of dates. An example might be from the Friday after Thanksgiving to the following
Monday. To get this, the following query uses the `hll_combine` aggregate
function. This function enables you to avoid double-counting buyers who purchased an
item on more than one day of the selected range.

```
SELECT hll_cardinality(hll_combine(sketch)) as distinct_buyers
FROM hll_sales
WHERE saletime BETWEEN '2008-11-28' AND '2008-12-01';
```

The output looks similar to the following.

```
distinct_buyers
---------------
1166
```

To keep the `hll_sales` table up-to-date, run the following query at the
end of each day. Doing this generates an HyperLogLog sketch based on the IDs of
buyers that purchased an item today and adds it to the `hll_sales`
table.

```
INSERT INTO hll_sales
SELECT saletime, hll_create_sketch(buyerid)
FROM spectrum.sales
WHERE TRUNC(saletime) = to_char(GETDATE(), 'YYYY-MM-DD')
GROUP BY saletime;
```
