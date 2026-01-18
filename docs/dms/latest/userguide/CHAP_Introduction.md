# DDL statements supported by AWS DMS

You can execute data definition language (DDL) statements on the source database
during the data migration process. These statements are replicated to the target
database by the replication server.

Supported DDL statements include the following:

- Create table
- Drop table
- Rename table
- Truncate table
- Add column
- Drop column
- Rename column
- Change column data type
  DMS doesn’t capture all supported DDL statements for some source engine types. And DMS handles DDL
  statements differently when applying them to specific target engines. For information about which DDL
  statements are supported for a specific source, and how they’re applied to a target, see the specific
  documentation topic for that source and target endpoint.

You can use task settings to configure the way DMS handles DDL behavior during change data capture (CDC).
For more information, see
[Task
settings for change processing DDL handling](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md").

## Limitations and

considerations

Rapid sequences of DDL operations in the source database (such as DDL>DML>DDL) can
cause AWS DMS to parse the log incorrectly, leading to data loss or unexpected
behavior. To maintain data consistency, wait for AWS DMS to apply each change to the
target before performing subsequent operations.

For example, during change data capture (CDC), multiple rapid table rename
operations on a source table can trigger errors. If you rename a table and then
quickly rename it back to its original name, AWS DMS might report that the table
already exists in the target database.
