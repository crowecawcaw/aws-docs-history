# Create a transit gateway attachment to a VPN in AWS Transit Gateway

###### To create a VPN attachment using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway
   Attachments**.
3. Choose **Create transit gateway attachment**.
4. For **Transit gateway ID**, choose the transit gateway for the attachment. You
   can choose a transit gateway that you own.
5. For **Attachment type**, choose **VPN**.
6. For **Customer Gateway**, do one of the following:
   - To use an existing customer gateway, choose **Existing**, and
     then select the gateway to use.

   If your customer gateway is behind a network address translation (NAT) device
   that's enabled for NAT traversal (NAT-T), use the public IP address of your NAT
   device, and adjust your firewall rules to unblock UDP port 4500.
   - To create a customer gateway, choose **New**, then for
     **IP Address**, type a static public IP address and
     **BGP ASN**.

   For **Routing options**, choose whether to use
   **Dynamic** or **Static**. For
   more information, see [Site-to-Site VPN Routing Options](../../../vpn/latest/s2svpn/VPNRoutingTypes.md "../../../vpn/latest/s2svpn/VPNRoutingTypes.md") in the _AWS Site-to-Site VPN User Guide_.

7. For **Tunnel Options**, enter the CIDR ranges and pre-shared keys
   for your tunnel. For more information, see [Site-to-Site VPN architectures](../../../vpn/latest/s2svpn/site-site-architectures.md "../../../vpn/latest/s2svpn/site-site-architectures.md").
8. Choose **Create transit gateway attachment**.

###### To create a VPN attachment using the AWS CLI

Use the [create-vpn-connection](../../../cli/latest/reference/ec2/create-vpn-connection.md "../../../cli/latest/reference/ec2/create-vpn-connection.md") command.
