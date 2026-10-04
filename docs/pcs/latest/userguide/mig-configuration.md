

# Configuring Multi-Instance GPU (MIG) in AWS PCS
<a name="mig-configuration"></a>

NVIDIA Multi-Instance GPU (MIG) partitions a supported GPU into isolated GPU instances, each with its own memory and compute resources. Slurm schedules each MIG profile as its own Generic Resource (GRES) type, so multiple jobs can share one physical GPU with hardware isolation.

MIG devices can't be described statically in `gres.conf`: their device files and UUIDs only exist after the MIG instances are created on the booted node, so there is no `File` or `Type` value to configure ahead of time. On AWS PCS you configure MIG with a `gres.conf` record that only enables `AutoDetect`, together with a `Gres` setting that declares the profiles. `slurmd` then discovers the MIG devices when the node boots. AWS PCS supports `AutoDetect`, and therefore MIG, on Slurm version 25.11 and later.

Configuring MIG means partitioning the GPUs on each node and declaring the resulting profiles to Slurm on the compute node group. Neither works alone, so apply both in one change. If Slurm doesn't know about a node's partitions, the node has no schedulable GRES. If no node creates the declared profiles, the nodes are drained when they register. With the recommended node lifecycle action, one compute node group update carries both the partitioning script and the GRES settings.

## Prerequisites
<a name="mig-configuration-prerequisites"></a>
+ A compute node group that uses a MIG-capable instance type.
+ Slurm version 25.11 or later.
+ Configured CPU topology. GPU autodetection requires the node's socket layout. On Slurm 25.11, set `Sockets` for the compute node group; on Slurm 26.05 and later, AWS PCS configures it automatically. For more information, see [Configuring hardware topology in AWS PCS](hardware-topology.md).

## What a MIG node must have on every boot
<a name="mig-configuration-requirements"></a>

MIG mode and MIG instances live on the GPU, not on disk, so a custom AMI can't carry them, and they're lost whenever the instance is stopped, suspended, or terminated. On every boot, all of the following must be true before `slurmd` starts:

1. **MIG mode is enabled** on every GPU that serves MIG instances. `nvidia-smi -q` reports a `Current` and a `Pending` mode, and `Current` must be `Enabled`.

1. **The MIG instances exist**, both GPU instances and compute instances, for every profile in the compute node group's `Gres` setting.

1. **The profiles and counts match** the `Gres` setting.

If MIG mode is enabled but no MIG instances exist, `slurmd` finds the parent GPUs but no MIG device. It logs `MIG mode is enabled, but no MIG devices were found`, then `Discarding the following config-only GPU due to lack of File specification` for each declared profile. Because the node reports fewer GPUs than `Gres` declares, the controller rejects the registration and drains the node with the reason `gres/gpu count reported lower than configured`. Jobs that request a GPU on the node fail with `Required node not available`. Creating the MIG instances afterward doesn't undrain the node; you have to resume or replace it. The node lifecycle action described in [Apply the configuration with a node lifecycle action](#mig-configuration-instances-nla) avoids this by failing the node before it registers.

## Configure MIG on the instances
<a name="mig-configuration-instances"></a>

Configuring the instances takes the following two operations. Run them from a node lifecycle action, which keeps the logic on the compute node group instead of in an AMI you have to rebuild. See [Apply the configuration with a node lifecycle action](#mig-configuration-instances-nla). If another process already holds the GPUs at that point, run them earlier from a `cloud-init` boothook or a `systemd` unit in a custom AMI. See [If MIG mode stays pending](#mig-configuration-instances-pending). For more information about the commands, see [NVIDIA Multi-Instance GPU User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/).

1. Enable MIG mode on the GPUs:

   ```
   nvidia-smi -mig 1
   ```

   The mode change can't take effect while a process is using the GPUs. At the `nodeBootstrapped` stage `slurmd` hasn't started, so on a node that runs no other GPU service the change takes effect without a reboot. Check that the applied mode is `Enabled` on every GPU with `nvidia-smi --query-gpu=mig.mode.current --format=csv`.
**Important**  
If MIG mode stays `Pending`, another process has the GPUs open. See [If MIG mode stays pending](#mig-configuration-instances-pending).

1. Create the GPU instances and compute instances for the profiles you want. For example, to partition each of 8 GPUs into one `3g.20gb`, one `2g.10gb`, and two `1g.5gb` instances:

   ```
   for i in 0 1 2 3 4 5 6 7; do
       nvidia-smi mig -i $i -cgi 3g.20gb,2g.10gb,1g.5gb,1g.5gb -C
   done
   ```

   `-cgi` also accepts numeric profile IDs, but the same ID means a different profile on a different GPU model: `9,14,19,19` is this layout on the 40 GB A100 in a `p4d` instance, and `3g.40gb`, `2g.20gb`, and two `1g.10gb` on an 80 GB part. Use the profile names, so that they match the `Gres` setting and creation fails on a GPU that has no such profile.

   Create the largest profiles first, as in the example. MIG placements are fixed, so a layout that fits can still fail to create if the small profiles take the slices the large ones need.

### Apply the configuration with a node lifecycle action
<a name="mig-configuration-instances-nla"></a>

Configure the node lifecycle action as follows. For how to add one to a compute node group, see [Configure node lifecycle actions in AWS PCS](cng-node-lifecycle-actions-configure.md).


| **Field** | **Value** | **Why** | 
| --- | --- | --- | 
| Lifecycle stage | `nodeBootstrapped` | Runs before `slurmd` opens the GPUs and registers the node. | 
| `executionPolicy` | `EVERY_BOOT` | MIG state doesn't survive a stop, suspend, or termination. | 
| `arguments` | `["3g.20gb,2g.10gb,1g.5gb,1g.5gb"]` | The MIG profiles to create on each GPU, by name. One script then serves compute node groups with different layouts. | 
| `onError` | `TERMINATE` | Replaces a node that can't be partitioned instead of letting it register without its MIG devices. While debugging, use `STOP_SEQUENCE` to keep the instance for inspection. | 

A script that runs on every boot must be idempotent. The following outline takes the per-GPU layout as its first argument and handles one GPU at a time. It skips a GPU that already has that layout, repartitions any other, and exits non-zero if it can't finish, which fails the node. It never reboots the node. For how arguments reach a script, see [Passing arguments to scripts](cng-node-lifecycle-actions-configure.md#cng-node-lifecycle-actions-configure-arguments).

```
#!/usr/bin/env bash
# Partition every GPU as $1 specifies, then verify the result. Expected
# nvidia-smi failures are handled inline, so this doesn't use 'set -e'.
set -uo pipefail

# $1 - per-GPU MIG profile names, comma-separated, largest first, as in Gres.
PROFILES="${1:-}"
if ! echo "$PROFILES" | grep -Eq '^[0-9]+g\.[0-9]+gb(,[0-9]+g\.[0-9]+gb)*$'; then
    echo "ERROR: pass the per-GPU MIG profiles as the first argument," >&2
    echo "       for example 3g.20gb,2g.10gb,1g.5gb,1g.5gb" >&2
    exit 1
fi
EXPECTED=$(echo "$PROFILES" | tr ',' '\n' | sort)

# Fail, rather than exit 0, when there is no GPU to configure.
GPUS=$(nvidia-smi --query-gpu=index --format=csv,noheader) || {
    echo "ERROR: nvidia-smi failed. This node has no usable NVIDIA driver." >&2
    exit 1
}
if [ -z "$GPUS" ]; then
    echo "ERROR: no NVIDIA GPUs detected." >&2
    exit 1
fi

# The MIG profiles on GPU $1, in the same form as EXPECTED. nvidia-smi -L lists
# what NVML reports, which is what slurmd autodetects.
mig_devices() {
    nvidia-smi -L | awk -v gpu="$1" '
        /^GPU [0-9]+:/ { current = ($2 + 0); next }
        $1 == "MIG" && current == gpu { print $2 }
    ' | sort
}

for i in $GPUS; do
    # 1. Skip a GPU that already has the requested layout.
    if [ "$(mig_devices "$i")" = "$EXPECTED" ]; then
        echo "GPU $i: already configured as $PROFILES"
        continue
    fi

    # 2. Enable MIG mode. Ignore the exit status; step 3 checks the result.
    enable_output=$(nvidia-smi -i "$i" -mig 1 2>&1) || true

    # 3. Fail if the mode isn't applied. Don't reboot: that would interrupt
    #    the AWS PCS bootstrap.
    current=$(nvidia-smi -i "$i" --query-gpu=mig.mode.current --format=csv,noheader)
    pending=$(nvidia-smi -i "$i" --query-gpu=mig.mode.pending --format=csv,noheader)
    if [ "$current" != "Enabled" ]; then
        echo "ERROR: GPU $i MIG mode is '$current', pending '$pending'." >&2
        echo "$enable_output" >&2
        if [ "$pending" = "Enabled" ]; then
            echo "The enable is pending, so a process is holding the GPU. Stop it," >&2
            echo "or configure MIG mode in a boothook instead." >&2
        elif [ "$current" = "[N/A]" ] || [ "$current" = "N/A" ]; then
            echo "This GPU does not support MIG." >&2
        fi
        exit 1
    fi

    # 4. Recreate the layout from scratch, because instances can't be added to
    #    a partial one. Nothing uses them yet, because slurmd hasn't started.
    nvidia-smi mig -i "$i" -dci >/dev/null 2>&1 || true
    nvidia-smi mig -i "$i" -dgi >/dev/null 2>&1 || true
    if ! nvidia-smi mig -i "$i" -cgi "$PROFILES" -C; then
        echo "ERROR: MIG instance creation failed on GPU $i" >&2
        exit 1
    fi

    # 5. Check which profiles exist, not only how many, so a layout that
    #    doesn't match Gres fails here instead of at job time.
    actual=$(mig_devices "$i")
    if [ "$actual" != "$EXPECTED" ]; then
        echo "ERROR: GPU $i has the wrong MIG layout." >&2
        echo "  expected: $(echo "$EXPECTED" | tr '\n' ' ')" >&2
        echo "  found:    $(echo "$actual" | tr '\n' ' ')" >&2
        exit 1
    fi
    echo "GPU $i: configured as $PROFILES"
done
```

To set the script and the GRES settings in one call, see the example in [Declare the MIG profiles to Slurm](#mig-configuration-slurm).

If you adapt the script, keep both checks. Without the mode check, a node whose MIG mode never became `Enabled` goes on to register without its MIG devices, and the cause shows only in the `slurmd` log. Without the layout check, a node that creates the wrong profiles registers normally and fails only the jobs that request the declared profiles. For where the script's output is written, see [Logging and debugging](cng-node-lifecycle-actions-configure.md#cng-node-lifecycle-actions-configure-logging).

### If MIG mode stays pending
<a name="mig-configuration-instances-pending"></a>

Enabling MIG mode fails while any process has the GPUs open. `nvidia-smi` reports the enable as pending, for example with `In use by another client`, and it takes effect only after those processes exit or the node reboots. On a AWS PCS compute node the process is usually a GPU monitoring agent, such as NVIDIA DCGM or an agent that ships in the AMI, or `slurmd` itself if MIG is configured after `slurmd` starts. You can't reboot from the lifecycle action, so use one of the following fixes:
+ **Stop the process that holds the GPUs.** In the custom AMI, disable or remove any daemon that opens the GPUs before MIG configuration runs. Also remove any daemon that configures MIG itself. Two components partitioning the same GPUs produce a layout that doesn't match the `Gres` setting.
+ **Configure MIG in a boothook.** If you can't stop the process, move the MIG mode change and the profile creation into a `cloud-init` boothook in the launch template user data. A boothook runs before the AWS PCS bootstrap and before the AMI's services start, so the mode change takes effect without a reboot. For how to write one, see [Example: Run early boot operations with a cloud-init boothook](working-with_ec2-user-data_early-boot.md). Keep the lifecycle action as a check: on every boot it confirms the layout and fails the node if the boothook didn't apply it.

## Declare the MIG profiles to Slurm
<a name="mig-configuration-slurm"></a>

Declare both GRES settings on the compute node group:
+ In `gresCustomSettings`, a GPU record that only enables `AutoDetect`. Don't set `Name`, `Type`, or `File`. The MIG devices are discovered on the node.
+ In `slurmCustomSettings`, a `Gres` setting that declares the MIG profiles and counts that jobs can request. The profile names and counts must match the MIG instances created on the node.

**Example – Applying both parts in one update (8 GPUs, each partitioned into one `3g.20gb`, one `2g.10gb`, and two `1g.5gb`)**  

```
aws pcs update-compute-node-group \
    --cluster-identifier {{my-cluster}} \
    --compute-node-group-identifier {{my-cng-1}} \
    --slurm-configuration '{
      "gresCustomSettings": [
        { "AutoDetect": "nvml" }
      ],
      "slurmCustomSettings": [
        { "parameterName": "Gres", "parameterValue": "gpu:3g.20gb:8,gpu:2g.10gb:8,gpu:1g.5gb:16" }
      ]
    }' \
    --node-lifecycle-actions '{
      "stages": {
        "nodeBootstrapped": [
          {
            "name": "configure-mig",
            "scriptSource": {
              "scriptLocation": "s3://{{my-bucket}}/configure-mig.sh"
            },
            "arguments": ["3g.20gb,2g.10gb,1g.5gb,1g.5gb"],
            "executionPolicy": "EVERY_BOOT",
            "onError": "TERMINATE"
          }
        ]
      }
    }'
```
The example passes both parameters as JSON because the `Gres` value contains commas, which CLI shorthand syntax would need escaped.  
Keep `arguments` and `Gres` consistent: `3g.20gb,2g.10gb,1g.5gb,1g.5gb` on each of 8 GPUs gives the 8, 8, and 16 instances that `gpu:3g.20gb:8,gpu:2g.10gb:8,gpu:1g.5gb:16` declares.

For the constraints between the two settings, see [Constraints between gres.conf and the Gres setting](gres-custom-settings.md#gres-custom-settings-constraints). Because AWS PCS can't count devices that are discovered at boot, it accepts any profile names and counts in the `Gres` setting for a record that only enables `AutoDetect`. Consistency with the actual MIG instances is only verified when the node registers.

When a node boots and registers, it advertises the discovered profiles with their socket affinity, for example `Gres=gpu:3g.20gb:8(S:0),gpu:1g.5gb:28(S:1)`. A job that requests a profile, such as `--gres=gpu:3g.20gb:1`, is placed on a single MIG instance and gets its UUID in `CUDA_VISIBLE_DEVICES` (for example, `MIG-e7aa6185-06d5-53e9-a4d9-00f7670f741e`), so CUDA restricts the job to that MIG instance.

**Note**  
The controller logs warnings such as `Ignoring file-less GPU gpu:3g.20gb from final GRES list` for MIG records. This is expected: the authoritative GRES comes from node registration.

## Limitations
<a name="mig-configuration-limitations"></a>

Because a MIG configuration names no devices, the controller only knows a node's real GRES after the node boots and registers. Until a node has registered once, the controller holds only the profile counts from the `Gres` setting. This causes the following limitation. It applies to any GPU record that only enables `AutoDetect`, and therefore to every MIG compute node group.

**Note**  
As a best practice, use a static compute node group for MIG: set `minInstanceCount` equal to `maxInstanceCount` in the scaling configuration. The nodes then register when they launch, before any job is allocated to them, which avoids the limitation.

### Jobs allocated before a node first registers can start without a GPU
<a name="mig-configuration-limitations-preboot"></a>

A job allocated to a node that is powered down and has never registered, for example on the first boot of a newly created compute node group, is granted a profile count but no specific device, because the devices aren't known yet. When the node then boots and the job starts, the job has no MIG device assigned: `CUDA_VISIBLE_DEVICES` is not set, and because AWS PCS doesn't constrain device access through cgroups, the job can use every MIG device on the node. Slurm reports the job as `RUNNING` though, and the MIG instance the job was counted against is assigned to the next job that requests that profile, so both jobs can end up on the same MIG instance. Jobs allocated to the node after it has registered once, including after later power-down and power-up cycles, get their device as expected.

To detect this condition, verify at the start of the job that `CUDA_VISIBLE_DEVICES` is set, and exit or requeue the job when it isn't:

```
if [ -z "${CUDA_VISIBLE_DEVICES-}" ]; then
    scontrol requeue "$SLURM_JOB_ID"
    exit 1
fi
```

A requeued job becomes eligible to run again after the `requeue_delay` scheduler parameter, 5 seconds by default. By then the node has registered, so the job gets a device on its next start.