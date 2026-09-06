# Render Autodesk 3ds Max scenes with V-Ray on Deadline Cloud

The
[3dsmax\_vray\_denoiser](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/3dsmax_vray_denoiser "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/3dsmax_vray_denoiser")
job bundle on the GitHub website renders 3ds Max scenes with V-Ray and converts the output from
V-Ray's native VRIMG format to EXR while preserving denoising data. The
bundle includes the following features:

- **Frame chunking**: Handles both
  contiguous ranges (for example, `1-100`) and non-contiguous
  ranges (for example, `1-5,10,15-20`).
- **VRIMG to EXR conversion**: Converts
  V-Ray's native VRIMG format to EXR while preserving denoising data,
  beauty passes, multi-channel data, and high dynamic range.
- **Automatic cleanup**: Removes
  temporary VRIMG files after successful conversion.
  To run this bundle, you need 3ds Max 2025 and V-Ray for 3ds Max 2025
  installed on Windows worker hosts. You can use the
  [3ds
  Max host configuration scripts](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/3dsmax "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/3dsmax") on the GitHub website to install 3ds
  Max and V-Ray on a Windows service-managed fleet. For more information, see
  [Install Autodesk 3ds Max on Deadline Cloud Windows workers](examples-host-config-3dsmax.md "examples-host-config-3dsmax.md").

Before submitting the job, configure your scene to save raw VRIMG output
to a local worker path (for example, `C:\Temp\output.vrimg`) and
remove absolute output paths from each render element including the
Denoiser. Then submit the bundle:

```
deadline bundle gui-submit 3dsmax_vray_denoiser/
```
