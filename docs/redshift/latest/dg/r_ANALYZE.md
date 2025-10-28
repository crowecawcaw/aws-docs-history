Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ANALYZE

Updates table statistics for use by the query planner.

## Required privileges

Following are required privileges for ANALYZE:

- Superuser
- Users with the ANALYZE privilege
- Owner of the relation
- Database owner whom the table is shared to

## Syntax

```
ANALYZE [ VERBOSE ]
[ [ *table\_name* [ ( *column\_name* [, ...] ) ] ]
[ PREDICATE COLUMNS | ALL  COLUMNS ]
```

## Parameters

VERBOSE

A clause that returns progress information messages about the ANALYZE
operation. This option is useful when you don't specify a table.

_table_name_

You can analyze specific tables, including temporary tables. You can qualify
the table with its schema name. You can optionally specify a table_name to
analyze a single table. You can't specify more than one
_table_name_ with a single ANALYZE
_table_name_ statement. If you don't specify a
_table_name_ value, all of the tables in the currently
connected database are analyzed, including the persistent tables in the system
catalog. Amazon Redshift skips analyzing a table if the percentage of rows that have
changed since the last ANALYZE is lower than the analyze threshold. For more
information, see [Analyze threshold](#r_ANALYZE-threshold "#r_ANALYZE-threshold").

You don't need to analyze Amazon Redshift system tables (STL and STV
tables).

_column_name_

If you specify a _table_name_, you can also specify one
or more columns in the table (as a column-separated list within parentheses).
If a column list is specified, only the listed columns are analyzed.

PREDICATE COLUMNS | ALL COLUMNS

Clauses that indicate whether ANALYZE should include only predicate columns.
Specify PREDICATE COLUMNS to analyze only columns that have been used as
predicates in previous queries or are likely candidates to be used as
predicates. Specify ALL COLUMNS to analyze all columns. The default is ALL
COLUMNS.

A column is included in the set of predicate columns if any of the following
is true:

- The column has been used in a query as a part of a filter, join
  condition, or group by clause.
- The column is a distribution key.
- The column is part of a sort key.

If no columns are marked as predicate columns, for example because the table
has not yet been queried, all of the columns are analyzed even when PREDICATE
COLUMNS is specified.
When this happens, Amazon Redshift might respond with a message like **`No
 predicate columns found for "`table-name`".
 Analyzing all columns`**. For more information about predicate
columns, see [Analyzing tables](t_Analyzing_tables.md "t_Analyzing_tables.md").

## Usage notes

Amazon Redshift automatically runs ANALYZE on tables that you create with the following
commands:

- CREATE TABLE AS
- CREATE TEMP TABLE AS
- SELECT INTO

You can't analyze an external table.

You don't need to run the ANALYZE command on these tables when they are first
created. If you modify them, you should analyze them in the same way as other
tables.

### Analyze threshold

To reduce processing time and improve overall system performance, Amazon Redshift skips
ANALYZE for a table if the percentage of rows that have changed since the last
ANALYZE command run is lower than the analyze threshold specified by the [analyze_threshold_percent](r_analyze_threshold_percent.md "r_analyze_threshold_percent.md") parameter. By default, `analyze_threshold_percent` is 10. To change
`analyze_threshold_percent` for the current session, run the [SET](r_SET.md "r_SET.md") command. The following example changes
`analyze_threshold_percent` to 20 percent.

```
set analyze_threshold_percent to 20;
```

To analyze tables when only a small number of rows have changed, set
`analyze_threshold_percent` to an arbitrarily small number. For
example, if you set `analyze_threshold_percent` to 0.01, then a table with
100,000,000 rows aren't skipped if at least 10,000 rows have changed.

```
set analyze_threshold_percent to 0.01;
```

If ANALYZE skips a table because it doesn't meet the analyze threshold,
Amazon Redshift returns the following message.

```
ANALYZE SKIP
```

To analyze all tables even if no rows have changed, set
`analyze_threshold_percent` to 0.

To view the results of ANALYZE operations, query the [STL_ANALYZE](r_STL_ANALYZE.md "r_STL_ANALYZE.md") system table.

For more information about analyzing tables, see [Analyzing tables](t_Analyzing_tables.md "t_Analyzing_tables.md").

## Examples

Analyze all of the tables in the TICKIT database and return progress
information.

```
analyze verbose;
```

Analyze the LISTING table only.

```
analyze listing;
```

Analyze the VENUEID and VENUENAME columns in the VENUE table.

```
analyze venue(venueid, venuename);
```

Analyze only predicate columns in the VENUE table.

```
analyze venue predicate columns;
```
