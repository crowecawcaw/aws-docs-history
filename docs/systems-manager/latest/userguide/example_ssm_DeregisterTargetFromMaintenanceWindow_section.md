• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Use `DeregisterTargetFromMaintenanceWindow` with a CLI

The following code examples show how to use `DeregisterTargetFromMaintenanceWindow`.

CLI

**AWS CLI**

**To remove a target from a maintenance window**

The following `deregister-target-from-maintenance-window` example removes the specified target from the specified maintenance window.

```
`aws ssm deregister-target-from-maintenance-window \
 --window-id `"mw-ab12cd34ef56gh78"` \
 --window-target-id `"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d-1a2"``

```

Output:

```
{
    "WindowId":"mw-ab12cd34ef56gh78",
    "WindowTargetId":"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d-1a2"
}
```

For more information, see [Update a Maintenance Window (AWS CLI)](maintenance-windows-cli-tutorials-update.md "maintenance-windows-cli-tutorials-update.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DeregisterTargetFromMaintenanceWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/deregister-target-from-maintenance-window.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/deregister-target-from-maintenance-window.html")
  in _AWS CLI Command Reference_.

PowerShell

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

- For API details, see
  [DeregisterTargetFromMaintenanceWindow](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

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

- For API details, see
  [DeregisterTargetFromMaintenanceWindow](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
