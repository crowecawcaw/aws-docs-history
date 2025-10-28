# Delete a subnet

If you no longer need a subnet, you can delete it. You cannot delete a subnet if it contains any network interfaces. For example, you must terminate any instances in a subnet before you can delete it.

When you delete a subnet, the CIDR block associated with that subnet is returned to the VPC's available IP address pool. This means that the IP addresses within the subnet's CIDR range can be reallocated to other subnets or resources within the same VPC.

It's important to note that deleting a subnet does not automatically delete the resources within it. You must first terminate any EC2 instances, delete any network interfaces, and remove any other resources associated with the subnet before you can proceed with the subnet deletion.

###### To delete a subnet using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Terminate all instances in the subnet. For more information, see [Terminate your
   instance](../../../AWSEC2/latest/UserGuide/terminating-instances.md "../../../AWSEC2/latest/UserGuide/terminating-instances.md") in the _Amazon EC2 User Guide_.
3. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
4. In the navigation pane, choose **Subnets**.
5. Select the subnet and choose **Actions**, **Delete
   subnet**.
6. When prompted for confirmation, type `delete` and then
   choose **Delete**.

###### To delete a subnet using the AWS CLI

Use the [delete-subnet](../../../cli/latest/reference/ec2/delete-subnet.md "../../../cli/latest/reference/ec2/delete-subnet.md")
command.
