# Use `GetMaintenanceWindow` with a CLI

The following code examples show how to use `GetMaintenanceWindow`.

CLI

**AWS CLI**

**To get information about a maintenance window**

The following `get-maintenance-window` example retrieves details about the specified maintenance window.

```
`aws ssm get-maintenance-window \
 --window-id `"mw-03eb9db428EXAMPLE"``

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

For more information, see [View information about maintenance windows (AWS CLI)](maintenance-windows-cli-tutorials-describe.md "maintenance-windows-cli-tutorials-describe.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [GetMaintenanceWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window.html")
  in _AWS CLI Command Reference_.

PowerShell

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

- For API details, see
  [GetMaintenanceWindow](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

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

- For API details, see
  [GetMaintenanceWindow](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
