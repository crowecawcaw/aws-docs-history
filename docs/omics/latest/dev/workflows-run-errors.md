# Run failure reasons

If a run fails, use the [GetRun](../api/API_GetRun.md "../api/API_GetRun.md") API
operation to retrieve the failure reason.

Review the failure reason to help you troubleshoot why the run failed. The following
table lists each failure reason along with a description of the error.

| Failure reason                          | Error description                                                                                                                                                                                                                     |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`ASSUME_ROLE_FAILED`**                | HealthOmics doesn't have permission to assume the role. Specify the HealthOmics<br>principal in the trust relationship for the role.                                                                                                  |
| **`CANNOT_START_CONTAINER_ERROR`**      | Unable to start workflow task: `name`,<br>id: `ID` container using image: `image name`.<br>Make sure that the image is valid<br>and try again.                                                                                        |
| **`CANNOT_START_CONTAINER_SIZE_ERROR`** | Unable to start workflow task: `name`,<br>id: `ID` container using image: `image name`.<br>Make sure that the image size is less than 45 GiB (95 GiB for a GPU instance) and try again.                                               |
| **`ECR_PERMISSION_ERROR`**              | HealthOmics doesn't have permission to access the image URI.<br>Confirm that the Amazon ECR private repository exists and has granted<br>access to the HealthOmics service principal.                                                 |
| **`EXPORT_FAILED`**                     | The export failed. Check that the output bucket exists and the run<br>role has write permission to the bucket.                                                                                                                        |
| **`FILE_SYSTEM_OUT_OF_SPACE`**          | The file system doesn't have enough space. Increase the file system<br>size and run again.                                                                                                                                            |
| **`IMAGE_VERIFICATION_FAILURE`**        | Unable to verify image `image name`. To correct the issue, try pulling the image and then push it to your ECR repository again.                                                                                                       |
| **`IMPORT_FAILED`**                     | The import failed. Check that the input file exists and the run<br>role can access input.                                                                                                                                             |
| **`INACTIVE_OMICS_STORAGE_RESOURCE`**   | The HealthOmics storage URI isn't in ACTIVE state. Activate the read set and try again.<br>To learn more about activating read sets, see<br>[Activating read sets in HealthOmics](activating-read-sets.md "activating-read-sets.md"). |
| **`INPUT_URI_NOT_FOUND`**               | The provided URI does not exist: `uri`. Check that the URI path exists and<br>confirm that the role can access the object.                                                                                                            |
| **`INSTANCE_RESERVATION_FAILED`**       | There isn't enough instance capacity to complete the workflow run.<br>Wait and try the workflow run again.                                                                                                                            |
| **`INVALID_ECR_IMAGE_URI`**             | The Amazon ECR image URI structure isn't valid. Provide a valid URI<br>and try again.                                                                                                                                                 |
| **`INVALID_TASK_RESOURCE_VALUE`**       | The requested GPU, CPU, or memory is either too high for available<br>compute capacity, or is less than the minimum value of 1 for task<br>`ID`.                                                                                      |
| **`INVALID_URI_INPUT`**                 | The URI structure isn't a valid `uri`. Check<br>the URI structure and try again.                                                                                                                                                      |
| **`MODIFIED_INPUT_RESOURCE`**           | The provided URI `uri` was modified after the run started. Retry the run.                                                                                                                                                             |
| **`OUT_OF_MEMORY_ERROR`**               | The workflow task `ID` ran out of memory.<br>Increase the memory value in the workflow definition and try the run<br>again.                                                                                                           |
| **`RUN_TASK_FAILED`**                   | The run failed because the task failed. To debug the task<br>failure, use the \*_GetRunTask_<br>• API operation and<br>the Amazon CloudWatch Logs stream.                                                                             |
| **`RUN_TIMED_OUT`**                     | Run timeout after `number` minutes.                                                                                                                                                                                                   |
| **`SERVICE_ERROR`**                     | There was a transient error in the service. Try the workflow run again.                                                                                                                                                               |
| **`TASK_TIMED_OUT`**                    | Task `id` timed out after `number` seconds.                                                                                                                                                                                           |
| **`UNSUPPORTED_INPUT_SIZE`**            | The total input size is too high. Decrease the input size and try again.                                                                                                                                                              |
| **`WORKFLOW_RUN_FAILED`**               | Workflow run failed. Review the CloudWatch Logs engine log stream: `ID` to debug the failure.                                                                                                                                         |
| **`WORKFLOW_VER_VALIDATION_FAILED`**    | HealthOmics doesn't support requested Nextflow version: `version` --. The latest supported version is `version`.<br>Modify your Nextflow version to a supported version and try again.                                                |
| **`UNSUPPORTED_GPU_INSTANCE_TYPE`**     | The requested instance type is not supported in `Region`. Retry the run with<br>a GPU instance type supported in this Region. Available instance types are `GPU instance<br>types`.                                                   |

## Guidance for unresponsive runs

When developing new workflows, runs or specific tasks could become "stuck" or "hang"
if there are issues with your code, and tasks fail to exit processes properly. This can
be challenging to troubleshoot and catch, as it is normal for tasks to run for extended
periods. To prevent and identify unresponsive runs, follow the suggested best practices
in the following sections.

**Best practices for preventing unresponsive runs**

- Ensure you are closing all the files opened in your task code. Opening too many
  files can ocassionally lead to threading issues within the workflow engines.
- Background processes created by a workflow task should exit when the task exits.
  However, if a background process does not exit cleanly, you must explicitly shut down
  that process in your task code.
- Ensure your processes do not loop without exiting. This can cause an unresponsive
  run, and requires a change to your workflow definition code to resolve.
- Provide appropriate memory and CPU allocation to your tasks. Analyze the
  [CloudWatch logs](monitoring-cloudwatch-logs.md "monitoring-cloudwatch-logs.md")
  or use the [Run Analyzer](workflows-run-optimize.md#workflows-run-analyzer "workflows-run-optimize.md#workflows-run-analyzer")
  on successfully completed runs of your workflow to verify you have optimal compute allocation.
  Use the Run Analyzer `headroom` parameter to include additional headroom,
  ensuring processes have sufficient resources to complete.
  Include at least 5% headroom in allocated memory and CPU, to account for
  background operating system processes.
  - Additionally, increase the instance bandwidth size if the instance requires a higher
    throughput. Amazon EC2 instances with fewer than 16 vCPUs (size 4xl and smaller) can experience throughput bursting. For more information
    on Amazon EC2 instance throughput, see
    [Amazon EC2 available instance bandwidth](../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md#available-instance-bandwidth "../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md#available-instance-bandwidth").

- Ensure you are using the correct file system size for your runs. For unresponsive
  runs that are using static run storage, consider increasing the static run storage
  allocation to enable higher IO throughput and storage capacity on the file system.
  Analyze the run manifest to see the maximum file system storage, use the Run Analyzer
  to determine if the file system allocation needs to be increased.

**Best practices for catching unresponsive runs**

- When developing new workflows, use a run group with the max run time limit set to
  catch runaway code. For instance, if a run should take 1 hour to complete, place it in
  a run group that times out after 2 or 3 hours (or a different time period based on your
  use case) to catch run-away jobs. Also, apply a buffer to account for variance in
  processing times.
- Set up a series of run groups with different maximum runtime limits. For instance,
  you could assign short runs to a run group that terminates the runs after a few hours,
  and a long runs group that terminates runs after a few days, based on your expected
  workflow duration.
- HealthOmics has a default maximum run duration service limit of 604,800 Seconds,
  or 7 days, which is adjustable through a request in the quotas tool. Only request
  a service limit increase of this quota if you have runs that approach a week in
  duration. If you have a mix of short and long runs and are not using run groups,
  consider putting the long-running runs in a separate account with a higher maximum
  run duration service limit.
- Inspect the [CloudWatch logs](monitoring-cloudwatch-logs.md "monitoring-cloudwatch-logs.md")
  for tasks that you suspect could be unresponsive. If a task normally outputs regular
  log statements and has not done so for an extended period, the task is likely stuck
  or frozen.

**What to do if you encounter an unresponsive run**

- Cancel the run to avoid incurring additional costs.
- Inspect the [task logs](monitoring-cloudwatch-logs.md#cloudwatch-logs "monitoring-cloudwatch-logs.md#cloudwatch-logs")
  to check if any processes failed to exit correctly.
- Inspect the [engine logs](monitoring-cloudwatch-logs.md#cloudwatch-logs "monitoring-cloudwatch-logs.md#cloudwatch-logs")
  to identify any abnormal engine behaviors.
- Compare the task and engine logs from the unresponsive run to those of identical,
  successfully completed runs. This can help identify any differences that may have
  caused the unresponsive behavior.
- If you are unable to determine the root cause, raise a [support case](../../../awssupport/latest/user/case-management.md#creating-a-support-case "../../../awssupport/latest/user/case-management.md#creating-a-support-case") and include the following:
  - ARN of the stuck run and ARN of an identical run that completed successfully.
  - Engine logs (available once the run has been cancelled or fails)
  - Task logs for the unresponsive task. We don't require task logs for all tasks in the workflow to troubleshoot.
