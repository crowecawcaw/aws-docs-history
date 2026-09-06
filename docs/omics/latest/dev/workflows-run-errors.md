

# Run failure reasons
<a name="workflows-run-errors"></a>

If a run fails, use the [GetRun](https://docs.aws.amazon.com/omics/latest/api/API_GetRun.html) API operation to retrieve the failure reason. 

Review the failure reason to help you troubleshoot why the run failed. The following table lists each failure reason along with a description of the error.


| Failure reason | Error description | 
| --- | --- | 
| ASSUME\_ROLE\_FAILED | HealthOmics doesn't have permission to assume the role. Specify the HealthOmics principal in the trust relationship for the role. | 
| CANNOT\_START\_CONTAINER\_ERROR | Unable to start workflow task: {{name}}, id: {{ID}} container using image: {{image name}}. Make sure that the image is valid and try again. | 
| CANNOT\_START\_CONTAINER\_SIZE\_ERROR | Unable to start workflow task: {{name}}, id: {{ID}} container using image: {{image name}}. Make sure that the image size is less than 45 GiB (95 GiB for a GPU instance) and try again. | 
| ECR\_PERMISSION\_ERROR | HealthOmics doesn't have permission to access the image URI. Confirm that the Amazon ECR private repository exists and has granted access to the HealthOmics service principal. | 
| EXPORT\_FAILED | The export failed. Check that the output bucket exists and the run role has write permission to the bucket. | 
| FILE\_SYSTEM\_OUT\_OF\_SPACE | The file system doesn't have enough space. Increase the file system size and run again. | 
| IMAGE\_VERIFICATION\_FAILURE | Unable to verify image {{image name}}. To correct the issue, try pulling the image and then push it to your ECR repository again. | 
| IMPORT\_FAILED | The import failed. Check that the input file exists and the run role can access input. | 
| INACTIVE\_OMICS\_STORAGE\_RESOURCE  | The HealthOmics storage URI isn't in ACTIVE state. Activate the read set and try again. To learn more about activating read sets, see [Activating read sets in HealthOmics](activating-read-sets.md). | 
| INPUT\_URI\_NOT\_FOUND | The provided URI does not exist: {{uri}}. Check that the URI path exists and confirm that the role can access the object. | 
| INSTANCE\_RESERVATION\_FAILED | There isn't enough instance capacity to complete the workflow run. Wait and try the workflow run again. | 
| INVALID\_ECR\_IMAGE\_URI | The Amazon ECR image URI structure isn't valid. Provide a valid URI and try again. | 
| INVALID\_TASK\_RESOURCE\_VALUE | The requested GPU, CPU, or memory is either too high for available compute capacity, or is less than the minimum value of 1 for task {{ID}}. | 
| INVALID\_URI\_INPUT | The URI structure isn't a valid {{uri}}. Check the URI structure and try again. | 
|  MODIFIED\_INPUT\_RESOURCE  | The provided URI {{uri}} was modified after the run started. Retry the run. | 
| OUT\_OF\_MEMORY\_ERROR | The workflow task {{ID}} ran out of memory. Increase the memory value in the workflow definition and try the run again.  | 
| RUN\_TASK\_FAILED | The run failed because the task failed. To debug the task failure, use the **GetRunTask** API operation and the Amazon CloudWatch Logs stream. | 
| RUN\_TIMED\_OUT | Run timeout after {{number}} minutes. | 
|  SERVICE\_ERROR  | There was a transient error in the service. Try the workflow run again. | 
| TASK\_TIMED\_OUT | Task {{id}} timed out after {{number}} seconds. | 
| UNSUPPORTED\_INPUT\_SIZE | The total input size is too high. Decrease the input size and try again. | 
| WORKFLOW\_RUN\_FAILED | Workflow run failed. Review the CloudWatch Logs engine log stream: {{ID}} to debug the failure. | 
| WORKFLOW\_VER\_VALIDATION\_FAILED | HealthOmics doesn't support requested Nextflow version: {{version}} --. The latest supported version is {{version}}. Modify your Nextflow version to a supported version and try again. | 
| UNSUPPORTED\_GPU\_INSTANCE\_TYPE | The requested instance type is not supported in {{Region}}. Retry the run with a GPU instance type supported in this Region. Available instance types are {{GPU instance types}}. | 

## Guidance for unresponsive runs
<a name="workflows-guidance-unresponsive-runs"></a>

When developing new workflows, runs or specific tasks could become "stuck" or "hang" if there are issues with your code, and tasks fail to exit processes properly. This can be challenging to troubleshoot and catch, as it is normal for tasks to run for extended periods. To prevent and identify unresponsive runs, follow the suggested best practices in the following sections.

**Best practices for preventing unresponsive runs**
+ Ensure you are closing all the files opened in your task code. Opening too many files can ocassionally lead to threading issues within the workflow engines.
+ Background processes created by a workflow task should exit when the task exits. However, if a background process does not exit cleanly, you must explicitly shut down that process in your task code.
+ Ensure your processes do not loop without exiting. This can cause an unresponsive run, and requires a change to your workflow definition code to resolve.
+ Provide appropriate memory and CPU allocation to your tasks. Analyze the [CloudWatch logs](https://docs.aws.amazon.com/omics/latest/dev/monitoring-cloudwatch-logs.html) or use the [Run Analyzer](workflows-run-optimize.md#workflows-run-analyzer) on successfully completed runs of your workflow to verify you have optimal compute allocation. Use the Run Analyzer `headroom` parameter to include additional headroom, ensuring processes have sufficient resources to complete. Include at least 5% headroom in allocated memory and CPU, to account for background operating system processes.
  + Additionally, increase the instance bandwidth size if the instance requires a higher throughput. Amazon EC2 instances with fewer than 16 vCPUs (size 4xl and smaller) can experience throughput bursting. For more information on Amazon EC2 instance throughput, see [Amazon EC2 available instance bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html#available-instance-bandwidth).
+ Ensure you are using the correct file system size for your runs. For unresponsive runs that are using static run storage, consider increasing the static run storage allocation to enable higher IO throughput and storage capacity on the file system. Analyze the run manifest to see the maximum file system storage, use the Run Analyzer to determine if the file system allocation needs to be increased.

**Best practices for catching unresponsive runs**
+ When developing new workflows, use a run group with the max run time limit set to catch runaway code. For instance, if a run should take 1 hour to complete, place it in a run group that times out after 2 or 3 hours (or a different time period based on your use case) to catch run-away jobs. Also, apply a buffer to account for variance in processing times.
+ Set up a series of run groups with different maximum runtime limits. For instance, you could assign short runs to a run group that terminates the runs after a few hours, and a long runs group that terminates runs after a few days, based on your expected workflow duration.
+ HealthOmics has a default maximum run duration service limit of 604,800 Seconds, or 7 days, which is adjustable through a request in the quotas tool. Only request a service limit increase of this quota if you have runs that approach a week in duration. If you have a mix of short and long runs and are not using run groups, consider putting the long-running runs in a separate account with a higher maximum run duration service limit.
+ Inspect the [CloudWatch logs](https://docs.aws.amazon.com/omics/latest/dev/monitoring-cloudwatch-logs.html) for tasks that you suspect could be unresponsive. If a task normally outputs regular log statements and has not done so for an extended period, the task is likely stuck or frozen.

**What to do if you encounter an unresponsive run**
+ Cancel the run to avoid incurring additional costs.
+ Inspect the [task logs](https://docs.aws.amazon.com/omics/latest/dev/monitoring-cloudwatch-logs.html#cloudwatch-logs) to check if any processes failed to exit correctly.
+ Inspect the [engine logs](https://docs.aws.amazon.com/omics/latest/dev/monitoring-cloudwatch-logs.html#cloudwatch-logs) to identify any abnormal engine behaviors.
+ Compare the task and engine logs from the unresponsive run to those of identical, successfully completed runs. This can help identify any differences that may have caused the unresponsive behavior.
+ If you are unable to determine the root cause, raise a [support case](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html#creating-a-support-case) and include the following:
  + ARN of the stuck run and ARN of an identical run that completed successfully.
  + Engine logs (available once the run has been cancelled or fails)
  + Task logs for the unresponsive task. We don't require task logs for all tasks in the workflow to troubleshoot.