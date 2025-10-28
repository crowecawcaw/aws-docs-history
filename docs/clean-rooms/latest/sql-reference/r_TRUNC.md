# TRUNC function

The TRUNC function truncates numbers to the previous integer or decimal.

The TRUNC function can optionally include a second argument as an integer to indicate
the number of decimal places for rounding, in either direction. When you don't provide
the second argument, the function rounds to the nearest whole number. When the second
argument *>n*is specified, the function rounds to the nearest number
with _>n_ decimal places of precision. This function also truncates a
timestamp and returns a date.

## Syntax

```
TRUNC (*number* [ , *integer* ] |
*timestamp* )
```

## Arguments

_number_

A number or expression that evaluates to a number. It can be the
DECIMAL
or
FLOAT8
type. AWS Clean Rooms can convert other data types per the implicit conversion rules.

_integer_ (optional)

An integer that indicates the number of decimal places of precision, in
either direction. If no integer is provided, the number is truncated as a whole
number; if an integer is specified, the number is truncated to the specified
decimal place.

_timestamp_

The function can also return the date from a timestamp. (To return a
timestamp value with `00:00:00` as the time, cast the function
result to a timestamp.)

## Return type

TRUNC returns the same data type as the first input argument. For timestamps, TRUNC
returns a date.

## Examples

Truncate the commission paid for a given sales transaction.

```
select commission, trunc(commission)
from sales where salesid=784;

commission | trunc
-----------+-------
    111.15 |   111

(1 row)
```

Truncate the same commission value to the first decimal place.

```
select commission, trunc(commission,1)
from sales where salesid=784;

commission | trunc
-----------+-------
    111.15 | 111.1

(1 row)
```

Truncate the commission with a negative value for the second argument;
`111.15` is rounded down to `110`.

```
select commission, trunc(commission,-1)
from sales where salesid=784;

commission | trunc
-----------+-------
    111.15 |   110
(1 row)
```

Return the date portion from the result of the SYSDATE function (which returns a
timestamp):

```
select sysdate;

timestamp
----------------------------
2011-07-21 10:32:38.248109
(1 row)

select trunc(sysdate);

trunc
------------
2011-07-21
(1 row)
```

Apply the TRUNC function to a TIMESTAMP column. The return type is a date.

```
select trunc(starttime) from event
order by eventid limit 1;

trunc
------------
2008-01-25
(1 row)
```
