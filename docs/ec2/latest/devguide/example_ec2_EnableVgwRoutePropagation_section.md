

# Use `EnableVgwRoutePropagation` with a CLI
<a name="example_ec2_EnableVgwRoutePropagation_section"></a>

The following code examples show how to use `EnableVgwRoutePropagation`.

------
#### [ CLI ]

**AWS CLI**  
**To enable route propagation**  
This example enables the specified virtual private gateway to propagate static routes to the specified route table. If the command succeeds, no output is returned.  
Command:  

```
aws ec2 enable-vgw-route-propagation --route-table-id {{rtb-22574640}} --gateway-id {{vgw-9a4cacf3}}
```
+  For API details, see [EnableVgwRoutePropagation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-vgw-route-propagation.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example enables the specified VGW to propagate routes automatically to the specified routing table.**  

```
Enable-EC2VgwRoutePropagation -RouteTableId rtb-12345678 -GatewayId vgw-1a2b3c4d
```
+  For API details, see [EnableVgwRoutePropagation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example enables the specified VGW to propagate routes automatically to the specified routing table.**  

```
Enable-EC2VgwRoutePropagation -RouteTableId rtb-12345678 -GatewayId vgw-1a2b3c4d
```
+  For API details, see [EnableVgwRoutePropagation](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.