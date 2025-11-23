# Oracle automatic indexing and self-managed PostgreSQL

With AWS DMS, you can migrate databases to Amazon Aurora PostgreSQL with the self-managed PostgreSQL option or Oracle databases with the automatic indexing feature. Self-managed PostgreSQL provides more control over database configurations and settings, while automatic indexing optimizes indexes for Oracle databases automatically.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                | Key differences                                                                                                                                             |
| ------------------------------ | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| One star feature compatibility | No automation                      | [Indexes](chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.indexes "chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.indexes") | PostgreSQL doesn’t provide an automatic indexing feature but in self-managed PostgreSQL instances you can use some extensions for automatic index creation. |

## Oracle usage

Oracle 19 introduces automatic indexing feature. This feature automates the index management tasks by automatically creating, rebuilding, and dropping indexes based on the changes in application workload, thus improving database performance.

Important functionality provided by automatic indexing:

- Automatic indexing process runs in the background at a predefined time interval and analyzes application workload. It identifies the tables/columns that are candidates for new indexes and creates new indexes.
- The auto indexes as initially created as invisible indexes. These invisible auto indexes are verified against SQL statements and if the performance is improved, then these indexes are converted as visible indexes.
- Identify and drop any existing under-performing auto indexes or any auto indexes not used for long period.
- Rebuilds the auto indexes that are marked unusable due to DDL operations.
- Provides package DBMS_AUTO_INDEX to configure automatic indexing and for generating reports related to automatic indexing operations.

###### Note

Up to date table statistics are very important for the Auto indexing to function efficiently. Tables without statistics or with stale statistics aren’t considered for auto indexing.

Package `DBMS_AUTO_INDEX` is used to configuring auto indexes and generating reports. Following are some of the configuration options which can be set by using `CONFIGURE` procedure of `DBMS_AUTO_INDEX` package:

- Enabling and disabling automatic indexing in a database.
- Specifying schemas and tables that can use auto indexes.
- Specifying a retention period for unused auto indexes. By default, the unused auto indexes are deleted after 373 days.
- Specifying a retention period for unused non-auto indexes.
- Specifying a tablespace and a percentage of tablespace to store auto indexes.

Following are some of the reports related to automatic indexing operations which you can generate using `REPORT_ACTIVITY` and `REPORT_LAST_ACTIVITY` functions of the `DBMS_AUTO_INDEX` package.

- Report of automatic indexing operations for a specific period.
- Report of the last automatic indexing operation.

For more information, see [Managing Indexes](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/managing-indexes.html#GUID-E4149397-FF37-4367-A12F-675433715904 "https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/managing-indexes.html#GUID-E4149397-FF37-4367-A12F-675433715904") in the _Oracle documentation_.

## PostgreSQL usage

PostgreSQL doesn’t provide an automatic indexing feature. However, in self-managed PostgreSQL instances, you can use extensions such as [Dexter](https://github.com/ankane/dexter "https://github.com/ankane/dexter") or [HypoPG](https://hypopg.readthedocs.io/en/latest/ "https://hypopg.readthedocs.io/en/latest/") to generate indexes with limitations. Amazon Aurora PostgreSQL doesn’t support these extensions.

These extensions use the following approach:

- Identify the queries.
- Update the table statistics if they haven’t been analyzed recently.
- Get the initial cost of the queries and create hypothetical indexes on columns that aren’t already indexes.
- Get costs again and see if any hypothetical indexes were used. Hypothetical indexes that were used and significantly reduced cost are selected to be indexes.

Find the examples and user guides for [Dexter](https://github.com/ankane/dexter "https://github.com/ankane/dexter") or [HypoPG](https://hypopg.readthedocs.io/en/latest/ "https://hypopg.readthedocs.io/en/latest/") in the official documentation.

Another applicable option for Aurora for PostgreSQL would be to run a scheduled set of queries to estimate if additional indexes are needed.

The following queries can help determine that.

Find user-tables without primary keys.

```
SELECT c.table_schema, c.table_name, c.table_type
FROM information_schema.tables c
WHERE c.table_schema NOT IN('information_schema', 'pg_catalog') AND c.table_type = 'BASE TABLE'
AND NOT EXISTS(SELECT i.tablename FROM pg_catalog.pg_indexes i
  WHERE i.schemaname = c.table_schema
  AND i.tablename = c.table_name AND indexdef LIKE '%UNIQUE%')
AND NOT EXISTS (SELECT cu.table_name FROM information_schema.key_column_usage cu
  WHERE cu.table_schema = c.table_schema AND
  cu.table_name = c.table_name)
ORDER BY c.table_schema, c.table_name;
```

Query all geometry tables that have no index on the geometry column.

```
SELECT c.table_schema, c.table_name, c.column_name
FROM (SELECT * FROM information_schema.tables WHERE table_type = 'BASE TABLE') As t
INNER JOIN (SELECT * FROM information_schema.columns WHERE udt_name = 'geometry') c
  ON (t.table_name = c.table_name AND t.table_schema = c.table_schema)
  LEFT JOIN pg_catalog.pg_indexes i ON
  (i.tablename = c.table_name AND i.schemaname = c.table_schema
  AND indexdef LIKE '%' || c.column_name || '%')
WHERE i.tablename IS NULL
ORDER BY c.table_schema, c.table_name;
```

Unused indexes that can probably be dropped.

```
SELECT s.relname, indexrelname, i.indisunique, idx_scan
FROM pg_catalog.pg_stat_user_indexes s, pg_index i
WHERE i.indexrelid = s.indexrelid and idx_scan = 0;
```

All of these should not be implemented in a script to decide if indexes should be created or dropped in a production environment. The Oracle automatic indexes will first assess if a new index is needed and if so, it will create an invisible index and only after ensuring nothing is harmed, then the index will become visible. This process can’t be used in PostgreSQL to avoid any production performance issues as PostgreSQL doesn’t allow for indexes be created have them be invisible.
