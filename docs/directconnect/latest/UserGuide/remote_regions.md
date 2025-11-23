# Access to remote Direct Connect Regions

Direct Connect locations in public Regions or AWS GovCloud (US) can access public services in any other
public Region (excluding China (Beijing and Ningxia)). In addition, Direct Connect connections in
public Regions or AWS GovCloud (US) can be configured to access a VPC in your account in any
other public Region (excluding China (Beijing and Ningxia). You can therefore use a single
Direct Connect connection to build multi-Region services. All networking traffic remains on the
AWS global network backbone, regardless of whether you access public AWS services or a
VPC in another Region.

Any data transfer out of a remote Region is billed at the remote Region data transfer
rate. For more information about data transfer pricing, see the [Pricing](http://aws.amazon.com/directconnect/pricing/ "http://aws.amazon.com/directconnect/pricing/") section on the AWS
Direct Connect detail page.

For more information about the routing policies and supported BGP communities for an
Direct Connect connection, see [Routing policies and BGP communities](routing-and-bgp.md "routing-and-bgp.md").

## Access to public services in a remote Region

To access public resources in a remote Region, you must set up a public virtual interface and
establish a Border Gateway Protocol (BGP) session. For more information, see [Virtual interfaces and hosted virtual interfaces](WorkingWithVirtualInterfaces.md "WorkingWithVirtualInterfaces.md").

After you have created a public virtual interface and established a BGP session to it, your
router learns the routes of the other public AWS Regions. For more information about
prefixes currently advertised by AWS, see [AWS IP Address Ranges](../../../general/latest/gr/aws-ip-ranges.md "../../../general/latest/gr/aws-ip-ranges.md") in the _Amazon Web Services General Reference_.

## Access to VPCs in a remote Region

You can create a _Direct Connect gateway_ in any public Region. Use
it to connect your Direct Connect connection over a private virtual interface to VPCs in your
account that are located in different Regions or to a transit gateway. For more
information, see [Direct Connect gateways](direct-connect-gateways.md "direct-connect-gateways.md").

Alternatively, you can create a public virtual interface for your Direct Connect connection
and then establish a VPN connection to your VPC in the remote Region. For more
information about configuring VPN connectivity to a VPC, see [Scenarios for Using Amazon Virtual Private Cloud](../../../vpc/latest/userguide/VPC_Scenarios.md "../../../vpc/latest/userguide/VPC_Scenarios.md") in the
_Amazon VPC User Guide_.

## Network-to-Amazon VPC Connectivity Options

The following configuration can be used to connect remote networks with your Amazon
VPC environment. These options are useful for integrating AWS resources with your
existing on-site services:

- [Amazon Virtual Private Cloud Connectivity Options](../../../whitepapers/latest/aws-vpc-connectivity-options/welcome.md "../../../whitepapers/latest/aws-vpc-connectivity-options/welcome.md")
