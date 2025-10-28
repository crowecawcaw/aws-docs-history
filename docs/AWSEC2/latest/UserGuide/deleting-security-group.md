# Delete an Amazon EC2 security group

When you are finished with a security group that you created for use with your
Amazon EC2 instances, you can delete it.

###### Requirements

- The security group can't be associated with an instance or network
  interface.
- The security group can't be referenced by a rule in another
  security group.

Console

###### To delete a security group

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. (Optional) To verify that your security group is not associated with an
   instance, do the following:
   1. In the navigation pane, choose **Security Groups**.
   2. Copy the ID of the security group to delete.
   3. In the navigation pane, choose **Instances**.
   4. In the search bar, add **Security group IDs equals**
      filter and paste the ID of the security group. If there are no results,
      then the security group is not associated with an instance. Otherwise,
      you must disassociate the security group before you can delete it.

3. In the navigation pane, choose **Security Groups**.
4. Select the security group and choose **Actions**, **Delete
   security groups**.
5. If you selected more than one security group, you are prompted for
   confirmation. If some of the security groups can't be deleted, we display
   the status of each security group, which indicates whether it will be
   deleted. To confirm deletion, enter **Delete**.
6. Choose **Delete**.

AWS CLI

###### To delete a security group

Use the following [delete-security-group](../../../cli/latest/reference/ec2/delete-security-group.md "../../../cli/latest/reference/ec2/delete-security-group.md")
command.

```
aws ec2 delete-security-group --group-id `sg-1234567890abcdef0`
```

PowerShell

###### To delete a security group

Use the [Remove-EC2SecurityGroup](../../../powershell/latest/reference/items/Remove-EC2SecurityGroup.md "../../../powershell/latest/reference/items/Remove-EC2SecurityGroup.md")
cmdlet.

```
Remove-EC2SecurityGroup -GroupId `sg-1234567890abcdef0`
```
