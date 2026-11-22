

# Use a GPU accelerator

You can configure worker hosts in your service-managed fleets to use one or more GPUs to accelerate processing your jobs. Using an accelerator can reduce the time that it takes to process a job, but can increase the cost of each worker instance. You should test your workloads to understand the trade offs between a fleet using GPU accelerators and fleets that don't.

GPUs are not available for fleets with wait-and-save instances.

**GPU quota is zero by default**  
The default quota for GPUs in service-managed fleets is **zero**, for both Spot and On-Demand instances. Creating a fleet that uses GPU accelerators fails with a `ServiceQuotaExceededException` until you request an increase. The check happens when you create or update the fleet, not when the fleet scales out. For the steps, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.  
Choose the quota that matches the instance purchasing option your fleet uses:  
`Spot G Instance GPUs per region` (quota code `L-2CCF07BF`)
`OnDemand G instance GPUs per region` (quota code `L-5D6BA491`)
Spot and On-Demand have separate quotas. Increasing one doesn't change the other.  
Deadline Cloud counts a fleet against these quotas at its maximum possible usage. That usage is the fleet's maximum worker count multiplied by the maximum number of GPUs for each instance. Deadline Cloud then adds up that usage across all service-managed fleets in the AWS Region, whether or not those fleets have running workers. A fleet that has scaled to zero workers still counts against the quota.  
Request at least enough GPUs for the fleets that you plan to run at the same time. For more information, see [Service quotas and throttling for Deadline Cloud](deadline-cloud-quotas.md).

You decide whether your fleet will use GPU accelerators when you specify the worker instance capabilities. If you decide to use GPUs, you can specify the minimum and maximum number of GPUs for each instance, the types of GPU chips to use, and the runtime driver for the GPUs.

Instance capabilities are also how you guarantee the amount of memory each worker has. A step's `amount.worker.memory` host requirement selects compatible fleets and doesn't launch larger instances. For more information about how host requirements and fleet configuration interact, see [Host requirements and fleet capabilities](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/host-requirements-overview.html) in the *Deadline Cloud Developer Guide*.

The available GPU accelerators are:
+ `T4` – NVIDIA T4 Tensor Core GPU
+ `A10G` – NVIDIA A10G Tensor Core GPU
+ `L4` – NVIDIA L4 Tensor Core GPU
+ `L40S` – NVIDIA L40S Tensor Core GPU
+ `RTX PRO Server 6000` – NVIDIA RTX PRO 6000 Blackwell Server Edition GPU
+ `RTX PRO 4500` – NVIDIA RTX PRO 4500 Blackwell Server Edition GPU. Supports only the `latest` runtime driver.

You can choose from the following runtime drivers:
+ `Latest` – Use the latest runtime available for the chip. If you specify `latest` and a new version of the runtime is released, the new version of the runtime is used.
+ `grid:r595` – For more information about NVIDIA vGPU software 20, see [NVIDIA vGPU software 20](https://docs.nvidia.com/vgpu/20.0/index.html) on the NVIDIA website (Production Branch).
+ `grid:r580` – For more information about NVIDIA vGPU software 19, see [NVIDIA vGPU software 19](https://docs.nvidia.com/vgpu/19.0/index.html) on the NVIDIA website (Long-Term Support).

Deadline Cloud uses `latest` as the default runtime driver for all accelerators. If you specify a runtime driver for some accelerators, you must specify one for all of them. Mixing explicit values with blank values returns an error.

**RTX PRO 4500 supports only the latest driver**  
The `RTX PRO 4500` accelerator for G7 instances supports only the `latest` runtime driver, which currently uses R595. With `latest`, Deadline Cloud upgrades your fleet to newer drivers automatically as they are released. Set the runtime to `latest` or leave it blank.

To run jobs on G7 instances, add the `RTX PRO 4500` accelerator to an existing service-managed fleet that uses GPU-accelerated instances. You can't change a CPU-only fleet to use GPUs. For a CPU-only fleet, create a new fleet, and then choose GPU-accelerated instances. The following procedure uses the Deadline Cloud console.

**To add G7 instances to an existing fleet**

1. In the navigation pane, choose **Farms**, and then select your farm.

1. Choose the **Fleets** tab, select the fleet, and then choose **Edit fleet**.

1. On the **Configure worker capabilities** page, for **GPU chip names**, add **RTX PRO 4500**.  
![The Compute capabilities section of the Configure worker capabilities page, with RTX PRO 4500 selected for GPU chip names, Latest selected for Driver version, and the GPU count and vCPU configuration fields.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/smf-gpu-add-g7-worker-capabilities.png)

1. For **Driver version**, confirm that **Latest** is selected.

1. Under **vCPU configuration**, set the vCPU and memory ranges so that they include at least one G7 instance size. For example, `g7.8xlarge` has 32 vCPUs and 128 GiB of memory. Under **GPU configuration**, set **GPU count maximum** high enough for that size. `g7.2xlarge`, `g7.4xlarge`, and `g7.8xlarge` have 1 GPU. `g7.12xlarge`, `g7.24xlarge`, and `g7.48xlarge` have 2, 4, and 8 GPUs. The G7 sizes that match appear in the list of resulting instance types.

1. If the fleet uses **Select instance types** to allow only specific instance types, add the G7 instance types to the list.

1. Complete the remaining steps, and then choose **Save changes**.

Workers that are already running keep their instance type, so G7 workers start as the fleet scales out. For more information, see [Update a fleet configuration](smf-update-config.md).