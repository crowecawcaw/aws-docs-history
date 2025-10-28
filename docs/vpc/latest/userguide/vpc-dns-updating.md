# View and update DNS attributes for your VPC

You can view and update the DNS support attributes for your VPC using the Amazon VPC console. These settings control whether your
instances get public DNS hostnames and whether the Amazon DNS server can resolve your private
DNS names. Configuring these attributes correctly is vital for ensuring seamless communication
within your VPC.

###### To describe and update DNS support for a VPC using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Your VPCs**.
3. Select the checkbox for the VPC.
4. Review the information in **Details**. In this example, both
   **DNS hostnames** and **DNS resolution** are
   enabled.

![The DNS Settings tab](images/dns-settings.png) 5. To update these settings, choose **Actions** and then choose
**Edit VPC settings**. Select or clear **Enable** on
the appropriate DNS attribute and choose **Save changes**.

###### To describe DNS support for a VPC using the command line

- [describe-vpc-attribute](../../../cli/latest/reference/ec2/describe-vpc-attribute.md "../../../cli/latest/reference/ec2/describe-vpc-attribute.md") (AWS CLI)
- [Get-EC2VpcAttribute](../../../powershell/latest/reference/items/Get-EC2VpcAttribute.md "../../../powershell/latest/reference/items/Get-EC2VpcAttribute.md") (AWS Tools for Windows PowerShell)

###### To update DNS support for a VPC using the command line

- [modify-vpc-attribute](../../../cli/latest/reference/ec2/modify-vpc-attribute.md "../../../cli/latest/reference/ec2/modify-vpc-attribute.md") (AWS CLI)
- [Edit-EC2VpcAttribute](../../../powershell/latest/reference/items/Edit-EC2VpcAttribute.md "../../../powershell/latest/reference/items/Edit-EC2VpcAttribute.md") (AWS Tools for Windows PowerShell)
