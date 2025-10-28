# Delete a network interface

Deleting a network interface releases all attributes associated with the interface
and releases any private IP addresses or Elastic IP addresses to be used by another
instance.

You can't delete a network interface that is in use. First, you must [detach the network interface](network-interface-attachments.md#detach_eni "network-interface-attachments.md#detach_eni").

Console

###### To delete a network interface

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Network
   Interfaces**.
3. Select the checkbox for the network interface, and then choose
   **Actions**, **Delete**.
4. When prompted for confirmation, choose **Delete**.

AWS CLI

###### To delete a network interface

Use the following [delete-network-interface](../../../cli/latest/reference/ec2/delete-network-interface.md "../../../cli/latest/reference/ec2/delete-network-interface.md")
command.

```
aws ec2 delete-network-interface --network-interface-id `eni-1234567890abcdef0`
```

PowerShell

###### To delete a network interface

Use the [Remove-EC2NetworkInterface](../../../powershell/latest/reference/items/Remove-EC2NetworkInterface.md "../../../powershell/latest/reference/items/Remove-EC2NetworkInterface.md")
cmdlet.

```
Remove-EC2NetworkInterface -NetworkInterfaceId `eni-1234567890abcdef0`
```
