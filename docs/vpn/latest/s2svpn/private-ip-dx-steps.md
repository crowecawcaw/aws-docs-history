# Create a private IP AWS Site-to-Site VPN over AWS Direct Connect

To create a private IP VPN with AWS Direct Connect follow these steps. Before you create the private
IP VPN over Direct Connect, you need to ensure that a transit gateway and Direct Connect
gateway are first created. After creating the two gateways you then need to create an
assocation between the two. These prerequisites are described in the following table. Once
you've created and associated the two gateways, you'll create a VPN customer cateway and
connection using that association.

## Prerequisites

The following table describes the perquisites before creating a private IP VPN over
Direct Connect.

| Item                                                         | Steps                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prepare the transit gateway for Site-to-Site VPN.            | Create the transit gateway by using the Amazon Virtual Private Cloud (VPC) console or<br>using the command-line or API.<br>See [Transit<br>gateways](../../../vpc/latest/tgw/tgw-transit-gateways.md "../../../vpc/latest/tgw/tgw-transit-gateways.md") in the _Amazon VPC Transit Gateways<br>Guide_.                                                                                                                                                             | A transit gateway is a network transit hub that you can use to<br>interconnect your VPCs and on-premises networks. You can create a new<br>transit gateway or use an existing one for the private IP VPN<br>connection. When you create the transit gateway, or modify an existing<br>transit gateway, you specify a private IP CIDR block for the connection.NoteWhen specifying the transit gateway CIDR block to be<br>associated with your Private IP VPN, ensure the CIDR block does<br>not overlap with any IP addresses for any other network<br>attachments on the transit gateway. If any IP CIDR blocks do<br>overlap, it may cause configuration issues with your customer<br>gateway device. |
| Create the AWS Direct Connect gateway for Site-to-Site VPN.  | Create the Direct Connect gateway by using the Direct Connect<br>console or by using the command-line or API.<br>See [Create an AWS Direct Connect gateway](../../../directconnect/latest/UserGuide/create-direct-connect-gateway.md "../../../directconnect/latest/UserGuide/create-direct-connect-gateway.md") in the<br>_AWS Direct Connect User Guide_.                                                                                                        | A Direct Connect gateway allows you to connect virtual interfaces<br>(VIFs) across multiple AWS Regions. This gateway is used to connect to<br>your VIF.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Create the transit gateway association for Site-to-Site VPN. | Create the association between the Direct Connect gateway and the<br>transit gateway by using the Direct Connect console or using the command-line<br>or API.<br>See [Associate or disassociate AWS Direct Connect with a transit gateway](../../../directconnect/latest/UserGuide/associate-tgw-with-direct-connect-gateway.md "../../../directconnect/latest/UserGuide/associate-tgw-with-direct-connect-gateway.md") in the<br>_AWS Direct Connect User Guide_. | After creating the AWS Direct Connect gateway, create a transit gateway<br>association for the AWS Direct Connect gateway. Specify the private IP CIDR<br>for the transit gateway that was identified earlier in the allowed<br>prefixes list.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## Create the customer gateway and connection for

Site-to-Site VPN

A customer gateway is a resource that you create in AWS. It represents the customer
gateway device in your on-premises network. When you create a customer gateway, you
provide information about your device to AWS. For more details, see [Customer gateway](how_it_works.md#CustomerGateway "how_it_works.md#CustomerGateway").

###### To create a customer gateway using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Customer gateways**.
3. Choose **Create customer gateway**.
4. (Optional) For **Name tag**, enter a name for your customer
   gateway. Doing so creates a tag with a key of `Name` and the value
   that you specify.
5. For **BGP ASN**, enter a Border Gateway Protocol (BGP)
   Autonomous System Number (ASN) for your customer gateway.
6. For **IP address**, enter the private IP address for your
   customer gateway device.

###### Important

When configuring AWS Private IP AWS Site-to-Site VPN, you must specify your own
tunnel endpoint IP addresses using RFC 1918 addresses. Do not use the point-to-point
IP addresses for the eBGP peering between your
customer gateway router and the AWS Direct Connect endpoint. AWS recommends
using a loopback or LAN interface on your customer gateway router as the
source or destination address instead of point-to-point
connections.

For more information about RFC 1918, see [Address Allocation for Private Internets](https://datatracker.ietf.org/doc/html/rfc1918 "https://datatracker.ietf.org/doc/html/rfc1918"). 7. (Optional) For **Device**, enter a name for the device that
hosts this customer gateway. 8. Choose **Create customer gateway**. 9. In the navigation pane, choose **Site-to-Site VPN connections**. 10. Choose **Create VPN connection**. 11. (Optional) For **Name tag**, enter a name for your Site-to-Site VPN
connection. Doing so creates a tag with a key of `Name` and the value
that you specify. 12. For **Target gateway type**, choose **Transit
gateway**. Then, choose the transit gateway that you identified
earlier. 13. For **Customer gateway**, select
**Existing**. Then, choose the customer gateway that you
created earlier. 14. Select one of the routing options based on whether your customer gateway
device supports Border Gateway Protocol (BGP):

    * If your customer gateway device supports BGP, choose **Dynamic
     (requires BGP)**.
    * If your customer gateway device does not support BGP, choose
     **Static**.

15. For **Tunnel inside IP version**, specify whether the VPN
    tunnels support IPv4 or IPv6 traffic.
16. (Optional) If you specified **IPv4** for **Tunnel
    inside IP Version**, you can optionally specify the IPv4 CIDR
    ranges for the customer gateway and AWS sides that are allowed to communicate
    over the VPN tunnels. The default is `0.0.0.0/0`.

If you specified **IPv6** for **Tunnel inside IP
version**, you can optionally specify the IPv6 CIDR ranges for the
customer gateway and AWS sides that are allowed to communicate over the VPN
tunnels. The default for both ranges is `::/0`. 17. For **Outside IP address type**, choose
**PrivateIpv4**. 18. For **Transport attachment ID**, choose the transit gateway
attachment for the appropriate AWS Direct Connect gateway. 19. Choose **Create VPN connection**.

###### Note

The **Enable acceleration** option is not applicable for VPN
connections over AWS Direct Connect.

###### To create a customer gateway using the command line or API

- [CreateCustomerGateway](../../../AWSEC2/latest/APIReference/API_CreateCustomerGateway.md "../../../AWSEC2/latest/APIReference/API_CreateCustomerGateway.md") (Amazon EC2 Query API)
- [create-customer-gateway](../../../cli/latest/reference/ec2/create-customer-gateway.md "../../../cli/latest/reference/ec2/create-customer-gateway.md") (AWS CLI)
