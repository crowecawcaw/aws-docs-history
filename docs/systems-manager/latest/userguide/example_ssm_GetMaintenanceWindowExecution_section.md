

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `GetMaintenanceWindowExecution` with a CLI
<a name="example_ssm_GetMaintenanceWindowExecution_section"></a>

The following code examples show how to use `GetMaintenanceWindowExecution`.

------
#### [ CLI ]

**AWS CLI**  
**To get information about a maintenance window task execution**  
The following `get-maintenance-window-execution` example lists information about a task executed as part of the specified maintenance window execution.  

```
aws ssm get-maintenance-window-execution \
    --window-execution-id {{"518d5565-5969-4cca-8f0e-da3b2EXAMPLE"}}
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
For more information, see [View Information About Tasks and Task Executions (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-task-info.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [GetMaintenanceWindowExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window-execution.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

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
+  For API details, see [GetMaintenanceWindowExecution](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

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
+  For API details, see [GetMaintenanceWindowExecution](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.