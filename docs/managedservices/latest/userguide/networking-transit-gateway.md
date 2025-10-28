# AWS Transit Gateway

AWS Transit Gateway (TGW) is a service that enables you to connect your Amazon
Virtual Private Clouds (VPCs) and your on-premises networks to a single gateway.
Transit gateway is the networking backbone that handles the routing between
AMS account networks and external networks. For information about Transit
Gateway, see [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/").

Provide the following input to create this resource:

- _Transit Gateway ASN number_\*: Provide the private
  Autonomous System Number (ASN) for your
  transit gateway. This should be the ASN for the AWS side of a Border Gateway Protocol (BGP) session.
  The range is 64512 to 65534 for 16-bit ASNs.
