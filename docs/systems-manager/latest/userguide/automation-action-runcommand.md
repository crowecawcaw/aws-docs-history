# `aws:runCommand` – Run

a command on a managed instance

Runs the specified commands.

###### Note

Automation only supports _output_ of one AWS Systems Manager Run Command
action. A runbook can include multiple Run Command actions, but output is supported for
only one action at a time.

###### Input

This action supports most send command parameters. For more information, see
[SendCommand](../APIReference/API_SendCommand.md "../APIReference/API_SendCommand.md").

YAML

```
- name: checkMembership
  action: 'aws:runCommand'
  inputs:
    DocumentName: AWS-RunPowerShellScript
    InstanceIds:
      - '{{InstanceIds}}'
    Parameters:
      commands:
        - (Get-WmiObject -Class Win32_ComputerSystem).PartOfDomain
```

JSON

```
{
    "name": "checkMembership",
    "action": "aws:runCommand",
    "inputs": {
        "DocumentName": "AWS-RunPowerShellScript",
        "InstanceIds": [
            "{{InstanceIds}}"
        ],
        "Parameters": {
            "commands": [
                "(Get-WmiObject -Class Win32_ComputerSystem).PartOfDomain"
            ]
        }
    }
}
```

DocumentName

If the Command type document is owned by you or AWS, specify the name of
the document. If you're using a document shared with you by a different
AWS account, specify the Amazon Resource Name (ARN) of the document. For
more information about using shared documents, see [Using shared SSM documents](documents-ssm-sharing.md#using-shared-documents "documents-ssm-sharing.md#using-shared-documents").

Type: String

Required: Yes

InstanceIds

The instance IDs where you want the command to run. You can specify a
maximum of 50 IDs.

You can also use the pseudo parameter `{{RESOURCE_ID}}` in
place of instance IDs to run the command on all instances in the target
group. For more information about pseudo parameters, see [Using pseudo parameters
when registering maintenance window tasks](maintenance-window-tasks-pseudo-parameters.md "maintenance-window-tasks-pseudo-parameters.md").

Another alternative is to send commands to a fleet of instances by using
the `Targets` parameter. The `Targets` parameter
accepts Amazon Elastic Compute Cloud (Amazon EC2) tags. For more information about how to use the
`Targets` parameter, see [Run commands at scale](send-commands-multiple.md "send-commands-multiple.md").

Type: StringList

Required: No (If you don't specify InstanceIds or use the
`{{RESOURCE_ID}}` pseudo parameter, then you must specify the
`Targets` parameter.)

Targets

An array of search criteria that targets instances by using a Key,Value
combination that you specify. `Targets` is required if you don't
provide one or more instance IDs in the call. For more information about how
to use the `Targets` parameter, see [Run commands at scale](send-commands-multiple.md "send-commands-multiple.md").

Type: MapList (The schema of the map in the list must match the object.)
For information, see [Target](../APIReference/API_Target.md "../APIReference/API_Target.md") in the _AWS Systems Manager API Reference_.

Required: No (If you don't specify `Targets`, then you must
specify InstanceIds or use the `{{RESOURCE_ID}}` pseudo
parameter.)

Following is an example.

YAML

```
- name: checkMembership
  action: aws:runCommand
  inputs:
    DocumentName: AWS-RunPowerShellScript
    Targets:
      - Key: tag:Stage
        Values:
          - Gamma
          - Beta
      - Key: tag-key
        Values:
          - Suite
    Parameters:
      commands:
        - (Get-WmiObject -Class Win32_ComputerSystem).PartOfDomain
```

JSON

```
{
    "name": "checkMembership",
    "action": "aws:runCommand",
    "inputs": {
        "DocumentName": "AWS-RunPowerShellScript",
        "Targets": [
            {
                "Key": "tag:Stage",
                "Values": [
                    "Gamma", "Beta"
                ]
            },
            {
                "Key": "tag:Application",
                "Values": [
                    "Suite"
                ]
            }
        ],
        "Parameters": {
            "commands": [
                "(Get-WmiObject -Class Win32_ComputerSystem).PartOfDomain"
            ]
        }
    }
}
```

Parameters

The required and optional parameters specified in the document.

Type: Map

Required: No

CloudWatchOutputConfig

Configuration options for sending command output to Amazon CloudWatch Logs. For more
information about sending command output to CloudWatch Logs, see [Configuring Amazon CloudWatch Logs for Run Command](sysman-rc-setting-up-cwlogs.md "sysman-rc-setting-up-cwlogs.md").

Type: StringMap (The schema of the map must match the object. For more
information, see [CloudWatchOutputConfig](../APIReference/API_CloudWatchOutputConfig.md "../APIReference/API_CloudWatchOutputConfig.md") in the
_AWS Systems Manager API Reference_).

Required: No

Following is an example.

YAML

```
- name: checkMembership
  action: aws:runCommand
  inputs:
    DocumentName: AWS-RunPowerShellScript
    InstanceIds:
      - "{{InstanceIds}}"
    Parameters:
      commands:
        - "(Get-WmiObject -Class Win32_ComputerSystem).PartOfDomain"
    CloudWatchOutputConfig:
      CloudWatchLogGroupName: CloudWatchGroupForSSMAutomationService
      CloudWatchOutputEnabled: true
```

JSON

```
{
    "name": "checkMembership",
    "action": "aws:runCommand",
    "inputs": {
        "DocumentName": "AWS-RunPowerShellScript",
        "InstanceIds": [
            "{{InstanceIds}}"
        ],
        "Parameters": {
            "commands": [
                "(Get-WmiObject -Class Win32_ComputerSystem).PartOfDomain"
            ]
        },
        "CloudWatchOutputConfig" : {
                "CloudWatchLogGroupName": "CloudWatchGroupForSSMAutomationService",
                "CloudWatchOutputEnabled": true
        }
    }
}
```

Comment

User-defined information about the command.

Type: String

Required: No

DocumentHash

The hash for the document.

Type: String

Required: No

DocumentHashType

The type of the hash.

Type: String

Valid values: `Sha256` | `Sha1`

Required: No

NotificationConfig

The configurations for sending notifications.

Required: No

OutputS3BucketName

The name of the S3 bucket for command output responses. Your managed node
must have permissions for the S3 bucket to successfully log output.

Type: String

Required: No

OutputS3KeyPrefix

The prefix.

Type: String

Required: No

ServiceRoleArn

The ARN of the AWS Identity and Access Management (IAM) role.

Type: String

Required: No

TimeoutSeconds

The amount of time in seconds to wait for a command to deliver to the
AWS Systems Manager SSM Agent on an instance. If the command isn't received by the
SSM Agent on the instance before the value specified is reached, then the
status of the command changes to `Delivery Timed Out`.

Type: Integer

Required: No

Valid values: 30-2592000

###### Output

CommandId

The ID of the command.

Status

The status of the command.

ResponseCode

The response code of the command. If the document you run has more than 1
step, a value isn't returned for this output.

Output

The output of the command. If you target a tag or multiple instances with
your command, no output value is returned. You can use the
`GetCommandInvocation` and
`ListCommandInvocations` API operations to retrieve output
for individual instances.
