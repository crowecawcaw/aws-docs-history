# COALESCE expression

A COALESCE expression returns the value of the first expression in the
list that is not null. If all expressions are null, the result is null. When a non-null
value is found, the remaining expressions in the list are not evaluated.

This type of expression is useful when you want to return a backup value for something
when the preferred value is missing or null. For example, a query might return one of three
phone numbers (cell, home, or work, in that order), whichever is found first in the table
(not null).

## Syntax

```
COALESCE (`expression`, `expression`, ... )
```

## Examples

Apply COALESCE expression to two columns.

```
select coalesce(start_date, end_date)
from datetable
order by 1;
```

The default column name for an NVL expression is COALESCE. The
following query returns the same results.

```
select coalesce(start_date, end_date) from datetable order by 1;
```
