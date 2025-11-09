AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use `GetMaintenanceWindowExecution` with a CLI

The following code examples show how to use `GetMaintenanceWindowExecution`.

CLI

**AWS CLI**

**To get information about a maintenance window task execution**

The following `get-maintenance-window-execution` example lists information about a task executed as part of the specified maintenance window execution.

```
`aws ssm get-maintenance-window-execution \
 --window-execution-id `"518d5565-5969-4cca-8f0e-da3b2EXAMPLE"``

```

Output:

```
{
    "Status": "SUCCESS",
    "TaskIds": [
        "ac0c6ae1-daa3-4a89-832e-d3845EXAMPLE"
    ],
    "StartTime": 1487692834.595,
    "EndTime": 1487692835.051,
    "WindowExecutionId": "518d5565-5969-4cca-8f0e-da3b2EXAMPLE",
}
```

For more information, see [View Information About Tasks and Task Executions (AWS CLI)](mw-cli-tutorial-task-info.md "mw-cli-tutorial-task-info.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [GetMaintenanceWindowExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window-execution.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window-execution.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example lists information about a task executed as part of a maintenance window execution.**

```
Get-SSMMaintenanceWindowExecution -WindowExecutionId "518d5565-5969-4cca-8f0e-da3b2a638355"

```

**Output:**

```
EndTime           : 2/21/2017 4:00:35 PM
StartTime         : 2/21/2017 4:00:34 PM
Status            : FAILED
StatusDetails     : One or more tasks in the orchestration failed.
TaskIds           : {ac0c6ae1-daa3-4a89-832e-d384503b6586}
WindowExecutionId : 518d5565-5969-4cca-8f0e-da3b2a638355
```

- For API details, see
  [GetMaintenanceWindowExecution](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example lists information about a task executed as part of a maintenance window execution.**

```
Get-SSMMaintenanceWindowExecution -WindowExecutionId "518d5565-5969-4cca-8f0e-da3b2a638355"

```

**Output:**

```
EndTime           : 2/21/2017 4:00:35 PM
StartTime         : 2/21/2017 4:00:34 PM
Status            : FAILED
StatusDetails     : One or more tasks in the orchestration failed.
TaskIds           : {ac0c6ae1-daa3-4a89-832e-d384503b6586}
WindowExecutionId : 518d5565-5969-4cca-8f0e-da3b2a638355
```

- For API details, see
  [GetMaintenanceWindowExecution](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
