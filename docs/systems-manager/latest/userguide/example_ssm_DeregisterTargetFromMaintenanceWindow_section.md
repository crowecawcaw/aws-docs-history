

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `DeregisterTargetFromMaintenanceWindow` with a CLI
<a name="example_ssm_DeregisterTargetFromMaintenanceWindow_section"></a>

The following code examples show how to use `DeregisterTargetFromMaintenanceWindow`.

------
#### [ CLI ]

**AWS CLI**  
**To remove a target from a maintenance window**  
The following `deregister-target-from-maintenance-window` example removes the specified target from the specified maintenance window.  

```
aws ssm deregister-target-from-maintenance-window \
    --window-id {{"mw-ab12cd34ef56gh78"}} \
    --window-target-id {{"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d-1a2"}}
```
Output:  

```
{
    "WindowId":"mw-ab12cd34ef56gh78",
    "WindowTargetId":"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d-1a2"
}
```
For more information, see [Update a Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-update.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [DeregisterTargetFromMaintenanceWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/deregister-target-from-maintenance-window.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example removes a target from a maintenance window.**  

```
Unregister-SSMTargetFromMaintenanceWindow -WindowTargetId "6ab5c208-9fc4-4697-84b7-b02a6cc25f7d" -WindowId "mw-06cf17cbefcb4bf4f"
```
**Output:**  

```
WindowId             WindowTargetId
--------             --------------
mw-06cf17cbefcb4bf4f 6ab5c208-9fc4-4697-84b7-b02a6cc25f7d
```
+  For API details, see [DeregisterTargetFromMaintenanceWindow](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example removes a target from a maintenance window.**  

```
Unregister-SSMTargetFromMaintenanceWindow -WindowTargetId "6ab5c208-9fc4-4697-84b7-b02a6cc25f7d" -WindowId "mw-06cf17cbefcb4bf4f"
```
**Output:**  

```
WindowId             WindowTargetId
--------             --------------
mw-06cf17cbefcb4bf4f 6ab5c208-9fc4-4697-84b7-b02a6cc25f7d
```
+  For API details, see [DeregisterTargetFromMaintenanceWindow](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.