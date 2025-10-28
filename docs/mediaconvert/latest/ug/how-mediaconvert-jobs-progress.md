# Monitoring MediaConvert job

progress

MediaConvert provides status information for each job that you create. You can monitor a
job's status to determine what is happening with your job, track its progress, or
toubleshoot issues.

###### Topics

- [Job statuses](#job-statuses "#job-statuses")
- [How to find a job's status](#finding-job-status "#finding-job-status")
- [Job phases](#job-phase "#job-phase")

## Job statuses

Each job you submit will progress through a number of different possible statuses.
Successful jobs end with a `COMPLETE` status, and unsuccessful jobs end
with an `ERROR` or `CANCELED` status.

**Successful jobs**

A successful job results in all of its outputs being written to your
Amazon S3 bucket. The following list contains details about the different
statuses successful jobs go through:

1. `SUBMITTED`: Jobs that you created in the MediaConvert
   console or through a [`CreateJob`](../apireference/jobs.md#jobs-http-methods "../apireference/jobs.md#jobs-http-methods") operation that MediaConvert
   hasn't started processing.
2. `INPUT_INFORMATION`: MediaConvert read details about your
   input or inputs.
3. `PROGRESSING`: MediaConvert began processing your
   job.
4. `STATUS_UPDATE`: MediaConvert has been processing your job
   for at least a minute or longer. Jobs with this status go
   through three different _job
   phases_. For more information, see [Job phases](#job-phase "#job-phase").
5. `COMPLETE`: MediaConvert completed your job and all of
   your outputs were saved to your Amazon S3 bucket.

Successful jobs may also include [NEW_WARNING](ev_status_new_warning.md "ev_status_new_warning.md") or [QUEUE_HOP](ev_status_new_warning.md "ev_status_new_warning.md")
statuses.

**Unsuccessful jobs**

An unsuccessful job results in no outputs being written to your Amazon S3
bucket, although it may initially progress similar to a successful job.
Unsuccessful jobs have one of the the following two statuses:

- `ERROR`: MediaConvert had an issue processing your job.
  For more information, see [Error codes](mediaconvert_error_codes.md "mediaconvert_error_codes.md").
- `CANCELED`: You canceled a job in the MediaConvert console
  or through a `CancelJob` operation.

## How to find a job's status

To view a list of all job statuses in the current Region, open the [Jobs](https://console.aws.amazon.com/mediaconvert/home#/jobs/list "https://console.aws.amazon.com/mediaconvert/home#/jobs/list") page in the MediaConvert
console. Or submit a `GetJob` or `ListJobs` operation.

AWS CloudTrail records details about each create job request you make. CloudTrail only emits
an EventBridge event for `SUBMITTED` jobs if you also create a CloudTrail trail. For
more information, see [Working
with CloudTrail trails](../../../awscloudtrail/latest/userguide/cloudtrail-getting-started.md "../../../awscloudtrail/latest/userguide/cloudtrail-getting-started.md") and [Accessing AWS service
events via AWS CloudTrail](../../../eventbridge/latest/userguide/eb-service-event.md "../../../eventbridge/latest/userguide/eb-service-event.md").

MediaConvert emits an EventBridge event when a job begins processing and then whenever its
status changes, for example if it changes from `PROGRESSING` to
`COMPLETE` or `ERROR`. For list of EventBridge events, see [List of MediaConvert EventBridge events](mediaconvert_event_list.md "mediaconvert_event_list.md").

## Job phases

If a job's status is `PROGRESSING` for over a minute, MediaConvert emits a
`STATUS_UPDATE` event with the current job _phase_. A job phase provides details about what is happening with a
job. Job phases progress through the following order:

1. `PROBING`: When your job is in the `PROBING` phase,
   MediaConvert reads the information from your input files that the service
   needs for transcoding.
2. `TRANSCODING`: When your job is in the `TRANSCODING`
   phase, the service demuxes, decodes, encodes, and remuxes your content. In
   some jobs, the service begins uploading outputs to your output Amazon S3 bucket
   during this phase. The phase ends when all transcoding is complete.
3. `UPLOADING`: When your job is in the `UPLOADING`
   phase, the service uploads your transcoded outputs to your output Amazon S3
   bucket. In the case of outputs that the service begins to upload during the
   `TRANSCODING` phase, the `UPLOADING` phase begins
   when the transcoding is done. It continues until all uploads are
   finished.

To view a job's phase, open the [Jobs](https://console.aws.amazon.com/mediaconvert/home#/jobs/list "https://console.aws.amazon.com/mediaconvert/home#/jobs/list") page in the MediaConvert console, check
the [STATUS_UPDATE EventBridge
event](ev_status_status_update.md "ev_status_status_update.md"), or submit a `GetJob` or `ListJobs`
operation.
