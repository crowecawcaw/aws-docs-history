# AWS.Networking.ENI

A network interface is a logical networking component in a VPC that represents a virtual
network card. A network interface is assigned an IP address either automatically or
manually based on its subnet. After you deploy an Amazon EC2 instance in a subnet, you can
attach a network interface to it, or detach a network interface from that Amazon EC2 instance
and reattach to another Amazon EC2 instance in that subnet. The device index identifies the
position in the attachment order.

## Syntax

```
tosca.nodes.AWS.Networking.ENI:
  properties:
    device_index: Integer
    source_dest_check: Boolean
    tags: List
  requirements:
    subnet: String
    security_groups: List

```

## Properties

`device_index`

The device index must be greater than zero.

Required: Yes

Type: Integer

`source_dest_check`

Indicates whether the network interface performs source/destination
checking. A value of `true` means that checking is enabled, and
`false` means that checking is disabled.

Allowed value: true, false

Default: true

Required: No

Type: Boolean

`tags`

The tags to be attached to the resource.

Required: No

Type: List

## Requirements

`subnet`

An [AWS.Networking.Subnet](node-subnet.md "node-subnet.md") node.

Required: Yes

Type: String

`security_groups`

An [AWS.Networking.SecurityGroup](node-networking-security-group.md "node-networking-security-group.md") node.

Required: No

Type: String

## Example

```
SampleENI:
  type: tosca.nodes.AWS.Networking.ENI
  properties:
    device_index: 5
    source_dest_check: true
    tags:
      - "Name=SampleVPC"
      - "Environment=Testing"
  requirements:
    subnet: SampleSubnet
    security_groups:
      - SampleSecurityGroup01
      - SampleSecurityGroup02
```
