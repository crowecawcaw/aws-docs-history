# Modify a job in Deadline Cloud

You can use the following AWS Command Line Interface (AWS CLI) `update` commands to modify the
 configuration of a job, or to set the target status of a job, step, or task: 


* `aws deadline update-job`
* `aws deadline update-step`
* `aws deadline update-task`
In the following examples of the `update` commands, replace each
 ``user input placeholder`` with your own
 information.

###### Example – Requeue a job

All tasks in the job switch to the `READY` status, unless there are step
 dependencies. Steps with dependencies switch to either `READY` or
 `PENDING` as they are restored.


```
aws deadline update-job \
--farm-id `farmID` \
--queue-id `queueID` \
--job-id `jobID` \
--target-task-run-status PENDING
```
###### Example – Cancel a job

All tasks in the job that don't have the status `SUCCEEDED` or
 `FAILED` are marked `CANCELED`.


```
aws deadline update-job \
--farm-id `farmID` \
--queue-id `queueID` \
--job-id `jobID` \
--target-task-run-status CANCELED
```
###### Example – Mark a job failed

All tasks in the job that have the status `SUCCEEDED` are left unchanged. All
 other tasks are marked `FAILED`.


```
aws deadline update-job \
--farm-id `farmID` \
--queue-id `queueID` \
--job-id `jobID` \
--target-task-run-status FAILED
```
###### Example – Mark a job successful

All tasks in the job move to the `SUCCEEDED` state.


```
aws deadline update-job \
--farm-id `farmID` \
--queue-id `queueID` \
--job-id `jobID` \
--target-task-run-status SUCCEEDED
```
###### Example – Suspend a job

Tasks in the job in the `SUCCEEDED`, `CANCELED`, or
 `FAILED` state don't change. All other tasks are marked
 `SUSPENDED`.


```
aws deadline update-job \
--farm-id `farmID` \
--queue-id `queueID` \
--job-id `jobID` \
--target-task-run-status SUSPENDED
```
###### Example – Change the priority of a job

Updates the priority of a job in a queue to change the order that it is scheduled.
 Higher priority jobs are generally scheduled first.


```
aws deadline update-job \
--farm-id `farmID` \
--queue-id `queueID` \
--job-id `jobID` \
--priority 100
```
###### Example – Change the number of failed tasks allowed

Updates the maximum number of failed tasks that the job can have before the remaining
 tasks are canceled.


```
aws deadline update-job \
--farm-id `farmID` \
--queue-id `queueID` \
--job-id `jobID` \
--max-failed-tasks-count 200
```
###### Example – Change the number of task retries allowed

Updates the maximum number of retries for a task before the task fails. A task that has
 reached the maximum number of retries can't be requeued until this value is
 increased.


```
aws deadline update-job \
--farm-id `farmID` \
--queue-id `queueID` \
--job-id `jobID` \
--max-retries-per-task 10
```
###### Example – Archive a job

Updates the job's lifecycle status to `ARCHIVED`. Archived jobs can't be
 scheduled or modified. You can only archive a job that is in the `FAILED`,
 `CANCELED`, `SUCCEEDED`, or `SUSPENDED` state.


```
aws deadline update-job \
--farm-id `farmID` \
--queue-id `queueID` \
--job-id `jobID` \
--lifecycle-status ARCHIVED
```
###### Example – Requeue a step

All tasks in the step switch to the `READY` state, unless there are step
 dependencies. Tasks in steps with dependencies switch to either `READY` or
 `PENDING`, and the task is restored.


```
aws deadline update-step \
--farm-id `farmID` \
--queue-id `queueID` \
--job-id `jobID` \
--step-id `stepID` \
--target-task-run-status PENDING
```
###### Example – Cancel a step

All tasks in the step that don't have the status `SUCCEEDED` or
 `FAILED` are marked `CANCELED`.


```
aws deadline update-step \
--farm-id `farmID` \
--queue-id `queueID` \
--job-id `jobID` \
--step-id `stepID` \
--target-task-run-status CANCELED
```
###### Example – Mark a step failed

All tasks in the step that have the status `SUCCEEDED` are left unchanged.
 All other tasks are marked `FAILED`.


```
aws deadline update-step \
--farm-id `farmID` \
--queue-id `queueID` \
--job-id `jobID` \
--step-id `stepID` \
--target-task-run-status FAILED
```
###### Example – Mark a step successful

All tasks in the step are marked `SUCCEEDED`.


```
aws deadline update-step \
--farm-id `farmID` \
--queue-id `queueID` \
--job-id `jobID` \
--step-id `stepID` \
--target-task-run-status SUCCEEDED
```
###### Example – Suspend a step

Tasks in the step in the `SUCCEEDED`, `CANCELED`, or
 `FAILED` state don't change. All other tasks are marked
 `SUSPENDED`.


```
aws deadline update-step \
--farm-id `farmID` \
--queue-id `queueID` \
--job-id `jobID` \
--step-id `stepID` \
--target-task-run-status SUSPENDED
```
###### Example – Change the status of a task

When you use the `update-task` Deadline Cloud CLI command, the task switches to the
 specified status.


```
aws deadline update-task \
--farm-id `farmID` \
--queue-id `queueID` \
--job-id `jobID` \
--step-id `stepID` \
--task-id `taskID` \
--target-task-run-status `SUCCEEDED` | `SUSPENDED` | `CANCELED` | `FAILED` | `PENDING`
```
