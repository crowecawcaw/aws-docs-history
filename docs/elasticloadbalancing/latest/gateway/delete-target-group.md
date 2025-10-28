# Delete a target group for your Gateway Load Balancer

You can delete a target group if it is not referenced by the forward actions of any
listener rules. Deleting a target group does not affect the targets registered with the
target group. If you no longer need a registered EC2 instance, you can stop or terminate
it.

###### To delete a target group using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Select the target group and choose **Actions**,
   **Delete**.
4. When prompted for confirmation, choose **Yes,
   delete**.

###### To delete a target group using the AWS CLI

Use the [delete-target-group](../../../cli/latest/reference/elbv2/delete-target-group.md "../../../cli/latest/reference/elbv2/delete-target-group.md") command.
