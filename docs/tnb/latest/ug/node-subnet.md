

# AWS.Networking.Subnet
<a name="node-subnet"></a>

A subnet is a range of IP addresses in your VPC, and it must reside entirely within one Availability Zone. You must specify a VPC, a CIDR block, Availability Zone, and a route table for your subnet. You must also define whether your subnet is private or public.

## Syntax
<a name="node-subnet-syntax"></a>

```
tosca.nodes.AWS.Networking.Subnet:
  properties:
    type: String
    availability\_zone: String
    cidr\_block: String
    ipv6\_cidr\_block: String
    ipv6\_cidr\_block\_suffix: String        
    outpost\_arn: String
    tags: List
  requirements:
    vpc: String
    route\_table: String
```

## Properties
<a name="node-subnet-properties"></a>

 `type`    
Indicates whether instances launched in this subnet receive a public IPv4 address.  
Required: Yes  
Type: String  
Possible values: `PUBLIC` \| `PRIVATE`

 `availability_zone`    
The Availability Zone for the subnet. This field supports AWS Availability Zones within a AWS Region, for example `us-west-2` (US West (Oregon)). It also supports AWS Local Zones within the Availability Zone, for example `us-west-2-lax-1a`.  
Required: Yes  
Type: String

 `cidr_block`    
The CIDR block for the subnet.  
Required: No  
Type: String

 `ipv6_cidr_block`    
The CIDR block used to create the IPv6 subnet. If you include this property, do not include `ipv6_cidr_block_suffix`.  
Required: No  
Type: String

 `ipv6_cidr_block_suffix`    
The 2-digit hexadecimal suffix of the IPv6 CIDR block for the subnet created over Amazon VPC. Use the following format: `{{2-digit hexadecimal}}::/{{subnetMask}}`  
If you include this property, do not include `ipv6_cidr_block`.  
Required: No  
Type: String

 `outpost_arn`    
The ARN of AWS Outposts that the subnet will be created in. Add this property to the NSD template if you want to launch Amazon EKS self-managed nodes on AWS Outposts. For more information, see [Amazon EKS on AWS Outposts](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts.html) in the *Amazon EKS User Guide*.  
If you add this property to the NSD template, you must set the value for the `availability_zone` property to the Availability Zone of the AWS Outposts.  
Required: No  
Type: String

 `tags`    
The tags to be attached to the resource.  
Required: No  
Type: List

## Requirements
<a name="node-subnet-requirements"></a>

 `vpc`    
An [AWS.Networking.VPC](node-vpc.md) node.  
Required: Yes  
Type: String

 `route_table`    
An [AWS.Networking.RouteTable](node-route-table.md) node.  
Required: Yes  
Type: String

## Example
<a name="node-subnet-example"></a>

```
SampleSubnet01:
  type: tosca.nodes.AWS.Networking.Subnet
  properties:
    type: "PUBLIC"
    availability_zone: "us-east-1a"
    cidr_block: "10.100.50.0/24"
    ipv6_cidr_block_suffix: "aa::/64"
    outpost_arn: "arn:aws:outposts:region:accountId:outpost/op-11223344EXAMPLE"
    tags:
      - "Name=SampleVPC"
      - "Environment=Testing"
  requirements:
    vpc: SampleVPC
    route_table: SampleRouteTable
         
SampleSubnet02:
  type: tosca.nodes.AWS.Networking.Subnet
  properties:
    type: "PUBLIC"
    availability_zone: "us-west-2b"
    cidr_block: "10.100.50.0/24"
    ipv6_cidr_block: "2600:1f14:3758:ca00::/64"
  requirements:
    route_table: SampleRouteTable
    vpc: SampleVPC
```