# Delete an internet gateway

If you no longer need internet access for a VPC, you can detach the internet gateway
from the VPC and then delete it. You can't delete an internet gateway if it's still
attached to a VPC. You can't detach an internet gateway if the VPC has
resources with associated public IP addresses or Elastic IP addresses.

###### To detach an internet gateway from a VPC using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Internet gateways**.
3. Select the check box for the internet gateway.
4. To attach it, choose **Actions**, Attach to VPC, select an available VPC, and choose **Attach internet gateway**.
5. To detach it, choose **Actions**, **Detach from VPC** and choose **Detach internet gateway**. When prompted for confirmation, choose **Detach internet gateway**.

###### To describe your internet gateways, including attachments, using the command line

- [describe-internet-gateways](../../../cli/latest/reference/ec2/describe-internet-gateways.md "../../../cli/latest/reference/ec2/describe-internet-gateways.md") (AWS CLI)
- [Get-EC2InternetGateway](../../../powershell/latest/reference/items/Get-EC2InternetGateway.md "../../../powershell/latest/reference/items/Get-EC2InternetGateway.md") (AWS Tools for Windows PowerShell)

###### To detach an internet gateway from a VPC using the command line

- [detach-internet-gateway](../../../cli/latest/reference/ec2/detach-internet-gateway.md "../../../cli/latest/reference/ec2/detach-internet-gateway.md") (AWS CLI)
- [Dismount-EC2InternetGateway](../../../powershell/latest/reference/items/Dismount-EC2InternetGateway.md "../../../powershell/latest/reference/items/Dismount-EC2InternetGateway.md") (AWS Tools for Windows PowerShell)

###### To delete an internet gateway using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Internet gateways**.
3. Select the check box for the internet gateway.
4. Choose **Actions**, **Delete internet gateway**.
5. When prompted for confirmation, enter `delete`, and then choose
   **Delete internet gateway**.

###### To delete an internet gateway using the command line

- [delete-internet-gateway](../../../cli/latest/reference/ec2/delete-internet-gateway.md "../../../cli/latest/reference/ec2/delete-internet-gateway.md") (AWS CLI)
- [Remove-EC2InternetGateway](../../../powershell/latest/reference/items/Remove-EC2InternetGateway.md "../../../powershell/latest/reference/items/Remove-EC2InternetGateway.md") (AWS Tools for Windows PowerShell)
