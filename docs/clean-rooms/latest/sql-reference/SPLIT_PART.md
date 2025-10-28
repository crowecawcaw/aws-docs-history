# SPLIT_PART function

Splits a string on the specified delimiter and returns the part at the specified
position.

## Syntax

```
SPLIT_PART(*string*, *delimiter*, *position*)
```

## Arguments

_string_

A string column, expression, or string literal to be split. The string can
be CHAR or VARCHAR.

_delimiter_

The delimiter string indicating sections of the input
_string_.

If _delimiter_ is a literal, enclose it in single
quotation marks.

_position_

Position of the portion of _string_ to return (counting
from 1). Must be an integer greater than 0. If _position_ is
larger than the number of string portions, SPLIT_PART returns an empty string.
If _delimiter_ is not found in _string_,
then the returned value contains the contents of the specified part, which
might be the entire _string_ or an empty value.

## Return type

A CHAR or VARCHAR string, the same as the _string_
parameter.

## Examples

The following example splits a string literal into parts using the `$`
delimiter and returns the second part.

```
`select split_part('abc$def$ghi','$',2)`
`split_part
----------
def`
```

The following example splits a string literal into parts using the `$`
delimiter. It returns an empty string because part `4` is not found.

```
`select split_part('abc$def$ghi','$',4)`
`split_part
----------`
```

The following example splits a string literal into parts using the `#`
delimiter. It returns the entire string, which is the first part, because the delimiter
is not found.

```
`select split_part('abc$def$ghi','#',1)`
`split_part
------------
abc$def$ghi`
```

The following example splits the timestamp field LISTTIME into year, month, and day
components.

```
`select listtime, split_part(listtime,'-',1) as year,
split_part(listtime,'-',2) as month,
split_part(split_part(listtime,'-',3),' ',1) as day
from listing limit 5;`
`listtime | year | month | day
---------------------+------+-------+------
 2008-03-05 12:25:29 | 2008 | 03 | 05
 2008-09-09 08:03:36 | 2008 | 09 | 09
 2008-09-26 05:43:12 | 2008 | 09 | 26
 2008-10-04 02:00:30 | 2008 | 10 | 04
 2008-01-06 08:33:11 | 2008 | 01 | 06`
```

The following example selects the LISTTIME timestamp field and splits it on the
`'-'` character to get the month (the second part of the LISTTIME string),
then counts the number of entries for each month:

```
`select split_part(listtime,'-',2) as month, count(*)
from listing
group by split_part(listtime,'-',2)
order by 1, 2;`
`month | count
-------+-------
 01 | 18543
 02 | 16620
 03 | 17594
 04 | 16822
 05 | 17618
 06 | 17158
 07 | 17626
 08 | 17881
 09 | 17378
 10 | 17756
 11 | 12912
 12 | 4589`
```
