# Tracking job status and completion reports

With S3 Batch Operations, you can view and update job status, add notifications and logging,
track job failures, and generate completion reports.

###### Topics

- [Job statuses](#batch-ops-job-status-table "#batch-ops-job-status-table")
- [Updating job status](#updating-job-statuses "#updating-job-statuses")
- [Notifications and logging](#batch-ops-notifications "#batch-ops-notifications")
- [Tracking job failures](#batch-ops-job-status-failure "#batch-ops-job-status-failure")
- [Completion reports](#batch-ops-completion-report "#batch-ops-completion-report")
- [Examples: Tracking an S3 Batch Operations job in Amazon EventBridge through AWS CloudTrail](batch-ops-examples-event-bridge-cloud-trail.md "batch-ops-examples-event-bridge-cloud-trail.md")
- [Examples: S3 Batch Operations completion reports](batch-ops-examples-reports.md "batch-ops-examples-reports.md")

## Job statuses

After you create and run a job, it progresses through a series of statuses. The following
table describes the statuses and possible transitions between them.

| Status       | Description                                                                                                                                                                                                                                                                                                                                                                                                | Transitions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `New`        | A job begins in the `New` state when you create it.                                                                                                                                                                                                                                                                                                                                                        | A job automatically moves to the `Preparing` state when Amazon S3 begins<br>processing the manifest object.                                                                                                                                                                                                                                                                                                                                                                                       |
| `Preparing`  | Amazon S3 is processing the manifest object and other job parameters to set up and run<br>the job.                                                                                                                                                                                                                                                                                                         | A job automatically moves to the `Ready` state after Amazon S3 finishes<br>processing the manifest and other parameters. The job is then ready to begin running<br>the specified operation on the objects listed in the manifest.If the job<br>requires confirmation before running, such as when you create a job using the Amazon S3<br>console, then the job transitions from `Preparing` to<br>`Suspended`. It remains in the `Suspended` state until you<br>confirm that you want to run it. |
| `Suspended`  | The job requires confirmation, but you haven't yet confirmed that you want to run<br>it. Only jobs that you create using the Amazon S3 console require confirmation. A job<br>that's created using the console enters the `Suspended` state immediately<br>after `Preparing`. After you confirm that you want to run the job and the<br>job becomes `Ready`, it never returns to the `Suspended`<br>state. | After you confirm that you want to run the job, its status changes to<br>`Ready`.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `Ready`      | Amazon S3 is ready to begin running the requested object operations.                                                                                                                                                                                                                                                                                                                                       | A job automatically moves to `Active` when Amazon S3 begins to run it. The<br>amount of time that a job remains in the `Ready` state depends on whether<br>you have higher-priority jobs running already and how long those jobs take to<br>complete.                                                                                                                                                                                                                                             |
| `Active`     | Amazon S3 is performing the requested operation on the objects listed in the manifest. While a job<br>is `Active`, you can monitor its progress using the Amazon S3 console or the<br>`DescribeJob` operation through the REST API, AWS CLI, or AWS<br>SDKs.                                                                                                                                               | A job moves out of the `Active` state when the job is no longer<br>running operations on objects. This behavior can happen automatically, such as when a<br>job completes successfully or fails. Or this behavior can occur as a result of user<br>actions, such as canceling a job. The state that the job moves to depends on the<br>reason for the transition.                                                                                                                                 |
| `Pausing`    | The job is transitioning to `Paused` from another state.                                                                                                                                                                                                                                                                                                                                                   | A job automatically moves to `Paused` when the `Pausing`<br>stage is finished.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `Paused`     | A job can become `Paused` if you submit another job with a higher<br>priority while the current job is running.                                                                                                                                                                                                                                                                                            | A `Paused` job automatically returns to `Active` after any<br>higher-priority jobs that are blocking the job's' execution complete, fail, or are<br>suspended.                                                                                                                                                                                                                                                                                                                                    |
| `Completing` | The job is transitioning to `Complete` from another state.                                                                                                                                                                                                                                                                                                                                                 | A job automatically moves to `Complete` when the `Completing` stage is<br>finished.                                                                                                                                                                                                                                                                                                                                                                                                               |
| `Complete`   | The job has finished performing the requested operation on all objects in the<br>manifest. The operation might have succeeded or failed for every object. If you<br>configured the job to generate a completion report, the report is available as soon as<br>the job is `Complete`.                                                                                                                       | `Complete` is a terminal state. Once a job reaches<br>`Complete`, it doesn't transition to any other state.                                                                                                                                                                                                                                                                                                                                                                                       |
| `Cancelling` | The job is transitioning to the `Cancelled` state.                                                                                                                                                                                                                                                                                                                                                         | A job automatically moves to `Cancelled` when the<br>`Cancelling` stage is finished.                                                                                                                                                                                                                                                                                                                                                                                                              |
| `Cancelled`  | You requested that the job be canceled, and S3 Batch Operations has successfully<br>canceled the job. The job won't submit any new requests to Amazon S3.                                                                                                                                                                                                                                                  | `Cancelled` is a terminal state. After a job reaches<br>`Cancelled`, the job won't transition to any other state.                                                                                                                                                                                                                                                                                                                                                                                 |
| `Failing`    | The job is transitioning to the `Failed` state.                                                                                                                                                                                                                                                                                                                                                            | A job automatically moves to `Failed` once the `Failing`<br>stage is finished.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `Failed`     | The job has failed and is no longer running. For more information about job<br>failures, see [Tracking job failures](#batch-ops-job-status-failure "#batch-ops-job-status-failure").                                                                                                                                                                                                                       | `Failed` is a terminal state. After a job reaches `Failed`,<br>it won't transition to any other state.                                                                                                                                                                                                                                                                                                                                                                                            |

## Updating job status

The following AWS CLI and AWS SDK for Java examples update the status of a Batch Operations job. For
more information about using the Amazon S3 console to manage Batch Operations jobs, see [Using the Amazon S3 console to manage your S3 Batch Operations jobs](batch-ops-managing-jobs.md#batch-ops-manage-console "batch-ops-managing-jobs.md#batch-ops-manage-console").

To use the following example commands, replace the `user input
 placeholders` with your own information.

- If you didn't specify the `--no-confirmation-required` parameter in
  your `create-job` command, the job remains in a suspended state until you
  confirm the job by setting its status to `Ready`. Amazon S3 then makes the job
  eligible for execution.

```
aws s3control update-job-status \
    --region `us-west-2` \
    --account-id `123456789012` \
    --job-id `00e123a4-c0d8-41f4-a0eb-b46f9ba5b07c` \
    --requested-job-status 'Ready'
```

- Cancel the job by setting the job status to `Cancelled`.

```
aws s3control update-job-status \
     --region `us-west-2` \
     --account-id `123456789012` \
     --job-id `00e123a4-c0d8-41f4-a0eb-b46f9ba5b07c` \
     --status-update-reason "`No longer needed`" \
     --requested-job-status Cancelled
```

For examples of how to update job status with the AWS SDK for Java, see [Update the status of a batch job](../API/s3-control_example_s3-control_UpdateJobStatus_section.md "../API/s3-control_example_s3-control_UpdateJobStatus_section.md") in the _Amazon S3 API Reference_.

## Notifications and logging

In addition to requesting completion reports, you can also capture, review, and audit
Batch Operations activity by using AWS CloudTrail. Because Batch Operations uses existing Amazon S3 API operations to
perform tasks, those tasks also emit the same events that they would if you called them
directly. Therefore, you can track and record the progress of your job and all of its tasks by
using the same notification, logging, and auditing tools and processes that you already use
with Amazon S3. For more information, see the examples in the following sections.

###### Note

Batch Operations generates both management and data events in CloudTrail during job execution. The
volume of these events scale with the number of keys in each job's manifest. For more
information, see the [CloudTrail pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/")
page, which includes examples of how pricing changes depending on the number of trails that
you have configured in your account. To learn how to configure and log events to fit your
needs, see [Create your
first trail](../../../awscloudtrail/latest/userguide/cloudtrail-tutorial.md#tutorial-step2 "../../../awscloudtrail/latest/userguide/cloudtrail-tutorial.md#tutorial-step2") in the _AWS CloudTrail User Guide_.

For more information about Amazon S3 events, see [Amazon S3 Event Notifications](EventNotifications.md "EventNotifications.md").

## Tracking job failures

If an S3 Batch Operations job encounters a problem that prevents it from running successfully,
such as not being able to read the specified manifest, the job fails. When a job fails, it
generates one or more failure codes or failure reasons. S3 Batch Operations stores the failure
codes and reasons with the job so that you can view them by requesting the job's details. If
you requested a completion report for the job, the failure codes and reasons also appear
there.

To prevent jobs from running a large number of unsuccessful operations, Amazon S3 imposes a
task-failure threshold on every Batch Operations job. When a job has run at least 1,000 tasks, Amazon S3
monitors the task-failure rate. At any point, if the failure rate (the number of tasks that
have failed as a proportion of the total number of tasks that have run) exceeds 50 percent,
the job fails. If your job fails because it exceeded the task-failure threshold, you can
identify the cause of the failures. For example, you might have accidentally included some
objects in the manifest that don't exist in the specified bucket. After fixing the errors, you
can resubmit the job.

###### Note

S3 Batch Operations operates asynchronously and the tasks don't necessarily run in the order
that the objects are listed in the manifest. Therefore, you can't use the manifest ordering
to determine which objects' tasks succeeded and which ones failed. Instead, you can examine
the job's completion report (if you requested one) or view your AWS CloudTrail event logs to help
determine the source of the failures.

## Completion reports

When you create a job, you can request a completion report. As long as
S3 Batch Operations successfully invokes at least one task, Amazon S3 generates a completion
report after the job finishes running tasks, fails, or is canceled. You can configure the
completion report to include all tasks or only failed tasks.

The completion report includes the job configuration, status, and information for each
task, including the object key and version, status, error codes, and descriptions of any
errors. Completion reports provide an easy way to view the results of your tasks in a
consolidated format with no additional setup required. Completion reports are encrypted by
using server-side encryption with Amazon S3 managed keys (SSE-S3). For an example of a completion
report, see [Examples: S3 Batch Operations completion reports](batch-ops-examples-reports.md "batch-ops-examples-reports.md").

If you don't configure a completion report, you can still monitor and audit your job and
its tasks by using CloudTrail and Amazon CloudWatch. For more information, see the following topics:

###### Topics

- [Examples: Tracking an S3 Batch Operations job in Amazon EventBridge through AWS CloudTrail](batch-ops-examples-event-bridge-cloud-trail.md "batch-ops-examples-event-bridge-cloud-trail.md")
- [Examples: S3 Batch Operations completion reports](batch-ops-examples-reports.md "batch-ops-examples-reports.md")
