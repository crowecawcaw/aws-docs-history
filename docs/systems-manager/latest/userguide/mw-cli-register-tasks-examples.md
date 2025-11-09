AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Examples: Register

tasks with a maintenance window

You can register a task in Run Command, a tool in AWS Systems Manager, with a
maintenance window using the AWS Command Line Interface (AWS CLI), as demonstrated in [Register tasks with the maintenance window](mw-cli-tutorial-tasks.md "mw-cli-tutorial-tasks.md"). You can also register
tasks for Systems Manager Automation workflows, AWS Lambda functions, and AWS Step Functions
tasks, as demonstrated later in this topic.

###### Note

Specify one or more targets for maintenance window Run Command-type tasks. Depending on the
task, targets are optional for other maintenance window task types (Automation, AWS Lambda,
and AWS Step Functions). For more information about running tasks that don't specify targets,
see [Registering maintenance window
tasks without targets](maintenance-windows-targetless-tasks.md "maintenance-windows-targetless-tasks.md").

In this topic, we provide examples of using the AWS Command Line Interface (AWS CLI)
command `register-task-with-maintenance-window` to register
each of the four supported task types with a maintenance window. The
examples are for demonstration only, but you can modify them to create
working task registration commands.

###### Using the --cli-input-json option

To better manage your task options, you can use the command option
`--cli-input-json`, with option values referenced in
a JSON file.

To use the sample JSON file content we provide in the following
examples, do the following on your local machine:

1. Create a file with a name such as
   `MyRunCommandTask.json`,
   `MyAutomationTask.json`, or another name
   that you prefer.
2. Copy the contents of our JSON sample into the file.
3. Modify the contents of the file for your task registration,
   and then save the file.
4. In the same directory where you stored the file, run the
   following command. Substitute your file name for
   `MyFile.json`.

Linux & macOS

```
aws ssm register-task-with-maintenance-window \
    --cli-input-json file://`MyFile.json`
```

Windows

```
aws ssm register-task-with-maintenance-window ^
    --cli-input-json file://`MyFile.json`
```

###### Pseudo parameters in maintenance window tasks

In some examples, we use _pseudo
parameters_ as the method to pass ID information to
your tasks. For instance, `{{TARGET_ID}}` and
`{{RESOURCE_ID}}` can be used to pass IDs of AWS
resources to Automation, Lambda, and Step Functions tasks. For more
information about pseudo parameters in
`--task-invocation-parameters` content, see [Using pseudo parameters
when registering maintenance window tasks](maintenance-window-tasks-pseudo-parameters.md "maintenance-window-tasks-pseudo-parameters.md").

**More info**

- [Parameter options for the
  register-task-with-maintenance-windows command](mw-cli-task-options.md "mw-cli-task-options.md").
- [register-task-with-maintenance-window](../../../cli/latest/reference/ssm/register-task-with-maintenance-window.md "../../../cli/latest/reference/ssm/register-task-with-maintenance-window.md")
  in the _AWS CLI Command Reference_
- [RegisterTaskWithMaintenanceWindow](../APIReference/API_RegisterTaskWithMaintenanceWindow.md "../APIReference/API_RegisterTaskWithMaintenanceWindow.md") in the
  _AWS Systems Manager API Reference_

## Task registration examples

The following sections provide a sample AWS CLI command for
registering a supported task type and a JSON sample that can be used
with the `--cli-input-json` option.

The following examples demonstrate how to register Systems Manager
Run Command tasks with a maintenance window using the
AWS CLI.

Linux & macOS

```
aws ssm register-task-with-maintenance-window \
    --window-id mw-0c50858d01EXAMPLE \
    --task-arn "AWS-RunShellScript" \
    --max-concurrency 1 --max-errors 1 --priority 10 \
    --targets "Key=InstanceIds,Values=i-02573cafcfEXAMPLE" \
    --task-type "RUN_COMMAND" \
    --task-invocation-parameters '{"RunCommand":{"Parameters":{"commands":["df"]}}}'
```

Windows

```
aws ssm register-task-with-maintenance-window ^
    --window-id mw-0c50858d01EXAMPLE ^
    --task-arn "AWS-RunShellScript" ^
    --max-concurrency 1 --max-errors 1 --priority 10 ^
    --targets "Key=InstanceIds,Values=i-02573cafcfEXAMPLE" ^
    --task-type "RUN_COMMAND" ^
    --task-invocation-parameters "{\"RunCommand\":{\"Parameters\":{\"commands\":[\"df\"]}}}"
```

**JSON content to use with
`--cli-input-json` file
option:**

```
{
    "TaskType": "RUN_COMMAND",
    "WindowId": "mw-0c50858d01EXAMPLE",
    "Description": "My Run Command task to update SSM Agent on an instance",
    "MaxConcurrency": "1",
    "MaxErrors": "1",
    "Name": "My-Run-Command-Task",
    "Priority": 10,
    "Targets": [
        {
            "Key": "WindowTargetIds",
            "Values": [
                "e32eecb2-646c-4f4b-8ed1-205fbEXAMPLE"
            ]
        }
    ],
    "TaskArn": "AWS-UpdateSSMAgent",
    "TaskInvocationParameters": {
        "RunCommand": {
            "Comment": "A TaskInvocationParameters test comment",
            "NotificationConfig": {
                "NotificationArn": "arn:aws:sns:`region`:123456789012:my-sns-topic-name",
                "NotificationEvents": [
                    "All"
                ],
                "NotificationType": "Invocation"
            },
            "OutputS3BucketName": "amzn-s3-demo-bucket",
            "OutputS3KeyPrefix": "`S3-PREFIX`",
            "TimeoutSeconds": 3600
        }
    }
}
```

The following examples demonstrate how to register Systems Manager
Automation tasks with a maintenance window using the AWS CLI:

**AWS CLI command:**

Linux & macOS

```
aws ssm register-task-with-maintenance-window \
    --window-id "mw-0c50858d01EXAMPLE" \
    --task-arn "AWS-RestartEC2Instance" \
    --service-role-arn arn:aws:iam::123456789012:role/MyMaintenanceWindowServiceRole \
    --task-type AUTOMATION \
    --task-invocation-parameters "Automation={DocumentVersion=5,Parameters={InstanceId='{{RESOURCE_ID}}'}}" \
    --priority 0 --name "My-Restart-EC2-Instances-Automation-Task" \
    --description "Automation task to restart EC2 instances"
```

Windows

```
aws ssm register-task-with-maintenance-window ^
    --window-id "mw-0c50858d01EXAMPLE" ^
    --task-arn "AWS-RestartEC2Instance" ^
    --service-role-arn arn:aws:iam::123456789012:role/MyMaintenanceWindowServiceRole ^
    --task-type AUTOMATION ^
    --task-invocation-parameters "Automation={DocumentVersion=5,Parameters={InstanceId='{{TARGET_ID}}'}}" ^
    --priority 0 --name "My-Restart-EC2-Instances-Automation-Task" ^
    --description "Automation task to restart EC2 instances"
```

**JSON content to use with
`--cli-input-json` file
option:**

```
{
    "WindowId": "mw-0c50858d01EXAMPLE",
        "TaskArn": "AWS-PatchInstanceWithRollback",
    "TaskType": "AUTOMATION","TaskInvocationParameters": {
        "Automation": {
            "DocumentVersion": "1",
            "Parameters": {
                "instanceId": [
                    "{{RESOURCE_ID}}"
                ]
            }
        }
    }
}
```

The following examples demonstrate how to register Lambda
function tasks with a maintenance window using the AWS CLI.

For these examples, the user who created the Lambda
function named it `SSMrestart-my-instances` and
created two parameters called `instanceId` and
`targetType`.

###### Important

The IAM policy for Maintenance Windows requires that you add the prefix `SSM` to
Lambda function (or alias) names. Before you proceed to register this type of task,
update its name in AWS Lambda to include `SSM`. For example, if your Lambda
function name is `MyLambdaFunction`, change it to
`SSMMyLambdaFunction`.

**AWS CLI command:**

Linux & macOS

###### Important

If you are using version 2 of the AWS CLI, you
must include the option `--cli-binary-format
 raw-in-base64-out` in the following command
if your Lambda payload is not base64 encoded. The
`cli_binary_format` option is available
only in version 2. For information about this and
other AWS CLI `config` file
settings, see [Supported `config` file
settings](../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-settings "../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-settings") in the
_AWS Command Line Interface User Guide_.

```
aws ssm register-task-with-maintenance-window \
    --window-id "mw-0c50858d01EXAMPLE" \
    --targets "Key=WindowTargetIds,Values=e32eecb2-646c-4f4b-8ed1-205fbEXAMPLE" \
    --priority 2 --max-concurrency 10 --max-errors 5 --name "My-Lambda-Example" \
    --description "A description for my LAMBDA example task" --task-type "LAMBDA" \
    --task-arn "arn:aws:lambda:`region`:123456789012:function:serverlessrepo-SSMrestart-my-instances-C4JF9EXAMPLE" \
    --task-invocation-parameters '{"Lambda":{"Payload":"{\"InstanceId\":\"{{RESOURCE_ID}}\",\"targetType\":\"{{TARGET_TYPE}}\"}","Qualifier": "$LATEST"}}'
```

PowerShell

###### Important

If you are using version 2 of the AWS CLI, you
must include the option `--cli-binary-format
 raw-in-base64-out` in the following command
if your Lambda payload is not base64 encoded. The
`cli_binary_format` option is available
only in version 2. For information about this and
other AWS CLI `config` file
settings, see [Supported `config` file
settings](../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-settings "../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-settings") in the
_AWS Command Line Interface User Guide_.

```
aws ssm register-task-with-maintenance-window `
    --window-id "mw-0c50858d01EXAMPLE" `
    --targets "Key=WindowTargetIds,Values=e32eecb2-646c-4f4b-8ed1-205fbEXAMPLE" `
    --priority 2 --max-concurrency 10 --max-errors 5 --name "My-Lambda-Example" `
    --description "A description for my LAMBDA example task" --task-type "LAMBDA" `
    --task-arn "arn:aws:lambda:`region`:123456789012:function:serverlessrepo-SSMrestart-my-instances-C4JF9EXAMPLE" `
    --task-invocation-parameters '{\"Lambda\":{\"Payload\":\"{\\\"InstanceId\\\":\\\"{{RESOURCE_ID}}\\\",\\\"targetType\\\":\\\"{{TARGET_TYPE}}\\\"}\",\"Qualifier\": \"$LATEST\"}}'
```

**JSON content to use with
`--cli-input-json` file
option:**

```
{
    "WindowId": "mw-0c50858d01EXAMPLE",
    "Targets": [
        {
            "Key": "WindowTargetIds",
            "Values": [
                "e32eecb2-646c-4f4b-8ed1-205fbEXAMPLE"
            ]
        }
    ],
    "TaskArn": "SSM_RestartMyInstances",
    "TaskType": "LAMBDA",
    "MaxConcurrency": "10",
    "MaxErrors": "10",
    "TaskInvocationParameters": {
        "Lambda": {
            "ClientContext": "ew0KICAi--truncated--0KIEXAMPLE",
            "Payload": "{ \"instanceId\": \"{{RESOURCE_ID}}\", \"targetType\": \"{{TARGET_TYPE}}\" }",
            "Qualifier": "$LATEST"
        }
    },
    "Name": "My-Lambda-Task",
    "Description": "A description for my LAMBDA task",
    "Priority": 5
}
```

The following examples demonstrate how to register Step Functions
state machine tasks with a maintenance window using the
AWS CLI.

###### Note

Maintenance window tasks support Step Functions Standard state
machine workflows only. They don't support Express state
machine workflows. For information about state machine
workflow types, see [Standard vs. Express Workflows](../../../step-functions/latest/dg/concepts-standard-vs-express.md "../../../step-functions/latest/dg/concepts-standard-vs-express.md") in the
_AWS Step Functions Developer Guide_.

For these examples, the user who created the Step Functions state
machine created a state machine named
`SSMMyStateMachine` with a parameter called
`instanceId`.

###### Important

The AWS Identity and Access Management (IAM) policy for Maintenance Windows requires
that you prefix Step Functions state machine names with
`SSM`. Before you proceed to register
this type of task, you must update its name in AWS Step Functions
to include `SSM`. For example, if your state
machine name is `MyStateMachine`,
change it to
`SSMMyStateMachine`.

**AWS CLI command:**

Linux & macOS

```
aws ssm register-task-with-maintenance-window \
    --window-id "mw-0c50858d01EXAMPLE" \
    --targets "Key=WindowTargetIds,Values=e32eecb2-646c-4f4b-8ed1-205fbEXAMPLE" \
    --task-arn arn:aws:states:`region`:123456789012:stateMachine:SSMMyStateMachine-MggiqEXAMPLE \
    --task-type STEP_FUNCTIONS \
    --task-invocation-parameters '{"StepFunctions":{"Input":"{\"InstanceId\":\"{{RESOURCE_ID}}\"}", "Name":"{{INVOCATION_ID}}"}}' \
    --priority 0 --max-concurrency 10 --max-errors 5 \
    --name "My-Step-Functions-Task" --description "A description for my Step Functions task"
```

PowerShell

```
aws ssm register-task-with-maintenance-window `
    --window-id "mw-0c50858d01EXAMPLE" `
    --targets "Key=WindowTargetIds,Values=e32eecb2-646c-4f4b-8ed1-205fbEXAMPLE" `
    --task-arn arn:aws:states:`region`:123456789012:stateMachine:SSMMyStateMachine-MggiqEXAMPLE `
    --task-type STEP_FUNCTIONS `
    --task-invocation-parameters '{\"StepFunctions\":{\"Input\":\"{\\\"InstanceId\\\":\\\"{{RESOURCE_ID}}\\\"}\", \"Name\":\"{{INVOCATION_ID}}\"}}' `
    --priority 0 --max-concurrency 10 --max-errors 5 `
    --name "My-Step-Functions-Task" --description "A description for my Step Functions task"
```

**JSON content to use with
`--cli-input-json` file
option:**

```
{
    "WindowId": "mw-0c50858d01EXAMPLE",
    "Targets": [
        {
            "Key": "WindowTargetIds",
            "Values": [
                "e32eecb2-646c-4f4b-8ed1-205fbEXAMPLE"
            ]
        }
    ],
    "TaskArn": "SSM_MyStateMachine",
    "TaskType": "STEP_FUNCTIONS",
    "MaxConcurrency": "10",
    "MaxErrors": "10",
    "TaskInvocationParameters": {
        "StepFunctions": {
            "Input": "{ \"instanceId\": \"{{TARGET_ID}}\" }",
            "Name": "{{INVOCATION_ID}}"
        }
    },
    "Name": "My-Step-Functions-Task",
    "Description": "A description for my Step Functions task",
    "Priority": 5
}
```
