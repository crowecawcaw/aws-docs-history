Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Interleaved sort key

An interleaved sort gives equal weight to each column, or subset of columns, in
the sort key. If multiple queries use different columns for filters, then you can
often improve performance for those queries by using an interleaved sort style. When
a query uses restrictive predicates on secondary sort columns, interleaved sorting
significantly improves query performance as compared to compound sorting.

###### Important

Don't use an interleaved sort key on columns with monotonically increasing
attributes, such as identity columns, dates, or timestamps.

The performance improvements you gain by implementing an interleaved sort key
should be weighed against increased load and vacuum times.

Interleaved sorts are most effective with highly selective queries that filter on
one or more of the sort key columns in the WHERE clause, for example `select
 c_name from customer where c_region = 'ASIA'`. The benefits of interleaved
sorting increase with the number of sorted columns that are restricted.

An interleaved sort is more effective with large tables. Sorting is applied on
each slice. Thus, an interleaved sort is most effective when a table is large enough
to require multiple 1 MB blocks per slice. Here, the query processor can skip a
significant proportion of the blocks using restrictive predicates. To view the
number of blocks a table uses, query the [STV_BLOCKLIST](r_STV_BLOCKLIST.md "r_STV_BLOCKLIST.md") system view.

When sorting on a single column, an interleaved sort might give better
performance than a compound sort if the column values have a long common prefix. For
example, URLs commonly begin with "http://www". Compound sort keys use a limited
number of characters from the prefix, which results in a lot of duplication of keys.
Interleaved sorts use an internal compression scheme for zone map values that
enables them to better discriminate among column values that have a long common
prefix.

When migrating Amazon Redshift provisioned clusters to Amazon Redshift Serverless,
Redshift converts tables with both interleaved sort keys and DISTSTYLE
KEY to compound sort keys. However, tables with only interleaved sort keys remain unchanged.
For more information on distribution styles, see [Working with data distribution styles](t_Distributing_data.md "t_Distributing_data.md").

###### VACUUM REINDEX

As you add rows to a sorted table that already contains data, performance
might deteriorate over time. This deterioration occurs for both compound and
interleaved sorts, but it has a greater effect on interleaved tables. A VACUUM
restores the sort order, but the operation can take longer for interleaved
tables because merging new interleaved data might involve modifying every data
block.

When tables are initially loaded, Amazon Redshift analyzes the distribution of the values
in the sort key columns and uses that information for optimal interleaving of the
sort key columns. As a table grows, the distribution of the values in the sort key
columns can change, or skew, especially with date or timestamp columns. If the skew
becomes too large, performance might be affected. To re-analyze the sort keys and
restore performance, run the VACUUM command with the REINDEX key word. Because it
must take an extra analysis pass over the data, VACUUM REINDEX can take longer than
a standard VACUUM for interleaved tables. To view information about key distribution
skew and last reindex time, query the [SVV_INTERLEAVED_COLUMNS](r_SVV_INTERLEAVED_COLUMNS.md "r_SVV_INTERLEAVED_COLUMNS.md") system view.

For more information about how to determine how often to run VACUUM and when to
run a VACUUM REINDEX, see [Decide whether to reindex](vacuum-managing-vacuum-times.md#r_vacuum-decide-whether-to-reindex "vacuum-managing-vacuum-times.md#r_vacuum-decide-whether-to-reindex").
