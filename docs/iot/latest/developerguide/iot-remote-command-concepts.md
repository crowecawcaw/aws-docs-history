# Commands concepts and status

Use AWS IoT Commands to send instructions from the cloud to connected devices. To use this feature:

1. Create a command with a payload containing the configurations required to run on the device.
2. Specify the target device that will receive the payload and perform the actions.
3. Execute the command on the target device and retrieve status information. To troubleshoot issues, see CloudWatch logs.
   For more information about this workflow, see [High-level commands workflow](iot-remote-command-workflow.md "iot-remote-command-workflow.md").

###### Topics

- [Commands key concepts](#iot-command-concepts "#iot-command-concepts")
- [Command states](#iot-command-states "#iot-command-states")
- [Command execution status](#iot-command-execution-status "#iot-command-execution-status")

## Commands key concepts

The following key concepts help you understand the Commands feature. Terms are used consistently throughout this documentation:

- _Command_ - A reusable template defining device instructions
- _Execution_ - An instance of a command running on a device
- _Thing name_ - Identifier for devices registered in IoT registry
- _Client ID_ - MQTT identifier for unregistered devices
- _Payload_ - The instruction data sent to devices
- _Topic_ - MQTT channel for command communication

**Commands**

Commands are instructions sent from the cloud to your IoT devices as MQTT messages. After receiving the payload, devices process the instructions and take corresponding actions, such as modifying configuration settings, transmitting sensor readings, or uploading logs. Devices then return results to the cloud, enabling remote monitoring and control.

**Namespace**

When creating a command, specify its namespace. For AWS IoT Device Management commands, use the default `AWS-IoT` namespace and provide either a payload or payloadTemplate. For AWS IoT FleetWise commands, use the `AWS-IoT-FleetWise` namespace. For more information, see [Remote commands](../../../iot-fleetwise/latest/developerguide/remote-commands.md "../../../iot-fleetwise/latest/developerguide/remote-commands.md") in the _AWS IoT FleetWise Developer Guide_.

**Payload**

When creating a command, provide a static payload that defines the actions the device must perform. The payload can use any supported format. To ensure devices correctly interpret the payload, we recommend specifying the payload format type. Devices using the MQTT5 protocol can follow the MQTT standard to identify the format. Format indicators for JSON or CBOR are available in the commands request topic.

**Payload template**

A payload template defines a command payload with placeholders that generate different payloads at runtime based on parameter values you provide. For example, instead of creating separate payloads for different temperature values, create one template with a temperature placeholder and specify the value during execution. This eliminates maintaining multiple similar payloads.

**Target device**

To execute a command, specify a target device using either its thing name (for devices registered with AWS IoT) or MQTT client ID (for unregistered devices). The client ID is a unique identifier defined in the [MQTT](mqtt.md "mqtt.md") protocol used to connect devices to AWS IoT. For details, see [Target device
considerations](iot-remote-command-execution-start-monitor.md#iot-command-execution-target "iot-remote-command-execution-start-monitor.md#iot-command-execution-target").

**Commands topics**

Before executing a command, devices must subscribe to the commands request topic. When you execute a command, the payload is sent to the device on this topic. After execution, devices publish results and status to the commands response topic. For more information, see [Commands topics](reserved-topics.md#reserved-topics-commands "reserved-topics.md#reserved-topics-commands").

**Command execution**

An execution is an instance of a command running on a target device. When you start an execution, the payload is delivered to the device and a unique execution ID is generated. The device executes the command and reports progress to AWS IoT. Device-side logic determines execution behavior and status reporting to reserved topics.

### Parameter value conditions

When creating commands with payload templates, define value conditions to validate parameter values before execution. Value conditions ensure parameters meet requirements, preventing invalid executions.

**Supported operators by [CommandParameterValue](../apireference/API_CommandParameterValue.md "../apireference/API_CommandParameterValue.md") type**

**Numeric types (INTEGER, LONG, DOUBLE, UNSIGNEDLONG)**

- `EQUALS` - Value must equal the specified number
- `NOT_EQUALS` - Value must not equal the specified number
- `GREATER_THAN` - Value must be greater than the specified number
- `GREATER_THAN_EQUALS` - Value must be greater than or equal to the specified number
- `LESS_THAN` - Value must be less than the specified number
- `LESS_THAN_EQUALS` - Value must be less than or equal to the specified number
- `IN_RANGE` - Value must be within the specified range (inclusive)
- `NOT_IN_RANGE` - Value must be outside the specified range (inclusive)
- `IN_SET` - Value must match one of the specified numbers
- `NOT_IN_SET` - Value must not match any of the specified numbers

**String type (STRING)**

- `EQUALS` - Value must equal the specified string
- `NOT_EQUALS` - Value must not equal the specified string
- `IN_SET` - Value must match one of the specified strings
- `NOT_IN_SET` - Value must not match any of the specified strings

**Boolean type**

- Value conditions are not supported

**Binary type**

- Value conditions are not supported

**Example: Temperature control command**

```
{
  "commandId": "SetTemperature",
  "namespace": "AWS-IoT",
  "payloadTemplate": "{\"temperature\": \"${aws:iot:commandexecution::parameter:temperature}\"}",
  "parameters": [
    {
      "name": "temperature",
      "type": "INTEGER",
      "valueConditions": [
        {
          "comparisonOperator": "IN_RANGE",
          "operand": {
            "numberRange": {
              "min": "60",
              "max": "80"
            }
          }
        }
      ]
    }
  ]
}
```

In this example, the `temperature` parameter must be between 60 and 80 (inclusive). Execution requests with values outside this range fail validation.

###### Note

Value conditions are evaluated at invocation of [StartCommandExecution API](../apireference/API_iot-jobs-data_StartCommandExecution.md "../apireference/API_iot-jobs-data_StartCommandExecution.md"). Failed validations return an error and prevent execution creation.

### Parameter value priority and evaluation

When starting command executions with payload templates, parameter values are resolved using the following priority:

1. **Execution request parameters** - Values provided in the `StartCommandExecution` request take highest priority
2. **Command default values** - If a parameter is not provided in the execution request, the parameter's `defaultValue` is used
3. **No value** - If neither is provided, execution fails as the parameter required to generate the execution request

Value conditions are evaluated on the final parameter value derived above on the priority and before execution creation. If validation fails, the execution request returns an error.

**Example: SetTemperature command with `defaultValue`**

```
{
  "parameters": [
    {
      "name": "temperature",
      "type": "INTEGER",
      "defaultValue": {"I": 72},
      "valueConditions": [
        {
          "comparisonOperator": "IN_RANGE",
          "operand": {"numberRange": {"min": "60", "max": "80"}}
        }
      ]
    }
  ]
}
```

When starting execution:

- If you provide `"temperature": {"I": 75}` in the request, 75 is used
- If you omit the temperature parameter, the default value 72 is used
- Both values are validated against the range condition [60,80]

## Command states

Commands in your AWS account can be in one of three states: _Available_, _Deprecated_, or _Pending deletion_.

**Available**

After successful creation, a command is in the Available state and can be executed on devices.

**Deprecated**

Mark commands for deprecation when no longer needed. Deprecated commands cannot start new executions, but pending executions continue to completion. To enable new executions, restore the command to Available state.

**Pending deletion**

When you mark a command for deletion, it is deleted automatically if deprecated longer than the maximum timeout (default: 12 hours). This action is permanent. If not deprecated or deprecated for less than the timeout, the command enters Pending deletion state and is removed after the timeout expires.

## Command execution status

When you start an execution on a target device, it enters `CREATED` status and can transition to other statuses based on device reports. You can retrieve status information and track executions.

###### Note

You can run multiple commands concurrently on a device. Use concurrency control to limit executions per device and prevent overload. For maximum concurrent executions per device, see [AWS IoT Device Management
commands quotas](../../../general/latest/gr/iot_device_management.md#commands-limits "../../../general/latest/gr/iot_device_management.md#commands-limits").

The following table shows execution statuses and their transitions based on execution progress.

| Command execution status and source | Command execution status | Initiated by device/cloud? | Terminal execution?                                                   | Allowed status transitions |
| ----------------------------------- | ------------------------ | -------------------------- | --------------------------------------------------------------------- | -------------------------- |
| `CREATED`                           | Cloud                    | No                         | • IN_PROGRESS<br>• SUCCEEDED<br>• FAILED<br>• REJECTED<br>• TIMED_OUT |
| `IN_PROGRESS`                       | Device                   | No                         | • IN_PROGRESS<br>• SUCCEEDED<br>• FAILED<br>• REJECTED<br>• TIMED_OUT |
| `TIMED_OUT`                         | Device and cloud         | No                         | • SUCCEEDED<br>• FAILED<br>• REJECTED<br>• TIMED_OUT                  |
| `SUCCEEDED`                         | Device                   | Yes                        | Not applicable                                                        |
| `FAILED`                            | Device                   | Yes                        | Not applicable                                                        |
| `REJECTED`                          | Device                   | Yes                        | Not applicable                                                        |

Devices can publish status and result updates anytime using commands reserved MQTT topics. To provide additional context, devices can use `reasonCode` and `reasonDescription` fields in the `statusReason` object.

The following diagram shows execution status transitions.

![Image showing how a command execution status transitions between various statuses.](images/command-execution-status-transitions.png)

###### Note

When AWS IoT detects no device response within the timeout period, it sets `TIMED_OUT` as a temporary status allowing retries and state changes. If your device explicitly reports `TIMED_OUT`, this becomes a terminal status with no further transitions. For more information, see [Non-terminal command
executions](#iot-command-execution-status-nonterminal "#iot-command-execution-status-nonterminal").

The following sections describe terminal and non-terminal executions and their statuses.

###### Topics

- [Non-terminal command
  executions](#iot-command-execution-status-nonterminal "#iot-command-execution-status-nonterminal")
- [Terminal command
  executions](#iot-command-execution-status-terminal "#iot-command-execution-status-terminal")

### Non-terminal command

executions

An execution is non-terminal if it can accept updates from devices. Non-terminal executions are considered _Active_. The following statuses are non-terminal:

- ###### CREATED

When you start an execution from the AWS IoT console or use the `StartCommandExecution` API, successful requests change the status to `CREATED`. From this status, executions can transition to any other non-terminal or terminal status.

- ###### IN_PROGRESS

After receiving the payload, devices can start executing instructions and performing specified actions. While executing, devices can publish responses to the commands response topic and update status to `IN_PROGRESS`. From `IN_PROGRESS`, executions can transition to any terminal or non-terminal status except `CREATED`.

###### Note

The `UpdateCommandExecution` API can be invoked multiple times with `IN_PROGRESS` status. Specify additional execution details using the `statusReason` object.

- ###### TIMED_OUT

Both cloud and device can trigger this status. Executions in `CREATED` or `IN_PROGRESS` status can change to `TIMED_OUT` for the following reasons:

    + After sending the command, a timer starts. If the device doesn't respond within the specified duration, the cloud changes status to `TIMED_OUT`. In this case, the execution is non-terminal.
    + The device can override status to any terminal status or report a timeout and set status to `TIMED_OUT`. In this case, status remains `TIMED_OUT`, but `StatusReason` object fields change based on device information. The execution becomes terminal.

For more information, see [Time out value and
TIMED_OUT execution status](iot-remote-command-execution-start-monitor.md#iot-command-execution-timeout-status "iot-remote-command-execution-start-monitor.md#iot-command-execution-timeout-status").

### Terminal command

executions

An execution becomes terminal when it no longer accepts updates from devices. The following statuses are terminal. Executions can transition to terminal statuses from any non-terminal status: `CREATED`, `IN_PROGRESS`, or `TIMED_OUT`.

- ###### SUCCEEDED

If the device successfully completes execution, it can publish a response to the commands response topic and update status to `SUCCEEDED`.

- ###### FAILED

When a device fails to complete execution, it can publish a response to the commands response topic and update status to `FAILED`. Use the `reasonCode` and `reasonDescription` fields in the `statusReason` object, or CloudWatch logs, to troubleshoot failures.

- ###### REJECTED

When a device receives an invalid or incompatible request, it can invoke the `UpdateCommandExecution` API with status `REJECTED`. Use the `reasonCode` and `reasonDescription` fields in the `statusReason` object, or CloudWatch logs, to troubleshoot issues.
