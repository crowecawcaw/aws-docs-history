# T-sorting Stream Input

Amazon Kinesis Data Analytics real-time analytics use the fact that arriving data is ordered by ROWTIME.
However, sometimes data arriving from multiple sources may not be time-synchronized.

While Amazon Kinesis Data Analytics can sort data from individual data sources that have been independently
inserted into Amazon Kinesis Data Analytics application's native stream, in some cases such data may have already
combined from multiple sources (such as for efficient consumption at an earlier stage
in processing). At other times, high volume data sources could make direct insertion
impossible.

In addition, an unreliable data source could block progress
by forcing Amazon Kinesis Data Analytics application to wait indefinitely, unable to proceed until all
connected data sources deliver. In this case, data from this source could be
unsynchronized.

You can use the ORDER BY clause to resolve these issues. Amazon Kinesis Data Analytics uses a sliding
time-based window of incoming rows to reorder those rows by ROWTIME.

###### Syntax

You specify the time-based parameter for sorting and
the time-based window in which the streaming rows are to be time-sorted, using the
following syntax:

```
  ORDER BY <timestamp_expr> WITHIN
      <interval_literal>
```

###### Restrictions

The T-sort has the following restrictions:

- The datatype of the ORDER BY expression must be timestamp.
- The partially-ordered expression <timestamp_expr> must be present in the select list of the query with the alias ROWTIME.
- The leading expression of the ORDER BY clause must not contain the ROWTIME function and must not use the DESC keyword.
- The ROWTIME column needs to be fully qualified. For example:

- `ORDER BY FLOOR(ROWTIME TO MINUTE), ...` fails.
- `ORDER BY FLOOR(s.ROWTIME TO MINUTE), ...` works.
  If any of these requirements are not met, the statement will fail with errors.

Additional notes:

- You cannot use incoming rowtimebounds. These are ignored by the system.
- If <timestamp_expr> evaluates to NULL, the corresponding row is discarded.
