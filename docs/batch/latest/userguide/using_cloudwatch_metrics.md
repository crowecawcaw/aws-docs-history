

# Using CloudWatch Metrics with AWS Batch
<a name="using_cloudwatch_metrics"></a>

AWS Batch publishes job metrics to Amazon CloudWatch for monitoring state transitions and durations of jobs as they move through their lifecycle. AWS Batch publishes these metrics under the `AWS/Batch` namespace at no additional charge.

Metrics are emitted as jobs transition between states and as job attempts complete. State transition metrics track how many jobs entered a given state, and duration metrics track how long jobs or job attempts spent moving between states. Use these metrics to build CloudWatch dashboards, set CloudWatch alarms, and establish performance baselines for your workloads. For more information, see [Using CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) and [Using CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

The reporting behavior for [Array jobs](array_jobs.md) and [Multi-node parallel jobs](multi-node-parallel-jobs.md) differs from single-node jobs. The **Reporting behavior** column in the following table notes these cases, and [Metrics for array jobs and multi-node parallel jobs](#cloudwatch_metrics_array_mnp) describes the array and MNP behavior in detail.

**Note**  
AWS Batch emits these metrics for jobs submitted to a job queue. All metrics are published with the `JobQueueName` dimension. You can use this dimension to group and filter metric data by the job queue that a job was submitted to.

**Important**  
These metrics are provided on a best-effort basis and are intended for monitoring and observability rather than billing, auditing, or reconciliation. Because job state transitions are event-driven, a metric can occasionally be missed. For example, if a job begins running and then succeeds or fails almost immediately, the transition into the `RUNNING` state might not be observed before the job reaches its terminal state. In that case, AWS Batch does not emit the metrics associated with the `RUNNING` transition for that job. Design any alarms or dashboards to tolerate occasional gaps, and don't rely on exact counts derived from these metrics.

## AWS Batch CloudWatch metrics
<a name="cloudwatch_metrics_available"></a>

AWS Batch sends the following job metrics to CloudWatch. State transition metrics use the `Count` unit and duration metrics use the `Milliseconds` unit.

The following metrics apply to AWS Batch jobs regardless of type.


| Metric | Description | Units | Reporting behavior | 
| --- | --- | --- | --- | 
| `JobsSubmitted` | The number of jobs that were submitted to the job queue. | Count | Emitted when a job is first submitted (enters the `SUBMITTED` state). For an array job, the value is the size of the array. | 
| `JobsMovedToPending` | The number of jobs that moved to the `PENDING` state. | Count | Emitted when a job moves to `PENDING`. A job is typically `PENDING` while it waits on a job dependency. | 
| `JobsMovedToRunnable` | The number of jobs that moved to the `RUNNABLE` state. | Count | Emitted when a job moves to `RUNNABLE`, either the first time or as the result of a retry attempt. | 
| `JobsMovedToStarting` | The number of jobs that moved to the `STARTING` state. | Count | Emitted when a job moves to `STARTING`. | 
| `JobsMovedToRunning` | The number of jobs that moved to the `RUNNING` state. | Count | Emitted when a job moves to `RUNNING`. | 
| `JobsMovedToSucceeded` | The number of jobs that completed successfully. | Count | Emitted when a job moves to `SUCCEEDED`. | 
| `JobsMovedToFailed` | The number of jobs that moved to the `FAILED` state. | Count | Emitted when a job enters the `FAILED` state. Includes jobs that were cancelled or terminated. | 
| `JobsCancelled` | The number of jobs that were cancelled. | Count | Emitted when a job enters the `FAILED` state as the result of a cancel request (before the job started running). | 
| `JobsTerminated` | The number of jobs that were terminated. | Count | Emitted when a job enters the `FAILED` state as the result of a terminate request. | 
| `JobsRetried` | The number of job attempts that were retried. | Count | Emitted when a job attempt fails and the job is returned to `RUNNABLE` to be retried. | 
| `JobSubmittedToRunnableDuration` | The time a job took to go from `SUBMITTED` to `RUNNABLE`. | Milliseconds | Emitted when the job enters `RUNNABLE`. For an array child job, this measures the time from when the parent job was submitted to when the child job became `RUNNABLE`. | 
| `JobAttemptStartingToRunningDuration` | The time a job attempt spent in `STARTING` before it began running. | Milliseconds | Emitted per attempt when the job enters `RUNNING`. A retried job emits one data point per attempt that reaches `RUNNING`. | 
| `JobAttemptExecutionDuration` | The time a job attempt spent running, measured from when the attempt started to when it stopped. | Milliseconds | Emitted when a job attempt completes, measured from when the attempt started running to when it stopped. | 
| `JobAttemptDuration` | The total time a job attempt lasted, measured from when it entered `STARTING` until the attempt ended. | Milliseconds | Emitted when an attempt ends. The attempt ends either when the job reaches a terminal state (`SUCCEEDED` or `FAILED`) or when it returns to `RUNNABLE` to be retried. | 

The following metrics apply only to AWS Batch compute jobs.


| Metric | Description | Units | Reporting behavior | 
| --- | --- | --- | --- | 
| `JobSubmittedToFirstStartingDuration` | The time a job took to go from `SUBMITTED` to its first time in `STARTING`. | Milliseconds | Emitted on the first attempt, when the job first enters `STARTING`.  | 
| `JobAttemptRunnableToStartingDuration` | The time a job attempt spent in `RUNNABLE` before it started. | Milliseconds | Emitted when the job enters `STARTING`. | 

The following metrics apply only to [Service jobs in AWS Batch](service-jobs.md).


| Metric | Description | Units | Reporting behavior | 
| --- | --- | --- | --- | 
| `JobsMovedToScheduled` | The number of jobs that moved to the `SCHEDULED` state. | Count | Emitted for service jobs when the job first moves to `SCHEDULED`, and again each time the job moves to `SCHEDULED` after a preemption. | 
| `JobSubmittedToFirstScheduledDuration` | The time a service job took to go from `SUBMITTED` to its first time in `SCHEDULED`. | Milliseconds | Emitted for service jobs when the job first moves to `SCHEDULED`. | 
| `JobAttemptRunnableToScheduledDuration` | The time a job attempt spent in `RUNNABLE` before it moved to `SCHEDULED`. | Milliseconds | Emitted per attempt when a service job moves to `SCHEDULED`, both the first time the job moves to `SCHEDULED` and each time it moves to `SCHEDULED` after a preemption. | 
| `JobAttemptScheduledToStartingDuration` | The time a service job attempt spent between first moving to `SCHEDULED` and moving to `STARTING`. | Milliseconds | Emitted for service jobs when the job moves from `SCHEDULED` to `STARTING`. | 
| `JobsPreempted` | The number of jobs that were preempted. | Count | Emitted for quota management jobs each time the job is preempted. | 

## Metrics for array jobs and multi-node parallel jobs
<a name="cloudwatch_metrics_array_mnp"></a>

AWS Batch represents [Array jobs](array_jobs.md) and [Multi-node parallel jobs](multi-node-parallel-jobs.md) as a *parent* job that tracks one or more *child* jobs. So that a single logical job isn't counted twice, AWS Batch emits metrics from only one of these two records, depending on the job type.

Array jobs  
The array parent job does not emit metrics, except for `JobsSubmitted`. Instead, each array child job emits these metrics independently as it moves through the job lifecycle, so the metric counts reflect the number of child jobs rather than the number of array jobs submitted.  
The `JobsSubmitted` metric is emitted once for the array parent job at submission, and its value is the size of the array (the number of child jobs). For example, submitting one array job with 1,000 children publishes a single `JobsSubmitted` data point with a value of `1000`.  
Duration metrics that measure time from submission — such as `JobSubmittedToRunnableDuration` — are emitted per array child job and measure from when the array parent was submitted to when that child reached the state in question.

Multi-node parallel (MNP) jobs  
MNP metrics are emitted from the MNP parent job, which represents the job as a whole. The individual MNP child (node) jobs do not emit these metrics. As a result, an MNP job is counted once regardless of how many nodes it uses.

## Dimensions for AWS Batch CloudWatch metrics
<a name="cloudwatch_metrics_dimensions"></a>

AWS Batch job metrics in CloudWatch use a single dimension: `JobQueueName`. All metric data is grouped and filtered by the name of the job queue that a job was submitted to.

## View AWS Batch CloudWatch metrics
<a name="viewing-batch-cloudwatch-metrics"></a>

You can view AWS Batch job metrics in the AWS Batch console, or in the CloudWatch console under the `AWS/Batch` namespace.

**Important**  
Displaying metrics in the console incurs standard CloudWatch charges. You can turn off metric viewing at any time to stop the charges. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

**To view metrics on the Batch metrics dashboard**

1. Open the [AWS Batch console](https://console.aws.amazon.com/batch).

1. In the navigation pane, choose **Dashboard**, then choose the **Batch metrics** tab.

1. Turn on **Display CloudWatch metrics**.

1. Under **Filter metrics**, select up to five **Job queues** and the **Metrics** you want to graph.

1. Choose **Apply filters**. The console shows one graph per metric, with one line per job queue.

1. To start over, choose **Clear filters** to remove your selections, or **Reset filters** to restore the defaults.

1. (Optional) To reuse a combination of job queues and metrics, work with a saved filter set. Filter sets are saved to your AWS user preferences, so they persist across sessions, and you can save up to five. Manage them from the **Saved filter sets** dropdown and the arrow menu on the **Clear filters** button, then choose any of the following:
   + **Save** - Select your job queues and metrics, then choose **Save as new filter set**. Enter a unique name and optionally mark it as the default.
   + **Apply** - Choose a set from the **Saved filter sets** dropdown, then choose **Apply filters**.
   + **Update** - With a set selected, change your selections and choose **Update current filter set**.
   + **Set as default** - With a set selected, choose **Settings**, then **Set as default**. The default set loads automatically when you open the tab.
   + **Delete** - With a set selected, choose **Delete current filter set**.

**To view metrics for a single job queue**

1. In the navigation pane, choose **Job queues**, then choose a job queue.

1. Choose the **Monitoring** tab.

1. Turn on **Display CloudWatch metrics**.

1. In the **State transition metrics**, **Lifecycle event metrics**, and **Duration metrics** sections, use each metrics selector to choose which metrics to graph.

The metrics shown are scoped to this job queue. Your selections are saved per job queue and persist across sessions.

To work with these metrics directly in CloudWatch — for example, to build dashboards or set alarms — open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch) and choose the `AWS/Batch` namespace.