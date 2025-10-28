# Delete a security group

When you are finished with a security group that you created, you can delete it.

###### Requirements

- The security group can't be associated with any resources.
- The security group can't be referenced by a rule in another
  security group.
- The security group can't be the default security group for a VPC.

###### To delete a security group using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Security groups**.
3. Select the security group and choose **Actions**,
   **Delete security groups**.
4. If you selected more than one security group, you are prompted for
   confirmation. If some of the security groups can't be deleted, we display
   the status of each security group, which indicates whether it will be
   deleted. To confirm deletion, enter **Delete**.
5. Choose **Delete**.

###### To delete a security group using the AWS CLI

Use the [delete-security-group](../../../cli/latest/reference/ec2/delete-security-group.md "../../../cli/latest/reference/ec2/delete-security-group.md") command.
