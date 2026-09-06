# Build an Infinigen conda package for Deadline Cloud

The
[infinigen-1.19.0](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/infinigen-1.19.0 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/infinigen-1.19.0")
rattler-build recipe on the GitHub website packages Infinigen, a procedural 3D
scene generator from Princeton Vision & Learning Lab. For more
information, see [Infinigen](https://infinigen.org/ "https://infinigen.org/") on the
Infinigen website. The package includes the following:

- Infinigen v1.19.0 procedural scene generation engine.
- `bpy 4.2.0` (Blender as a Python module) for headless
  rendering through Cycles. No standalone Blender installation is needed
  at runtime.
- Terrain C++ shared libraries (CPU and optional CUDA) compiled from
  Infinigen source for landscape generation.
  To build this recipe, deploy the
  [CUDA
  farm CloudFormation template](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm") on the GitHub website to create a
  Deadline Cloud farm with a CUDA GPU fleet for the build. The build requires a GPU
  worker (for CUDA terrain compilation) and takes approximately 6 minutes.

Submit the build from the `conda_recipes` directory:

```
./submit-package-job infinigen-1.19.0
```

To reuse conda environments between jobs, attach the
[conda\_queue\_env\_improved\_caching.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_improved_caching.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_improved_caching.yaml")
queue environment on the GitHub website to your queue. The dependency
closure of Infinigen contains many gigabytes of packages, so caching saves
significant time and bandwidth.

For a job bundle that uses this package, see
[Generate procedural 3D scenes with Infinigen on Deadline Cloud](examples-jb-infinigen.md "examples-jb-infinigen.md").
