

# AWS.Networking.Route
<a name="node-route"></a>

You can define a route node that associates the destination route to the NAT Gateway as the target resource, and adds the route to the associated route table.

## Syntax
<a name="node-route-syntax"></a>

```
tosca.nodes.AWS.Networking.Route:
  properties:
    dest\_cidr\_blocks: List          
  requirements:
    nat\_gateway: String
    route\_table: String
```

## Properties
<a name="node-route-properties"></a>

 `dest_cidr_blocks`    
The list of destination IPv4 routes to the target resource.  
Required: Yes  
Type: List  
Member type: String

## Requirements
<a name="node-route-requirements"></a>

 `nat_gateway`    
The [AWS.Networking.NATGateway](https://docs.aws.amazon.com/tnb/latest/ug/node-nat-gateway.html) node reference.  
Required: Yes  
Type: String

 `route_table`    
The [AWS.Networking.RouteTable](https://docs.aws.amazon.com/tnb/latest/ug/node-route-table.html) node reference.  
Required: Yes  
Type: String

## Example
<a name="node-route-example"></a>

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