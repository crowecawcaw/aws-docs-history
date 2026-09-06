

# CURRENT\_ROW\_TIMESTAMP
<a name="sql-reference-current-row-timestamp"></a>

CURRENT\_ROW\_TIMESTAMP is an Amazon Kinesis Data Analytics extension to the SQL:2008 specification. This function returns the current timestamp as defined by the environment on which the Amazon Kinesis Data Analytics application is running. CURRENT\_ROW\_TIMESTAMP is always returned as UTC, not the local timezone.

CURRENT\_ROW\_TIMESTAMP is similar to [LOCALTIMESTAMP](sql-reference-local-timestamp.md), but returns a new timestamp for each row in a stream.

A query run with LOCALTIMESTAMP (or CURRENT\_TIMESTAMP or CURRENT\_TIME) as one of the columns puts into all output rows the time the query is first run.

If that column instead contains CURRENT\_ROW\_TIMESTAMP, each output row gets a newly-calculated value of TIME representing when that row was output.

**Note**  
CURRENT\_ROW\_TIMESTAMP is not defined in the SQL:2008 specification; it is an Amazon Kinesis Data Analytics extension.

For more information, see [CURRENT\_TIME](sql-reference-current-time.md), [CURRENT\_DATE](sql-reference-current-date.md), [CURRENT\_TIMESTAMP](sql-reference-current-timestamp.md), [LOCALTIMESTAMP](sql-reference-local-timestamp.md), [LOCALTIME](sql-reference-localtime.md), and [CURRENT\_ROW\_TIMESTAMP](#sql-reference-current-row-timestamp).