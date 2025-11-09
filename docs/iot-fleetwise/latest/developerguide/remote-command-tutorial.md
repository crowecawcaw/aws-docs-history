# Example: Using commands to control a vehicle

steering mode (AWS CLI)

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

The following example shows you how to use the commands feature using the
AWS CLI. This example uses an AWS IoT FleetWise vehicle as a target device to
show how you can send a command to remotely control the steering mode.

###### Topics

- [Overview of vehicle steering
  mode example](#iot-remote-command-tutorial-overview "#iot-remote-command-tutorial-overview")
- [Prerequisites](#iot-remote-command-tutorial-prereq "#iot-remote-command-tutorial-prereq")
- [IAM policy for using remote
  commands](#remote-command-policy "#remote-command-policy")
- [Run AWS IoT commands (AWS CLI)](#iot-remote-command-tutorial-run "#iot-remote-command-tutorial-run")
- [Cleaning up](#remote-command-tutorial-clean "#remote-command-tutorial-clean")

## Overview of vehicle steering

mode example

In this example, you'll:

1. Create a command resource for the operation using the
   `create-command` AWS CLI to change the steering mode of the
   vehicle.
2. Retrieve information about the command, such as the time when it was
   created or last updated using the `get-command` AWS CLI.
3. Send the command to the vehicle using the
   `start-command-execution` AWS CLI with the steering mode as a
   mandatory parameter, which will then get executed on the device.
4. Get the result of the command execution using the
   `get-command-execution` AWS CLI. You can check when the
   execution completes, and retrieve additional details such as the execution
   result, and the time it took to complete executing the command.
5. Perform clean up activities by removing any commands and command executions
   that you no longer want to use.

## Prerequisites

Before you run this example:

- Provision your AWS IoT FleetWise vehicle as an AWS IoT thing in
  the AWS IoT registry. You must also add a certificate to your thing and
  activate it, and attach a policy to your thing. Your device can then connect
  to the cloud and execute the commands. For more information,
  see [Provision vehicles](provision-vehicles.md "provision-vehicles.md").
- Create an IAM user and an IAM policy that grants you permission to
  perform the API operations for using commands, as shown in
  [IAM policy for using remote
  commands](#remote-command-policy "#remote-command-policy").

## IAM policy for using remote

commands

The following table shows a sample IAM policy that grants access to all the
control plane and data plane API operations for the commands
feature. The user of the application will have permissions to perform all remote
command API operations, as shown in the table.

| API operation            | API action    | Control/data plane | Protocol                                               | Description          | Resource |
| ------------------------ | ------------- | ------------------ | ------------------------------------------------------ | -------------------- | -------- |
| `CreateCommand`          | Control plane | HTTP               | Creates a command resource                             | • command            |
| `GetCommand`             | Control plane | HTTP               | Retrieves information about a command                  | • command            |
| `UpdateCommand`          | Control plane | HTTP               | Updates information about a command or to deprecate it | • command            |
| `ListCommands`           | Control plane | HTTP               | Lists commands in your account                         | • command            |
| `DeleteCommand`          | Control plane | HTTP               | Deletes a command                                      | • command            |
| `StartCommandExecution`  | Data plane    | HTTP               | Starts executing a command                             | • command<br>• thing |
| `UpdateCommandExecution` | Data plane    | MQTT               | Update a command execution                             | • command<br>• thing |
| `GetCommandExecution`    | Control plane | HTTP               | Retrieves information about a command execution        | • command<br>• thing |
| `ListCommandExecutions`  | Control plane | HTTP               | Lists command executions in your account               | • command<br>• thing |
| `DeleteCommandExecution` | Control plane | HTTP               | Deletes a command execution                            | • command<br>• thing |

In this example, replace:

- `us-east-1` with your AWS Region,
  such as `ap-south-1`.
- `111122223333` with your AWS account
  number, such as `57EXAMPLE833`.
- `command-id`,
  `command-id1`, and
  `command-id2` with your
  unique command identifier, such as `LockDoor` or
  `TurnOffAC`.
- `thing-name` with your AWS IoT thing
  name, such as `my_car`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "iot:CreateCommand",
 "iot:GetCommand",
 "iot:ListCommands",
 "iot:UpdateCommand",
 "iot:DeleteCommand"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:iot:`us-east-1`:`111122223333`:command/`command-id1`",
 "arn:aws:iot:`us-east-1`:`111122223333`:command/`command-id2`"
 ]
 },
 {
 "Action": [
 "iot:GetCommandExecution",
 "iot:ListCommandExecutions",
 "iot:DeleteCommandExecution"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:iot:`us-east-1`:`111122223333`:command/`command-id`",
 "arn:aws:iot:`us-east-1`:`111122223333`:thing/`thing-name`"
 ]
 },
 {
 "Action": "iot:StartCommandExecution",
 "Effect": "Allow",
 "Resource": [
 "arn:aws:iot:`us-east-1`:`111122223333`:command/`command-id`",
 "arn:aws:iot:`us-east-1`:`111122223333`:thing/`thing-name`"
 ]
 }
 ]
}`

```

## Run AWS IoT commands (AWS CLI)

The following shows how you can use the AWS CLI to perform commands
operations and change the vehicle steering mode.

1. ###### Create a command resource for the steering mode operation

Create the command that you want to send to your device using the
`create-command` CLI. In this example, specify:

    * `command-id` as
     ``TurnOffSteeringMode``
    * `role-arn` as
     `"arn:aws:iam:`accountId`:role/`FwCommandExecutionRole`"`
     The `role-arn` must be provided, as it is the IAM role that
     grants permissions to create and run commands on your vehicle. For more information, see [Grant AWS IoT Device Management permission to generate the
     payload for commands with AWS IoT FleetWise](controlling-access.md#generate-command-payload "controlling-access.md#generate-command-payload").
    * `display-name` as "``Turn off steering
     mode``"
    * `namespace` must be `AWS-IoT-FleetWise`
    * `mandatory-parameters` as a name-value pair, with
     `name` as
     "`$actuatorPath.Vehicle.Chassis.SteeringWheel.TurnOffSteeringMode`"
     and defaultValue as ``{ "S": "true"
     }``


    ###### Note

    You can also create a command without specifying any mandatory
     parameters. You must then specify the parameters to use when
     executing the command using the
     `start-command-execution` CLI. For an example,
     see [Command usage scenarios](remote-command-use-cases.md "remote-command-use-cases.md").

###### Important

When using the `AWS-IoT-FleetWise` namespace, you must
ensure that the `Name` field specified as part of the
`mandatory-parameters` use the `$actuatorPath.`
prefix, and the `Value` field must use the string data
type.

```
aws iot create-command \
    --command-id `TurnOffSteeringMode` \
    --role-arn "arn:aws:iam:`accountId`:role/`FwCommandExecutionRole`" \
    --display-name "`Turn off steering mode`" \
    --namespace AWS-IoT-FleetWise \
    --mandatory-parameters '[
      {
        "name": "`$actuatorPath.Vehicle.Chassis.SteeringWheel.TurnOffSteeringMode`",
        "defaultValue": { `"S": "true"` }
      }
    ]'
```

The following output shows a sample response from the CLI, where
`ap-south-1` and `123456789012` are examples of
the AWS Region and AWS account ID.

```
{
    "commandId": "TurnOffSteeringMode",
    "commandArn": "arn:aws:iot:ap-south-1:123456789012:command/TurnOffSteeringMode"
}
```

For additional examples on using this command, see [Create a command resource](create-manage-remote-command-cli.md#create-remote-command-cli "create-manage-remote-command-cli.md#create-remote-command-cli"). 2. ###### Retrieve information about the command

Run the following command to retrieve information about the command, where
`command-id` is the command ID in the output of the
`create-command` operation from above.

###### Note

If you create more than one command, you can use the `ListCommands`
API to list all commands in your account, and then use the `GetCommand` API
to obtain additional information about a specific command. For more information,
see [List commands in your account](create-manage-remote-command-cli.md#list-remote-command-cli "create-manage-remote-command-cli.md#list-remote-command-cli").

```
aws iot get-command --command-id `TurnOffSteeringMode`
```

Running this command generates the following response. You'll see the time
when the command was created and when it was last updated, any parameters that
you specified, and whether the command is available to run on the device.

```
{
    "commandId": "TurnOffSteeringMode",
    "commandArn": "arn:aws:iot:ap-south-1:123456789012:command/TurnOffSteeringMode",
    "namespace": "AWS-IoT-FleetWise",
    "mandatoryParameters":[
        {
            "name": "$actuatorPath.Vehicle.Chassis.SteeringWheel.TurnOffSteeringMode",
            "defaultValue": {"S": "true" }
        }
    ],
    "createdAt": "2024-03-23T00:50:10.095000-07:00",
    "lastUpdatedAt": "2024-03-23T00:50:10.095000-07:00",
    "deprecated": false
}
```

For additional examples on using this command, see [Retrieve information about a command](create-manage-remote-command-cli.md#get-remote-command-cli "create-manage-remote-command-cli.md#get-remote-command-cli"). 3. ###### Start the command execution

Run the following command to start executing the command, where
`command-arn` is the command ARN in the output of the
`get-command` operation from above. The `target-arn`
is the ARN of the target device for which you're executing the command, for
example, `myVehicle`.

In this example, since you provided default values for the parameters when
creating the command, the `start-command-execution` CLI can use
these values when executing the command. You can also choose to override the
default value by specifying a different value for the parameters when using
the CLI.

```
aws iot-data start-command-execution \
    --command-arn arn:aws:iot:`ap-south-1`:`123456789012`:command/`TurnOffSteeringMode` \
    --target-arn arn:aws:iot:`ap-south-1`:`123456789012`:thing/`myVehicle`
```

Running this command returns a command execution ID. You can use this ID
to query the command execution status, details, and command execution
history.

```
{
    "executionId": "07e4b780-7eca-4ffd-b772-b76358da5542"
}
```

For additional examples on using the CLI, see [Send a command (AWS CLI)](send-monitor-remote-command-cli.md#send-remote-command-cli "send-monitor-remote-command-cli.md#send-remote-command-cli"). 4. ###### Retrieve information about the command execution

Run the following command to retrieve information about the command that
you executed on the target device. Specify the `execution-id`,
which you obtained as output of the `start-command-execution`
operation from above, and the `target-arn`, which is the ARN of
the device that you're targeting.

###### Note

    * To obtain the latest status information, your devices must have
     published the updated status information to the MQTT reserved response
     topic for commands using the `UpdateCommandExecution` MQTT
     API. For more information, see [Update command execution
     result](send-monitor-remote-command-cli.md#update-remote-command-execution-cli "send-monitor-remote-command-cli.md#update-remote-command-execution-cli").
    * If you start more than one command execution, you can use the
     `ListCommandExecutions` API to list all command executions in
     your account, and then use the `GetCommandExecution` API
     to obtain additional information about a specific execution. For more information,
     see [List command executions in your
     account](send-monitor-remote-command-cli.md#list-remote-command-execution-cli "send-monitor-remote-command-cli.md#list-remote-command-execution-cli").

```
aws iot get-command-execution \
    --execution-id `<"07e4b780-7eca-4ffd-b772-b76358da5542">` \
    --target-arn arn:aws:iot:`us-east-1`:`<account>`:thing/`myVehicle`
```

Running this command returns information about the command execution, the
execution status, the time when it started executing, and the time when it
was completed. For example, the following response shows that the command
execution succeeded on the target device and the steering mode was turned
off.

```
{
    "executionId": "07e4b780-7eca-4ffd-b772-b76358da5542",
    "commandArn": "arn:aws:iot:ap-south-1:123456789012:command/TurnOffSteeringMode",
    "targetArn": "arn:aws:iot:ap-south-1:123456789012:thing/myVehicle",
    "result": "SUCCEEDED",
     "statusReason": {
        "reasonCode": "65536",
        "reasonDescription": "SUCCESS"
    },
    "result": {
        "KeyName": {
            "S": "",
            "B": true,
            "BIN": null
        }
    },
    "createdAt": "2024-03-23T00:50:10.095000-07:00",
    "completedAt": "2024-03-23T00:50:10.095000-07:00",
    "parameters": '{
         "$actuatorPath.Vehicle.Chassis.SteeringWheel.TurnOffSteeringMode":
         { "S": "true" }
    }'
}
```

## Cleaning up

Now that you've created a command and executed it on your device, if you no longer
intend to use this command, you can delete it. Any pending command executions that
are in progress will continue to run without getting impacted by the deletion
request.

###### Note

Alternatively, you can also deprecate a command if it's outdated and you might
need to use it later to run on the target device.

1. ###### (Optional) Deprecate the command resource

Run the following command to deprecate the command, where
`command-id` is the command ID in the output of the
`get-command` operation from above.

```
aws iot update-command \
   --command-id `TurnOffSteeringMode` \
   --deprecated
```

Running this command returns an output that shows the command has been
deprecated. You can also use the CLI to restore the command.

###### Note

You can also use the `update-command` CLI to update the display
name and description of a command. For additional information, see [Update or deprecate a command
resource](create-manage-remote-command-cli.md#update-remote-command-cli "create-manage-remote-command-cli.md#update-remote-command-cli").

```
{
    "commandId": "TurnOffSteeringMode",
    "deprecated": true,
    "lastUpdatedAt": "2024-05-09T23:16:51.370000-07:00"
}
```

2. ###### Delete the command

Run the following command to delete the command, specified by the
`command-id`.

###### Note

The deletion action is permanent and can't be undone.

```
aws iot delete-command --command-id `TurnOffSteeringMode`
```

If the deletion request is successful, you'll see a HTTP
`statusCode` of 202 or 204 depending on whether you marked
the command for deprecation and when it was deprecated. For more information
and an example, see [Delete a command resource](create-manage-remote-command-cli.md#delete-remote-command-cli "create-manage-remote-command-cli.md#delete-remote-command-cli").

You can use the `get-command` CLI to verify that the command
has been removed from your account. 3. ###### (Optional) Delete the command executions

By default, all command executions will be deleted in six months
from the date that you create them. You can view this information using
the `timeToLive` parameter from the `GetCommandExecution`
API.

Alternatively, if your command execution has become terminal, such
as when your execution status is one of `SUCCEEDED`, `FAILED`,
or `REJECTED`, you can delete the command execution. Run the
following command to delete the execution, where `execution-id` is the
Execution ID in the output of the `get-command-execution` operation
from above.

```
aws iot delete-command-execution \
            --execution-id `"07e4b780-7eca-4ffd-b772-b76358da5542"`
```

You can use the `get-command-execution` CLI to verify that the command
execution has been removed from your account.
