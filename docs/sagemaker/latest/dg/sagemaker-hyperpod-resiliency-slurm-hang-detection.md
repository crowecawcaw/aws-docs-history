

# Hung job detection

A training job can hang without exiting, for example because of an NVIDIA Collective Communications Library (NCCL) timeout, a data pipeline stall, or a process deadlock. The job keeps its GPUs but makes no progress. Hung job detection finds these jobs and writes an event to Amazon CloudWatch, and can optionally cancel the job.

Hung job detection runs as an agent on each node of a SageMaker HyperPod Slurm cluster. It's off by default and you turn it on for each job with the `HYPERPOD_HANG_RULES` environment variable. It needs no changes to your training scripts or containers, and works with PyTorch, TensorFlow, JAX, and custom scripts.

**Important**  
To use hung job detection on an existing cluster, you must update the cluster software to the latest AMI. Otherwise, hung job detection isn't available on that cluster. For more information, see [Update the SageMaker HyperPod platform software of a cluster](sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software).

## Turning on hung job detection for a job
<a name="sagemaker-hyperpod-resiliency-slurm-hang-detection-turn-on"></a>

The rules file must be readable from every compute node in the job. For multi-node jobs, use shared storage such as Amazon FSx for Lustre.

**To turn on hung job detection**

1. Create a rules file that turns on hung job detection.

   ```sh
   echo '{"enabled": true}' > /fsx/my-project/rules.json
   ```

1. When you submit the job, set the `HYPERPOD_HANG_RULES` environment variable to the path of the rules file.

   ```sh
   #SBATCH --export=ALL,HYPERPOD_HANG_RULES=/fsx/my-project/rules.json
   ```

With this file, the agent uses default detection, which watches the job's output and GPU activity, and only writes an event when it finds a hang. For details, see [How hung job detection works](#sagemaker-hyperpod-resiliency-slurm-hang-detection-how). To add your own rules or cancel hung jobs, see [Configuring custom detection rules](#sagemaker-hyperpod-resiliency-slurm-hang-detection-rules).

## How hung job detection works
<a name="sagemaker-hyperpod-resiliency-slurm-hang-detection-how"></a>

A job that doesn't set `HYPERPOD_HANG_RULES` isn't monitored.

If the rules file has no enabled `log_pattern` rules, the agent uses *default detection*. It declares a job hung when either of the following is true:
+ Job output (stdout) has stopped for an extended period while the GPUs are idle but still hold memory. This catches rendezvous hangs, where one node fails and the others wait at a barrier.
+ Job output has stopped for a longer period, regardless of GPU state.

If the rules file has `log_pattern` rules, the agent watches your log file for those patterns instead. A job is hung when a pattern stops matching for its timeout, or immediately when a `fault_on_match` pattern appears.

**Important**  
Custom rules replace default detection for that job. If your patterns keep matching, the agent doesn't declare a hang even when the GPUs are idle.

Hung job detection is independent of auto-resume, which restarts jobs that exit after a hardware failure. For more information about auto-resume, see [Automatic node recovery and auto-resume](sagemaker-hyperpod-resiliency-slurm-auto-resume.md).

## Viewing detection events
<a name="sagemaker-hyperpod-resiliency-slurm-hang-detection-events"></a>

HyperPod writes detection events from the controller node to your cluster's CloudWatch log group:
+ Log group: `/aws/sagemaker/Clusters/{{cluster-name}}/{{cluster-id}}`
+ Log stream: `SageMakerHangJobDetectionEvents/{{controller-instance-group-name}}/{{controller-instance-id}}`

Events for every job are written to this stream, whichever node the job ran on. Each event's `node` field shows the Slurm node where the hang was detected. To find the events for a job, filter the log group by its job ID:

```sh
aws logs filter-log-events \
  --log-group-name /aws/sagemaker/Clusters/{{cluster-name}}/{{cluster-id}} \
  --log-stream-name-prefix SageMakerHangJobDetectionEvents/ \
  --filter-pattern '{ $.job_id = "{{12345}}" }'
```

The following is an example `HANG_DETECTED` event.

```json
{
  "event_type": "HANG_DETECTED",
  "job_id": "12345",
  "step_id": "0",
  "node": "ip-172-22-230-3",
  "evidence": "stdout stale for 18 min and GPU idle with memory allocated",
  "layer": "signal_evaluator",
  "detected_at": "2026-04-22T00:58:47Z",
  "job_action": "notify",
  "config_source": "per_job_env_var"
}
```

The `layer` field shows what fired: `signal_evaluator` for default detection or `pattern_evaluator` for your rules. `job_action` is `notify` or `cancel`.

The log stream can also contain the following events:
+ `HANG_ACTION_TAKEN`: the agent cancelled the job. The `action` field shows what Slurm did. By default, Slurm requeues jobs on SageMaker HyperPod Slurm clusters, so a cancel usually reports `requeue`.
+ `CONFIG_ERROR`: if the rules file is missing or invalid, the agent doesn't monitor the job. If a pattern doesn't compile, the agent skips that rule. The event includes the file path and the error. This error doesn't appear in `sbatch`, `squeue`, `sacct`, or the job's output, so test a new rules file with a short job and check the log stream before you use it for production jobs.

## Configuring custom detection rules
<a name="sagemaker-hyperpod-resiliency-slurm-hang-detection-rules"></a>

We recommend that you add at least one `log_pattern` rule that tracks your training progress, such as steps or epochs. Default detection can't catch a job that keeps its GPUs busy without making progress.

A rules file is a JSON file. The following example watches for epoch completion and cancels the job if no epoch completes within 45 minutes, or as soon as an NCCL error appears.

```json
{
  "enabled": true,
  "rules": [
    {
      "name": "epoch_progress",
      "type": "log_pattern",
      "enabled": true,
      "log_pattern": "Epoch \\d+/\\d+ complete",
      "timeout_minutes": 45
    },
    {
      "name": "nccl_error",
      "type": "log_pattern",
      "enabled": true,
      "log_pattern": "NCCL error|NCCL WARN",
      "fault_on_match": true
    }
  ],
  "action_policy": {
    "action": "cancel"
  }
}
```

The following table describes the fields in a rules file.


**Rules file fields**  

| Field | Required | Description | 
| --- | --- | --- | 
| enabled | Yes | Set to true to turn on detection for jobs that use this file. If it's false or missing, those jobs aren't monitored. | 
| monitoring.log\_file | No | Log file to watch. Defaults to the job's Slurm output file (the --output file, or slurm-{{job-id}}.out). | 
| rules | No | Up to 20 rules. Enabled log\_pattern rules replace default detection. | 
| action\_policy.action | No | notify (default) writes an event only. cancel also cancels the job. Slurm requeues cancelled jobs by default; to stop the job instead, submit it with \#SBATCH --no-requeue. | 

The following table describes the fields in each rule.


**Rule fields**  

| Field | Required | Description | 
| --- | --- | --- | 
| name | Yes | Rule name, shown in events. | 
| type | Yes | log\_pattern. This is the only rule type the agent evaluates. | 
| enabled | No | Defaults to false. Set to true to use the rule. | 
| log\_pattern | Yes | RE2 regular expression, up to 256 characters. | 
| timeout\_minutes | Yes, unless fault\_on\_match is true | How long the pattern can go unmatched before the job is hung. | 
| fault\_on\_match | No | If true, a match means the job is hung. Use for error patterns. | 
| stop\_pattern | No | A pattern that turns off the rule when it matches, for example Training complete. | 
| start\_timeout\_minutes | No | Maximum time from job start to the first match. Catches jobs that hang during startup. | 
| metric\_evaluation\_data\_points | No | Number of consecutive 10-second checks that must fail before the job is hung. Default is 1. Raise it to reduce false positives. | 

To apply one rules file to many jobs, set `HYPERPOD_HANG_RULES` in your batch script, your shell profile, or a site-wide profile script. If you aren't sure how `sbatch` propagates your environment, set the variable on the `#SBATCH --export` line.

To make sure a change to a rules file takes effect, cancel the job and submit it again.

## Turning off hung job detection
<a name="sagemaker-hyperpod-resiliency-slurm-hang-detection-turn-off"></a>

A job that doesn't set `HYPERPOD_HANG_RULES` isn't monitored. To turn off detection in other cases, do one of the following:
+ For one job, add `--no-hang-detection` to `srun`, or to `sbatch` to cover all steps in the job.

  ```sh
  srun --no-hang-detection python train.py
  ```
+ For all jobs that use a rules file, set `"enabled": false` in the file.

## Securing rules files
<a name="sagemaker-hyperpod-resiliency-slurm-hang-detection-security"></a>

The agent applies the rules file that a job points to. It doesn't check who owns the file or who can change it. Anyone who can write to the file, or replace it in its directory, can change detection for every job that uses it, including making the agent cancel those jobs.

Keep each rules file, and the directory that contains it, writable only by its owner. For a rules file that a team shares, let the team read it and let only the person who maintains it write to it.

```sh
# Rules file for your own jobs
chmod 600 /fsx/my-project/rules.json

# Shared rules file: others can read, only the owner can write
chmod 644 /fsx/team/rules.json
ls -l /fsx/team/rules.json
```

## Limitations
<a name="sagemaker-hyperpod-resiliency-slurm-hang-detection-limitations"></a>
+ Default detection doesn't catch a job that keeps its GPUs busy without making progress, such as a job stuck in a loop. To catch these, we recommend that you always add a `log_pattern` rule that tracks steps or epochs.
+ Default detection waits for a sustained period of inactivity, so detection isn't immediate. Shorter custom timeouts detect faster but can flag normal pauses such as checkpoint saves.
+ Patterns use RE2 syntax. A pattern that uses backreferences or lookaround doesn't compile, and the agent skips that rule.
+ A rules file can have up to 20 rules and can be up to 1 MB. A file over either limit is rejected and the job isn't monitored.