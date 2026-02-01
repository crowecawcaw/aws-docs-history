Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# APPROXIMATE PERCENTILE_DISC

function

APPROXIMATE PERCENTILE_DISC is an inverse distribution function that assumes a
discrete distribution model. It takes a percentile value and a sort specification and
returns an element from the given set. Approximation enables the function to run much
faster, with a low relative error of around 0.5 percent.

For a given _percentile_ value, APPROXIMATE PERCENTILE_DISC uses a
quantile summary algorithm to approximate the discrete percentile of the expression in
the ORDER BY clause. APPROXIMATE PERCENTILE_DISC returns the value with the smallest
cumulative distribution value (with respect to the same sort specification) that is
greater than or equal to _percentile_.

## Syntax

```
APPROXIMATE  PERCENTILE_DISC ( *percentile* )
WITHIN GROUP (ORDER BY *expr*)
```

## Arguments

_percentile_

Numeric constant between 0 and 1. Nulls are ignored in the
calculation.

WITHIN GROUP ( ORDER BY _expr_)

Clause that specifies numeric or date/time values to sort and compute the
percentile over.

## Returns

The same data type as the ORDER BY expression in the WITHIN GROUP clause.

## Usage notes

If the APPROXIMATE PERCENTILE_DISC statement includes a GROUP BY clause, the
result set is limited. The limit varies based on node type and the number of nodes.
If the limit is exceeded, the function fails and returns the following error.

```
GROUP BY limit for approximate percentile_disc exceeded.
```

If you need to evaluate more groups than the limit permits, consider using [PERCENTILE_CONT function](r_PERCENTILE_CONT.md "r_PERCENTILE_CONT.md").

## Examples

The following example returns the number of sales, total sales, and fiftieth
percentile value for the top 10 dates.

```
select top 10 date.caldate,
count(totalprice), sum(totalprice),
approximate percentile_disc(0.5)
within group (order by totalprice)
from listing
join date on listing.dateid = date.dateid
group by date.caldate
order by 3 desc;

caldate    | count | sum        | percentile_disc
-----------+-------+------------+----------------
2008-01-07 |   658 | 2081400.00 |         2020.00
2008-01-02 |   614 | 2064840.00 |         2178.00
2008-07-22 |   593 | 1994256.00 |         2214.00
2008-01-26 |   595 | 1993188.00 |         2272.00
2008-02-24 |   655 | 1975345.00 |         2070.00
2008-02-04 |   616 | 1972491.00 |         1995.00
2008-02-14 |   628 | 1971759.00 |         2184.00
2008-09-01 |   600 | 1944976.00 |         2100.00
2008-07-29 |   597 | 1944488.00 |         2106.00
2008-07-23 |   592 | 1943265.00 |         1974.00
```
