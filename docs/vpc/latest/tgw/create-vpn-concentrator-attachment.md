# Create a VPN Concentrator attachment in AWS Transit Gateway

**Prerequisites**

- You must have an existing transit gateway in your account.

###### To create a VPN Concentrator attachment using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Site-to-Site VPN Concentrators**.
3. Choose **Create Site-to-Site VPN Concentrator**.
4. (Optional) For **Name tag**, enter a name for your Site-to-Site VPN Concentrator.
5. For **Transit gateway**, select an existing transit gateway.
6. (Optional) To add additional tags, choose **Add new tag** and specify the key and value for each tag.
7. Choose **Create Site-to-Site VPN Concentrator**.
   After you create the VPN Concentrator attachment, it appears in the list of attachments with a resource type of **VPN Concentrator** and an initial state of **Pending**. When the attachment is ready, the state changes to **Available**. You can then create Site-to-Site VPN connections on this Concentrator.

###### To create a VPN Concentrator attachment using the AWS CLI

Use the [create-vpn-concentrator](../../../cli/latest/reference/ec2/create-vpn-concentrator.md "../../../cli/latest/reference/ec2/create-vpn-concentrator.md") command.

###### To create a VPN connection on a VPN Concentrator using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Site-to-Site VPN Connections**.
3. Choose **Create VPN connection**.
4. For **Target Gateway Type**, choose **Site-to-Site VPN Concentrator**.
5. For **Site-to-Site VPN Concentrator**, choose the VPN Concentrator where you want to create the VPN connection.
6. For **Customer Gateway**, do one of the following:
   - To use an existing customer gateway, choose **Existing**, and then select the gateway to use. Ensure that the customer gateway supports BGP routing.
   - To create a customer gateway, choose **New**. For **IP Address**, enter the static public IP address for your customer gateway device. For **BGP ASN**, enter the Border Gateway Protocol (BGP) Autonomous System Number (ASN) for your customer gateway.

   If your customer gateway is behind a network address translation (NAT) device that's enabled for NAT traversal (NAT-T), use the public IP address of your NAT device, and adjust your firewall rules to unblock UDP port 4500.

7. For **Routing options**, **Dynamic (requires BGP)** is automatically selected. VPN Concentrator only supports dynamic routing with BGP.
8. For **Pre-shared key storage**, select either **Standard** or **Secrets Manager**.
9. For **Tunnel bandwidth**, **Standard** is automatically selected. VPN Concentrator only supports standard tunnel bandwidth.
10. For **Tunnel inside IP version**, select either **IPv4** or **IPv6**.
11. (Optional) Select **Enable acceleration** to improve performance of VPN tunnels.
12. (Optional) For **Local IPv4 network CIDR**, provide an IPv4 CIDR range.
13. (Optional) For **Remote IPv4 network CIDR**, provide an IPv4 CIDR range.
14. For **Outside IP Address Type**, you can select either **Public IPv4** or **IPv6** address.
15. (Optional) For **Tunnel Options**, you can configure tunnel settings such as inside tunnel IP addresses and pre-shared keys. For more information, see [Site-to-Site VPN architectures](../../../vpn/latest/s2svpn/site-site-architectures.md "../../../vpn/latest/s2svpn/site-site-architectures.md") in the _AWS Site-to-Site VPN User Guide_.
16. (Optional) To add additional tags, choose **Add new tag** and specify the key and value for each tag.
17. Choose **Create VPN connection**.
    The VPN connection appears in the list of VPN connections with the VPN Concentrator ID in the **Transit Gateway ID** column and an initial state of **Pending**. When the VPN connection is ready, the state changes to **Available**.

###### To create a VPN connection on a VPN Concentrator using the AWS CLI

Use the [create-vpn-connection](../../../cli/latest/reference/ec2/create-vpn-connection.md "../../../cli/latest/reference/ec2/create-vpn-connection.md") command and specify the VPN Concentrator ID using the `--vpn-concentrator-id` parameter.
