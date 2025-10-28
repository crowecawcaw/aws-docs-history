# Delete a placement group

If you need to replace a placement group or no longer need one, you can delete it.
Before you can delete a placement group, it must contain no instances. You can
terminate the instances, move them to another placement group, or remove them
from the placement group.

Console

###### To delete a placement group

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Placement
   Groups**.
3. Select the placement group and choose
   **Actions**,
   **Delete**.
4. When prompted for confirmation, enter
   `Delete` and then choose
   **Delete**.

AWS CLI

###### To delete a placement group

Use the [delete-placement-group](../../../cli/latest/reference/ec2/delete-placement-group.md "../../../cli/latest/reference/ec2/delete-placement-group.md") command.

```
aws ec2 delete-placement-group --group-name `my-cluster`
```

PowerShell

###### To delete a placement group

Use the [Remove-EC2PlacementGroup](../../../powershell/latest/reference/items/Remove-EC2PlacementGroup.md "../../../powershell/latest/reference/items/Remove-EC2PlacementGroup.md") cmdlet.

```
Remove-EC2PlacementGroup -GroupName `my-cluster`
```
