Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# NULLIF function

## Syntax

The NULLIF expression compares two arguments and returns null if the arguments are
equal. If they are not equal, the first argument is returned. This expression is the
inverse of the NVL or COALESCE expression.

```
NULLIF ( *expression1*, *expression2* )
```

## Arguments

_expression1, expression2_

The target columns or expressions that are compared. The return type is
the same as the type of the first expression. The default column name of the
NULLIF result is the column name of the first expression.

## Examples

In the following example, the query returns the string `first` because the arguments are not equal.

```
`SELECT NULLIF('first', 'second');`
`case
-------
first`
```

In the following example, the query returns `NULL` because the string literal arguments are equal.

```
`SELECT NULLIF('first', 'first');`
`case
-------
NULL`
```

In the following example, the query returns `1` because the integer arguments are not equal.

```
`SELECT NULLIF(1, 2);`
`case
-------
1`
```

In the following example, the query returns `NULL` because the integer arguments are equal.

```
`SELECT NULLIF(1, 1);`
`case
-------
NULL`
```

In the following example, the query returns null when the LISTID and SALESID
values match:

````
select nullif(listid,salesid), salesid
from sales where salesid<10 order by 1, 2 desc;

listid  | salesid
--------+---------
     4  |       2
     5  |       4
     5  |       3
     6  |       5
     10 |       9
     10 |       8
     10 |       7
     10 |       6
|       1 (9 rows) ``` You can use NULLIF to ensure that empty strings are always returned as nulls. In the example below, the NULLIF expression returns either a null value or a string that contains at least one character. ``` insert into category values(0,'','Special','Special'); select nullif(catgroup,'') from category where catdesc='Special'; catgroup ---------- null (1 row) ``` NULLIF ignores trailing blanks. If a string is not empty but contains blanks, NULLIF still returns null: ``` create table nulliftest(c1 char(2), c2 char(2)); insert into nulliftest values ('a','a '); insert into nulliftest values ('b','b'); select nullif(c1,c2) from nulliftest; c1 ------ null null (2 rows) ```
````
