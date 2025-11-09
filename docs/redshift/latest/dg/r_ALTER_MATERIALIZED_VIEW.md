Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ALTER MATERIALIZED VIEW

Changes the attributes of a materialized view.

## Syntax

```
ALTER MATERIALIZED VIEW *mv\_name*
{
AUTO REFRESH { YES | NO }
| ALTER DISTKEY column_name
| ALTER DISTSTYLE ALL
| ALTER DISTSTYLE EVEN
| ALTER DISTSTYLE KEY DISTKEY column_name
| ALTER DISTSTYLE AUTO
| ALTER [COMPOUND] SORTKEY ( column_name [,...] )
| ALTER SORTKEY AUTO
| ALTER SORTKEY NONE
| ROW LEVEL SECURITY { ON | OFF } [ CONJUNCTION TYPE { AND | OR } ] [FOR DATASHARES]
};
```

## Parameters

_mv_name_

The name of the materialized view to alter.

AUTO REFRESH { YES | NO }

A clause that turns on or off automatic refreshing of a materialized view.
For more information about automatic refresh of materialized views, see [Refreshing a materialized view](materialized-view-refresh.md "materialized-view-refresh.md").

ALTER DISTSTYLE ALL

A clause that changes the existing distribution style of a relation to
`ALL`. Consider the following:

- An ALTER DISTSTYLE, ALTER SORTKEY, and VACUUM can't run
  concurrently on the same relation.
  - If VACUUM is currently running, then running ALTER DISTSTYLE ALL
    returns an error.
  - If ALTER DISTSTYLE ALL is running, then a background vacuum
    doesn't start on a relation.

- The ALTER DISTSTYLE ALL command is not supported for relations with
  interleaved sort keys and temporary tables.
- If the distribution style was previously defined as AUTO, then the
  relation is no longer a candidate for automatic table optimization.

For more information about DISTSTYLE ALL, go to [CREATE MATERIALIZED VIEW](materialized-view-create-sql-command.md "materialized-view-create-sql-command.md").

ALTER DISTSTYLE EVEN

A clause that changes the existing distribution style of a relation to
`EVEN`. Consider the following:

- An ALTER DISTSYTLE, ALTER SORTKEY, and VACUUM can't run
  concurrently on the same relation.
  - If VACUUM is currently running, then running ALTER DISTSTYLE
    EVEN returns an error.
  - If ALTER DISTSTYLE EVEN is running, then a background vacuum
    doesn't start on a relation.

- The ALTER DISTSTYLE EVEN command is not supported for relations with
  interleaved sort keys and temporary tables.
- If the distribution style was previously defined as AUTO, then the
  relation is no longer a candidate for automatic table optimization.

For more information about DISTSTYLE EVEN, go to [CREATE MATERIALIZED VIEW](materialized-view-create-sql-command.md "materialized-view-create-sql-command.md").

ALTER DISTKEY _column_name_ or ALTER DISTSTYLE KEY DISTKEY
_column_name_

A clause that changes the column used as the distribution key of a relation.
Consider the following:

- VACUUM and ALTER DISTKEY can't run concurrently on the same
  relation.
  - If VACUUM is already running, then ALTER DISTKEY returns an
    error.
  - If ALTER DISTKEY is running, then background vacuum doesn't
    start on a relation.
  - If ALTER DISTKEY is running, then foreground vacuum returns an
    error.

- You can only run one ALTER DISTKEY command on a relation at a time.
- The ALTER DISTKEY command is not supported for relations with
  interleaved sort keys.
- If the distribution style was previously defined as AUTO, then the
  relation is no longer a candidate for automatic table optimization.

When specifying DISTSTYLE KEY, the data is distributed by the values in the
DISTKEY column. For more information about DISTSTYLE, go to [CREATE MATERIALIZED VIEW](materialized-view-create-sql-command.md "materialized-view-create-sql-command.md").

ALTER DISTSTYLE AUTO

A clause that changes the existing distribution style of a relation to AUTO.

When you alter a distribution style to AUTO, the distribution style of the
relation is set to the following:

- A small relation with DISTSTYLE ALL is converted to AUTO(ALL).
- A small relation with DISTSTYLE EVEN is converted to AUTO(ALL).
- A small relation with DISTSTYLE KEY is converted to AUTO(ALL).
- A large relation with DISTSTYLE ALL is converted to AUTO(EVEN).
- A large relation with DISTSTYLE EVEN is converted to AUTO(EVEN).
- A large relation with DISTSTYLE KEY is converted to AUTO(KEY) and the
  DISTKEY is preserved. In this case, Amazon Redshift makes no changes to the
  relation.

If Amazon Redshift determines that a new distribution style or key will improve the
performance of queries, then Amazon Redshift might change the distribution style or key of
your relation in the future. For example, Amazon Redshift might convert a relation
with a DISTSTYLE of AUTO(KEY) to AUTO(EVEN), or vice versa. For more
information about behavior when distribution keys are altered, including data
redistribution and locks, go to [Amazon Redshift Advisor recommendations](advisor-recommendations.md#alter-diststyle-distkey-recommendation "advisor-recommendations.md#alter-diststyle-distkey-recommendation").

For more information about DISTSTYLE AUTO, go to [CREATE MATERIALIZED VIEW](materialized-view-create-sql-command.md "materialized-view-create-sql-command.md").

To view the distribution style of a relation, query the SVV_TABLE_INFO
system catalog view. For more information, go to [SVV_TABLE_INFO](r_SVV_TABLE_INFO.md "r_SVV_TABLE_INFO.md"). To view the
Amazon Redshift Advisor recommendations for relations, query the
SVV_ALTER_TABLE_RECOMMENDATIONS system catalog view. For more information, go
to [SVV_ALTER_TABLE_RECOMMENDATIONS](r_SVV_ALTER_TABLE_RECOMMENDATIONS.md "r_SVV_ALTER_TABLE_RECOMMENDATIONS.md"). To view the actions
taken by Amazon Redshift, query the SVL_AUTO_WORKER_ACTION system catalog view. For more
information, go to [SVL_AUTO_WORKER_ACTION](r_SVL_AUTO_WORKER_ACTION.md "r_SVL_AUTO_WORKER_ACTION.md").

ALTER [COMPOUND] SORTKEY ( _column_name_ [,...] )

A clause that changes or adds the sort key used for a relation. ALTER
SORTKEY isn't supported for temporary tables.

When you alter a sort key, the compression encoding of columns in the new or
original sort key can change. If no encoding is explicitly defined for the
relation, then Amazon Redshift automatically assigns compression encodings as
follows:

- Columns that are defined as sort keys are assigned RAW
  compression.
- Columns that are defined as BOOLEAN, REAL, or DOUBLE PRECISION data
  types are assigned RAW compression.
- Columns that are defined as SMALLINT, INTEGER, BIGINT, DECIMAL, DATE,
  TIME, TIMETZ, TIMESTAMP, or TIMESTAMPTZ are assigned AZ64
  compression.
- Columns that are defined as CHAR or VARCHAR are assigned LZO
  compression.

Consider the following:

- You can define a maximum of 400 columns for a sort key per relation.
- You can alter an interleaved sort key to a compound sort key or no
  sort key. However, you can't alter a compound sort key to an
  interleaved sort key.
- If the sort key was previously defined as AUTO, then the relation is
  no longer a candidate for automatic table optimization.
- Amazon Redshift recommends using RAW encoding (no compression) for columns
  defined as sort keys. When you alter a column to choose it as a sort key,
  the column’s compression is changed to RAW compression (no compression).
  This can increase the amount of storage required by the relation. How
  much the relation size increases depend on the specific relation
  definition and relation contents. For more information about compression,
  go to [Compression encodings](c_Compression_encodings.md "c_Compression_encodings.md").

When data is loaded into a relation, the data is loaded in the order of the
sort key. When you alter the sort key, Amazon Redshift reorders the data. For more
information about SORTKEY, go to [CREATE MATERIALIZED VIEW](materialized-view-create-sql-command.md "materialized-view-create-sql-command.md").

ALTER SORTKEY AUTO

A clause that changes or adds the sort key of the target relation to AUTO.
ALTER SORTKEY AUTO isn't supported for temporary tables.

When you alter a sort key to AUTO, Amazon Redshift preserves the existing sort key of
the relation.

If Amazon Redshift determines that a new sort key will improve the performance of
queries, then Amazon Redshift might change the sort key of your relation in the future.

For more information about SORTKEY AUTO, go to [CREATE MATERIALIZED VIEW](materialized-view-create-sql-command.md "materialized-view-create-sql-command.md").

To view the sort key of a relation, query the SVV_TABLE_INFO system catalog
view. For more information, go to [SVV_TABLE_INFO](r_SVV_TABLE_INFO.md "r_SVV_TABLE_INFO.md"). To view the Amazon Redshift Advisor recommendations
for relations, query the SVV_ALTER_TABLE_RECOMMENDATIONS system catalog view.
For more information, go to [SVV_ALTER_TABLE_RECOMMENDATIONS](r_SVV_ALTER_TABLE_RECOMMENDATIONS.md "r_SVV_ALTER_TABLE_RECOMMENDATIONS.md"). To view the actions
taken by Amazon Redshift, query the SVL_AUTO_WORKER_ACTION system catalog view. For more
information, go to [SVL_AUTO_WORKER_ACTION](r_SVL_AUTO_WORKER_ACTION.md "r_SVL_AUTO_WORKER_ACTION.md").

ALTER SORTKEY NONE

A clause that removes the sort key of the target relation.

If the sort key was previously defined as AUTO, then the relation is no
longer a candidate for automatic table optimization.

ROW LEVEL SECURITY { ON | OFF } [ CONJUNCTION TYPE { AND | OR } ] [ FOR
DATASHARES ]

A clause that turns on or off row-level security for a relation.

When row-level security is turned on for a relation, you can only read the
rows that the row-level security policy permits you to access. When there
isn't any policy granting you access to the relation, you can't see
any rows from the relation. Only superusers and users or roles that have the
`sys:secadmin` role can set the ROW LEVEL SECURITY clause. For
more information, see [Row-level security](t_rls.md "t_rls.md").

- [ CONJUNCTION TYPE { AND | OR } ]

A clause that allows you to choose the conjunction type of row-level
security policy for a relation. When multiple row-level security policies
are attached to a relation, you can combine the policies with the AND or
OR clause. By default, Amazon Redshift combines RLS policies with the AND
clause. Superusers, users, or roles that have the
`sys:secadmin` role can use this clause to define the
conjunction type of row-level security policy for a relation. For more
information, see [Combining multiple policies per user](t_rls_combine_policies.md "t_rls_combine_policies.md").

- FOR DATASHARES

A clause that determines whether an RLS-protected relation can be
accessed over datashares. By default, an RLS-protected relation can’t be
accessed over a datashare. An ALTER MATERIALIZED VIEW ROW LEVEL SECURITY
command run with this clause only affects the relation’s datashare
accessibility property. The ROW LEVEL SECURITY property isn’t
changed.

If you make an RLS-protected relation accessible over datashares, the
relation doesn’t have row-level security in the consumer-side datashared
database. The relation retains its RLS property on the producer side.

## Examples

The following example enables the `tickets_mv` materialized view to be
automatically refreshed.

```
ALTER MATERIALIZED VIEW tickets_mv AUTO REFRESH YES
```
