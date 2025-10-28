# LOCALTIME

Returns the current time when the query executes as defined by the environment on which
Amazon Kinesis Data Analytics is running. LOCALTIME is always returned as UTC (GMT), not the local
timezone.

For more information, see [CURRENT_TIME](sql-reference-current-time.md "sql-reference-current-time.md"), [CURRENT_DATE](sql-reference-current-date.md "sql-reference-current-date.md"), [CURRENT_TIMESTAMP](sql-reference-current-timestamp.md "sql-reference-current-timestamp.md"), [LOCALTIMESTAMP](sql-reference-local-timestamp.md "sql-reference-local-timestamp.md"), and
[CURRENT_ROW_TIMESTAMP](sql-reference-current-row-timestamp.md "sql-reference-current-row-timestamp.md").

## Example

````
 VALUES localtime;
+------------+
| LOCALTIME  | +------------+
| 01:11:15   | +------------+ 1 row selected (1.558 seconds) ``` ## Limitations Amazon Kinesis Data Analytics does not support the optional <time precision> parameter specified in SQL:2008. This is a departure from the SQL:2008 standard.
````
