

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `GetConnectionStatus` with a CLI
<a name="example_ssm_GetConnectionStatus_section"></a>

The following code examples show how to use `GetConnectionStatus`.

------
#### [ CLI ]

**AWS CLI**  
**To display the connection status of a managed instance**  
This `get-connection-status` example returns the connection status of the specified managed instance.  

```
aws ssm get-connection-status \
    --target {{i-1234567890abcdef0}}
```
Output:  

```
{
    "Target": "i-1234567890abcdef0",
    "Status": "connected"
}
```
+  For API details, see [GetConnectionStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-connection-status.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example retrieves the Session Manager connection status for an instance to determine whether it is connected and ready to receive Session Manager connections. **  

```
Get-SSMConnectionStatus -Target i-0a1caf234f12d3dc4
```
**Output:**  

```
Status    Target
------    ------
Connected i-0a1caf234f12d3dc4
```
+  For API details, see [GetConnectionStatus](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example retrieves the Session Manager connection status for an instance to determine whether it is connected and ready to receive Session Manager connections. **  

```
Get-SSMConnectionStatus -Target i-0a1caf234f12d3dc4
```
**Output:**  

```
Status    Target
------    ------
Connected i-0a1caf234f12d3dc4
```
+  For API details, see [GetConnectionStatus](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.