

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `GetMaintenanceWindow` with a CLI
<a name="example_ssm_GetMaintenanceWindow_section"></a>

The following code examples show how to use `GetMaintenanceWindow`.

------
#### [ CLI ]

**AWS CLI**  
**To get information about a maintenance window**  
The following `get-maintenance-window` example retrieves details about the specified maintenance window.  

```
aws ssm get-maintenance-window \
    --window-id {{"mw-03eb9db428EXAMPLE"}}
```
Output:  

```
{
    "AllowUnassociatedTargets": true,
    "CreatedDate": 1515006912.957,
    "Cutoff": 1,
    "Duration": 6,
    "Enabled": true,
    "ModifiedDate": 2020-01-01T10:04:04.099Z,
    "Name": "My-Maintenance-Window",
    "Schedule": "rate(3 days)",
    "WindowId": "mw-03eb9db428EXAMPLE",
    "NextExecutionTime": "2020-02-25T00:08:15.099Z"
}
```
For more information, see [View information about maintenance windows (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-describe.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [GetMaintenanceWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example gets details about a maintenance window.**  

```
Get-SSMMaintenanceWindow -WindowId "mw-03eb9db42890fb82d"
```
**Output:**  

```
AllowUnassociatedTargets : False
CreatedDate              : 2/20/2017 6:14:05 PM
Cutoff                   : 1
Duration                 : 2
Enabled                  : True
ModifiedDate             : 2/20/2017 6:14:05 PM
Name                     : TestMaintWin
Schedule                 : cron(0 */30 * * * ? *)
WindowId                 : mw-03eb9db42890fb82d
```
+  For API details, see [GetMaintenanceWindow](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example gets details about a maintenance window.**  

```
Get-SSMMaintenanceWindow -WindowId "mw-03eb9db42890fb82d"
```
**Output:**  

```
AllowUnassociatedTargets : False
CreatedDate              : 2/20/2017 6:14:05 PM
Cutoff                   : 1
Duration                 : 2
Enabled                  : True
ModifiedDate             : 2/20/2017 6:14:05 PM
Name                     : TestMaintWin
Schedule                 : cron(0 */30 * * * ? *)
WindowId                 : mw-03eb9db42890fb82d
```
+  For API details, see [GetMaintenanceWindow](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.