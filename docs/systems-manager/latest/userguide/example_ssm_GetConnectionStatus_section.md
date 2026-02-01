• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Use `GetConnectionStatus` with a CLI

The following code examples show how to use `GetConnectionStatus`.

CLI

**AWS CLI**

**To display the connection status of a managed instance**

This `get-connection-status` example returns the connection status of the specified managed instance.

```
`aws ssm get-connection-status \
 --target `i-1234567890abcdef0``

```

Output:

```
{
    "Target": "i-1234567890abcdef0",
    "Status": "connected"
}
```

- For API details, see
  [GetConnectionStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-connection-status.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-connection-status.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example retrieves the Session Manager connection status for an instance to determine whether it is connected and ready to receive Session Manager connections.**

```
Get-SSMConnectionStatus -Target i-0a1caf234f12d3dc4

```

**Output:**

```
Status    Target
------    ------
Connected i-0a1caf234f12d3dc4
```

- For API details, see
  [GetConnectionStatus](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example retrieves the Session Manager connection status for an instance to determine whether it is connected and ready to receive Session Manager connections.**

```
Get-SSMConnectionStatus -Target i-0a1caf234f12d3dc4

```

**Output:**

```
Status    Target
------    ------
Connected i-0a1caf234f12d3dc4
```

- For API details, see
  [GetConnectionStatus](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
