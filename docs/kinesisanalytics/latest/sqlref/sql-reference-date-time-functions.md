

# Date and Time Functions
<a name="sql-reference-date-time-functions"></a>

The following built-in functions relate to dates and time. 

**Topics**
+ [Time Zones](#sql-reference-date-time-functions-time-zones)
+ [Datetime Conversion Functions](sql-reference-datetime-conversion-functions.md)
+ [Date, Timestamp, and Interval Operators](sql-reference-date-timestamp-interval.md)
+ [Date and Time Patterns](sql-reference-parse-timestamp-format.md)
+ [CURRENT\_DATE](sql-reference-current-date.md)
+ [CURRENT\_ROW\_TIMESTAMP](sql-reference-current-row-timestamp.md)
+ [CURRENT\_TIME](sql-reference-current-time.md)
+ [CURRENT\_TIMESTAMP](sql-reference-current-timestamp.md)
+ [EXTRACT](sql-reference-extract.md)
+ [LOCALTIME](sql-reference-localtime.md)
+ [LOCALTIMESTAMP](sql-reference-local-timestamp.md)
+ [TSDIFF](sql-reference-tsdiff.md)

 Of these, the SQL extension CURRENT\_ROW\_TIMESTAMP is the most useful for a streaming context, because it gives you information about the times of streaming data as it emerges, not just when the query is run. This is a key difference between a streaming query and a traditional RDMS query: streaming queries remain "open," producing more data, so the timestamp for when the query was run does not offer good information. 

LOCALTIMESTAMP, LOCALTIME, CURRENT\_DATE, and CURRENT\_TIMESTAMP all produce results which are set to values at the time the query first executes. Only CURRENT\_ROW\_TIMESTAMP generates a row with a unique timestamp (date and time) for each row. 

A query run with LOCALTIMESTAMP (or CURRENT\_TIMESTAMP or CURRENT\_TIME) as one of the columns puts into all output rows the time the query is first run. If that column instead contains CURRENT\_ROW\_TIMESTAMP, each output row gets a newly-calculated value of TIME representing when that row was output.

To return a part (such as the day of the month) from a Datetime value, use [EXTRACT](sql-reference-extract.md)

## Time Zones
<a name="sql-reference-date-time-functions-time-zones"></a>

Amazon Kinesis Data Analytics runs in UTC. As a result, all time functions return time in UTC.