

# Use `DeleteVpnConnection` with a CLI
<a name="example_ec2_DeleteVpnConnection_section"></a>

The following code examples show how to use `DeleteVpnConnection`.

------
#### [ CLI ]

**AWS CLI**  
**To delete a VPN connection**  
This example deletes the specified VPN connection. If the command succeeds, no output is returned.  
Command:  

```
aws ec2 delete-vpn-connection --vpn-connection-id {{vpn-40f41529}}
```
+  For API details, see [DeleteVpnConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpn-connection.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example deletes the specified VPN connection. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**  

```
Remove-EC2VpnConnection -VpnConnectionId vpn-12345678
```
**Output:**  

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2VpnConnection (DeleteVpnConnection)" on Target "vpn-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteVpnConnection](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example deletes the specified VPN connection. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**  

```
Remove-EC2VpnConnection -VpnConnectionId vpn-12345678
```
**Output:**  

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2VpnConnection (DeleteVpnConnection)" on Target "vpn-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteVpnConnection](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.