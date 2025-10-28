# Amazon VPC subnet endpoints for custom routing accelerators in Global Accelerator

Endpoints for custom routing accelerators are Amazon Virtual Private Cloud (VPC) subnets that can receive traffic
through an accelerator. Each subnet can contain one or many Amazon EC2 instance destinations. When you add a subnet endpoint, Global Accelerator
generates new port mapping. Then, you can use the Global Accelerator API to get a static list of all the port mappings for the subnet,
which you can use to route traffic to destination EC2 instance IP addresses in the subnet. For more information, see
[ListCustomRoutingPortMappings](../api/API_ListCustomRoutingPortMappings.md "../api/API_ListCustomRoutingPortMappings.md").

Be aware of the following when you add VPC subnets and destinations for your custom routing accelerator:

- You can only direct traffic to EC2 instances in the subnets, not other resources, like load balancers (in contrast to
  standard accelerators).
- An EC2 instance destination in a subnet endpoint can't be one of the following types: C1, CC1, CC2, CG1,
  CG2, CR1, CS1, G1, G2, HI1, HS1, M1, M2, M3, or T1.
- By default, traffic directed through a custom routing accelerator can't arrive at any destinations in your subnet. To enable destination instances
  to receive traffic, you must choose to allow all traffic to the subnet or, alternatively, enable traffic to specific instance
  IP addresses and ports (destination sockets) in the subnet.

###### Important

Updating a subnet or specific destination to allow or deny traffic takes time to propagate across the
internet. To determine if a change has propagated, you can use the `DescribeCustomRoutingAccelerator`
API action to check the accelerator status. For more information, see [DescribeCustomRoutingAccelerator](../api/API_DescribeCustomRoutingAccelerator.md "../api/API_DescribeCustomRoutingAccelerator.md").

- Because VPC subnets preserve the client IP address, you should review the relevant security and configuration information
  when you add subnets as endpoints for custom routing accelerators. For more information, see [Requirements for endpoints with client IP address preservation](about-endpoints.md "about-endpoints.md").
- When you configure resources as endpoints behind Global Accelerator, we recommend that you don't
  also send traffic directly to the same endpoints over the internet. Sending direct traffic can lead to connection
  collision issues.
  To learn more, see [How custom routing accelerators work in Global Accelerator](about-custom-routing-how-it-works.md "about-custom-routing-how-it-works.md").

###### Contents

- [Add an Amazon VPC subnet endpoint](about-custom-routing-endpoints-adding-endpoints.md "about-custom-routing-endpoints-adding-endpoints.md")
- [Edit an Amazon VPC subnet endpoint](about-custom-routing-endpoints-editing-endpoints.md "about-custom-routing-endpoints-editing-endpoints.md")
- [Remove an Amazon VPC subnet endpoint](about-custom-routing-endpoints-removing-endpoints.md "about-custom-routing-endpoints-removing-endpoints.md")
