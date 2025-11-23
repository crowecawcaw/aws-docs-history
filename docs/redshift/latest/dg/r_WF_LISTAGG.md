Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# LISTAGG window function

For each group in a query, the LISTAGG window function orders the rows for that group
according to the ORDER BY expression, then concatenates the values into a single string.

## Syntax

```
LISTAGG( *[DISTINCT] expression* [, '*delimiter*' ] )
[ WITHIN GROUP (ORDER BY *order\_list*) ]
OVER ( [PARTITION BY partition_expression] )
```

## Arguments

DISTINCT

(Optional) A clause that eliminates duplicate values from the specified
expression before concatenating. Trailing spaces are ignored, so the strings
`'a'` and `'a '` are treated as duplicates. LISTAGG
uses the first value encountered. For more information, see [Significance of trailing blanks](r_Character_types.md#r_Character_types-significance-of-trailing-blanks "r_Character_types.md#r_Character_types-significance-of-trailing-blanks").

_aggregate_expression_

Any valid expression (such as a column name) that provides the values to
aggregate. NULL values and empty strings are ignored.

_delimiter_

(Optional) The string constant to will separate the concatenated values.
The default is NULL.

WITHIN GROUP (ORDER BY _order_list_)

(Optional) A clause that specifies the sort order of the aggregated
values. Deterministic only if ORDER BY provides unique ordering. The default
is to aggregate all rows and return a single value.

OVER

A clause that specifies the window partitioning. The OVER clause cannot
contain a window ordering or window frame specification.

PARTITION BY _partition_expression_

(Optional) Sets the range of records for each group in the OVER
clause.

## Returns

If the result set is larger than 16,000,000 bytes, then LISTAGG returns the following
error:

```
Invalid operation: Result size exceeds LISTAGG limit
```

## Examples

The following examples uses the WINSALES table. For a description of the WINSALES
table, see [Sample table for window function examples](c_Window_functions.md#r_Window_function_example "c_Window_functions.md#r_Window_function_example").

The following example returns a list of seller IDs, ordered by seller ID.

```
`select listagg(sellerid)
within group (order by sellerid)
over() from winsales;`

 `listagg
------------
 11122333344
...
...
 11122333344
 11122333344
   (11 rows)`
```

The following example returns a list of seller IDs for buyer B, ordered by date.

```
`select listagg(sellerid)
within group (order by dateid)
over () as seller
from winsales
where buyerid = 'b' ;`

 `seller
---------
 3233
 3233
 3233
 3233`
```

The following example returns a comma-separated list of sales dates for buyer
B.

```
`select listagg(dateid,',')
within group (order by sellerid desc,salesid asc)
over () as dates
from winsales
where buyerid = 'b';`

 `dates
-------------------------------------------
2003-08-02,2004-04-18,2004-04-18,2004-02-12
2003-08-02,2004-04-18,2004-04-18,2004-02-12
2003-08-02,2004-04-18,2004-04-18,2004-02-12
2003-08-02,2004-04-18,2004-04-18,2004-02-12`
```

The following example uses DISTINCT to return a list of unique sales dates for
buyer B.

```
`select listagg(distinct dateid,',')
within group (order by sellerid desc,salesid asc)
over () as dates
from winsales
where buyerid = 'b';`

 `dates
--------------------------------
2003-08-02,2004-04-18,2004-02-12
2003-08-02,2004-04-18,2004-02-12
2003-08-02,2004-04-18,2004-02-12
2003-08-02,2004-04-18,2004-02-12`
```

The following example returns a comma-separated list of sales IDs for each buyer
ID.

```
`select buyerid,
listagg(salesid,',')
within group (order by salesid)
over (partition by buyerid) as sales_id
from winsales
order by buyerid;`

`+---------+-------------------------+
| buyerid | sales_id |
+---------+-------------------------+
| a | 10005,40001,40005 |
| a | 10005,40001,40005 |
| a | 10005,40001,40005 |
| b | 20001,30001,30003,30004 |
| b | 20001,30001,30003,30004 |
| b | 20001,30001,30003,30004 |
| b | 20001,30001,30003,30004 |
| c | 10001,10006,20002,30007 |
| c | 10001,10006,20002,30007 |
| c | 10001,10006,20002,30007 |
| c | 10001,10006,20002,30007 |
+---------+-------------------------+`
```

The following example demonstrates LISTAGG support with concatenated results up to 16,000,000 bytes:

```
CREATE TABLE large_data (
    id INT,
    content VARCHAR(65535)
);

INSERT INTO large_data VALUES
    (1, REPEAT('A', 65535)),
    (2, REPEAT('B', 65535)),
    (3, REPEAT('C', 65535));

SELECT LEN(LISTAGG(content, ',') WITHIN GROUP (ORDER BY id)) AS total_length
FROM large_data;

 `total_length
--------------
 196607`
```
