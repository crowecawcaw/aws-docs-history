# Start and monitor command

executions

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

After you've created a command resource, you can start a command execution on the target
vehicle. Once the vehicle starts executing the command, it can start updating the result of
the command execution and publish status updates and result information to the MQTT reserved
topics. You can then retrieve the status of the command execution and monitor the status of
the executions in your account.

This topic shows how you can send a command to your vehicle using the AWS CLI or AWS IoT FleetWise console. It also shows
you how to monitor and update the status of the command execution.

###### Topics

- [Update command execution
  result](#update-remote-command-execution-cli "#update-remote-command-execution-cli")
- [Get command execution](#get-remote-command-execution-cli "#get-remote-command-execution-cli")
- [List command executions in your
  account](#list-remote-command-execution-cli "#list-remote-command-execution-cli")
- [Delete a command execution](#delete-remote-command-execution-cli "#delete-remote-command-execution-cli")
  To send a command from the console, go to the [Vehicles](https://console.aws.amazon.com/iotfleetwise/home#/vehicles "https://console.aws.amazon.com/iotfleetwise/home#/vehicles") page of the AWS IoT FleetWise console and
  perform the following steps.

1. Choose the vehicle that you want to send a command to.
2. Choose **Run command**.
3. Select the command ID.
4. Specify the command execution timeout, and then choose **Run command**.
   You can use the [`StartCommandExecution`](../../../iot/latest/apireference/API_iot_data_StartCommandExecution.md "../../../iot/latest/apireference/API_iot_data_StartCommandExecution.md") AWS IoT data plane API operation to
   send a command to a vehicle. The vehicle then forwards the command to an automotive
   middleware service (like SOME/IP (Scalable Service-Oriented Middleware over IP)) or
   publishes it on a vehicle network (like a controller area network (CAN) device
   interface). The following example uses the AWS CLI.

###### Topics

- [Considerations when sending a
  command](#send-remote-command-considerations "#send-remote-command-considerations")
- [Obtain account-specific data plane
  endpoint](#send-remote-command-endpoint "#send-remote-command-endpoint")
- [Send a command example](#send-remote-command-example "#send-remote-command-example")

### Considerations when sending a

command

When you start a command execution in AWS IoT FleetWise:

- You must provision an AWS IoT thing for the vehicle. For more information,
  see [Provision AWS IoT FleetWise vehicles](provision-vehicles.md "provision-vehicles.md").
- You must have already created a command with
  `AWS-IoT-FleetWise` as the namespace and provided a
  `role-Arn` that grants you permission to create and run
  commands in AWS IoT FleetWise. For more information, see [Create a command resource](create-manage-remote-command-cli.md#create-remote-command-cli "create-manage-remote-command-cli.md#create-remote-command-cli").
- You can skip the `parameters` field if you choose to use any
  default values that were specified for the parameters when creating the
  command. If the `mandatory-parameters` wasn't specified at
  creation time, or if you want to override any default values by specifying
  your own values for the parameters, you must specify the
  `parameters` field. For these additional examples, see [Command usage scenarios](remote-command-use-cases.md "remote-command-use-cases.md").
- You can specify up to three name-value pairs for the
  `mandatory-parameters` field. However, when executing the
  command on the vehicle, only one name-value pair is accepted, and the
  `name` field must use the fully qualified name with the
  `$actuatorPath.` prefix.

### Obtain account-specific data plane

endpoint

Before you run the API command, you must obtain the account-specific endpoint URL
for the `iot:Jobs` endpoint. For example, if you run this command:

```
aws iot describe-endpoint --endpoint-type iot:Jobs
```

It will return the account-specfic endpoint URL as shown in the sample response
below.

```
{
    "endpointAddress": "`<account-specific-prefix>`.jobs.iot.`<region>`.amazonaws.com"
}
```

### Send a command example

To send a command to a vehicle, run the following command.

- Replace `command-arn` with the ARN for the
  command that you want to execute. You can obtain this information from the
  response of the `create-command` CLI command.
- Replace `target-arn` with the ARN for the target
  device, or AWS IoT thing, for which you want to execute the command.

###### Note

You can specify the target ARN of an AWS IoT thing (AWS IoT FleetWise vehicle). Thing groups and fleets aren't currently supported.

- Replace `endpoint-url` with the account-specific
  endpoint that you obtained in [Obtain account-specific data plane
  endpoint](#send-remote-command-endpoint "#send-remote-command-endpoint"), prefixed by
  `https://`, for example,
  `https://`123456789012abcd`.jobs.iot.`ap-south-1`.amazonaws.com`.
- Replace `name` and
  `value` with the
  `mandatory-parameters` field that you specified when you
  created the command using the `create-command` CLI.

The `name` field is the fully qualified name as defined in the
signal catalog with `$actuatorPath.` as the prefix. For example,
`name` can be
`$actuatorPath.Vehicle.Chassis.SteeringWheel.HandsOff.HandsOffSteeringMode`
and `value` can be a boolean that indicates a steering mode
status like `{"B": false}`.

- (Optional) You can also specify an additional parameter,
  `executionTimeoutSeconds`. This optional field specifies the
  time in seconds within which the device must respond with the execution
  result. You can configure the timeout to a maximum value of 24 hours.

When the command execution has been created, a timer starts. Before the
timer expires, if the command execution status doesn't change to a status
that makes it terminal, such as `SUCCEEDED` or
`FAILED`, then the status automatically changes to
`TIMED_OUT`.

###### Note

The device can also report a `TIMED_OUT` status, or
override this status to a status such as `SUCCEEDED`,
`FAILED`, or `REJECTED`, and the command
execution will become terminal. For more information, see [Command execution
timeout status](remote-command-concepts-states.md#remote-command-execution-status-timeout "remote-command-concepts-states.md#remote-command-execution-status-timeout").

```
aws iot-jobs-data start-command-execution \
    --command-arn `command-arn` \
    --target-arn `target-arn` \
    --execution-timeout-seconds `30` \
    --endpoint-url `endpoint-url` \
    --parameters '[
        {
            "name": `name`,
            "value": `value`
        }
   ]'
```

The `StartCommandExecution` API operation returns a command execution
ID. You can use this ID to query the command execution status, details, and command
execution history.

```
{
    "executionId": "07e4b780-7eca-4ffd-b772-b76358da5542"
 }
```

After you run the command, your devices will receive a notification that contains
the following information. The `issued_timestamp_ms` field corresponds to
the time that the `StartCommandExecution` API was invoked. The
`timeout_ms` corresponds to the time out value that's configured
using the `executionTimeoutSeconds` parameter when invoking the
`StartCommandExecution` API.

```
timeout_ms: `9000000`
issued_timestamp_ms: `1723847831317`
```

## Update command execution

result

To update the status of the command execution, your device must have established an
MQTT connection and subscribed to the following commands request topic.

In this example, replace `<device-id>`
with the unique identifier of your target device, which can be the
`VehicleId` or the thing name, and
`<execution-id>` with the identifier
for the command execution.

###### Note

- The payload must use the protobuf format.
- It is optional for your devices to subscribe to the `/accepted`
  and `/rejected` response topics. Your devices will receive these
  response messages even if they haven't explicitly subscribed to them.

```
// Request topic
$aws/devices/`<DeviceID>`/command_executions/+/request/protobuf

// Response topics (Optional)
$aws/devices/`<DeviceID>`/command_executions/`<ExecutionId>`/response/accepted/protobuf
$aws/devices/`<DeviceID>`/command_executions/`<ExecutionId>`/response/rejected/protobuf
```

Your device can publish a message to the commands response topic. After processing the
command, it sends a protobuf-encoded response to this topic. The
`<DeviceID>` field must match the corresponding
field in the request topic.

```
$aws/devices/`<DeviceID>`/command_executions/`<ExecutionId>`/response/`<PayloadFormat>`
```

After your device publishes a response to this topic, you can retrieve the updated
status information using the `GetCommandExecution` API. The status of a
command execution can be any of those listed here.

- `IN_PROGRESS`
- `SUCCEEDED`
- `FAILED`
- `REJECTED`
- `TIMED_OUT`

Note that a command execution in any of the statuses `SUCCEEDED`,
`FAILED`, and `REJECTED` is terminal, and the status is
reported by the device. When a command execution is terminal, this means that no further
updates will be made to its status or related fields. A `TIMED_OUT` status
may be reported by the device or the cloud. If reported by the cloud, an update of the
status reason field may later be made by the device.

For example, the following shows a sample MQTT message that's published by the
device.

###### Note

For the command execution status, if your devices use the
`statusReason` object to publish the status information, you must
make sure that:

- The `reasonCode` uses the pattern `[A-Z0-9_-]+`, and
  it does not exceed 64 characters in length.
- The `reasonDescription` doesn't exceed 1,024 characters in length.
  It can use any characters except control characters such as new lines.

```
{
    "deviceId": "",
    "executionId": "",
    "status": "CREATED",
    "statusReason": {
        "reasonCode": "",
        "reasonDescription": ""
    }
}
```

For an example that shows how you can use the AWS IoT Core MQTT test client to subscribe
to the topics and see the command execution messages, see [Viewing commands updates using the MQTT test client](../../../iot/latest/developerguide/iot-remote-command-execution-start-monitor.md#iot-remote-command-execution-update-mqtt "../../../iot/latest/developerguide/iot-remote-command-execution-start-monitor.md#iot-remote-command-execution-update-mqtt") in the
_AWS IoT Core developer guide_.

## Get command execution

You can use the [`GetCommandExecution`](../../../iot/latest/apireference/API_GetCommandExecution.md "../../../iot/latest/apireference/API_GetCommandExecution.md") AWS IoT control plane API operation to
retrieve information about a command execution. You must have already executed this
command using the `StartCommandExecution` API operation.

To retrieve the metadata of an executed command, run the following command.

- Replace `execution-id` with the ID of the command.
  You can obtain this information from the response of the
  `start-command-execution` CLI command.
- Replace `target-arn` with the ARN for the target
  vehicle, or AWS IoT thing, for which you want to execute the command.

```
aws iot get-command-execution --execution-id `execution-id` \
    --target-arn `target-arn`
```

The `GetCommandExecution` API operation returns a response that contains
information about the ARN of the command execution, the execution status, and the time
when the command started executing and when it completed. The following code shows a
sample response from the API request.

To provide additional context about the status of each command execution, the commands
feature provides a `statusReason` object. The object contains two fields,
`reasonCode` and `reasonDescription`. Using these fields, your
devices can provide additional information about the status of a command execution. This
information will override any default `reasonCode` and
`reasonDescription` that's reported from the cloud.

To report this information, your devices can publish the updated status information to
the cloud. Then, when you retrieve the command execution status using the
`GetCommandExecution` API, you'll see the latest status codes.

###### Note

The `completedAt` field in the execution response corresponds to the
time when the device reports a terminal status to the cloud. In the case of
`TIMED_OUT` status, this field will be set only when the device
reports A timeout. When the `TIMED_OUT` status is set by the cloud, the
`TIMED_OUT` status is not updated. For more information about the
time out behavior, see [Command execution
timeout status](remote-command-concepts-states.md#remote-command-execution-status-timeout "remote-command-concepts-states.md#remote-command-execution-status-timeout").

```
{
    "executionId": "07e4b780-7eca-4ffd-b772-b76358da5542",
    "commandArn": "arn:aws:iot:ap-south-1:123456789012:command/LockDoor",
    "targetArn": "arn:aws:iot:ap-south-1:123456789012:thing/myFrontDoor",
    "status": "SUCCEEDED",
    "statusReason": {
        "reasonCode": "65536",
        "reasonDescription": "SUCCESS"
    },
    "createdAt": "2024-03-23T00:50:10.095000-07:00",
    "completedAt": "2024-03-23T00:50:10.095000-07:00",
    "Parameters": '{
         "$actuatorPath.Vehicle.Chassis.SteeringWheel.HandsOff.HandsOffSteeringMode":
         { "B": true }
    }'
}
```

## List command executions in your

account

Use the [`ListCommandExecutions`](../../../iot/latest/apireference/API_ListCommandExecutions.md "../../../iot/latest/apireference/API_ListCommandExecutions.md") AWS IoT Core control plane HTTP API
operation to list all command executions in your account. The example uses the
AWS CLI.

###### Topics

- [Considerations when listing
  command executions](#list-remote-command-considerations "#list-remote-command-considerations")
- [List command executions
  example](#list-remote-command-example "#list-remote-command-example")

### Considerations when listing

command executions

The following are some considerations when using the
`ListCommandExecutions` API.

- You must specify at least the `targetArn` or the
  `commandArn` depending on whether you want to list executions
  for a particular command or a target vehicle. The API request cannot be
  empty and cannot contain both fields in the same request.
- You must provide only the `startedTimeFilter` or the
  `completedTimeFilter` information. The API request cannot be
  empty and cannot contain both fields in the same request. You can use the
  `before` and `after` fields of the object to list
  command executions that were either created or completed within a specific
  timeframe.
- Both the `before` and `after` fields must not be
  greater than the current time. By default, if you don't specify any value,
  the `before` field is the current time and `after`
  field is current time - 6 months. That is, depending on the filter that you
  use, the API will list all executions that were either created or completed
  within the last six months.
- You can use the `sort-order` parameter to specify whether you
  want to list the executions in the ascending order. By default, the
  executions will be listed in the descending order if you don't specify this
  field.
- You cannot filter the command executions based on their status when
  listing command executions for a command ARN.

### List command executions

example

The following example shows you how to list command executions in your
AWS account.

When running the command, you must specify whether to filter the list to
display only command executions that were created for a particular device
using the `targetArn`, or executions for a particular command
specified using the `commandArn`.

In this example, replace:

- `<target-arn>` with
  the Amazon Resource Number (ARN) of the device for which you're
  targeting the execution, such as
  `arn:aws:iot:`us-east-1`:`123456789012`:thing/`b8e4157c98f332cffb37627f``.
- `<target-arn>` with
  the Amazon Resource Number (ARN) of the device for which you're
  targeting the execution, such as
  `arn:aws:iot:`us-east-1`:`123456789012`:thing/`b8e4157c98f332cffb37627f``.
- `<after>` with the
  time after which you want to list the executions that were created,
  for example, `2024-11-01T03:00`.

```
aws iot list-command-executions \
--target-arn ``<target-arn>`` \
--started-time-filter '{after=``<after>``}' \
--sort-order "ASCENDING"
```

Running this command generates a response that contains a list of command
executions that you created, and the time when the executions started
executing, and when it completed. It also provides status information, and
the `statusReason` object that contains additional information
about the status.

```
{
    "commandExecutions": [
        {
            "commandArn": "arn:aws:iot:us-east-1:123456789012:command/TestMe002",
            "executionId": "b2b654ca-1a71-427f-9669-e74ae9d92d24",
            "targetArn": "arn:aws:iot:us-east-1:123456789012:thing/b8e4157c98f332cffb37627f",
            "status": "TIMED_OUT",
            "createdAt": "2024-11-24T14:39:25.791000-08:00",
            "startedAt": "2024-11-24T14:39:25.791000-08:00"
        },
        {
            "commandArn": "arn:aws:iot:us-east-1:123456789012:command/TestMe002",
            "executionId": "34bf015f-ef0f-4453-acd0-9cca2d42a48f",
            "targetArn": "arn:aws:iot:us-east-1:123456789012:thing/b8e4157c98f332cffb37627f",
            "status": "IN_PROGRESS",
            "createdAt": "2024-11-24T14:05:36.021000-08:00",
            "startedAt": "2024-11-24T14:05:36.021000-08:00"
        }
    ]
}
```

## Delete a command execution

If you no longer want to use a command execution, you can remove it permanently from
your account.

###### Note

A command execution can be deleted only if it has entered a terminal status, such
as `SUCCEEDED`, `FAILED`, or `REJECTED`.

The following example shows you how to delete a command execution using the
`delete-command-execution` AWS CLI command. Replace
`<execution-id>` with the identifier
of the command execution that you're deleting.

```
aws iot delete-command-execution --execution-id `<execution-id>`
```

If the API request is successful, then the command execution generates a status code
of 200. You can use the `GetCommandExecution` API to verify that the command
execution no longer exists in your account.
