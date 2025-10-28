# dateDiff

`dateDiff` returns the difference in days between two date fields. If
you include a value for the period, `dateDiff` returns the difference in
the period interval, rather than in days.

## Syntax

```
dateDiff(`date1`, `date2`,[`period`])
```

## Arguments

`dateDiff` takes two dates as arguments. Specifying a period is
optional.

_date 1_

The first date in the comparison. A date field or a call to
another function that outputs a date.

_date 2_

The second date in the comparison. A date field or a call to
another function that outputs a date.

_period_

The period of difference that you want returned, enclosed in
quotes. Valid periods are as follows:

- YYYY: This returns the year portion of the date.
- Q: This returns the date of the first day of the quarter
  that the date belongs to.
- MM: This returns the month portion of the date.
- DD: This returns the day portion of the date.
- WK: This returns the week portion of the date. The week
  starts on Sunday in Amazon Quick Suite.
- HH: This returns the hour portion of the date.
- MI: This returns the minute portion of the date.
- SS: This returns the second portion of the date.
- MS: This returns the millisecond portion of the
  date.

## Return type

Integer

## Example

The following example returns the difference between two dates.

```
dateDiff(orderDate, shipDate, "MM")
```

The following are the given field values.

```
orderDate          shipdate
=============================
01/01/18            03/05/18
09/13/17            10/20/17
```

For these field values, the following values are returned.

```
2
1
```
