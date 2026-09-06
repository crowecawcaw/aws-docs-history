

# Delete a placement group
<a name="delete-placement-group"></a>

If you need to replace a placement group or no longer need one, you can delete it. Before you can delete a placement group, it must contain no instances. You can terminate the instances, move them to another placement group, or remove them from the placement group.

You can't delete a placement group that is a parent of a cluster placement group. Delete the cluster placement groups first.

------
#### [ Console ]

**To delete a placement group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Placement Groups**.

1. Select the placement group and choose **Actions**, **Delete**.

1. When prompted for confirmation, enter **Delete** and then choose **Delete**.

------
#### [ AWS CLI ]

**To delete a placement group**  
Use the [delete-placement-group](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-placement-group.html) command.

```
aws ec2 delete-placement-group --group-name {{my-cluster}}
```

------
#### [ PowerShell ]

**To delete a placement group**  
Use the [Remove-EC2PlacementGroup](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2PlacementGroup.html) cmdlet.

```
Remove-EC2PlacementGroup -GroupName {{my-cluster}}
```

------