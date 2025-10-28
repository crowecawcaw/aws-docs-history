# Understanding log events for sensitive data

discovery jobs

To help you monitor your sensitive data discovery jobs, Amazon Macie automatically
publishes logging data for jobs to Amazon CloudWatch Logs. The data in these logs provides a record
of changes to a job's progress or status. For example, you can use the data to determine
the exact date and time when a job started to run or finished running. The data also
provides details about certain types of errors that can occur while a job runs. This
data can help you identify, investigate, and address errors that prevent Macie from
analyzing the data that you want.

When you start running jobs, Macie automatically creates and configures the
appropriate resources in CloudWatch Logs to log events for all of your jobs. Macie then publishes
event data to those resources automatically when your jobs run. For more information,
see [How logging works
for jobs](discovery-jobs-monitor-cw-logs-configure.md "discovery-jobs-monitor-cw-logs-configure.md").

By using CloudWatch Logs, you can then query and analyze log data for your jobs. For example,
you can search and filter aggregate data to identify specific types of events that
occurred for all of your jobs during a specific time range. Or you can perform a
targeted review of all the events that occurred for a particular job. CloudWatch Logs also
provides options for monitoring log data, defining metric filters, and creating custom
alarms. For example, you can configure CloudWatch Logs to notify you if a certain type of event
occurs when your jobs run. For more information, see the [Amazon CloudWatch Logs User
Guide](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md").

###### Topics

- [Log event schema
  for jobs](discovery-jobs-monitor-cw-logs-ref.md#discovery-jobs-monitor-cw-logs-schema "discovery-jobs-monitor-cw-logs-ref.md#discovery-jobs-monitor-cw-logs-schema")
- [Types of
  log events for jobs](discovery-jobs-monitor-cw-logs-ref.md#discovery-jobs-monitor-cw-logs-event-index "discovery-jobs-monitor-cw-logs-ref.md#discovery-jobs-monitor-cw-logs-event-index")
  - [Job status events](discovery-jobs-monitor-cw-logs-ref.md#discovery-jobs-monitor-cw-logs-event-index-status "discovery-jobs-monitor-cw-logs-ref.md#discovery-jobs-monitor-cw-logs-event-index-status")
  - [Account-level error events](discovery-jobs-monitor-cw-logs-ref.md#discovery-jobs-monitor-cw-logs-event-index-account-errors "discovery-jobs-monitor-cw-logs-ref.md#discovery-jobs-monitor-cw-logs-event-index-account-errors")
  - [Bucket-level error events](discovery-jobs-monitor-cw-logs-ref.md#discovery-jobs-monitor-cw-logs-event-index-bucket-errors "discovery-jobs-monitor-cw-logs-ref.md#discovery-jobs-monitor-cw-logs-event-index-bucket-errors")

## Log event schema for

sensitive data discovery jobs

Each log event for a sensitive data discovery job is a JSON object that contains a
standard set of fields and conforms to the Amazon CloudWatch Logs event schema. Some types of
events have additional fields that provide information that's particularly useful
for that type of event. For example, events for account-level errors include the
account ID for the affected AWS account. Events for bucket-level errors include
the name of the affected Amazon Simple Storage Service (Amazon S3) bucket.

The following example shows the log event schema for sensitive data discovery
jobs. In this example, the event reports that Amazon Macie wasn't able to analyze any
objects in an S3 bucket because Amazon S3 denied access to the bucket.

```
{
    "adminAccountId": "123456789012",
    "jobId": "85a55dc0fa6ed0be5939d0408example",
    "eventType": "BUCKET_ACCESS_DENIED",
    "occurredAt": "2024-04-14T17:11:30.574809Z",
    "description": "Macie doesn’t have permission to access the affected S3 bucket.",
    "jobName": "My_Macie_Job",
    "operation": "ListObjectsV2",
    "runDate": "2024-04-14T17:08:30.345809Z",
    "affectedAccount": "111122223333",
    "affectedResource": {
        "type": "S3_BUCKET_NAME",
        "value": "amzn-s3-demo-bucket"
    }
}
```

In the preceding example, Macie attempted to list the bucket's objects by using
the [ListObjectsV2](../../../AmazonS3/latest/API/API_ListObjectsV2.md "../../../AmazonS3/latest/API/API_ListObjectsV2.md") operation of the Amazon S3 API. When Macie sent the request to
Amazon S3, Amazon S3 denied access to the bucket.

The following fields are common to all log events for sensitive data discovery
jobs:

- `adminAccountId` – The unique identifier for the
  AWS account that created the job.
- `jobId` – The unique identifier for the job.
- `eventType` – The type of event that occurred.
- `occurredAt` – The date and time, in Coordinated
  Universal Time (UTC) and extended ISO 8601 format, when the event
  occurred.
- `description` – A brief description of the event.
- `jobName` – The name of the job.

Depending on the type and nature of an event, a log event can also contain the
following fields:

- `affectedAccount` – The unique identifier for the
  AWS account that owns the affected resource.
- `affectedResource` – A JSON object that provides details
  about the affected resource. In the object, the `type` field
  specifies a field that stores metadata about a resource. The
  `value` field specifies the value for the field
  (`type`).
- `operation` – The operation that Macie attempted to
  perform and caused the error.
- `runDate` – The date and time, in Coordinated Universal
  Time (UTC) and extended ISO 8601 format, when the applicable job or job run
  started.

## Types of log events for

sensitive data discovery jobs

Amazon Macie publishes log events for three categories of events that can occur for a
sensitive data discovery job:

- Job status events, which record changes to the status or progress of a job
  or a job run.
- Account-level error events, which record errors that prevented Macie from
  analyzing Amazon S3 data for a specific AWS account.
- Bucket-level error events, which record errors that prevented Macie from
  analyzing data in a specific S3 bucket.

The topics in this section list and describe the types of events that Macie
publishes for each category.

### Job status

events

A job status event records a change to the status or progress of a job or a
job run. For periodic jobs, Macie logs and publishes these events for both the
overall job and individual job runs.

The following example uses sample data to show the structure and nature of the
fields in a job status event. In this example, a
`SCHEDULED_RUN_COMPLETED` event indicates that a scheduled run of
a periodic job finished running. The run started on April 14, 2024, at 17:09:30
UTC, as indicated by the `runDate` field. The run finished on April
14, 2024, at 17:16:30 UTC, as indicated by the `occurredAt`
field.

```
{
    "adminAccountId": "123456789012",
    "jobId": "ffad0e71455f38a4c7c220f3cexample",
    "eventType": "SCHEDULED_RUN_COMPLETED",
    "occurredAt": "2024-04-14T17:16:30.574809Z",
    "description": "The scheduled job run finished running.",
    "jobName": "My_Daily_Macie_Job",
    "runDate": "2024-04-14T17:09:30.574809Z"
}
```

The following table lists and describes the types of job status events that
Macie logs and publishes to CloudWatch Logs. The **Event
type** column indicates the name of each event as it appears in the
`eventType` field of an event. The **Description** column provides a brief description of the event as
it appears in the `description` field of an event. The **Additional information** provides information about the
type of job that the event applies to. The table is sorted first by the general
chronological order in which events might occur, and then in ascending
alphabetical order by event type.

| Event type                                | Description                                                                                                                                                       | Additional information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| JOB_CREATED                               | The job was created.                                                                                                                                              | Applies to one-time and periodic jobs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ONE_TIME_JOB_STARTED                      | The job started running.                                                                                                                                          | Applies only to one-time jobs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| SCHEDULED_RUN_STARTED                     | The scheduled job run started running.                                                                                                                            | Applies only to periodic jobs. To log the start of a one-time job, Macie publishes a ONE_TIME_JOB_STARTED event, not this type of event.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| BUCKET_MATCHED_THE_CRITERIA               | The affected bucket matched the bucket criteria specified for the job.                                                                                            | Applies to one-time and periodic jobs that use runtime bucket criteria to determine which S3 buckets to analyze. The `affectedResource` object specifies the name of the bucket that matched the criteria and was included in the job's analysis.                                                                                                                                                                                                                                                                                                               |
| NO_BUCKETS_MATCHED_THE_CRITERIA           | The job started running but no buckets currently match the bucket criteria specified for the job. The job didn't analyze any data.                                | Applies to one-time and periodic jobs that use runtime bucket criteria to determine which S3 buckets to analyze.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SCHEDULED_RUN_COMPLETED                   | The scheduled job run finished running.                                                                                                                           | Applies only to periodic jobs. To log completion of a one-time job, Macie publishes a JOB_COMPLETED event, not this type of event.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| JOB_PAUSED_BY_USER                        | The job was paused by a user.                                                                                                                                     | Applies to one-time and periodic jobs that you stopped temporarily (paused).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| JOB_RESUMED_BY_USER                       | The job was resumed by a user.                                                                                                                                    | Applies to one-time and periodic jobs that you stopped temporarily (paused) and later resumed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| JOB_PAUSED_BY_MACIE_SERVICE_QUOTA_MET     | The job was paused by Macie. Completion of the job would exceed a monthly quota for the affected account.                                                         | Applies to one-time and periodic jobs that Macie stopped temporarily (paused). Macie automatically pauses a job when additional processing by the job or a job run would exceed the monthly [sensitive data discovery quota](macie-quotas.md "macie-quotas.md") for one or more accounts that the job analyzes data for. To avoid this issue, consider increasing the quota for the affected accounts.                                                                                                                                                          |
| JOB_RESUMED_BY_MACIE_SERVICE_QUOTA_LIFTED | The job was resumed by Macie. The monthly service quota was lifted for the affected account.                                                                      | Applies to one-time and periodic jobs that Macie stopped temporarily (paused) and later resumed. If Macie automatically paused a one-time job, Macie automatically resumes the job when the subsequent month starts or the monthly sensitive data discovery quota is increased for all the affected accounts, whichever occurs first. If Macie automatically paused a periodic job, Macie automatically resumes the job when the next run is scheduled to start or the subsequent month starts, whichever occurs first.                                         |
| JOB_CANCELLED                             | The job was cancelled.                                                                                                                                            | Applies to one-time and periodic jobs that you stopped permanently (cancelled) or, for one-time jobs, paused and didn't resume within 30 days. If you suspend or disable Macie, this type of event also applies to jobs that were active or paused when you suspended or disabled Macie. Macie automatically cancels your jobs in an AWS Region if you suspend or disable Macie in the Region.                                                                                                                                                                  |
| JOB_COMPLETED                             | The job finished running.                                                                                                                                         | Applies only to one-time jobs. To log completion of a job run for a periodic job, Macie publishes a SCHEDULED_RUN_COMPLETED event, not this type of event.                                                                                                                                                                                                                                                                                                                                                                                                      | ### Account-level error events An account-level error event records an error that prevented Macie from analyzing objects in S3 buckets that are owned by a specific AWS account. The `affectedAccount` field in each event specifies the account ID for that account. The following example uses sample data to show the structure and nature of the fields in an account-level error event. In this example, an `ACCOUNT_ACCESS_DENIED` event indicates that Macie wasn't able to analyze objects in any S3 buckets that are owned by account `444455556666`. `{ "adminAccountId": "123456789012", "jobId": "85a55dc0fa6ed0be5939d0408example", "eventType": "ACCOUNT_ACCESS_DENIED", "occurredAt": "2024-04-14T17:08:30.585709Z", "description": "Macie doesn’t have permission to access S3 bucket data for the affected account.", "jobName": "My_Macie_Job", "operation": "ListBuckets", "runDate": "2024-04-14T17:05:27.574809Z", "affectedAccount": "444455556666" }` The following table lists and describes the types of account-level error events that Macie logs and publishes to CloudWatch Logs. The **Event type** column indicates the name of each event as it appears in the `eventType` field of an event. The **Description** column provides a brief description of the event as it appears in the `description` field of an event. The **Additional information** column provides any applicable tips for investigating or addressing the error that occurred. The table is sorted in ascending alphabetical order by event type.                                                                                                                                                                                                                                                                                                                                                                                     |
| Event type                                | Description                                                                                                                                                       | Additional information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                       | ---                                                                                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ACCOUNT_ACCESS_DENIED                     | Macie doesn’t have permission to access S3 bucket data for the affected account.                                                                                  | This typically occurs because the buckets that are owned by the account have restrictive bucket policies. For information about how to address this issue, see [Allowing Macie to access S3 buckets and objects](monitoring-restrictive-s3-buckets.md "monitoring-restrictive-s3-buckets.md"). The value for the `operation` field in the event can help you determine which permissions settings prevented Macie from accessing S3 data for the account. This field indicates the Amazon S3 operation that Macie attempted to perform when the error occurred. |
| ACCOUNT_DISABLED                          | The job skipped resources that are owned by the affected account. Macie was disabled for the account.                                                             | To address this issue, re-enable Macie for the account in the same AWS Region.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ACCOUNT_DISASSOCIATED                     | The job skipped resources that are owned by the affected account. The account isn't associated with your Macie administrator account as a member account anymore. | This occurs if you, as a Macie administrator for an organization, configure a job to analyze data for a member account and the account is later removed from your organization. To address this issue, re-associate the affected account with your Macie administrator account as a member account. For more information, see [Managing multiple accounts](macie-accounts.md "macie-accounts.md").                                                                                                                                                              |
| ACCOUNT_ISOLATED                          | The job skipped resources that are owned by the affected account. The AWS account was isolated.                                                                   | –                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ACCOUNT_REGION_DISABLED                   | The job skipped resources that are owned by the affected account. The AWS account isn't active in the current AWS Region.                                         | –                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ACCOUNT_SUSPENDED                         | The job was cancelled or skipped resources that are owned by the affected account. Macie was suspended for the account.                                           | If the specified account is your own account, Macie automatically cancelled the job when you suspended Macie in the same Region. To address the issue, re-enable Macie in the Region. If the specified account is a member account, re-enable Macie for that account in the same Region.                                                                                                                                                                                                                                                                        |
| ACCOUNT_TERMINATED                        | The job skipped resources that are owned by the affected account. The AWS account was terminated.                                                                 | –                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | ### Bucket-level error events A bucket-level error event records an error that prevented Macie from analyzing objects in a specific S3 bucket. The `affectedAccount` field in each event specifies the account ID for the AWS account that owns the bucket. The `affectedResource` object in each event specifies the name of the bucket. The following example uses sample data to show the structure and nature of the fields in a bucket-level error event. In this example, a `BUCKET_ACCESS_DENIED` event indicates that Macie wasn't able to analyze any objects in the S3 bucket named `amzn-s3-demo-bucket`. When Macie attempted to list the bucket's objects by using the [ListObjectsV2](../../../AmazonS3/latest/API/API_ListObjectsV2.md "../../../AmazonS3/latest/API/API_ListObjectsV2.md") operation of the Amazon S3 API, Amazon S3 denied access to the bucket. `{ "adminAccountId": "123456789012", "jobId": "85a55dc0fa6ed0be5939d0408example", "eventType": "BUCKET_ACCESS_DENIED", "occurredAt": "2024-04-14T17:11:30.574809Z", "description": "Macie doesn’t have permission to access the affected S3 bucket.", "jobName": "My_Macie_Job", "operation": "ListObjectsV2", "runDate": "2024-04-14T17:09:30.685209Z", "affectedAccount": "111122223333", "affectedResource": { "type": "S3_BUCKET_NAME", "value": "amzn-s3-demo-bucket" } }` The following table lists and describes the types of bucket-level error events that Macie logs and publishes to CloudWatch Logs. The **Event type** column indicates the name of each event as it appears in the `eventType` field of an event. The **Description** column provides a brief description of the event as it appears in the `description` field of an event. The **Additional information** column provides any applicable tips for investigating or addressing the error that occurred. The table is sorted in ascending alphabetical order by event type. |
| Event type                                | Description                                                                                                                                                       | Additional information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                       | ---                                                                                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| BUCKET_ACCESS_DENIED                      | Macie doesn’t have permission to access the affected S3 bucket.                                                                                                   | This typically occurs because a bucket has a restrictive bucket policy. For information about how to address this issue, see [Allowing Macie to access S3 buckets and objects](monitoring-restrictive-s3-buckets.md "monitoring-restrictive-s3-buckets.md"). The value for the `operation` field in the event can help you determine which permissions settings prevented Macie from accessing the bucket. This field indicates the Amazon S3 operation that Macie attempted to perform when the error occurred.                                                |
| BUCKET_DETAILS_UNAVAILABLE                | A temporary issue prevented Macie from retrieving details about the bucket and the bucket’s objects.                                                              | This occurs if a transient issue prevented Macie from retrieving the bucket and object metadata that it needs to analyze a bucket's objects. For example, an Amazon S3 exception occurred when Macie tried to verify that it's allowed to access the bucket. To address the issue for a one-time job, consider creating and running a new, one-time job to analyze objects in the bucket. For a scheduled job, Macie will try to retrieve the metadata again during the next job run.                                                                           |
| BUCKET_DOES_NOT_EXIST                     | The affected S3 bucket doesn’t exist anymore.                                                                                                                     | This typically occurs because a bucket was deleted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| BUCKET_IN_DIFFERENT_REGION                | The affected S3 bucket was moved to a different AWS Region.                                                                                                       | –                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| BUCKET_OWNER_CHANGED                      | The owner of the affected S3 bucket changed. Macie doesn’t have permission to access the bucket anymore.                                                          | This typically occurs if ownership of a bucket was transferred to an AWS account that isn't part of your organization. The `affectedAccount` field in the event indicates the account ID for the account that previously owned the bucket.                                                                                                                                                                                                                                                                                                                      |
