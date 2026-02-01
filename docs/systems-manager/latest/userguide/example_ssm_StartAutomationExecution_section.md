• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Use `StartAutomationExecution` with a CLI

The following code examples show how to use `StartAutomationExecution`.

CLI

**AWS CLI**

**Example 1: To execute an automation document**

The following `start-automation-execution` example runs an Automation document.

```
`aws ssm start-automation-execution \
 --document-name `"AWS-UpdateLinuxAmi"` \
 --parameters `"AutomationAssumeRole=arn:aws:iam::123456789012:role/SSMAutomationRole,SourceAmiId=ami-EXAMPLE,IamInstanceProfileName=EC2InstanceRole"``

```

Output:

```
{
  "AutomationExecutionId": "4105a4fc-f944-11e6-9d32-0a1b2EXAMPLE"
}
```

For more information, see [Running an Automation Workflow Manually](automation-working-executing-manually.md "automation-working-executing-manually.md") in the _AWS Systems Manager User Guide_.

**Example 2: To run a shared automation document**

The following `start-automation-execution` example runs a shared Automation document.

```
`aws ssm start-automation-execution \
 --document-name `"arn:aws:ssm:us-east-1:123456789012:document/ExampleDocument"``

```

Output:

```
{
  "AutomationExecutionId": "4105a4fc-f944-11e6-9d32-0a1b2EXAMPLE"
}
```

For more information, see [Using shared SSM documents](ssm-using-shared.md "ssm-using-shared.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [StartAutomationExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/start-automation-execution.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/start-automation-execution.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example runs a document specifying an Automation role, an AMI source ID, and an Amazon EC2 instance role.**

```
Start-SSMAutomationExecution -DocumentName AWS-UpdateLinuxAmi -Parameter @{'AutomationAssumeRole'='arn:aws:iam::123456789012:role/SSMAutomationRole';'SourceAmiId'='ami-f173cc91';'InstanceIamRole'='EC2InstanceRole'}

```

**Output:**

```
3a532a4f-0382-11e7-9df7-6f11185f6dd1
```

- For API details, see
  [StartAutomationExecution](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example runs a document specifying an Automation role, an AMI source ID, and an Amazon EC2 instance role.**

```
Start-SSMAutomationExecution -DocumentName AWS-UpdateLinuxAmi -Parameter @{'AutomationAssumeRole'='arn:aws:iam::123456789012:role/SSMAutomationRole';'SourceAmiId'='ami-f173cc91';'InstanceIamRole'='EC2InstanceRole'}

```

**Output:**

```
3a532a4f-0382-11e7-9df7-6f11185f6dd1
```

- For API details, see
  [StartAutomationExecution](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
