

# Use `CreateRoute` with a CLI
<a name="example_ec2_CreateRoute_section"></a>

The following code examples show how to use `CreateRoute`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples: 
+  [Create a basic virtual private network](example_vpc_GettingStartedCLI_section.md) 
+  [Getting started with graph databases](example_ec2_GettingStarted_064_section.md) 
+  [Getting started with network transit gateways](example_vpc_TransitGatewayGettingStarted_section.md) 
+  [Virtual private network with private servers](example_vpc_GettingStartedPrivate_section.md) 
+  [Working with network peering connections](example_ec2_GettingStarted_015_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To create a route**  
This example creates a route for the specified route table. The route matches all IPv4 traffic (`0.0.0.0/0`) and routes it to the specified Internet gateway. If the command succeeds, no output is returned.  
Command:  

```
aws ec2 create-route --route-table-id {{rtb-22574640}} --destination-cidr-block {{0.0.0.0/0}} --gateway-id {{igw-c0a643a9}}
```
This example command creates a route in route table rtb-g8ff4ea2. The route matches traffic for the IPv4 CIDR block 10.0.0.0/16 and routes it to VPC peering connection, pcx-111aaa22. This route enables traffic to be directed to the peer VPC in the VPC peering connection. If the command succeeds, no output is returned.  
Command:  

```
aws ec2 create-route --route-table-id {{rtb-g8ff4ea2}} --destination-cidr-block {{10.0.0.0/16}} --vpc-peering-connection-id {{pcx-1a2b3c4d}}
```
This example creates a route in the specified route table that matches all IPv6 traffic (`::/0`) and routes it to the specified egress-only Internet gateway.  
Command:  

```
aws ec2 create-route --route-table-id {{rtb-dce620b8}} --destination-ipv6-cidr-block {{::/0}} --egress-only-internet-gateway-id {{eigw-01eadbd45ecd7943f}}
```
+  For API details, see [CreateRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-route.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example creates the specified route for the specified route table. The route matches all traffic and sends it to the specified Internet gateway.**  

```
New-EC2Route -RouteTableId rtb-1a2b3c4d -DestinationCidrBlock 0.0.0.0/0 -GatewayId igw-1a2b3c4d
```
**Output:**  

```
True
```
+  For API details, see [CreateRoute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example creates the specified route for the specified route table. The route matches all traffic and sends it to the specified Internet gateway.**  

```
New-EC2Route -RouteTableId rtb-1a2b3c4d -DestinationCidrBlock 0.0.0.0/0 -GatewayId igw-1a2b3c4d
```
**Output:**  

```
True
```
+  For API details, see [CreateRoute](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.