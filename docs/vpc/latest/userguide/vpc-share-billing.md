# Billing and metering for owner and participants

This section contains billing and metering details for those who own the shared subnet and for those working with the shared subnet:

- In a shared VPC, each participant pays for their application resources including Amazon EC2
  instances, Amazon Relational Database Service databases, Amazon Redshift clusters, and AWS Lambda functions. Participants also
  pay for data transfer charges associated with inter-Availability Zone data transfer as well as data transfer over VPC peering connections, across internet gateways, and across AWS Direct Connect gateways.
- VPC owners pay hourly charges (where applicable), data processing and data transfer charges
  across NAT gateways, virtual private gateways, transit gateways, AWS PrivateLink, and VPC
  endpoints. In addition, public IPv4 addresses used in shared VPCs are billed to VPC
  owners. For more information about public IPv4 address pricing, see the **Public
  IPv4 Address** tab on the [Amazon VPC
  pricing page](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/").
- Data transfer within the same Availability Zone (uniquely identified using the AZ-ID) is free
  irrespective of account ownership of the communicating resources.
