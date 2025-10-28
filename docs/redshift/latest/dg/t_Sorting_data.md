Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Sort keys

###### Note

We recommend that you create your tables with `SORTKEY AUTO`. If you do so, then Amazon Redshift uses
automatic table optimization to choose the sort key.
For more information, see [Automatic table optimization](t_Creating_tables.md "t_Creating_tables.md").
The rest of this section provides details about the sort order.

When you create a table, you can alternatively define one or more of its columns as _sort
keys_. When data is initially loaded into the empty table, the rows are
stored on disk in sorted order. Information about sort key columns is passed to the
query planner, and the planner uses this information to construct plans that exploit the
way that the data is sorted.
For more information, see
[CREATE TABLE](r_CREATE_TABLE_NEW.md "r_CREATE_TABLE_NEW.md"). For information
on best practices when creating a sort key, see [Choose the best sort key](c_best-practices-sort-key.md "c_best-practices-sort-key.md").

Sorting enables efficient handling of range-restricted predicates. Amazon Redshift stores
columnar data in 1 MB disk blocks. The min and max values for each block are stored as
part of the metadata. If a query uses a range-restricted predicate, the query processor
can use the min and max values to rapidly skip over large numbers of blocks during table
scans. For example, suppose that a table stores five years of data sorted by date and a
query specifies a date range of one month. In this case, you can remove up to 98 percent
of the disk blocks from the scan. If the data is not sorted, more of the disk blocks
(possibly all of them) have to be scanned.

You can specify either a compound or interleaved sort key. A compound sort key is more
efficient when query predicates use a _prefix_, which
is a subset of the sort key columns in order. An interleaved sort key gives equal weight
to each column in the sort key, so query predicates can use any subset of the columns
that make up the sort key, in any order.

To understand the impact of the chosen sort key on query performance, use the [EXPLAIN](r_EXPLAIN.md "r_EXPLAIN.md") command. For more information, see
[Query planning and execution workflow](c-query-planning.md "c-query-planning.md").

To define a sort type, use either the INTERLEAVED or COMPOUND keyword with your CREATE
TABLE or CREATE TABLE AS statement. The default is COMPOUND. COMPOUND is
recommended when you update your tables regularly with INSERT, UPDATE, or
DELETE operations. An INTERLEAVED sort key can use a maximum of eight columns. Depending on your
data and cluster size, VACUUM REINDEX takes significantly longer than VACUUM FULL
because it makes an additional pass to analyze the interleaved sort keys. The sort and
merge operation can take longer for interleaved tables because the interleaved sort
might have to rearrange more rows than a compound sort.

To view the sort keys for a table, query the [SVV_TABLE_INFO](r_SVV_TABLE_INFO.md "r_SVV_TABLE_INFO.md") system view.

###### Topics

- [Multidimensional data layout sorting](t_Sorting_mutidimensional-sort-key.md "t_Sorting_mutidimensional-sort-key.md")
- [Compound sort key](t_Sorting_data-compound.md "t_Sorting_data-compound.md")
- [Interleaved sort key](t_Sorting_data-interleaved.md "t_Sorting_data-interleaved.md")
