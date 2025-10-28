# Start and monitor command

executions

After you've created a command resource, you can start a command execution on the target
device. Once the device starts executing the command, it can start updating the result of
the command execution and publish status updates and result information to the MQTT reserved
topics. You can then retrieve the status of the command execution and monitor the status of
the executions in your account.

This section shows how you can start and monitor commands using both the AWS IoT console and
the AWS CLI.

###### Start and monitor commands operations

- [Start a command execution](#iot-remote-command-execution-start "#iot-remote-command-execution-start")
- [Update the result of a command
  execution](#iot-remote-command-execution-update "#iot-remote-command-execution-update")
- [Retrieve a command execution](#iot-remote-command-execution-get "#iot-remote-command-execution-get")
- [Viewing commands updates
  using the MQTT test client](#iot-remote-command-execution-update-mqtt "#iot-remote-command-execution-update-mqtt")
- [List command executions in your
  AWS account](#iot-remote-command-execution-list "#iot-remote-command-execution-list")
- [Delete a command execution](#iot-remote-command-execution-delete "#iot-remote-command-execution-delete")

## Start a command execution

###### Important

You are solely responsible for deploying commands in a manner that is safe and
compliant with applicable laws.

Before you start a command execution, you must make sure that:

- You have created a command in the AWS IoT namespace and provided the payload
  information. When you start executing the command, the device will process the
  instructions in the payload and perform the actions specified. For information
  about creating commands, see [Create a command resource](iot-remote-command-create-manage.md#iot-remote-command-create "iot-remote-command-create-manage.md#iot-remote-command-create").
- Your device has subscribed to the MQTT reserved topics for commands. When you
  start the command execution, the payload information will be published to the
  following reserved MQTT request topic.

In this case, `<devices>` can be either be IoT
things or MQTT clients, and `<DeviceID>` is the
thing name, or the client ID. The supported
`<PayloadFormat>` are JSON and CBOR. For more
information about commands topics, see [Commands topics](reserved-topics.md#reserved-topics-commands "reserved-topics.md#reserved-topics-commands").

```
$aws/commands/`<devices>`/`<DeviceID>`/executions/+/request/`<PayloadFormat>`
```

If the `<PayloadFormat>` is not JSON and CBOR,
then following shows the commands topic format.

```
$aws/commands/`<devices>`/`<DeviceID>`/executions/+/request
```

When you want to run the command, you must specify the target device that will
receive the command and perform the instructions specified. The target device
can either be an AWS IoT thing, or the client ID if the device has not been
registered in the AWS IoT registry. After receiving the command payload, the
device can start executing the command and perform the specified actions.

#### AWS IoT thing

The target device for the command can be an AWS IoT thing that you have
registered in the AWS IoT thing registry. Things in AWS IoT make it easier to
search and manage your devices.

You can register your device as a thing when you connect your device to
AWS IoT from the [Connect device page](https://console.aws.amazon.com/iot/home#/connect-overview "https://console.aws.amazon.com/iot/home#/connect-overview") or using the [`CreateThing`](../apireference/API_CreateThing.md "../apireference/API_CreateThing.md")
API. You can find an existing thing for which you want to run the command
from the [Thing Hub](https://console.aws.amazon.com/iot/home#/thinghub "https://console.aws.amazon.com/iot/home#/thinghub")
page of the AWS IoT console or using the [`DescribeThing`](../apireference/API_DescribeThing.md "../apireference/API_DescribeThing.md") API. For information about how to
register your device as an AWS IoT thing, see [Managing things with the
registry](thing-registry.md "thing-registry.md").

#### Client ID

If your device hasn't been registered as a thing with AWS IoT, you can use
the client ID instead.

The client ID is a unique identifier that you assign to your device or
client. The client ID is defined in the MQTT protocol, and it can contain
alphanumeric characters, underscores, or dashes. It must be unique to each
device that connects to AWS IoT.

###### Note

- If your device has been registered as a
  _thing_ in the AWS IoT registry, the client
  ID can be the same as the thing name.
- If your command execution targets a specific MQTT client ID,
  to receive the command payload from the client ID based commands
  topic, your device must connect to AWS IoT using the same client
  ID.

The client ID is typically the MQTT client ID that your devices can use
when connecting to AWS IoT Core. This ID is used by AWS IoT to identify each
specific device and manage connections and subscriptions.

The timeout indicates the duration in seconds within which your device can
provide the result of the command execution.

After you create a command execution, a timer starts. If the device went
offline or failed to report the execution result within the timeout duration,
the command execution will time out, and the execution status will be reported
as `TIMED_OUT`.

This field is optional and will default to 10 seconds if you don't specify any
value. You can also configure the timeout to a maximum value of 12 hours.

#### Time out value and

`TIMED_OUT` execution status

A time out can be reported by both the cloud and the device.

After the command is sent to the device, a timer starts. If there was no
response received from the device within the specified time out duration, as
described above. In this case, the cloud sets the command execution status
as `TIMED_OUT` with reason code as
`$NO_RESPONSE_FROM_DEVICE`.

This could happen in either of the following cases.

- The device went offline while executing the command.
- The device failed to complete running the command within the
  specified duration.
- The device failed to report the updated status information within
  the timeout duration.

In this instance, when the execution status of `TIMED_OUT` is
reported from the cloud, the command execution is non-terminal. Your device
can publish a response that overrides the status to any of the terminal
statuses, `SUCCEEDED`, `FAILED`, or
`REJECTED`. The command execution now becomes terminal and
doesn't accept any further updates.

Your device can also update a `TIMED_OUT` status initiated by
the cloud by reporting that a time out occurred when it was executing the
command. In this case, the command execution status stays at
`TIMED_OUT` but the `statusReason` object will be
updated based on the information reported by the device. The command
execution will now become terminal and no further updates will be
accepted.

#### Using MQTT

persistent sessions

You can configure MQTT persistent sessions to use with the AWS IoT Device Management commands
feature. This feature is especially useful in cases such as when your device
goes offline and you want to make sure that the device still receives the
command when it comes back online before the timeout duration, and performs
the instructions specified.

By default, the MQTT persistent session expiry is set to 60 minutes. If
your command execution time out is configured to a value that exceeds this
duration, command executions that run longer than 60 minutes can get
rejected by the message broker and it can fail. To run commands that are
longer than 60 minutes in duration, you can request an increase to the
persistent session expiry time.

###### Note

To ensure that you're using the MQTT persistent sessions feature
correctly, make sure that the Clean Start flag is set to zero. For more
information, see [MQTT persistent sessions](mqtt.md#mqtt-persistent-sessions "mqtt.md#mqtt-persistent-sessions").

To start running the command from the console, go to the [Command Hub](https://console.aws.amazon.com/iot/home#/commandHub "https://console.aws.amazon.com/iot/home#/commandHub") page of the AWS IoT console and
perform the following steps.

1. To run the command that you've created, choose **Run
   command**.
2. Review information about the command that you've created, the payload
   file and format type, and the reserved MQTT topics.
3. Specify the target device for which you want to run the command. The
   device can be specified as an AWS IoT thing if it has been registered with
   AWS IoT, or using the client ID if your device has not been registered
   yet. For more information, see [Target device
   considerations](#iot-command-execution-target "#iot-command-execution-target")
4. (Optional) Configure a time out value for the command that determines
   the duration for which you want the command to run before it times out.
   If your command needs to run longer than 60 minutes, you may have to
   increase the MQTT persistent sessions expiry time. For more information,
   see [Command execution timeout
   considerations](#iot-command-execution-timeout "#iot-command-execution-timeout").
5. Choose **Run command**.
   Use the [`StartCommandExecution`](../apireference/API_StartCommandExecution.md "../apireference/API_StartCommandExecution.md") HTTP data plane API
   operation to start a command execution. The API request and response are
   correlated by the command execution ID. After the device completes executing the
   command, it can report the status and execution result to the cloud by
   publishing a message to the commands response topic. For a custom response code,
   application codes that you own can process the response message and post the
   result to AWS IoT.

If your devices have subscribed to the commands request topic, the
`StartCommandExecution` API will publish the payload message to
the topic. The payload can use any format of your choice. For more information,
see [Command payload](iot-remote-command-create-manage.md#iot-commands-payload "iot-remote-command-create-manage.md#iot-commands-payload").

```
$aws/commands/`<devices>`/`<DeviceID>`/executions/+/request/`<PayloadFormat>`
```

If the payload format is not JSON or CBOR, then following shows the format of
the commands request topic.

```
$aws/commands/`<devices>`/`<DeviceID>`/executions/+/request
```

#### Sample IAM

policy

Before you use this API operation, make sure that your IAM policy
authorizes you to perform this action on the device. The following example
shows an IAM policy that allows the user permission to perform the
`StartCommandExecution` action.

In this example, replace:

- `region` with your
  AWS Region, such as `ap-south-1`.
- `account-id` with your
  AWS account number, such as
  `123456789012`.
- `command-id` with a unique
  identifier for your AWS IoT command, such as
  `LockDoor`. If you
  want to send more than one command, you can specify these commands
  in the IAM policy.
- `devices` with either
  `thing` or `client` depending on whether
  your devices have been registered as AWS IoT things, or are specified
  as MQTT clients.
- `device-id` with your AWS IoT
  `thing-name` or `client-id`.

```
{
  "Effect": "Allow",
  "Action": [
      "iot:StartCommandExecution"
  ],
  "Resource": [
      "arn:aws:iot:`region`:`account-id`:command/`command-id`",
      "arn:aws:iot:`region`:`account-id`:`devices`/`device-id`"
  ]
}
```

#### Obtain

account-specific data plane endpoint

Before you run the API command, you must obtain the account-specific
endpoint URL for the endpoint. If you're using dual-stack endpoints (IPv4
and IPv6), use the `iot:Data-ATS`. The `iot:Jobs`
endpoint is for IPv4 only. For example, if you run this command:

```
aws iot describe-endpoint --endpoint-type iot:Data-ATS
```

It will return the account-specfic endpoint URL as shown in the sample
response below.

```
{
    "endpointAddress": "`<account-specific-prefix>`-ats.iot.`<region>`.api.com"
}
```

#### Start a command

execution example (AWS CLI)

The following example displays how to start executing a command using the
`start-command-execution` AWS CLI command.

In this example, replace:

- `<command-arn>` with
  the ARN for the command that you want to execute. You can obtain
  this information from the response of the
  `create-command` CLI command. For example, if you're
  executing the command for changing the steering wheel mode, use
  `arn:aws:iot:`region`:`account-id`:command/`SetComfortSteeringMode``.
- `<target-arn>` with
  the Thing ARN for the target device, which can be an IoT thing or
  MQTT client, for which you want to execute the command. For example,
  if you're executing the command for the target device
  `myRegisteredThing`, use
  `arn:aws:iot:`region`:`account-id`:thing/`myRegisteredThing``.
- `<endpoint-url>` with
  the account-specific endpoint that you obtained in [Obtain
  account-specific data plane endpoint](#iot-remote-command-execution-start-endpoint "#iot-remote-command-execution-start-endpoint"),
  prefixed by `https://`. For example,
  `https://`123456789012abcd`.jobs.iot.`ap-south-1`.amazonaws.com`.
- (Optional) You can also specify an additional parameter,
  `executionTimeoutSeconds`, when performing the
  `StartCommandExecution` API operation. This optional
  field specifies the time in seconds within which the device must
  complete executing the command. By default, the value is 10 seconds.
  When the command execution status is `CREATED`, a timer
  starts. If the command execution result is not received before the
  timer expires, then the status automatically changes to
  `TIMED_OUT`.

```
aws iot-jobs-data start-command-execution \
    --command-arn `<command-arn>`  \
    --target-arn `<target-arn>` \
    --endpoint `<endpoint-url>` \
    --execution-timeout-seconds `900`
```

Running this command returns a command execution ID. You can use this ID
to query the command execution status, details, and command execution
history.

###### Note

If the command has been deprecated, then the
`StartCommandExecution` API request will fail with a
validation exception. To fix this error, first restore the command using
the `UpdateCommand` API, and then perform the
`StartCommandExecution` request.

```
{
    "executionId": "07e4b780-7eca-4ffd-b772-b76358da5542"
}
```

## Update the result of a command

execution

Use the `UpdateCommandExecution` MQTT data plane API operation to update
the status or result of a command execution.

###### Note

Before you use this API:

- Your device must have established an MQTT connection and subscribed to the
  commands request and response topics. For more information, see [High level commands workflow](iot-remote-command-workflow.md "iot-remote-command-workflow.md").
- You must have already executed this command using the
  `StartCommandExecution` API operation.

Before you use this API operation, make sure that your IAM policy authorizes
your device to perform these actions. Following shows an example policy that
authorizes your device to perform the action. For additional sample IAM
policies that allow the user permission to perform the
`UpdateCommandExecution` action, see [Connect and publish policy examples](connect-and-pub.md "connect-and-pub.md").

In this example, replace:

- `Region` with your AWS Region,
  such as `ap-south-1`.
- `AccountID` with your
  AWS account number, such as
  `123456789012`.
- `ThingName` with the name of
  your AWS IoT thing for which you are targeting the command execution, such
  as `myRegisteredThing`.
- `commands-request-topic` and
  `commands-response-topic`
  with the names of your AWS IoT commands request and response topics. For
  more information, see [High level commands workflow](iot-remote-command-workflow.md "iot-remote-command-workflow.md").

#### Sample

IAM policy for MQTT client ID

The following code shows a sample device policy when using MQTT client
ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iot:Publish",
 "Resource": [
 "arn:aws:iot:us-east-1:123456789012:topic/$aws/commands/clients/${iot:ClientId}/executions/*/response",
 "arn:aws:iot:us-east-1:123456789012:topic/$aws/commands/clients/${iot:ClientId}/executions/*/response/json"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iot:Receive",
 "Resource": [
 "arn:aws:iot:us-east-1:123456789012:topic/$aws/commands/clients/${iot:ClientId}/executions/*/request",
 "arn:aws:iot:us-east-1:123456789012:topic/$aws/commands/clients/${iot:ClientId}/executions/*/response/accepted",
 "arn:aws:iot:us-east-1:123456789012:topic/$aws/commands/clients/${iot:ClientId}/executions/*/response/rejected",
 "arn:aws:iot:us-east-1:123456789012:topic/$aws/commands/clients/${iot:ClientId}/executions/*/request/json",
 "arn:aws:iot:us-east-1:123456789012:topic/$aws/commands/clients/${iot:ClientId}/executions/*/response/accepted/json",
 "arn:aws:iot:us-east-1:123456789012:topic/$aws/commands/clients/${iot:ClientId}/executions/*/response/rejected/json"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iot:Subscribe",
 "Resource": [
 "arn:aws:iot:us-east-1:123456789012:topicfilter/$aws/commands/clients/${iot:ClientId}/executions/+/request",
 "arn:aws:iot:us-east-1:123456789012:topicfilter/$aws/commands/clients/${iot:ClientId}/executions/+/response/accepted",
 "arn:aws:iot:us-east-1:123456789012:topicfilter/$aws/commands/clients/${iot:ClientId}/executions/+/response/rejected",
 "arn:aws:iot:us-east-1:123456789012:topicfilter/$aws/commands/clients/${iot:ClientId}/executions/+/request/json",
 "arn:aws:iot:us-east-1:123456789012:topicfilter/$aws/commands/clients/${iot:ClientId}/executions/+/response/accepted/json",
 "arn:aws:iot:us-east-1:123456789012:topicfilter/$aws/commands/clients/${iot:ClientId}/executions/+/response/rejected/json"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iot:Connect",
 "Resource": "arn:aws:iot:us-east-1:123456789012:client/${iot:ClientId}"
 }
 ]
}`

```

#### Sample

IAM policy for IoT thing

The following code shows a sample device policy when using an AWS IoT
thing.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iot:Publish",
 "Resource": "arn:aws:iot:us-east-1:123456789012:topic/$aws/commands/things/${iot:Connection.Thing.ThingName}/executions/*/response"
 },
 {
 "Effect": "Allow",
 "Action": "iot:Receive",
 "Resource": [
 "arn:aws:iot:us-east-1:123456789012:topic/$aws/commands/things/${iot:Connection.Thing.ThingName}/executions/*/request",
 "arn:aws:iot:us-east-1:123456789012:topic/$aws/commands/things/${iot:Connection.Thing.ThingName}/executions/*/response/accepted",
 "arn:aws:iot:us-east-1:123456789012:topic/$aws/commands/things/${iot:Connection.Thing.ThingName}/executions/*/response/rejected",
 "arn:aws:iot:us-east-1:123456789012:topic/$aws/commands/things/${iot:Connection.Thing.ThingName}/executions/*/request/json",
 "arn:aws:iot:us-east-1:123456789012:topic/$aws/commands/things/${iot:Connection.Thing.ThingName}/executions/*/response/accepted/json",
 "arn:aws:iot:us-east-1:123456789012:topic/$aws/commands/things/${iot:Connection.Thing.ThingName}/executions/*/response/rejected/json"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iot:Subscribe",
 "Resource": [
 "arn:aws:iot:us-east-1:123456789012:topicfilter/$aws/commands/things/${iot:Connection.Thing.ThingName}/executions/+/request",
 "arn:aws:iot:us-east-1:123456789012:topicfilter/$aws/commands/things/${iot:Connection.Thing.ThingName}/executions/+/response/accepted",
 "arn:aws:iot:us-east-1:123456789012:topicfilter/$aws/commands/things/${iot:Connection.Thing.ThingName}/executions/+/response/rejected",
 "arn:aws:iot:us-east-1:123456789012:topicfilter/$aws/commands/things/${iot:Connection.Thing.ThingName}/executions/+/request/json",
 "arn:aws:iot:us-east-1:123456789012:topicfilter/$aws/commands/things/${iot:Connection.Thing.ThingName}/executions/+/response/accepted/json",
 "arn:aws:iot:us-east-1:123456789012:topicfilter/$aws/commands/things/${iot:Connection.Thing.ThingName}/executions/+/response/rejected/json"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iot:Connect",
 "Resource": "arn:aws:iot:us-east-1:123456789012:client/${iot:ClientId}"
 }
 ]
}`

```

After the command execution is received at the request topic, the device
processes the command. It then uses the `UpdateCommandExecution` API
to update the status and result of the command execution to the following response
topic.

```
$aws/commands/`<devices>`/`<DeviceID>`/executions/`<ExecutionId>`/response/`<PayloadFormat>`
```

In this example, `<DeviceID>` is
the unique identifier of your target device, and
`<execution-id>` is the
identifier of the command execution on the target device. The
`<PayloadFormat>` can be JSON or CBOR.

###### Note

If you haven't registered your device with AWS IoT, you can use the client
ID as your identifier instead of a thing name.

```
$aws/commands/clients/`<ClientID>`/executions/`<ExecutionId>`/response/`<PayloadFormat>`
```

#### Device reported updates to

execution status

Your devices can use the API to report any of the following status updates to
the command execution. For more information
about these statuses, see [Command execution status](iot-remote-command-concepts.md#iot-command-execution-status "iot-remote-command-concepts.md#iot-command-execution-status").

- `IN_PROGRESS`: When the device starts executing the
  command, it can update the status to `IN_PROGRESS`.
- `SUCCEEDED`: When the device successfully processes the
  command and completes executing it, the device can publish a message to
  the response topic as `SUCCEEDED`.
- `FAILED`: If the device failed to execute the command, it
  can publish a message to the response topic as
  `FAILED`.
- `REJECTED`: If the device failed to accept the command, it
  can publish a message to the response topic as
  `REJECTED`.
- `TIMED_OUT`: The command execution status can change to
  `TIMED_OUT` due to any of the following reasons.
  - The result of the command execution wasn't received. This can
    happen because the execution wasn't completed within the
    specified duration, or if the device failed to publish the
    status information to the response topic.
  - The device reports that a time out occurred when attempting to
    execute the command.

For more information about the `TIMED_OUT` status, see [Time out value and
TIMED_OUT execution status](#iot-command-execution-timeout-status "#iot-command-execution-timeout-status").

#### Considerations

when using the `UpdateCommandExecution` API

The following are some important considerations when using the
`UpdateCommandExecution` API.

- Your devices can use an optional `statusReason` object, which can be used
  to provide additional information about the execution. If your devices provide this object,
  then the `reasonCode` field of the object is required, but the
  `reasonDescription` field is optional.
- When your devices use the `statusReason` object, the `reasonCode`
  must use the pattern `[A-Z0-9_-]+`, and it does not exceed 64 characters
  in length. If you provide the `reasonDescription`, make sure that it doesn't exceed
  1,024 characters in length. It can use any characters except control characters such
  as new lines.
- Your devices can use an optional `result` object to provide information
  about the result of the command execution, such as the return value of a remote function
  call. If you provide the `result`, it must require at least one entry.
- In the `result` field, you specify the entries as key-value pairs. For
  each entry, you must specify the data type information as a string, boolean, or binary.
  A string data type must use the key `s`, a boolean data type uses the key
  `b`, and a binary data type must use the key `bin`. You must make
  sure that these data types are mentioned as lowercase.
- If you encounter an error when running the `UpdateCommandExecution` API,
  you can view the error in the `AWSIoTLogsV2` log group in Amazon CloudWatch. For information
  about enabling logging and viewing the logs, see [Configure AWS IoT logging](configure-logging.md "configure-logging.md").

#### `UpdateCommandExecution`

API example

The following code shows an example of how your device can use the
`UpdateCommandExecution` API to report the execution status, the
`statusReason` field to provide additional information about the status,
and the result field to provide information about the result of the execution, such
as the car battery percentage in this case.

```
{
  "status": "IN_PROGRESS",
  "statusReason": {
    "reasonCode": "200",
    "reasonDescription": "Execution_in_progress"
  },
  "result": {
        "car_battery": {
            "s": "car battery at 50 percent"
        }
    }
}
```

## Retrieve a command execution

After you run a command, you can retrieve information about the command execution from
the AWS IoT console and using the AWS CLI. You can obtain the following information.

###### Note

To retrieve the latest command execution status, your device must publish the
status information to the response topic using the
`UpdateCommandExecution` MQTT API, as described below. Until the
device publishes to this topic, the `GetCommandExecution` API will report
the status as `CREATED` or `TIMED_OUT`.

Each command execution that you create will have:

- An **Execution ID**, which is a unique identifier
  of the command execution.
- The **Status** of the command execution. When you
  run the command on the target device, the command execution enters a
  `CREATED` state. It can then transition to other command
  execution statuses as described below.
- The **Result** of the command execution.
- The unique **Command ID** and the target device
  for which executions have been created.
- The **Start date**, which shows the time when the
  command execution was created.

You can retrieve a command execution from the console using either of the
following methods.

- ###### From the Command hub page

Go to the [Command
Hub](https://console.aws.amazon.com/iot/home#/commandHub "https://console.aws.amazon.com/iot/home#/commandHub") page of the AWS IoT console and perform these
steps.

    1. Choose the command for which you created an execution on the
     target device.
    2. In the command details page, on the **Command
     history** tab, you'll see the executions that you
     created. Choose the execution for which you want to retrive
     information.
    3. If your devices used the `UpdateCommandExecution` API to
     provide the result information, you can then find this information in
     the **Results** tab of this page.

- ###### From the Thing hub page

If you chose an AWS IoT thing as your target device when running the
command, you can view the execution details from the Thing hub
page.

    1. Go to the [Thing
     Hub](https://console.aws.amazon.com/iot/home#/thinghub "https://console.aws.amazon.com/iot/home#/thinghub") page in the AWS IoT console and choose the thing
     for which you created the command execution.
    2. In the thing details page, on the **Command
     history**, you'll see the executions that you
     created. Choose the execution for which you want to retrive
     information.
    3. If your devices used the `UpdateCommandExecution` API to
     provide the result information, you can then find this information in
     the **Results** tab of this page.

Use the [`GetCommandExecution`](../apireference/API_GetCommandExecution.md "../apireference/API_GetCommandExecution.md") AWS IoT Core control plane HTTP
API operation to retrieve information about a command execution. You must have
already executed this command using the `StartCommandExecution` API
operation.

#### Sample IAM

policy

Before you use this API operation, make sure that your IAM policy
authorizes you to perform this action on the device. The following example
shows an IAM policy that allows the user permission to perform the
`GetCommandExecution` action.

In this example, replace:

- `region` with your
  AWS Region, such as `ap-south-1`.
- `account-id` with your
  AWS account number, such as
  `123456789012`.
- `command-id` with your
  unique AWS IoT command identifier, such as
  `LockDoor`.
- `devices` with either
  `thing` or `client` depending on whether
  your devices have been registered as AWS IoT things, or are specified
  as MQTT clients.
- `device-id` with your AWS IoT
  `thing-name` or `client-id`.

```
{
  "Effect": "Allow",
  "Action": [
      "iot:GetCommandExecution"
  ],
  "Resource": [
      "arn:aws:iot:`region`:`account-id`:command/`command-id`",
      "arn:aws:iot:`region`:`account-id`:`devices`/`device-id`"
  ]
}
```

#### Retrieve a

command execution example

The following example shows you how to retrieve information about a
command that was executed using the `start-command-execution`
AWS CLI command. The following example shows how you can retrieve information
about a command that was executed to turn off the steering wheel
mode.

In this example, replace:

- `<execution-id>` with the
  identifier for the command execution for which you want to retrieve
  information.
- `<target-arn>` with the
  Amazon Resource Number (ARN) of the device for which you're
  targeting the execution. You can obtain this information from the response
  of the `start-command-execution` CLI command.
- Optionally, if your devices used the `UpdateCommandExection`
  API to provide the execution result, you can specify whether to include the
  command execution result in the response of the `GetCommandExecution`
  API using the `GetCommandExecution` API.

```
aws iot get-command-execution
    --execution-id `<execution-id>` \
    --target-arn `<target-arn>` \
    --include-result
```

Running this command generates a response that contains information about
the ARN of the command execution, the execution status, and the time when it
started executing, and when it completed. It also provides a
`statusReason` object that contains additional information
about the status. For more information about the different statuses and
status reason, see [Command execution status](iot-remote-command-concepts.md#iot-command-execution-status "iot-remote-command-concepts.md#iot-command-execution-status").

The following code shows a sample response from the API request.

###### Note

The `completedAt` field in the execution response
corresponds to the time when the device reports a terminal status to the
cloud. In the case of `TIMED_OUT` status, this field will be
set only when the device reports a time out. When the
`TIMED_OUT` status is set by the cloud, the
`TIMED_OUT` status is not updated. For more information
about the time out behavior, see [Command execution timeout
considerations](#iot-command-execution-timeout "#iot-command-execution-timeout").

```
{
    "executionId": "07e4b780-7eca-4ffd-b772-b76358da5542",
    "commandArn": "arn:aws:iot:ap-south-1:123456789012:command/LockDoor",
    "targetArn": "arn:aws:iot:ap-south-1:123456789012:thing/myRegisteredThing",
    "status": "SUCCEEDED",
    "statusReason": {
        "reasonCode": "DEVICE_SUCCESSFULLY_EXECUTED",
        "reasonDescription": "SUCCESS"
    },
    "result": {
        "sn": { "s": "ABC-001" },
        "digital": { "b": true }
    },
    "createdAt": "2024-03-23T00:50:10.095000-07:00",
    "completedAt": "2024-03-23T00:50:10.095000-07:00"
}
```

## Viewing commands updates

using the MQTT test client

You can use the MQTT test client to view the message exchange over MQTT when using the
commands feature. After your device has established an MQTT connection with AWS IoT, you
can create a command, specify the payload, and then run it on the device. When you run
the command, if your device has subscribed to the MQTT reserved request topic for
commands, it will see the payload message published to this topic.

The device then receives the payload instructions and performs the specified
operations on the IoT device. It then uses the `UpdateCommandExecution` API
to publish the command execution result and status information to the MQTT reserved
response topics for commands. AWS IoT Device Management listens to updates on the reponse Topics and stores
the updated information and publishes logs to AWS CloudTrail and Amazon CloudWatch.
You can then retrieve the latest command execution information from the console or using
the `GetCommandExecution` API.

The following steps show how to use the MQTT test client to observe messages.

1. Open the [MQTT test client](https://console.aws.amazon.com/iot/home#/test "https://console.aws.amazon.com/iot/home#/test")
   in the AWS IoT console.
2. On the **Subscribe** tab, enter the following topic and then
   choose **Subscribe**, where
   `<thingId>` is the thing name of the device
   that you have registered with AWS IoT.

###### Note

You can find the thing name for your device from the [Thing Hub](https://console.aws.amazon.com/iot/home#/thinghub "https://console.aws.amazon.com/iot/home#/thinghub") page of the AWS IoT console, or
if haven't registered your device as a thing, you can register the device
when connecting to AWS IoT from the [Connect device page](https://console.aws.amazon.com/iot/home#/connect-overview "https://console.aws.amazon.com/iot/home#/connect-overview").

```
$aws/commands/things/`<thingId>`/executions/+/request
```

3. (Optional) On the **Subscribe** tab, you can also enter the
   following topics and choose **Subscribe**.

```
$aws/commands/things/+/executions/+/response/accepted/json
$aws/commands/things/+/executions/+/response/rejected/json
```

4. When you start a command execution, the message payload will be sent to the
   device using the request topic that the device has subscribed to,
   `$aws/commands/things/`<thingId>`/executions/+/request`.
   In the MQTT test client, you should see the command payload that contains the
   instructions for the device to process the command.
5. After the device starts executing the command, it can publish status updates
   to the following MQTT reserved response topic for commands.

```
$aws/commands/`<devices>`/`<device-id>`/executions/`<executionId>`/response/json
```

For example, consider a command that you executed to turn on the AC of your
car to reduce the temperature to a desired value. The following JSON shows a
sample message that the vehicle published to the response topic which shows that
it failed to execute the command.

```
{
  "deviceId": "My_Car",
  "executionId": "07e4b780-7eca-4ffd-b772-b76358da5542",
  "status": "FAILED",
  "statusReason": {
    "reasonCode": "CAR_LOW_ON_BATTERY",
    "reasonDescription": "Car battery is lower than 5 percent"
  }
}
```

In this case, you can charge your car's battery and then run the command
again.

## List command executions in your

AWS account

After you run a command, you can retrieve information about the command execution from
the AWS IoT console and using the AWS CLI. You can obtain the following information.

- An **Execution ID**, which is a unique identifier
  of the command execution.
- The **Status** of the command execution. When you
  run the command on the target device, the command execution enters a
  `CREATED` state. It can then transition to other command
  execution statuses as described below.
- The unique **Command ID** and the target device
  for which executions have been created.
- The **Start date**, which shows the time when the
  command execution was created.

You can see all the command executions from the console using either of the
following methods.

- ###### From the Command hub page

Go to the [Command
Hub](https://console.aws.amazon.com/iot/home#/commandHub "https://console.aws.amazon.com/iot/home#/commandHub") page of the AWS IoT console and perform these
steps.

    1. Choose the command for which you created an execution on the
     target device.
    2. In the command details page, go to the **Command
     history** tab, and you'll see a list of executions
     that you created.

- ###### From the Thing hub page

If you chose an AWS IoT thing as your target device when running the
command, and created multiple command executions for a single
device, you can view the executions for the device from the Thing
hub page.

    1. Go to the [Thing
     Hub](https://console.aws.amazon.com/iot/home#/thinghub "https://console.aws.amazon.com/iot/home#/thinghub") page in the AWS IoT console and choose the thing
     for which you created the executions.
    2. In the thing details page, on the **Command
     history**, you'll see a list of executions that
     you created for the device.

Use the [`ListCommandExecutions`](../apireference/API_ListCommandExecutions.md "../apireference/API_ListCommandExecutions.md") AWS IoT Core control plane HTTP
API operation to list all command executions in your account.

#### Sample IAM

policy

Before you use this API operation, make sure that your IAM policy
authorizes you to perform this action on the device. The following example
shows an IAM policy that allows the user permission to perform the
`ListCommandExecutions` action.

In this example, replace:

- `region` with your
  AWS Region, such as `ap-south-1`.
- `account-id` with your
  AWS account number, such as
  `123456789012`.
- `command-id` with your
  unique AWS IoT command identifier, such as
  `LockDoor`.

```
{
  "Effect": "Allow",
  "Action": "iot:ListCommandExecutions",
  "Resource": *
}
```

#### List command

executions example

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

For more information about the different statuses and status reason, see
[Command execution status](iot-remote-command-concepts.md#iot-command-execution-status "iot-remote-command-concepts.md#iot-command-execution-status").

## Delete a command execution

If you no longer want to use a command execution, you can remove it permanently from
your account.

###### Note

- A command execution can be deleted only if it has entered a terminal
  status, such as `SUCCEEDED`, `FAILED`, or
  `REJECTED`.
- This operation can be performed only using the AWS IoT Core API or the AWS CLI.
  It is not available from the console.

Before you use this API operation, make sure that your IAM policy authorizes
your device to perform these actions. Following shows an example policy that
authorizes your device to perform the action.

In this example, replace:

- `Region` with your AWS Region,
  such as `ap-south-1`.
- `AccountID` with your
  AWS account number, such as
  `123456789012`.
- `CommandID` with the identifier
  of the command for which you want to delete the execution.
- `devices` with either
  `thing` or `client` depending on whether your
  devices have been registered as AWS IoT things, or are specified as MQTT
  clients.
- `device-id` with your AWS IoT
  `thing-name` or `client-id`.

```
{
  "Effect": "Allow",
  "Action": [
      "iot:DeleteCommandExecution"
  ],
  "Resource": [
      "arn:aws:iot:`region`:`account-id`:command/`command-id`",
      "arn:aws:iot:`region`:`account-id`:`devices`/`device-id`"
  ]
}
```

The following example shows you how to delete a command using the
`delete-command` AWS CLI command. Depending on your application,
replace `<execution-id>` with the
identifier for the command execution that you're deleting, and the
`<target-arn>` with the ARN
of your target device.

```
aws iot delete-command-execution \
--execution-id `<execution-id>` \
--target-arn `<target-arn>`
```

If the API request is successful, then the command execution generates a
status code of 200. You can use the `GetCommandExecution` API to
verify that the command execution no longer exists in your account.
