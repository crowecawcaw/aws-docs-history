# Commands concepts

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

Commands are instructions that are sent from the cloud to your target device. The
target device can be a vehicle and it must registered as an _AWS IoT
thing_ in the thing registry. The command can contain parameters that
define an action that the actuators of the vehicle need to perform. The vehicle then
parses the command and its parameters, and processes them to take the corresponding
action. It then responds to the cloud application with the status of the command
execution.

For the detailed workflow, see [Vehicles and commands](remote-command-vehicles.md "remote-command-vehicles.md").

###### Topics

- [Commands key concepts](#remote-command-concepts "#remote-command-concepts")
- [Command execution
  status](#remote-command-execution-status-codes "#remote-command-execution-status-codes")

## Commands key concepts

The following shows some key concepts for using the commands feature and
how it works with last known state (LKS) state templates.

**Command**

A _Command_ is an entity that you can use to send
instructions to a physical vehicle to have it perform actions such as
turning on the engine or changing the position of the windows. You can
pre-define a set of commands for specific use cases, or use them to
create reusable configurations for recurrent use cases. For example, you
can configure commands that can be used by an App to lock a vehicle's
door or to change the temperature remotely.

**Namespace**

When you use the commands feature, you must specify the namespace for
the command. When you create a command in AWS IoT FleetWise, you must choose
`AWS-IoT-FleetWise` as your namespace. When you use this
namespace, you must provide the parameters that will be used to run the
command on the vehicle. If you want to create a command in AWS IoT Device Management instead,
you must use the `AWS-IoT` namespace instead. For more
information, see [commands](../../../iot/latest/developerguide/iot-remote-command.md "../../../iot/latest/developerguide/iot-remote-command.md") in the _AWS IoT Device Management developer guide_.

**Command states**

The commands that you create will be in an
available state, which means that it can be
used to start a command execution on the vehicle. If a command becomes
outdated, you can deprecate the command. For a command in the
deprecated state, existing command executions
will run to completion. You cannot update the command or run any new
executions. To send new executions, you must restore the command so that
it becomes available.

You can also delete a command if it's no longer required. When you
mark a command for deletion, if the command has been deprecated for a
duration that's longer than the maximum timeout of 24 hours, the command
will be deleted immediately. If the command isn't deprecated, or has
been deprecated for a duration shorter than the maximum timeout, the
command will be in a pending deletion state. The command
will be removed automatically from your account after 24 hours.

**Parameters**

When creating a command, you can optionally specify the parameters
that you want the target vehicle to execute when running the command.
The command you create is a reusable configuration and it can be used to
send multiple command executions to your vehicle and execute them
concurrently. Alternatively, you can also specify the parameters only at
runtime and choose to perform a one-time operation of creating a command
and sending it to your vehicle.

**Target vehicle**

When you want to run the command, you must specify a target vehicle
that will receive the command and perform specific actions. The target
vehicle must have already been registered as a
_thing_ with AWS IoT. After you send the command to
the vehicle, it will start executing an instance of the command based on
the parameters and the values that you specified.

**Actuators**

When you want to run the command, you must specify the actuators on
the vehicle that will receive the command and their values that
determine the actions to be performed. You can optionally configure
default values for the actuators to avoid sending inaccurate commands.
For example, you can use a default value of `LockDoor` to a
door lock actuator so that the command doesn't accidentally unlock the
doors. For general information about actuators, see [Key concepts](how-iotfleetwise-works.md#key-concepts "how-iotfleetwise-works.md#key-concepts").

**Data type support**

The following data types are supported for the actuators that are used
for the commands feature.

###### Note

Arrays are not supported for telematics data, commands, or
last known state (LKS). You can only use the array data type for
vision systems data.

- Floating point types. The following types are
  supported.
  - Float (32 bits)
  - Double (64 bits)

- Integer (both signed and unsigned). The following integer
  types are supported.
  - int8 and uint8
  - int16 and uint16
  - int32 and uint32

- Long. The following long types are supported.
  - Long (int64)
  - Unsigned long (uint64)

- String
- Boolean

**Command execution**

A command execution is an instance of a command running on a target
device. The vehicle executes the command using either the parameters
that you specified when you created the command or when you started the
command execution. The vehicle then performs the operations specified
and returns the status of the execution.

###### Note

For a given vehicle, you can run multiple commands concurrently.
For information about the maximum number of concurrent executions
that you can run for each vehicle, see [AWS IoT Device Management commands quotas](../../../general/latest/gr/iot_device_management.md#commands-limits "../../../general/latest/gr/iot_device_management.md#commands-limits").

**Last known state (LKS) state
templates**

State templates provide a mechanism for vehicle owners to track the
state of their vehicle. To monitor the last known state (LKS) of your
vehicles in near-real time, you can create state templates and associate
them with your vehicles.

Using the commands feature, you can perform "On Demand" operations
that can be used for state data collection and processing. For example,
you can request the current vehicle state one-time (fetch), or activate
or deactivate previously deployed LKS state templates to start or stop
reporting vehicle data. For examples that show how to use commands with
state templates, see [Command usage scenarios](remote-command-use-cases.md "remote-command-use-cases.md").

## Command execution

status

After you start the command execution, your vehicle can publish the status of the
execution, and provide the reasons for the status as additional information about
the execution. The following sections describe the various command execution
statuses, and the status codes.

###### Topics

- [Command execution
  status reason code and description](#remote-command-execution-status-reason-codes "#remote-command-execution-status-reason-codes")
- [Command execution status
  and status codes](#remote-command-execution-status-codes "#remote-command-execution-status-codes")
- [Command execution
  timeout status](#remote-command-execution-status-timeout "#remote-command-execution-status-timeout")

### Command execution

status reason code and description

To report updates to the command execution status, your vehicles can use the
`UpdateCommandExecution` API to publish the updated status
information to the cloud, using the [Commands reserved topics](../../../iot/latest/developerguide/reserved-topics.md#reserved-topics-commands "../../../iot/latest/developerguide/reserved-topics.md#reserved-topics-commands") described in the _AWS IoT Core
developer guide_. When reporting the status
information, your devices can provide additional context about the status of
each command execution using the `StatusReason` object, and the
fields `reasonCode` and `reasonDescription` that are
contained within the object.

### Command execution status

and status codes

The following table shows the various command execution status codes and the
allowed statuses that a command execution can transition to. It also shows
whether a command execution is "terminal" (that is, no further status updates
are forthcoming), whether the change is initiated by the vehicle or the cloud,
and the different pre-defined status codes and how they map to the statuses that
are reported by the cloud.

- For information about how AWS IoT FleetWise uses the
  predefined status codes, and the `statusReason` object, see
  [Command status](https://github.com/aws/aws-iot-fleetwise-edge/blob/main/include/aws/iotfleetwise/ICommandDispatcher.h "https://github.com/aws/aws-iot-fleetwise-edge/blob/main/include/aws/iotfleetwise/ICommandDispatcher.h") in the _Edge Agent for AWS IoT FleetWise software
  documentation_.
- For additional information about terminal and non-terminal executions,
  and the transitions between the statuses, see [Command execution status](../../../iot/latest/developerguide/iot-remote-command-concepts.md#iot-command-execution-status "../../../iot/latest/developerguide/iot-remote-command-concepts.md#iot-command-execution-status") in the _AWS IoT Core
  developer guide_.

| Command execution status and source | Command execution status                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description      | Initiated by device/cloud? | Terminal execution?                                                                     | Allowed status transitions           | Pre-defined status codes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | -------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CREATED`                           | When the API request to start executing the command (`StartCommandExecution` API) is successful, the command execution status changes to `CREATED`.                                                                                                                                                                                                                                                                                                                                                                                          | Cloud            | No                         | <br>• `IN_PROGRESS` <br>• `SUCCEEDED` <br>• `FAILED` <br>• `REJECTED` <br>• `TIMED_OUT` | None                                 |
| `IN_PROGRESS`                       | When the vehicle starts executing the command, it can publish a message to the response topic to update the status to `IN_PROGRESS`.                                                                                                                                                                                                                                                                                                                                                                                                         | Device           | No                         | <br>• IN_PROGRESS <br>• SUCCEEDED <br>• FAILED <br>• REJECTED <br>• TIMED_OUT           | `COMMAND_STATUS_COMMAND_IN_PROGRESS` |
| `SUCCEEDED`                         | When the vehicle has successfully processed the command and completed the execution, it can publish a message to the response topic to update the status to `SUCCEEDED`.                                                                                                                                                                                                                                                                                                                                                                     | Device           | Yes                        | Not applicable                                                                          | `COMMAND_STATUS_SUCCEEDED`           |
| `FAILED`                            | When the vehicle failed to execute the command, it can publish a message to the response topic to update the status to `FAILED`.                                                                                                                                                                                                                                                                                                                                                                                                             | Device           | Yes                        | Not applicable                                                                          | `COMMAND_STATUS_EXECUTION_FAILED`    |
| `REJECTED`                          | If the vehicle fails to accept the command, it can publish a message to the response topic to update the status to `REJECTED`.                                                                                                                                                                                                                                                                                                                                                                                                               | Device           | Yes                        | Not applicable                                                                          | None                                 |
| `TIMED_OUT`                         | The command execution status can change to `TIMED_OUT` due to any of the following reasons. <br>• The result of the command execution wasn't received and the cloud automatically reports a `TIMED_OUT` status. <br>• The vehicle reports that a time out occurred when it was attempting to execute the command. In this case, the command execution becomes terminal. For more information about this status, see [Command execution timeout status](#remote-command-execution-status-timeout "#remote-command-execution-status-timeout"). | Device and cloud | No                         | <br>• SUCCEEDED <br>• FAILED <br>• REJECTED <br>• TIMED_OUT                             | `COMMAND_STATUS_EXECUTION_TIMEOUT`   | ### Command execution timeout status A command execution timeout can be reported both by the cloud and the device. After the command is sent to the device, a timer starts. If there was no response received from the device within the specified duration, the cloud reports a `TIMED_OUT` status. In this case, the command execution in `TIMED_OUT` status is non-terminal. The device can override this status to a terminal status, such as `SUCCEEDED`, `FAILED`, or `REJECTED`. It can also report that a timeout occurred when running the command. In this case, the command execution status stays at `TIMED_OUT` but the fields of the `StatusReason` object are updated based on the information reported by the device. The command execution in the `TIMED_OUT` status now becomes terminal. For additional information, see [Command execution timeout considerations](../../../iot/latest/developerguide/iot-remote-command-execution-start-monitor.md#iot-command-execution-timeout "../../../iot/latest/developerguide/iot-remote-command-execution-start-monitor.md#iot-command-execution-timeout") in the _AWS IoT Core developer guide_. |
