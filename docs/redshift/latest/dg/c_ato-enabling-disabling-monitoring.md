Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Enabling, disabling, and monitoring automatic table optimization

By default, tables created without explicitly defining sort keys or distributions keys are set to `AUTO`.
At the time of table creation, you can also explicitly set a sort or a distribution key manually.
If you set the sort or distribution key, then the table is not automatically managed.

## Enabling automatic table optimization

To enable an existing table to be automatically optimized,
use the ALTER statement options to change the table to `AUTO`.
You might choose to define automation for sort keys, but not for distribution keys (and vice versa).

If you run an ALTER statement to convert a table to be an automated table, existing sort keys and distribution styles are preserved.

```
ALTER TABLE `table_name` ALTER SORTKEY AUTO;
```

```
ALTER TABLE `table_name` ALTER DISTSTYLE AUTO;
```

For more information, see
[ALTER TABLE](r_ALTER_TABLE.md "r_ALTER_TABLE.md").

Initially, a table has no distribution key or sort key. The distribution style is
set to either `EVEN` or `ALL` depending on table size. As the
table grows in size, Amazon Redshift applies the optimal distribution keys and sort keys.
Optimizations are applied within hours after a minimum number of queries are run.
When determining sort key optimizations, Amazon Redshift attempts to optimize the data blocks read from disk during a table scan.
When determining distribution style optimizations, Amazon Redshift tries to optimize the number of bytes transferred between cluster nodes.

## Removing automatic table optimization from a table

You can remove a table from automatic optimization. Removing a table from automation
involves selecting a sort key or distribution style. To change distribution style,
specify a specific distribution style.

```
ALTER TABLE `table_name` ALTER DISTSTYLE EVEN;
```

```
ALTER TABLE `table_name` ALTER DISTSTYLE ALL;
```

```
ALTER TABLE `table_name` ALTER DISTSTYLE KEY DISTKEY `c1`;
```

To change a sort key, you can define a sort key or choose none.

```
ALTER TABLE `table_name` ALTER SORTKEY(`c1, c2`);
```

```
ALTER TABLE `table_name` ALTER SORTKEY NONE;
```

## Monitoring automatic table optimization

The system view `SVV_ALTER_TABLE_RECOMMENDATIONS` records the current Amazon Redshift
Advisor recommendations for tables. This view shows recommendations for all tables,
those that are defined for automatic optimization and those that aren't.

To view if a table is defined for automatic optimization, query the system view
`SVV_TABLE_INFO`. Entries appear only for tables visible in the current
session's database. Recommendations are inserted into the view twice per day starting
within hours from the time the cluster was created. After a recommendation is available,
it's started within an hour. After a recommendation has been applied (either by Amazon Redshift or
by you), it no longer appears in the view.

The system view `SVL_AUTO_WORKER_ACTION` shows an audit log of all actions taken by Amazon Redshift,
and the previous state of the table.

The system view `SVV_TABLE_INFO` lists all of the tables in the system,
along with a column to indicate whether the sort key and distribution style of the table is set to `AUTO`.

For more information about these system views, see
[System monitoring (provisioned only)](c_intro_system_views.md "c_intro_system_views.md").
