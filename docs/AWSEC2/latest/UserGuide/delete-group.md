# Delete a Capacity Reservation group

You can use the following examples to delete a Capacity Reservation group.

AWS CLI

###### To delete a group

Use the [delete-group](../../../cli/latest/reference/resource-groups/delete-group.md "../../../cli/latest/reference/resource-groups/delete-group.md") command.

```
aws resource-groups delete-group --group `MyCRGroup`
```

PowerShell

###### To delete a group

Use the [Remove-RGGroup](../../../powershell/latest/reference/items/Remove-RGGroup.md "../../../powershell/latest/reference/items/Remove-RGGroup.md")
cmdlet.

```
Remove-RGGroup -GroupName `MyCRGroup`
```
