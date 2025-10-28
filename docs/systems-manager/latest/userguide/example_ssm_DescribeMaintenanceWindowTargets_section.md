# Use `DescribeMaintenanceWindowTargets` with a CLI

The following code examples show how to use `DescribeMaintenanceWindowTargets`.

CLI

**AWS CLI**

**Example 1: To list all targets for a Maintenance Window**

The following `describe-maintenance-window-targets` example lists all of the targets for a maintenance window.

```
`aws ssm describe-maintenance-window-targets \
 --window-id `"mw-06cf17cbefEXAMPLE"``

```

Output:

```
{
    "Targets": [
        {
            "ResourceType": "INSTANCE",
            "OwnerInformation": "Single instance",
            "WindowId": "mw-06cf17cbefEXAMPLE",
            "Targets": [
                {
                    "Values": [
                        "i-0000293ffdEXAMPLE"
                    ],
                    "Key": "InstanceIds"
                }
            ],
            "WindowTargetId": "350d44e6-28cc-44e2-951f-4b2c9EXAMPLE"
        },
        {
            "ResourceType": "INSTANCE",
            "OwnerInformation": "Two instances in a list",
            "WindowId": "mw-06cf17cbefEXAMPLE",
            "Targets": [
                {
                    "Values": [
                        "i-0000293ffdEXAMPLE",
                        "i-0cb2b964d3EXAMPLE"
                    ],
                    "Key": "InstanceIds"
                }
            ],
            "WindowTargetId": "e078a987-2866-47be-bedd-d9cf4EXAMPLE"
        }
    ]
}
```

**Example 2: To list all targets for a maintenance window matching a specific owner information value**

This `describe-maintenance-window-targets` example lists all of the targets for a maintenance window with a specific value.

```
`aws ssm describe-maintenance-window-targets \
 --window-id `"mw-0ecb1226ddEXAMPLE"` \
 --filters `"Key=OwnerInformation,Values=CostCenter1"``

```

Output:

```
{
    "Targets": [
        {
            "WindowId": "mw-0ecb1226ddEXAMPLE",
            "WindowTargetId": "da89dcc3-7f9c-481d-ba2b-edcb7d0057f9",
            "ResourceType": "INSTANCE",
            "Targets": [
                {
                    "Key": "tag:Environment",
                    "Values": [
                        "Prod"
                    ]
                }
            ],
            "OwnerInformation": "CostCenter1",
            "Name": "ProdTarget1"
        }
    ]
}
```

For more information, see [View Information About Maintenance Windows (AWS CLI)](maintenance-windows-cli-tutorials-describe.md "maintenance-windows-cli-tutorials-describe.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DescribeMaintenanceWindowTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-targets.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-targets.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example lists all of the targets for a maintenance window.**

```
Get-SSMMaintenanceWindowTarget -WindowId "mw-06cf17cbefcb4bf4f"

```

**Output:**

```
OwnerInformation : Single instance
ResourceType     : INSTANCE
Targets          : {InstanceIds}
WindowId         : mw-06cf17cbefcb4bf4f
WindowTargetId   : 350d44e6-28cc-44e2-951f-4b2c985838f6

OwnerInformation : Two instances in a list
ResourceType     : INSTANCE
Targets          : {InstanceIds}
WindowId         : mw-06cf17cbefcb4bf4f
WindowTargetId   : e078a987-2866-47be-bedd-d9cf49177d3a
```

- For API details, see
  [DescribeMaintenanceWindowTargets](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example lists all of the targets for a maintenance window.**

```
Get-SSMMaintenanceWindowTarget -WindowId "mw-06cf17cbefcb4bf4f"

```

**Output:**

```
OwnerInformation : Single instance
ResourceType     : INSTANCE
Targets          : {InstanceIds}
WindowId         : mw-06cf17cbefcb4bf4f
WindowTargetId   : 350d44e6-28cc-44e2-951f-4b2c985838f6

OwnerInformation : Two instances in a list
ResourceType     : INSTANCE
Targets          : {InstanceIds}
WindowId         : mw-06cf17cbefcb4bf4f
WindowTargetId   : e078a987-2866-47be-bedd-d9cf49177d3a
```

- For API details, see
  [DescribeMaintenanceWindowTargets](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
