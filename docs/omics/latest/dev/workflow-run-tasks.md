# Task lifecycle in a HealthOmics run

A _task_ is a single process within a run. HealthOmics maps each task in your workflow
to an omics computing instance type that best fits the task's required resources. You specify the required resources
in the workflow definition. For more information, See [Compute and memory requirements for HealthOmics tasks](memory-and-compute-tasks.md "memory-and-compute-tasks.md").

HealthOmics provides temporary run storage for the task to use. HealthOmics copies the task input files to the temporary run
storage as read-only files. HealthOmics provides symbolic links so that the task can access the input files from the
working directory. The task has access only to the files that you declare in the workflow definition file.

## Task status values

You can track the progress of a task by monitoring the task status.
When you start a run, HealthOmics sets the task status to **Pending** for each task in the run. When
the task starts and progresses through its lifecycle, HealthOmics updates the status value to reflect its current
progress.

You can retrieve task status using any of the following methods:

- The HealthOmics console
  displays the status of each task in a run on the **Run details** page.
- The **GetRunTask** API operation returns the task status.
- You can monitor task status using EventBridge events. For more information, see [Using EventBridge with AWS HealthOmics](eventbridge.md "eventbridge.md").

You can retrieve the current status of a task using the **GetRunTask** API operation.
The HealthOmics console displays the status for each task in a run on the **Run details** page.

HealthOmics supports the following task status values:

**Pending**

Your task is in the queue, waiting to start. Tasks stay in pending for a brief period before they
start.

- Tasks remain in pending after your account has reached the maximum number of concurrent tasks.
- Tasks remain in pending if the run is part of a run group that has reached any of its resource
  maximum values.
- You can adjust run priorities so that specific queued runs and their tasks start before
  other queued runs. For more information
  about run priority, see [Run priority](creating-run-groups.md#run-priority "creating-run-groups.md#run-priority")

**Starting**

HealthOmics is creating the task and provisioning the resources required for the task, such as the workflow
task node.

**Running**

The task status is Running while HealthOmics is processing the task.

**Stopping**

After completing the task processing and exporting the output data, the task transitions to
Stopping.

- HealthOmics deprovisions the workflow task node.

**Completed**

HealthOmics has finished processing the task and has transferred the output data to the run storage file
system.

**Failed**

HealthOmics encountered an error while processing the task and didn't complete it.

- The task transitions to Stopping status (HealthOmics deprovisions the resources) and then to Failed status.
- If the error is a service error (5XX HTTP status code), and the workflow supports retries for this
  task, HealthOmics attempts to process the task again. HealthOmics assigns a new task ID to the retry.

**Cancelled**

HealthOmics stops the task after a user-initiated request to cancel the run.

- The task transitions to Stopping status (HealthOmics deprovisions the resources) and then to Cancelled status.

## Troubleshooting workflow tasks

The following are best practices and considerations for troubleshooting your tasks.

- Task logs rely on `STDOUT` and `STDERR` being
  produced by the task. If the application used in the task doesn’t produce
  either of these, then there won't be a task log. To assist with debugging,
  use applications in `verbose` mode.
- To view the commands being run in a task along with their interpolated
  values, use the `set -x` Bash command. This can help determine if
  the task is using the correct inputs and identify where errors might have
  kept the task from running as intended.
- Use the `echo` command to output the values of variables to
  `STDOUT` or `STDERR`. This helps you confirm that
  they're being set as expected.
- Use commands like `ls -l` `<name_of_input_file>`
  to confirm that inputs are present and are of the expected size. If they
  aren't, this might reveal a problem with a prior task producing empty
  outputs due to a bug.
- Use the command `df -Ph . | awk 'NR==2 {print $4}'` in a tasks
  script to determine the space currently available to the task and help
  identify situations where you might need to run the workflow with additional
  storage allocation.

Including any of the preceding commands in a task script assumes that the task
container also includes these commands and that they are on the `path` of
the container environment.
