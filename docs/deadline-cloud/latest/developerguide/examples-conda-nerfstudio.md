# Build a NeRF Studio conda package for Deadline Cloud

The
[nerfstudio](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nerfstudio "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nerfstudio")
rattler-build recipe on the GitHub website packages
[NeRF Studio](https://docs.nerf.studio/ "https://docs.nerf.studio/") from the Nerfstudio website plus the following:

- The
  [Splatfacto
  in the Wild](https://docs.nerf.studio/nerfology/methods/splatw.html "https://docs.nerf.studio/nerfology/methods/splatw.html") external model.
- NeRF Studio dependencies that are not yet available on
  conda-forge.
- The
  [nerfstudio/gsplat](https://github.com/nerfstudio-project/gsplat "https://github.com/nerfstudio-project/gsplat")
  package's `simple_trainer.py` example, available as the
  command `gsplat_simple_trainer`.
- The
  [KevinXu02/splatfacto-w](https://github.com/KevinXu02/splatfacto-w "https://github.com/KevinXu02/splatfacto-w")
  package's `export_script.py`, available as the command
  `splatfactow_export`.
  To build this recipe, deploy the
  [CUDA
  farm CloudFormation template](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm") on the GitHub website to create a Deadline Cloud farm
  with a CUDA fleet for the build, then submit the package build job:

```
./submit-package-job nerfstudio
```

To reuse conda environments between jobs, attach the
[conda\_queue\_env\_improved\_caching.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_improved_caching.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_improved_caching.yaml")
queue environment on the GitHub website to your queue. Because the
dependency closure of NeRF Studio contains many gigabytes of packages,
caching saves significant time and bandwidth.

For a job bundle that uses this package, see
[Train 3D Gaussian Splatting from video on Deadline Cloud](examples-jb-gaussian-splatting.md "examples-jb-gaussian-splatting.md").
