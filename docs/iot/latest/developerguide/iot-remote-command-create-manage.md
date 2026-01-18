# Create and manage commands

Use AWS IoT Device Management Commands to configure reusable remote actions or
send immediate instructions to devices. Create and manage Commands from the AWS IoT console or using the AWS CLI.

###### Create and manage commands operations

- [Create a command resource](#iot-remote-command-create "#iot-remote-command-create")
- [Retrieve information about a command](#iot-remote-command-get "#iot-remote-command-get")
- [List commands in your AWS account](#iot-remote-command-list "#iot-remote-command-list")
- [Update a command resource](#iot-remote-command-update "#iot-remote-command-update")
- [Deprecate or restore a command
  resource](#iot-remote-command-deprecatecmd "#iot-remote-command-deprecatecmd")
- [Delete a command resource](#iot-remote-command-delete "#iot-remote-command-delete")

## Create a command resource

Provide the following information when creating a Command:

- ###### General information

Provide a unique Command ID to identify the Command when running it on target devices. Optionally specify a display name, description,
and tags for management.

- **Payload**

For static Commands, provide a Payload defining device actions. Specify the
Payload format type for correct device interpretation.

For dynamic Commands, see the Payload template attribute.

- **Payload template**

For dynamic Commands, provide a payloadTemplate with placeholders and parameters.
Optionally provide `defaultValue` and conditions. AWS IoT Device Management Commands replaces placeholders
at runtime. Missing parameters use their defaultValue. All values must
satisfy defined conditions.

The following case-sensitive placeholder types are supported:

    + `${aws:iot:commandexecution::parameter:`parameter1`}` – A placeholder for the value of a parameter with the name `parameter1`.
    + `${aws:iot:commandexecution::executionTimeoutSec}` – A placeholder for the command execution timeout parameter supplied at runtime.

Commands reserved Topics use a format based on Payload format type.

- For `application/json`
  or `application/cbor` content types, use this request Topic:

```
$aws/commands/`<devices>`/`<DeviceID>`/executions/+/request/`<PayloadFormat>`
```

- For other content types or unspecified format, use this request
  Topic. The Payload format appears in the MQTT message header.

```
$aws/commands/`<devices>`/`<DeviceID>`/executions/+/request
```

The Commands response Topic uses `json` or `cbor` format regardless of Payload
type. `<PayloadFormat>`
must be `json` or `cbor`:

```
$aws/commands/`<devices>`/`<DeviceID>`/executions/`<ExecutionId>`/response/`<PayloadFormat>`
```

The following sections describe Payload format considerations and
Command creation from the console.

###### Topics

- [Static command payload format](#iot-commands-payload-format "#iot-commands-payload-format")
- [Dynamic command payload format](#iot-commands-dynamic-payload-format "#iot-commands-dynamic-payload-format")
- [How to create a command (console)](#iot-commands-console-how "#iot-commands-console-how")

#### Static command payload format

The Payload supports any format up to 32 KB. Specify
the Payload format type for secure and correct device interpretation.

Specify Payload format type using `type/subtype`
format (e.g., `application/json` or
`application/cbor`). Default: `application/octet-stream`. See [Common MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types "https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types") for supported formats.

#### Dynamic command payload format

The payloadTemplate must be valid JSON with at least one placeholder, up to 32 KB.

For `AwsJsonSubstitution` preprocessor, AWS IoT Device Management Commands sends notifications in JSON or CBOR format based on
preprocessor configuration.

#### How to create a command (console)

To create a Command from the console, go to [Command Hub](https://console.aws.amazon.com/iot/home#/commandHub "https://console.aws.amazon.com/iot/home#/commandHub") and
follow these steps:

1. Choose **Create
   command**.
2. Specify a unique Command ID.
3. (Optional) Specify display name, description, and tags.
4. Upload the Payload file containing device actions. Specify the Payload format type for correct device interpretation.
5. (Optional) For JSON payload templates with placeholders, parameters
   pre-populate in the inline table for editing.
6. (Optional) Configure parameter value type (required), default value, and conditions.
7. Choose **Create command**.

Use the [`CreateCommand`](../apireference/API_CreateCommand.md "../apireference/API_CreateCommand.md") API or [`create-command`](../../../cli/latest/reference/iot/create-command.md "../../../cli/latest/reference/iot/create-command.md") CLI command to create a
Command.

###### Topics

- [Command payload](#iot-commands-payload "#iot-commands-payload")
- [Sample IAM policy](#iot-remote-command-create-iam "#iot-remote-command-create-iam")
- [Static command creation
  example](#iot-remote-command-create-example "#iot-remote-command-create-example")
- [Dynamic command creation
  example](#iot-remote-dynamic-command-create-example "#iot-remote-dynamic-command-create-example")

#### Command payload

Provide a static Payload or payload template. Static Payloads are base64 encoded. For payload templates, the final Payload generates at runtime
using parameter values. Devices process the Payload and perform
specified actions. Specify
the Payload content type for correct device reception.

###### Note

Payloads cannot be modified after Command creation.
Create a new Command to modify the Payload.

#### Sample IAM policy

Before you use this API operation, make sure that your IAM policy
authorizes you to perform this action on the device. The following example
shows an IAM policy that allows the user permission to perform the
`CreateCommand` action.

In this example, replace:

- `region` with your
  AWS Region, such as
  `us-east-1`.
- `account-id` with your
  AWS account number, such as
  `123456789012`.
- `command-id` with a unique
  identifier for your AWS IoT command ID, such as
  `LockDoor`. If you
  want to send more than one command, you can specify these commands
  under the _Resource_ section in the
  IAM policy.

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Action": "iot:CreateCommand",
 "Effect": "Allow",
 "Resource": "arn:aws:iot:`us-east-1`:`123456789012`:command/`command-id`"
 }
}`

```

#### Static command creation

example

The following example shows how you can create a static command. Depending on your
application, replace:

- `<command-id>` with a
  unique identifier for the command. For example, to lock the door
  of your house, you can specify `LockDoor`.
  We recommend that you use UUID. You can also use alpha-numeric
  characters, "-", and "\_".
- (Optional)
  `<display-name>` and
  `<description>`
  , which are optional fields that you can use to provide a friendly
  name and a meaningful description for the command, such as
  `Lock the doors of my home`.
- `namespace`, which you can use to specify the namespace
  of the command. It must be `AWS-IoT`. For information about using this feature for
  AWS IoT FleetWise, see [Remote
  commands](../../../iot-fleetwise/latest/developerguide/remote-commands.md "../../../iot-fleetwise/latest/developerguide/remote-commands.md")
- `payload` contains information about the payload that
  you want to use when running the command and it's content
  type.

```
aws iot create-command \
    --command-id `<command-id>` \
    --display-name ``<display-name>`` \
    --description `<description>` \
    --namespace AWS-IoT \
    --payload '{"content":`"eyAibWVzc2FnZSI6ICJIZWxsbyBJb1QiIH0="`,"contentType":"application/json"}'
```

Running this command generates a response that contains the ID and ARN
(Amazon resource name) of the command. For example, if you specified the
`LockDoor`
command during creation, the following shows a sample output of running the
command.

```
{
    "commandId": "LockDoor",
    "commandArn": "arn:aws:iot:us-east-1:123456789012:command/LockDoor"
}
```

#### Dynamic command creation

example

The following example shows how you can create a dynamic command. Depending on your
application, replace:

- `<command-id>` with a
  unique identifier for the command. For example, to set the light power status,
  you can specify `Light_Power_Status`.
  We recommend that you use UUID. You can also use alpha-numeric
  characters, "-", and "\_".
- (Optional)
  `<display-name>` and
  `<description>`
  , which are optional fields that you can use to provide a friendly
  name and a meaningful description for the command, such as
  `Turn a light ON or OFF`.
- `namespace`, which you can use to specify the namespace
  of the command. It must be `AWS-IoT`. For information about using this feature for
  AWS IoT FleetWise, see [Remote
  commands](../../../iot-fleetwise/latest/developerguide/remote-commands.md "../../../iot-fleetwise/latest/developerguide/remote-commands.md")
- `payloadTemplate` contains the JSON formatted playoad template with placehodlers.
- `preprocessor` contains the configuration for preprocessor that determines how the payloadTemplate must be processed.
- `mandatoryParameter` contains the parameters corresponding to the placeholders in the payloadTemplate, their type, default values, and conditions.

```
aws iot create-command \
    --command-id `Light_Power_Status` \
    --description `"Turn a light ON or OFF"` \
    --namespace AWS-IoT \
    --payload-template `'{"powerStatus":"${aws:iot:commandexecution::parameter:powerStatus}"}'` \
    --preprocessor `awsJsonSubstitution={outputFormat=JSON}` \
    --mandatory-parameters `"name=powerStatus, defaultValue={S=OFF}, valueConditions=[{comparisonOperator=IN_SET, operand={strings=['ON','OFF']}}]"`

```

Running this command generates a response that contains the ID and ARN
(Amazon resource name) of the command. For example, if you specified the
`Light_Power_Status`
command during creation, the following shows a sample output of running the
command.

```
{
    "commandId": "Light_Power_Status",
    "commandArn": "arn:aws:iot:us-east-1:123456789012:command/Light_Power_Status"
}
```

## Retrieve information about a command

After you create a command, you can retrieve information about it from the AWS IoT
console and using the AWS CLI. You can obtain the following information.

- The command ID, Amazon resource name (ARN), any display name and
  description that you specified for the command.
- The command state, which indicates whether a command is available to
  run on the target device, or whether it's being deprecated or deleted.
- The payload or payloadTemplate that you provided.
- The preprocessor that you provided.
- The mandatoryParameters that you provided.
- The time when the command was created and last updated.

To retrieve a command from the console, go to the [Command Hub](https://console.aws.amazon.com/iot/home#/commandHub "https://console.aws.amazon.com/iot/home#/commandHub") of the AWS IoT console and then
choose the command that you created to view it's details.

In addition to the command details, you can see the command history, which
provides information about the executions of the command on the target device.
After you run this command on the device, you can find information about the
executions on this tab.

Use the [`GetCommand`](../apireference/API_GetCommand.md "../apireference/API_GetCommand.md") HTTP control plane API operation or the
[`get-command`](../../../cli/latest/reference/get-command.md "../../../cli/latest/reference/get-command.md") AWS CLI command to retrieve information
about a command resource. You must've already created the command using the
`CreateCommand` API request or the `create-command`
CLI.

#### Sample IAM policy

Before you use this API operation, make sure that your IAM policy
authorizes you to perform this action on the device. The following example
shows an IAM policy that allows the user permission to perform the
`GetCommand` action.

In this example, replace:

- `region` with your
  AWS Region, such as `us-east-1`.
- `account-id` with your
  AWS account number, such as
  `123456789023`.
- `command-id` with your AWS IoT
  unique command identifier, such as
  `LockDoor` or `Light_Power_Status`. If you
  want to retrieve more than one command, you can specify these
  commands under the _Resource_
  section in the IAM policy.

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Action": "iot:GetCommand",
 "Effect": "Allow",
 "Resource": "arn:aws:iot:`us-east-1`:`123456789012`:command/`command-id`"
 }
}`

```

#### Retrieve a command example

(AWS CLI)

The following example shows you how to retrieve information about a
command using the `get-command` AWS CLI. Depending on your
application, replace
`<command-id>` with the
identifier for the command for which you want to retrieve information. You
can obtain this information from the response of the
`create-command` CLI.

```
aws iot get-command --command-id `<command-id>`
```

Running this command generates a response that contains information about
the command, the payload, and the time when it was created and last updated.
It also provides information that indicates whether a command has been
deprecated or is being deleted.

For example, the following code shows a sample response.

```
{
    "commandId": "LockDoor",
    "commandArn": "arn:aws:iot:<region>:<account>:command/LockDoor",
    "namespace": "AWS-IoT",
    "payload":{
        "content": "eyAibWVzc2FnZSI6ICJIZWxsbyBJb1QiIH0=",
        "contentType": "application/json"
    },
    "createdAt": "2024-03-23T00:50:10.095000-07:00",
    "lastUpdatedAt": "2024-03-23T00:50:10.095000-07:00",
    "deprecated": false,
    "pendingDeletion": false
}
```

## List commands in your AWS account

After you have created commands, you can view the commands that you have created in
your account. In the list, you can find information about:

- The command ID, and any display name that you specified for the
  commands.
- The Amazon resource name (ARN) of the commands.
- The command state which indicates whether the commands are available to run on
  the target device, or whether they are deprecated.

###### Note

The list does not display that are being deleted from your account. If the
commands are pending deletion, you can still view the details for these
commands using their command ID.

- The time when the commands were created and last updated.

In the AWS IoT console, you can find the list of commands that you created and
their details by going to the [Command Hub](https://console.aws.amazon.com/iot/home#/commandHub "https://console.aws.amazon.com/iot/home#/commandHub").

To list the commands that you created, use the [`ListCommands`](../apireference/API_ListCommands.md "../apireference/API_ListCommands.md")
API operation or the [`list-commands`](../../../cli/latest/reference/iot/list-commands.md "../../../cli/latest/reference/iot/list-commands.md") CLI.

#### Sample IAM policy

Before you use this API operation, make sure that your IAM policy
authorizes you to perform this action on the device. The following example
shows an IAM policy that allows the user permission to perform the
`ListCommands` action.

In this example, replace:

- `region` with your
  AWS Region, such as `us-east-1`.
- `account-id` with your
  AWS account number, such as
  `123456789012`.

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Action": "iot:ListCommands",
 "Effect": "Allow",
 "Resource": "arn:aws:iot:`us-east-1`:`123456789012`:command/*"
 }
}`

```

#### List commands in your account

example

The following command shows how to list commands in your account.

```
aws iot list-commands --namespace "AWS-IoT"
```

Running this command generates a response that contains a list of commands
that you created, the time when the commands were created and when it was
last updated. It also provides the command state information, which
indicates whether a command has been deprecated or is available to run on
the target device. For more information about the different statuses and
status reason, see [Command execution status](iot-remote-command-concepts.md#iot-command-execution-status "iot-remote-command-concepts.md#iot-command-execution-status").

## Update a command resource

After you have created a command, you can update the display name and description of
the command.

###### Note

The payload for the command can't be updated. To update this
information or to use a modified payload, you'll need to create a new
command.

To update a command from the console, go to the [Command Hub](https://console.aws.amazon.com/iot/home#/commandHub "https://console.aws.amazon.com/iot/home#/commandHub") of the AWS IoT console and
perform the following steps.

1. To update an existing command resource, choose the command that you
   want to update, and then under **Actions**, choose
   **Edit**.
2. Specify the display name and description that you want to use, and any
   name-value pairs as tags for your command.
3. Choose **Edit** to save the command with the new
   settings.
   Use the [`UpdateCommand`](../apireference/API_UpdateCommand.md "../apireference/API_UpdateCommand.md") control plane API operation or the
   [`update-command`](../../../cli/latest/reference/iot/update-command.md "../../../cli/latest/reference/iot/update-command.md") AWS CLI to update a command
   resource. Using this API, you can:

- Edit the display name and description of a command that you
  created.
- Deprecate a command resource, or restore a command that has already
  been deprecated.

#### Sample IAM policy

Before you use this API operation, make sure that your IAM policy
authorizes you to perform this action on the device. The following example
shows an IAM policy that allows the user permission to perform the
`UpdateCommand` action.

In this example, replace:

- `region` with your
  AWS Region, such as `us-east-1`.
- `account-id` with your
  AWS account number, such as
  `123456789012`.
- `command-id` with your AWS IoT
  unique command identifier, such as
  `LockDoor`. If you
  want to retrieve more than one command, you can specify these
  commands under the _Resource_
  section in the IAM policy.

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Action": "iot:UpdateCommand",
 "Effect": "Allow",
 "Resource": "arn:aws:iot:`us-east-1`:`123456789012`:command/`command-id`"
 }
}`

```

#### Update information about

a command examples (AWS CLI)

The following example shows you how to update information about a command
using the `update-command` AWS CLI command. For information about
how you can use this API to deprecate or restore a command resource, see
[Update a command resource
(CLI)](iot-remote-command-deprecate.md#iot-remote-command-deprecate-cli "iot-remote-command-deprecate.md#iot-remote-command-deprecate-cli").

The example shows how you can update the display name and description of a
command. Depending on your application, replace
`<command-id>` with the
identifier for the command for which you want to retrieve
information.

```
aws iot update-command \
    --command-id `<command-id>`
    --displayname `<display-name>` \
    --description `<description>`
```

Running this command generates a response that contains the updated
information about the command and the time when it was last updated. The
following code shows a sample request and response for updating the display
name and description of a command that turns off the AC.

```
aws iot update-command \
    --command-id `<LockDoor>` \
    --displayname `<Secondary lock door>` \
    --description `<Locks doors to my home>`
```

Running this command generates the following response.

```
{
    "commandId": "LockDoor",
    "commandArn": "arn:aws:iot:us-east-1:123456789012:command/LockDoor",
    "displayName": "Secondary lock door",
    "description": "Locks doors to my home",
    "lastUpdatedAt": "2024-05-09T23:15:53.899000-07:00"
}
```

## Deprecate or restore a command

resource

After you have created a command, if no longer want to continue using the command, you
can mark it as deprecated. When you deprecate a command, all pending command executions
will continue running on the target device until they reach a terminal status. Once a
command has been deprecated, if you want to use it such as for sending a new command
execution to the target device, you must restore it.

###### Note

You can't edit a deprecated command, or run any new executions for it. To
run new commands on the device, you must restore it so that the command state
changes to _Available_.

For additional information about deprecating and restoring a command, and
considerations for it, see [Deprecate a command resource](iot-remote-command-deprecate.md "iot-remote-command-deprecate.md").

## Delete a command resource

If you no longer want to use a command, you can remove it permanently from your
account. If the deletion action is successful:

- If the command has been deprecated for a duration that's longer than the maximum
  timeout of 12 hours, the command will be deleted immediately.
- If the command isn't deprecated, or has been deprecated for a duration shorter
  than the maximum timeout, the command will be in a `pending deletion` state.
  It will be removed automatically from your account after the maximum timeout of 12 hours.

###### Note

The command might be deleted even if there are any pending command executions. The
command will be in a pending deletion state and will be removed from your account
automatically.

To delete a command from the console, go to the [Command Hub](https://console.aws.amazon.com/iot/home#/commandHub "https://console.aws.amazon.com/iot/home#/commandHub") of the AWS IoT console and
perform the following steps.

1. Choose the command that you want to delete, and and then under
   **Actions**, choose
   **Delete**.
2. Confirm that you want to delete the command and then choose
   **Delete**.
   The command will be marked for deletion and will be permanently removed from
   your account after 12 hours.

Use the `DeleteCommand` HTTP control plane API operation or the
`delete-command` AWS CLI command to delete a command resource. If
the deletion action is successful, you'll see a HTTP `statusCode` of
204 or 202, and the command will be deleted from your account automatically after
the maximum timeout duration of 12 hours. In the case of the 204 status, it
indicates that the command has been deleted.

#### Sample IAM policy

Before you use this API operation, make sure that your IAM policy
authorizes you to perform this action on the device. The following example
shows an IAM policy that allows the user permission to perform the
`DeleteCommand` action.

In this example, replace:

- `region` with your
  AWS Region, such as `us-east-1`.
- `account-id` with your
  AWS account number, such as
  `123456789012`.
- `command-id` with your AWS IoT
  unique command identifier, such as
  `LockDoor`. If you
  want to retrieve more than one command, you can specify these
  commands under the _Resource_
  section in the IAM policy.

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Action": "iot:DeleteCommand",
 "Effect": "Allow",
 "Resource": "arn:aws:iot:`us-east-1`:`123456789012`:command/`command-id`"
 }
}`

```

#### Delete a command example

(AWS CLI)

The following examples show you how to delete a command using the
`delete-command` AWS CLI command. Depending on your
application, replace
`<command-id>` with the
identifier for the command that you're deleting.

```
aws iot delete-command --command-id `<command-id>`
```

If the API request is successful, then the command generates a status code
of 202 or 204. You can use the `GetCommand` API to verify that the
command no longer exists in your account.
