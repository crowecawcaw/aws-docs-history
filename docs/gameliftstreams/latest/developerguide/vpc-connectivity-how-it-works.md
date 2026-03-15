# How VPC connectivity works

AWS Transit Gateway is a network transit hub that you can use to interconnect your
virtual private clouds (VPCs) and on-premises networks. A transit gateway acts as a
Regional virtual router for traffic flowing between VPCs and other connected networks.
For more information about transit gateways, see [What is a transit gateway?](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md")
in the _Amazon VPC Transit Gateway Guide_.

When you create a stream group location with VPC connectivity enabled, Amazon GameLift Streams performs the
following actions:

1. Creates a transit gateway in your streaming location (or reuses an existing one if you have other
   stream groups connected to the same VPC).
2. Shares the transit gateway with your AWS account using AWS Resource Access Manager (RAM).
3. Attaches the Amazon GameLift Streams service-managed VPC for your stream group to the transit gateway.
4. Configures routing in the Amazon GameLift Streams service-managed VPC to direct traffic destined for your CIDR
   blocks through the transit gateway.
   After the stream group location is active, you can complete the setup by performing the following
   steps for each stream group location with VPC connectivity configured. For detailed instructions,
   see [Configuring VPC connectivity](vpc-connectivity-configure.md "vpc-connectivity-configure.md").

5. **Accepting the RAM resource share invitation** – Grants your
   account access to the transit gateway. If you have already accepted a resource share invitation
   for another stream group that uses the same VPC, you don't need to accept it again.

###### Note

The resource share invitation expires after 7 days. If the invitation expires before you
accept it, you must delete and recreate the stream group or stream group location to generate
a new invitation. 2. **Creating a VPC attachment** – Connects your VPC to the shared
transit gateway. Only the VPC that matches the CreateStreamGroup request is allowed to attach
to the transit gateway. 3. **Adding routes in your VPC route tables** – Directs traffic
destined for the Amazon GameLift Streams service-managed VPC through the transit gateway. 4. **(Optional) Updating security groups** – Allows inbound traffic
from the Amazon GameLift Streams service-managed VPC CIDR block to reach your private resources.
