# Amazon Neptune and interface VPC endpoints (AWS PrivateLink)

You can use [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/") to create a private connection between your VPC and
Amazon Neptune API endpoints. You can access Amazon Neptune API operations as though they were
in your VPC, without the use of an internet gateway, NAT device, VPN connection, or
connection. Traffic between your VPC and Amazon Neptune stays within the Amazon network.

Amazon Neptune shares API infrastructure with Amazon Relational Database Service. To set up interface VPC endpoints
for Amazon Neptune, follow the instructions in [Amazon RDS API and
interface VPC endpoints (AWS PrivateLink)](../../../AmazonRDS/latest/AuroraUserGuide/vpc-interface-endpoints.md "../../../AmazonRDS/latest/AuroraUserGuide/vpc-interface-endpoints.md") in the
_Amazon Aurora User Guide_.
