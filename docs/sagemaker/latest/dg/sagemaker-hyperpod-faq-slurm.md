# SageMaker HyperPod FAQs

Use the following frequently asked questions to troubleshoot problems with using
SageMaker HyperPod.

###### Amazon SageMaker HyperPod FAQs

- [Why can't I find log groups of my SageMaker HyperPod
  cluster in Amazon CloudWatch?](#hyperpod-faqs-q1 "#hyperpod-faqs-q1")
- [What particular configurations does HyperPod manage in
  Slurm configuration files such as slurm.conf and
  gres.conf?](#hyperpod-faqs-q2 "#hyperpod-faqs-q2")
- [How do I run Docker on Slurm nodes on HyperPod?](#hyperpod-faqs-q3 "#hyperpod-faqs-q3")
- [Why does my parallel training job fail when I use
  NVIDIA Collective Communications Library (NCCL) with Slurm on SageMaker HyperPod platform?](#hyperpod-faqs-q4 "#hyperpod-faqs-q4")
- [How do I use local NVMe store of P instances for launching Docker
  or Enroot containers with Slurm?](#hyperpod-faqs-q5 "#hyperpod-faqs-q5")
- [How to set up EFA security groups?](#hyperpod-faqs-q6 "#hyperpod-faqs-q6")
- [How do I monitor my HyperPod cluster nodes?
  Are there any CloudWatch metrics exported from HyperPod?](#hyperpod-faqs-q7 "#hyperpod-faqs-q7")
- [Can I add an additional storage to the
  HyperPod cluster nodes? The cluster instances have limited local instance
  store.](#hyperpod-faqs-q8 "#hyperpod-faqs-q8")
- [Why are my compute nodes showing as "DOWN" or "DRAINED"
  after a reboot?](#hyperpod-faqs-q9 "#hyperpod-faqs-q9")
- [Why do my nodes keep getting drained due to Out of
  Memory (OOM) issues?](#hyperpod-faqs-q10 "#hyperpod-faqs-q10")
- [How can I ensure resources are properly cleaned up after jobs complete?](#hyperpod-faqs-q11 "#hyperpod-faqs-q11")

## Why can't I find log groups of my SageMaker HyperPod

cluster in Amazon CloudWatch?

By default, agent logs and instance start-up logs are sent to the HyperPod platform
account’s CloudWatch. In case of user lifecycle scripts, lifecycle configuration logs are
sent to your account’s CloudWatch.

If you use the [sample
lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-base-config.md "sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-base-config.md") provided by the HyperPod service team, you can expect
to find the lifecycle configuration logs written to
`/var/log/provision/provisioning.log`, and you wouldn’t encounter this
problem.

However, if you use custom paths for collecting logs from lifecycle provisioning and can’t
find the log groups appearing in your account's CloudWatch, it might be due to mismatches in
the log file paths specified in your lifecycle scripts and what the CloudWatch agent running
on the HyperPod cluster instances looks for. In this case, it means that you need to
properly set up your lifecycle scripts to send logs to the CloudWatch agent, and also set up
the CloudWatch agent configuration accordingly. To resolve the problem, choose one of the
following options.

- **Option 1:** Update your lifecycle scripts to write
  logs to `/var/log/provision/provisioning.log`.
- **Option 2:** Update the CloudWatch agent to look for your
  custom paths for logging lifecycle provisioning.
  1.  Each HyperPod cluster instance contains a CloudWatch agent
      configuration file in JSON format at
      `/opt/aws/amazon-cloudwatch-agent/sagemaker_cwagent_config.json`.
      In the configuration file, find the field name
      `logs.logs_collected.files.collect_list.file_path`. With the
      default setup by HyperPod, the key-value pair should be
      `"file_path": "/var/log/provision/provisioning.log"` as
      documented at [Logging SageMaker HyperPod at instance level](sagemaker-hyperpod-cluster-management-slurm.md#sagemaker-hyperpod-cluster-management-slurm-logging-at-instance-level "sagemaker-hyperpod-cluster-management-slurm.md#sagemaker-hyperpod-cluster-management-slurm-logging-at-instance-level"). The following code snippet shows how the JSON file looks with the
      HyperPod default configuration.

  ```
  "logs": {
      "logs_collected": {
          "files": {
              "collect_list": [
                  {
                      **"file\_path": "/var/log/provision/provisioning.log"**,
                      "log_group_name": "/aws/sagemaker/Clusters/[ClusterName]/[ClusterID]",
                      "log_stream_name": "LifecycleConfig/[InstanceGroupName]/{instance_id}",
                      "retention_in_days": -1
                  }
              ]
          }
      },
      "force_flush_interval": 3
  }
  ```

  2.  Replace the value for the `"file_path"` field name with
      the custom path you use in your lifecycle scripts. For example, if you have
      set up your lifecycle scripts to write to
      `/var/log/custom-provision/custom-provisioning.log`, update
      the value to match with it as follows.

  ```
  "file_path": "`/var/log/custom-provision/custom-provisioning.log`"
  ```

  3.  Restart the CloudWatch agent with the configuration file to finish
      applying the custom path. For example, the following CloudWatch command
      shows how to restart the CloudWatch agent with the CloudWatch agent
      configuration file from step 1. For more information, see also [Troubleshooting the CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/troubleshooting-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/troubleshooting-CloudWatch-Agent.md").

  ```
  sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
      -a fetch-config -m ec2 -s -c \
      file:/opt/aws/amazon-cloudwatch-agent/sagemaker_cwagent_config.json
  ```

## What particular configurations does HyperPod manage in

Slurm configuration files such as `slurm.conf` and
`gres.conf`?

When you create a Slurm cluster on HyperPod, the HyperPod agent sets up
the [`slurm.conf`](https://slurm.schedmd.com/slurm.conf.html "https://slurm.schedmd.com/slurm.conf.html")
and [`gres.conf`](https://slurm.schedmd.com/gres.conf.html "https://slurm.schedmd.com/gres.conf.html")
files at `/opt/slurm/etc/` to manage the Slurm cluster based on your
HyperPod cluster creation request and lifecycle scripts. The following list shows
what specific parameters the HyperPod agent handles and overwrites.

###### Important

We strongly recommend that you DON’T change these parameters managed by
HyperPod.

- In [`slurm.conf`](https://slurm.schedmd.com/slurm.conf.html "https://slurm.schedmd.com/slurm.conf.html"), HyperPod sets up the following basic
  parameters: `ClusterName`, `SlurmctldHost`,
  `PartitionName`, and `NodeName`.

Also, to enable the [Automatic node
recovery and auto-resume](sagemaker-hyperpod-resiliency-slurm-auto-resume.md "sagemaker-hyperpod-resiliency-slurm-auto-resume.md")
functionality, HyperPod requires the `TaskPlugin` and
`SchedulerParameters` parameters set as follows. The
HyperPod agent sets up these two parameters with the required values by
default.

```
TaskPlugin=task/none
SchedulerParameters=permit_job_expansion
```

- In [`gres.conf`](https://slurm.schedmd.com/gres.conf.html "https://slurm.schedmd.com/gres.conf.html"), HyperPod manages `NodeName` for GPU
  nodes.

## How do I run Docker on Slurm nodes on HyperPod?

To help you run Docker on your Slurm nodes running on HyperPod, the HyperPod service team
provides setup scripts that you can include as part of the lifecycle configuration for cluster
creation. To learn more, see [Base lifecycle scripts provided by HyperPod](sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-base-config.md "sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-base-config.md") and [Running Docker containers on
a Slurm compute node on HyperPod](sagemaker-hyperpod-run-jobs-slurm-docker.md "sagemaker-hyperpod-run-jobs-slurm-docker.md").

## Why does my parallel training job fail when I use

NVIDIA Collective Communications Library (NCCL) with Slurm on SageMaker HyperPod platform?

By default, the Linux OS sets the `#RemoveIPC=yes` flag. Slurm and mpirun
jobs that use NCCL generate inter-process communication (IPC) resources under non-root user sessions. These user sessions
might log out during the job process.

When you run jobs with Slurm or mpirun, if `systemd` detects that the user isn't logged in, it cleans up the IPC resources.
Slurm and mpirun jobs can run without the
user being logged in, but that requires that you disable cleanup at the systemd level and set it
up at the Slurm level instead. For more information, see
[Systemd in the NCCL documentation](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting.html#systemd "https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting.html#systemd").

To disable cleanup at the systemd level, complete the following steps.

1. Set the flag `#RemoveIPC=no` in the file `/etc/systemd/logind.conf` if you're running training jobs that use Slurm and NCCL.
2. By default, Slurm doesn't clean up shared resources. We recommend that you set up a Slurm epilog script to clean up shared resources.
   This cleanup is useful when you have a lot of shared resources and want to clean them up after training jobs. The following is an example script.

```
#!/bin/bash
: <<'SUMMARY'
Script: epilog.sh

Use this script with caution, as it can potentially delete unnecessary resources and cause issues if you don't use it correctly.

Note: You must save this script in a shared in a shared location that is accessible to all nodes in the cluster, such as `/fsx volume`.
Workers must be able to access the script to run the script after jobs.

SUMMARY

# Define the log directory and create it if it doesn't exist
LOG_DIR="/`<PLACEHOLDER>`/epilogue" #NOTE: Update `PLACEHOLDER` to be a shared value path, such as `/fsx/epilogue`.
mkdir -p "$LOG_DIR"

# Name the log file using the Slurm job name and job ID
log_file="$LOG_DIR/epilogue-${SLURM_JOB_NAME}_${SLURM_JOB_ID}.log"

logging() {
    echo "[$(date)] $1" | tee -a "$log_file"
}

# Slurm epilogue script to clean up IPC resources
logging "Starting IPC cleanup for Job $SLURM_JOB_ID"

# Clean up shared memory segments by username
for seg in $(ipcs -m | awk -v owner="$SLURM_JOB_USER" '$3 == owner {print $2}'); do
    if ipcrm -m "$seg"; then
        logging "Removed shared memory segment $seg"
    else
        logging "Failed to remove shared memory segment $seg"
    fi
done

# Clean up semaphores by username
for sem in $(ipcs -s | awk -v user="$SLURM_JOB_USER" '$3 == user {print $2}'); do
    if ipcrm -s "$sem"; then
        logging "Removed semaphore $sem"
    else
        logging "Failed to remove semaphore $sem"
    fi
done

# Clean up NCCL IPC
NCCL_IPC_PATH="/dev/shm/nccl-*"
for file in $NCCL_IPC_PATH; do
    if [ -e "$file" ]; then
        if rm "$file"; then
            logging "Removed NCCL IPC file $file"
        else
            logging "Failed to remove NCCL IPC file $file"
        fi
    fi
done
logging "IPC cleanup completed for Job $SLURM_JOB_ID"
exit 0
```

For more information about the Epilog parameter, see [Slurm documentation](https://slurm.schedmd.com/slurm.conf.html#OPT_Epilog "https://slurm.schedmd.com/slurm.conf.html#OPT_Epilog"). 3. In the `slurm.conf` file from the controller node, add in a line to point to the epilog script you created.

```
Epilog="/path/to/epilog.sh"  #For example: /fsx/epilogue/epilog.sh
```

4. Run the following commands to change permissions of the script and to make it executable.

```
chown slurm:slurm /path/to/epilog.sh
chmod +x  /path/to/epilog.sh
```

5. To apply all of your changes, run `scontrol reconfigure`.

## How do I use local NVMe store of P instances for launching Docker

or Enroot containers with Slurm?

Because the default root volume of your head node usually is limited by 100GB EBS volume,
you need to set up Docker and Enroot to use local NVMe instance store. To learn how to set
up NVMe store and use it for launching Docker containers, see [Running Docker containers on
a Slurm compute node on HyperPod](sagemaker-hyperpod-run-jobs-slurm-docker.md "sagemaker-hyperpod-run-jobs-slurm-docker.md").

## How to set up EFA security groups?

If you want to create a HyperPod cluster with EFA-enabled instances, make sure
that you set up a security group to allow all inbound and outbound traffic to and from the
security group itself. To learn more, see [Step 1: Prepare an
EFA-enabled security group](../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security "../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security") in the _Amazon EC2 User
Guide_.

## How do I monitor my HyperPod cluster nodes?

Are there any CloudWatch metrics exported from HyperPod?

To gain observability into the resource utilization of your HyperPod cluster, we
recommend that you integrate the HyperPod cluster with Amazon Managed Grafana and Amazon Managed Service for Prometheus. With
various open-source Grafana dashboards and exporter packages, you can export and visualize
metrics related to the HyperPod cluster resources. To learn more about setting up
SageMaker HyperPod with Amazon Managed Grafana and Amazon Managed Service for Prometheus, see [SageMaker HyperPod cluster
resources monitoring](sagemaker-hyperpod-cluster-observability-slurm.md "sagemaker-hyperpod-cluster-observability-slurm.md"). Note that SageMaker HyperPod currently
doesn't support the exportation of system metrics to Amazon CloudWatch.

## Can I add an additional storage to the

HyperPod cluster nodes? The cluster instances have limited local instance
store.

If the default instance storage is insufficient for your workload, you can configure
additional storage per instance. Starting from the [release on June 20, 2024](sagemaker-hyperpod-release-notes.md#sagemaker-hyperpod-release-notes-20240620 "sagemaker-hyperpod-release-notes.md#sagemaker-hyperpod-release-notes-20240620"), you
can add an additional Amazon Elastic Block Store (EBS) volume to each instance in your SageMaker HyperPod cluster.
Note that this capability cannot be applied to existing instance groups of SageMaker HyperPod
clusters created before June 20, 2024. You can utilize this capability by patching existing
SageMaker HyperPod clusters created before June 20, 2024 and adding new instance groups to them.
This capability is fully effective for any SageMaker HyperPod clusters created after June 20, 2024.

## Why are my compute nodes showing as "DOWN" or "DRAINED"

after a reboot?

This typically occurs when nodes are rebooted using `sudo reboot` instead
of Slurm's control interface. To properly reboot nodes, use the Slurm command
`scontrol reboot nextstate=resume <list_of_nodes>`. This ensures Slurm
maintains proper control of the node state and resumes normal operation after
reboot.

For GPU instances (like NVIDIA P5), this can also happen if the node can't complete
its boot process within Slurm's default time limit (60 seconds). To resolve this,
increase the `TimeToResume` parameter in `slurm.conf` to 300
seconds. This gives GPU instances sufficient time to boot and initialize drivers.

## Why do my nodes keep getting drained due to Out of

Memory (OOM) issues?

OOM issues occur when jobs exceed the node's memory capacity. To prevent this, implement `cgroups` to enforce memory
limits per job. This prevents a single job from affecting the entire node and improves isolation and stability.

Example setup in `slurm.conf`:

```
TaskPlugin=task/cgroup
```

Example setup in `cgroup.conf`:

```
CgroupAutomount=yes
ConstrainCores=yes
CgroupPlugin=autodetect
ConstrainDevices=yes
ConstrainRAMSpace=yes
ConstrainSwapSpace=yes
SignalChildrenProcesses=yes
MaxRAMPercent=99
MaxSwapPercent=80
MinRAMSpace=100
```

For more information, see [Control
Group in Slurm](https://slurm.schedmd.com/cgroups.html "https://slurm.schedmd.com/cgroups.html"), [Cgroup and PAM-based login control for Slurm compute nodes](https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config/utils/pam_adopt_cgroup_wheel.sh#L197 "https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config/utils/pam_adopt_cgroup_wheel.sh#L197"), and [Configure Cgroups for Slurm](https://catalog.workshops.aws/sagemaker-hyperpod/en-US/07-tips-and-tricks/16-enable-cgroups "https://catalog.workshops.aws/sagemaker-hyperpod/en-US/07-tips-and-tricks/16-enable-cgroups").

## How can I ensure resources are properly cleaned up after jobs complete?

Implement epilogue scripts to automatically clean up resources after jobs complete.
Resources might not be cleared correctly when jobs crash unexpectedly, contain bugs that
prevent normal cleanup, or when shared memory buffers (include those shared between
processes and GPU drivers) retain allocated.

Epilogue scripts can perform tasks such as clearing GPU memory, removing temporary
files, and unmounting file systems. These scripts have limitations when resources are
not exclusively allocated to a single job. For detailed instructions and sample scripts,
see the second bullet point of the question [Why does my parallel training job fail when I use
NVIDIA Collective Communications Library (NCCL) with Slurm on SageMaker HyperPod platform?](#hyperpod-faqs-q4 "#hyperpod-faqs-q4"). For more
information, see [Enable Slurm epilog script](https://catalog.workshops.aws/sagemaker-hyperpod/en-US/07-tips-and-tricks/18-slurm-epilogue "https://catalog.workshops.aws/sagemaker-hyperpod/en-US/07-tips-and-tricks/18-slurm-epilogue").
