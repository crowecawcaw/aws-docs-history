

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `StartAutomationExecution` with a CLI
<a name="example_ssm_StartAutomationExecution_section"></a>

The following code examples show how to use `StartAutomationExecution`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To execute an automation document**  
The following `start-automation-execution` example runs an Automation document.  

```
aws ssm start-automation-execution \
    --document-name {{"AWS-UpdateLinuxAmi"}} \
    --parameters {{"AutomationAssumeRole=arn:aws:iam::123456789012:role/SSMAutomationRole,SourceAmiId=ami-EXAMPLE,IamInstanceProfileName=EC2InstanceRole"}}
```
Output:  

```
{
  "AutomationExecutionId": "4105a4fc-f944-11e6-9d32-0a1b2EXAMPLE"
}
```
For more information, see [Running an Automation Workflow Manually](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing-manually.html) in the *AWS Systems Manager User Guide*.  
**Example 2: To run a shared automation document**  
The following `start-automation-execution` example runs a shared Automation document.  

```
aws ssm start-automation-execution \
    --document-name {{"arn:aws:ssm:us-east-1:123456789012:document/ExampleDocument"}}
```
Output:  

```
{
  "AutomationExecutionId": "4105a4fc-f944-11e6-9d32-0a1b2EXAMPLE"
}
```
For more information, see [Using shared SSM documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-using-shared.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [StartAutomationExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/start-automation-execution.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example runs a document specifying an Automation role, an AMI source ID, and an Amazon EC2 instance role.**  

```
Start-SSMAutomationExecution -DocumentName AWS-UpdateLinuxAmi -Parameter @{'AutomationAssumeRole'='arn:aws:iam::123456789012:role/SSMAutomationRole';'SourceAmiId'='ami-f173cc91';'InstanceIamRole'='EC2InstanceRole'}
```
**Output:**  

```
3a532a4f-0382-11e7-9df7-6f11185f6dd1
```
+  For API details, see [StartAutomationExecution](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example runs a document specifying an Automation role, an AMI source ID, and an Amazon EC2 instance role.**  

```
Start-SSMAutomationExecution -DocumentName AWS-UpdateLinuxAmi -Parameter @{'AutomationAssumeRole'='arn:aws:iam::123456789012:role/SSMAutomationRole';'SourceAmiId'='ami-f173cc91';'InstanceIamRole'='EC2InstanceRole'}
```
**Output:**  

```
3a532a4f-0382-11e7-9df7-6f11185f6dd1
```
+  For API details, see [StartAutomationExecution](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.