

# Command execution events
<a name="command-events"></a>

AWS IoT publishes event messages to MQTT topics when command executions change status. You can use these events to monitor command execution progress and build applications that respond to status changes.

**Command execution event topics**  
Command execution events are published to the following MQTT topic:

```
$aws/events/commandExecution/{{commandId}}/{{status}}
```

Where:
+ `{{commandId}}` is the identifier of the command.
+ `{{status}}` is the status of the command execution. Valid values are: `CREATED`, `IN_PROGRESS`, `SUCCEEDED`, `FAILED`, `REJECTED`, `TIMED_OUT`.

To receive notifications for all commands and all statuses, subscribe to the following topic using wildcard characters:

```
$aws/events/commandExecution/+/#
```

**Command execution event message**  
When a command execution status changes, AWS IoT publishes an event message to the corresponding MQTT topic. The message contains the following example payload:

```
{
    "executionId": "2bd65c51-4cfd-49e4-9310-d5cbfdbc8554",
    "status": "FAILED",
    "statusReason": {
        "reasonCode": "DEVICE_TOO_BUSY",
        "reasonDescription": ""
    },
    "eventType": "COMMAND_EXECUTION",
    "commandArn": "arn:aws:iot:us-east-1:123456789012:command/0b9d9ddf-e873-43a9-8e2c-9fe004a90086",
    "targetArn": "arn:aws:iot:us-east-1:123456789012:thing/5006c3fc-de96-4def-8427-7eee36c6f2bd",
    "timestamp": 1717708862107
}
```

The payload contains the following attributes:

**executionId**  
A unique identifier for the command execution (string).

**status**  
The status of the command execution. Valid values are: `CREATED`, `IN_PROGRESS`, `SUCCEEDED`, `FAILED`, `REJECTED`, `TIMED_OUT`.

**statusReason**  
An object containing additional information about the status, if available. Contains `reasonCode` and `reasonDescription` fields.

**eventType**  
Set to "COMMAND\_EXECUTION".

**commandArn**  
The Amazon Resource Name (ARN) of the command.

**targetArn**  
The ARN of the target device (thing or client) for the command execution.

**timestamp**  
The UNIX timestamp of when the event occurred.