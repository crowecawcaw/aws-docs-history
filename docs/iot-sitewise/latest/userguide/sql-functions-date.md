# Date time functions

Date time functions work with dates and times. These functions allow extraction of
specific components of a date, perform calculations, and manipulate date values.

The allowed identifiers in these functions are:

- YEAR
- MONTH
- DAY
- HOUR
- MINUTE
- SECOND

| **Function**    | **Signature**                                         | **Description**                                                                                                                                                                                                                                     |
| --------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `NOW`           | NOW ( )                                               | Returns the current timestamp with millisecond precision. It provides the exact time at the moment it's executed within a query.                                                                                                                    |
| `DATE_ADD`      | DATE_ADD (identifier, interval_duration, column)      | Returns the sum of a date/time and a number of days/hours, or of a date/time and date/time interval.                                                                                                                                                |
| `DATE_SUB`      | DATE_SUB (identifier, interval_duration, column)      | Returns the difference between a date/time and a number of days/hours, or between a date/time and date/time interval.                                                                                                                               |
| `TIMESTAMP_ADD` | TIMESTAMP_ADD (identifier, interval_duration, column) | Adds an interval of time, in the given time units, to a datetime expression.                                                                                                                                                                        |
| `TIMESTAMP_SUB` | TIMESTAMP_SUB (identifier, interval_duration, column) | Subtracts an interval of time, in the given time units, from a datetime expression.                                                                                                                                                                 |
| `CAST`          | CAST (expression AS TIMESTAMP FORMAT pattern)         | Converts a string expression to a timestamp using the specified format pattern. Common patterns include `'yyyy-MM-dd HH:mm:ss'` for standard datetime format. For example, `SELECT CAST('2023-12-25 14:30:00' AS TIMESTAMP) AS converted_timestamp` | ###### Example of a SQL query using the listed functions: `SELECT r.asset_id, r.int_value, date_add(DAY, 7, r.event_timestamp) AS date_in_future, date_sub(YEAR, 2, r.event_timestamp) AS date_in_past, timestamp_add(DAY, 2, r.event_timestamp) AS timestamp_in_future, timestamp_sub(DAY, 2, r.event_timestamp) AS timestamp_in_past, now() AS time_now FROM raw_time_series AS r` |
