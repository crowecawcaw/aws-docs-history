

# Configuring Multi-Instance GPU (MIG) in AWS PCS
<a name="mig-configuration"></a>

NVIDIA Multi-Instance GPU (MIG) partitions a supported GPU into isolated GPU instances, each with its own memory and compute resources. Slurm schedules each MIG profile as its own Generic Resource (GRES) type, so multiple jobs can share one physical GPU with hardware isolation.

MIG devices can't be described statically in `gres.conf`: their device files and UUIDs only exist after the MIG instances are created on the booted node, so there is no `File` or `Type` value to configure ahead of time. On AWS PCS you configure MIG with a `gres.conf` record that only enables `AutoDetect`, together with a `Gres` setting that declares the profiles. `slurmd` then discovers the MIG devices when the node boots. AWS PCS supports `AutoDetect`, and therefore MIG, on Slurm version 25.11 and later.

## Prerequisites
<a name="mig-configuration-prerequisites"></a>
+ A compute node group that uses a MIG-capable instance type.
+ Slurm version 25.11 or later.
+ Configured CPU topology. GPU autodetection requires the node's socket layout. On Slurm 25.11, set `Sockets` for the compute node group; on Slurm 26.05 and later, AWS PCS configures it automatically. For more information, see [Configuring hardware topology in AWS PCS](hardware-topology.md).

## Step 1: Configure MIG on the instances
<a name="mig-configuration-instances"></a>

The MIG instances must exist before `slurmd` starts and registers the node. If MIG mode is enabled but no MIG instances are created, `slurmd` detects the parent GPUs, finds no usable MIG device, and the node registers with no schedulable GPU. Create the MIG instances in the node's boot process, for example in a custom AMI or a launch template user data script that runs before `slurmd` starts. For more information, see [NVIDIA Multi-Instance GPU User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/).

1. Enable MIG mode on the GPUs:

   ```
   nvidia-smi -mig 1
   ```

   MIG mode is GPU state, not disk state, and it resets between EC2 instance allocations, so it must be enabled on every launch; it can't be baked into an AMI as already enabled. It also can't take effect while processes are using the GPUs. Enable it early in the boot sequence, before any service that uses the GPUs starts (for example, from a `systemd` unit in a custom AMI or a `cloud-init` boothook in the launch template user data; see [Example: Run early boot operations with a cloud-init boothook](working-with_ec2-user-data_early-boot.md)). At that point no process holds the GPUs, so the mode change takes effect without a reboot. Verify that MIG mode is `Enabled` (not `Pending`) on every GPU with `nvidia-smi -q`.
**Important**  
If your platform does require a reboot to change MIG mode, reboot from an early boot stage such as a `cloud-init` boothook, before the [AWS PCS bootstrap](working-with_ec2-user-data.md) starts. Don't reboot from a node lifecycle action script: a reboot there interrupts the AWS PCS bootstrap sequence. For how to create the boot hook, see [Example: Run early boot operations with a cloud-init boothook](working-with_ec2-user-data_early-boot.md).

1. Create the GPU instances and compute instances for the profiles you want. For example, to partition each of 8 GPUs into one `3g.20gb`, one `2g.10gb`, and two `1g.5gb` instances:

   ```
   for i in 0 1 2 3 4 5 6 7; do
       nvidia-smi mig -i $i -cgi 9,14,19,19 -C
   done
   ```

## Step 2: Configure the compute node group
<a name="mig-configuration-slurm"></a>

Declare both halves of the GRES configuration on the compute node group:
+ In `gresCustomSettings`, a GPU record that only enables `AutoDetect`. Don't set `Name`, `Type`, or `File`. The MIG devices are discovered on the node.
+ In `slurmCustomSettings`, a `Gres` setting that declares the MIG profiles and counts that jobs can request. The profile names and counts must match the MIG instances created on the node.

**Example – Declaring MIG profiles on a compute node group (8 GPUs partitioned as shown in Step 1)**  

```
aws pcs update-compute-node-group \
    --cluster-identifier {{my-cluster}} \
    --compute-node-group-identifier {{my-cng-1}} \
    --slurm-configuration \
    'gresCustomSettings=[{AutoDetect=nvml}],slurmCustomSettings=[{parameterName=Gres,parameterValue=gpu:3g.20gb:8\,gpu:2g.10gb:8\,gpu:1g.5gb:16}]'
```

For the constraints between the two halves, see [Constraints between gres.conf and the Gres setting](gres-custom-settings.md#gres-custom-settings-constraints). Because AWS PCS can't count devices that are discovered at boot, it accepts any profile names and counts in the `Gres` setting for a record that only enables `AutoDetect`. Consistency with the actual MIG instances is only verified when the node registers.

When a node boots and registers, it advertises the discovered profiles with their socket affinity, for example `Gres=gpu:3g.20gb:8(S:0),gpu:1g.5gb:28(S:1)`. A job that requests a profile, such as `--gres=gpu:3g.20gb:1`, is placed on a single MIG instance and gets its UUID in `CUDA_VISIBLE_DEVICES` (for example, `MIG-e7aa6185-06d5-53e9-a4d9-00f7670f741e`), so CUDA restricts the job to that partition.

**Note**  
The controller logs warnings such as `Ignoring file-less GPU gpu:3g.20gb from final GRES list` for MIG records. This is expected: the authoritative GRES comes from node registration.

## Limitations
<a name="mig-configuration-limitations"></a>

Because a MIG configuration names no devices, the controller only knows a node's real GRES after the node boots and registers. This causes the following limitations. They apply to any GPU record that only enables `AutoDetect`, and therefore to every MIG compute node group.

**Note**  
As a best practice, use a static compute node group for MIG: set `minInstanceCount` equal to `maxInstanceCount` in the scaling configuration. The nodes then stay running and registered instead of powering down between jobs, which mitigates both limitations.

### Configuration updates don't reach powered-down nodes
<a name="mig-configuration-limitations-update"></a>

When you change the MIG configuration of a compute node group (the profiles in the `Gres` setting, or the MIG partitioning in the boot process), the change doesn't reach nodes that previously registered the old configuration and are powered down at that moment. Those nodes keep advertising the profiles they last registered until they next boot and register, which only happens when a job is allocated to them. The consequences are:
+ Jobs that request the new profiles are rejected at submission with `Requested node configuration is not available`, because no node advertises them yet.
+ Jobs that request the old profiles are still accepted, even though the configuration no longer declares them.
+ If you reduce a profile count, a job sized for the old count can be admitted and run on a node that has fewer MIG instances than the job requested.

After you change the MIG configuration, boot every node that registered the previous configuration so it re-registers and advertises the new profiles. To boot a powered-down node without submitting a job to it, run `scontrol` from a login node:

```
scontrol update NodeName={{my-cng-1-[1-8]}} State=POWER_UP
```

### Jobs allocated to powered-down nodes can start without a GPU
<a name="mig-configuration-limitations-preboot"></a>

A job allocated to a node while the node is powered down is granted a profile count, but no specific device, because the devices aren't known yet. When the node then boots and the job starts, the job has no MIG device assigned: it runs with an empty `CUDA_VISIBLE_DEVICES`, and with `ConstrainDevices` set in the cgroup configuration it is denied access to every GPU. Slurm reports the job as `RUNNING` though. The MIG instance the job was counted against isn't assigned to any other job either, so it stays unusable until the job ends.

To detect this condition, verify at the start of the job that `CUDA_VISIBLE_DEVICES` is not empty, and exit or requeue the job when it is:

```
if [ -z "$CUDA_VISIBLE_DEVICES" ]; then
    scontrol requeue "$SLURM_JOB_ID"
    exit 1
fi
```