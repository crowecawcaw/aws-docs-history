# Create and manage commands

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

You can configure reusable remote actions or send one-time, immediate instructions to your
devices. When you use this feature, you can specify the instructions that your devices can
execute in near real time. A command enables you to configure resuable remote actions for
your target vehicle. After you create a command, you can start a command execution that
targets a specific vehicle.

This topic shows how you can create and manage a command resource using the AWS IoT Core API
or the AWS CLI. It shows you how to perform the following actions on a command
resource.

###### Topics

- [Create a command resource](#create-remote-command-cli "#create-remote-command-cli")
- [Retrieve information about a command](#get-remote-command-cli "#get-remote-command-cli")
- [List commands in your account](#list-remote-command-cli "#list-remote-command-cli")
- [Update or deprecate a command
  resource](#update-remote-command-cli "#update-remote-command-cli")
- [Delete a command resource](#delete-remote-command-cli "#delete-remote-command-cli")

## Create a command resource

You can use the [`CreateCommand`](../../../iot/latest/apireference/API_CreateCommand.md "../../../iot/latest/apireference/API_CreateCommand.md") AWS IoT Core control plane API operation or the AWS IoT FleetWise console to create a command.

You can use the AWS IoT FleetWise console to create a command.

###### To create a command

1. Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise "https://console.aws.amazon.com/iotfleetwise").
2. On the navigation pane, choose **Commands**.
3. Choose **Create command**.
4. Specify a unique command ID to help you identify the command that you want to run on the vehicle.
5. (Optional) Specify an optional display name and description.
6. (Optional) Select the actuator and default parameter value. Parameters specify the actions the target vehicle can perform upon receiving the command. If you don't add parameters, you will need to provide them when running the command.
7. Choose an IAM role that grants permissions to generate the payload for commands. See [Controlling access](controlling-access.md#generate-command-payload "controlling-access.md#generate-command-payload").
8. Choose **Create command**.

The following example shows how to create a command with a
parameter.

#### Considerations when creating

a command

When you create a command in AWS IoT FleetWise:

- You must specify the `roleArn` that grants permission to create
  and run commands on your vehicle. For more information and about sample
  policies including when KMS keys are enabled, see [Grant AWS IoT Device Management permission to generate the
  payload for commands with AWS IoT FleetWise](controlling-access.md#generate-command-payload "controlling-access.md#generate-command-payload").
- You must specify `AWS-IoT-FleetWise` as the namespace.
- You can skip the `mandatory-parameters` field and specify them
  at run time instead. Alternatively, you can create a command with
  parameters, and optionally specify default values for them. If you specified
  default values, then at run time, you can use these values or override them
  by specifying your own values. For these additional examples, see [Command usage scenarios](remote-command-use-cases.md "remote-command-use-cases.md").
- You can specify up to three name-value pairs for the
  `mandatory-parameters` field. However, when executing the
  command on the vehicle, only one name-value pair is accepted, and the
  `name` field must use the fully qualified name with the
  `$actuatorPath.` prefix.

- Replace `command-id` with a unique identifier for
  the command. You can use UUID, alphanumeric characters, "-", and "\_".
- Replace `role-arn` with the IAM role that
  grants you permission to create and run commands, for example,
  `"arn:aws:iam:`accountId`:role/`FwCommandExecutionRole`"`.
- (Optional) Replace `display-name` with a
  user-friendly name for the command, and
  `description` with a meaningful description of
  the command.
- Replace `name` and
  `value` of the
  `mandatory-parameters` object with the required information
  for the command being created. The `name` field is the fully
  qualified name as defined in the signal catalog with
  `$actuatorPath.` as the prefix. For example,
  `name` can be
  `$actuatorPath.Vehicle.Chassis.SteeringWheel.HandsOff.HandsOffSteeringMode`
  and `value` can be a boolean that indicates a steering mode
  status like `{"B": false}`.

```
aws iot create-command --command-id `command-id` \
    --role-arn `role-arn` \
    --description `description` \
    --display-name `display-name` \
    --namespace "AWS-IoT-FleetWise" \
    --mandatory-parameters '[
        {
            "name": `name`,
            "value": `value`
        }
   ]'
```

The `CreateCommand` API operation returns a response that contains the
ID and ARN (Amazon Resource Name) of the command.

```
{
    "commandId": "HandsOffSteeringMode",
    "commandArn": "arn:aws:iot:ap-south-1:123456789012:command/HandsOffSteeringMode"
}
```

## Retrieve information about a command

You can use the [`GetCommand`](../../../iot/latest/apireference/API_GetCommand.md "../../../iot/latest/apireference/API_GetCommand.md")
AWS IoT Core control plane API operation to retrieve information about a command
resource.

To get information about a command resource, run the following command. Replace
`command-id` with the identifier that was used when
creating the command.

```
aws iot get-command --command-id `command-id`
```

The `GetCommand` API operation returns a response that contains the
following information.

- The ID and ARN (Amazon Resource Name) of the command.
- The date and time when the command was created and last updated.
- The command state which indicates whether it's available to run on the
  vehicle.
- Any parameters that you specified when creating the command.

```
{
    "commandId": "HandsOffSteeringMode",
    "commandArn": "arn:aws:iot:ap-south-1:123456789012:command/HandsOffSteeringMode"",
    "namespace": "AWS-IoT-FleetWise",
    "mandatoryParameters":[
        {
            "name": "$actuatorPath.Vehicle.Chassis.SteeringWheel.HandsOff.HandsOffSteeringMode",
            "value": {"B": false }
        }
    ],
    "createdAt": "2024-03-23T11:24:14.919000-07:00",
    "lastUpdatedAt": "2024-03-23T11:24:14.919000-07:00",
    "deprecated": false,
    "pendingDeletion": false
}
```

## List commands in your account

You can use the [`ListCommands`](../../../iot/latest/apireference/API_ListCommands.md "../../../iot/latest/apireference/API_ListCommands.md") AWS IoT Core control plane API operation to list all
commands in your account that you created.

To list commands in your account, run the following command. By default, the API
returns commands that were created for both namespaces. To filter the list to display
only commands that were created for AWS IoT FleetWise, run the following
command.

###### Note

You can also sort the list in ascending or descending order, or filter the list to
display only commands that have a specific command parameter name.

```
aws iot list-commands --namespace "AWS-IoT-FleetWise"
```

The `ListCommands` API operation returns a response that contains the
following information.

- The ID and ARN (Amazon Resource Name) of the commands.
- The date and time when the command was created and last updated.
- The command state which indicates whether the commands are available to run on
  the vehicle.

## Update or deprecate a command

resource

You can use the [`UpdateCommand`](../../../iot/latest/apireference/API_UpdateCommand.md "../../../iot/latest/apireference/API_UpdateCommand.md") AWS IoT Core control plane API operation or AWS IoT FleetWise console to update
a command resource. You can update the display name and
description of a command. You can also deprecate a command if it's not currently being used.

###### Note

You can't modify the namespace
information or the parameters to be used when executing the command.

###### Update a command

To update a command from the console, go to the [Commands](https://console.aws.amazon.com/iotfleetwise/home#/commands "https://console.aws.amazon.com/iotfleetwise/home#/commands") page of the AWS IoT FleetWise console and
perform the following steps.

1. Choose the command that you want to update, and then choose **Edit**.
2. Edit the command details, and then choose **Save changes**.

###### Deprecate a command

To deprecate a command from the console, go to the [Commands](https://console.aws.amazon.com/iotfleetwise/home#/commands "https://console.aws.amazon.com/iotfleetwise/home#/commands") page of the AWS IoT FleetWise console and
perform the following steps.

1. Choose the command that you want to deprecate, and then choose **Deprecate**.
2. Confirm the deprecation, and then choose **Deprecate**.

###### Update a command

To update a command resource, run the following command. Replace
`command-id` with the identifier of the command that
you want to update, and provide the updated `display-name`
and `description`.

```
aws iot update-command \
    --command-id `command-id` \
    --display-name `display-name` \
    --description `description`
```

The `UpdateCommand` API operation returns the following response.

```
{
    "commandId": "HandsOffSteeringMode",
    "deprecated": false,
    "lastUpdatedAt": "2024-05-09T23:16:51.370000-07:00"
}
```

###### Deprecate a command

You deprecate a command when you intend to no longer continue using it for your
device or when it's outdated. The following example shows how to deprecate a
command.

```
aws iot update-command \
    --command-id `command-id` \
    --deprecated
```

The `UpdateCommand` API operation returns a response that contains the ID
and ARN (Amazon Resource Name) of the command.

```
{
    "commandId": "HandsOffSteeringMode",
    "deprecated": true,
    "lastUpdatedAt": "2024-05-09T23:16:51.370000-07:00"
}
```

Once a command has been deprecated, existing command executions will continue running
on the vehicle until they become terminal. To run any new command executions, you must
use the `UpdateCommand` API to restore the command so that it becomes
available. For additional information about deprecating and restoring a command and
considerations for it, see [Deprecate a command
resource](../../../iot/latest/developerguide/iot-remote-command-deprecate.md "../../../iot/latest/developerguide/iot-remote-command-deprecate.md") in the _AWS IoT Core Developer Guide_.

## Delete a command resource

You can use the [`DeleteCommand`](../../../iot/latest/apireference/API_DeleteCommand.md "../../../iot/latest/apireference/API_DeleteCommand.md") AWS IoT Core control plane API operation or AWS IoT FleetWise console to delete
a command resource.

###### Note

Deletion actions are permanent and can't be undone. The command will be
permanently removed from your account.

To delete a command from the console, go to the [Commands](https://console.aws.amazon.com/iotfleetwise/home#/commands "https://console.aws.amazon.com/iotfleetwise/home#/commands") page of the AWS IoT FleetWise console and
perform the following steps.

1. Choose the command that you want to delete, and then choose **Delete**.
2. Confirm that you want to delete the command, and then choose **Delete**.

To delete a command resource, run the following command. Replace
`command-id` with the identifier of the command that you
want to delete. The following example shows how to delete a command resource.

```
aws iot delete-command --command-id `command-id`
```

If the deletion request is successful:

- If the command has been deprecated for a duration that's longer than the
  maximum timeout of 24 hours, the command will be deleted immediately and you'll
  see a HTTP `statusCode` of 204.
- If the command isn't deprecated, or has been deprecated for a duration shorter
  than the maximum timeout, the command will be in a `pending deletion`
  state and you'll see a HTTP `statusCode` of 202. The command will be
  removed automatically from your account after the maximum timeout of 24
  hours.
