Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CREATE MATERIALIZED VIEW

Creates a materialized view based on one or more Amazon Redshift tables. You can also base
materialized views on external tables created using Spectrum or federated query. For
information about Spectrum, see [Amazon Redshift Spectrum](c-using-spectrum.md "c-using-spectrum.md"). For information about federated query, see [Querying data with federated queries in Amazon Redshift](federated-overview.md "federated-overview.md").

## Syntax

```
CREATE MATERIALIZED VIEW mv_name
[ BACKUP { YES | NO } ]
[ table_attributes ]
[ AUTO REFRESH { YES | NO } ]
AS query
```

## Parameters

BACKUP

A clause that specifies whether the materialized view should be included in
automated and manual cluster snapshots.

For materialized views that don't contain critical
data, specify BACKUP NO to save processing time when creating snapshots and
restoring from snapshots and to reduce storage space on Amazon Simple Storage Service. The BACKUP NO
setting has no affect on automatic replication of data to other nodes within
the cluster, so materialized views with BACKUP NO specified are restored in the
event of a node failure. The default is BACKUP YES.

_table_attributes_

A clause that specifies how the data in the materialized view is
distributed, including the following:

- The distribution style for the materialized view, in the format
  `DISTSTYLE { EVEN | ALL | KEY }`. If you omit this clause,
  the distribution style is `EVEN`. For more information, see
  [Distribution styles](c_choosing_dist_sort.md "c_choosing_dist_sort.md").
- The distribution key for the materialized view, in the format
  `DISTKEY ( *distkey\_identifier*
)`. For more information, see [Designating distribution
  styles](t_designating_distribution_styles.md "t_designating_distribution_styles.md").
- The sort key for the materialized view, in the format `SORTKEY (
*column\_name* [, ...] )`.
  For more information, see [Sort keys](t_Sorting_data.md "t_Sorting_data.md").

AS _query_

A valid `SELECT` statement that defines the materialized view and
its content. The result set from the query defines the columns and rows of the
materialized view. For information about limitations when creating materialized
views, see [Limitations](#mv_CREATE_MATERIALIZED_VIEW-limitations "#mv_CREATE_MATERIALIZED_VIEW-limitations").

Furthermore, specific SQL language constructs used in the query determines
whether the materialized view can be incrementally or fully refreshed. For
information about the refresh method, see [REFRESH MATERIALIZED VIEW](materialized-view-refresh-sql-command.md "materialized-view-refresh-sql-command.md"). For information
about the limitations for incremental refresh, see [Limitations for incremental
refresh](materialized-view-refresh-sql-command.md#mv_REFRESH_MARTERIALIZED_VIEW_limitations "materialized-view-refresh-sql-command.md#mv_REFRESH_MARTERIALIZED_VIEW_limitations").

If the query contains an SQL command that doesn't support incremental
refresh, Amazon Redshift displays a message indicating that the materialized view will use
a full refresh. The message may or may not be displayed, depending on the SQL
client application.
Check the `state` column of the
[STV_MV_INFO](r_STV_MV_INFO.md "r_STV_MV_INFO.md") to see the
refresh type used by a materialized view.

AUTO REFRESH

A clause that defines whether the materialized view should be automatically
refreshed with latest changes from its base tables. The default value is
`NO`. For more information, see [Refreshing a materialized view](materialized-view-refresh.md "materialized-view-refresh.md").

## Usage notes

To create a materialized view, you must have the following privileges:

- CREATE privileges for a schema.
- Table-level or column-level SELECT privilege on the base tables to create a
  materialized view. If you have column-level privileges on specific columns, you
  can create a materialized view on only those columns.

## Incremental refresh for

materialized views in a datashare

Amazon Redshift supports automatic and incremental refresh for materialized views in a consumer
datashare when the base tables are shared. Incremental refresh is an operation where
Amazon Redshift identifies changes in the base table or tables that happened after the previous
refresh and updates only the corresponding records in the materialized view. This runs
more quickly than a full refresh and improves workload performance. You don't have to
change your materialized-view definition to take advantage of incremental refresh.

There are a couple limitations to note for taking advantage of incremental refresh
with a materialized view:

- The materialized view must reference only one database, either local or remote.
- Incremental refresh is available only on new materialized views. Therefore, you
  must drop existing materialized views and recreate them for incremental refresh to
  occur.

For more information about creating materialized views in a datashare, see [Working with views in Amazon Redshift
data sharing](datashare-views.md "datashare-views.md"), which contains several query examples.

## DDL updates to materialized views or base

tables

When using materialized views in Amazon Redshift, follow these usage notes for data definition
language (DDL) updates to materialized views or base tables.

- You can add columns to a base table without affecting any materialized views
  that reference the base table.
- Some operations can leave the materialized view in a state that can't be
  refreshed at all. Examples are operations such as renaming or dropping a column,
  changing the type of a column, and changing the name of a schema. Such
  materialized views can be queried but can't be refreshed. In this case, you
  must drop and recreate the materialized view.
- In general, you can't alter a materialized view's definition (its SQL
  statement).
- You can't rename a materialized view.

## Limitations

You can't define a materialized view that references or includes any of the
following:

- Standard views, or system tables and views.
- Temporary tables.
- User-defined functions.
- The ORDER BY, LIMIT, or OFFSET clause.
- Late-binding references to base tables. In other words, any base tables or
  related columns referenced in the defining SQL query of the materialized view must
  exist and must be valid.
- Leader node-only functions: CURRENT_SCHEMA, CURRENT_SCHEMAS,
  HAS_DATABASE_PRIVILEGE, HAS_SCHEMA_PRIVILEGE, HAS_TABLE_PRIVILEGE.
- You can't use the AUTO REFRESH YES option when the materialized view
  definition includes mutable functions or external schemas. You also can't use it
  when you define a materialized view on another materialized view.
- You don't have to manually run [ANALYZE](r_ANALYZE.md "r_ANALYZE.md") on materialized views. This happens currently only
  via AUTO ANALYZE. For more information, see [Analyzing tables](t_Analyzing_tables.md "t_Analyzing_tables.md").
- RLS-protected or DDM-protected tables.

## Examples

The following example creates a materialized view from three base tables that are
joined and aggregated. Each row represents a category with the number of tickets sold.
When you query the tickets_mv materialized view, you directly access the precomputed
data in the tickets_mv materialized view.

```
CREATE MATERIALIZED VIEW tickets_mv AS
    select   catgroup,
    sum(qtysold) as sold
    from     category c, event e, sales s
    where    c.catid = e.catid
    and      e.eventid = s.eventid
    group by catgroup;
```

The following example creates a materialized view similar to the previous example and
uses the aggregate function MAX().

```
CREATE MATERIALIZED VIEW tickets_mv_max AS
    select   catgroup,
    max(qtysold) as sold
    from     category c, event e, sales s
    where    c.catid = e.catid
    and      e.eventid = s.eventid
    group by catgroup;

SELECT name, state FROM STV_MV_INFO;
```

The following example uses a UNION ALL clause to join the Amazon Redshift
`public_sales` table and the Redshift Spectrum `spectrum.sales` table to
create a material view `mv_sales_vw`. For information about the CREATE
EXTERNAL TABLE command for Amazon Redshift Spectrum, see [CREATE EXTERNAL TABLE](r_CREATE_EXTERNAL_TABLE.md "r_CREATE_EXTERNAL_TABLE.md"). The Redshift Spectrum external table references the
data on Amazon S3.

```
CREATE MATERIALIZED VIEW mv_sales_vw as
select salesid, qtysold, pricepaid, commission, saletime from public.sales
union all
select salesid, qtysold, pricepaid, commission, saletime from spectrum.sales

```

The following example creates a materialized view `mv_fq` based on a
federated query external table. For information about federated query, see [CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md").

```
CREATE MATERIALIZED VIEW mv_fq as select firstname, lastname from apg.mv_fq_example;

select firstname, lastname from mv_fq;
 firstname | lastname
-----------+----------
 John      | Day
 Jane      | Doe
(2 rows)
```

The following example shows the definition of a materialized view.

```
SELECT pg_catalog.pg_get_viewdef('mv_sales_vw'::regclass::oid, true);

pg_get_viewdef
---------------------------------------------------
create materialized view mv_sales_vw as select a from t;
```

The following sample shows how to set AUTO REFRESH in the materialized view
definition and also specifies a DISTSTYLE. First, create a simple base table.

```
CREATE TABLE baseball_table (ball int, bat int);
```

Then, create a materialized view.

```
CREATE MATERIALIZED VIEW mv_baseball DISTSTYLE ALL AUTO REFRESH YES AS SELECT ball AS baseball FROM baseball_table;
```

Now you can query the mv_baseball materialized view. To check if AUTO REFRESH is
turned on for a materialized view, see [STV_MV_INFO](r_STV_MV_INFO.md "r_STV_MV_INFO.md").

The following sample creates a materialized view that references a source table in
another database. It assumes that the database containing the source table, database_A,
is in the same cluster or workgroup as your materialized view, which you create in
database_B. (You can substitute your own databases for the sample.) First, create a
table in database_A called _cities_, with
a *cityname* column. Make the column's data type a VARCHAR. After
you create the source table, run the following command in database_B to create a
materialized view whose source is your *cities* table. Make sure to
specify the source table's database and schema in the FROM clause:

```
CREATE MATERIALIZED VIEW cities_mv AS
SELECT  cityname
FROM    database_A.public.cities;
```

Query the materialized view you created. The query retrieves records whose original
source is the *cities* table in database_A:

```
select * from cities_mv;
```

When you run the SELECT statement, _cities_mv_ returns the
records. Records are refreshed from the source table only when a REFRESH statement is
run. Also, note that you can't update records directly in the materialized view. For
information about refreshing the data in a materialized view, see [REFRESH MATERIALIZED VIEW](materialized-view-refresh-sql-command.md "materialized-view-refresh-sql-command.md").

For details about materialized view overview and SQL commands used to refresh and
drop materialized views, see the following topics:

- [Materialized views in Amazon Redshift](materialized-view-overview.md "materialized-view-overview.md")
- [REFRESH MATERIALIZED VIEW](materialized-view-refresh-sql-command.md "materialized-view-refresh-sql-command.md")
- [DROP MATERIALIZED VIEW](materialized-view-drop-sql-command.md "materialized-view-drop-sql-command.md")
