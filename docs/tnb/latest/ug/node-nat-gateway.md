# AWS.Networking.NATGateway

You can define a public or private NAT Gateway node over a subnet. For a public gateway,
if you do not provide an Elastic IP allocation id, AWS TNB will allocate an Elastic IP
for your account and associate that to the gateway.

## Syntax

```
tosca.nodes.AWS.Networking.NATGateway:
  requirements:
    subnet: String
    internet_gateway: String
  properties:
    type: String
    eip_allocation_id: String
    tags: List
```

## Properties

`subnet`

The [AWS.Networking.Subnet](node-subnet.md "node-subnet.md") node reference.

Required: Yes

Type: String

`internet_gateway`

The [AWS.Networking.InternetGateway](node-internet-gateway.md "node-internet-gateway.md") node reference.

Required: Yes

Type: String

## Properties

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
