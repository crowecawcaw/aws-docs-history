

# Monitoring Deadline Cloud jobs
<a name="jobs-monitoring"></a>

Use the AWS Deadline Cloud monitor to get an overall view of your jobs, including:
+ Monitor and manage jobs
+ View worker activity on fleets
+ Track budgets and usage
+ Download a job's results

To monitor a specific job, select the farm and queue containing the job, then select the job from the list. You can use the search box to locate a specific job or jobs in the queue.

![The job monitor for a queue showing a jobs table with progress, status, duration, and priority, and step and task panels.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/monitor/queue-jobs.png)


Open the context menu for a job, step, or task. You can:
+ Change the status
+ Suspend and resume the item
+ Requeue the item
+ Download the output
+ For jobs: Modify job properties like the name, description, priority, or max worker count
+ For tasks: View task and worker logs

For more information, see [Using the Deadline Cloud monitor](working-with-deadline-monitor.md). To modify a job with the AWS Command Line Interface (AWS CLI) or the Deadline Cloud API, see [Modify a job in Deadline Cloud](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-jobs-modifying.html) in the *Deadline Cloud Developer Guide*.

If your team uses automatic downloads, the jobs and tasks tables in the Deadline Cloud monitor desktop application also show a **Download status** column that reports whether each job's outputs reached your file system. For more information, see [View output download status in Deadline Cloud](auto-downloads-status.md).

Each task in a job or step has a status, and the job or step shows a status based on its tasks. A job shows the first status in the following list that any of its tasks has. For example, a job with some `READY` tasks and some `SUSPENDED` tasks shows `READY`. A job is `SUCCEEDED` only when all of its tasks succeeded. Steps work the same way.

The following list describes the statuses:

`NOT_COMPATIBLE`  
The job is not compatible with the farm because there are no fleets that can complete one of the tasks in the job. 

`RUNNING`  
One or more workers are running tasks from the job. As long as there is at least one running task, the job is marked `RUNNING`.

`ASSIGNED`  
One or more workers are assigned tasks in the job as their next action. The environment, if any, is set up. 

`STARTING`  
One or more workers are setting up the environment for running tasks.

`SCHEDULED`  
Tasks for the job are scheduled on one or more workers as the worker's next action.

`READY`  
At least one task for the job is ready to be processed.

`INTERRUPTING`  
A running task in the job is stopping because you changed the status of the job, step, or task. This status is always temporary. When the task stops, it moves to the status that you requested, such as `CANCELED`, `SUSPENDED`, or `READY`.  
When a worker stops unexpectedly, for example when Amazon Elastic Compute Cloud (Amazon EC2) reclaims a Spot Instance, its tasks return to `READY` so that another worker can run them.

`FAILED`  
One or more tasks in the job didn't complete successfully.

`CANCELED`  
Tasks in the job were canceled and won't run. Cancel a job when you don't intend to run the work. Canceling a task also cancels the steps that depend on it. You can't submit a job as canceled. To run canceled tasks again, requeue the job.

`SUSPENDED`  
Tasks in the job are paused and won't run until you requeue the job. Suspend a job when you plan to come back to it later. Deadline Cloud doesn't suspend jobs on its own. A job is suspended only when you submit it as suspended or suspend it after it's in the queue. Suspending a job doesn't change tasks that already succeeded, failed, or were canceled.

`PENDING`  
A task in the job is waiting on the availability of another resource.

`SUCCEEDED`  
All tasks in the job were successfully processed.