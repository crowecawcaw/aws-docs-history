# Jobs device MQTT and HTTPS API operations and

data types

The following commands are available over the MQTT and HTTPS protocols. Use these API
operations on the data plane for devices executing the jobs.

## Jobs device MQTT and HTTPS data

types

The following data types are used to communicate with the AWS IoT Jobs service
over the MQTT and HTTPS protocols.

The `JobExecution` object represents the execution of a job on
a device. The following example shows the syntax:

###### Note

When you use the MQTT and HTTP data plane API operations, the `JobExecution`
data type contains a `JobDocument` field. Your devices can use
this information to retrieve the job document from a job execution.

```
{
    "jobId" : "string",
    "thingName" : "string",
    "jobDocument" : "string",
    "status": "QUEUED|IN_PROGRESS|FAILED|SUCCEEDED|CANCELED|TIMED_OUT|REJECTED|REMOVED",
    "statusDetails": {
        "string": "string"
    },
    "queuedAt" : "timestamp",
    "startedAt" : "timestamp",
    "lastUpdatedAt" : "timestamp",
    "versionNumber" : "number",
    "executionNumber": long
}
```

For more information, see [`JobExecution`](../apireference/API_iot-jobs-data_JobExecution.md "../apireference/API_iot-jobs-data_JobExecution.md") or
[`job-execution`](../../../cli/latest/reference/iot-data/job-execution.md "../../../cli/latest/reference/iot-data/job-execution.md").

The `JobExecutionState` contains information about the state of a job execution.
The following example shows the syntax:

```
{
    "status": "QUEUED|IN_PROGRESS|FAILED|SUCCEEDED|CANCELED|TIMED_OUT|REJECTED|REMOVED",
    "statusDetails": {
        "string": "string"
        ...
    }
    "versionNumber": "number"
}
```

For more information, see [`JobExecutionState`](../apireference/API_iot-jobs-data_JobExecutionState.md "../apireference/API_iot-jobs-data_JobExecutionState.md") or
[`job-execution-state`](../../../cli/latest/reference/iot-data/job-execution-state.md "../../../cli/latest/reference/iot-data/job-execution-state.md").

Contains a subset of information about a job execution. The following
example shows the syntax:

```
{
    "jobId": "string",
    "queuedAt": timestamp,
    "startedAt": timestamp,
    "lastUpdatedAt": timestamp,
    "versionNumber": "number",
    "executionNumber": long
}
```

For more information, see [`JobExecutionSummary`](../apireference/API_iot-jobs-data_JobExecutionSummary.md "../apireference/API_iot-jobs-data_JobExecutionSummary.md") or
[`job-execution-summary`](../../../cli/latest/reference/iot-data/job-execution-summary.md "../../../cli/latest/reference/iot-data/job-execution-summary.md").

###### Learn more about the MQTT and HTTPS API operations in the following

sections:

- [Jobs device MQTT API operations](jobs-mqtt-api.md "jobs-mqtt-api.md")
- [Jobs device HTTP API](jobs-http-device-api.md "jobs-http-device-api.md")
