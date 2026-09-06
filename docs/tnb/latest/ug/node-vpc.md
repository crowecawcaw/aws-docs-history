

# AWS.Networking.VPC
<a name="node-vpc"></a>

You must specify a CIDR block for your virtual private cloud (VPC).

## Syntax
<a name="node-vpc-syntax"></a>

```
tosca.nodes.AWS.Networking.VPC:
  properties:
    cidr\_block: String
    ipv6\_cidr\_block: String        
    dns\_support: String
    tags: List
```

## Properties
<a name="node-vpc-properties"></a>

 `cidr_block`    
The IPv4 network range for the VPC, in CIDR notation.  
Required: Yes  
Type: String

 `ipv6_cidr_block`    
The IPv6 CIDR block used to create the VPC.  
Allowed value: `AMAZON_PROVIDED`  
Required: No  
Type: String

 `dns_support`    
Indicates whether the instances launched in the VPC get DNS hostnames.  
Required: No  
Type: Boolean  
Default: `false` 

 `tags`    
Tags to be attached to the resource.  
Required: No  
Type: List

## Example
<a name="node-vpc-example"></a>

```
SampleVPC:
  type: tosca.nodes.AWS.Networking.VPC
  properties:
    cidr_block: "10.100.0.0/16"
    ipv6_cidr_block: "AMAZON_PROVIDED"
    dns_support: true
    tags:
      - "Name=SampleVPC"
      - "Environment=Testing"
```