Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# LISTAGG function

For each group in a query, the LISTAGG aggregate function orders the rows for that
group according to the ORDER BY expression, then concatenates the values into a single
string.

## Syntax

```
LISTAGG( [DISTINCT] *aggregate\_expression* [, '*delimiter*' ] )
[ WITHIN GROUP (ORDER BY *order\_list*) ]
```

## Arguments

DISTINCT

A clause that eliminates duplicate values from the specified
expression before concatenating. Trailing spaces are ignored. For example, the strings
`'a'` and `'a '` are treated as duplicates. LISTAGG
uses the first value encountered. For more information, see [Significance of trailing blanks](r_Character_types.md#r_Character_types-significance-of-trailing-blanks "r_Character_types.md#r_Character_types-significance-of-trailing-blanks").

_aggregate_expression_

Any valid expression, such as a column name, that provides the values to
aggregate. NULL values and empty strings are ignored.

_delimiter_

The string constant to separate the concatenated values. The
default is NULL.

_WITHIN GROUP (ORDER BY order_list)_

A clause that specifies the sort order of the aggregated
values.

## Returns

VARCHAR(MAX). If the result set is larger than the maximum VARCHAR size, LISTAGG returns the following error:

```
Invalid operation: Result size exceeds LISTAGG limit
```

## Usage notes

- If a statement includes multiple LISTAGG functions that use WITHIN GROUP clauses,
  each WITHIN GROUP clause must use the same ORDER BY values.

For example, the following statement returns an error.

```
SELECT LISTAGG(sellerid)
WITHIN GROUP (ORDER BY dateid) AS sellers,
LISTAGG(dateid)
WITHIN GROUP (ORDER BY sellerid) AS dates
FROM sales;
```

The following statements runs successfully.

```
SELECT LISTAGG(sellerid)
WITHIN GROUP (ORDER BY dateid) AS sellers,
LISTAGG(dateid)
WITHIN GROUP (ORDER BY dateid) AS dates
FROM sales;

SELECT LISTAGG(sellerid)
WITHIN GROUP (ORDER BY dateid) AS sellers,
LISTAGG(dateid) AS dates
FROM sales;
```

- You can't use the LISTAGG, PERCENTILE_CONT, and MEDIAN aggregate functions with other
  distinct aggregate functions.

## Examples

The following example aggregates seller IDs, ordered by seller ID.

```
SELECT LISTAGG(sellerid, ', ')
WITHIN GROUP (ORDER BY sellerid)
FROM sales
WHERE eventid = 4337;

`listagg
----------------------------------------------------------------------------------------------------------------------------------------
380, 380, 1178, 1178, 1178, 2731, 8117, 12905, 32043, 32043, 32043, 32432, 32432, 38669, 38750, 41498, 45676, 46324, 47188, 47188, 48294`
```

The following example uses DISTINCT to return a list of unique seller IDs.

```
SELECT LISTAGG(DISTINCT sellerid, ', ')
WITHIN GROUP (ORDER BY sellerid)
FROM sales
WHERE eventid = 4337;

`listagg
-------------------------------------------------------------------------------------------
380, 1178, 2731, 8117, 12905, 32043, 32432, 38669, 38750, 41498, 45676, 46324, 47188, 48294`
```

The following example aggregates seller IDs in date order.

```
SELECT LISTAGG(sellerid, ', ')
WITHIN GROUP (ORDER BY dateid)
FROM sales
WHERE eventid = 4337;

   listagg
-----------------------------------------------------------------------------------------------------------------------------------------
 41498, 47188, 47188, 1178, 1178, 1178, 380, 45676, 46324, 48294, 32043, 32043, 32432, 12905, 8117, 38750, 2731, 32432, 32043, 380, 38669
```

The following example returns a pipe-separated list of sales dates for the buyer with an ID of 660.

```
SELECT LISTAGG(
    (SELECT caldate FROM date WHERE date.dateid=sales.dateid), ' | '
)
WITHIN GROUP (ORDER BY sellerid DESC, salesid ASC)
FROM sales
WHERE buyerid = 660;

 `listagg
-------------------------------------------------
2008-07-16 | 2008-07-09 | 2008-01-01 | 2008-10-26`
```

The following example returns a comma-separated list of sales IDs for the buyer IDs 660, 661, and 662.

```
SELECT buyerid,
LISTAGG(salesid,', ')
WITHIN GROUP (ORDER BY salesid) AS sales_id
FROM sales
WHERE buyerid BETWEEN 660 AND 662
GROUP BY buyerid
ORDER BY buyerid;

`buyerid | sales_id
--------+-----------------------------------------------------
660 | 32872, 33095, 33514, 34548
661 | 19951, 20517, 21695, 21931
662 | 3318, 3823, 4215, 51980, 53202, 55908, 57832, 171603`
```
