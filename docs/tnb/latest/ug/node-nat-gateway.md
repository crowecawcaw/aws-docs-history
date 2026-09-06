

# AWS.Networking.NATGateway
<a name="node-nat-gateway"></a>

You can define a public or private NAT Gateway node over a subnet. For a public gateway, if you do not provide an Elastic IP allocation id, AWS TNB will allocate an Elastic IP for your account and associate that to the gateway.

## Syntax
<a name="node-nat-gateway-syntax"></a>

```
tosca.nodes.AWS.Networking.NATGateway:
  requirements:
    subnet: String
    internet\_gateway: String
  properties:
    type: String
    eip\_allocation\_id: String
    tags: List
```

## Properties
<a name="node-nat-gateway-requirements"></a>

 `subnet`    
The [AWS.Networking.Subnet](https://docs.aws.amazon.com/tnb/latest/ug/node-subnet.html) node reference.  
Required: Yes  
Type: String

 `internet_gateway`    
The [AWS.Networking.InternetGateway](https://docs.aws.amazon.com/tnb/latest/ug/node-internet-gateway.html) node reference.  
Required: Yes  
Type: String

## Properties
<a name="node-nat-gateway-properties"></a>

 `type`    
Indicates if the gateway is public or private.  
Allowed value: `PUBLIC`, `PRIVATE`  
Required: Yes  
Type: String

 `eip_allocation_id`    
The ID that represents the allocation of the Elastic IP address.  
Required: No  
Type: String

 `tags`    
Tags to be attached to the resource.  
Required: No  
Type: List

## Example
<a name="node-nat-gateway-example"></a>

```
Free5GCNatGateway01:
  type: tosca.nodes.AWS.Networking.NATGateway
    requirements:
       subnet: Free5GCSubnet01
       internet_gateway: Free5GCIGW
    properties:
       type: PUBLIC
       eip_allocation_id: eipalloc-12345
```