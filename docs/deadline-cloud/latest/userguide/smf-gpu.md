# Use a GPU accelerator

You can configure worker hosts in your service-managed fleets to use one or more GPUs
to accelerate processing your jobs. Using an accelerator can reduce the time that it
takes to process a job, but can increase the cost of each worker instance. You should
test your workloads to understand the trade offs between a fleet using GPU accelerators
and fleets that don't.

GPUs are not available for fleets with wait-and-save intances.

###### Note

For testing purposes you are limited to one GPU. To request more for your
production workloads, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the
_Service Quotas User Guide_.

You decide whether your fleet will use GPU accelerators when you specify the worker
instance capabilities. If you decide to use GPUs, you can specify the minimum and
maximum number of GPUs for each instance, the types of GPU chips to use, and the runtime
driver for the GPUs.

The available GPU accelerators are:

- `T4` - NVIDIA T4 Tensor Core GPU
- `A10G` - NVIDIA A10G Tensor Core GPU
- `L4` - NVIDIA L4 Tensor Core GPU
- `L40s` - NVIDIA L40S Tensor Core GPU
  You can choose from the following runtime drivers:

- `Latest` - Use the latest runtime available for the chip. If you
  specify `latest` and a new version of the runtime is released, the
  new version of the runtime is used.
- `grid:r570` - [NVIDIA vGPU software
  18](https://docs.nvidia.com/vgpu/18.0/index.html "https://docs.nvidia.com/vgpu/18.0/index.html")
- `grid:r550` (deprecated) - [NVIDIA vGPU software
  17](https://docs.nvidia.com/vgpu/17.0/index.html "https://docs.nvidia.com/vgpu/17.0/index.html")
  If you don't specify a runtime, Deadline Cloud uses `latest` as the default.
  However, if you have multiple accelerators and specify `latest` for some and
  leave others blank, Deadline Cloud raises an exception.
