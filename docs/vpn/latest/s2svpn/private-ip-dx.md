# Private IP AWS Site-to-Site VPN with AWS Direct Connect

With private IP VPN, you can deploy IPsec VPN over AWS Direct Connect, encrypting traffic between
your on-premises network and AWS, without the use of public IP addresses or additional
third-party VPN equipment.

One of the main use cases for private IP VPN over AWS Direct Connect is helping customers in the
financial, healthcare, and federal industries meet regulatory and compliance goals. Private
IP VPN over AWS Direct Connect ensures that traffic between AWS and on-premises networks is both
secure and private, allowing customers to comply with their regulatory and security
mandates.

## Benefits of private IP VPN

- **Simplified network management and operations:**
  Without private IP VPN, customers have to deploy third-party VPN and routers to
  implement private VPNs over AWS Direct Connect networks. With private IP VPN capability,
  customers don’t have to deploy and manage their own VPN infrastructure. This
  leads to simplified network operations and reduced costs.
- **Improved security posture:** Previously,
  customers had to use a public AWS Direct Connect virtual interface (VIF) for encrypting
  traffic over AWS Direct Connect, which requires public IP addresses for VPN endpoints.
  Using public IPs increases the probability of external (DOS) attacks, which in
  turn compels customers to deploy additional security gear for network
  protection. Also, a public VIF opens access between all AWS public services
  and customer on-premises networks, increasing the severity of the risk.
  The
  private IP VPN feature allows encryption over AWS Direct Connect transit VIFs (instead of
  public VIFs), coupled with the ability to configure private IPs. This provides
  end-to-end private connectivity in addition to encryption, improving the overall
  security posture.
- **Higher route scale:** Private IP VPN
  connections offer higher route limits (5000 outbound routes and 1000 inbound
  routes) as compared to AWS Direct Connect alone, which currently has a limit of 200
  outbound and 100 inbound routes.

## How private IP VPN works

Private IP Site-to-Site VPN works over an AWS Direct Connect transit virtual interface (VIF). It uses an
AWS Direct Connect gateway and a transit gateway to interconnect your on-premises networks with
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
from the one associated with the underlying AWS Direct Connect attachment. This gives you the
ability to route both encrypted and unencrypted traffic simultaneously between your VPCs
and your on-premises networks.

For more details on the traffic path leaving the VPN, see [Private virtual interface and transit virtual interface routing policies](../../../directconnect/latest/UserGuide/routing-and-bgp.md#private-routing-policies "../../../directconnect/latest/UserGuide/routing-and-bgp.md#private-routing-policies")
in the _AWS Direct Connect User Guide_.

###### Tasks

- [Create a private IP VPN over Direct
  Connect](private-ip-dx-steps.md "private-ip-dx-steps.md")
