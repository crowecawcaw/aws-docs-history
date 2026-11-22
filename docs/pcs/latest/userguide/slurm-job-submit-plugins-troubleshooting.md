

# Troubleshooting Slurm Job Submit Plugin issues in AWS PCS

Use this troubleshooting information to resolve common Job Submit Plugin issues.

**Cluster creation or update fails because AWS PCS can't read the script**  
**Symptoms:** `CreateCluster` or `UpdateCluster` fails with an error that says the script doesn't exist or AWS PCS can't access it.  
**Possible causes:**  
+ Incorrect Amazon S3 URI or `s3VersionId`
+ Script object doesn't exist
+ IAM identity that calls the API lacks permission to read the script
+ Bucket policy, IAM policy, or service control policy denies the request
**Resolution:**  
+ Verify the script exists at the Amazon S3 URI, using the same identity that calls AWS PCS
+ Verify the identity has the permissions in [Minimum permissions to use Job Submit Plugins](security-min-permissions.md#security-min-permissions_job-submit-plugins)
+ Check that no policy denies the request, including policies that require requests to come from a VPC

**Cluster creation or update fails because of the Slurm version**  
**Symptoms:** `CreateCluster` or `UpdateCluster` fails with a `ValidationException` and the message `slurmConfiguration parameter jobSubmitPlugins is only supported for Slurm version 25.11 or later.`  
**Possible causes:**  
+ Cluster uses a Slurm version earlier than 25.11
**Resolution:**  
+ Use Slurm version 25.11 or later. For more information, see [Slurm versions in AWS PCS](slurm-versions.md).

**Cluster creation or update fails with Job Submit Plugin validation error**  
**Symptoms:** The cluster status changes to `CREATE_FAILED` or `UPDATE_FAILED` with an error about the script.  
**Possible causes:**  
+ Script doesn't match the `checksum` that you specified
+ Script is larger than 1 MB
**Resolution:**  
+ Calculate the SHA-256 checksum of the object in Amazon S3 and update `checksum`
+ Reduce the size of the script

**Job Submit Plugin script change doesn't take effect**  
**Symptoms:** You uploaded a new script and updated the cluster, but jobs still behave as before.  
**Possible causes:**  
+ Script overwritten at the same Amazon S3 location without a change to `jobSubmitPlugins`
**Resolution:**  
+ Update the cluster with a new `scriptLocation`, `s3VersionId`, or `checksum`

**Job Submit Plugin script runs but jobs are rejected unexpectedly**  
**Symptoms:** Some or all job submissions fail with `Unspecified error`, and users see no other message.  
**Possible causes:**  
+ Starlark syntax or runtime errors, or a missing required function
+ Script exceeded a run time or memory limit
+ Script changed a read-only field or set a value of the wrong type
+ Script rejected the job without calling `log.user()`
**Resolution:**  
+ Review the `job_submit/json` entries in the Slurm controller log for errors. For more information, see [Scheduler logs in AWS PCS](monitoring_scheduler-logs.md).
+ Fix the script and update the cluster with the corrected version
+ To restore job submission immediately, disable the plugin with `"jobSubmitPlugins": []`

**Job has no memory request after the script runs**  
**Symptoms:** A job that requested memory runs without a memory request.  
**Possible causes:**  
+ Script set `min_mem_per_cpu` and also set `min_mem_per_node` to `None`
**Resolution:**  
+ Set only the memory field that you want. For more information, see [Write the script](slurm-job-submit-plugins-scripts.md#slurm-job-submit-plugins-scripts-write).

**Slurm commands are slow during bursts of job submissions**  
**Symptoms:** Job submissions and commands such as `squeue` and `scancel` are slow when many users submit jobs at once.  
**Possible causes:**  
+ Slow script, because the Slurm controller runs the script for one job at a time
**Resolution:**  
+ Make the script faster
+ Use job arrays instead of many separate job submissions