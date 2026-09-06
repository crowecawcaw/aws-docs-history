

# Use `DisableVgwRoutePropagation` with a CLI
<a name="example_ec2_DisableVgwRoutePropagation_section"></a>

The following code examples show how to use `DisableVgwRoutePropagation`.

------
#### [ CLI ]

**AWS CLI**  
**To disable route propagation**  
This example disables the specified virtual private gateway from propagating static routes to the specified route table. If the command succeeds, no output is returned.  
Command:  

```
aws ec2 disable-vgw-route-propagation --route-table-id {{rtb-22574640}} --gateway-id {{vgw-9a4cacf3}}
```
+  For API details, see [DisableVgwRoutePropagation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-vgw-route-propagation.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example disables the VGW from automatically propagating routes to the specified routing table.**  

```
Disable-EC2VgwRoutePropagation -RouteTableId rtb-12345678 -GatewayId vgw-1a2b3c4d
```
+  For API details, see [DisableVgwRoutePropagation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example disables the VGW from automatically propagating routes to the specified routing table.**  

```
Disable-EC2VgwRoutePropagation -RouteTableId rtb-12345678 -GatewayId vgw-1a2b3c4d
```
+  For API details, see [DisableVgwRoutePropagation](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.