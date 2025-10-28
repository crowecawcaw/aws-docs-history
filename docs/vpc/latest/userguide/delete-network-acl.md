# Delete a network ACL for your VPC

When you are finished with a network ACL, you can delete it. You can't delete
a network ACL if there are subnets associated with it. You can't delete the default
network ACL.

###### To remove subnet associations from a network ACL using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Network ACLs**. The
   **Associated with** column indicates the number of subnets
   associated with each network ACL. This column is `-` if there are
   no associated subnets.
3. Select the network ACL.
4. Choose **Actions**, **Edit subnet associations**.
5. Remove the subnet associations.
6. Choose **Save changes**.

###### To describe your network ACLs, including associations, using the command line

- [describe-network-acls](../../../cli/latest/reference/ec2/describe-network-acls.md "../../../cli/latest/reference/ec2/describe-network-acls.md") (AWS CLI)
- [Get-EC2NetworkAcl](../../../powershell/latest/reference/items/Get-EC2NetworkAcl.md "../../../powershell/latest/reference/items/Get-EC2NetworkAcl.md") (AWS Tools for Windows PowerShell)

###### To replace a network ACL association using the command line

- [replace-network-acl-association](../../../cli/latest/reference/ec2/replace-network-acl-association.md "../../../cli/latest/reference/ec2/replace-network-acl-association.md") (AWS CLI)
- [Set-EC2NetworkAclAssociation](../../../powershell/latest/reference/items/Set-EC2NetworkAclAssociation.md "../../../powershell/latest/reference/items/Set-EC2NetworkAclAssociation.md") (AWS Tools for Windows PowerShell)

###### To delete a network ACL using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Network ACLs**.
3. Select the network ACL.
4. Choose **Actions**, **Delete network ACLs**.
5. When prompted for confirmation, enter `delete` and then choose
   **Delete**.

###### To delete a network ACL using the command line

- [delete-network-acl](../../../cli/latest/reference/ec2/delete-network-acl.md "../../../cli/latest/reference/ec2/delete-network-acl.md") (AWS CLI)
- [Remove-EC2NetworkAcl](../../../powershell/latest/reference/items/Remove-EC2NetworkAcl.md "../../../powershell/latest/reference/items/Remove-EC2NetworkAcl.md") (AWS Tools for Windows PowerShell)
