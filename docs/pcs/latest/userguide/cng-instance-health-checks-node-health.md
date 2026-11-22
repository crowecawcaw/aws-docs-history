

# Checking compute node health in Slurm

Instance health checks report their results in two Slurm fields of each compute node:
+ `Reason`: written only when a repair action changes the compute node's state. It names the action and the fault.
+ `Comment`: the current health monitoring result, in JSON. The agent updates it whenever the result changes, even when no repair action runs.

Run the commands in this topic on a login node or a compute node in the cluster, unless the step says otherwise.

**Contents**
+ [Finding compute nodes that a repair action changed](#cng-instance-health-checks-node-health-find)
+ [Reading a compute node's health check results](#cng-instance-health-checks-node-health-fields)
+ [Finding past repair actions](#cng-instance-health-checks-node-health-history)
+ [Returning an isolated compute node to service](#cng-instance-health-checks-node-health-resume)
+ [Keeping a compute node in service while a fault is present](#cng-instance-health-checks-node-health-keep)
+ [Collecting diagnostic data from an instance](#cng-instance-health-checks-node-health-evidence)

## Finding compute nodes that a repair action changed
<a name="cng-instance-health-checks-node-health-find"></a>

To list compute nodes that are out of service and why, run `sinfo -R`. The default output shortens the `Reason`, so set a wider format:

```
sinfo -R -o "%70E %19H %N"
```

Compute nodes that a repair action changed have a `Reason` that starts with `pcs-healthcheck:`.

```
REASON                                                                 TIMESTAMP           NODELIST
pcs-healthcheck:faulted/isolate GPU_XID_79 @2026-11-10T14:02:31Z       2026-11-10T14:05:12 gpu-1
pcs-healthcheck:faulted/replace GPU_ECC_DBE @2026-11-10T14:20:07Z      2026-11-10T14:22:40 gpu-4
```

## Reading a compute node's health check results
<a name="cng-instance-health-checks-node-health-fields"></a>

The following example shows the relevant lines of `scontrol show node` for a compute node that health monitoring isolated.

```
State=IDLE+FAIL ...
Reason=pcs-healthcheck:faulted/isolate GPU_XID_79 @2026-11-10T14:02:31Z [slurm@2026-11-10T14:05:12]
Comment={"health":"faulted","monitors":[{"monitor_type":"AcceleratedHardwareReady","status":"faulted","codes":["GPU_XID_79"]},{"monitor_type":"NetworkingReady","status":"healthy","codes":[]}]}
```

The `Reason` has the format `pcs-healthcheck:faulted/{{action}} {{CODE}} @{{time}}`, where {{action}} is `isolate` or `replace` and {{CODE}} is one of the `Fatal` faults. Other faults are in the `Comment`.

A repair action replaces the compute node's existing `Reason`, including one that you set when you drained the compute node. AWS PCS writes the `Reason` only when it changes the compute node's state. While the compute node stays isolated, the `Reason` keeps the fault that isolated it. Later faults appear only in the `Comment`, which always shows the current result. Slurm clears the `Reason` when the compute node returns to service.

If the compute node is already powering down, or is in the `FAIL` state and the repair action is `ISOLATE`, the repair action doesn't change it, and the `Reason` stays as it is. With `REPLACE`, a compute node in the `FAIL` state is still replaced.

The `Comment` has a `health` value and one entry for each type of hardware that the agent monitors, with its status and condition codes.


**Health values**  

| **Value** | **Meaning** | 
| --- | --- | 
| `healthy` | The agent found no faults. | 
| `degraded` | The agent found only `Warning` faults, or it can't read part of the hardware's status, for example while the DCGM host engine is down. No repair action runs. | 
| `faulted` | The agent found at least one `Fatal` fault. The repair action runs. | 
| `not-monitoring` | The instance has no NVIDIA GPUs, Neuron devices, or EFA devices. | 
| `cannot-tell` | The health monitoring result is missing or out of date, for example because `pcs-hma` isn't running. No repair action runs. | 

The `Comment` has no timestamp. Before you rely on it, check that the agents are running on the instance:

```
systemctl is-active pcs-hma pcs-health-recovery
```

**Why the results can disagree after a deep health check**

After a deep health check isolates a compute node, the `Comment` can show `healthy` while the `Reason` shows a `GPU_DIAG` code. The `Reason` is the result of the tests at start, and the `Comment` is the current status.

## Finding past repair actions
<a name="cng-instance-health-checks-node-health-history"></a>

Repair actions are recorded in Slurm. A compute node's `Reason` shows the repair action until the compute node returns to service or AWS PCS replaces its instance.

To keep a record of every repair action, turn on scheduler log delivery. `slurmctld` logs each repair action as `update_node: node {{node-name}} reason set to: pcs-healthcheck:...`. For more information, see [Scheduler logs in AWS PCS](monitoring_scheduler-logs.md).

If the cluster uses Slurm accounting, Slurm also records each state change with its `Reason`. To list them for a compute node, run the following command.

```
sacctmgr show event Nodes={{node-name}} Start={{2026-11-01}} format=NodeName,Start,End,State,Reason%90
```

For more information, see [Slurm accounting in AWS PCS](slurm-accounting.md).

## Returning an isolated compute node to service
<a name="cng-instance-health-checks-node-health-resume"></a>

After you investigate the instance, either return the compute node to service or replace its instance.

**To return an isolated compute node to service**

1. On the instance, restart the health monitoring agent to clear the fault.

   ```
   sudo systemctl restart pcs-hma
   ```

1. Return the compute node to service.

   ```
   scontrol update nodename={{node-name}} state=resume
   ```

If the hardware reports the fault again, the repair action runs again. To keep the compute node in service anyway, see [Keeping a compute node in service while a fault is present](#cng-instance-health-checks-node-health-keep).

To replace the instance instead, run the following command. Running jobs finish first, and then AWS PCS replaces the instance.

```
scontrol update nodename={{node-name}} state=power_down_asap
```

To try to recover the compute node without replacing its instance, for example to reset a GPU, reboot it. Running jobs finish first.

```
scontrol reboot {{node-name}}
```

If deep health checks are turned on, they run again while the instance starts. Health monitoring starts over with a fresh result, so you don't need to restart `pcs-hma`. While the compute node is isolated, its `Reason` isn't cleared or refreshed.

To check the deep health check result, run the following command on the instance.

```
journalctl -b -u pcs-boot-health-check | grep 'Boot health check'
```

When the deep health check passed and the `Comment` shows `healthy`, return the compute node to service.

```
scontrol update nodename={{node-name}} state=resume
```

## Keeping a compute node in service while a fault is present
<a name="cng-instance-health-checks-node-health-keep"></a>

You can stop the repair action on one instance, for example while you confirm that a fault affects your workload. The compute node keeps running jobs, and health monitoring continues to report faults in the `Comment`.

This ignores every later `Fatal` fault on the instance, not only the current one, and it stays in effect after the instance reboots. Jobs keep running on the instance even if its hardware is faulty.

**To keep a compute node in service while a fault is present**

1. On the instance, open `/etc/amazon/pcs/health-recovery/config.yaml` as root, and set `repair_action` to `NONE`.

   ```
   repair_action: NONE
   ```

1. Restart the health recovery agent.

   ```
   sudo systemctl restart pcs-health-recovery
   ```

1. Check that the health recovery agent is running. If the output isn't `active`, run `journalctl -u pcs-health-recovery` to find the error, fix `config.yaml`, and restart the agent.

   ```
   systemctl is-active pcs-health-recovery
   ```

1. If the compute node is isolated, return it to service.

   ```
   scontrol update nodename={{node-name}} state=resume
   ```

The change applies only to that instance:
+ It doesn't change deep health checks. If the instance reboots, the deep health check uses the compute node group's repair action.
+ It ends when AWS PCS replaces the instance. The new instance uses the compute node group's settings.

## Collecting diagnostic data from an instance
<a name="cng-instance-health-checks-node-health-evidence"></a>

To save the health monitoring agent's evidence for a fault, run the following command on the instance. The command only reads data. It doesn't run diagnostics, so it's safe to run while jobs run.

```
sudo /opt/aws/pcs/bin/pcs-hma snapshot > {{snapshot.txt}}
```

Copy the file off the instance before AWS PCS replaces it. AWS PCS scales down a compute node above the group's minimum instance count when its idle time is reached, even while it is isolated.

The agents also write these logs on the instance:
+ `journalctl -u pcs-hma` and `journalctl -u pcs-health-recovery`: the agent logs. Each time the health recovery agent checks the result, it logs a decision line with the outcome and the Slurm state that it set.
+ `/var/log/amazon/pcs/bootstrap.log` on the first start, and `journalctl -u pcs-boot-health-check` after a reboot: one `Boot health check ... exited` line for each deep health check.
+ `/var/log/amazon/pcs/hma/events.jsonl`: each change in the health monitoring result. The agent creates the file at the first change.
+ `/var/log/amazon/pcs/boot-health-check/`: the deep health check results, if deep health checks are turned on.