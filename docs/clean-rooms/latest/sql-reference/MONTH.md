# MONTH function

The MONTH function is a time extraction function that takes a time or timestamp as input
and returns the month component (a value between 0 and 12).

## Syntax

```
month(date)
```

## Arguments

_date_

A TIMESTAMP expression or a STRING of a valid timestamp format.

## Returns

The MONTH function returns an INTEGER.

## Example

The following example extracts the month component (`7`) from the input
timestamp `'2016-07-30'`.

```
SELECT month('2016-07-30');
 7
```
