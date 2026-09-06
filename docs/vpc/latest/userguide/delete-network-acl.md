

# Delete a network ACL for your VPC
<a name="delete-network-acl"></a>

When you are finished with a network ACL, you can delete it. You can't delete a network ACL if there are subnets associated with it. You can't delete the default network ACL.

**To remove subnet associations from a network ACL using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Network ACLs**. The **Associated with** column indicates the number of subnets associated with each network ACL. This column is `-` if there are no associated subnets.

1. Select the network ACL.

1. Choose **Actions**, **Edit subnet associations**.

1. Remove the subnet associations.

1. Choose **Save changes**.

**To describe your network ACLs, including associations, using the command line**
+ [describe-network-acls](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-network-acls.html) (AWS CLI)
+ [Get-EC2NetworkAcl](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2NetworkAcl.html) (AWS Tools for Windows PowerShell)

**To replace a network ACL association using the command line**
+ [replace-network-acl-association](https://docs.aws.amazon.com/cli/latest/reference/ec2/replace-network-acl-association.html) (AWS CLI)
+ [Set-EC2NetworkAclAssociation](https://docs.aws.amazon.com/powershell/latest/reference/items/Set-EC2NetworkAclAssociation.html) (AWS Tools for Windows PowerShell)

**To delete a network ACL using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Network ACLs**.

1. Select the network ACL.

1. Choose **Actions**, **Delete network ACLs**.

1. When prompted for confirmation, enter **delete** and then choose **Delete**.

**To delete a network ACL using the command line**
+ [delete-network-acl](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-network-acl.html) (AWS CLI)
+ [Remove-EC2NetworkAcl](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2NetworkAcl.html) (AWS Tools for Windows PowerShell)