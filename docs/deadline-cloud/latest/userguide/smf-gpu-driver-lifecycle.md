

# GPU driver lifecycle
<a name="smf-gpu-driver-lifecycle"></a>

Deadline Cloud supports NVIDIA Long-Term Support (LTS) branch drivers for service-managed fleets. Deadline Cloud plans to continue supporting LTS branches as NVIDIA releases them. For more information about the NVIDIA vGPU software lifecycle, see the [NVIDIA vGPU Software Lifecycle Policy](https://docs.nvidia.com/vgpu/news/vgpu-software-lifecycle-policy/) on the NVIDIA website.

When NVIDIA reaches end-of-life for a driver branch, Deadline Cloud deprecates that driver and eventually removes it. If you use a pinned driver version, migrate your fleets to `latest` or to a newer supported driver before the removal date.

The following table shows the current driver support status.


**GPU runtime driver lifecycle**  

| Runtime driver | NVIDIA vGPU software | Branch type | Status | NVIDIA end-of-life | 
| --- | --- | --- | --- | --- | 
| grid:r580 | vGPU 19 | Long-Term Support | Active | July 2028 | 