

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `DescribeAutomationStepExecutions` with a CLI
<a name="example_ssm_DescribeAutomationStepExecutions_section"></a>

The following code examples show how to use `DescribeAutomationStepExecutions`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To describe all steps for an automation execution**  
The following `describe-automation-step-executions` example displays details about the steps of an Automation execution.  

```
aws ssm describe-automation-step-executions \
    --automation-execution-id {{73c8eef8-f4ee-4a05-820c-e354fEXAMPLE}}
```
Output:  

```
{
    "StepExecutions": [
        {
            "StepName": "startInstances",
            "Action": "aws:changeInstanceState",
            "ExecutionStartTime": 1583737234.134,
            "ExecutionEndTime": 1583737234.672,
            "StepStatus": "Success",
            "Inputs": {
                "DesiredState": "\"running\"",
                "InstanceIds": "[\"i-0cb99161f6EXAMPLE\"]"
            },
            "Outputs": {
                "InstanceStates": [
                    "running"
                ]
            },
            "StepExecutionId": "95e70479-cf20-4d80-8018-7e4e2EXAMPLE",
            "OverriddenParameters": {}
        }
    ]
}
```
**Example 2: To describe a specific step for an automation execution**  
The following `describe-automation-step-executions` example displays details about a specific step of an Automation execution.  

```
aws ssm describe-automation-step-executions \
    --automation-execution-id {{73c8eef8-f4ee-4a05-820c-e354fEXAMPLE}} \
    --filters {{Key=StepExecutionId,Values=95e70479-cf20-4d80-8018-7e4e2EXAMPLE}}
```
For more information, see [Running an Automation Workflow Step by Step (Command Line)](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing-manually.html#automation-working-executing-manually-commandline) in the *AWS Systems Manager User Guide*.  
+  For API details, see [DescribeAutomationStepExecutions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-automation-step-executions.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This exmaple displays information about all active and terminated step executions in an Automation workflow.**  

```
Get-SSMAutomationStepExecution -AutomationExecutionId e1d2bad3-4567-8901-ae23-456c7c8901be | Select-Object StepName, Action, StepStatus
```
**Output:**  

```
StepName                  Action                  StepStatus
--------                  ------                  ----------
LaunchInstance            aws:runInstances        Success
OSCompatibilityCheck      aws:runCommand          Success
RunPreUpdateScript        aws:runCommand          Success
UpdateEC2Config           aws:runCommand          Cancelled
UpdateSSMAgent            aws:runCommand          Pending
UpdateAWSPVDriver         aws:runCommand          Pending
UpdateAWSEnaNetworkDriver aws:runCommand          Pending
UpdateAWSNVMe             aws:runCommand          Pending
InstallWindowsUpdates     aws:runCommand          Pending
RunPostUpdateScript       aws:runCommand          Pending
RunSysprepGeneralize      aws:runCommand          Pending
StopInstance              aws:changeInstanceState Pending
CreateImage               aws:createImage         Pending
TerminateInstance         aws:changeInstanceState Pending
```
+  For API details, see [DescribeAutomationStepExecutions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This exmaple displays information about all active and terminated step executions in an Automation workflow.**  

```
Get-SSMAutomationStepExecution -AutomationExecutionId e1d2bad3-4567-8901-ae23-456c7c8901be | Select-Object StepName, Action, StepStatus
```
**Output:**  

```
StepName                  Action                  StepStatus
--------                  ------                  ----------
LaunchInstance            aws:runInstances        Success
OSCompatibilityCheck      aws:runCommand          Success
RunPreUpdateScript        aws:runCommand          Success
UpdateEC2Config           aws:runCommand          Cancelled
UpdateSSMAgent            aws:runCommand          Pending
UpdateAWSPVDriver         aws:runCommand          Pending
UpdateAWSEnaNetworkDriver aws:runCommand          Pending
UpdateAWSNVMe             aws:runCommand          Pending
InstallWindowsUpdates     aws:runCommand          Pending
RunPostUpdateScript       aws:runCommand          Pending
RunSysprepGeneralize      aws:runCommand          Pending
StopInstance              aws:changeInstanceState Pending
CreateImage               aws:createImage         Pending
TerminateInstance         aws:changeInstanceState Pending
```
+  For API details, see [DescribeAutomationStepExecutions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.