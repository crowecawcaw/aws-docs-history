Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Date and time functions

In this section, you can find information about the date and time scalar functions that
Amazon Redshift supports.

###### Topics

- [Summary of date and time functions](#date-functions-summary "#date-functions-summary")
- [Date and time functions in transactions](#date-functions-transactions "#date-functions-transactions")
- [Deprecated leader node-only functions](#date-functions-deprecated "#date-functions-deprecated")
- [+ (Concatenation) operator](r_DATE-CONCATENATE_function.md "r_DATE-CONCATENATE_function.md")
- [ADD\_MONTHS function](r_ADD_MONTHS.md "r_ADD_MONTHS.md")
- [AT TIME ZONE function](r_AT_TIME_ZONE.md "r_AT_TIME_ZONE.md")
- [CONVERT\_TIMEZONE function](CONVERT_TIMEZONE.md "CONVERT_TIMEZONE.md")
- [CURRENT\_DATE function](r_CURRENT_DATE_function.md "r_CURRENT_DATE_function.md")
- [DATE\_CMP function](r_DATE_CMP.md "r_DATE_CMP.md")
- [DATE\_CMP\_TIMESTAMP function](r_DATE_CMP_TIMESTAMP.md "r_DATE_CMP_TIMESTAMP.md")
- [DATE\_CMP\_TIMESTAMPTZ function](r_DATE_CMP_TIMESTAMPTZ.md "r_DATE_CMP_TIMESTAMPTZ.md")
- [DATEADD function](r_DATEADD_function.md "r_DATEADD_function.md")
- [DATEDIFF function](r_DATEDIFF_function.md "r_DATEDIFF_function.md")
- [DATE\_PART function](r_DATE_PART_function.md "r_DATE_PART_function.md")
- [DATE\_PART\_YEAR function](r_DATE_PART_YEAR.md "r_DATE_PART_YEAR.md")
- [DATE\_TRUNC function](r_DATE_TRUNC.md "r_DATE_TRUNC.md")
- [EXTRACT function](r_EXTRACT_function.md "r_EXTRACT_function.md")
- [GETDATE function](r_GETDATE.md "r_GETDATE.md")
- [INTERVAL\_CMP function](r_INTERVAL_CMP.md "r_INTERVAL_CMP.md")
- [LAST\_DAY function](r_LAST_DAY.md "r_LAST_DAY.md")
- [MONTHS\_BETWEEN function](r_MONTHS_BETWEEN_function.md "r_MONTHS_BETWEEN_function.md")
- [NEXT\_DAY function](r_NEXT_DAY.md "r_NEXT_DAY.md")
- [SYSDATE function](r_SYSDATE.md "r_SYSDATE.md")
- [TIMEOFDAY function](r_TIMEOFDAY_function.md "r_TIMEOFDAY_function.md")
- [TIMESTAMP\_CMP function](r_TIMESTAMP_CMP.md "r_TIMESTAMP_CMP.md")
- [TIMESTAMP\_CMP\_DATE function](r_TIMESTAMP_CMP_DATE.md "r_TIMESTAMP_CMP_DATE.md")
- [TIMESTAMP\_CMP\_TIMESTAMPTZ function](r_TIMESTAMP_CMP_TIMESTAMPTZ.md "r_TIMESTAMP_CMP_TIMESTAMPTZ.md")
- [TIMESTAMPTZ\_CMP function](r_TIMESTAMPTZ_CMP.md "r_TIMESTAMPTZ_CMP.md")
- [TIMESTAMPTZ\_CMP\_DATE function](r_TIMESTAMPTZ_CMP_DATE.md "r_TIMESTAMPTZ_CMP_DATE.md")
- [TIMESTAMPTZ\_CMP\_TIMESTAMP function](r_TIMESTAMPTZ_CMP_TIMESTAMP.md "r_TIMESTAMPTZ_CMP_TIMESTAMP.md")
- [TIMEZONE function](r_TIMEZONE.md "r_TIMEZONE.md")
- [TO\_TIMESTAMP function](r_TO_TIMESTAMP.md "r_TO_TIMESTAMP.md")
- [TRUNC function](r_TRUNC_date.md "r_TRUNC_date.md")
- [Date parts for date or timestamp functions](r_Dateparts_for_datetime_functions.md "r_Dateparts_for_datetime_functions.md")

## Summary of date and time functions

| Function                                                                                                                                                                                                                                                                             | Syntax                                                           | Returns                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- | --------------------------- |
| [+ (Concatenation) operator](r_DATE-CONCATENATE_function.md "r_DATE-CONCATENATE_function.md")<br>Concatenates a date to a time on either side of the + symbol and returns a TIMESTAMP or TIMESTAMPTZ.                                                                                | *date<br>• + _time_                                              | `TIMESTAMP` or `TIMESTAMPZ` |
| [ADD\_MONTHS](r_ADD_MONTHS.md "r_ADD_MONTHS.md")Adds the specified number of<br>months to a date or timestamp.                                                                                                                                                                       | ADD\_MONTHS<br>({_date_                                          | _timestamp_},<br>_integer_) | `TIMESTAMP`                  |
| [AT TIME ZONE](r_AT_TIME_ZONE.md "r_AT_TIME_ZONE.md")Specifies which time zone to use<br>with a TIMESTAMP or TIMESTAMPTZ expression.                                                                                                                                                 | AT TIME ZONE '_timezone_'                                        | `TIMESTAMP` or `TIMESTAMPZ` |
| [CONVERT\_TIMEZONE](CONVERT_TIMEZONE.md "CONVERT_TIMEZONE.md")Converts a timestamp from one<br>time zone to another.                                                                                                                                                                 | CONVERT\_TIMEZONE (['_timezone_',]<br>'_timezone_', _timestamp_) | `TIMESTAMP`                 |
| [CURRENT\_DATE](r_CURRENT_DATE_function.md "r_CURRENT_DATE_function.md")Returns a date in the<br>current session time zone (UTC by default) for the start of the current<br>transaction.                                                                                             | CURRENT\_DATE                                                    | `DATE`                      |
| [DATE\_CMP](r_DATE_CMP.md "r_DATE_CMP.md")Compares two dates and returns `0` if the dates are<br>identical, `1` if *date1<br>• is greater, and<br>`-1` if *date2<br>• is greater.                                                                                                    | DATE\_CMP (_date1_,<br>_date2_)                                  | `INTEGER`                   |
| [DATE\_CMP\_TIMESTAMP](r_DATE_CMP_TIMESTAMP.md "r_DATE_CMP_TIMESTAMP.md")Compares a date to a time<br>and returns `0` if the values are identical, `1` if<br>*date<br>• is greater and `-1` if<br>*timestamp<br>• is greater.                                                        | DATE\_CMP\_TIMESTAMP (_date_,<br>_timestamp_)                    | `INTEGER`                   |
| [DATE\_CMP\_TIMESTAMPTZ](r_DATE_CMP_TIMESTAMPTZ.md "r_DATE_CMP_TIMESTAMPTZ.md")Compares a date and a<br>timestamp with time zone and returns `0` if the values are<br>identical, `1` if *date<br>• is greater and<br>`-1` if *timestamptz<br>• is<br>greater.                        | DATE\_CMP\_TIMESTAMPTZ (_date_,<br>_timestamptz_)                | `INTEGER`                   |
| [DATE\_PART\_YEAR](r_DATE_PART_YEAR.md "r_DATE_PART_YEAR.md")Extracts the year from a<br>date.                                                                                                                                                                                       | DATE\_PART\_YEAR (_date_)                                        | `INTEGER`                   |
| [DATEADD](r_DATEADD_function.md "r_DATEADD_function.md")Increments a date or time by<br>a specified interval.                                                                                                                                                                        | DATEADD (_datepart_,<br>_interval_,<br>{_date_                   | _time_                      | _timetz_                     | _timestamp_})           | `TIMESTAMP` or `TIME` or `TIMETZ` |
| [DATEDIFF](r_DATEDIFF_function.md "r_DATEDIFF_function.md")Returns the difference<br>between two dates or times for a given date part, such as a day or<br>month.                                                                                                                    | DATEDIFF (_datepart_,<br>{_date_                                 | _time_                      | _timetz_                     | _timestamp_}`,` {_date_ | _time_                            | _timetz_ | _timestamp_}) | `BIGINT` |
| [DATE\_PART](r_DATE_PART_function.md "r_DATE_PART_function.md")Extracts a date part value<br>from a date or time.                                                                                                                                                                    | DATE\_PART (_datepart_,<br>{_date_                               | _timestamp_})               | `DOUBLE`                     |
| [DATE\_TRUNC](r_DATE_TRUNC.md "r_DATE_TRUNC.md")Truncates a timestamp based on a<br>date part.                                                                                                                                                                                       | DATE\_TRUNC (_'datepart'_,<br>_timestamp_)                       | `TIMESTAMP`                 |
| [EXTRACT](r_EXTRACT_function.md "r_EXTRACT_function.md")Extracts a date or time part from a<br>timestamp, timestamptz, time, or timetz.                                                                                                                                              | EXTRACT (*datepart<br>• FROM _source_)                           | `INTEGER or DOUBLE`         |
| [GETDATE](r_GETDATE.md "r_GETDATE.md")Returns the current date and time in the current session time zone<br>(UTC by default). The parentheses are required.                                                                                                                          | GETDATE()                                                        | `TIMESTAMP`                 |
| [INTERVAL\_CMP](r_INTERVAL_CMP.md "r_INTERVAL_CMP.md")Compares two intervals and<br>returns `0` if the intervals are equal, `1` if<br>*interval1<br>• is greater, and `-1` if<br>*interval2<br>• is greater.                                                                         | INTERVAL\_CMP (_interval1_,<br>_interval2_)                      | `INTEGER`                   |
| [LAST\_DAY](r_LAST_DAY.md "r_LAST_DAY.md")Returns the date of the last day of the month that contains<br>_date_.                                                                                                                                                                     | LAST\_DAY(_date_)                                                | `DATE`                      |
| [MONTHS\_BETWEEN](r_MONTHS_BETWEEN_function.md "r_MONTHS_BETWEEN_function.md")Returns the number of<br>months between two dates.                                                                                                                                                     | MONTHS\_BETWEEN (_date_,<br>_date_)                              | `FLOAT8`                    |
| [NEXT\_DAY](r_NEXT_DAY.md "r_NEXT_DAY.md")Returns the date of the first instance of _day_<br>that is later than _date_.                                                                                                                                                              | NEXT\_DAY (_date_,<br>_day_)                                     | `DATE`                      |
| [SYSDATE](r_SYSDATE.md "r_SYSDATE.md")Returns the date and time in UTC for the start of the current<br>transaction.                                                                                                                                                                  | SYSDATE                                                          | `TIMESTAMP`                 |
| [TIMEOFDAY](r_TIMEOFDAY_function.md "r_TIMEOFDAY_function.md")Returns the current<br>weekday, date, and time in the current session time zone (UTC by default) as<br>a string value.                                                                                                 | TIMEOFDAY()                                                      | `VARCHAR`                   |
| [TIMESTAMP\_CMP](r_TIMESTAMP_CMP.md "r_TIMESTAMP_CMP.md")Compares two timestamps and<br>returns `0` if the timestamps are equal, `1` if<br>*timestamp1<br>• is greater, and `-1` if<br>*timestamp2<br>• is greater.                                                                  | TIMESTAMP\_CMP (_timestamp1_,<br>_timestamp2_)                   | `INTEGER`                   |
| [TIMESTAMP\_CMP\_DATE](r_TIMESTAMP_CMP_DATE.md "r_TIMESTAMP_CMP_DATE.md")Compares a timestamp to a<br>date and returns `0` if the values are identical, `1`<br>if *timestamp<br>• is greater, and `-1` if<br>*date<br>• is greater.                                                  | TIMESTAMP\_CMP\_DATE (_timestamp_,<br>_date_)                    | `INTEGER`                   |
| [TIMESTAMP\_CMP\_TIMESTAMPTZ](r_TIMESTAMP_CMP_TIMESTAMPTZ.md "r_TIMESTAMP_CMP_TIMESTAMPTZ.md")Compares a<br>timestamp with a timestamp with time zone and returns `0` if the<br>values are equal, `1` if *timestamp<br>• is<br>greater, and `-1` if *timestamptz<br>• is<br>greater. | TIMESTAMP\_CMP\_TIMESTAMPTZ (_timestamp_,<br>_timestamptz_)      | `INTEGER`                   |
| [TIMESTAMPTZ\_CMP](r_TIMESTAMPTZ_CMP.md "r_TIMESTAMPTZ_CMP.md")Compares two timestamp with<br>time zone values and returns `0` if the values are equal,<br>`1` if *timestamptz1<br>• is greater, and<br>`-1` if *timestamptz2<br>• is<br>greater.                                    | TIMESTAMPTZ\_CMP (_timestamptz1_,<br>_timestamptz2_)             | `INTEGER`                   |
| [TIMESTAMPTZ\_CMP\_DATE](r_TIMESTAMPTZ_CMP_DATE.md "r_TIMESTAMPTZ_CMP_DATE.md")Compares the value of a<br>timestamp with time zone and a date and returns `0` if the<br>values are equal, `1` if *timestamptz<br>• is<br>greater, and `-1` if *date<br>• is<br>greater.              | TIMESTAMPTZ\_CMP\_DATE (_timestamptz_,<br>_date_)                | `INTEGER`                   |
| [TIMESTAMPTZ\_CMP\_TIMESTAMP](r_TIMESTAMPTZ_CMP_TIMESTAMP.md "r_TIMESTAMPTZ_CMP_TIMESTAMP.md")Compares a<br>timestamp with time zone with a timestamp and returns `0` if the<br>values are equal, `1` if *timestamptz<br>• is<br>greater, and `-1` if *timestamp<br>• is<br>greater. | TIMESTAMPTZ\_CMP\_TIMESTAMP (_timestamptz_,<br>_timestamp_)      | `INTEGER`                   |
| [TIMEZONE](r_TIMEZONE.md "r_TIMEZONE.md")Returns a timestamp for the specified time zone and timestamp<br>value.                                                                                                                                                                     | TIMEZONE ('_timezone_' {<br>*timestamp<br>•                      | *timestamptz<br>• )         | `TIMESTAMP` or `TIMESTAMPTZ` |
| [TO\_TIMESTAMP](r_TO_TIMESTAMP.md "r_TO_TIMESTAMP.md")Returns a timestamp with time<br>zone for the specified timestamp and time zone format.                                                                                                                                        | TO\_TIMESTAMP ('_timestamp_',<br>'_format_')                     | `TIMESTAMPTZ`               |
| [TRUNC](r_TRUNC_date.md "r_TRUNC_date.md")Truncates a timestamp and returns<br>a date.                                                                                                                                                                                               | TRUNC(_timestamp_)                                               | `DATE`                      |

###### Note

Leap seconds are not considered in elapsed-time calculations.

## Date and time functions in transactions

When you run the following functions within a transaction block (BEGIN … END), the
function returns the start date or time of the current transaction, not the start of the
current statement.

- SYSDATE
- TIMESTAMP
- CURRENT\_DATE

The following functions always return the start date or time of the current statement,
even when they are within a transaction block.

- GETDATE
- TIMEOFDAY

## Deprecated leader node-only functions

The following date functions are deprecated because they run only on the leader
node. For more information, see [Leader node–only functions](c_SQL_functions_leader_node_only.md "c_SQL_functions_leader_node_only.md").

- AGE. Use [DATEDIFF function](r_DATEDIFF_function.md "r_DATEDIFF_function.md") instead.
- CURRENT\_TIME. Use [GETDATE function](r_GETDATE.md "r_GETDATE.md") or
  [SYSDATE](r_SYSDATE.md "r_SYSDATE.md") instead.
- CURRENT\_TIMESTAMP. Use [GETDATE function](r_GETDATE.md "r_GETDATE.md") or
  [SYSDATE](r_SYSDATE.md "r_SYSDATE.md") instead.
- LOCALTIME. Use [GETDATE function](r_GETDATE.md "r_GETDATE.md") or [SYSDATE](r_SYSDATE.md "r_SYSDATE.md") instead.
- LOCALTIMESTAMP. Use [GETDATE function](r_GETDATE.md "r_GETDATE.md") or
  [SYSDATE](r_SYSDATE.md "r_SYSDATE.md") instead.
- ISFINITE
- NOW. Use [GETDATE function](r_GETDATE.md "r_GETDATE.md") or [SYSDATE](r_SYSDATE.md "r_SYSDATE.md") instead. If you use the NOW
  function within a materialized view, it sets to the timestamp of the creation of the
  materialized view, instead of the current timestamp.
