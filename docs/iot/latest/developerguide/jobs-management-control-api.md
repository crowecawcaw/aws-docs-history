# Jobs management and control API and

data types

###### The following commands are available for Job management and control

in the CLI and over the HTTPS protocol.

- [Job management and control data
  types](#jobs-control-plane-data-types "#jobs-control-plane-data-types")
- [Job management and control API operations](#jobs-http-api "#jobs-http-api")
  To determine the `endpoint-url` parameter for your CLI
  commands, run this command.

```
aws iot describe-endpoint --endpoint-type=iot:Jobs
```

This command returns the following output.

```

{
"endpointAddress": "`account-specific-prefix`.jobs.iot.`aws-region`.amazonaws.com"
}

```

###### Note

The Jobs endpoint doesn't support ALPN `x-amzn-http-ca`.

If you're using dual-stack endpoints (IPv6 and IPv6), use the
`iot:Data-ATS` endpoint. The `iot:Jobs` endpoint supports
only IPv4.

## Job management and control data

types

The following data types are used by management and control applications to
communicate with AWS IoT Jobs.

The `Job` object contains details about a job. The following
example shows the syntax:

```
{
    "jobArn": "string",
    "jobId": "string",
    "status": "IN_PROGRESS|CANCELED|SUCCEEDED",
    "forceCanceled": boolean,
    "targetSelection": "CONTINUOUS|SNAPSHOT",
    "comment": "string",
    "targets": ["string"],
    "description": "string",
    "createdAt": timestamp,
    "lastUpdatedAt": timestamp,
    "completedAt": timestamp,
    "jobProcessDetails": {
        "processingTargets": ["string"],
        "numberOfCanceledThings": long,
        "numberOfSucceededThings": long,
        "numberOfFailedThings": long,
        "numberOfRejectedThings": long,
        "numberOfQueuedThings": long,
        "numberOfInProgressThings": long,
        "numberOfRemovedThings": long,
        "numberOfTimedOutThings": long
    },
    "presignedUrlConfig": {
        "expiresInSec": number,
        "roleArn": "string"
    },
    "jobExecutionsRolloutConfig": {
        "exponentialRate": {
           "baseRatePerMinute": integer,
           "incrementFactor": integer,
           "rateIncreaseCriteria": {
              "numberOfNotifiedThings": integer, // Set one or the other
              "numberOfSucceededThings": integer // of these two values.
           },
           "maximumPerMinute": integer
      }
    },
    "abortConfig": {
       "criteriaList": [
          {
             "action": "string",
             "failureType": "string",
             "minNumberOfExecutedThings": integer,
             "thresholdPercentage": integer
          }
       ]
    },
    "SchedulingConfig": {
      "startTime": string
      "endTime": string
      "timeZone": string


      "endTimeBehavior": string

   },
    "timeoutConfig": {
        "inProgressTimeoutInMinutes": long
    }
}
```

For more information, see [`Job`](../apireference/API_Job.md "../apireference/API_Job.md") or [`job`](../../../cli/latest/reference/iot/job.md "../../../cli/latest/reference/iot/job.md").

The `JobSummary` object contains a job summary. The following
example shows the syntax:

```
{
    "jobArn": "string",
    "jobId": "string",
    "status": "IN_PROGRESS|CANCELED|SUCCEEDED|SCHEDULED",
    "targetSelection": "CONTINUOUS|SNAPSHOT",
    "thingGroupId": "string",
    "createdAt": timestamp,
    "lastUpdatedAt": timestamp,
    "completedAt": timestamp
}
```

For more information, see [`JobSummary`](../apireference/API_JobSummary.md "../apireference/API_JobSummary.md") or [`job-summary`](../../../cli/latest/reference/iot/job-summary.md "../../../cli/latest/reference/iot/job-summary.md").

The `JobExecution` object represents the execution of a job on
a device. The following example shows the syntax:

###### Note

When you use the control plane API operations, the `JobExecution`
data type doesn't contain a `JobDocument` field. To obtain this
information, you can use the [`GetJobDocument`](../apireference/API_GetJobDocument.md "../apireference/API_GetJobDocument.md") API operation or the [`get-job-document`](../../../cli/latest/reference/get-job-document.md "../../../cli/latest/reference/get-job-document.md") CLI command.

```
{
    "approximateSecondsBeforeTimedOut": 50,
    "executionNumber": 1234567890,
    "forceCanceled": true|false,
    "jobId": "string",
    "lastUpdatedAt": timestamp,
    "queuedAt": timestamp,
    "startedAt": timestamp,
    "status": "QUEUED|IN_PROGRESS|FAILED|SUCCEEDED|CANCELED|TIMED_OUT|REJECTED|REMOVED",
    "forceCanceled": boolean,
    "statusDetails": {
        "detailsMap": {
            "string": "string" ...
        },
        "status": "string"
    },
    "thingArn": "string",
    "versionNumber": 123
}
```

For more information, see [`JobExecution`](../apireference/API_JobExecution.md "../apireference/API_JobExecution.md") or [`job-execution`](../../../cli/latest/reference/iot/job-execution.md "../../../cli/latest/reference/iot/job-execution.md").

The `JobExecutionSummary` object contains job execution summary
information. The following example shows the syntax:

```
{
    "executionNumber": 1234567890,
    "queuedAt": timestamp,
    "lastUpdatedAt": timestamp,
    "startedAt": timestamp,
    "status": "QUEUED|IN_PROGRESS|FAILED|SUCCEEDED|CANCELED|TIMED_OUT|REJECTED|REMOVED"
}
```

For more information, see [`JobExecutionSummary`](../apireference/API_JobExecutionSummary.md "../apireference/API_JobExecutionSummary.md") or [`job-execution-summary`](../../../cli/latest/reference/iot/job-execution-summary.md "../../../cli/latest/reference/iot/job-execution-summary.md").

The `JobExecutionSummaryForJob` object contains a summary of
information about job executions for a specific job. The following example
shows the syntax:

```
{
    "executionSummaries": [
        {
            "thingArn": "arn:aws:iot:us-west-2:123456789012:thing/MyThing",
            "jobExecutionSummary": {
                "status": "IN_PROGRESS",
                "lastUpdatedAt": 1549395301.389,
                "queuedAt": 1541526002.609,
                "executionNumber": 1
            }
        },
        ...
    ]
}

```

For more information, see [`JobExecutionSummaryForJob`](../apireference/API_JobExecutionSummaryForJob.md "../apireference/API_JobExecutionSummaryForJob.md") or [`job-execution-summary-for-job`](../../../cli/latest/reference/iot/job-execution-summary-for-job.md "../../../cli/latest/reference/iot/job-execution-summary-for-job.md").

The `JobExecutionSummaryForThing` object contains a summary of
information about a job execution on a specific thing. FThe following
example shows the syntax:

```
{
    "executionSummaries": [
        {
            "jobExecutionSummary": {
                "status": "IN_PROGRESS",
                "lastUpdatedAt": 1549395301.389,
                "queuedAt": 1541526002.609,
                "executionNumber": 1
            },
            "jobId": "MyThingJob"
        },
        ...
    ]
}
```

For more information, see [`JobExecutionSummaryForThing`](../apireference/API_JobExecutionSummaryForThing.md "../apireference/API_JobExecutionSummaryForThing.md") or [`job-execution-summary-for-thing`](../../../cli/latest/reference/iot/job-execution-summary-for-thing.md "../../../cli/latest/reference/iot/job-execution-summary-for-thing.md").

## Job management and control API operations

Use the following API operations or CLI commands:

Associates a group with a continuous job. The following criteria
must be met:

- The job must have been created with the `targetSelection`
  field set to `CONTINUOUS`.
- The job status must currently be `IN_PROGRESS`.
- The total number of targets associated with a job must
  not exceed 100.

HTTPS request

```
POST /jobs/`jobId`/targets

{
"targets": [ "string" ],
"comment": "string"
}
```

For more information, see [`AssociateTargetsWithJob`](../apireference/API_AssociateTargetsWithJob.md "../apireference/API_AssociateTargetsWithJob.md").

CLI syntax

```
aws iot  associate-targets-with-job \
--targets <value> \
--job-id <value> \
[--comment <value>]  \
[--cli-input-json <value>] \
[--generate-cli-skeleton]
```

`cli-input-json` format:

```
{
"targets": [
"string"
],
"jobId": "string",
"comment": "string"
}
```

For more information, see [`associate-targets-with-job`](../../../cli/latest/reference/iot/associate-targets-with-job.md "../../../cli/latest/reference/iot/associate-targets-with-job.md").

Cancels a job.

HTTPS request

```
PUT /jobs/`jobId`/cancel

{
"force": boolean,
"comment": "string",
"reasonCode": "string"
}
```

For more information, see [`CancelJob`](../apireference/API_CancelJob.md "../apireference/API_CancelJob.md").

CLI syntax

```
aws iot cancel-job \
    --job-id <value> \
    [--force <value>]  \
    [--comment <value>]  \
    [--reasonCode <value>]  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

`cli-input-json` format:

```
{
    "jobId": "string",
    "force": boolean,
    "comment": "string"
}
```

For more information, see [`cancel-job`](../../../cli/latest/reference/iot/cancel-job.md "../../../cli/latest/reference/iot/cancel-job.md").

Cancels a job execution on a device.

HTTPS request

```
PUT /things/`thingName`/jobs/`jobId`/cancel

{
"force": boolean,
"expectedVersion": "string",
"statusDetails": {
    "string": "string"
    ...
}
}
```

For more information, see [`CancelJobExecution`](../apireference/API_CancelJobExecution.md "../apireference/API_CancelJobExecution.md").

CLI syntax

```
aws iot cancel-job-execution \
--job-id <value> \
--thing-name <value> \
[--force | --no-force] \
[--expected-version <value>] \
[--status-details <value>]  \
[--cli-input-json <value>] \
[--generate-cli-skeleton]
```

`cli-input-json` format:

```
{
"jobId": "string",
"thingName": "string",
"force": boolean,
"expectedVersion": long,
"statusDetails": {
"string": "string"
}
}
```

For more information, see [`cancel-job-execution`](../../../cli/latest/reference/iot/cancel-job-execution.md "../../../cli/latest/reference/iot/cancel-job-execution.md").

Creates a job. You can provide the job document as a link to a file in an
Amazon S3 bucket (`documentSource` parameter), or in the body of the
request (`document` parameter).

A job can be made _continuous_ by setting the optional
`targetSelection` parameter to `CONTINUOUS` (the
default is `SNAPSHOT`). A continuous job can be used to onboard
or upgrade devices as they are added to a group because it continues to run
and is launched on newly added things. This can occur even after the things
in the group at the time the job was created have completed the job.

A job can have an optional [TimeoutConfig](../apireference/API_TimeoutConfig.md "../apireference/API_TimeoutConfig.md"), which sets the value of the
in-progress timer. The in-progress timer can't be updated and
applies to all executions of the job.

The following validations are performed on arguments to the
`CreateJob` API:

- The `targets` argument must be a list of
  valid thing or thing group ARNs. All things and thing
  groups must be in your AWS account.
- The `documentSource` argument must be a valid Amazon S3 URL to
  a job document. Amazon S3 URLs are in the form:
  `https://s3.amazonaws.com/`bucketName`/`objectName``.
- The document stored in the URL specified by the
  `documentSource` argument must be a UTF-8
  encoded JSON document.
- The size of a job document is limited to 32 KB due to the limit on
  the size of an MQTT message (128 KB) and encryption.
- The `jobId` must be unique in your AWS account.

HTTPS request

```
PUT /jobs/`jobId`

{
"targets": [ "string" ],
"document": "string",
"documentSource": "string",
"description": "string",
"jobTemplateArn": "string",
"presignedUrlConfigData": {
    "roleArn": "string",
    "expiresInSec": "integer"
},
"targetSelection": "CONTINUOUS|SNAPSHOT",
"jobExecutionsRolloutConfig": {
    "exponentialRate": {
       "baseRatePerMinute": integer,
       "incrementFactor": integer,
       "rateIncreaseCriteria": {
          "numberOfNotifiedThings": integer, // Set one or the other
          "numberOfSucceededThings": integer // of these two values.
       },
       "maximumPerMinute": integer
  }
},
"abortConfig": {
   "criteriaList": [
      {
         "action": "string",
         "failureType": "string",
         "minNumberOfExecutedThings": integer,
         "thresholdPercentage": integer
      }
   ]
},
"SchedulingConfig": {
    "startTime": string
    "endTime": string
    "timeZone": string


    "endTimeBehavior": string

   }
"timeoutConfig": {
  "inProgressTimeoutInMinutes": long
}
}

```

For more information, see [`CreateJob`](../apireference/API_CreateJob.md "../apireference/API_CreateJob.md").

CLI syntax

```
aws iot create-job \
    --job-id <value> \
    --targets <value> \
    [--document-source <value>] \
    [--document <value>] \
    [--description <value>] \
    [--job-template-arn <value>] \
    [--presigned-url-config <value>] \
    [--target-selection <value>] \
    [--job-executions-rollout-config <value>] \
    [--abort-config <value>] \
    [--timeout-config <value>] \
    [--document-parameters <value>]  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

`cli-input-json` format:

```
{
    "jobId": "string",
    "targets": [ "string" ],
    "documentSource": "string",
    "document": "string",
    "description": "string",
    "jobTemplateArn": "string",
    "presignedUrlConfig": {
        "roleArn": "string",
        "expiresInSec": long
     },
    "targetSelection": "string",
    "jobExecutionsRolloutConfig": {
          "exponentialRate": {
              "baseRatePerMinute": integer,
              "incrementFactor": integer,
              "rateIncreaseCriteria": {
                 "numberOfNotifiedThings": integer, // Set one or the other
                 "numberOfSucceededThings": integer // of these two values.
              },
      "maximumPerMinute": integer
      }
    },
    "abortConfig": {
    "criteriaList": [
        {
           "action": "string",
           "failureType": "string",
           "minNumberOfExecutedThings": integer,
           "thresholdPercentage": integer
         }
      ]
    },
    "timeoutConfig": {
          "inProgressTimeoutInMinutes": long
    },
    "documentParameters": {
    "string": "string"
    }
}
```

For more information, see [`create-job`](../../../cli/latest/reference/iot/create-job.md "../../../cli/latest/reference/iot/create-job.md").

Deletes a job and its related job executions.

Deleting a job can take time, depending on the number of job
executions created for the job and various other factors. While
the job is being deleted, the status of the job is shown as
"DELETION_IN_PROGRESS". Attempting to delete or cancel a job
whose status is already "DELETION_IN_PROGRESS" results in an
error.

HTTPS request

```
DELETE /jobs/`jobId`?force=`force`
```

For more information, see [`DeleteJob`](../apireference/API_DeleteJob.md "../apireference/API_DeleteJob.md").

CLI syntax

```
aws iot  delete-job \
--job-id <value> \
[--force | --no-force]  \
[--cli-input-json <value>] \
[--generate-cli-skeleton]
```

`cli-input-json` format:

```
{
"jobId": "string",
"force": boolean
}
```

For more information, see [`delete-job`](../../../cli/latest/reference/iot/delete-job.md "../../../cli/latest/reference/iot/delete-job.md").

Deletes a job execution.

HTTPS request

```
DELETE /things/`thingName`/jobs/`jobId`/executionNumber/`executionNumber`?force=`force`
```

For more information, see [`DeleteJobExecution`](../apireference/API_DeleteJobExecution.md "../apireference/API_DeleteJobExecution.md").

CLI syntax

```
aws iot  delete-job-execution \
--job-id <value> \
--thing-name <value> \
--execution-number <value> \
[--force | --no-force]  \
[--cli-input-json <value>] \
[--generate-cli-skeleton]
```

`cli-input-json` format:

```
{
"jobId": "string",
"thingName": "string",
"executionNumber": long,
"force": boolean
}
```

For more information, see [`delete-job-execution`](../../../cli/latest/reference/iot/delete-job-execution.md "../../../cli/latest/reference/iot/delete-job-execution.md").

Gets the details of the job execution.

HTTPS request

```
GET /jobs/`jobId`
```

For more information, see [`DescribeJob`](../apireference/API_DescribeJob.md "../apireference/API_DescribeJob.md").

CLI syntax

```
aws iot describe-job \
--job-id <value>  \
[--cli-input-json <value>] \
[--generate-cli-skeleton]
```

`cli-input-json` format:

```
{
"jobId": "string"
}
```

For more information, see [`describe-job`](../../../cli/latest/reference/iot/describe-job.md "../../../cli/latest/reference/iot/describe-job.md").

Gets details of a job execution. The job's execution status
must be `SUCCEEDED` or `FAILED`.

HTTPS request

```
GET /things/`thingName`/jobs/`jobId`?executionNumber=`executionNumber`
```

For more information, see [`DescribeJobExecution`](../apireference/API_DescribeJobExecution.md "../apireference/API_DescribeJobExecution.md").

CLI syntax

```
aws iot  describe-job-execution \
--job-id <value> \
--thing-name <value> \
[--execution-number <value>]  \
[--cli-input-json <value>] \
[--generate-cli-skeleton]
```

`cli-input-json` format:

```
{
"jobId": "string",
"thingName": "string",
"executionNumber": long
}
```

For more information, see [`describe-job-execution`](../../../cli/latest/reference/iot/describe-job-execution.md "../../../cli/latest/reference/iot/describe-job-execution.md").

Gets the job document for a job.

###### Note

Placeholder URLs are not replaced with presigned Amazon S3 URLs
in the document returned. Presigned URLs are generated only
when the AWS IoT Jobs service receives a request over
MQTT.

HTTPS request

```
GET /jobs/`jobId`/job-document
```

For more information, see [`GetJobDocument`](../apireference/API_GetJobDocument.md "../apireference/API_GetJobDocument.md").

CLI syntax

```
aws iot get-job-document \
--job-id <value>  \
[--cli-input-json <value>] \
[--generate-cli-skeleton]
```

`cli-input-json` format:

```
{
"jobId": "string"
}
```

For more information, see [`get-job-document`](../../../cli/latest/reference/iot/get-job-document.md "../../../cli/latest/reference/iot/get-job-document.md").

Gets a list of job executions for a job.

HTTPS request

```
GET /jobs/`jobId`/things?status=`status`&maxResults=`maxResults`&nextToken=`nextToken`
```

For more information, see [`ListJobExecutionsForJob`](../apireference/API_ListJobExecutionsForJob.md "../apireference/API_ListJobExecutionsForJob.md").

CLI syntax

```
aws iot  list-job-executions-for-job \
--job-id <value> \
[--status <value>] \
[--max-results <value>] \
[--next-token <value>]  \
[--cli-input-json <value>] \
[--generate-cli-skeleton]
```

`cli-input-json` format:

```
{
"jobId": "string",
"status": "string",
"maxResults": "integer",
"nextToken": "string"
}
```

For more information, see [`list-job-executions-for-job`](../../../cli/latest/reference/iot/list-job-executions-for-job.md "../../../cli/latest/reference/iot/list-job-executions-for-job.md").

Gets a list of job executions for a thing.

HTTPS request

```
GET /things/`thingName`/jobs?status=`status`&maxResults=`maxResults`&nextToken=`nextToken`
```

For more information, see [`ListJobExecutionsForThing`](../apireference/API_ListJobExecutionsForThing.md "../apireference/API_ListJobExecutionsForThing.md").

CLI syntax

```
aws iot list-job-executions-for-thing \
--thing-name <value> \
[--status <value>] \
[--max-results <value>] \
[--next-token <value>]  \
[--cli-input-json <value>] \
[--generate-cli-skeleton]
```

`cli-input-json` format:

```
{
"thingName": "string",
"status": "string",
"maxResults": "integer",
"nextToken": "string"
}
```

For more information, see [`list-job-executions-for-thing`](../../../cli/latest/reference/iot/list-job-executions-for-thing.md "../../../cli/latest/reference/iot/list-job-executions-for-thing.md").

Gets a list of jobs in your AWS account.

HTTPS request

```
GET /jobs?status=`status`&targetSelection=`targetSelection`&thingGroupName=`thingGroupName`&thingGroupId=`thingGroupId`&maxResults=`maxResults`&nextToken=`nextToken`
```

For more information, see [`ListJobs`](../apireference/API_ListJobs.md "../apireference/API_ListJobs.md").

CLI syntax

```
aws iot list-jobs \
[--status <value>] \
[--target-selection <value>] \
[--max-results <value>] \
[--next-token <value>] \
[--thing-group-name <value>] \
[--thing-group-id <value>]  \
[--cli-input-json <value>] \
[--generate-cli-skeleton]
```

`cli-input-json` format:

```
{
"status": "string",
"targetSelection": "string",
"maxResults": "integer",
"nextToken": "string",
"thingGroupName": "string",
"thingGroupId": "string"
}
```

For more information, see [`list-jobs`](../../../cli/latest/reference/iot/list-jobs.md "../../../cli/latest/reference/iot/list-jobs.md").

Updates supported fields of the specified job. Updated values for
`timeoutConfig` take effect for only newly in-progress
launches. Currently, in-progress launches continue to launch with the
previous timeout configuration.

HTTPS request

```
PATCH /jobs/`jobId`
{
"description": "string",
"presignedUrlConfig": {
  "expiresInSec": number,
  "roleArn": "string"
},
"jobExecutionsRolloutConfig": {
  "exponentialRate": {
     "baseRatePerMinute": number,
     "incrementFactor": number,
     "rateIncreaseCriteria": {
        "numberOfNotifiedThings": number,
        "numberOfSucceededThings": number
     },
  "maximumPerMinute": number
  },
"abortConfig": {
  "criteriaList": [
     {
        "action": "string",
        "failureType": "string",
        "minNumberOfExecutedThings": number,
        "thresholdPercentage": number
     }
  ]
},
"timeoutConfig": {
  "inProgressTimeoutInMinutes": number
}
}

```

For more information, see [`UpdateJob`](../apireference/API_UpdateJob.md "../apireference/API_UpdateJob.md").

CLI syntax

```
aws iot  update-job \
--job-id <value> \
[--description <value>] \
[--presigned-url-config <value>] \
[--job-executions-rollout-config <value>] \
[--abort-config <value>] \
[--timeout-config <value>] \
[--cli-input-json <value>] \
[--generate-cli-skeleton]
```

`cli-input-json` format:

```
{
"description": "string",
"presignedUrlConfig": {
  "expiresInSec": number,
  "roleArn": "string"
},
"jobExecutionsRolloutConfig": {
  "exponentialRate": {
     "baseRatePerMinute": number,
     "incrementFactor": number,
     "rateIncreaseCriteria": {
        "numberOfNotifiedThings": number,
        "numberOfSucceededThings": number
     }
  },
  "maximumPerMinute": number
},
"abortConfig": {
  "criteriaList": [
     {
        "action": "string",
        "failureType": "string",
        "minNumberOfExecutedThings": number,
        "thresholdPercentage": number
     }
  ]
},
"timeoutConfig": {
  "inProgressTimeoutInMinutes": number
}
}
```

For more information, see [`update-job`](../../../cli/latest/reference/iot/update-job.md "../../../cli/latest/reference/iot/update-job.md").
