

# AWS IoT Commands Troubleshooting
<a name="commands-troubleshooting"></a>

This is the troubleshooting section for AWS IoT Device Management Commands.

## Command execution issues
<a name="commands-execution-troubleshooting"></a>

**Command execution stays in CREATED status**  
When a command execution remains in `CREATED` status and does not proceed to `IN_PROGRESS` or another status, consider the following:  
+ Verify the device is connected to AWS IoT Core and has subscribed to the commands request topic.
+ Check that the device policy allows `iot:Subscribe` and `iot:Receive` on the commands request topic, and `iot:Publish` on the commands response topic.
+ If the device is offline and uses MQTT persistent sessions, the command waits at AWS IoT Core. When the device reconnects before the persistent session timeout and execution timeout, it can process the command. If the execution timeout expires, the execution transitions to `TIMED_OUT`.

**DataConflict error on UpdateCommandExecution**  
A `DataConflict` error occurs when multiple `UpdateCommandExecution` requests are made to the service in parallel or within a short timeframe (for example, `IN_PROGRESS` followed immediately by `SUCCEEDED`).  
To resolve this issue:  
+ Subscribe to the `/accepted` and `/rejected` response topics to confirm each status update was processed before sending the next one.
+ Implement retry logic with exponential backoff when receiving `DataConflict` errors.

**Command executions move to a TIMED\_OUT terminal status unexpectedly**  
When a command execution transitions to `TIMED_OUT` before the device can process it:  
+ Review the timeout value configured for the command execution. The default timeout may be too short for your use case.
+ If the device was offline when the command was sent, verify that the device reconnected and received the execution request before the timeout expired.
+ A cloud-initiated `TIMED_OUT` is non-terminal. The device can still update the execution to a terminal status (`SUCCEEDED`, `FAILED`, `REJECTED`, or `TIMED_OUT`).
A device-initiated `TIMED_OUT` is a terminal status and no further updates can be made to this command execution.

**How do I view errors in CloudWatch logs?**  
Errors from the `UpdateCommandExecution` MQTT request are logged in the `AWSIoTLogsV2` log group in Amazon CloudWatch. To enable logging and view the logs, see [Configure AWS IoT logging](configure-logging.md).

## UpdateCommandExecution error codes
<a name="commands-error-codes"></a>

When the `UpdateCommandExecution` MQTT request fails, the service publishes an error response to the `/rejected` topic. The error response contains an error code and message. The following table lists the error codes that can be returned.


| Error code | Retryable | Description | 
| --- | --- | --- | 
| InvalidStateTransition | No | The requested status transition is not allowed. For example, transitioning from SUCCEEDED to IN\_PROGRESS, updating a device-initiated TIMED\_OUT execution. | 
| TerminalStateReached | No | The command execution has already reached a terminal state and cannot be updated. | 
| ResourceNotFound | No | The specified command execution does not exist. | 
| DataConflict | Yes | The command execution was modified concurrently. This can occur when status updates are sent in rapid succession. Subscribe to the /accepted and /rejected response topics to confirm each status update was processed before sending the next one. For more details, see [DataConflict error on UpdateCommandExecution](#commands-execution-troubleshooting). | 
| InternalError | Yes | An internal server error occurred. Retry the request with exponential backoff. | 

The following is an example of an error response published to the `/rejected` topic:

```
{
    "clientToken": "client-token-1",
    "executionId": "2bd65c51-4cfd-49e4-9310-d5cbfdbc8554",
    "error": "DataConflict",
    "errorMessage": "The command execution was modified concurrently"
}
```