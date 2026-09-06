

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `DeregisterTaskFromMaintenanceWindow` with a CLI
<a name="example_ssm_DeregisterTaskFromMaintenanceWindow_section"></a>

The following code examples show how to use `DeregisterTaskFromMaintenanceWindow`.

------
#### [ CLI ]

**AWS CLI**  
**To remove a task from a maintenance window**  
The following `deregister-task-from-maintenance-window` example removes the specified task from the specified maintenance window.  

```
aws ssm deregister-task-from-maintenance-window \
    --window-id {{"mw-ab12cd34ef56gh78"}} \
    --window-task-id {{"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d5e6c"}}
```
Output:  

```
{
    "WindowTaskId":"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d5e6c",
    "WindowId":"mw-ab12cd34ef56gh78"
}
```
For more information, see [Systems Manager Maintenance Windows Tutorials (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-tutorials.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [DeregisterTaskFromMaintenanceWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/deregister-task-from-maintenance-window.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example removes a task from a maintenance window.**  

```
Unregister-SSMTaskFromMaintenanceWindow -WindowTaskId "f34a2c47-ddfd-4c85-a88d-72366b69af1b" -WindowId "mw-03a342e62c96d31b0"
```
**Output:**  

```
WindowId             WindowTaskId
--------             ------------
mw-03a342e62c96d31b0 f34a2c47-ddfd-4c85-a88d-72366b69af1b
```
+  For API details, see [DeregisterTaskFromMaintenanceWindow](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example removes a task from a maintenance window.**  

```
Unregister-SSMTaskFromMaintenanceWindow -WindowTaskId "f34a2c47-ddfd-4c85-a88d-72366b69af1b" -WindowId "mw-03a342e62c96d31b0"
```
**Output:**  

```
WindowId             WindowTaskId
--------             ------------
mw-03a342e62c96d31b0 f34a2c47-ddfd-4c85-a88d-72366b69af1b
```
+  For API details, see [DeregisterTaskFromMaintenanceWindow](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.