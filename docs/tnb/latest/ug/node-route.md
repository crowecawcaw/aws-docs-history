# AWS.Networking.Route

You can define a route node that associates the destination route to the NAT Gateway as
the target resource, and adds the route to the associated route table.

## Syntax

```
tosca.nodes.AWS.Networking.Route:
  properties:
    dest_cidr_blocks: List
  requirements:
    nat_gateway: String
    route_table: String
```

## Properties

`dest_cidr_blocks`

The list of destination IPv4 routes to the target resource.

Required: Yes

Type: List

Member type: String

## Requirements

`nat_gateway`

The [AWS.Networking.NATGateway](node-nat-gateway.md "node-nat-gateway.md") node reference.

Required: Yes

Type: String

`route_table`

The [AWS.Networking.RouteTable](node-route-table.md "node-route-table.md") node reference.

Required: Yes

Type: String

## Example

```
Free5GCRoute:
  type: tosca.nodes.AWS.Networking.Route
  properties:
    dest_cidr_blocks:
      - 0.0.0.0/0
      - 10.0.0.0/28
  requirements:
    nat_gateway: Free5GCNatGateway01
    route_table: Free5GCRouteTable
```
