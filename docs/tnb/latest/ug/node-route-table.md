# AWS.Networking.RouteTable

A route table contains a set of rules, called routes, that determine where network
traffic from subnets within your VPC or gateway is directed. You must associate a route
table with a VPC.

## Syntax

```
tosca.nodes.AWS.Networking.RouteTable:
  properties:
    tags: List
  requirements:
    vpc: String
```

## Properties

`tags`

Tags to be attached to the resource.

Required: No

Type: List

## Requirements

`vpc`

An [AWS.Networking.VPC](node-vpc.md "node-vpc.md") node.

Required: Yes

Type: String

## Example

```
SampleRouteTable:
  type: tosca.nodes.AWS.Networking.RouteTable
  properties:
    tags:
      - "Name=SampleVPC"
      - "Environment=Testing"
  requirements:
    vpc: SampleVPC
```
