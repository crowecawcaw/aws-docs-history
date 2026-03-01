# Turning off Babelfish

When you no longer need Babelfish, you can turn off Babelfish
functionality.

Be aware of some considerations:

- In some cases, you might turn off Babelfish before completing a
  migration to Aurora PostgreSQL. If you do and your DDL depends on SQL Server data
  types or you use any T-SQL functionality in your code, your code fails.
- If after provisioning a Babelfish instance you turn off the
  Babelfish extension, you can't provision that same database again on the
  same cluster.
  To turn off Babelfish, modify your parameter group, setting
  `rds.babelfish_status` to `OFF`. You can continue to use your
  SQL Server data types with Babelfish off, by setting
  `rds.babelfish_status` to `datatypesonly`.

If you turn off Babelfish in parameter group, all clusters that use that
parameter group lose Babelfish functionality.

For more information about modifying parameter groups, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
For information about Babelfish–specific parameters, see [DB cluster parameter group settings for Babelfish](babelfish-configuration.md "babelfish-configuration.md").
