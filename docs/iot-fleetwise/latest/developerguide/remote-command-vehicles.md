# Vehicles and commands

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see
[AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

You are solely responsible for deploying commands in a manner that is safe and
compliant with applicable laws.

To use the commands feature:

1. First, create a command resource. Optionally, specify the parameters that
   contain the information required to execute the command.
2. Specify the target vehicle that will receive the command and perform the
   specified actions.
3. Now, you can run the command on the target device, and check the command execution
   details to retrieve the status and use CloudWatch logs to further troubleshoot
   any issues.
   The following sections show you the workflow between vehicles and commands.

###### Topics

- [Workflow overview](#remote-command-vehicles-overview "#remote-command-vehicles-overview")
- [Vehicle workflow](#iot-remote-command-devices-workflow "#iot-remote-command-devices-workflow")
- [Commands workflow](#iot-remote-command-commands-workflow "#iot-remote-command-commands-workflow")
- [(Optional) Commands
  notifications](#remote-command-notifications "#remote-command-notifications")

## Workflow overview

The following steps provide an overview of the commands workflow between your
vehicles and commands. When you use any of the commands HTTP API operations, the
request is signed using Sigv4 credentials.

###### Note

Except for the `StartCommandExecution` API operation, all
operations that are performed over HTTP protocol use the control plane
endpoint.

1. ###### Establish MQTT connection and subscribe to commands topics

To prepare for the commands workflow, the devices must establish an MQTT
connection with the `iot:Data-ATS` endpoint, and subscribe to the
commands request topic mentioned above. Optionally, your devices can also
subscribe to the commands accepted and rejected response topics. 2. ###### Create a vehicle model and command resource

You can now create a vehicle and a command resource using the
`CreateVehicle` and `CreateCommand` control plane
API operations. The command resource contains the configurations to be
applied when the command is executed on the vehicle. 3. ###### Start command execution on the target device

Start the command execution on the vehicle using the
`StartCommandExecution` data plane API with your
account-specific `iot:Jobs` endpoint. The API publishes a
protobuf-encoded payload message to the commands request topic. 4. ###### Update the result of the command execution

The vehicle processes the command and the payload received, and then
publishes the result of the command execution to the response topic using
the `UpdateCommandExecution` API. If your vehicle subscribed to
the commands accepted and rejected response topics, it will receive a
message that indicates whether the response was accepted or rejected by the
cloud service. 5. ###### (Optional) Retrieve command execution result

To retrieve the result of the command execution, you can use the
`GetCommandExecution` control plane API operation. After your
vehicle publishes the command execution result to the response topic, this
API will return the updated information. 6. ###### (Optional) Subscribe and manage commands events

To receive notifications for command execution status updates, you can
subscribe to the commands events topic. You can then use the
`CreateTopicRule` control plane API to route the commands
events data to other applications such as AWS Lambda functions or
Amazon SQS and build applications on top of it.

## Vehicle workflow

The following steps describe the vehicle workflow in detail when using
the commands feature.

###### Note

The operations that are described in this section use the MQTT
protocol.

1. ###### Establish an MQTT connection

To prepare your vehicles to use the commands feature, it must
first connect to the AWS IoT Core message broker. Your vehicle must be allowed
to perform the `iot:Connect` action to connect to AWS IoT Core and
establish an MQTT connection with the message broker. To find the data
plane endpoint for your AWS account, use the `DescribeEndpoint`
API or the `describe-endpoint` CLI command as shown below.

```
aws iot describe-endpoint --endpoint-type iot:Data-ATS
```

Running this command returns the account-specific data plane endpoint as
shown below.

```
`account-specific-prefix`.iot.`region`.amazonaws.com
```

2. ###### Susbcribe to commands request topic

After a connection has been established, your devices can then subscribe
to the AWS IoT commands MQTT request topic. When you create a command and
start the command execution on your target device, a protobuf encoded
payload message will be published to the request topic by the message
broker. Your device can then receive the payload message and process the
command. In this example, replace
`<DeviceID>` with the
unique identifier of your target vehicle. This ID can be the unique
identifier of your vehicle or a thing name

###### Note

The payload message that's sent to the device must use the protobuf
format.

```
$aws/commands/things/`<DeviceID>`/executions/+/request/protobuf
```

3. ###### (Optional) Subscribe to commands response topics

Optionally, you can subscribe to these commands response topics to receive
a message that indicates whether the cloud service accepted or rejected the
response from the device.

###### Note

It is optional for your vehicles to subscribe to the
`/accepted` and `/rejected` response topics.
Your vehicles will automatically receive these response messages even if they
haven't explicitly subscribed to these topics.

```
$aws/commands/things/`<DeviceID>`/executions/`<ExecutionId>`/response/protobuf/accepted
$aws/commands/things/`<DeviceID>`/executions/`<ExecutionId>`/response/protobuf/rejected
```

4. ###### Update the result of a command execution

The target vehicle then processes the command. It then uses the
`UpdateCommandExecution` API to publish the result of the
execution to the following MQTT response topic.

###### Note

For a given vehicle and command execution, the
`<DeviceID>` must match the
corresponding field in the request topic
that the device subscribed to.

```
$aws/commands/things/`<DeviceID>`/executions/`<ExecutionId>`/response/protobuf
```

The `UpdateCommandExecution` API is a data plane API operation
over MQTT that's authenticated with TLS.

    * If the cloud service successfully processed the command execution
     result, a message is published to the MQTT accepted topic. The
     accepted topic uses the following format.



    ```
    $aws/commands/things/`<DeviceID>`/executions/`<ExecutionId>`/response/protobuf/accepted
    ```
    * If the cloud service failed to process the command execution
     result, a response is published to the MQTT rejected topic. The
     rejected topic uses the following format.



    ```
    $aws/commands/things/`<DeviceID>`/executions/`<ExecutionId>`/response/protobuf/rejected
    ```

For more information about this API and an example, see [Update command execution
result](send-monitor-remote-command-cli.md#update-remote-command-execution-cli "send-monitor-remote-command-cli.md#update-remote-command-execution-cli").

## Commands workflow

The following steps describe the commands workflow in detail.

###### Note

The operations that are described in this section use the HTTP
protocol.

1. ###### Register your vehicle

Now that you've prepared your vehicle to use the commands feature, you can prepare
your application by registering your vehicle and then creating a command
that will be sent to the vehicle. To register the vehicle, create an
instance of a vehicle model (model manifest) using the
[`CreateVehicle`](../APIReference/API_CreateVehicle.md "../APIReference/API_CreateVehicle.md")
control plane API operation. For more information and examples, see [Create a
vehicle](create-vehicle.md "create-vehicle.md"). 2. ###### Create a command

Use the [`CreateCommand`](../../../iot/latest/apireference/API_CreateCommand.md "../../../iot/latest/apireference/API_CreateCommand.md")
HTTP control plane API operation to
model commands that are applicable to the vehicle that you're targeting.
Specify any parameters and default values to be used when executing the
command, and make sure that it uses the `AWS-IoT-FleetWise`
namespace. For more information and examples for using this API, see [Create a command resource](create-manage-remote-command-cli.md#create-remote-command-cli "create-manage-remote-command-cli.md#create-remote-command-cli"). 3. ###### Start the command execution

You can now execute the command that you created on the vehicle using the
[`StartCommandExecution`](../../../iot/latest/apireference/API_iotdata_StartCommandExecution.md "../../../iot/latest/apireference/API_iotdata_StartCommandExecution.md")
data plane API operation. AWS IoT Device Management
fetches the command and command parameters, and validates the incoming
request. It then invokes AWS IoT FleetWise API with the required
parameters to generate the vehicle-specific payload. The payload is then
sent to the device by AWS IoT Device Management over MQTT to the command request topic that
your device subscribed to. For more information and examples for using this
API, see [Send a command (AWS CLI)](send-monitor-remote-command-cli.md#send-remote-command-cli "send-monitor-remote-command-cli.md#send-remote-command-cli").

```
$aws/commands/things/`<DeviceID>`/executions/+/request/protobuf
```

###### Note

If the device was offline when the command was sent from the cloud and
MQTT persistent sessions is in use, the command waits at the message
broker. If the device comes back online before the time out duration,
and if it has subscribed to the commands request topic, the device can
then process the command and publish the result to the response topic.
If the device doesn't come back online before the time out duration, the
command execution will time out and the payload message will expire. 4. ###### Retrieve the command execution

After you've executed the command on the device, use the
[`GetCommandExecution`](../../../iot/latest/apireference/API_GetCommandExecution.md "../../../iot/latest/apireference/API_GetCommandExecution.md")
control plane API operation to retrieve
and monitor the result of the command execution. You can also use the API to
obtain additional information about the execution data, such as when it was
last updated, when the execution was completed, and the parameters
specified.

###### Note

To retrieve the latest status information, your device must have
published the command execution result to the response topic.

For more information and examples for using this API, see [Get command execution](send-monitor-remote-command-cli.md#get-remote-command-execution-cli "send-monitor-remote-command-cli.md#get-remote-command-execution-cli").

## (Optional) Commands

notifications

You can subscribe to commands events to receive notifications when the status of a
command execution changes. The following steps show you how to subscribe to commands
events, and then process them.

1. ###### Create a topic rule

You can subscribe to the commands events topic and receive notifications
when the status of a command execution changes. You can also create a topic
rule to route the data processed by the vehicle to other applications such
as AWS Lambda functions. You can create a topic rule either using
the AWS IoT console, or the
[`CreateTopicRule`](../../../iot/latest/apireference/API_CreateTopicRule.md "../../../iot/latest/apireference/API_CreateTopicRule.md")
AWS IoT Core control plane API operation. For more information, see [Creating
and AWS IoT rule](../../../iot/latest/developerguide/iot-create-rule.md "../../../iot/latest/developerguide/iot-create-rule.md").

In this example, replace
`<CommandID>` with the
identifier of the command for which you want to receive notifications and
`<CommandExecutionStatus>`
with the status of the command execution.

```
$aws/events/commandExecution/`<CommandID>`/`<CommandExecutionStatus>`
```

###### Note

To receive notifications for all commands and command execution
statuses, you can use wildcard characters and subscribe to the following
topic.

```
$aws/events/commandExecution/+/#
```

2. ###### Receive and process commands events

If you created a topic rule in the previous step to subscribe to commands
events, then you can manage the commands push notifications that you
receive. You can also optionally build applications on top of it, such as
with AWS Lambda, Amazon SQS, Amazon SNS, or AWS Step Functions using the
topic rule that you created.

The following code shows a sample payload for the commands events notifications
that you'll receive.

```
{
    "executionId": "`2bd65c51-4cfd-49e4-9310-d5cbfdbc8554`",
    "status":"FAILED",
    "statusReason": {
         "reasonCode": "4",
         "reasonDescription": ""
    },
    "eventType": "COMMAND_EXECUTION",
    "commandArn":"arn:aws:iot:`us-east-1`:`123456789012`:command/`0b9d9ddf-e873-43a9-8e2c-9fe004a90086`",
    "targetArn":"arn:aws:iot:`us-east-1`:`123456789012`:thing/`5006c3fc-de96-4def-8427-7eee36c6f2bd`",
    "timestamp":`1717708862107`
}
```
