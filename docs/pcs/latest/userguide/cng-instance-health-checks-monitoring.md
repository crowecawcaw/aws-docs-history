

# What health monitoring detects

When health monitoring is turned on, an agent on each instance watches the hardware for faults. It writes the current result to the compute node's Slurm `Comment` field, and when it finds a `Fatal` fault, AWS PCS applies the repair action.

To test the hardware under load, use deep health checks. For more information, see [Running deep health checks when compute nodes start](cng-instance-health-checks-deep.md).

**Contents**
+ [NVIDIA GPU faults](#cng-instance-health-checks-monitoring-gpu)
+ [AWS Neuron faults](#cng-instance-health-checks-monitoring-neuron)
+ [EFA faults](#cng-instance-health-checks-monitoring-network)
+ [Instances with nothing to monitor](#cng-instance-health-checks-monitoring-other)
+ [How health monitoring uses DCGM](#cng-instance-health-checks-monitoring-dcgm)

## NVIDIA GPU faults
<a name="cng-instance-health-checks-monitoring-gpu"></a>

On instances with NVIDIA GPUs, health monitoring uses NVIDIA Data Center GPU Manager (DCGM) and the NVIDIA driver.


**NVIDIA GPU condition codes**  

| **Condition code** | **Severity** | **Fault** | 
| --- | --- | --- | 
| `GPU_COUNT_MISMATCH` | Fatal | The instance has fewer GPUs than its instance type, or DCGM and the NVIDIA device files report different numbers of GPUs. | 
| `GPU_ECC_DBE` | Fatal | An uncorrectable (double-bit) error correction code (ECC) error in GPU memory. | 
| `GPU_FABRIC_HEALTH` | Fatal | The GPU fabric reports degraded bandwidth, an unhealthy route, a route or access timeout recovery, or an incorrect configuration. | 
| `GPU_FABRIC_MGR` | Fatal or Warning | NVIDIA Fabric Manager reports a failure (`Fatal`), or a status that means the NVIDIA driver and DCGM versions don't match (`Warning`). | 
| `GPU_NVLINK` | Fatal | NVLink errors. | 
| `GPU_XID_{{n}}` | Fatal or Warning | The NVIDIA driver reported XID error {{n}}. These XIDs are `Fatal`: 46, 48, 54, 62, 63, 64, 74, 79, 95, 109, 110, 119, 120, 136, 140, 142, 143, 151, 155, 156, 158. All other XIDs are `Warning`. | 
| `GPU_DCGM_HEALTH_{{n}}` | Fatal or Warning | DCGM's health watches reported error code {{n}}. Failures are `Fatal` and warnings are `Warning`, except code 123 and some code 71 failures, which are `Warning`. | 
| `GPU_PAGE_RETIRE` | Warning | The GPU retired memory pages. | 
| `GPU_PCIE` | Warning | PCIe replays on the GPU's link. | 
| `GPU_THERMAL` | Warning | The GPU temperature crossed the DCGM policy threshold. | 
| `GPU_DCGM_FIELD_{{n}}` | Warning | DCGM couldn't read watched field {{n}}, such as clock event reasons or NVSwitch errors. | 
| `GPU_NCCL` | Warning | The kernel log shows a segmentation fault in the NCCL library. | 

For information about what each XID means, see [Xid Errors](https://docs.nvidia.com/deploy/xid-errors/index.html) on the NVIDIA website.

## AWS Neuron faults
<a name="cng-instance-health-checks-monitoring-neuron"></a>

On instances with AWS Neuron devices, such as Trainium and Inferentia instances, health monitoring detects the following faults.


**AWS Neuron condition codes**  

| **Condition code** | **Severity** | **Fault** | 
| --- | --- | --- | 
| `NEURON_DMA` | Fatal | A direct memory access (DMA) error on a Neuron device. | 
| `NEURON_HBM_UE` | Fatal | An uncorrectable error in a Neuron device's high-bandwidth memory. | 
| `NEURON_NC_UE` | Fatal | An uncorrectable error in a NeuronCore. | 
| `NEURON_SRAM_UE` | Fatal | An uncorrectable error in a Neuron device's on-chip SRAM. | 

## EFA faults
<a name="cng-instance-health-checks-monitoring-network"></a>

On instances with Elastic Fabric Adapter (EFA) devices, health monitoring detects the following fault.


**EFA condition codes**  

| **Condition code** | **Severity** | **Fault** | 
| --- | --- | --- | 
| `EFA_COUNTER` | Warning | An EFA error counter, such as drops or retransmit timeouts, increased faster than its allowed rate. | 

## Instances with nothing to monitor
<a name="cng-instance-health-checks-monitoring-other"></a>

On an instance without NVIDIA GPUs, Neuron devices, or EFA devices, the compute node's health is `not-monitoring`, and AWS PCS takes no action on it.

We recommend that you keep instance health checks turned off on compute node groups whose instances have no NVIDIA GPUs or Neuron devices.

## How health monitoring uses DCGM
<a name="cng-instance-health-checks-monitoring-dcgm"></a>

We recommend that you enable `nvidia-dcgm.service` on custom GPU AMIs. PCS-ready DLAMI already enables it. Without it, health monitoring runs its own DCGM engine, which adds background CPU activity that can slow tightly coupled multi-node jobs.