

# Detecting and repairing hardware faults with instance health checks

A fault in an instance's GPU or accelerator can stop or slow every job that runs on the compute node. Amazon EC2 status checks can miss these faults, because they check whether the instance and its host are reachable and working, not whether its GPUs or accelerators work correctly. Instance health checks find them and act on the compute node through Slurm, so that the scheduler stops placing jobs there.

**Contents**
+ [Prerequisites](#cng-instance-health-checks-requirements)
+ [Turning on health monitoring with the default settings](#cng-instance-health-checks-get-started)
+ [Checking that health monitoring is running](#cng-instance-health-checks-verify)
+ [Choosing a configuration](#cng-instance-health-checks-choose)
+ [Repair actions](#cng-instance-health-checks-repair-actions)
+ [Before you turn on instance health checks](#cng-instance-health-checks-limitations)
+ [Configuring instance health checks](cng-instance-health-checks-configure.md)
  + [Instance health check settings](cng-instance-health-checks-configure.md#cng-instance-health-checks-configure-settings)
  + [Turning on instance health checks when you create a compute node group](cng-instance-health-checks-configure.md#cng-instance-health-checks-configure-create)
  + [Changing or turning off instance health checks](cng-instance-health-checks-configure.md#cng-instance-health-checks-configure-update)
  + [Viewing instance health check settings](cng-instance-health-checks-configure.md#cng-instance-health-checks-configure-view)
+ [What health monitoring detects](cng-instance-health-checks-monitoring.md)
  + [NVIDIA GPU faults](cng-instance-health-checks-monitoring.md#cng-instance-health-checks-monitoring-gpu)
  + [AWS Neuron faults](cng-instance-health-checks-monitoring.md#cng-instance-health-checks-monitoring-neuron)
  + [EFA faults](cng-instance-health-checks-monitoring.md#cng-instance-health-checks-monitoring-network)
  + [Instances with nothing to monitor](cng-instance-health-checks-monitoring.md#cng-instance-health-checks-monitoring-other)
  + [How health monitoring uses DCGM](cng-instance-health-checks-monitoring.md#cng-instance-health-checks-monitoring-dcgm)
+ [Running deep health checks when compute nodes start](cng-instance-health-checks-deep.md)
  + [Profiles](cng-instance-health-checks-deep.md#cng-instance-health-checks-deep-profiles)
  + [Start time limit](cng-instance-health-checks-deep.md#cng-instance-health-checks-deep-timeout)
  + [Results](cng-instance-health-checks-deep.md#cng-instance-health-checks-deep-results)
  + [Where to find the results](cng-instance-health-checks-deep.md#cng-instance-health-checks-deep-logs)
+ [Checking compute node health in Slurm](cng-instance-health-checks-node-health.md)
  + [Finding compute nodes that a repair action changed](cng-instance-health-checks-node-health.md#cng-instance-health-checks-node-health-find)
  + [Reading a compute node's health check results](cng-instance-health-checks-node-health.md#cng-instance-health-checks-node-health-fields)
  + [Finding past repair actions](cng-instance-health-checks-node-health.md#cng-instance-health-checks-node-health-history)
  + [Returning an isolated compute node to service](cng-instance-health-checks-node-health.md#cng-instance-health-checks-node-health-resume)
  + [Keeping a compute node in service while a fault is present](cng-instance-health-checks-node-health.md#cng-instance-health-checks-node-health-keep)
  + [Collecting diagnostic data from an instance](cng-instance-health-checks-node-health.md#cng-instance-health-checks-node-health-evidence)
+ [Troubleshooting instance health checks](cng-instance-health-checks-troubleshooting.md)
  + [Health checks are turned on, but nothing runs](cng-instance-health-checks-troubleshooting.md#cng-instance-health-checks-troubleshooting-nothing-runs)
  + [A compute node was isolated or replaced, and you don't know why](cng-instance-health-checks-troubleshooting.md#cng-instance-health-checks-troubleshooting-why)
  + [Instances are replaced repeatedly when compute nodes start](cng-instance-health-checks-troubleshooting.md#cng-instance-health-checks-troubleshooting-loop)
  + [Every deep health check reports a Warning](cng-instance-health-checks-troubleshooting.md#cng-instance-health-checks-troubleshooting-investigate)
  + [Health results don't appear on the compute node](cng-instance-health-checks-troubleshooting.md#cng-instance-health-checks-troubleshooting-comment)
  + [A job stays pending with `ReqNodeNotAvail`](cng-instance-health-checks-troubleshooting.md#cng-instance-health-checks-troubleshooting-pending)

## Prerequisites
<a name="cng-instance-health-checks-requirements"></a>

To use instance health checks, you need the following:
+ The cluster must use Slurm version 26.05 or later.
+ The AMI must have AWS PCS agent version 1.6.0-1 or later. With an older agent, compute nodes start with no checks, and AWS PCS reports no error. For more information, see [AWS PCS agent versions](pcs-agent-versions.md).
+ The AMI must use a supported operating system other than Amazon Linux 2.
+ For GPU instances, the AMI must have the NVIDIA driver and NVIDIA Data Center GPU Manager (DCGM) version 4. Also enable GPU persistence mode (`nvidia-persistenced`); without it, every deep health check reports a `Warning`. For more information, see [Every deep health check reports a Warning](cng-instance-health-checks-troubleshooting.md#cng-instance-health-checks-troubleshooting-investigate).
+ For deep health checks, every instance type in the compute node group must have an NVIDIA GPU. Health monitoring has no instance type requirement.

Instance health checks don't need additional IAM permissions.

## Turning on health monitoring with the default settings
<a name="cng-instance-health-checks-get-started"></a>

To turn on health monitoring for a compute node group that doesn't have instance health checks yet, run the following command. To turn it on when you create a compute node group, add the same option to `create-compute-node-group`.

```
aws pcs update-compute-node-group --region {{region}} \
    --cluster-identifier {{my-cluster}} \
    --compute-node-group-identifier {{my-node-group}} \
    --instance-health-checks '{"healthMonitoring": {"mode": "STANDARD"}}'
```

Replace {{region}} with the ID of the AWS Region where your cluster is. This configuration does the following:
+ An agent on each instance checks the GPUs, AWS Neuron devices, and Elastic Fabric Adapter (EFA) devices for faults while the compute node runs jobs.
+ When the agent finds a fault that needs repair, AWS PCS applies the default repair action, `AUTO`.
+ Deep health checks stay off.

In the console, turn on **Enable health monitoring** in the **Instance health checks** section of the create or edit page. For all the settings and the console steps, see [Configuring instance health checks](cng-instance-health-checks-configure.md).

**Important**  
Like other changes to a compute node group, changing instance health checks drains the compute nodes and replaces their instances. Make the change when the compute node group has few running jobs.

## Checking that health monitoring is running
<a name="cng-instance-health-checks-verify"></a>

After instances launch with the new settings, run the following command on a login node, for a compute node whose instance is running.

```
scontrol show node {{node-name}} | grep Comment
```

The output looks like the following.

```
Comment={"health":"healthy","monitors":[{"monitor_type":"AcceleratedHardwareReady","status":"healthy","codes":[]},{"monitor_type":"NetworkingReady","status":"healthy","codes":[]}]}
```

The `Comment` field shows the agent's result, for example `"health":"healthy"`. On an instance without GPUs, Neuron devices, or EFA devices, it shows `"health":"not-monitoring"`. If the `Comment` is empty, see [Health checks are turned on, but nothing runs](cng-instance-health-checks-troubleshooting.md#cng-instance-health-checks-troubleshooting-nothing-runs). To read the results, see [Checking compute node health in Slurm](cng-instance-health-checks-node-health.md).

## Choosing a configuration
<a name="cng-instance-health-checks-choose"></a>

Change the default settings in the following cases.

You want to find faults before jobs run on a new instance  
Also turn on deep health checks. Start with the `QUICK` or `MEDIUM` profile. For the start time limit, see [Start time limit](cng-instance-health-checks-deep.md#cng-instance-health-checks-deep-timeout).  

```
{"healthMonitoring": {"mode": "STANDARD"},
 "deepHealthChecks": {"onStart": {"profile": "MEDIUM"}}}
```
For more information, see [Running deep health checks when compute nodes start](cng-instance-health-checks-deep.md).

You want to keep a faulty instance to investigate it  
Use the `ISOLATE` repair action. The compute node stays out of service, and its instance keeps running and is billed, until you return it to service. A compute node above the group's minimum instance count is still scaled down when its idle time is reached, even while it is isolated, and AWS PCS terminates its instance.  

```
{"healthMonitoring": {"mode": "STANDARD", "repairAction": "ISOLATE"}}
```

You want to see what health checks find before they act  
Use the `NONE` repair action. The agent reports faults in the compute node's `Comment` field and changes nothing. Change the repair action when you trust the results.  

```
{"healthMonitoring": {"mode": "STANDARD", "repairAction": "NONE"}}
```

## Repair actions
<a name="cng-instance-health-checks-repair-actions"></a>

Each fault that a health check finds has a condition code, such as `GPU_ECC_DBE`, and a severity. Only a fault with `Fatal` severity starts the repair action. AWS PCS reports a `Warning` fault but doesn't act on it.

The repair action is what AWS PCS does with the compute node when a health check finds a `Fatal` fault, as the following table shows.


**Repair actions**  

| **Repair action** | **Slurm state** | **What happens** | 
| --- | --- | --- | 
| `AUTO` (default)<br />Console: **Automatic** | Depends on the action | AWS PCS chooses the action. | 
| `REPLACE`<br />Console: **Replace** | `POWER_DOWN_ASAP` | The compute node takes no new jobs. Its running jobs finish, and then AWS PCS replaces the instance. If a deep health check finds the fault while the instance starts, AWS PCS replaces the instance immediately. | 
| `ISOLATE`<br />Console: **Isolate** | `FAIL` | The compute node takes no new jobs, and its running jobs continue. It stays in the `FAIL` state until you return it to service, so you can investigate the instance, which keeps running and is billed. AWS PCS still scales down a compute node above the group's minimum instance count when its idle time is reached, and terminates its instance. To collect data before then, see [Collecting diagnostic data from an instance](cng-instance-health-checks-node-health.md#cng-instance-health-checks-node-health-evidence). | 
| `NONE`<br />Console: **None** | No change | AWS PCS doesn't change the compute node's state. The health check writes the fault to the compute node's Slurm `Comment` field. | 

AWS PCS never returns a compute node to service by itself. It stays out of service until you return it to service or AWS PCS replaces its instance. For more information, see [Checking compute node health in Slurm](cng-instance-health-checks-node-health.md).

## Before you turn on instance health checks
<a name="cng-instance-health-checks-limitations"></a>

AWS PCS doesn't limit how many compute nodes it repairs at once. If a problem affects many instances, start with the repair action `NONE`.