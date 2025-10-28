AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Data structures for AWS Blu Age user

You can learn about various data structures for AWS Blu Age engine in the following section.

###### Topics

- [Job execution details message structure](#job-execution-details "#job-execution-details")
- [Transaction launch outcome structure](#transaction-outcome "#transaction-outcome")
- [Transaction launch record outcome structure](#transaction-record-outcome "#transaction-record-outcome")
- [Possible status of a job on a queue](#jobs-status "#jobs-status")
- [Submit job and schedule job input](#submit-job "#submit-job")
- [List of scheduled jobs response](#list-scheduled-jobs "#list-scheduled-jobs")
- [List of repeating jobs response](#list-on-hold-jobs "#list-on-hold-jobs")

## Job execution details message structure

Each job execution details will have the following fields:

scriptId

the identifier of the called script.

caller

I.P. address of the caller.

identifier

unique job execution identifier.

startTime

date and time at which the job execution started.

endTime

date and time at which the job execution ended.

status

a status for the job execution. One possible value amongst:

- `DONE`: job execution ended normally.
- `TRIGGERED`: job execution triggered but not launched yet.
- `RUNNING`: job execution is running.
- `KILLED`: job execution has been killed.
- `FAILED`: job execution has failed.

executionResult

a message to sum up the outcome of the job execution.
This message can either be a simple message if the job execution is not finished yet or a JSON structure with the following fields:

- exitCode: numeric exit code; negative values indicate failure situations.
- program: latest program launched by the job.
- status: one possible value amongst:
  - `Error`: when exitCode = -1; this corresponds to an (technical) error occurring during job execution.
  - `Failed`: when exitcode = -2; This corresponds to a failure occurring during a service program execution (like an ABEND situation).
  - `Succeeded`: when exitCode >= 0;

- stepName: name of the latest step executed in the job.

executionMode

either SYNCHRONOUS or ASYNCHRONOUS, depending on the way the job has been launched.

Sample output:

```
{
    "scriptId": "INTCALC",
    "caller": "127.0.0.1",
    "identifier": "97d410be-efa7-4bd3-b7b9-d080e5769771",
    "startTime": "06-09-2023 11:42:41",
    "endTime": "06-09-2023 11:42:42",
    "status": "DONE",
    "executionResult": "{ \"exitCode\": -1, \"stepName\": \"STEP15\", \"program\": \"CBACT04C\", \"status\": \"Error\" }",
    "executionMode": "ASYNCHRONOUS"
  }
```

## Transaction launch outcome structure

The structure might contain the following fields:

outCome

a string representing the transaction execution outcome. Possible values are:

- `Success`: transaction execution went to the end properly.
- `Failure`: transaction execution failed to end properly, some problem(s) were encountered.

commarea

a string representing the COMMAREA final value, as a byte64 encoded byte array. Might be an empty string.

containerRecord

(Optional) a string representing the CONTAINER's record content as a byte64 encoded byte
array.

serverDescription

May contain information about the server which served the request (for debugging purpose). Might be an empty string.

abendCode

(Optional) if the program referenced by the launched transaction abended, the abend code
value will be returned as as string in this field.

Sample responses:

Success

```
{
    "outCome": "Success",
    "commarea": "",
    "serverDescription": ""
  }
```

Failure

```
{
    "outCome": "Failure",
    "commarea": "",
    "serverDescription": "",
    "abendCode": "AEIA"
  }
```

## Transaction launch record outcome structure

The structure might contain the following fields:

recordContent

a string representing the COMMAREA's record content as a byte64 encoded byte array.

containerRecord

a string representing the CONTAINER's record content as a byte64 encoded byte array.

serverDescription

May contain information about the server which served the request (for debugging purpose). Might be an empty string.

Sample responses:

Success

```
{
    "recordContent": "",
    "serverDescription": ""
}
```

## Possible status of a job on a queue

On a queue, jobs can have the following status:

ACTIVE

The job is currently being run on the queue.

EXECUTION_WAIT

The job is waiting for a thread to be available.

SCHEDULED

Jobs is scheduled for execution at a specific date and time.

HOLD

Job is waiting to be released before being run.

COMPLETED

Job has been executed successfully.

FAILED

Job execution has failed.

UNKNOWN

Status is unknown.

## Submit job and schedule job input

The submit job and schedule job input is the JSON serialization of a `com.netfective.bluage.gapwalk.rt.jobqueue.SubmitJobMessage` object.
The sample input below exhibits all the fields for such a bean.

Sample input for submit job:

```
{
    "messageQueueName":null,
    "scheduleDate":null,
    "scheduleTime":null,
    "programName":"PTA0044",
    "programParams":
     {"wmind":"B"},
    "localDataAreaValue":"",
    "userName":"USER1",
    "jobName":"PTA0044",
    "jobNumber":9,
    "jobPriority":5,
    "executionDate":"20181231",
    "jobQueue":"queue1",
    "jobOnHold":false
}
```

Sample input for schedule job:

```
{
     "scheduleCron": "*/2 * * * * ?",
     "programName":"LOGPGM",
     "programParams": {
         "cl_sbmjob_param_json": "[\"./output/schedule-job-log.txt\", \"Every 2 seconds!\"]"
     },
     "localDataAreaValue":"",
     "userName":"PVO",
     "jobName":"LOGGERJOB",
     "jobPriority":5,
     "jobQueue":"queue1",
     "scheduleMisfirePolicy": 4,
     "startTime": "2003/05/04 07:00:00.000 GMT-06:00",
     "endTime": "2003/05/04 07:00:07.000 GMT-06:00"
 }
```

jobNumber

if the job number is 0, the job number will be automatically generated using the next number in the job number sequence.
That value should be set to 0 (except for testing purpose).

jobPriority

Default job priority in AS400 is 5. Valid range is 0-9, 0 being the highest priority.

jobOnHold

If a job is submitted on hold, it won’t be executed right away but only when somebody “releases” it.
A job can be released using the REST API (/release or /release-all).

scheduleDate and scheduleTime

If these values are not null, the job will be executed at the specified date and time.

Date

Can be provided with format MMddyy or ddMMyyyy (size of the input will determine what format is used)

Time

Can be provided with format HHmm or HHmmss (size of the input will determine what format is used)

programParams

Will be passed to the program as a map.

scheduleMisfirePolicy

Defines the strategy used when a trigger is misfired. The following are the possible values:

1. Release the first misfire and discard the other misfires.
2. Submit a job on hold for the first misfire and discard the other misfires.
3. Discard the misfire.
4. Release all misfires. The job queue will run all jobs.

## List of scheduled jobs response

This is the structure of the list-jobs job queue endpoint.
The submit job message that was used to submit that job is part of the response.
This can be used for tracking or testing / resubmitting purpose.
When a job is completed, the start date and end date will also be populated.

```
[
  {
    "jobName": "PTA0044",
    "userName": "USER1",
    "jobNumber": 9,
    "jobPriority": 5,
    "status": "HOLD",
    "jobDelay": 0,
    "startDate": null,
    "endDate": null,
    "jobQueue": "queue1",
    "message": {
      "messageQueueName": null,
      "scheduleDate": null,
      "scheduleTime": null,
      "programName": "PTA0044",
      "programParams": {"wmind": "B"},
      "localDataAreaValue": "",
      "userName": "USER1",
      "jobName": "PTA0044",
      "jobNumber": 9,
      "jobPriority": 5,
      "executionDate": "20181231",
      "jobQueue": "queue1",
      "jobOnHold": true,
      "scheduleCron": null,
      "save": false,
      "scheduleMisfirePolicy": 4,
      "omitdates": null
    },
    "executionId": 1,
    "jobScheduledId": 0,
    "jobScheduledAt": null
  },
  {
    "jobName": "PTA0044",
    "userName": "USER1",
    "jobNumber": 9,
    "jobPriority": 5,
    "status": "COMPLETED",
    "jobDelay": 0,
    "startDate": "2022-10-13T22:48:34.025+00:00",
    "endDate": "2022-10-13T22:52:54.475+00:00",
    "jobQueue": "queue1",
    "message": {
      "messageQueueName": null,
      "scheduleDate": null,
      "scheduleTime": null,
      "programName": "PTA0044",
      "programParams": {"wmind": "B"},
      "localDataAreaValue": "",
      "userName": "USER1",
      "jobName": "PTA0044",
      "jobNumber": 9,
      "jobPriority": 5,
      "executionDate": "20181231",
      "jobQueue": "queue1",
      "jobOnHold": true,
      "scheduleCron": "*/20 * * * * ?",
      "save": false,
      "scheduleMisfirePolicy": 4,
      "omitdates": null
    },
    "executionId": 2,
    "jobScheduledId": 0,
    "jobScheduledAt": null
  }
]
```

## List of repeating jobs response

This is the structure of the /schedule/list job queue endpoint.

```
[
  {
    "id": 1,
    "status": "ACTIVE",
    "jobNumber": 1,
    "userName": "PVO",
    "msg": {
      "messageQueueName": null,
      "scheduleDate": null,
      "scheduleTime": null,
      "startTime": "2024/03/07 21:12:00.000 UTC",
      "endTime": "2024/03/07 21:13:59.000 UTC",
      "programName": "LOGPGM",
      "programParams": {"cl_sbmjob_param_json": "[\"./output/schedule-job-log.txt\", \"Every 20 seconds!\"]"},
      "localDataAreaValue": "",
      "userName": "PVO",
      "jobName": "LOGGERJOB",
      "jobNumber": 1,
      "jobScheduleId": 1,
      "jobPriority": 5,
      "executionDate": null,
      "jobQueue": "queue1",
      "jobOnHold": false,
      "scheduleCron": "*/20 * * * * ?",
      "save": false,
      "scheduleMisfirePolicy": 4,
      "omitdates": null
    },
    "lastUpdatedAt": "2024-03-07T21:11:13.282+00:00",
    "lastUpdatedBy": ""
  }
]
```
