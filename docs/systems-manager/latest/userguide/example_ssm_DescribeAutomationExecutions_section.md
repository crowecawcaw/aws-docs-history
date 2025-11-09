AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use `DescribeAutomationExecutions` with a CLI

The following code examples show how to use `DescribeAutomationExecutions`.

CLI

**AWS CLI**

**To describe an automation execution**

The following `describe-automation-executions` example displays details about an Automation execution.

```
`aws ssm describe-automation-executions \
 --filters `Key=ExecutionId,Values=73c8eef8-f4ee-4a05-820c-e354fEXAMPLE``

```

Output:

```
{
    "AutomationExecutionMetadataList": [
        {
            "AutomationExecutionId": "73c8eef8-f4ee-4a05-820c-e354fEXAMPLE",
            "DocumentName": "AWS-StartEC2Instance",
            "DocumentVersion": "1",
            "AutomationExecutionStatus": "Success",
            "ExecutionStartTime": 1583737233.748,
            "ExecutionEndTime": 1583737234.719,
            "ExecutedBy": "arn:aws:sts::29884EXAMPLE:assumed-role/mw_service_role/OrchestrationService",
            "LogFile": "",
            "Outputs": {},
            "Mode": "Auto",
            "Targets": [],
            "ResolvedTargets": {
                "ParameterValues": [],
                "Truncated": false
            },
            "AutomationType": "Local"
        }
    ]
}
```

For more information, see [Running a Simple Automation Workflow](automation-working-executing.md "automation-working-executing.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DescribeAutomationExecutions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-automation-executions.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-automation-executions.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example describes all active and terminated Automation Executions associated with your account.**

```
Get-SSMAutomationExecutionList

```

**Output:**

```
AutomationExecutionId     : 4105a4fc-f944-11e6-9d32-8fb2db27a909
AutomationExecutionStatus : Failed
DocumentName              : AWS-UpdateLinuxAmi
DocumentVersion           : 1
ExecutedBy                : admin
ExecutionEndTime          : 2/22/2017 9:17:08 PM
ExecutionStartTime        : 2/22/2017 9:17:02 PM
LogFile                   :
Outputs                   : {[createImage.ImageId, Amazon.Runtime.Internal.Util.AlwaysSendList`1[System.String]]}
```

**Example 2: This example displays ExecutionID, document, execution start/end timestamp for executions with AutomationExecutionStatus other than 'Success'**

```
Get-SSMAutomationExecutionList | Where-Object AutomationExecutionStatus -ne "Success" | Select-Object AutomationExecutionId, DocumentName, AutomationExecutionStatus, ExecutionStartTime, ExecutionEndTime | Format-Table -AutoSize

```

**Output:**

```
AutomationExecutionId                DocumentName                            AutomationExecutionStatus ExecutionStartTime   ExecutionEndTime
---------------------                ------------                            ------------------------- ------------------   ----------------
e1d2bad3-4567-8901-ae23-456c7c8901be AWS-UpdateWindowsAmi                    Cancelled                 4/16/2019 5:37:04 AM 4/16/2019 5:47:29 AM
61234567-a7f8-90e1-2b34-567b8bf9012c Fixed-UpdateAmi                         Cancelled                 4/16/2019 5:33:04 AM 4/16/2019 5:40:15 AM
91234d56-7e89-0ac1-2aee-34ea5d6a7c89 AWS-UpdateWindowsAmi                    Failed                    4/16/2019 5:22:46 AM 4/16/2019 5:27:29 AM
```

- For API details, see
  [DescribeAutomationExecutions](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example describes all active and terminated Automation Executions associated with your account.**

```
Get-SSMAutomationExecutionList

```

**Output:**

```
AutomationExecutionId     : 4105a4fc-f944-11e6-9d32-8fb2db27a909
AutomationExecutionStatus : Failed
DocumentName              : AWS-UpdateLinuxAmi
DocumentVersion           : 1
ExecutedBy                : admin
ExecutionEndTime          : 2/22/2017 9:17:08 PM
ExecutionStartTime        : 2/22/2017 9:17:02 PM
LogFile                   :
Outputs                   : {[createImage.ImageId, Amazon.Runtime.Internal.Util.AlwaysSendList`1[System.String]]}
```

**Example 2: This example displays ExecutionID, document, execution start/end timestamp for executions with AutomationExecutionStatus other than 'Success'**

```
Get-SSMAutomationExecutionList | Where-Object AutomationExecutionStatus -ne "Success" | Select-Object AutomationExecutionId, DocumentName, AutomationExecutionStatus, ExecutionStartTime, ExecutionEndTime | Format-Table -AutoSize

```

**Output:**

```
AutomationExecutionId                DocumentName                            AutomationExecutionStatus ExecutionStartTime   ExecutionEndTime
---------------------                ------------                            ------------------------- ------------------   ----------------
e1d2bad3-4567-8901-ae23-456c7c8901be AWS-UpdateWindowsAmi                    Cancelled                 4/16/2019 5:37:04 AM 4/16/2019 5:47:29 AM
61234567-a7f8-90e1-2b34-567b8bf9012c Fixed-UpdateAmi                         Cancelled                 4/16/2019 5:33:04 AM 4/16/2019 5:40:15 AM
91234d56-7e89-0ac1-2aee-34ea5d6a7c89 AWS-UpdateWindowsAmi                    Failed                    4/16/2019 5:22:46 AM 4/16/2019 5:27:29 AM
```

- For API details, see
  [DescribeAutomationExecutions](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
