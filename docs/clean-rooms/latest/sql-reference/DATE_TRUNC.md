# DATE_TRUNC function

The DATE_TRUNC function truncates a timestamp expression or literal based on the date
part that you specify, such as hour, day, or month.

## Syntax

```
date_trunc(format, datetime)
```

## Arguments

_format_

The format representing the unit to be truncated to. Valid formats are as
follows:

- "YEAR", "YYYY", "YY" - truncate to the first date of the year that the
  ts falls in, the time part will be zero out
- "QUARTER" - truncate to the first date of the quarter that the ts
  falls in, the time part will be zero out
- "MONTH", "MM", "MON" - truncate to the first date of the month that
  the ts falls in, the time part will be zero out
- "WEEK" - truncate to the Monday of the week that the ts falls in, the
  time part will be zero out
- "DAY", "DD" - zero out the time part
- "HOUR" - zero out the minute and second with fraction part
- "MINUTE"- zero out the second with fraction part
- "SECOND" - zero out the second fraction part
- "MILLISECOND" - zero out the microseconds
- "MICROSECOND" - everything remains

_ts_

A datetime value

## Return type

Returns timestamp _ts_ truncated to the unit
specified by the format model

## Examples

The following example truncates a date value to the beginning of the year. The output
shows that the date "2015-03-05" has been truncated to "2015-01-01", which is the
beginning of the year 2015.

```
SELECT date_trunc('YEAR', '2015-03-05');

 date_trunc
-----------
2015-01-01
```
