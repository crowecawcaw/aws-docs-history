# Use `DescribeMaintenanceWindows` with a CLI

The following code examples show how to use `DescribeMaintenanceWindows`.

CLI

**AWS CLI**

**Example 1: To list all maintenance windows**

The following `describe-maintenance-windows` example lists all maintenance windows in your AWS account in the current Region.

```
`aws ssm describe-maintenance-windows`

```

Output:

```
{
    "WindowIdentities": [
        {
            "WindowId": "mw-0ecb1226ddEXAMPLE",
            "Name": "MyMaintenanceWindow-1",
            "Enabled": true,
            "Duration": 2,
            "Cutoff": 1,
            "Schedule": "rate(180 minutes)",
            "NextExecutionTime": "2020-02-12T23:19:20.596Z"
        },
        {
            "WindowId": "mw-03eb9db428EXAMPLE",
            "Name": "MyMaintenanceWindow-2",
            "Enabled": true,
            "Duration": 3,
            "Cutoff": 1,
            "Schedule": "rate(7 days)",
            "NextExecutionTime": "2020-02-17T23:22:00.956Z"
        },
    ]
}
```

**Example 2: To list all enabled maintenance windows**

The following `describe-maintenance-windows` example lists all enabled maintenance windows.

```
`aws ssm describe-maintenance-windows \
 --filters `"Key=Enabled,Values=true"``

```

**Example 3: To list maintenance windows matching a specific name**

This `describe-maintenance-windows` example lists all maintenance windows with the specified name.

```
`aws ssm describe-maintenance-windows \
 --filters `"Key=Name,Values=MyMaintenanceWindow"``

```

For more information, see [View Information About Maintenance Windows (AWS CLI)](maintenance-windows-cli-tutorials-describe.md "maintenance-windows-cli-tutorials-describe.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DescribeMaintenanceWindows](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-windows.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-windows.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example lists all maintenance windows on your account.**

```
Get-SSMMaintenanceWindowList

```

**Output:**

```
Cutoff   : 1
Duration : 4
Enabled  : True
Name     : My-First-Maintenance-Window
WindowId : mw-06d59c1a07c022145
```

- For API details, see
  [DescribeMaintenanceWindows](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example lists all maintenance windows on your account.**

```
Get-SSMMaintenanceWindowList

```

**Output:**

```
Cutoff   : 1
Duration : 4
Enabled  : True
Name     : My-First-Maintenance-Window
WindowId : mw-06d59c1a07c022145
```

- For API details, see
  [DescribeMaintenanceWindows](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
