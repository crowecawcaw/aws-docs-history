# Route Analyzer for AWS Network Manager

With AWS Global Networks for Transit Gateways, you can use the Route Analyzer to perform an analysis of the routes in
your transit gateway route tables. Through AWS Network Manager, Route Analyzer analyzes the routing
path between a specified source and destination, and returns information about the
connectivity between components. You can use the Route Analyzer to do the
following:

- Verify that the transit gateway route table configuration will work as expected
  before you start sending traffic.
- Validate your existing route configuration.
- Diagnose route-related issues that are causing traffic disruption in your global
  network.

###### Note

Route Analyzer does not work with intra-Region peering.

###### Topics

- [Route Analyzer basics](#route-analyzer-basics "#route-analyzer-basics")
- [Perform a route analysis](working-with-route-analyzer.md "working-with-route-analyzer.md")
- [Example: Route analysis for peered transit
  gateways](example-route-analyzer.md "example-route-analyzer.md")
- [Example: Route analysis with a
  middlebox configuration](example-route-analyzer-middlebox.md "example-route-analyzer-middlebox.md")

## Route Analyzer basics

To use the Route Analyzer, you indicate the path for the traffic from a source to a
destination. For the source, you specify the transit gateway, the transit gateway
attachment from which the traffic originates, and a source IPv4 or IPv6 address. The
Route Analyzer analyzes the routes in the associated transit gateway route table for
the transit gateway attachment. For the destination, you specify a target IPv4 or IPv6
address, and the destination transit gateway and transit gateway attachment.

If you've configured a middlebox appliance in your VPC, you can indicate the location
of the appliance in the route analysis. This enables you to specify multiple network
hops in a route between a source and destination, to help you analyze the route of the
traffic. We store this information for use in future analyses. You can update your
middlebox appliances later on as needed.

You can also analyze the return path for traffic from the specified destination back
to the source.

The following rules apply when using the Route Analyzer:

- The Route Analyzer analyzes routes in transit gateway route tables only. It
  does not analyze routes in VPC route tables or in your customer gateway devices.
- The transit gateways must be registered in your global network.
- The Route Analyzer does not analyze security group rules or network ACL
  rules. To capture information about accepted and rejected IP traffic in your
  VPC, you can use [VPC flow
  logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md").
- The Route Analyzer only returns information for the return path if it can
  successfully return information for the forward path.
