# Run lifecycle in a HealthOmics workflow

You can track the progress of a run by monitoring the run status. HealthOmics updates the run status as a run proceeds
through its lifecycle.

You can retrieve run status using any of the following methods:

- The HealthOmics console
  displays the status of each run on the **Runs** page.
- The **GetRun** API operation returns the current run status.
- You can monitor run status using EventBridge events. For more information, see [Using EventBridge with AWS HealthOmics](eventbridge.md "eventbridge.md").

###### Topics

- [Run status values](#run-status-values "#run-status-values")
- [Task Retries](#run-status-task-retries "#run-status-task-retries")
- [Pricing implications of run status](#run-status-billing "#run-status-billing")

## Run status values

When you start a run, HealthOmics sets the run status to **Pending**. As the run proceeds through its
lifecycle, HealthOmics updates the status value to reflect its current progress.

###### Note

You don't incur charges during any run status other than Running. See the next section for details.

HealthOmics supports the following run status values:

**Pending**

The run is in the queue, waiting to start. Runs typically remain in Pending for a brief period before
they start.

- Runs can remain in Pending for a longer time if you submit many jobs at the same time.
- Runs remain in Pending after your account reaches the maximum number of concurrent runs.
- A run remains in Pending if the run is part of a run group that has reached any of its resource
  maximum values.
- You can adjust run priorities so that specific queued runs start before others. For more information
  about run priority, see [Run priority](creating-run-groups.md#run-priority "creating-run-groups.md#run-priority").

**Starting**

HealthOmics creates the run and provisions the resources required for the run (such as temporary run storage
and the engine node).

- HealthOmics provisions temporary run storage at the start of the run, and deprovisions the run storage when
  the run is Stopping.

**Running**

A run remains in Running status during the import process, the processing of each task, and the export
process.

- HealthOmics imports the input files to the temporary run storage file system. The input files are
  read-only, to prevent tasks from modifying the inputs to other tasks in a workflow.
- During file export, HealthOmics exports the output files from the run storage file system to the S3
  location.
- HealthOmics delivers the run logs and task logs to CloudWatch in real time while the run status is Running.
  For more information, see [Logs in CloudWatch](monitoring-cloudwatch-logs.md#cloudwatch-logs "monitoring-cloudwatch-logs.md#cloudwatch-logs") .

**Stopping**

After completion of the export process, the run transitions to the Stopping status.

- HealthOmics deprovisions all resources (including the run storage file system and the engine node).

**Completed**

The run transitions to Completed after HealthOmics completes the resource deprovisioning.

- HealthOmics has completed all run tasks and exported the output data without error.
- The run outputs are available in the specified Amazon S3 URI output location. For WDL and CWL, HealthOmics
  generates a run output summary file, which provides information about the [HealthOmics run outputs](workflows-run-outputs.md "workflows-run-outputs.md").
- The final run manifest logs and engine logs (if applicable) are available in CloudWatch.
- For runs that support task retries, a run with Completed status can include one or more tasks that
  failed. As long as a task retry succeeded for each failed task, HealthOmics transitions the run to Completed. HealthOmics assigns a new
  task ID to each retry, so the run includes task IDs for the failed attempts and the completed attempt.

**Failed**

HealthOmics encountered one or more errors and failed to complete all the run tasks.

- A failed run transitions through Stopping status while HealthOmics deprovisions the resources.

**Cancelled**

A user initiated a request to cancel the run.

- HealthOmics stops any running tasks and deprovisions all resources.
- HealthOmics doesn't export any run output data when a user cancels a run. You don't have access to any
  intermediate files for a cancelled run.
- Your account incurs charges for the tasks and resources that the run consumed during Running status
  before the cancellation.
- There are no charges if you cancel a run in Pending or Starting status.

## Task Retries

HealthOmics supports task retries for tasks that fail because of service errors (5XX HTTP status codes).

If every task in the run eventually completes, even if they required retries, HealthOmics transitions the run to
Completed. HealthOmics assigns a new task ID to each retry, so the run includes task IDs for the failed attempts and the
completed attempt.

The default retry behavior depends on which definition language the workflow uses. The default for Nextflow is no retries.
For WDL and CWL, HealthOmics attempts up to two retries of a failed task, but you can opt out of task retry for specific tasks
or for all tasks in a workflow. Task retry is useful to address intermittent service errors.
However, you might consider opting out a task that is idempotent.

For specific information about each workflow definition language, see the following topics:

- WDL – Configure task retry behavior in the workflow definition.
  See [Configure WDL task retry behavior](workflow-languages-wdl.md#workflow-wdl-task-retry "workflow-languages-wdl.md#workflow-wdl-task-retry").
- Nextflow – Configure task retry behavior in the Nextflow config file or the workflow definition.
  See [Configure Nextflow task retry behavior](workflow-definition-nextflow.md#workflow-nextflow-retry-5xx "workflow-definition-nextflow.md#workflow-nextflow-retry-5xx").
- CWL – Configure task retry behavior in the workflow definition.
  See [Configure CWL task retry behavior](workflow-languages-cwl.md#workflow-cwl-retry-5xx "workflow-languages-cwl.md#workflow-cwl-retry-5xx").

## Pricing implications of run status

Your account can incur charges while the run status is Running. You don't incur charges during any other run
status. For example, there is no charge for resources when the run is Starting or Stopping.

A run with Running status has the following billing implications:

- Your account incurs charges for run storage file-system usage while the run status is Running.
  For information about the run storage types,
  See [Run storage types in HealthOmics workflows](workflows-run-types.md "workflows-run-types.md").
- Your account incurs charges for running tasks, based on the compute and memory resources that you
  specified for each task in the workflow definition, and based on the task duration. For more information,
  see [Compute and memory requirements for HealthOmics tasks](memory-and-compute-tasks.md "memory-and-compute-tasks.md").
- Each task has a minimum billing threshold of one minute. If you run a task for less than a minute, you incur a
  charge for the minimum one minute of usage. If possible, group small tasks together to optimize costs.
  Grouping tasks also reduces run time by avoiding the spin-up of multiple sequential tasks.

For additional information about
HealthOmics pricing, see the [HealthOmics Pricing](https://aws.amazon.com/healthomics/pricing/ "https://aws.amazon.com/healthomics/pricing/").
