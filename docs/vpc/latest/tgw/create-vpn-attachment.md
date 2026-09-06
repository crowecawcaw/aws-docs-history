

# Create a transit gateway attachment to a VPN in AWS Transit Gateway
<a name="create-vpn-attachment"></a>

**To create a VPN attachment using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Attachments**.

1. Choose **Create transit gateway attachment**.

1. For **Transit gateway ID**, choose the transit gateway for the attachment. You can choose a transit gateway that you own.

1. For **Attachment type**, choose **VPN**.

1. For **Customer Gateway**, do one of the following:
   + To use an existing customer gateway, choose **Existing**, and then select the gateway to use.

     If your customer gateway is behind a network address translation (NAT) device that's enabled for NAT traversal (NAT-T), use the public IP address of your NAT device, and adjust your firewall rules to unblock UDP port 4500.
   + To create a customer gateway, choose **New**, then for **IP Address**, type a static public IP address and **BGP ASN**.

     For **Routing options**, choose whether to use **Dynamic** or **Static**. For more information, see [Site-to-Site VPN Routing Options](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNRoutingTypes.html) in the *AWS Site-to-Site VPN User Guide*.

1. For **Tunnel Options**, enter the CIDR ranges and pre-shared keys for your tunnel. For more information, see [Site-to-Site VPN architectures](https://docs.aws.amazon.com/vpn/latest/s2svpn/site-site-architectures.html).

1. Choose **Create transit gateway attachment**.

**To create a VPN attachment using the AWS CLI**  
Use the [create-vpn-connection](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpn-connection.html) command.