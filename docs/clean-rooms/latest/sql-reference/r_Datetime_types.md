# Datetime types

Datetime data types include DATE, TIME, TIMETZ, TIMESTAMP, and TIMESTAMPTZ.

###### Topics

- [Storage and ranges](#r_Datetime_types-storage-and-ranges "#r_Datetime_types-storage-and-ranges")
- [DATE](r_Datetime_types-date.md "r_Datetime_types-date.md")
- [TIME](r_Datetime_types-time.md "r_Datetime_types-time.md")
- [TIMETZ](r_Datetime_types-timetz.md "r_Datetime_types-timetz.md")
- [TIMESTAMP](r_Datetime_types-timestamp.md "r_Datetime_types-timestamp.md")
- [TIMESTAMPTZ](r_Datetime_types-timestamptz.md "r_Datetime_types-timestamptz.md")
- [Examples with datetime types](r_Examples_with_datetime_types.md "r_Examples_with_datetime_types.md")
- [Date, time, and timestamp literals](r_Date_and_time_literals.md "r_Date_and_time_literals.md")
- [Interval literals](r_interval_literals.md "r_interval_literals.md")
- [Interval data types and literals](interval_data_types.md "interval_data_types.md")

## Storage and ranges

| Name        | Storage | Range                          | Resolution    |
| ----------- | ------- | ------------------------------ | ------------- |
| DATE        | 4 bytes | 4713 BC to 294276 AD           | 1 day         |
| TIME        | 8 bytes | 00:00:00 to 24:00:00           | 1 microsecond |
| TIMETZ      | 8 bytes | 00:00:00+1459 to 00:00:00+1459 | 1 microsecond |
| TIMESTAMP   | 8 bytes | 4713 BC to 294276 AD           | 1 microsecond |
| TIMESTAMPTZ | 8 bytes | 4713 BC to 294276 AD           | 1 microsecond |
