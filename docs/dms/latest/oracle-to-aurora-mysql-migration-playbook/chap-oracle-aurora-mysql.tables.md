# Oracle automatic indexing

With AWS DMS, you can leverage Oracle automatic indexing to optimize database performance and reduce manual tuning efforts.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                            | Key differences                                      |
| ------------------------------ | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| One star feature compatibility | No automation                      | [Indexes](chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.indexes "chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.indexes") | MySQL doesn’t provide an automatic indexing feature. |

## Oracle usage

Oracle 19 introduces the automatic indexing feature. This feature automates the index management tasks by automatically creating, rebuilding, and dropping indexes based on the changes in application workload, thus improving database performance.

Important functionality provided by automatic indexing:

- Automatic indexing process runs in the background at a predefined time interval and analyzes application workload. It identifies the tables/columns that are candidates for new indexes and creates new indexes.
- The auto indexes as initially created as invisible indexes. These invisible auto indexes are verified against SQL statements and if the performance is improved, then these indexes are converted as visible indexes.
- Identify and drop any existing under-performing auto indexes or any auto indexes not used for long period.
- Rebuilds the auto indexes that are marked unusable due to DDL operations.
- Provides package DBMS_AUTO_INDEX to configure automatic indexing and for generating reports related to automatic indexing operations.

###### Note

Up-to-date table statistics are very important for the auto indexing to function efficiently. Tables without statistics or with stale statistics aren’t considered for auto indexing.

Oracle uses the `DBMS_AUTO_INDEX` package to configure auto indexes and generating reports. Following are some of the configuration options which can be set by using `CONFIGURE` procedure of `DBMS_AUTO_INDEX` package:

- Turning on and turning off automatic indexing in a database.
- Specifying schemas and tables that can use auto indexes.
- Specifying a retention period for unused auto indexes. By default, the unused auto indexes are deleted after 373 days.
- Specifying a retention period for unused non-auto indexes.
- Specifying a tablespace and a percentage of tablespace to store auto indexes.

Following are some of the reports related to automatic indexing operations which you can generate using `REPORT_ACTIVITY` and `REPORT_LAST_ACTIVITY` functions of the `DBMS_AUTO_INDEX` package.

- Report of automatic indexing operations for a specific period.
- Report of the last automatic indexing operation.

For more information, see [Managing Indexes](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/managing-indexes.html#GUID-E4149397-FF37-4367-A12F-675433715904 "https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/managing-indexes.html#GUID-E4149397-FF37-4367-A12F-675433715904") in the _Oracle documentation_.

## MySQL usage

Currently, Amazon Aurora MySQL doesn’t provide a comparable alternative for automatic indexing. The most reasonable option would be to run a scheduled set of queries to estimate if additional indexes are
needed.

The following queries can help determine that.

Find user-tables without primary keys.

```
SELECT tab.table_schema,tab.table_name
FROM information_schema.tables tab
LEFT JOIN information_schema.table_constraints tco
  ON tab.table_schema = tco.table_schema
  AND tab.table_name = tco.table_name
  AND tco.constraint_type = 'PRIMARY KEY'
WHERE tco.constraint_type is null
  AND tab.table_schema not in('information_schema', 'performance_schema', 'sys')
  AND tab.table_type = 'BASE TABLE'
ORDER BY tab.table_schema, tab.table_name;
```

Unused indexes that can probably be dropped.

```
SELECT * FROM sys.schema_unused_indexes;
```

All of these should not be implemented in a script to decide if indexes should be created or dropped in a production environment. The Oracle Automatic Indexes will first assess if a new index is needed and if so, it will create an invisible index and only after ensuring nothing is harmed, then the index will become visible. You can’t use this process in MySQL to avoid any production performance issues.
