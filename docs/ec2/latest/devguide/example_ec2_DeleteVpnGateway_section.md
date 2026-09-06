

# Use `DeleteVpnGateway` with a CLI
<a name="example_ec2_DeleteVpnGateway_section"></a>

The following code examples show how to use `DeleteVpnGateway`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Get started with dedicated network connections](example_directconnect_GettingStarted_051_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To delete a virtual private gateway**  
This example deletes the specified virtual private gateway. If the command succeeds, no output is returned.  
Command:  

```
aws ec2 delete-vpn-gateway --vpn-gateway-id {{vgw-9a4cacf3}}
```
+  For API details, see [DeleteVpnGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpn-gateway.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example deletes the specified virtual private gateway. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**  

```
Remove-EC2VpnGateway -VpnGatewayId vgw-1a2b3c4d
```
**Output:**  

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2VpnGateway (DeleteVpnGateway)" on Target "vgw-1a2b3c4d".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteVpnGateway](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example deletes the specified virtual private gateway. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**  

```
Remove-EC2VpnGateway -VpnGatewayId vgw-1a2b3c4d
```
**Output:**  

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2VpnGateway (DeleteVpnGateway)" on Target "vgw-1a2b3c4d".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteVpnGateway](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.