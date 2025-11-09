# Date, time, and timestamp literals

Following are rules for working with date, time, and timestamp literals that are
supported by AWS Clean Rooms Spark SQL.

## Dates

The following table shows input dates that are valid examples of literal date
values that you can load into AWS Clean Rooms tables. The default `MDY DateStyle`
mode is assumed to be in effect. This mode means that the month value precedes the
day value in strings such as `1999-01-08` and `01/02/00`.

###### Note

A date or timestamp literal must be enclosed in quotation marks when you load
it into a table.

| Input date      | Full date                                                                       |
| --------------- | ------------------------------------------------------------------------------- |
| January 8, 1999 | January 8, 1999                                                                 |
| 1999-01-08      | January 8, 1999                                                                 |
| 1/8/1999        | January 8, 1999                                                                 |
| 01/02/00        | January 2, 2000                                                                 |
| 2000-Jan-31     | January 31, 2000                                                                |
| Jan-31-2000     | January 31, 2000                                                                |
| 31-Jan-2000     | January 31, 2000                                                                |
| 20080215        | February 15, 2008                                                               |
| 080215          | February 15, 2008                                                               |
| 2008.366        | December 31, 2008 (the three-digit part of date must<br>be between 001 and 366) |

## Times

The following table shows input times that are valid examples of literal time
values that you can load into AWS Clean Rooms tables.

| Input times  | Description (of time part)                              |
| ------------ | ------------------------------------------------------- |
| 04:05:06.789 | 4:05 AM and 6.789 seconds                               |
| 04:05:06     | 4:05 AM and 6 seconds                                   |
| 04:05        | 4:05 AM exactly                                         |
| 040506       | 4:05 AM and 6 seconds                                   |
| 04:05 AM     | 4:05 AM exactly; AM is optional                         |
| 04:05 PM     | 4:05 PM exactly; the hour value must be less than<br>12 |
| 16:05        | 4:05 PM exactly                                         |

## Special datetime

values

The following table shows special values that can be used as datetime literals and
as arguments to date functions. They require single quotation marks and are converted
to regular timestamp values during query processing.

| Special value | Description                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------- |
| `now`         | Evaluates to the start time of the current transaction<br>and returns a timestamp with microsecond precision. |
| `today`       | Evaluates to the appropriate date and returns a<br>timestamp with zeroes for the time parts.                  |
| `tomorrow`    | Evaluates to the appropriate date and returns a timestamp with<br>zeroes for the time<br>parts.               |
| `yesterday`   | Evaluates to the appropriate date and returns a timestamp with<br>zeroes for the time<br>parts.               |

The following examples show how `now` and `today` work with
the DATEADD function.

```
select dateadd(day,1,'today');

date_add
---------------------
2009-11-17 00:00:00
(1 row)

select dateadd(day,1,'now');

date_add
----------------------------
2009-11-17 10:45:32.021394
(1 row)
```
