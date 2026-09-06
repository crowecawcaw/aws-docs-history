

# AWS.Networking.RouteTable
<a name="node-route-table"></a>

A route table contains a set of rules, called routes, that determine where network traffic from subnets within your VPC or gateway is directed. You must associate a route table with a VPC.

## Syntax
<a name="node-route-table-syntax"></a>

```
tosca.nodes.AWS.Networking.RouteTable:
  properties:
    tags: List
  requirements:
    vpc: String
```

## Properties
<a name="node-route-table-properties"></a>

 `tags`    
Tags to be attached to the resource.  
Required: No  
Type: List

## Requirements
<a name="node-route-table-requirements"></a>

 `vpc`    
An [AWS.Networking.VPC](node-vpc.md) node.  
Required: Yes  
Type: String

## Example
<a name="node-route-table-example"></a>

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