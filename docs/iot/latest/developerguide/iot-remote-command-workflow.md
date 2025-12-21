# High-level commands workflow

This workflow shows how devices interact with AWS IoT Device Management Commands. All HTTP API requests use [Sigv4 credentials](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") for signing.

![Overview of the AWS IoT Device Management device command high-level workflow.](images/device-command-workflow.png)

###### Workflow overview

- [Create and manage commands](#command-create-command "#command-create-command")
- [Choose target device for your commands and
  subscribe to MQTT topics](#command-choose-target "#command-choose-target")
- [Start and monitor command executions for
  your target device](#command-command-executions "#command-command-executions")
- [(Optional) Enable
  notifications for commands events](#iot-remote-command-commands-notifications "#iot-remote-command-commands-notifications")

## Create and manage commands

To create and manage commands for your devices, perform the following steps.

1. ###### Create a command resource

Create a Command from the [Command Hub](https://console.aws.amazon.com/iot/home#/commandHub "https://console.aws.amazon.com/iot/home#/commandHub") or using the [`CreateCommand`](../apireference/API_CreateCommand.md "../apireference/API_CreateCommand.md") API. 2. ###### Specify the payload

Provide a Payload in any format. Specify the content type to ensure correct device interpretation.

For dynamic Commands with payload templates, the final payload is generated at runtime using your supplied parameters. Templates support JSON format only, but the generated Payload can be sent as JSON or CBOR. 3. ###### (Optional) Manage the created commands

Update the display name and description after creation. Mark Commands as deprecated when no longer needed, or delete them permanently. To modify Payload information, create a new Command.

## Choose target device for your commands and

subscribe to MQTT topics

Choose your target device and configure MQTT topics for receiving Commands and publishing responses.

1. ###### Choose the target device for your command

Choose a target device to receive and execute the Command. Use a Thing name for registered devices or a Client ID for unregistered devices. For more information, see [Target device
considerations](iot-remote-command-execution-start-monitor.md#iot-command-execution-target "iot-remote-command-execution-start-monitor.md#iot-command-execution-target"). 2. ###### Configure the AWS IoT device policy

Configure an IAM policy granting permissions to receive Executions and publish updates. See
[Sample IAM
policy](iot-remote-command-execution-start-monitor.md#iot-remote-command-execution-update-policy "iot-remote-command-execution-start-monitor.md#iot-remote-command-execution-update-policy") for policy examples. 3. ###### Establish an MQTT connection

Connect devices to the message broker and subscribe to request and response Topics. Devices need `iot:Connect` permission. Find your data plane endpoint using the
`DescribeEndpoint` API or `describe-endpoint` CLI command:

```
aws iot describe-endpoint --endpoint-type iot:Data-ATS
```

Running this command returns the account-specific data plane endpoint as shown
below.

```
`account-specific-prefix`.iot.`region`.amazonaws.com
```

4. ###### Subscribe to commands topics

Subscribe to the Commands request Topic. When you start an Execution, the message broker publishes the Payload to this Topic. Your device receives and processes the Command.

(Optional) Subscribe to response Topics (`accepted` or `rejected`) to receive confirmation whether the cloud service accepted or rejected the device response.

In this example, replace:

    * ``<device>``
     with `thing` or `client` depending on
     whether the device you're targeting has been registered as an
     IoT thing, or specified as an MQTT client.
    * ``<DeviceID>``
     with the unique identifier of your target device. This ID can
     be the unique MQTT client ID or a thing name.

###### Note

If the payload type is not JSON or CBOR, the
`<PayloadFormat>` field might not be
present in the commands request topic. To get the payload format, we
recommend that you use MQTT5 to get the format information from the
MQTT message headers. For more information, see [Commands topics](reserved-topics.md#reserved-topics-commands "reserved-topics.md#reserved-topics-commands").

```
$aws/commands/`<devices>`/`<DeviceID>`/executions/+/request/`<PayloadFormat>`
$aws/commands/`<devices>`/`<DeviceID>`/executions/+/response/accepted/`<PayloadFormat>`
$aws/commands/`<devices>`/`<DeviceID>`/executions/+/response/rejected/`<PayloadFormat>`

```

## Start and monitor command executions for

your target device

After you have created the commands and specified the targets for the command, you can
start the execution on the target device by performing the following steps.

1. ###### Start command execution on the target device

Start the Execution from the [Command Hub](https://console.aws.amazon.com/iot/home#/commandHub "https://console.aws.amazon.com/iot/home#/commandHub") or using the `StartCommandExecution` API with
your account-specific endpoint. Use `iot:Data-ATS` for dual-stack (IPv4/IPv6) or `iot:Jobs` for IPv4 only.

The API publishes the Payload to the Commands request Topic.

###### Note

If the device is offline and uses MQTT persistent sessions, the
Command waits at the message broker. When the device reconnects before
timeout, it can process the Command and publish results. If timeout expires,
the execution times out and the payload will be discarded. 2. ###### Update the result of the command execution

The device receives the Payload, processes the Command,
performs the specified actions, and publishes results to the Commands response Topic using
`UpdateCommandExecution` MQTT based API. If subscribed to accepted and rejected Topics, the device receives confirmation whether the cloud service accepted or rejected the response.

Depending on what you specified in the request topic, `<devices>`
can be either things or clients, and `<DeviceID>`
can be your AWS IoT thing name or the MQTT client ID.

###### Note

The `<PayloadFormat>` can only be JSON
or CBOR in the commands response topic.

```
$aws/commands/`<devices>`/`<DeviceID>`/executions/`<ExecutionId>`/response/`<PayloadFormat>`
```

3. ###### (Optional) Retrieve command execution result

Retrieve Execution results from the AWS IoT console or using `GetCommandExecution`. The device must publish results to the Commands response
Topic for latest information. View additional details including last update time, result, and completion time.

## (Optional) Enable

notifications for commands events

Subscribe to Commands events for notifications when Execution status changes.

1. ###### Create a topic rule

Subscribe to the Commands events Topic for status change notifications. Create a topic rule to
route device data to other AWS IoT services like AWS Lambda, Amazon SQS, and AWS Step Functions using the AWS IoT console or
[Creating an AWS IoT rule](iot-create-rule.md "iot-create-rule.md").

In this example, replace
`<CommandID>` with the
identifier of the command for which you want to receive notifications and
`<CommandExecutionStatus>`
with the status of the command execution.

```
$aws/events/commandExecution/`<CommandID>`/`<CommandExecutionStatus>`
```

###### Note

To receive notifications for all commands and command execution statuses,
you can use wildcard characters and subscribe to the following topic.

```
$aws/events/commandExecution/+/#
```

2. ###### Receive and process commands events

Manage Commands push notifications and build applications using the subscribed events.

The following code shows a sample payload for the commands events notifications that
you'll receive.

```
{
    "executionId": "`2bd65c51-4cfd-49e4-9310-d5cbfdbc8554`",
    "status":"FAILED",
    "statusReason": {
         "reasonCode": "DEVICE_TOO_BUSY",
         "reasonDescription": ""
    },
    "eventType": "COMMAND_EXECUTION",
    "commandArn":"arn:aws:iot:`us-east-1`:`123456789012`:command/`0b9d9ddf-e873-43a9-8e2c-9fe004a90086`",
    "targetArn":"arn:aws:iot:`us-east-1`:`123456789012`:thing/`5006c3fc-de96-4def-8427-7eee36c6f2bd`",
    "timestamp":`1717708862107`
}
```
