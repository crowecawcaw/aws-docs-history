

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `StopAutomationExecution` with a CLI
<a name="example_ssm_StopAutomationExecution_section"></a>

The following code examples show how to use `StopAutomationExecution`.

------
#### [ CLI ]

**AWS CLI**  
**To stop an automation execution**  
The following `stop-automation-execution` example stops an Automation document.  

```
aws ssm stop-automation-execution
    --automation-execution-id {{"4105a4fc-f944-11e6-9d32-0a1b2EXAMPLE"}}
```
This command produces no output.  
For more information, see [Running an Automation Workflow Manually](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing-manually.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [StopAutomationExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/stop-automation-execution.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example stops an Automation Execution. There is no output if the command succeeds.**  

```
Stop-SSMAutomationExecution -AutomationExecutionId "4105a4fc-f944-11e6-9d32-8fb2db27a909"
```
+  For API details, see [StopAutomationExecution](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example stops an Automation Execution. There is no output if the command succeeds.**  

```
Stop-SSMAutomationExecution -AutomationExecutionId "4105a4fc-f944-11e6-9d32-8fb2db27a909"
```
+  For API details, see [StopAutomationExecution](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.