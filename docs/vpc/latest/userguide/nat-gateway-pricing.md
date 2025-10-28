# Pricing for NAT gateways

When you provision a NAT gateway, you are charged for each hour that your NAT gateway is
available and each gigabyte of data that it processes. For more information, see [Amazon VPC Pricing](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/").

The following strategies can help you reduce the data transfer charges for your NAT gateway:

- If your AWS resources send or receive a significant volume of traffic across
  Availability Zones, ensure that the resources are in the same Availability Zone as the NAT
  gateway. Alternatively, create a NAT gateway in each Availability Zone with resources.
- If most traffic through your NAT gateway is to AWS services that support interface
  endpoints or gateway endpoints, consider creating an interface endpoint or gateway endpoint
  for these services. For more information about the potential cost savings, see [AWS PrivateLink pricing](https://aws.amazon.com/privatelink/pricing/ "https://aws.amazon.com/privatelink/pricing/").
