# Endpoint groups for custom routing accelerators in Global Accelerator

With a custom routing accelerator in AWS Global Accelerator, an endpoint group defines the ports and protocols that destination Amazon EC2
instances in your virtual private cloud (VPC) subnets accept traffic on.

You create an endpoint group for your custom routing accelerator for each AWS Region in which your VPC subnets and EC2
instances are located. Each endpoint group in a custom routing accelerator can have multiple VPC subnet endpoints. Similarly, you
can add each VPC to multiple endpoint groups, but the endpoint groups must be associated with different
listeners.

For each endpoint group, you specify a set of one or more port ranges that include the ports that you want to direct traffic
to on the EC2 instances in the Region. For each endpoint group port range, you specify the protocol to use:
UDP, TCP, or both UDP and TCP. This provides maximum flexibility for you, without having to duplicate sets of
port ranges for each protocol. For example, you might have a game server with gaming traffic running over
UDP on ports 8080-8090 while you also have a server listening for chat messages over TCP on port 80.

To learn more, see [How custom routing accelerators work in Global Accelerator](about-custom-routing-how-it-works.md "about-custom-routing-how-it-works.md").

###### Contents

- [Add endpoint group](about-custom-routing-endpoint-groups.md "about-custom-routing-endpoint-groups.md")
- [Edit endpoint group](about-custom-routing-endpoint-groups.md "about-custom-routing-endpoint-groups.md")
- [Remove endpoint group](about-custom-routing-endpoint-groups.md "about-custom-routing-endpoint-groups.md")
