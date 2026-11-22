

# GPU driver lifecycle

Deadline Cloud supports NVIDIA vGPU software branches for service-managed fleets, including Long-Term Support (LTS) and Production branches. Production branches receive support for one year, while LTS branches receive support for three years. For the longest support window, pin `grid:r580` (LTS), except for `RTX PRO 4500`, which supports only `latest`. The `latest` runtime resolves to `grid:r595` for all supported accelerators. For more information about the NVIDIA vGPU software lifecycle, see the [NVIDIA vGPU Software Lifecycle Policy](https://docs.nvidia.com/vgpu/news/vgpu-software-lifecycle-policy/) on the NVIDIA website.

When NVIDIA reaches end-of-life for a driver branch, Deadline Cloud deprecates that driver and eventually removes it. If you use a pinned driver version, migrate your fleets to `latest` or to a newer supported driver before the removal date.

The following table shows the current driver support status.


**GPU runtime driver lifecycle**  

| Runtime driver | NVIDIA vGPU software | Branch type | Status | NVIDIA end-of-life | 
| --- | --- | --- | --- | --- | 
| grid:r595 | vGPU 20 | Production | Active | March 2027 | 
| grid:r580 | vGPU 19 | Long-Term Support | Active | July 2028 | 