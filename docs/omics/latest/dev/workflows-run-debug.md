

# Debugging a HealthOmics workflow run
<a name="workflows-run-debug"></a>

HealthOmics reports a run's behavior through several sources, each of which answers a different question. For a run that failed, read them in this order instead of starting with the logs:

1. Read the run record for whether the run failed, and why.

1. Read the task records, if a task failed, for which tasks failed and on which instance types. A run can also fail before any task is created, or after every task finished.

1. Read the logs: the task log for what a task reported, the run log for what the run reported outside any task, and the engine log for what the engine reported.

1. Read the run metrics and run manifest log for what the task consumed.

For a run that completed but was slower or more expensive than you expected, start from [Compare runs of the same workflow](#workflows-run-debug-compare).

The resource and cost guidance in this topic applies to private workflows, for the reason given in [Run optimization for a private HealthOmics workflow](workflows-run-optimize.md). For the API operations and response fields that the following steps use, see [Get run information](getinfo-about-runs.md).

In the commands in this topic, replace the following values with your own:

`{{run_id}}`  
The ID of the run you are debugging.

`{{duration}}`  
The window that **aws logs tail** reads: a relative time such as `2h` for a run that finished recently, or a timestamp such as `2026-03-26T22:00:00` for an older one.

`{{run_uuid}}`  
The `uuid` field of that run's record.

`{{task_id}}`  
The ID of a failed task in that run.

`{{workflow_id}}`  
The ID of the workflow whose runs you want to list.

**Topics**
+ [Diagnose a failed run](#workflows-run-debug-failed)
+ [Inspect resource use with run metrics](#workflows-run-debug-metrics)
+ [Compare runs of the same workflow](#workflows-run-debug-compare)
+ [Turn findings into cost and sizing changes](#workflows-run-debug-cost)

## Diagnose a failed run
<a name="workflows-run-debug-failed"></a>

**To diagnose a failed run**

1. Retrieve the run record, and read `status`, `failureReason`, `statusMessage`, and `logLocation`. Keep the response: later steps use it. `logLocation` gives the ARNs of the run log (`runLogStream`) and the engine log (`engineLogStream`).

   ```
   aws omics get-run --id {{run_id}}
   ```

   Look up the value of `failureReason` in [Run failure reasons](workflows-run-errors.md). If `status` isn't `FAILED`, see [Run status values](monitoring-runs.md#run-status-values) instead.

   Some failures happen before HealthOmics creates any task, or after every task finished, so they leave no task record for the next three steps to read. A role, input, import, or export failure is one; so is an image that HealthOmics rejects before it creates the task (ECR\_IMAGE\_NOT\_FOUND, ECR\_PERMISSION\_ERROR, ECR\_REPOSITORY\_NOT\_FOUND, or INVALID\_ECR\_IMAGE\_URI). For any of them, skip to the run log later in this procedure. For an image failure, `statusMessage` names the image URI, so continue from [Container images for private workflows](workflows-ecr.md) and [Amazon ECR permissions](permissions-ecr.md). If the next step does return a failed task, read that task instead.

1. List the tasks that failed. Each item includes the task's `taskId`, which the next step uses, plus its name, its `creationTime`, and, once it reached them, its instance type, `startTime`, and `stopTime`.

   ```
   aws omics list-run-tasks --id {{run_id}} --status FAILED
   ```

   If this returns no tasks, the run is one of the cases in step 1: skip the next two steps and read the run log.

1. For each failed task, retrieve its record. It adds `failureReason`, `statusMessage`, `imageDetails`, and `logStream` to what the previous step returned. `logStream` is the ARN of the log stream that the next step reads, and the stream's name follows `log-stream:` in it.

   ```
   aws omics get-run-task --id {{run_id}} --task-id {{task_id}}
   ```

1. Read the task log. The events that explain the failure are at the end of the stream.

   ```
   aws logs tail /aws/omics/WorkflowLog \
     --log-stream-names run/{{run_id}}/task/{{task_id}} \
     --since {{duration}}
   ```

   Set {{duration}} to start before the task did: the command reads from then until now, and its default window is the last 10 minutes, so a run that finished earlier returns no events. For the log group and the format of every stream, see [Logs in CloudWatch](monitoring-cloudwatch-logs.md#cloudwatch-logs).
**Note**  
For why a task might have no log at all, and for ways to make a task more debuggable, see [Troubleshooting workflow tasks](workflow-run-tasks.md#debugging-tasks).

1. Read whichever of the run's other two logs answers the question that brought you here. Both take the step 4 command with a different stream.

   ```
   aws logs tail /aws/omics/WorkflowLog \
     --log-stream-names run/{{run_id}} \
     --since {{duration}}
   ```  
The run has no failed task  
Read the run log, `run/{{run_id}}`, as in the preceding command. It reports the run's own progress, including the import and export steps that fail with no task. For what it reports, see [Log types for HealthOmics workflows](monitoring-cloudwatch-logs.md#log-descriptions).  
A task failed and its log doesn't explain why  
Read the engine log, `run/{{run_id}}/engine`, which reports what the engine made of the failure, such as the position in the workflow definition. Its ARN is in `logLocation.engineLogStream` from step 1; if that field isn't in the response, the run has no engine log.  
To read the definition at the position the engine names, export it. The following command returns a download URL for the definition that the run used.  

   ```
   aws omics get-workflow --id {{workflow_id}} --export DEFINITION
   ```

Where to continue depends on the failure reason. The following list covers the most common resource and container failures. For what the tasks consumed, which tells you whether the failure was a sizing problem, see [Turn findings into cost and sizing changes](#workflows-run-debug-cost).

**CANNOT\_START\_CONTAINER\_ERROR, CANNOT\_START\_CONTAINER\_SIZE\_ERROR, or IMAGE\_VERIFICATION\_FAILURE**  
HealthOmics created the task and couldn't start its container, so the task produced no log. Take the image from the task record's `imageDetails`, then see [Container images for private workflows](workflows-ecr.md).

**OUT\_OF\_MEMORY\_ERROR**  
Compare the task's memory use against its allocation, as described in [How do I right-size the compute and storage for my workflow?](troubleshooting.md#troubleshooting-metrics-right-size), using either its run metrics or its statistics in the run manifest log, which [Turn findings into cost and sizing changes](#workflows-run-debug-cost) locates. Then raise the memory in the workflow definition, and check which instance type the new value selects in [Compute and memory requirements for HealthOmics tasks](memory-and-compute-tasks.md).

**TASK\_TIMED\_OUT or RUN\_TIMED\_OUT**  
Confirm whether the task was still doing work when the timeout expired. If it wasn't, treat it as unresponsive rather than slow, and see [Guidance for unresponsive runs](workflows-run-errors.md#workflows-guidance-unresponsive-runs). If the limit that ended the run came from a run group, see [Using HealthOmics run groups](creating-run-groups.md).

## Inspect resource use with run metrics
<a name="workflows-run-debug-metrics"></a>

Run metrics cover a run that is still in progress, so you can use them before a run finishes. Which series exist for a run depends on its run storage type, its scratch storage mode, and whether its tasks requested accelerators, so check the conditions in [Available metrics](monitoring-run-metrics.md#monitoring-run-metrics-available) before you conclude that a metric is missing. If a run has no series at all, check that its role could publish them, as described in [Enabling metrics for a run](monitoring-run-metrics.md#monitoring-run-metrics-enabling). For the query syntax and the console procedure, see [Querying HealthOmics run metrics](monitoring-run-metrics.md#monitoring-run-metrics-viewing).

Scope every query to one run with the run resource label. Per-task metrics also carry the task resource label, which joins a series to the task record and its logs. For both labels, see [Common attributes](monitoring-run-metrics.md#monitoring-run-metrics-common-attributes).

**Note**  
CloudWatch caps both the number of time series a PromQL query returns and the time range it spans. A run produces at least one series per task for each per-task metric, and more where the metric splits by direction or by GPU. For a run with many tasks, aggregate the series in the query itself, or filter to one task, one direction, or one GPU. Split a long run into consecutive windows. For the current limits, see [PromQL limits and restrictions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL.html#CloudWatch-PromQL-Limits).

## Compare runs of the same workflow
<a name="workflows-run-debug-compare"></a>

When a run is slower or more expensive than an earlier run of the same workflow, compare the two runs task by task. Align the tasks by name rather than by task ID: retrieve the tasks of both runs, group them by `name`, and compare the duration and the peak values for each name. One read of each run's manifest log gives you every task's timings and, where the entry reports them, its peaks; **ListRunTasks** gives you the timings for a run that is still going, without the `--status FAILED` filter that the preceding procedure uses.

Compare two spans per task: `startTime` to `stopTime` is the task's duration, and `creationTime` to `startTime` is how long it waited to start, which covers its Pending and Starting phases in [Task status values](workflow-run-tasks.md#task-status-values). A run can be much slower than another while every task's duration matches, because no task metric covers the wait.

**Note**  
Several tasks in one run can share a name, and a scatter index in a name doesn't necessarily cover the same input data in both runs. Compare the aggregate across the tasks that share a name, such as the longest duration or the highest peak, rather than pairing them index by index.

To establish what is normal for a workflow rather than comparing two runs, aggregate a set of its completed runs. Run Analyzer does this in `--batch` mode, as described in [Impact of file size variance between runs](workflows-run-optimize.md#workflows-run-file-variance). To collect the runs yourself, filter the response of **ListRuns** on `workflowId`. The operation has no workflow filter of its own, so **ListRuns** pages through every completed run before your filter narrows them.

```
aws omics list-runs --status COMPLETED \
  --query "items[?workflowId=='{{workflow_id}}'].id"
```

The distribution across a set of runs, not any single run, shows whether a task's allocation fits the variance in your data, and whether a slow-looking run is outside the normal range.

## Turn findings into cost and sizing changes
<a name="workflows-run-debug-cost"></a>

What a task consumed is in the run manifest log, whose stream is `manifest/run/{{run_id}}/{{run_uuid}}`. HealthOmics writes it after the run finishes, so set {{duration}} to reach the run's stop time rather than a task's. Read it with the same **aws logs tail** command as the other streams. For the statistics it reports, see [Log types for HealthOmics workflows](monitoring-cloudwatch-logs.md#log-descriptions).

A manifest task entry reports what the task reserved, its instance type, and its duration. It reports what the task used alongside those, but not for every task. Where an entry doesn't report usage, or reports less than the task's work can account for, size against the task's run metrics instead, for the reason given in [Callouts](monitoring-run-metrics.md#monitoring-run-metrics-callouts).

Three HealthOmics behaviors limit what a change saves:
+ A task's cost follows the instance type that HealthOmics selects for the resources you request, not the resources the task uses. See [Compute and memory requirements for HealthOmics tasks](memory-and-compute-tasks.md).
+ Task charges have a minimum billable duration, so shortening an already short task saves nothing. See [Pricing implications of run status](monitoring-runs.md#run-status-billing).
+ Static run storage comes in fixed sizes, so a reduction changes the bill only when it drops to a smaller supported size. See [Static run storage](workflows-run-types.md#workflows-run-type-static).

For the optimization methods that these findings feed into, see [Methods to optimize runs](workflows-run-optimize.md#run-optimize-methods).