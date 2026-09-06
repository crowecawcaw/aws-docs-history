

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `DescribeMaintenanceWindowExecutionTasks` with a CLI
<a name="example_ssm_DescribeMaintenanceWindowExecutionTasks_section"></a>

The following code examples show how to use `DescribeMaintenanceWindowExecutionTasks`.

------
#### [ CLI ]

**AWS CLI**  
**To list all tasks associated with a maintenance window execution**  
The following `ssm describe-maintenance-window-execution-tasks` example lists the tasks associated with the specified maintenance window execution.  

```
aws ssm describe-maintenance-window-execution-tasks \
    --window-execution-id {{"518d5565-5969-4cca-8f0e-da3b2EXAMPLE"}}
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
For more information, see [View Information About Tasks and Task Executions (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-task-info.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [DescribeMaintenanceWindowExecutionTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-execution-tasks.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

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
+  For API details, see [DescribeMaintenanceWindowExecutionTasks](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

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
+  For API details, see [DescribeMaintenanceWindowExecutionTasks](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.