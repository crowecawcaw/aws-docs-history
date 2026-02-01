• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Use `DeregisterTaskFromMaintenanceWindow` with a CLI

The following code examples show how to use `DeregisterTaskFromMaintenanceWindow`.

CLI

**AWS CLI**

**To remove a task from a maintenance window**

The following `deregister-task-from-maintenance-window` example removes the specified task from the specified maintenance window.

```
`aws ssm deregister-task-from-maintenance-window \
 --window-id `"mw-ab12cd34ef56gh78"` \
 --window-task-id `"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d5e6c"``

```

Output:

```
{
    "WindowTaskId":"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d5e6c",
    "WindowId":"mw-ab12cd34ef56gh78"
}
```

For more information, see [Systems Manager Maintenance Windows Tutorials (AWS CLI)](maintenance-windows-tutorials.md "maintenance-windows-tutorials.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DeregisterTaskFromMaintenanceWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/deregister-task-from-maintenance-window.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/deregister-task-from-maintenance-window.html")
  in _AWS CLI Command Reference_.

PowerShell

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

- For API details, see
  [DeregisterTaskFromMaintenanceWindow](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

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

- For API details, see
  [DeregisterTaskFromMaintenanceWindow](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
