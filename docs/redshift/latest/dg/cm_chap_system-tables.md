Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# System tables and views reference

Amazon Redshift has many system tables and views that contain information about how the
system is functioning. You can query these system tables and views the same way that you
would query any other database tables. This section shows some sample system table
queries and explains:

- How different types of system tables and views are generated
- What types of information you can obtain from these tables
- How to join Amazon Redshift system tables to catalog tables
- How to manage the growth of system table log files
  Some system tables can only be used by AWS staff for diagnostic purposes. The
  following sections discuss the system tables that can be queried for useful information
  by system administrators or other database users.

###### Note

System tables are not included in automated or manual cluster backups (snapshots).
STL system views retain seven days of log history. Retaining logs doesn't require
any customer action, but if you want to store log data for more than 7 days, you
have to periodically copy it to other tables or unload it to Amazon S3.

###### Topics

- [Types of system tables and views](#c_types-of-system-tables-and-views "#c_types-of-system-tables-and-views")
- [Visibility of data in system tables and
  views](#c_visibility-of-data "#c_visibility-of-data")
- [Migrating provisioned-only queries to SYS
  monitoring view queries](#sys_view_migration-use_cases "#sys_view_migration-use_cases")
- [Improving query identifier tracking using
  the SYS monitoring views](#sys_view_migration-query-id "#sys_view_migration-query-id")
- [System table query, process,
  and session ids](#system-table-query-process-session-ids "#system-table-query-process-session-ids")
- [SVV metadata views](svv_views.md "svv_views.md")
- [SYS monitoring views](serverless_views-monitoring.md "serverless_views-monitoring.md")
- [System view mapping for migrating to SYS monitoring views](sys_view_migration.md "sys_view_migration.md")
- [System monitoring (provisioned only)](c_intro_system_views.md "c_intro_system_views.md")
- [System catalog tables](c_intro_catalog_views.md "c_intro_catalog_views.md")

## Types of system tables and views

There are several types of system tables and views:

- SVV views contain information about database objects with references to
  transient STV tables.
- SYS views are used to monitor query and workload usage for provisioned
  clusters and serverless workgroups.
- STL views are generated from logs that have been persisted to disk to provide
  a history of the system.
- STV tables are virtual system tables that contain snapshots of the current
  system data. They are based on transient in-memory data and are not persisted to
  disk-based logs or regular tables.
- SVCS views provide details about queries on both the main and concurrency
  scaling clusters.
- SVL views provide details about queries on main clusters.

System tables and views do not use the same consistency model as regular tables. It is
important to be aware of this issue when querying them, especially for STV tables and
SVV views. For example, given a regular table t1 with a column c1, you would expect that
the following query to return no rows:

```
select * from t1
where c1 > (select max(c1) from t1)
```

However, the following query against a system table might well return rows:

```
select * from stv_exec_state
where currenttime > (select max(currenttime) from stv_exec_state)
```

The reason this query might return rows is that currenttime is transient and the two
references in the query might not return the same value when evaluated.

On the other hand, the following query might well return no rows:

```
select * from stv_exec_state
where currenttime = (select max(currenttime) from stv_exec_state)
```

## Visibility of data in system tables and

views

###### Note

Amazon Redshift automatically masks certain system table columns when logging information
about queries made to Data Catalog views to prevent exposure of sensitive metadata. For
more information, see
[Secure logging](../mgmt/db-auditing-secure-logging.md "../mgmt/db-auditing-secure-logging.md") in the _Amazon Redshift Management Guide_.

There are two classes of visibility for data in system tables and views: visible to
users and visible to superusers.

Only users with superuser privileges can see the data in those tables that are in the
superuser-visible category. Regular users can see data in the user-visible tables. To
give a regular user access to superuser-visible tables, grant SELECT privilege on that
table to the regular user. For more information, see [GRANT](r_GRANT.md "r_GRANT.md").

By default, in most user-visible tables, rows generated by another user are invisible
to a regular user. If a regular user is given [SYSLOG ACCESS UNRESTRICTED](r_ALTER_USER.md#alter-user-syslog-access "r_ALTER_USER.md#alter-user-syslog-access"), that user can see all rows in user-visible
tables, including rows generated by another user. For more information, see [ALTER USER](r_ALTER_USER.md "r_ALTER_USER.md") or [CREATE USER](r_CREATE_USER.md "r_CREATE_USER.md").
All rows
in SVV_TRANSACTIONS are visible to all users. For more information about data
visibility, see the AWS re:Post knowledge base article [How can I allow
Amazon Redshift database regular users permission to view data in system tables from
other users for my cluster?](https://repost.aws/knowledge-center/amazon-redshift-system-tables "https://repost.aws/knowledge-center/amazon-redshift-system-tables").

For metadata views, Amazon Redshift doesn't allow visibility to users that are granted
SYSLOG ACCESS UNRESTRICTED.

###### Note

Giving a user unrestricted access to system tables gives the user visibility to
data generated by other users. For example, STL_QUERY and STL_QUERY_TEXT contain the
full text of INSERT, UPDATE, and DELETE statements, which might contain sensitive
user-generated data.

A superuser can see all rows in all tables. To give a regular user access to
superuser-visible tables, [GRANT](r_GRANT.md "r_GRANT.md") SELECT
privilege on that table to the regular user.

### Filtering system-generated

queries

The query-related system tables and views, such as SVL_QUERY_SUMMARY, SVL_QLOG,
and others, usually contain a large number of automatically generated statements
that Amazon Redshift uses to monitor the status of the database. These system-generated
queries are visible to a superuser, but are seldom useful. To filter them out when
selecting from a system table or system view that uses the `userid`
column, add the condition `userid > 1` to the WHERE clause. For
example:

```
 select * from svl_query_summary where userid > 1
```

## Migrating provisioned-only queries to SYS

monitoring view queries

### Migrating from provisioned

clusters to Amazon Redshift Serverless

If you're migrating a provisioned cluster to Amazon Redshift Serverless, you may have queries using
the following system views, which only store data from provisioned clusters.

- All STL views
- All STV views
- All SVCS views
- All SVL views
- Some SVV views
  - For a full list of SVV views unsupported in Amazon Redshift Serverless, see the
    list at the bottom of [Monitoring queries and workloads with Amazon Redshift Serverless](../mgmt/serverless-monitoring.md "../mgmt/serverless-monitoring.md") in the
    _Amazon Redshift Management Guide_.

To keep using your queries, refit them to use columns defined in the SYS
monitoring views that correspond to the columns in your provisioned-only views. To
see the mapping relation between the provisioned-only views and the SYS monitoring
views, go to [System view mapping for migrating to SYS monitoring views](sys_view_migration.md "sys_view_migration.md")

### Updating queries while

staying on a provisioned cluster

If you're not migrating to Amazon Redshift Serverless, you might still want to update your existing
queries. The SYS monitoring views are designed for ease of use and reduced
complexity, providing a complete array of metrics for effective monitoring and
troubleshooting. Using SYS views such as [SYS_QUERY_HISTORY](SYS_QUERY_HISTORY.md "SYS_QUERY_HISTORY.md") and [SYS_QUERY_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md") that consolidate the information of multiple
provisioned-only views, you can streamline your queries.

## Improving query identifier tracking using

the SYS monitoring views

SYS monitoring views such as such as [SYS_QUERY_HISTORY](SYS_QUERY_HISTORY.md "SYS_QUERY_HISTORY.md") and [SYS_QUERY_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md") contain the query_id column, which holds the
identifier for users’ queries. Similarly, provisioned-only views such as [STL_QUERY](r_STL_QUERY.md "r_STL_QUERY.md") and [SVL_QLOG](r_SVL_QLOG.md "r_SVL_QLOG.md") contain the query column, which also holds the query
identifiers. However, the query identifiers recorded in the SYS system views are
different from those recorded in the provisioned-only views.

The difference between the SYS views’ query_id column values and the provisioned-only
views’ query column values is as follows:

- In SYS views, the query_id column records user-submitted queries in their
  original form. The Amazon Redshift optimizer might break them down into child queries
  for improved performance, but a single query you run will still only have a
  single row in [SYS_QUERY_HISTORY](SYS_QUERY_HISTORY.md "SYS_QUERY_HISTORY.md"). If you want to see the individual child
  queries, you can find them in [SYS_QUERY_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md").
- In provisioned-only views, the query column records queries at the child
  query level. If the Amazon Redshift optimizer rewrites your original query into
  multiple child queries, there will be multiple rows in [STL_QUERY](r_STL_QUERY.md "r_STL_QUERY.md") with differing query
  identifier values for a single query you run.

When you migrate your monitoring and diagnostic queries from provisioned-only views to
SYS views, consider this difference and edit your queries accordingly. For more
information on how Amazon Redshift processes queries, see [Query planning and execution workflow](c-query-planning.md "c-query-planning.md").

### Example

For an example of how Amazon Redshift records queries differently in provisioned-only and
SYS monitoring views, see the following sample query. This is the query written as
you would run it in Amazon Redshift.

```
SELECT
  s_name
  , COUNT(*) AS numwait
FROM
  supplier,
  lineitem l1,
  orders,
  nation
WHERE    s_suppkey = l1.l_suppkey
         AND o_orderkey = l1.l_orderkey
         AND o_orderstatus = 'F'
         AND l1.l_receiptdate > l1.l_commitdate
         AND EXISTS (SELECT
                       *
                     FROM
                       lineitem l2
                     WHERE  l2.l_orderkey = l1.l_orderkey
                            AND l2.l_suppkey <> l1.l_suppkey )
         AND NOT EXISTS (SELECT
                           *
                         FROM
                           lineitem l3
                         WHERE  l3.l_orderkey = l1.l_orderkey
                                AND l3.l_suppkey <> l1.l_suppkey
                                AND l3.l_receiptdate > l3.l_commitdate )
         AND s_nationkey = n_nationkey
         AND n_name = 'UNITED STATES'
GROUP BY
  s_name
ORDER BY
  numwait DESC
  , s_name LIMIT 100;
```

Under the hood the Amazon Redshift query optimizer rewrites the above user-submitted
query into 5 child queries.

The first child query creates a temporary table to materialize a subquery.

```
CREATE TEMP TABLE volt_tt_606590308b512(l_orderkey
                                        , l_suppkey
                                        , s_name   ) AS SELECT
                                                         l1.l_orderkey
                                                         , l1.l_suppkey
                                                         , public.supplier.s_name
                                                       FROM
                                                         public.lineitem AS l1,
                                                         public.nation,
                                                         public.orders,
                                                         public.supplier
                                                       WHERE  l1.l_commitdate < l1.l_receiptdate
                                                              AND l1.l_orderkey = public.orders.o_orderkey
                                                              AND l1.l_suppkey = public.supplier.s_suppkey
                                                              AND public.nation.n_name = 'UNITED STATES'::CHAR(8)
                                                              AND public.nation.n_nationkey = public.supplier.s_nationkey
                                                              AND public.orders.o_orderstatus = 'F'::CHAR(1);
```

The second child query collects statistics from the temporary table.

```
padb_fetch_sample: select count(*) from volt_tt_606590308b512;
```

The third child query creates another temporary table to materialize another
subquery, referencing the temporary table created above.

```
CREATE TEMP TABLE volt_tt_606590308c2ef(l_orderkey
                                        , l_suppkey) AS (SELECT
                                                          volt_tt_606590308b512.l_orderkey
                                                          , volt_tt_606590308b512.l_suppkey
                                                        FROM
                                                          public.lineitem AS l2,
                                                          volt_tt_606590308b512
                                                        WHERE  l2.l_suppkey <> volt_tt_606590308b512.l_suppkey
                                                               AND l2.l_orderkey = volt_tt_606590308b512.l_orderkey)
                                                               EXCEPT distinct (SELECT volt_tt_606590308b512.l_orderkey, volt_tt_606590308b512.l_suppkey
                                                               FROM public.lineitem AS l3, volt_tt_606590308b512
                                                               WHERE l3.l_commitdate < l3.l_receiptdate
                                                                 AND l3.l_suppkey <> volt_tt_606590308b512.l_suppkey
                                                                 AND l3.l_orderkey = volt_tt_606590308b512.l_orderkey);
```

The fourth child query again collects the temporary table’s statistics.

```
padb_fetch_sample: select count(*) from volt_tt_606590308c2ef
```

The last child query uses the temporary tables created above to generate the
output.

```
SELECT
  volt_tt_606590308b512.s_name AS s_name
  , COUNT(*) AS numwait
FROM
  volt_tt_606590308b512,
  volt_tt_606590308c2ef
WHERE    volt_tt_606590308b512.l_orderkey = volt_tt_606590308c2ef.l_orderkey
         AND volt_tt_606590308b512.l_suppkey = volt_tt_606590308c2ef.l_suppkey
GROUP BY
  1
ORDER BY
  2 DESC
  , 1 ASC LIMIT 100;
```

In the provisioned-only system view STL_QUERY, Amazon Redshift records five rows at the
child query level, as follows:

```
SELECT userid, xid, pid, query, querytxt::varchar(100);
FROM stl_query
WHERE xid = 48237350
ORDER BY xid, starttime;

 `userid | xid | pid | query | querytxt
--------+----------+------------+----------+------------------------------------------------------------------------------------------------------
 101 | 48237350 | 1073840810 | 12058151 | CREATE TEMP TABLE volt_tt_606590308b512(l_orderkey, l_suppkey, s_name) AS SELECT l1.l_orderkey, l1.l
 101 | 48237350 | 1073840810 | 12058152 | padb_fetch_sample: select count(*) from volt_tt_606590308b512
 101 | 48237350 | 1073840810 | 12058156 | CREATE TEMP TABLE volt_tt_606590308c2ef(l_orderkey, l_suppkey) AS (SELECT volt_tt_606590308b512.l_or
 101 | 48237350 | 1073840810 | 12058168 | padb_fetch_sample: select count(*) from volt_tt_606590308c2ef
 101 | 48237350 | 1073840810 | 12058170 | SELECT s_name , COUNT(*) AS numwait FROM supplier, lineitem l1, orders, nation WHERE s_suppkey = l1.
(5 rows)`
```

In the SYS monitoring view SYS_QUERY_HISTORY, Amazon Redshift records the query as
follows:

```
SELECT user_id, transaction_id, session_id, query_id, query_text::varchar(100)
FROM sys_query_history
WHERE transaction_id = 48237350
ORDER BY start_time;

 `user_id | transaction_id | session_id | query_id | query_text
---------+----------------+------------+----------+------------------------------------------------------------------------------------------------------
 101 | 48237350 | 1073840810 | 12058149 | SELECT s_name , COUNT(*) AS numwait FROM supplier, lineitem l1, orders, nation WHERE s_suppkey = l1.`
```

In SYS_QUERY_DETAIL, you can find child query-level details using the query_id
value from SYS_QUERY_HISTORY. The child_query_sequence column shows the order the
child queries are executed in. For more information on the columns in
SYS_QUERY_DETAIL, see [SYS_QUERY_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md").

```
select user_id,
       query_id,
       child_query_sequence,
       stream_id,
       segment_id,
       step_id,
       start_time,
       end_time,
       duration,
       blocks_read,
       blocks_write,
       local_read_io,
       remote_read_io,
       data_skewness,
       time_skewness,
       is_active,
       spilled_block_local_disk,
       spilled_block_remote_disk
from sys_query_detail
where query_id = 12058149
      and step_id = -1
order by query_id,
         child_query_sequence,
         stream_id,
         segment_id,
         step_id;

 `user_id | query_id | child_query_sequence | stream_id | segment_id | step_id | start_time | end_time | duration | blocks_read | blocks_write | local_read_io | remote_read_io | data_skewness | time_skewness | is_active | spilled_block_local_disk | spilled_block_remote_disk
---------+----------+----------------------+-----------+------------+---------+----------------------------+----------------------------+----------+-------------+--------------+---------------+----------------+---------------+---------------+-----------+--------------------------+---------------------------
 101 | 12058149 | 1 | 0 | 0 | -1 | 2023-09-27 15:40:38.512415 | 2023-09-27 15:40:38.533333 | 20918 | 0 | 0 | 0 | 0 | 0 | 44 | f | 0 | 0
 101 | 12058149 | 1 | 1 | 1 | -1 | 2023-09-27 15:40:39.931437 | 2023-09-27 15:40:39.972826 | 41389 | 12 | 0 | 12 | 0 | 0 | 77 | f | 0 | 0
 101 | 12058149 | 1 | 2 | 2 | -1 | 2023-09-27 15:40:40.584412 | 2023-09-27 15:40:40.613982 | 29570 | 32 | 0 | 32 | 0 | 0 | 25 | f | 0 | 0
 101 | 12058149 | 1 | 2 | 3 | -1 | 2023-09-27 15:40:40.582038 | 2023-09-27 15:40:40.615758 | 33720 | 0 | 0 | 0 | 0 | 0 | 1 | f | 0 | 0
 101 | 12058149 | 1 | 3 | 4 | -1 | 2023-09-27 15:40:46.668766 | 2023-09-27 15:40:46.705456 | 36690 | 24 | 0 | 15 | 0 | 0 | 17 | f | 0 | 0
 101 | 12058149 | 1 | 4 | 5 | -1 | 2023-09-27 15:40:46.707209 | 2023-09-27 15:40:46.709176 | 1967 | 0 | 0 | 0 | 0 | 0 | 18 | f | 0 | 0
 101 | 12058149 | 1 | 4 | 6 | -1 | 2023-09-27 15:40:46.70656 | 2023-09-27 15:40:46.71289 | 6330 | 0 | 0 | 0 | 0 | 0 | 0 | f | 0 | 0
 101 | 12058149 | 1 | 5 | 7 | -1 | 2023-09-27 15:40:46.71405 | 2023-09-27 15:40:46.714343 | 293 | 0 | 0 | 0 | 0 | 0 | 0 | f | 0 | 0
 101 | 12058149 | 2 | 0 | 0 | -1 | 2023-09-27 15:40:52.083907 | 2023-09-27 15:40:52.087854 | 3947 | 0 | 0 | 0 | 0 | 0 | 35 | f | 0 | 0
 101 | 12058149 | 2 | 1 | 1 | -1 | 2023-09-27 15:40:52.089632 | 2023-09-27 15:40:52.091129 | 1497 | 0 | 0 | 0 | 0 | 0 | 11 | f | 0 | 0
 101 | 12058149 | 2 | 1 | 2 | -1 | 2023-09-27 15:40:52.089008 | 2023-09-27 15:40:52.091306 | 2298 | 0 | 0 | 0 | 0 | 0 | 0 | f | 0 | 0
 101 | 12058149 | 3 | 0 | 0 | -1 | 2023-09-27 15:40:56.882013 | 2023-09-27 15:40:56.897282 | 15269 | 0 | 0 | 0 | 0 | 0 | 29 | f | 0 | 0
 101 | 12058149 | 3 | 1 | 1 | -1 | 2023-09-27 15:40:59.718554 | 2023-09-27 15:40:59.722789 | 4235 | 0 | 0 | 0 | 0 | 0 | 13 | f | 0 | 0
 101 | 12058149 | 3 | 2 | 2 | -1 | 2023-09-27 15:40:59.800382 | 2023-09-27 15:40:59.807388 | 7006 | 0 | 0 | 0 | 0 | 0 | 58 | f | 0 | 0
 101 | 12058149 | 3 | 3 | 3 | -1 | 2023-09-27 15:41:06.488685 | 2023-09-27 15:41:06.493825 | 5140 | 0 | 0 | 0 | 0 | 0 | 56 | f | 0 | 0
 101 | 12058149 | 3 | 3 | 4 | -1 | 2023-09-27 15:41:06.486206 | 2023-09-27 15:41:06.497756 | 11550 | 0 | 0 | 0 | 0 | 0 | 2 | f | 0 | 0
 101 | 12058149 | 3 | 4 | 5 | -1 | 2023-09-27 15:41:06.499201 | 2023-09-27 15:41:06.500851 | 1650 | 0 | 0 | 0 | 0 | 0 | 15 | f | 0 | 0
 101 | 12058149 | 3 | 4 | 6 | -1 | 2023-09-27 15:41:06.498609 | 2023-09-27 15:41:06.500949 | 2340 | 0 | 0 | 0 | 0 | 0 | 0 | f | 0 | 0
 101 | 12058149 | 3 | 5 | 7 | -1 | 2023-09-27 15:41:06.502945 | 2023-09-27 15:41:06.503282 | 337 | 0 | 0 | 0 | 0 | 0 | 0 | f | 0 | 0
 101 | 12058149 | 4 | 0 | 0 | -1 | 2023-09-27 15:41:06.62899 | 2023-09-27 15:41:06.631452 | 2462 | 0 | 0 | 0 | 0 | 0 | 22 | f | 0 | 0
 101 | 12058149 | 4 | 1 | 1 | -1 | 2023-09-27 15:41:06.632313 | 2023-09-27 15:41:06.63391 | 1597 | 0 | 0 | 0 | 0 | 0 | 20 | f | 0 | 0
 101 | 12058149 | 4 | 1 | 2 | -1 | 2023-09-27 15:41:06.631726 | 2023-09-27 15:41:06.633813 | 2087 | 0 | 0 | 0 | 0 | 0 | 0 | f | 0 | 0
 101 | 12058149 | 5 | 0 | 0 | -1 | 2023-09-27 15:41:12.571974 | 2023-09-27 15:41:12.584234 | 12260 | 0 | 0 | 0 | 0 | 0 | 39 | f | 0 | 0
 101 | 12058149 | 5 | 0 | 1 | -1 | 2023-09-27 15:41:12.569815 | 2023-09-27 15:41:12.585391 | 15576 | 0 | 0 | 0 | 0 | 0 | 4 | f | 0 | 0
 101 | 12058149 | 5 | 1 | 2 | -1 | 2023-09-27 15:41:13.758513 | 2023-09-27 15:41:13.76401 | 5497 | 0 | 0 | 0 | 0 | 0 | 39 | f | 0 | 0
 101 | 12058149 | 5 | 1 | 3 | -1 | 2023-09-27 15:41:13.749 | 2023-09-27 15:41:13.772987 | 23987 | 0 | 0 | 0 | 0 | 0 | 32 | f | 0 | 0
 101 | 12058149 | 5 | 2 | 4 | -1 | 2023-09-27 15:41:13.799526 | 2023-09-27 15:41:13.813506 | 13980 | 0 | 0 | 0 | 0 | 0 | 62 | f | 0 | 0
 101 | 12058149 | 5 | 2 | 5 | -1 | 2023-09-27 15:41:13.798823 | 2023-09-27 15:41:13.813651 | 14828 | 0 | 0 | 0 | 0 | 0 | 0 | f | 0 | 0
(28 rows)`
```

## System table query, process,

and session ids

When analyzing query, process, and session ids that appear in system tables, be aware
of the following:

- The query id value (in columns such as `query_id` and
  `query`) can be reused over time.
- The process id or session id value (in columns such as
  `process_id`, `pid`, and `session_id`) can be
  reused over time.
- The transaction id value (in columns such as `transaction_id` and
  `xid`) is unique.
