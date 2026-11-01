

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
    --automation-execution-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
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
            "StepExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "OverriddenParameters": {}
        }
    ]
}
```
**Example 2: To describe a specific step for an automation execution**  
The following `describe-automation-step-executions` example displays details about a specific step of an Automation execution.  

```
aws ssm describe-automation-step-executions \
    --automation-execution-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --filters {{Key=StepExecutionId,Values=a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}}
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
            "StepExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "OverriddenParameters": {}
        }
    ]
}
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