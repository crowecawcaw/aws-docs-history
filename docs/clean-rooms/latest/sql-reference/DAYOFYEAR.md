# DAYOFYEAR function

The DAYOFYEAR function is a date extraction function that takes a date or timestamp as
input and returns the day of the year (a value between 1 and 366, depending on the year and
whether it's a leap year).

This function is useful when you need to work with specific components of a date or
timestamp, such as when performing date-based calculations, filtering data, or formatting
date values.

## Syntax

```
dayofyear(date)
```

## Arguments

_date_

A DATE or TIMESTAMP expression.

## Returns

The DAYOFYEAR function returns an INTEGER (between 1 and 366, depending on the year
and whether it's a leap year).

## Examples

The following example extracts the day of the year (`100`) from the input
date `'2016-04-09'`.

```
SELECT dayofyear('2016-04-09');
 100
```

The following example extracts the day of the year from the `birthday`
column of the `squirrels` table and returns the results as the output of the
SELECT statement.

```
SELECT dayofyear(birthday) FROM squirrels
```
