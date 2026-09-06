

# Delete a VPC Lattice target group
<a name="delete-target-group"></a>

You can delete a target group if it is not referenced by the forward actions of any listener rules. Deleting a target group does not affect the targets registered with the target group. If you no longer need a registered EC2 instance, you can stop or terminate it.

**To delete a target group using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Target groups**.

1. Select the check box for the target group and then choose **Actions**, **Delete**.

1. When prompted for confirmation, enter **confirm** and then choose **Delete**.

**To delete a target group using the AWS CLI**  
Use the [delete-target-group](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/delete-target-group.html) command.