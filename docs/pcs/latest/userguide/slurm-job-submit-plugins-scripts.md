

# Write a Starlark Job Submit Plugin script for AWS PCS

Write a Job Submit Plugin script in Starlark to enforce your job policies on the Slurm controller. This topic covers the functions, modules, and job fields that AWS PCS provides to your script. For the Starlark language, see the [Starlark specification](https://github.com/bazelbuild/starlark/blob/master/spec.md) on the GitHub website.

## Prerequisites
<a name="slurm-job-submit-plugins-scripts-prerequisites"></a>

Before you write your script, complete these tasks:
+ Identify the job policies that you want to enforce, such as required accounts, time limits, or default memory
+ Create a non-production AWS PCS cluster that uses Slurm 25.11 or later, for testing

## Write the script
<a name="slurm-job-submit-plugins-scripts-write"></a>

**To write a Job Submit Plugin script**

1. Create a `.star` file that defines the `slurm_job_submit` and `slurm_job_modify` functions.

1. Add your policy logic. Read and change job fields in `job_desc`.

1. Call `log.user()` to tell users why you rejected their job.

1. Return `slurm.ACCEPT_JOB` or `slurm.REJECT_JOB` from each function.

1. Test the script on your non-production cluster. For each rule, submit a job that the script must accept and a job that it must reject. For more information, see [Configure a Slurm Job Submit Plugin on an AWS PCS cluster](slurm-job-submit-plugins-configure.md).

**Functions**


| Function | When it runs | 
| --- | --- | 
| slurm\_job\_submit(job\_desc, part\_list, submit\_uid) | A user submits a job with sbatch, salloc, or srun. | 
| slurm\_job\_modify(job\_desc, job\_rec, part\_list, modify\_uid) | A user modifies a job, for example with scontrol update job. | 

**Arguments**


| Argument | Description | 
| --- | --- | 
| job\_desc | The job request. To modify the job, change values in this dictionary. | 
| job\_rec | The existing job. Job details are in job\_rec["details"]. Read-only. | 
| part\_list | The Slurm partitions (AWS PCS queues). Read-only. | 
| submit\_uid, modify\_uid | The Linux user ID of the user who runs the command. | 

**Modules**


| Module | Use | 
| --- | --- | 
| log | log.user() shows a message to the user. log.info(), log.verbose(), log.debug(), and log.error() write to the Slurm controller log. | 
| slurm | Constants, such as ACCEPT\_JOB, REJECT\_JOB, NO\_VAL, and INFINITE. | 
| math | Math functions and constants, such as math.ceil(), math.floor(), math.round(), math.sqrt(), math.pow(), math.log(), math.pi, and math.e. | 

**Important**  
Don't use `print()`. Slurm discards its output, so it doesn't reach the user or the controller log. Use the `log` module instead.

**Job fields**

The keys of `job_desc` match the fields of the Slurm `job_desc_msg_t` structure, for example `account`, `partition`, `qos`, and `time_limit`. For more information about the available job fields, see [Job Submit Plugin API](https://slurm.schedmd.com/job_submit_plugins.html#attr) on the SchedMD website.


| Behavior | What to do | 
| --- | --- | 
| Read-only fields | Don't change fields such as user\_id or group\_id, and don't add keys that aren't job fields. Slurm rejects the job. | 
| Numbers are floats | Numeric fields arrive as values such as 60.0. When you set an integer field, use a whole number. If you set a fractional number, such as 60.5, Slurm rejects the job. | 
| Unset values | Unset string fields, min\_mem\_per\_cpu, min\_mem\_per\_node, and site\_factor are None. Other unset numeric fields use values such as slurm.NO\_VAL. To clear a field, set it to its unset value. Comparisons with slurm.NO\_VAL64 or slurm.INFINITE64 are never true, so check min\_mem\_per\_cpu and min\_mem\_per\_node with None instead. | 

**Important**  
The fields `min_mem_per_cpu` and `min_mem_per_node` set the same memory request. Set only the memory field that you want, and don't set the other field to `None`. Don't use `pn_min_memory`. Use `min_mem_per_cpu` or `min_mem_per_node` instead.  
For example, to change a `--mem` job to a per-CPU request, set only `job_desc["min_mem_per_cpu"] = 1024`. If you also set `job_desc["min_mem_per_node"] = None`, the job has no memory request.

## Example script
<a name="slurm-job-submit-plugins-scripts-examples"></a>

The following script rejects jobs that don't request a time limit, and accepts all job modifications.

```python
def slurm_job_submit(job_desc, part_list, submit_uid):
    if job_desc["time_limit"] == slurm.NO_VAL:
        log.user("Specify a time limit with --time.")
        return slurm.REJECT_JOB
    return slurm.ACCEPT_JOB

def slurm_job_modify(job_desc, job_rec, part_list, modify_uid):
    return slurm.ACCEPT_JOB
```

## Expected results
<a name="slurm-job-submit-plugins-scripts-results"></a>

After you write your script:
+ Your script defines `slurm_job_submit` and `slurm_job_modify`
+ Jobs that follow your policies are accepted, with any changes your script makes
+ Jobs that don't follow your policies are rejected with your custom error messages

## Troubleshooting
<a name="slurm-job-submit-plugins-scripts-troubleshooting"></a>

**Jobs are rejected without a message**  
**Symptoms:** Job submissions fail with `Unspecified error`.  
**Likely cause:** The script failed, changed a read-only field, or exceeded a run time or memory limit.  
**Resolution:** Check the `job_submit/json` entries in the Slurm controller log, and fix the error. Call `log.user()` before you return `slurm.REJECT_JOB`.

**Job has no memory request after the script runs**  
**Symptoms:** A job that requested memory runs without a memory request.  
**Likely cause:** The script set `min_mem_per_cpu` and also set `min_mem_per_node` to `None`.  
**Resolution:** Set only the memory field that you want.

**Messages don't appear**  
**Symptoms:** Messages from your script don't reach the user or the controller log.  
**Likely cause:** Your script uses `print()`, or it writes more messages than the limit allows.  
**Resolution:** Use the `log` module and write fewer messages.

**Script log messages are truncated**  
**Symptoms:** A message from your script ends with `... [truncated]`.  
**Likely cause:** The message is longer than the limit allows.  
**Resolution:** Shorten the message.

For more troubleshooting information, see [Troubleshooting Slurm Job Submit Plugin issues in AWS PCS](slurm-job-submit-plugins-troubleshooting.md).