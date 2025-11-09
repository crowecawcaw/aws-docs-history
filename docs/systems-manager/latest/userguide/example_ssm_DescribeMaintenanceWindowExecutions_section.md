AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use `DescribeMaintenanceWindowExecutions` with a CLI

The following code examples show how to use `DescribeMaintenanceWindowExecutions`.

CLI

**AWS CLI**

**Example 1: To list all executions for a maintenance window**

The following `describe-maintenance-window-executions` example lists all of the executions for the specified maintenance window.

```
`aws ssm describe-maintenance-window-executions \
 --window-id `"mw-ab12cd34eEXAMPLE"``

```

Output:

```
{
    "WindowExecutions": [
        {
            "WindowId": "mw-ab12cd34eEXAMPLE",
            "WindowExecutionId": "6027b513-64fe-4cf0-be7d-1191aEXAMPLE",
            "Status": "IN_PROGRESS",
            "StartTime": "2021-08-04T11:00:00.000000-07:00"

        },
        {
            "WindowId": "mw-ab12cd34eEXAMPLE",
            "WindowExecutionId": "ff75b750-4834-4377-8f61-b3cadEXAMPLE",
            "Status": "SUCCESS",
            "StartTime": "2021-08-03T11:00:00.000000-07:00",
            "EndTime": "2021-08-03T11:37:21.450000-07:00"
        },
        {
            "WindowId": "mw-ab12cd34eEXAMPLE",
            "WindowExecutionId": "9fac7dd9-ff21-42a5-96ad-bbc4bEXAMPLE",
            "Status": "FAILED",
            "StatusDetails": "One or more tasks in the orchestration failed.",
            "StartTime": "2021-08-02T11:00:00.000000-07:00",
            "EndTime": "2021-08-02T11:22:36.190000-07:00"
        }
    ]
}
```

**Example 2: To list all executions for a maintenance window before a specified date**

The following `describe-maintenance-window-executions` example lists all of the executions for the specified maintenance window before the specified date.

```
`aws ssm describe-maintenance-window-executions \
 --window-id `"mw-ab12cd34eEXAMPLE"` \
 --filters `"Key=ExecutedBefore,Values=2021-08-03T00:00:00Z"``

```

Output:

```
{
    "WindowExecutions": [
        {
        "WindowId": "mw-ab12cd34eEXAMPLE",
        "WindowExecutionId": "9fac7dd9-ff21-42a5-96ad-bbc4bEXAMPLE",
        "Status": "FAILED",
        "StatusDetails": "One or more tasks in the orchestration failed.",
        "StartTime": "2021-08-02T11:00:00.000000-07:00",
        "EndTime": "2021-08-02T11:22:36.190000-07:00"
    }
    ]
}
```

**Example 3: To list all executions for a maintenance window after a specified date**

The following `describe-maintenance-window-executions` example lists all of the executions for the specified maintenance window after the specified date.

```
`aws ssm describe-maintenance-window-executions \
 --window-id `"mw-ab12cd34eEXAMPLE"` \
 --filters `"Key=ExecutedAfter,Values=2021-08-04T00:00:00Z"``

```

Output:

```
{
    "WindowExecutions": [
        {
        "WindowId": "mw-ab12cd34eEXAMPLE",
        "WindowExecutionId": "6027b513-64fe-4cf0-be7d-1191aEXAMPLE",
        "Status": "IN_PROGRESS",
        "StartTime": "2021-08-04T11:00:00.000000-07:00"
        }
    ]
}
```

For more information, see [View information about tasks and task executions (AWS CLI)](mw-cli-tutorial-task-info.md "mw-cli-tutorial-task-info.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DescribeMaintenanceWindowExecutions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-executions.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-executions.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example lists all of the executions for a maintenance window.**

```
Get-SSMMaintenanceWindowExecutionList -WindowId "mw-03eb9db42890fb82d"

```

**Output:**

```
EndTime           : 2/20/2017 6:30:17 PM
StartTime         : 2/20/2017 6:30:16 PM
Status            : FAILED
StatusDetails     : One or more tasks in the orchestration failed.
WindowExecutionId : 6f3215cf-4101-4fa0-9b7b-9523269599c7
WindowId          : mw-03eb9db42890fb82d
```

**Example 2: This example lists all of the executions for a maintenance window before a specified date.**

```
$option1 = @{Key="ExecutedBefore";Values=@("2016-11-04T05:00:00Z")}
Get-SSMMaintenanceWindowExecutionList -WindowId "mw-03eb9db42890fb82d" -Filter $option1

```

**Example 3: This example lists all of the executions for a maintenance window after a specified date.**

```
$option1 = @{Key="ExecutedAfter";Values=@("2016-11-04T05:00:00Z")}
Get-SSMMaintenanceWindowExecutionList -WindowId "mw-03eb9db42890fb82d" -Filter $option1

```

- For API details, see
  [DescribeMaintenanceWindowExecutions](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example lists all of the executions for a maintenance window.**

```
Get-SSMMaintenanceWindowExecutionList -WindowId "mw-03eb9db42890fb82d"

```

**Output:**

```
EndTime           : 2/20/2017 6:30:17 PM
StartTime         : 2/20/2017 6:30:16 PM
Status            : FAILED
StatusDetails     : One or more tasks in the orchestration failed.
WindowExecutionId : 6f3215cf-4101-4fa0-9b7b-9523269599c7
WindowId          : mw-03eb9db42890fb82d
```

**Example 2: This example lists all of the executions for a maintenance window before a specified date.**

```
$option1 = @{Key="ExecutedBefore";Values=@("2016-11-04T05:00:00Z")}
Get-SSMMaintenanceWindowExecutionList -WindowId "mw-03eb9db42890fb82d" -Filter $option1

```

**Example 3: This example lists all of the executions for a maintenance window after a specified date.**

```
$option1 = @{Key="ExecutedAfter";Values=@("2016-11-04T05:00:00Z")}
Get-SSMMaintenanceWindowExecutionList -WindowId "mw-03eb9db42890fb82d" -Filter $option1

```

- For API details, see
  [DescribeMaintenanceWindowExecutions](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
