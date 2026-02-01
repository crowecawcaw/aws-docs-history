# Removing the EFS_INTEGRATION option

The steps for removing the `EFS_INTEGRATION` option depend on whether you're
removing the option from multiple DB instances or a single instance.

| Number of DB instances | Action                                                                                                                                                                                                    | Related information                                                                                                                                                                              |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Multiple               | Remove the `EFS_INTEGRATION` option from the option group to<br>which the DB instances belong. This change affects all instances that use the<br>option group.                                            | [Removing an option from an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption") |
| Single                 | Modify the DB instance and specify a different option group that doesn't<br>include the `EFS_INTEGRATION` option. You can specify the default<br>(empty) option group or a different custom option group. | [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md")                                                                                                           |

After you remove the `EFS_INTEGRATION` option, you can optionally delete the
EFS file system that was connected to your DB instances.
