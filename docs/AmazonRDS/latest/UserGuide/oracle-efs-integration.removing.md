

# Removing the EFS\_INTEGRATION option
<a name="oracle-efs-integration.removing"></a>

The steps for removing the `EFS_INTEGRATION` option depend on whether you're removing the option from multiple DB instances or a single instance.


| Number of DB instances | Action | Related information | 
| --- | --- | --- | 
| Multiple | Remove the EFS\_INTEGRATION option from the option group to which the DB instances belong. This change affects all instances that use the option group. | [Removing an option from an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption) | 
| Single | Modify the DB instance and specify a different option group that doesn't include the EFS\_INTEGRATION option. You can specify the default (empty) option group or a different custom option group. | [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md) | 

After you remove the `EFS_INTEGRATION` option, you can optionally delete the EFS file system that was connected to your DB instances.