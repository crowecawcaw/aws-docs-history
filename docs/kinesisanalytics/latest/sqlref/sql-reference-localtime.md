

# LOCALTIME
<a name="sql-reference-localtime"></a>

Returns the current time when the query executes as defined by the environment on which Amazon Kinesis Data Analytics is running. LOCALTIME is always returned as UTC (GMT), not the local timezone.

For more information, see [CURRENT\_TIME](sql-reference-current-time.md), [CURRENT\_DATE](sql-reference-current-date.md), [CURRENT\_TIMESTAMP](sql-reference-current-timestamp.md), [LOCALTIMESTAMP](sql-reference-local-timestamp.md), and [CURRENT\_ROW\_TIMESTAMP](sql-reference-current-row-timestamp.md).

## Example
<a name="sql-reference-localtime-example"></a>

```
 VALUES localtime;
+------------+
| LOCALTIME  |
+------------+
| 01:11:15   |
+------------+
1 row selected (1.558 seconds)
```

## Limitations
<a name="sql-reference-localtime-limitations"></a>

Amazon Kinesis Data Analytics does not support the optional <time precision> parameter specified in SQL:2008. This is a departure from the SQL:2008 standard.