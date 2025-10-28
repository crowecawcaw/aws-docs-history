# Common VPC peering connection configurations

This section describes two common types of VPC peering configurations that you can implement:

- **VPC peering configurations with routes to an entire VPC**: In
  this configuration, you create a route in each VPC's route table that sends all traffic
  destined for the peer VPC to the VPC peering connection. This allows any resource in one
  VPC to communicate with any resource in the peer VPC, simplifying management. However,
  it also means that all traffic between the VPCs will flow through the peering
  connection, which could become a bottleneck if the traffic volume is high.
- **VPC peering configurations with specific routes**:
  Alternatively, you can create more granular routes in each VPC's route table that only
  send traffic to specific subnets or resources in the peer VPC. This allows you to limit
  the traffic flowing through the peering connection to only what is necessary, which can
  be more efficient. However, it also requires more maintenance, as you'll need to update
  the route tables any time you add new resources in the peer VPC that need to
  communicate.
  The best approach depends on factors like the size and complexity of your VPC architecture, the volume of traffic expected between the VPCs, and your organizational needs around security and resource access. Many enterprises use a hybrid approach, with broad routes for common traffic patterns and specific routes for more sensitive or bandwidth-intensive use cases.

###### Configurations

- [VPC peering configurations with routes to an entire VPC](peering-configurations-full-access.md "peering-configurations-full-access.md")
- [VPC peering configurations with specific routes](peering-configurations-partial-access.md "peering-configurations-partial-access.md")
