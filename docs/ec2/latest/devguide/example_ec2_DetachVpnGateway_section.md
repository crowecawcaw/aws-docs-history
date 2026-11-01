

# Use `DetachVpnGateway` with a CLI
<a name="example_ec2_DetachVpnGateway_section"></a>

The following code examples show how to use `DetachVpnGateway`.

------
#### [ CLI ]

**AWS CLI**  
**To detach a virtual private gateway from your VPC**  
The following `detach-vpn-gateway` example detaches the specified virtual private gateway from the specified VPC.  

```
aws ec2 detach-vpn-gateway \
    --vpn-gateway-id {{vgw-9a4cacf3}} \
    --vpc-id {{vpc-a01106c2}}
```
This command produces no output.  
For more information, see [How AWS Site-to-Site VPN works](https://docs.aws.amazon.com/vpn/latest/s2svpn/how_it_works.html) in the *AWS Site-to-Site VPN User Guide*.  
+  For API details, see [DetachVpnGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-vpn-gateway.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example detaches the specified virtual private gateway from the specified VPC.**  

```
Dismount-EC2VpnGateway -VpnGatewayId vgw-1a2b3c4d -VpcId vpc-12345678
```
+  For API details, see [DetachVpnGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example detaches the specified virtual private gateway from the specified VPC.**  

```
Dismount-EC2VpnGateway -VpnGatewayId vgw-1a2b3c4d -VpcId vpc-12345678
```
+  For API details, see [DetachVpnGateway](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.