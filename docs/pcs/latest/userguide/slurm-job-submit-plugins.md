

# Use Slurm Job Submit Plugins to validate and modify jobs in AWS PCS

AWS PCS supports Slurm Job Submit Plugins to run custom Starlark scripts that validate and modify jobs on the Slurm controller. Unlike [Slurm CLI Filter Plugins](slurm-cli-filter-plugins.md), Job Submit Plugins can't be bypassed by users. For detailed information about Job Submit Plugins, see the [job\_submit Plugin API documentation](https://slurm.schedmd.com/job_submit_plugins.html) on the SchedMD website.

**Important**  
CloudFormation support for Job Submit Plugins is coming soon.

## Requirements
<a name="slurm-job-submit-plugins-requirements"></a>

Job Submit Plugins require Slurm version 25.11 or later and a Starlark script stored in Amazon Simple Storage Service (Amazon S3). The AWS Identity and Access Management (IAM) identity that creates or updates the cluster must have permission to read the script. For more information, see [Minimum permissions to use Job Submit Plugins](security-min-permissions.md#security-min-permissions_job-submit-plugins).

## Limitations and considerations
<a name="slurm-job-submit-plugins-limitations"></a>
+ **One plugin per cluster** – You can configure one Job Submit Plugin on a cluster. The plugin applies to all queues in the cluster.
+ **Starlark only** – AWS PCS supports Job Submit Plugins written in Starlark. Lua and C plugins aren't supported. For more information about translating a Lua script, see [Translate a Lua Job Submit Plugin script to Starlark for AWS PCS](slurm-job-submit-plugins-translate.md).
+ **Script limits** – The script can be at most 1 MB. Each run of the script has limits on run time, memory, and log output. If a run exceeds the run time or memory limit, or the script fails, Slurm rejects the job. Log output over the limit is truncated or dropped, and doesn't affect the job. A broken script can reject every job on the cluster, so test your script before you deploy it.
+ **Controller performance** – The Slurm controller runs the script for one job at a time. A slow script delays job submissions and other Slurm commands, such as `squeue` and `scancel`. Keep your script short and fast.

**Note**  
Job Submit Plugins aren't recommended for high-throughput workloads. For more information about high-throughput workloads, see [Slurm Configuration](https://slurm.schedmd.com/high_throughput.html#slurm_config) in the *High Throughput Computing Administration Guide* on the SchedMD website.

**Topics**
+ [Requirements](#slurm-job-submit-plugins-requirements)
+ [Limitations and considerations](#slurm-job-submit-plugins-limitations)
+ [Configure a Slurm Job Submit Plugin on an AWS PCS cluster](slurm-job-submit-plugins-configure.md)
+ [Write a Starlark Job Submit Plugin script for AWS PCS](slurm-job-submit-plugins-scripts.md)
+ [Translate a Lua Job Submit Plugin script to Starlark for AWS PCS](slurm-job-submit-plugins-translate.md)
+ [Frequently asked questions about Slurm Job Submit Plugins in AWS PCS](slurm-job-submit-plugins-faq.md)
+ [Troubleshooting Slurm Job Submit Plugin issues in AWS PCS](slurm-job-submit-plugins-troubleshooting.md)