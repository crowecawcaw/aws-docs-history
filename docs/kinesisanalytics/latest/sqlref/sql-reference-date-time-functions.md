# Date and Time Functions

The following built-in functions relate to dates and time.

###### Topics

- [Time Zones](#sql-reference-date-time-functions-time-zones "#sql-reference-date-time-functions-time-zones")
- [Datetime Conversion
  Functions](sql-reference-datetime-conversion-functions.md "sql-reference-datetime-conversion-functions.md")
- [Date, Timestamp, and Interval
  Operators](sql-reference-date-timestamp-interval.md "sql-reference-date-timestamp-interval.md")
- [Date and Time Patterns](sql-reference-parse-timestamp-format.md "sql-reference-parse-timestamp-format.md")
- [CURRENT_DATE](sql-reference-current-date.md "sql-reference-current-date.md")
- [CURRENT_ROW_TIMESTAMP](sql-reference-current-row-timestamp.md "sql-reference-current-row-timestamp.md")
- [CURRENT_TIME](sql-reference-current-time.md "sql-reference-current-time.md")
- [CURRENT_TIMESTAMP](sql-reference-current-timestamp.md "sql-reference-current-timestamp.md")
- [EXTRACT](sql-reference-extract.md "sql-reference-extract.md")
- [LOCALTIME](sql-reference-localtime.md "sql-reference-localtime.md")
- [LOCALTIMESTAMP](sql-reference-local-timestamp.md "sql-reference-local-timestamp.md")
- [TSDIFF](sql-reference-tsdiff.md "sql-reference-tsdiff.md")
  Of these, the SQL extension CURRENT_ROW_TIMESTAMP is the most useful for a streaming
  context, because it gives you information about the times of streaming data as it emerges, not
  just when the query is run. This is a key difference between a streaming query and a traditional
  RDMS query: streaming queries remain "open," producing more data, so the timestamp for when the
  query was run does not offer good information.

LOCALTIMESTAMP, LOCALTIME, CURRENT_DATE, and CURRENT_TIMESTAMP all produce results which are
set to values at the time the query first executes. Only CURRENT_ROW_TIMESTAMP generates a row
with a unique timestamp (date and time) for each row.

A query run with LOCALTIMESTAMP (or CURRENT_TIMESTAMP or CURRENT_TIME) as one of the columns
puts into all output rows the time the query is first run. If that column instead contains
CURRENT_ROW_TIMESTAMP, each output row gets a newly-calculated value of TIME representing when
that row was output.

To return a part (such as the day of the month) from a Datetime value, use [EXTRACT](sql-reference-extract.md "sql-reference-extract.md")

## Time Zones

Amazon Kinesis Data Analytics runs in UTC. As a result, all time functions return time in UTC.
