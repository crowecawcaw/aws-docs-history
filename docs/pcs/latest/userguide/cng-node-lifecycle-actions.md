

# Run custom scripts with node lifecycle actions in AWS PCS
<a name="cng-node-lifecycle-actions"></a>

Node lifecycle actions run custom scripts at defined points in a compute node's lifecycle. Use them to mount file systems, join directory services, install software, or set up monitoring. You define scripts in the compute node group configuration and reuse them across compute node groups and clusters.

A node lifecycle action is a script that AWS PCS runs automatically at a specific point in a compute node's lifecycle. You define scripts in your compute node group configuration: where each script lives (Amazon S3 or HTTPS), what arguments to pass, the stage at which it runs, when it re-runs on reboot, and what to do if it fails. AWS PCS retrieves the script, caches it on the instance, runs it as `root`, and writes its output to a dedicated log file.

Node lifecycle actions provide:
+ **Reusability** — Reference the same script from many compute node groups with different arguments.
+ **Per-script error handling** — Terminate the node, stop the sequence, or continue on a failure.
+ **API-native configuration** — Define and update lifecycle actions through `UpdateComputeNodeGroup`. Configuration changes drain and replace existing nodes. For more information, see [Configure node lifecycle actions in AWS PCS](cng-node-lifecycle-actions-configure.md).

## Lifecycle stages
<a name="cng-node-lifecycle-actions-stages"></a>

AWS PCS currently supports two stages. Within each stage, scripts run **in the order you define them**. By default, a script runs only on **first boot**; set its `executionPolicy` to `EVERY_BOOT` to also re-run it on reboot. For more information, see [Configure node lifecycle actions in AWS PCS](cng-node-lifecycle-actions-configure.md).


| **Stage** | **When it runs** | **Services available** | **Typical use** | 
| --- | --- | --- | --- | 
| **Node bootstrapped** (`nodeBootstrapped`) | Runs after AWS PCS finishes node setup and before `slurmd` starts. | Network and Amazon S3 are up, and SSH, SSM, NTP (chrony), and cron are active for debugging. AWS PCS-managed setup is done (Slurm configured, Hyper-Threading disabled), so you can rely on it. Slurm client commands are **not** yet available. | Tasks that must complete before the node accepts jobs, such as mounting shared storage, configuring networking, or installing software packages. | 
| **Node ready** (`nodeReady`) | Runs after `slurmd` starts and the node registers with the Slurm controller. | Everything in the `nodeBootstrapped` stage, plus Slurm client commands (`sinfo`, `scontrol`). | Tasks that require Slurm to be running. | 

**`nodeReady` and the job-dispatch window**  
`nodeReady` scripts run after `slurmd` starts, so there is a brief window in which the scheduler might dispatch a job to the node before your `nodeReady` scripts finish. If a script must complete before any job runs:  
Move it to the `nodeBootstrapped` stage, if it doesn't need Slurm commands.
Use a Slurm prolog.

## How execution works
<a name="cng-node-lifecycle-actions-execution"></a>

On first launch:

1. The node boots and the AWS PCS agent calls `RegisterComputeNodeGroupInstance`.

1. The agent caches the lifecycle configuration and downloads the scripts.

1. The AWS PCS configuration phase runs (Slurm is configured, Hyper-Threading is disabled, and so on).

1. **Node bootstrapped** scripts run in the order you defined them.

1. `slurmd` starts and the node registers with the Slurm controller. At this point the node is available to accept jobs.

1. **Node ready** scripts run in the order you defined them. These scripts run after the node is available to accept jobs, so the scheduler might dispatch a job before they finish (see [Lifecycle stages](#cng-node-lifecycle-actions-stages)).

On reboot, the same `nodeBootstrapped` → `slurmd` → `nodeReady` sequence runs. Only scripts marked `EVERY_BOOT` re-run. Scripts set to `FIRST_BOOT_ONLY` (the default) are skipped. The `scriptCachingPolicy` controls whether scripts are re-downloaded. For more information, see [Configure node lifecycle actions in AWS PCS](cng-node-lifecycle-actions-configure.md).

For limits on the number of scripts per stage, argument and script name lengths, and maximum script size, see [UpdateComputeNodeGroup](https://docs.aws.amazon.com/pcs/latest/APIReference/API_UpdateComputeNodeGroup.html) in the *AWS PCS API Reference*.

**Topics**
+ [Lifecycle stages](#cng-node-lifecycle-actions-stages)
+ [How execution works](#cng-node-lifecycle-actions-execution)
+ [Configure node lifecycle actions in AWS PCS](cng-node-lifecycle-actions-configure.md)
+ [Node lifecycle action examples for AWS PCS](cng-node-lifecycle-actions-examples.md)
+ [Use AWS-maintained scripts for node lifecycle actions in AWS PCS](cng-node-lifecycle-actions-vetted-scripts.md)
+ [Best practices for node lifecycle actions in AWS PCS](cng-node-lifecycle-actions-best-practices.md)
+ [Troubleshooting node lifecycle actions in AWS PCS](cng-node-lifecycle-actions-troubleshooting.md)