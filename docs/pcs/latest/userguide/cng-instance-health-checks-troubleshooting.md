

# Troubleshooting instance health checks

**Contents**
+ [Health checks are turned on, but nothing runs](#cng-instance-health-checks-troubleshooting-nothing-runs)
+ [A compute node was isolated or replaced, and you don't know why](#cng-instance-health-checks-troubleshooting-why)
+ [Instances are replaced repeatedly when compute nodes start](#cng-instance-health-checks-troubleshooting-loop)
+ [Every deep health check reports a Warning](#cng-instance-health-checks-troubleshooting-investigate)
+ [Health results don't appear on the compute node](#cng-instance-health-checks-troubleshooting-comment)
+ [A job stays pending with `ReqNodeNotAvail`](#cng-instance-health-checks-troubleshooting-pending)

## Health checks are turned on, but nothing runs
<a name="cng-instance-health-checks-troubleshooting-nothing-runs"></a>

The compute node group shows instance health check settings, but compute nodes have no `Comment` from the agent, and no repair action ever runs. Check the following on an instance in the compute node group:
+ **The agent version.** Run the following command. The output shows the agent version, for example `PCS Agent version: 1.6.0-1`.

  ```
  grep -o "PCS Agent version: [^,]*" /var/log/amazon/pcs/bootstrap.log | tail -1
  ```

  If the version is older than 1.6.0-1, AWS PCS accepted the settings, but the AMI has no health check agents. Update the agent in the AMI. For more information, see [AWS PCS agent versions](pcs-agent-versions.md).
+ **The agents.** Run `systemctl status pcs-hma pcs-health-recovery`. If they aren't installed, check whether the AMI uses Amazon Linux 2, which the health check agents don't support.
+ **DCGM version 4.** On GPU instances, run `ldconfig -p | grep libdcgm.so.4`. If there's no output, install NVIDIA DCGM version 4. Without it, the agent can't read GPU status.
+ **An AMI made from a running compute node.** This AMI contains that compute node's agent configuration. The agents don't start on other instances. Build the AMI from a clean instance instead.

## A compute node was isolated or replaced, and you don't know why
<a name="cng-instance-health-checks-troubleshooting-why"></a>

Run `sinfo -R`. A `Reason` that starts with `pcs-healthcheck:` names the repair action and the condition code. For more information, see [Checking compute node health in Slurm](cng-instance-health-checks-node-health.md).

## Instances are replaced repeatedly when compute nodes start
<a name="cng-instance-health-checks-troubleshooting-loop"></a>

If compute nodes never finish starting, and AWS PCS replaces each new instance, check the following:
+ **The deep health check runs past the 30-minute start time limit.** Choose a shorter profile. For more information, see [Start time limit](cng-instance-health-checks-deep.md#cng-instance-health-checks-deep-timeout).
+ **A fault on every instance.** If each new instance fails the deep health check, the cause can be the AMI, such as a driver and DCGM version mismatch, rather than the hardware. A replacement at start leaves no `Reason`. To find the condition code, read the `slurmctld` log, or set the deep health check repair action to `NONE` and read the results on an instance. For more information, see [Scheduler logs in AWS PCS](monitoring_scheduler-logs.md).

## Every deep health check reports a Warning
<a name="cng-instance-health-checks-troubleshooting-investigate"></a>

If the deep health check on every instance reports `GPU_DIAG_CONFIG_{{n}}`, GPU persistence mode is probably off in the AMI. Enable `nvidia-persistenced` in your AMI.

## Health results don't appear on the compute node
<a name="cng-instance-health-checks-troubleshooting-comment"></a>

The agent writes to the `Comment` only when it's empty or already holds the agent's result. If you or another tool wrote to the `Comment`, clear it:

```
scontrol update nodename={{node-name}} comment=""
```

If the `Comment` is empty, see [Health checks are turned on, but nothing runs](#cng-instance-health-checks-troubleshooting-nothing-runs).

## A job stays pending with `ReqNodeNotAvail`
<a name="cng-instance-health-checks-troubleshooting-pending"></a>

If a job requests specific compute nodes and one of them is isolated, the job waits for that compute node. Run `sinfo -R` to see whether the compute node has a `pcs-healthcheck:` `Reason`. If it does, ask your cluster administrator to investigate the compute node, or submit the job without that compute node.