# Jobs workflow

The following shows the different steps in the jobs workflow from starting a
new job to reporting the completion status of a job execution.

## Start a new job

When a new job is created, AWS IoT Jobs publishes a
message on the `$aws/things/`thing-name`/jobs/notify`
topic for each target device.

The message contains the following information:

```
{
    "timestamp":1476214217017,
    "jobs":{
        "QUEUED":[{
            "jobId":"0001",
            "queuedAt":1476214216981,
            "lastUpdatedAt":1476214216981,
            "versionNumber" : 1
        }]
    }
}
```

The device receives this message on the
`'$aws/things/`thingName`/jobs/notify'`
topic when the job execution is queued.

###### Note

For jobs with the optional `SchedulingConfig`, the job will
maintain an initial status state of `SCHEDULED`. When the job reaches
the selected
`startTime`,
the following will occur:

- The job status state will update to `IN_PROGRESS`.
- The job will begin rollout of the job document to all devices in the
  target group.

## Get job information

To get more information about a job execution, the device calls
the [DescribeJobExecution](jobs-mqtt-api.md#mqtt-describejobexecution "jobs-mqtt-api.md#mqtt-describejobexecution") MQTT API with the
`includeJobDocument` field set to `true`
(the default).

If the request is successful, the AWS IoT Jobs service publishes a
message on the `$aws/things/MyThing/jobs/0023/get/accepted`
topic:

```
{
    "clientToken" : "client-001",
    "timestamp" : 1489097434407,
    "execution" : {
        "approximateSecondsBeforeTimedOut": number,
        "jobId" : "023",
        "status" : "QUEUED",
        "queuedAt" : 1489097374841,
        "lastUpdatedAt" : 1489097374841,
        "versionNumber" : 1,
        "jobDocument" : {
            < contents of job document >
        }
    }
}
```

If the request fails, the AWS IoT Jobs service publishes a
message on the `$aws/things/MyThing/jobs/0023/get/rejected`
topic.

The device now has the job document that it can use to perform the remote
operations for the job. If the job document contains an Amazon S3 presigned URL, the
device can use that URL to download any required files for the job.

## Report job execution status

As the device is executing the job, it can call the [UpdateJobExecution](jobs-mqtt-api.md#mqtt-updatejobexecution "jobs-mqtt-api.md#mqtt-updatejobexecution")
MQTT API to update the status of the job execution.

For example, a device can update the job execution status to
`IN_PROGRESS` by publishing the following message on
the `$aws/things/MyThing/jobs/0023/update` topic:

```
{
    "status":"IN_PROGRESS",
    "statusDetails": {
        "progress":"50%"
    },
    "expectedVersion":"1",
    "clientToken":"client001"
}
```

Jobs respond by publishing a message to the
`$aws/things/MyThing/jobs/0023/update/accepted` or
`$aws/things/MyThing/jobs/0023/update/rejected` topic:

```
{
    "clientToken":"client001",
    "timestamp":1476289222841
}
```

The device can combine the two previous requests by calling [StartNextPendingJobExecution](jobs-mqtt-api.md#mqtt-startnextpendingjobexecution "jobs-mqtt-api.md#mqtt-startnextpendingjobexecution"). That gets
and starts the next pending job execution and allows the device to
update the job execution status. This request also returns the job
document when there is a job execution pending.

If the job contains a [TimeoutConfig](../apireference/API_TimeoutConfig.md "../apireference/API_TimeoutConfig.md"), the in-progress timer starts running.
You can also set a step timer for a job execution by setting a value
for `stepTimeoutInMinutes` when you call [UpdateJobExecution](../apireference/API_iot-jobs-data_UpdateJobExecution.md "../apireference/API_iot-jobs-data_UpdateJobExecution.md"). The step timer applies only to the
job execution that you update. You can set a new value for this
timer each time you update a job execution. You can also create a
step timer when you call [StartNextPendingJobExecution](../apireference/API_iot-jobs-data_StartNextPendingJobExecution.md "../apireference/API_iot-jobs-data_StartNextPendingJobExecution.md"). If the job execution
remains in the `IN_PROGRESS` status for longer than the
step timer interval, it fails and switches to the terminal
`TIMED_OUT` status. The step timer has no effect on
the in-progress timer that you set when you create a job.

The `status` field can be set to
`IN_PROGRESS`, `SUCCEEDED`, or
`FAILED`. You cannot update the status of a job
execution that is already in a terminal state.

## Report execution completed

When the device is finished executing the job, it calls the [UpdateJobExecution](jobs-mqtt-api.md#mqtt-updatejobexecution "jobs-mqtt-api.md#mqtt-updatejobexecution") MQTT API. If the job
was successful, set `status` to `SUCCEEDED`
and, in the message payload, in `statusDetails`, add
other information about the job as name-value pairs. The in-progress
and step timers end when the job execution is complete.

For example:

```
{
    "status":"SUCCEEDED",
    "statusDetails": {
        "progress":"100%"
    },
    "expectedVersion":"2",
    "clientToken":"client-001"
}
```

If the job was not successful, set `status` to
`FAILED` and, in `statusDetails`, add
information about the error that occurred:

```
{
    "status":"FAILED",
    "statusDetails": {
        "errorCode":"101",
        "errorMsg":"Unable to install update"
    },
    "expectedVersion":"2",
    "clientToken":"client-001"
}
```

###### Note

The `statusDetails` attribute can contain any
number of name-value pairs.

When the AWS IoT Jobs service receives this update, it publishes a message
on the `$aws/things/MyThing/jobs/notify` topic to indicate that the job
execution is complete:

```
{
    "timestamp":1476290692776,
    "jobs":{}
}
```

## Additional jobs

If there are other job executions pending for the device, they are
included in the message published to
`$aws/things/MyThing/jobs/notify`.

For example:

```
{
    "timestamp":1476290692776,
    "jobs":{
        "QUEUED":[{
            "jobId":"0002",
            "queuedAt":1476290646230,
            "lastUpdatedAt":1476290646230
        }],
        "IN_PROGRESS":[{
            "jobId":"0003",
            "queuedAt":1476290646230,
            "lastUpdatedAt":1476290646230
        }]
    }
}
```
