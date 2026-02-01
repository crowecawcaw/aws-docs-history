• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Use `DescribeMaintenanceWindowExecutionTasks` with a CLI

The following code examples show how to use `DescribeMaintenanceWindowExecutionTasks`.

CLI

**AWS CLI**

**To list all tasks associated with a maintenance window execution**

The following `ssm describe-maintenance-window-execution-tasks` example lists the tasks associated with the specified maintenance window execution.

```
`aws ssm describe-maintenance-window-execution-tasks \
 --window-execution-id `"518d5565-5969-4cca-8f0e-da3b2EXAMPLE"``

```

Output:

```
{
    "WindowExecutionTaskIdentities": [
        {
            "Status": "SUCCESS",
            "TaskArn": "AWS-RunShellScript",
            "StartTime": 1487692834.684,
            "TaskType": "RUN_COMMAND",
            "EndTime": 1487692835.005,
            "WindowExecutionId": "518d5565-5969-4cca-8f0e-da3b2EXAMPLE",
            "TaskExecutionId": "ac0c6ae1-daa3-4a89-832e-d3845EXAMPLE"
        }
    ]
}
```

For more information, see [View Information About Tasks and Task Executions (AWS CLI)](mw-cli-tutorial-task-info.md "mw-cli-tutorial-task-info.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DescribeMaintenanceWindowExecutionTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-execution-tasks.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-execution-tasks.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example lists the tasks associated with a maintenance window execution.**

```
Get-SSMMaintenanceWindowExecutionTaskList -WindowExecutionId "518d5565-5969-4cca-8f0e-da3b2a638355"

```

**Output:**

```
EndTime           : 2/21/2017 4:00:35 PM
StartTime         : 2/21/2017 4:00:34 PM
Status            : SUCCESS
TaskArn           : AWS-RunShellScript
TaskExecutionId   : ac0c6ae1-daa3-4a89-832e-d384503b6586
TaskType          : RUN_COMMAND
WindowExecutionId : 518d5565-5969-4cca-8f0e-da3b2a638355
```

- For API details, see
  [DescribeMaintenanceWindowExecutionTasks](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example lists the tasks associated with a maintenance window execution.**

```
Get-SSMMaintenanceWindowExecutionTaskList -WindowExecutionId "518d5565-5969-4cca-8f0e-da3b2a638355"

```

**Output:**

```
EndTime           : 2/21/2017 4:00:35 PM
StartTime         : 2/21/2017 4:00:34 PM
Status            : SUCCESS
TaskArn           : AWS-RunShellScript
TaskExecutionId   : ac0c6ae1-daa3-4a89-832e-d384503b6586
TaskType          : RUN_COMMAND
WindowExecutionId : 518d5565-5969-4cca-8f0e-da3b2a638355
```

- For API details, see
  [DescribeMaintenanceWindowExecutionTasks](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
