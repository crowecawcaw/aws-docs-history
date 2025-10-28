# DAYOFWEEK function

The DAYOFWEEK function takes a date or timestamp as input and returns the day of the
week as a number (1 for Sunday, 2 for Monday, ..., 7 for Saturday).

This date extraction function is useful when you need to work with specific components
of a date or timestamp, such as when performing date-based calculations, filtering data, or
formatting date values.

## Syntax

```
dayofweek(date)
```

## Arguments

_date_

A DATE or TIMESTAMP expression.

## Returns

The DAYOFWEEK function returns an INTEGER where

1 = Sunday

2 = Monday

3 = Tuesday

4 = Wednesday

5 = Thursday

6 = Friday

7 = Saturday

## Examples

The following example extracts the day of the week from this date, which is 5
(representing Thursday).

```
SELECT dayofweek('2009-07-30');
 5
```

The following example extracts the day of the week from the `birthday`
column of the `squirrels` table and returns the results as the output of the
SELECT statement. The output of this query will be a list of day of the week values, one
for each row in the `squirrels` table, representing the day of the week for
each squirrel's birthday.

```
SELECT dayofweek(birthday) FROM squirrels
```
