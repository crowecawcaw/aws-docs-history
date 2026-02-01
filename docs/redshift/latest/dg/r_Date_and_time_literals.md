Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Date, time, and timestamp

literals

Following are rules for working with date, time, and timestamp literals
supported by Amazon Redshift.

## Dates

The following input dates are all valid examples of literal date values
for the DATE data type that you can load into Amazon Redshift tables. The default
`MDY DateStyle` mode is assumed to be in effect. This mode
means that the month value precedes the day value in strings such as
`1999-01-08` and `01/02/00`.

###### Note

A date or timestamp literal must be enclosed in quotation marks when
you load it into a table.

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
| 2008.366        | December 31, 2008 (the three-digit part of<br>date must be between 001 and 366) |

## Times

The following input times are all valid examples of literal time values
for the TIME and TIMETZ data types that you can load into Amazon Redshift tables.

| Input times  | Description (of time part)                              |
| ------------ | ------------------------------------------------------- |
| 04:05:06.789 | 4:05 AM and 6.789 seconds                               |
| 04:05:06     | 4:05 AM and 6 seconds                                   |
| 04:05        | 4:05 AM exactly                                         |
| 040506       | 4:05 AM and 6 seconds                                   |
| 04:05 AM     | 4:05 AM exactly; AM is optional                         |
| 04:05 PM     | 4:05 PM exactly; the hour value must be less<br>than 12 |
| 16:05        | 4:05 PM exactly                                         |

## Timestamps

The following input timestamps are all valid examples of literal time
values for the TIMESTAMP and TIMESTAMPTZ data types that you can load into
Amazon Redshift tables. All of the valid date literals can be combined with the
following time literals.

| Input timestamps (concatenated dates and<br>times) | Description (of time part)                              |
| -------------------------------------------------- | ------------------------------------------------------- |
| 20080215 04:05:06.789                              | 4:05 AM and 6.789 seconds                               |
| 20080215 04:05:06                                  | 4:05 AM and 6 seconds                                   |
| 20080215 04:05                                     | 4:05 AM exactly                                         |
| 20080215 040506                                    | 4:05 AM and 6 seconds                                   |
| 20080215 04:05 AM                                  | 4:05 AM exactly; AM is optional                         |
| 20080215 04:05 PM                                  | 4:05 PM exactly; the hour value must be less<br>than 12 |
| 20080215 16:05                                     | 4:05 PM exactly                                         |
| 20080215                                           | Midnight (by default)                                   |

## Special

datetime values

The following special values can be used as datetime literals and as
arguments to date functions. They require single quotation marks and are
converted to regular timestamp values during query processing.

| Special value | Description                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------- |
| `now`         | Evaluates to the start time of the current<br>transaction and returns a timestamp with microsecond precision. |
| `today`       | Evaluates to the appropriate date and returns<br>a timestamp with zeroes for the time parts.                  |
| `tomorrow`    | Evaluates to the appropriate date and<br>returns a timestamp with zeroes for the time<br>parts.               |
| `yesterday`   | Evaluates to the appropriate date and<br>returns a timestamp with zeroes for the time<br>parts.               |

The following examples show how `now` and `today`
work with the DATEADD function.

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
