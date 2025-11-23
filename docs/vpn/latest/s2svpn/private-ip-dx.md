# Private IP AWS Site-to-Site VPN with Direct Connect

With private IP VPN, you can deploy IPsec VPN over Direct Connect, encrypting traffic between
your on-premises network and AWS, without the use of public IP addresses or additional
third-party VPN equipment.

One of the main use cases for private IP VPN over Direct Connect is helping customers in the
financial, healthcare, and federal industries meet regulatory and compliance goals. Private
IP VPN over Direct Connect ensures that traffic between AWS and on-premises networks is both
secure and private, allowing customers to comply with their regulatory and security
mandates.

## Benefits of private IP VPN

- **Simplified network management and operations:**
  Without private IP VPN, customers have to deploy third-party VPN and routers to
  implement private VPNs over Direct Connect networks. With private IP VPN capability,
  customers don’t have to deploy and manage their own VPN infrastructure. This
  leads to simplified network operations and reduced costs.
- **Improved security posture:** Previously,
  customers had to use a public Direct Connect virtual interface (VIF) for encrypting
  traffic over Direct Connect, which requires public IP addresses for VPN endpoints.
  Using public IPs increases the probability of external (DOS) attacks, which in
  turn compels customers to deploy additional security gear for network
  protection. Also, a public VIF opens access between all AWS public services
  and customer on-premises networks, increasing the severity of the risk.
  The
  private IP VPN feature allows encryption over Direct Connect transit VIFs (instead of
  public VIFs), coupled with the ability to configure private IPs. This provides
  end-to-end private connectivity in addition to encryption, improving the overall
  security posture.
- **Higher route scale:** Private IP VPN
  connections offer higher route limits (5000 outbound routes and 1000 inbound
  routes) as compared to Direct Connect alone, which currently has a limit of 200
  outbound and 100 inbound routes.

## How private IP VPN works

Private IP Site-to-Site VPN works over an Direct Connect transit virtual interface (VIF). It uses an
Direct Connect gateway and a transit gateway to interconnect your on-premises networks with
AWS VPCs. A private IP VPN connection has termination points at the transit gateway on
the AWS side, and at your customer gateway device on the on-premises side. You must
assign private IP addresses to both the transit gateway and the customer
gateway device ends of the IPsec tunnels. You can use private IP addresses from either RFC1918 or RFC6598 private IPv4 address ranges.

You attach a private IP VPN connection to a transit gateway. You then route traffic
between the VPN attachment and any VPCs (or other networks) that are also attached to
the transit gateway. You do that by associating a route table with the VPN attachment.
In the reverse direction, you can route traffic from your VPCs to the private IP VPN
attachment by using route tables that are associated with the VPCs.

The route table that's associated with the VPN attachment can be the same or different
from the one associated with the underlying Direct Connect attachment. This gives you the
ability to route both encrypted and unencrypted traffic simultaneously between your VPCs
and your on-premises networks.

For more details on the traffic path leaving the VPN, see [Private virtual interface and transit virtual interface routing policies](../../../directconnect/latest/UserGuide/routing-and-bgp.md#private-routing-policies "../../../directconnect/latest/UserGuide/routing-and-bgp.md#private-routing-policies")
in the _Direct Connect User Guide_.

## Prerequisites

The following table describes the perquisites before creating a private IP VPN over
Direct Connect.

| Item                                                         | Steps                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prepare the transit gateway for Site-to-Site VPN.            | Create the transit gateway by using the Amazon Virtual Private Cloud (VPC) console or<br>using the command-line or API.<br>See [Transit<br>gateways](../../../vpc/latest/tgw/tgw-transit-gateways.md "../../../vpc/latest/tgw/tgw-transit-gateways.md") in the _Amazon VPC Transit Gateways<br>Guide_.                                                                                                                                                     | A transit gateway is a network transit hub that you can use to<br>interconnect your VPCs and on-premises networks. You can create a new<br>transit gateway or use an existing one for the private IP VPN<br>connection. When you create the transit gateway, or modify an existing<br>transit gateway, you specify a private IP CIDR block for the connection.NoteWhen specifying the transit gateway CIDR block to be<br>associated with your Private IP VPN, ensure the CIDR block does<br>not overlap with any IP addresses for any other network<br>attachments on the transit gateway. If any IP CIDR blocks do<br>overlap, it may cause configuration issues with your customer<br>gateway device. |
| Create the Direct Connect gateway for Site-to-Site VPN.      | Create the Direct Connect gateway by using the Direct Connect<br>console or by using the command-line or API.<br>See [Create an AWS Direct Connect gateway](../../../directconnect/latest/UserGuide/create-direct-connect-gateway.md "../../../directconnect/latest/UserGuide/create-direct-connect-gateway.md") in the<br>_Direct Connect User Guide_.                                                                                                    | A Direct Connect gateway allows you to connect virtual interfaces<br>(VIFs) across multiple AWS Regions. This gateway is used to connect to<br>your VIF.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Create the transit gateway association for Site-to-Site VPN. | Create the association between the Direct Connect gateway and the<br>transit gateway by using the Direct Connect console or using the command-line<br>or API.<br>See [Associate or disassociate Direct Connect with a transit gateway](../../../directconnect/latest/UserGuide/associate-tgw-with-direct-connect-gateway.md "../../../directconnect/latest/UserGuide/associate-tgw-with-direct-connect-gateway.md") in the<br>_Direct Connect User Guide_. | After creating the Direct Connect gateway, create a transit gateway<br>association for the Direct Connect gateway. Specify the private IP CIDR<br>for the transit gateway that was identified earlier in the allowed<br>prefixes list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

###### Tasks

- [Create a private IP VPN over Direct
  Connect](private-ip-dx-steps.md "private-ip-dx-steps.md")
