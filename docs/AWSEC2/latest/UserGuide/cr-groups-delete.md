# Delete a group

If you no longer need your group, you can delete it at any time. When you
delete a group with running instances and active Capacity Reservations, instances that target
the group continue running in their current Capacity Reservation after the group deletion.
Amazon EC2 restores the capacity to the Capacity Reservation when you terminate the instances.

Console

###### To delete a group

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Capacity
   Reservations**.
3. Choose **Capacity Reservation
   Resource Group**.
4. Select the group you want to delete, choose
   **Action**, then choose
   **Delete**.
5. When prompted to confirm, choose
   **Delete**.

AWS CLI

###### To delete a group

Use the [delete-group](../../../cli/latest/reference/resource-groups/delete-group.md "../../../cli/latest/reference/resource-groups/delete-group.md") command.

```
aws resource-groups delete-group --group `MyCRGroup`
```

PowerShell

###### To delete a group

Use the [Remove-RGGroup](../../../powershell/latest/reference/items/Remove-RGGroup.md "../../../powershell/latest/reference/items/Remove-RGGroup.md") cmdlet.

```
Remove-RGGroup -GroupName `MyCRGroup`
```
