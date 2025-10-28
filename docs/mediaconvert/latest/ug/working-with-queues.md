# Working with queues in AWS Elemental MediaConvert

A queue is a set of resources that processes jobs. All jobs run in a queue.

To start a job, you submit it to a queue. AWS Elemental MediaConvert processes jobs that you submit to
a queue in parallel. When all of your queue's resources are used, additional jobs stay in a
`SUBMITTED` state until your queue's resources become available again. Use
queues to manage the resources that are available to your account, to process multiple jobs
concurrently, and to prioritize some jobs when needed.

MediaConvert offers the following two queue types:

**On-demand queues (recommended)**

With on-demand queues, you don't have to set up anything in advance. Your default queue is
an on-demand queue. You pay rates that depend on the features that you use. Most
customers use on-demand queues for their scalability and access to all
MediaConvert features. For more information, see [MediaConvert
Pricing](https://aws.amazon.com/mediaconvert/pricing/ "https://aws.amazon.com/mediaconvert/pricing/").

**Reserved queues**

With reserved queues, you pay for the transcoding capacity of the entire queue, regardless
of how much or how little you use it. Reserved queues require a 12-month
commitment, don't scale automatically, and have feature limitations compared to
on-demand queues. For more information, see [MediaConvert Pricing](https://aws.amazon.com/mediaconvert/pricing/ "https://aws.amazon.com/mediaconvert/pricing/") and
[Limitations](feature-limitations-with-reserved-queues.md "feature-limitations-with-reserved-queues.md").

If you don't specify a queue when you create your job, MediaConvert
sends it to the default on-demand queue.

For information about how many queues you can create and how many jobs those queues can run,
see [Service quotas](../../../general/latest/gr/mediaconvert.md#limits_mediaconvert "../../../general/latest/gr/mediaconvert.md#limits_mediaconvert") in
the _AWS General Reference Guide._

You can set up your job to move from one queue to another automatically if it stays in a
`SUBMITTED` state for too long. For more information, see [Moving a job to a different queue](setting-up-queue-hopping-to-avoid-long-waits.md "setting-up-queue-hopping-to-avoid-long-waits.md").

The time to complete a job varies significantly according to your input files and job
settings. Accordingly, MediaConvert doesn't always complete jobs in the same order that you
submit them.

###### How to specify a queue for your job

You specify a job's queue when you submit your job. The following tabs show different
options for specifying a queue for your job.

Console
To specify a queue for your job by using the MediaConvert console, complete these
steps:

1. Open the [Create job](https://console.aws.amazon.com/mediaconvert/home#/jobs/create "https://console.aws.amazon.com/mediaconvert/home#/jobs/create") page in the MediaConvert console.
2. Choose **Job management** from the **Job settings**
   menu.
3. Under **Queue**, choose a queue.

API, SDK, or the AWS CLI
To specify a job's queue by using the API, SDK, or the AWS Command Line Interface (AWS CLI),
specify the `Queue` property. This property is a direct child of
`Jobs`, which is in the top level of the JSON job specification.
Set `Queue` to the ARN of your queue.

The following is an excerpt of a job settings JSON with an example queue
specified.

```
{
	"Settings": {
		"OutputGroups": `[...]`,
		"Inputs": `[...]`
	},
	"Queue": `"arn:aws:mediaconvert:us-west-2:111122223333:queues/example"`
}
```

For more information, see the MediaConvert [API Reference](../apireference/jobs.md#jobs-prop-createjobrequest-queue "../apireference/jobs.md#jobs-prop-createjobrequest-queue").

The following topics provide information about how queues work in general, and about each
type of queue specifically.

###### Topics

- [On-demand
  queues](working-with-on-demand-queues.md "working-with-on-demand-queues.md")
- [Reserved queues](working-with-reserved-queues.md "working-with-reserved-queues.md")
- [Setting job priority](setting-the-priority-of-a-job.md "setting-the-priority-of-a-job.md")
- [Moving a job to a different queue](setting-up-queue-hopping-to-avoid-long-waits.md "setting-up-queue-hopping-to-avoid-long-waits.md")
