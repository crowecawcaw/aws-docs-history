# Removing the NATIVE_NETWORK_ENCRYPTION option

You can remove NNE from a DB instance.

To remove the `NATIVE_NETWORK_ENCRYPTION` option from a DB instance, do one of
the following:

- To remove the option from multiple DB instances, remove the
  `NATIVE_NETWORK_ENCRYPTION` option from the option group they
  belong to. This change affects all DB instances that use the option group. After you
  remove the `NATIVE_NETWORK_ENCRYPTION` option, you don't need to
  restart your DB instances. For more information, see [Removing an option from an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption").
- To remove the option from a single DB instance, modify the DB instance and specify a
  different option group that doesn't include the
  `NATIVE_NETWORK_ENCRYPTION` option. You can specify the default
  (empty) option group, or a different custom option group. After you remove the
  `NATIVE_NETWORK_ENCRYPTION` option, you don't need to restart
  your DB instance. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
