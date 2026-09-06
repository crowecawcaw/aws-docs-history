

# Create a Direct Connect virtual private gateway
<a name="create-virtual-private-gateway"></a>

The virtual private gateway must be attached to the VPC to which you want to connect. You can create a virtual private gateway and attach it to a VPC using either the Direct Connect console or using the command line or API.

**Note**  
If you are planning to use the virtual private gateway for a Direct Connect gateway and a dynamic VPN connection, set the ASN on the virtual private gateway to the value that you require for the VPN connection. Otherwise, the ASN on the virtual private gateway can be set to any permitted value. The Direct Connect gateway advertises all connected VPCs over the ASN assigned to it.

After you create a virtual private gateway, you must attach it to your VPC.

**To create a virtual private gateway and attach it to your VPC**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Private Gateways**, and then choose **Create Virtual Private Gateway**.

1. (Optional) Enter a name for your virtual private gateway. Doing so creates a tag with a key of `Name` and the value that you specify.

1. For **ASN**, leave the default selection to use the default Amazon ASN. Otherwise, choose **Custom ASN** and enter a value. For a 16-bit ASN, the value must be in the 64512 to 65534 range. For a 32-bit ASN, the value must be in the 4200000000 to 4294967294 range. 

1. Choose **Create Virtual Private Gateway**.

1. Select the virtual private gateway that you created, and then choose **Actions**, **Attach to VPC**.

1. Select your VPC from the list and choose **Yes, Attach**.

**To create a virtual private gateway using the command line or API**
+ [CreateVpnGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-CreateVpnGateway.html) (Amazon EC2 Query API)
+ [create-vpn-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpn-gateway.html) (AWS CLI)
+ [New-EC2VpnGateway](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2VpnGateway.html) (AWS Tools for Windows PowerShell)

**To attach a virtual private gateway to a VPC using the command line or API**
+ [AttachVpnGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-AttachVpnGateway.html) (Amazon EC2 Query API)
+ [attach-vpn-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/attach-vpn-gateway.html) (AWS CLI)
+ [Add-EC2VpnGateway](https://docs.aws.amazon.com/powershell/latest/reference/items/Add-EC2VpnGateway.html) (AWS Tools for Windows PowerShell)