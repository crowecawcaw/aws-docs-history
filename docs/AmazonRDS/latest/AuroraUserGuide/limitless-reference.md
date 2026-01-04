# Variables in Aurora PostgreSQL Limitless Database

You can use the following variables to configure Aurora PostgreSQL Limitless Database.

**rds_aurora.limitless_active_shard_key**

Sets a single shard key while querying the database, causing all `SELECT` and DML queries to be appended with the shard key
as a constant predicate. For more information, see [Setting an active shard key](limitless-query.md#limitless-query.single-shard.active "limitless-query.md#limitless-query.single-shard.active").

**rds_aurora.limitless_create_table_collocate_with**

Set this variable to a specific table name to collocate newly created tables with that table. For more information, see [Creating limitless tables by using variables](limitless-creating-config.md "limitless-creating-config.md").

**rds_aurora.limitless_create_table_mode**

Sets the table creation mode. For more information, see [Creating limitless tables by using variables](limitless-creating-config.md "limitless-creating-config.md").

**rds_aurora.limitless_create_table_shard_key**

Set this variable to an array of column names to use as shard keys. For more information, see [Creating limitless tables by using variables](limitless-creating-config.md "limitless-creating-config.md").

**rds_aurora.limitless_explain_options**

What to include in the `EXPLAIN` output. For more information, see [EXPLAIN](limitless-reference.md#limitless-reference.DML-limitations.EXPLAIN "limitless-reference.md#limitless-reference.DML-limitations.EXPLAIN").
