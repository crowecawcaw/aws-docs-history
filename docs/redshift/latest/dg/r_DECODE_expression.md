Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DECODE function

A DECODE expression replaces a specific value with either another specific value or a
default value, depending on the result of an equality condition. This operation is
equivalent to the operation of a simple CASE expression or an IF-THEN-ELSE
statement.

## Syntax

```
DECODE ( *expression*, *search*, *result* [, *search*, *result* ]... [ ,*default* ] )
```

This type of expression is useful for replacing abbreviations or codes that are
stored in tables with meaningful business values that are needed for reports.

## Parameters

_expression_

The source of the value that you want to compare, such as a column in a
table.

_search_

The target value that is compared against the source expression, such as
a numeric value or a character string. The search expression must evaluate
to a single fixed value. You cannot specify an expression that evaluates to
a range of values, such as `age between 20 and 29`; you need to
specify separate search/result pairs for each value that you want to
replace.

The data type of all instances of the search expression must be the same
or compatible. The _expression_ and
_search_ parameters must also be compatible.

_result_

The replacement value that query returns when the expression matches the
search value. You must include at least one search/result pair in the DECODE
expression.

The data types of all instances of the result expression must be the same
or compatible. The _result_ and
_default_ parameters must also be compatible.

_default_

An optional default value that is used for cases when the search
condition fails. If you do not specify a default value, the DECODE
expression returns NULL.

## Usage notes

If the _expression_ value and the _search_
value are both NULL, the DECODE result is the corresponding
_result_ value. For an illustration of this use of the
function, see the Examples section.

When used this way, DECODE is similar to [NVL2 function](r_NVL2.md "r_NVL2.md"), but there are some differences. For a description of
these differences, see the NVL2 usage notes.

## Examples

When the value `2008-06-01` exists in the caldate column of
datetable, the following example replaces it with `June 1st, 2008`. The
example replaces all other caldate values with NULL.

```
select decode(caldate, '2008-06-01', 'June 1st, 2008')
from datetable where month='JUN' order by caldate;

case
----------------
June 1st, 2008

...
(30 rows)
```

The following example uses a DECODE expression to convert the five abbreviated
CATNAME columns in the CATEGORY table to full names and convert other values in the
column to `Unknown`.

```
select catid, decode(catname,
'NHL', 'National Hockey League',
'MLB', 'Major League Baseball',
'MLS', 'Major League Soccer',
'NFL', 'National Football League',
'NBA', 'National Basketball Association',
'Unknown')
from category
order by catid;

catid  |	case
-------+---------------------------------
1      | Major League Baseball
2      | National Hockey League
3      | National Football League
4      | National Basketball Association
5      | Major League Soccer
6      | Unknown
7      | Unknown
8      | Unknown
9      | Unknown
10     | Unknown
11     | Unknown
(11 rows)

```

Use a DECODE expression to find venues in Colorado and Nevada with NULL in the
VENUESEATS column; convert the NULLs to zeroes. If the VENUESEATS column is not NULL,
return 1 as the result.

```
select venuename, venuestate, decode(venueseats,null,0,1)
from venue
where venuestate in('NV','CO')
order by 2,3,1;

venuename	              | venuestate     | case
------------------------------+----------------+-----------
Coors Field                   |	CO	       |   1
Dick's Sporting Goods Park    |	CO	       |   1
Ellie Caulkins Opera House    |	CO	       |   1
INVESCO Field		      |	CO	       |   1
Pepsi Center		      |	CO	       |   1
Ballys Hotel		      |	NV	       |   0
Bellagio Hotel                |	NV	       |   0
Caesars Palace                |	NV	       |   0
Harrahs Hotel                 |	NV	       |   0
Hilton Hotel                  |	NV	       |   0
...
(20 rows)

```
