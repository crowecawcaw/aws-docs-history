

# Running deep health checks when compute nodes start

Deep health checks run NVIDIA Data Center GPU Manager (DCGM) diagnostic tests on the GPUs each time an instance starts or reboots, before the compute node accepts jobs. The tests load the GPUs, so they find faults that health monitoring can't detect on an idle GPU.

Deep health checks add time to each start, and longer profiles add more time. 

**Contents**
+ [Profiles](#cng-instance-health-checks-deep-profiles)
+ [Start time limit](#cng-instance-health-checks-deep-timeout)
+ [Results](#cng-instance-health-checks-deep-results)
+ [Where to find the results](#cng-instance-health-checks-deep-logs)

## Profiles
<a name="cng-instance-health-checks-deep-profiles"></a>

The `QUICK`, `MEDIUM`, and `LONG` profiles run DCGM diagnostic levels 1, 2, and 3.

## Start time limit
<a name="cng-instance-health-checks-deep-timeout"></a>

A compute node must finish starting, including the deep health check, within 30 minutes. If it doesn't, AWS PCS replaces the instance, and because the new instance runs the same check, the replacements can repeat.

## Results
<a name="cng-instance-health-checks-deep-results"></a>


**Deep health check results**  

| **Result** | **Condition code** | **What AWS PCS does** | 
| --- | --- | --- | 
| Passed, or the tests couldn't run | None | Starts the compute node. | 
| Needs investigation (Warning) | `GPU_DIAG_INVESTIGATE`, or `GPU_DIAG_TRIAGE_{{n}}`, `GPU_DIAG_CONFIG_{{n}}`, `GPU_DIAG_UNKNOWN_{{n}}` | Starts the compute node and reports the result. | 
| A GPU needs a reset or must be isolated (Fatal) | `GPU_DIAG_RESET`, `GPU_DIAG_ISOLATE`, or the same with `_{{n}}` | Runs the repair action. | 

{{n}} is the DCGM error ID. For what it means, see [DCGM diagnostic errors](https://docs.nvidia.com/datacenter/dcgm/latest/reference/diagnostics/errors.html) on the NVIDIA website.

The result appears in the compute node's `Comment` field until health monitoring reports a newer result, and in its `Reason` field when the repair action runs. For more information, see [Reading a compute node's health check results](cng-instance-health-checks-node-health.md#cng-instance-health-checks-node-health-fields).

## Where to find the results
<a name="cng-instance-health-checks-deep-logs"></a>

Each instance keeps its deep health check results, including the DCGM output in `dcgm-diag-boot.json`, in `/var/log/amazon/pcs/boot-health-check/`. The files are deleted when AWS PCS replaces the instance.