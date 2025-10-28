# Use `RegisterTaskWithMaintenanceWindow` with a CLI

The following code examples show how to use `RegisterTaskWithMaintenanceWindow`.

CLI

**AWS CLI**

**Example 1: To register an Automation task with a maintenance window**

The following `register-task-with-maintenance-window` example registers an Automation task with a maintenance window that is targeted at an instance.

```
`aws ssm register-task-with-maintenance-window \
 --window-id `"mw-082dcd7649EXAMPLE"` \
 --targets `Key=InstanceIds,Values=i-1234520122EXAMPLE` \
 --task-arn `AWS-RestartEC2Instance` \
 --service-role-arn `arn:aws:iam::111222333444:role/SSM` --task-type `AUTOMATION` \
 --task-invocation-parameters "{\"Automation\":{\"DocumentVersion\":\"\$LATEST\",\"Parameters\":{\"InstanceId\":[\"{{RESOURCE_ID}}\"]}}}" \
 --priority `0` \
 --max-concurrency `1` \
 --max-errors `1` \
 --name `"AutomationExample"` \
 --description `"Restarting EC2 Instance for maintenance"``

```

Output:

```
{
    "WindowTaskId":"11144444-5555-6666-7777-88888888"
}
```

For more information, see [Register a Task with the Maintenance Window (AWS CLI)](mw-cli-tutorial-tasks.md "mw-cli-tutorial-tasks.md") in the _AWS Systems Manager User Guide_.

**Example 2: To register a Lambda task with a Maintenance Window**

The following `register-task-with-maintenance-window` example registers a Lambda task with a Maintenance Window that is targeted at an instance.

```
`aws ssm register-task-with-maintenance-window \
 --window-id `"mw-082dcd7649dee04e4"` \
 --targets `Key=InstanceIds,Values=i-12344d305eEXAMPLE` \
 --task-arn `arn:aws:lambda:us-east-1:111222333444:function:SSMTestLAMBDA` \
 --service-role-arn `arn:aws:iam::111222333444:role/SSM` \
 --task-type `LAMBDA` \
 --task-invocation-parameters '`{"Lambda":{"Payload":"{\"InstanceId\":\"{{RESOURCE_ID}}\",\"targetType\":\"{{TARGET_TYPE}}\"}","Qualifier":"$LATEST"}}`' \
 --priority `0` \
 --max-concurrency `10` \
 --max-errors `5` \
 --name `"Lambda_Example"` \
 --description `"My Lambda Example"``

```

Output:

```
{
    "WindowTaskId":"22244444-5555-6666-7777-88888888"
}
```

For more information, see [Register a Task with the Maintenance Window (AWS CLI)](mw-cli-tutorial-tasks.md "mw-cli-tutorial-tasks.md") in the _AWS Systems Manager User Guide_.

**Example 3: To register a Run Command task with a maintenance window**

The following `register-task-with-maintenance-window` example registers a Run Command task with a maintenance window that is targeted at an instance.

```
`aws ssm register-task-with-maintenance-window \
 --window-id `"mw-082dcd7649dee04e4"` \
 --targets `"Key=InstanceIds,Values=i-12344d305eEXAMPLE"` \
 --service-role-arn `"arn:aws:iam::111222333444:role/SSM"` \
 --task-type `"RUN_COMMAND"` \
 --name `"SSMInstallPowerShellModule"` \
 --task-arn `"AWS-InstallPowerShellModule"` \
 --task-invocation-parameters "{\"RunCommand\":{\"Comment\":\"\",\"OutputS3BucketName\":\"runcommandlogs\",\"Parameters\":{\"commands\":[\"Get-Module -ListAvailable\"],\"executionTimeout\":[\"3600\"],\"source\":[\"https:\/\/gallery.technet.microsoft.com\/EZOut-33ae0fb7\/file\/`1``1`0351\/1\/EZOut.zip\"],\"workingDirectory\":[\"\\\\\"]},\"TimeoutSeconds\":600}}" \
 --max-concurrency 1 \
 --max-errors 1 \
 --priority `10``

```

Output:

```
{
    "WindowTaskId":"33344444-5555-6666-7777-88888888"
}
```

For more information, see [Register a Task with the Maintenance Window (AWS CLI)](mw-cli-tutorial-tasks.md "mw-cli-tutorial-tasks.md") in the _AWS Systems Manager User Guide_.

**Example 4: To register a Step Functions task with a maintenance window**

The following `register-task-with-maintenance-window` example registers a Step Functions task with a maintenance window that is targeted at an instance.

```
`aws ssm register-task-with-maintenance-window \
 --window-id `"mw-1234d787d6EXAMPLE"` \
 --targets `Key=WindowTargetIds,Values=12347414-69c3-49f8-95b8-ed2dcEXAMPLE` \
 --task-arn `arn:aws:states:us-east-1:111222333444:stateMachine:SSMTestStateMachine` \
 --service-role-arn `arn:aws:iam::111222333444:role/MaintenanceWindows` \
 --task-type `STEP_FUNCTIONS` \
 --task-invocation-parameters '`{"StepFunctions":{"Input":"{\"InstanceId\":\"{{RESOURCE_ID}}\"}"}}`' \
 --priority `0` \
 --max-concurrency `10` \
 --max-errors `5` \
 --name `"Step_Functions_Example"` \
 --description `"My Step Functions Example"``

```

Output:

```
{
    "WindowTaskId":"44444444-5555-6666-7777-88888888"
}
```

For more information, see [Register a Task with the Maintenance Window (AWS CLI)](mw-cli-tutorial-tasks.md "mw-cli-tutorial-tasks.md") in the _AWS Systems Manager User Guide_.

**Example 5: To register a task using a maintenance windows target ID**

The following `register-task-with-maintenance-window` example registers a task using a maintenance window target ID. The maintenance window target ID was in the output of the `aws ssm register-target-with-maintenance-window` command. You can also retrieve it from the output of the `aws ssm describe-maintenance-window-targets` command.

```
`aws ssm register-task-with-maintenance-window \
 --targets `"Key=WindowTargetIds,Values=350d44e6-28cc-44e2-951f-4b2c9EXAMPLE"` \
 --task-arn `"AWS-RunShellScript"` \
 --service-role-arn `"arn:aws:iam::111222333444:role/MaintenanceWindowsRole"` \
 --window-id `"mw-ab12cd34eEXAMPLE"` \
 --task-type `"RUN_COMMAND"` \
 --task-parameters "{\"commands\":{\"Values\":[\"df\"]}}" \
 --max-concurrency `1` \
 --max-errors `1` \
 --priority `10``

```

Output:

```
{
    "WindowTaskId":"33344444-5555-6666-7777-88888888"
}
```

For more information, see [Register a Task with the Maintenance Window (AWS CLI)](mw-cli-tutorial-tasks.md "mw-cli-tutorial-tasks.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [RegisterTaskWithMaintenanceWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-task-with-maintenance-window.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-task-with-maintenance-window.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example registers a task with a maintenance window using an instance ID. The output is the Task ID.**

```
$parameters = @{}
$parameterValues = New-Object Amazon.SimpleSystemsManagement.Model.MaintenanceWindowTaskParameterValueExpression
$parameterValues.Values = @("Install")
$parameters.Add("Operation", $parameterValues)

Register-SSMTaskWithMaintenanceWindow -WindowId "mw-03a342e62c96d31b0" -ServiceRoleArn "arn:aws:iam::123456789012:role/MaintenanceWindowsRole" -MaxConcurrency 1 -MaxError 1 -TaskArn "AWS-RunShellScript" -Target @{ Key="InstanceIds";Values="i-0000293ffd8c57862" } -TaskType "RUN_COMMAND" -Priority 10 -TaskParameter $parameters

```

**Output:**

```
f34a2c47-ddfd-4c85-a88d-72366b69af1b
```

**Example 2: This example registers a task with a maintenance window using a target ID. The output is the Task ID.**

```
$parameters = @{}
$parameterValues = New-Object Amazon.SimpleSystemsManagement.Model.MaintenanceWindowTaskParameterValueExpression
$parameterValues.Values = @("Install")
$parameters.Add("Operation", $parameterValues)

register-ssmtaskwithmaintenancewindow -WindowId "mw-03a342e62c96d31b0" -ServiceRoleArn "arn:aws:iam::123456789012:role/MaintenanceWindowsRole" -MaxConcurrency 1 -MaxError 1 -TaskArn "AWS-RunShellScript" -Target @{ Key="WindowTargetIds";Values="350d44e6-28cc-44e2-951f-4b2c985838f6" } -TaskType "RUN_COMMAND" -Priority 10 -TaskParameter $parameters

```

**Output:**

```
f34a2c47-ddfd-4c85-a88d-72366b69af1b
```

**Example 3: This example creates a parameter object for the run command document `AWS-RunPowerShellScript` and creates a task with given maintenance window using target ID. The return output is the task ID.**

```
$parameters = [Collections.Generic.Dictionary[String,Collections.Generic.List[String]]]::new()
$parameters.Add("commands",@("ipconfig","dir env:\computername"))
$parameters.Add("executionTimeout",@(3600))

$props = @{
    WindowId = "mw-0123e4cce56ff78ae"
    ServiceRoleArn = "arn:aws:iam::123456789012:role/MaintenanceWindowsRole"
    MaxConcurrency = 1
    MaxError = 1
    TaskType = "RUN_COMMAND"
    TaskArn = "AWS-RunPowerShellScript"
    Target = @{Key="WindowTargetIds";Values="fe1234ea-56d7-890b-12f3-456b789bee0f"}
    Priority = 1
    RunCommand_Parameter = $parameters
    Name = "set-via-cmdlet"
}

Register-SSMTaskWithMaintenanceWindow @props

```

**Output:**

```
f1e2ef34-5678-12e3-456a-12334c5c6cbe
```

**Example 4: This example registers an AWS Systems Manager Automation task by using a document named `Create-Snapshots`.**

```
$automationParameters = @{}
$automationParameters.Add( "instanceId", @("{{ TARGET_ID }}") )
$automationParameters.Add( "AutomationAssumeRole", @("{arn:aws:iam::111111111111:role/AutomationRole}") )
$automationParameters.Add( "SnapshotTimeout", @("PT20M") )
Register-SSMTaskWithMaintenanceWindow -WindowId mw-123EXAMPLE456`
    -ServiceRoleArn "arn:aws:iam::123456789012:role/MW-Role"`
    -MaxConcurrency 1 -MaxError 1 -TaskArn "CreateVolumeSnapshots"`
    -Target @{ Key="WindowTargetIds";Values="4b5acdf4-946c-4355-bd68-4329a43a5fd1" }`
    -TaskType "AUTOMATION"`
    -Priority 4`
    -Automation_DocumentVersion '$DEFAULT' -Automation_Parameter $automationParameters -Name "Create-Snapshots"

```

- For API details, see
  [RegisterTaskWithMaintenanceWindow](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example registers a task with a maintenance window using an instance ID. The output is the Task ID.**

```
$parameters = @{}
$parameterValues = New-Object Amazon.SimpleSystemsManagement.Model.MaintenanceWindowTaskParameterValueExpression
$parameterValues.Values = @("Install")
$parameters.Add("Operation", $parameterValues)

Register-SSMTaskWithMaintenanceWindow -WindowId "mw-03a342e62c96d31b0" -ServiceRoleArn "arn:aws:iam::123456789012:role/MaintenanceWindowsRole" -MaxConcurrency 1 -MaxError 1 -TaskArn "AWS-RunShellScript" -Target @{ Key="InstanceIds";Values="i-0000293ffd8c57862" } -TaskType "RUN_COMMAND" -Priority 10 -TaskParameter $parameters

```

**Output:**

```
f34a2c47-ddfd-4c85-a88d-72366b69af1b
```

**Example 2: This example registers a task with a maintenance window using a target ID. The output is the Task ID.**

```
$parameters = @{}
$parameterValues = New-Object Amazon.SimpleSystemsManagement.Model.MaintenanceWindowTaskParameterValueExpression
$parameterValues.Values = @("Install")
$parameters.Add("Operation", $parameterValues)

register-ssmtaskwithmaintenancewindow -WindowId "mw-03a342e62c96d31b0" -ServiceRoleArn "arn:aws:iam::123456789012:role/MaintenanceWindowsRole" -MaxConcurrency 1 -MaxError 1 -TaskArn "AWS-RunShellScript" -Target @{ Key="WindowTargetIds";Values="350d44e6-28cc-44e2-951f-4b2c985838f6" } -TaskType "RUN_COMMAND" -Priority 10 -TaskParameter $parameters

```

**Output:**

```
f34a2c47-ddfd-4c85-a88d-72366b69af1b
```

**Example 3: This example creates a parameter object for the run command document `AWS-RunPowerShellScript` and creates a task with given maintenance window using target ID. The return output is the task ID.**

```
$parameters = [Collections.Generic.Dictionary[String,Collections.Generic.List[String]]]::new()
$parameters.Add("commands",@("ipconfig","dir env:\computername"))
$parameters.Add("executionTimeout",@(3600))

$props = @{
    WindowId = "mw-0123e4cce56ff78ae"
    ServiceRoleArn = "arn:aws:iam::123456789012:role/MaintenanceWindowsRole"
    MaxConcurrency = 1
    MaxError = 1
    TaskType = "RUN_COMMAND"
    TaskArn = "AWS-RunPowerShellScript"
    Target = @{Key="WindowTargetIds";Values="fe1234ea-56d7-890b-12f3-456b789bee0f"}
    Priority = 1
    RunCommand_Parameter = $parameters
    Name = "set-via-cmdlet"
}

Register-SSMTaskWithMaintenanceWindow @props

```

**Output:**

```
f1e2ef34-5678-12e3-456a-12334c5c6cbe
```

**Example 4: This example registers an AWS Systems Manager Automation task by using a document named `Create-Snapshots`.**

```
$automationParameters = @{}
$automationParameters.Add( "instanceId", @("{{ TARGET_ID }}") )
$automationParameters.Add( "AutomationAssumeRole", @("{arn:aws:iam::111111111111:role/AutomationRole}") )
$automationParameters.Add( "SnapshotTimeout", @("PT20M") )
Register-SSMTaskWithMaintenanceWindow -WindowId mw-123EXAMPLE456`
    -ServiceRoleArn "arn:aws:iam::123456789012:role/MW-Role"`
    -MaxConcurrency 1 -MaxError 1 -TaskArn "CreateVolumeSnapshots"`
    -Target @{ Key="WindowTargetIds";Values="4b5acdf4-946c-4355-bd68-4329a43a5fd1" }`
    -TaskType "AUTOMATION"`
    -Priority 4`
    -Automation_DocumentVersion '$DEFAULT' -Automation_Parameter $automationParameters -Name "Create-Snapshots"

```

- For API details, see
  [RegisterTaskWithMaintenanceWindow](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
