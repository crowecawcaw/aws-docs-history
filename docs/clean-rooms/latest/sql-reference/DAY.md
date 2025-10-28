# DAY function

The DAY function returns the day of month of the date/timestamp.

Date extraction functions are useful when you need to work with specific components of a
date or timestamp, such as when performing date-based calculations, filtering data, or
formatting date values.

## Syntax

```
day(date)
```

## Arguments

_date_

A DATE or TIMESTAMP expression.

## Returns

The DAY function returns an INTEGER.

## Examples

The following example extracts the day of the month (`30`) from the input
date `'2009-07-30'`.

```
SELECT day('2009-07-30');
 30
```

The following example extracts the day of the month from the `birthday`
column of the `squirrels` table and returns the results as the output of the
SELECT statement. The output of this query will be a list of day values, one for each
row in the `squirrels` table, representing the day of the month for each
squirrel's birthday.

```
SELECT day(birthday) FROM squirrels
```
