# CURRENT_ROW_TIMESTAMP

CURRENT_ROW_TIMESTAMP is an Amazon Kinesis Data Analytics extension to the SQL:2008 specification. This function
returns the current timestamp as defined by the environment on which the Amazon Kinesis Data Analytics application
is running. CURRENT_ROW_TIMESTAMP is always returned as UTC, not the local timezone.

CURRENT_ROW_TIMESTAMP is similar to [LOCALTIMESTAMP](sql-reference-local-timestamp.md "sql-reference-local-timestamp.md"), but returns a new timestamp for each row in a
stream.

A query run with LOCALTIMESTAMP (or CURRENT_TIMESTAMP or CURRENT_TIME) as one of the columns
puts into all output rows the time the query is first run.

If that column instead contains CURRENT_ROW_TIMESTAMP, each output row gets a
newly-calculated value of TIME representing when that row was output.

###### Note

CURRENT_ROW_TIMESTAMP is not defined in the SQL:2008 specification; it is an Amazon Kinesis Data Analytics
extension.

For more information, see [CURRENT_TIME](sql-reference-current-time.md "sql-reference-current-time.md"), [CURRENT_DATE](sql-reference-current-date.md "sql-reference-current-date.md"), [CURRENT_TIMESTAMP](sql-reference-current-timestamp.md "sql-reference-current-timestamp.md"), [LOCALTIMESTAMP](sql-reference-local-timestamp.md "sql-reference-local-timestamp.md"), [LOCALTIME](sql-reference-localtime.md "sql-reference-localtime.md"), and CURRENT_ROW_TIMESTAMP.
