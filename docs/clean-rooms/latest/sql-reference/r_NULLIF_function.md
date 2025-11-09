# NULLIF function

Compares two arguments and returns null if the arguments are equal. If they aren't
equal, the first argument is returned.

## Syntax

The NULLIF expression compares two arguments and returns null if the arguments are
equal. If they aren't equal, the first argument is returned. This expression is the
inverse of the NVL or COALESCE expression.

```
NULLIF ( *expression1*, *expression2* )
```

## Arguments

_expression1, expression2_

The target columns or expressions that are compared. The return type is the
same as the type of the first expression. The default column name of the NULLIF
result is the column name of the first expression.

## Examples

In the following example, the query returns the string `first` because the
arguments are not equal.

```
`SELECT NULLIF('first', 'second');`
`case
-------
first`
```

In the following example, the query returns `NULL` because the string
literal arguments are equal.

```
`SELECT NULLIF('first', 'first');`
`case
-------
NULL`
```

In the following example, the query returns `1` because the integer
arguments are not equal.

```
`SELECT NULLIF(1, 2);`
`case
-------
1`
```

In the following example, the query returns `NULL` because the integer
arguments are equal.

```
`SELECT NULLIF(1, 1);`
`case
-------
NULL`
```

In the following example, the query returns null when the LISTID and SALESID values
match:

```
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
        |       1
(9 rows)
```
