AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use `RegisterTargetWithMaintenanceWindow` with a CLI

The following code examples show how to use `RegisterTargetWithMaintenanceWindow`.

CLI

**AWS CLI**

**Example 1: To register a single target with a maintenance window**

The following `register-target-with-maintenance-window` example registers an instance with a maintenance window.

```
`aws ssm register-target-with-maintenance-window \
 --window-id `"mw-ab12cd34ef56gh78"` \
 --target `"Key=InstanceIds,Values=i-0000293ffd8c57862"` \
 --owner-information `"Single instance"` \
 --resource-type `"INSTANCE"``

```

Output:

```
{
    "WindowTargetId":"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d-1a2"
}
```

**Example 2: To register multiple targets with a maintenance window using instance IDs**

The following `register-target-with-maintenance-window` example registers two instances with a maintenance window by specifying their instance IDs.

```
`aws ssm register-target-with-maintenance-window \
 --window-id `"mw-ab12cd34ef56gh78"` \
 --target `"Key=InstanceIds,Values=i-0000293ffd8c57862,i-0cb2b964d3e14fd9f"` \
 --owner-information `"Two instances in a list"` \
 --resource-type `"INSTANCE"``

```

Output:

```
{
    "WindowTargetId":"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d-1a2"
}
```

**Example 3: To register targets with a maintenance window using resource tags**

The following `register-target-with-maintenance-window` example registers instances with a maintenance window by specifying resource tags that have been applied to the instances.

```
`aws ssm register-target-with-maintenance-window \
 --window-id `"mw-06cf17cbefcb4bf4f"` \
 --targets `"Key=tag:Environment,Values=Prod"` `"Key=Role,Values=Web"` \
 --owner-information `"Production Web Servers"` \
 --resource-type `"INSTANCE"``

```

Output:

```
{
    "WindowTargetId":"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d-1a2"
}
```

**Example 4: To register targets using a group of tag keys**

The following `register-target-with-maintenance-window` example register instances that all have one or more tag keys assigned to them, regardless of their key values.

```
`aws ssm register-target-with-maintenance-window \
 --window-id `"mw-0c50858d01EXAMPLE"` \
 --resource-type `"INSTANCE"` \
 --target `"Key=tag-key,Values=Name,Instance-Type,CostCenter"``

```

Output:

```
{
    "WindowTargetId":"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d-1a2"
}
```

**Example 5: To register targets using a resource group name**

The following `register-target-with-maintenance-window` example register a specified resource group, regardless of the type of resources it contains.

```
`aws ssm register-target-with-maintenance-window \
 --window-id `"mw-0c50858d01EXAMPLE"` \
 --resource-type `"RESOURCE_GROUP"` \
 --target `"Key=resource-groups:Name,Values=MyResourceGroup"``

```

Output:

```
{
    "WindowTargetId":"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d-1a2"
}
```

For more information, see [Register a Target Instance with the Maintenance Window (AWS CLI)](mw-cli-tutorial-targets.md "mw-cli-tutorial-targets.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [RegisterTargetWithMaintenanceWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-target-with-maintenance-window.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-target-with-maintenance-window.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example registers an instance with a maintenance window.**

```
$option1 = @{Key="InstanceIds";Values=@("i-0000293ffd8c57862")}
Register-SSMTargetWithMaintenanceWindow -WindowId "mw-06cf17cbefcb4bf4f" -Target $option1 -OwnerInformation "Single instance" -ResourceType "INSTANCE"

```

**Output:**

```
d8e47760-23ed-46a5-9f28-927337725398
```

**Example 2: This example registers multiple instances with a maintenance window.**

```
$option1 = @{Key="InstanceIds";Values=@("i-0000293ffd8c57862","i-0cb2b964d3e14fd9f")}
Register-SSMTargetWithMaintenanceWindow -WindowId "mw-06cf17cbefcb4bf4f" -Target $option1 -OwnerInformation "Single instance" -ResourceType "INSTANCE"

```

**Output:**

```
6ab5c208-9fc4-4697-84b7-b02a6cc25f7d
```

**Example 3: This example registers an instance with a maintenance window using EC2 tags.**

```
$option1 = @{Key="tag:Environment";Values=@("Production")}
Register-SSMTargetWithMaintenanceWindow -WindowId "mw-06cf17cbefcb4bf4f" -Target $option1 -OwnerInformation "Production Web Servers" -ResourceType "INSTANCE"

```

**Output:**

```
2994977e-aefb-4a71-beac-df620352f184
```

- For API details, see
  [RegisterTargetWithMaintenanceWindow](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example registers an instance with a maintenance window.**

```
$option1 = @{Key="InstanceIds";Values=@("i-0000293ffd8c57862")}
Register-SSMTargetWithMaintenanceWindow -WindowId "mw-06cf17cbefcb4bf4f" -Target $option1 -OwnerInformation "Single instance" -ResourceType "INSTANCE"

```

**Output:**

```
d8e47760-23ed-46a5-9f28-927337725398
```

**Example 2: This example registers multiple instances with a maintenance window.**

```
$option1 = @{Key="InstanceIds";Values=@("i-0000293ffd8c57862","i-0cb2b964d3e14fd9f")}
Register-SSMTargetWithMaintenanceWindow -WindowId "mw-06cf17cbefcb4bf4f" -Target $option1 -OwnerInformation "Single instance" -ResourceType "INSTANCE"

```

**Output:**

```
6ab5c208-9fc4-4697-84b7-b02a6cc25f7d
```

**Example 3: This example registers an instance with a maintenance window using EC2 tags.**

```
$option1 = @{Key="tag:Environment";Values=@("Production")}
Register-SSMTargetWithMaintenanceWindow -WindowId "mw-06cf17cbefcb4bf4f" -Target $option1 -OwnerInformation "Production Web Servers" -ResourceType "INSTANCE"

```

**Output:**

```
2994977e-aefb-4a71-beac-df620352f184
```

- For API details, see
  [RegisterTargetWithMaintenanceWindow](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
