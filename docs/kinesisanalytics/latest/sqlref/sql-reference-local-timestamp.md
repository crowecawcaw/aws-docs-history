

# LOCALTIMESTAMP
<a name="sql-reference-local-timestamp"></a>

Returns the current timestamp as defined by the environment on Amazon Kinesis Data Analytics application is running. Time is always returned as UTC (GMT), not the local timezone.

For more information, see [CURRENT\_TIME](sql-reference-current-time.md), [CURRENT\_DATE](sql-reference-current-date.md), [CURRENT\_TIMESTAMP](sql-reference-current-timestamp.md), [LOCALTIME](sql-reference-localtime.md), and [CURRENT\_ROW\_TIMESTAMP](sql-reference-current-row-timestamp.md).

## Example
<a name="sql-reference-local-timestamp-example"></a>

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
<a name="sql-reference-local-timestamp-limitations"></a>

Amazon Kinesis Data Analytics does not support the optional <timestamp precision> parameter specified in SQL:2008. This is a departure from the SQL:2008 standard.