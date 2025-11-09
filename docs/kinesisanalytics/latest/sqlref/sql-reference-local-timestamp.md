# LOCALTIMESTAMP

Returns the current timestamp as defined by the environment on Amazon Kinesis Data Analytics application is
running. Time is always returned as UTC (GMT), not the local timezone.

For more information, see [CURRENT_TIME](sql-reference-current-time.md "sql-reference-current-time.md"), [CURRENT_DATE](sql-reference-current-date.md "sql-reference-current-date.md"), [CURRENT_TIMESTAMP](sql-reference-current-timestamp.md "sql-reference-current-timestamp.md"), [LOCALTIME](sql-reference-localtime.md "sql-reference-localtime.md"), and [CURRENT_ROW_TIMESTAMP](sql-reference-current-row-timestamp.md "sql-reference-current-row-timestamp.md").

## Example

```
values localtimestamp;
+--------------------------+
|      LOCALTIMESTAMP      |
+--------------------------+
| 2008-08-27 01:13:42.206  |
+--------------------------+
1 row selected (1.133 seconds)
```

## Limitations

Amazon Kinesis Data Analytics does not support the optional <timestamp precision> parameter
specified in SQL:2008. This is a departure from the SQL:2008 standard.
