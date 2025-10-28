# Limits

The following limitations are applicable to the VPC-ENI feature:

- You can provide up to five security groups in the VPC configuration of a Device Farm project.
- You can provide up to eight subnets in the VPC configuration of a Device Farm project.
- When configuring a Device Farm project to work with your VPC, the smallest subnet you can provide must
  have a minimum of five available IPv4 addresses.
- Public IP addresses aren’t supported at this time. Instead, we recommend that you use private
  subnets in your Device Farm projects. If your need public internet access during your tests, use a [network
  address translation (NAT) gateway](../../../lambda/latest/dg/configuration-vpc.md#vpc-internet "../../../lambda/latest/dg/configuration-vpc.md#vpc-internet"). Configuring a Device Farm project with a public subnet
  doesn't give your tests internet access or a public IP address.
- VPC-ENI integration only supports private subnets in your VPC.
- Only outgoing traffic from the service-managed ENI is supported. This means that the ENI cannot
  receive unsolicited inbound requests from the VPC.
