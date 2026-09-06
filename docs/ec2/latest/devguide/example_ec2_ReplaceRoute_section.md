

# Use `ReplaceRoute` with a CLI
<a name="example_ec2_ReplaceRoute_section"></a>

The following code examples show how to use `ReplaceRoute`.

------
#### [ CLI ]

**AWS CLI**  
**To replace a route**  
This example replaces the specified route in the specified route table. The new route matches the specified CIDR and sends the traffic to the specified virtual private gateway. If the command succeeds, no output is returned.  
Command:  

```
aws ec2 replace-route --route-table-id {{rtb-22574640}} --destination-cidr-block {{10.0.0.0/16}} --gateway-id {{vgw-9a4cacf3}}
```
+  For API details, see [ReplaceRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-route.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example replaces the specified route for the specified route table. The new route sends the specified traffic to the specified virtual private gateway.**  

```
Set-EC2Route -RouteTableId rtb-1a2b3c4d -DestinationCidrBlock 10.0.0.0/24 -GatewayId vgw-1a2b3c4d
```
+  For API details, see [ReplaceRoute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example replaces the specified route for the specified route table. The new route sends the specified traffic to the specified virtual private gateway.**  

```
Set-EC2Route -RouteTableId rtb-1a2b3c4d -DestinationCidrBlock 10.0.0.0/24 -GatewayId vgw-1a2b3c4d
```
+  For API details, see [ReplaceRoute](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.