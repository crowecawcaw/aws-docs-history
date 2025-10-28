# Create and manage commands

You can use the AWS IoT Device Management commands feature to either configure reusable remote actions or
send one-time, immediate instructions to your devices. The following sections show you
how you can create and manage commands from the AWS IoT console and using the AWS CLI.

###### Create and manage commands operations

- [Create a command resource](#iot-remote-command-create "#iot-remote-command-create")
- [Retrieve information about a command](#iot-remote-command-get "#iot-remote-command-get")
- [List commands in your AWS account](#iot-remote-command-list "#iot-remote-command-list")
- [Update a command resource](#iot-remote-command-update "#iot-remote-command-update")
- [Deprecate or restore a command
  resource](#iot-remote-command-deprecatecmd "#iot-remote-command-deprecatecmd")
- [Delete a command resource](#iot-remote-command-delete "#iot-remote-command-delete")

## Create a command resource

When you create a command, you must provide the following information.

- ###### General information

When creating a command, you must provide a command ID, which is a unique
identifier to help you identify the command when you want to run it on the
target device. Optionally, you can also specify a display name, description,
and tags to further help you manage the command.

- ###### Payload

You must also provide a payload that defines the actions the
device must perform. While optional, we recommend that you specify the
payload format type so that the device correctly inteprets the payload.

The commands reserved topics use a format that depends on
the payload format type.

- If you specify a payload content type of `application/json`
  or `application/cbor`, then the request topic will be the following.

```
$aws/commands/`<devices>`/`<DeviceID>`/executions/+/request/`<PayloadFormat>`
```

- If you specify a payload content type other than
  `application/json` or `application/cbor`,
  or if you don't specify the payload format type, then the request
  topic will be the following. In this case, the payload format will
  be included in the MQTT message header.

```
$aws/commands/`<devices>`/`<DeviceID>`/executions/+/request
```

The commands response topic will return a format that
uses `json` or `cbor` independent of the payload
format type. The response topic will use the
following format where `<PayloadFormat>`
must be `json` or `cbor`.

```
$aws/commands/`<devices>`/`<DeviceID>`/executions/`<ExecutionId>`/response/`<PayloadFormat>`
```

The following sections show you the command payload format considerations and
how to create commands from the console.

###### Topics

- [Command payload format](#iot-commands-payload-format "#iot-commands-payload-format")
- [How to create a command (console)](#iot-commands-console-how "#iot-commands-console-how")

#### Command payload format

The payload can use any format of your choice. The maximum
size of the payload must not exceed 32 KB. To make sure that the device can
securely and correctly interpret the payload, we recommend that you specify
the payload format type.

You specify the payload format type using the `type/subtype`
format, such as `application/json` or
`application/cbor`. By default, it will
be set as `application/octet-stream`. For information about
payload formats that you can specify, see [Common MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types "https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types").

#### How to create a command (console)

To create a command from the console, go to the [Command Hub](https://console.aws.amazon.com/iot/home#/commandHub "https://console.aws.amazon.com/iot/home#/commandHub") of the AWS IoT console and
perform the following steps.

1. To create a new command resource, choose **Create
   command**.
2. Specify a unique command ID to help you identify the command that you
   want to run on the target device.
3. (Optional) Specify an optional display name, description, and any
   name-value pairs as tags for your command.
4. Upload the payload file from your local storage that contains the
   actions the device needs to perform. While optional, we recommend that
   you specify the payload format type so that the device correctly
   interprets the file and processes the instructions.
5. Choose **Create command**.

This section describes the HTTP control plane API operation, [`CreateCommand`](../apireference/API_CreateCommand.md "../apireference/API_CreateCommand.md"), and the corresponding AWS CLI command, [`create-command`](../../../cli/latest/reference/iot/create-command.md "../../../cli/latest/reference/iot/create-command.md") that you can run to create a
command resource.

###### Topics

- [Command payload](#iot-commands-payload "#iot-commands-payload")
- [Sample IAM policy](#iot-remote-command-create-iam "#iot-remote-command-create-iam")
- [Create command
  example](#iot-remote-command-create-example "#iot-remote-command-create-example")

#### Command payload

When creating the command, you must provide a payload. The payload
that you provide is base64 encoded. When your devices receive the
command, the device-side logic can process the payload and perform
the specified actions. To make sure that your devices correctly
receive the command and the payload, we recommend that you specify
the payload content type.

###### Note

After you create the command, you cannot modify the payload.
To modify the payload, you'll have to create a new command.

#### Sample IAM policy

Before you use this API operation, make sure that your IAM policy
authorizes you to perform this action on the device. The following example
shows an IAM policy that allows the user permission to perform the
`CreateCommand` action.

In this example, replace:

- `region` with your
  AWS Region, such as
  `ap-south-1`.
- `account-id` with your
  AWS account number, such as
  `123456789012`.
- `command-id` with a unique
  identifier for your AWS IoT command ID, such as
  `LockDoor`. If you
  want to send more than one command, you can specify these commands
  under the _Resource_ section in the
  IAM policy.

JSON

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

#### Create command

example

The following example shows how you can create a command. Depending on your
application, replace:

- `<command-id>` with a
  unique identifier for the command. For example, to lock the doc-history
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
  of the command. It must be `AWS-IoT`.
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
    "commandArn": "arn:aws:iot:ap-south-1:123456789012:command/LockDoor"
}
```

## Retrieve information about a command

After you create a command, you can retrieve information about it from the AWS IoT
console and using the AWS CLI. You can obtain the following information.

- The command ID, Amazon resource name (ARN), any display name and
  description that you specified for the command.
- The command state, which indicates whether a command is available to
  run on the target device, or whether it's being deprecated or deleted.
- The payload that you provided and it's format type.
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
  AWS Region, such as `ap-south-1`.
- `account-id` with your
  AWS account number, such as
  `123456789023`.
- `command-id` with your AWS IoT
  unique command identifier, such as
  `LockDoor`. If you
  want to retrieve more than one command, you can specify these
  commands under the _Resource_
  section in the IAM policy.

JSON

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
  AWS Region, such as `ap-south-1`.
- `account-id` with your
  AWS account number, such as
  `123456789012`.

JSON

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
  AWS Region, such as `ap-south-1`.
- `account-id` with your
  AWS account number, such as
  `123456789012`.
- `command-id` with your AWS IoT
  unique command identifier, such as
  `LockDoor`. If you
  want to retrieve more than one command, you can specify these
  commands under the _Resource_
  section in the IAM policy.

JSON

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
    "commandArn": "arn:aws:iot:ap-south-1:123456789012:command/LockDoor",
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
  AWS Region, such as `ap-south-1`.
- `account-id` with your
  AWS account number, such as
  `123456789012`.
- `command-id` with your AWS IoT
  unique command identifier, such as
  `LockDoor`. If you
  want to retrieve more than one command, you can specify these
  commands under the _Resource_
  section in the IAM policy.

JSON

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
