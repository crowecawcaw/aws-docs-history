# AWS.Networking.InternetGateway

Defines an AWS Internet Gateway Node.

## Syntax

```
tosca.nodes.AWS.Networking.InternetGateway:
  capabilities:
    routing:
      properties:
        dest_cidr: String
        ipv6_dest_cidr: String
  properties:
    tags: List
    egress_only: Boolean
  requirements:
    vpc: String
    route_table: String
```

## Capabilities

###### `routing`

Properties that define the routing connection within the VPC. You must include
either the `dest_cidr` or `ipv6_dest_cidr` property.

`dest_cidr`

The IPv4 CIDR block used for the destination match. This property is used to
create a route in `RouteTable` and its value is used as the
`DestinationCidrBlock`.

Required: No if you included the `ipv6_dest_cidr`
property.

Type: String

`ipv6_dest_cidr`

The IPv6 CIDR block used for the destination match.

Required: No if you included the `dest_cidr` property.

Type: String

## Properties

`tags`

The tags to be attached to the resource.

Required: No

Type: List

`egress_only`

An IPv6-specific property. Indicates if the internet gateway is only for
egress communication or not. When `egress_only` is true, you must
define the `ipv6_dest_cidr` property.

Required: No

Type: Boolean

## Requirements

`vpc`

An [AWS.Networking.VPC](node-vpc.md "node-vpc.md") node.

Required: Yes

Type: String

`route_table`

An [AWS.Networking.RouteTable](node-route-table.md "node-route-table.md")
node.

Required: Yes

Type: String

## Example

```
Free5GCIGW:
  type: tosca.nodes.AWS.Networking.InternetGateway
  properties:
    egress_only: false
  capabilities:
    routing:
      properties:
        dest_cidr: "0.0.0.0/0"
        ipv6_dest_cidr: "::/0"
  requirements:
    route_table: Free5GCRouteTable
    vpc: Free5GCVPC
Free5GCEGW:
  type: tosca.nodes.AWS.Networking.InternetGateway
  properties:
    egress_only: true
  capabilities:
    routing:
      properties:
        ipv6_dest_cidr: "::/0"
  requirements:
    route_table: Free5GCPrivateRouteTable
    vpc: Free5GCVPC
```
