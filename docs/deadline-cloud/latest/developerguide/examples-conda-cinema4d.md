# Build a Maxon Cinema 4D conda package for Deadline Cloud

The samples repository includes the following Cinema 4D conda
recipes:

- [cinema4d-2024](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/cinema4d-2024 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/cinema4d-2024")
  and
  [cinema4d-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/cinema4d-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/cinema4d-2025")
- [cinema4d-c4dtoa-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/cinema4d-c4dtoa-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/cinema4d-c4dtoa-2025"): Arnold renderer (C4DtoA) for Cinema 4D 2025.
- [cinema4d-vray-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/cinema4d-vray-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/cinema4d-vray-2025"): V-Ray for Cinema 4D 2025.
- [cinema4d-insydium-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/cinema4d-insydium-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/cinema4d-insydium-2025"): Insydium plugins for Cinema 4D 2025.
- [cinema4d-openjd](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/cinema4d-openjd "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/cinema4d-openjd"): Builds the Cinema 4D Open Job Description adaptor with rattler-build for Python
  3.13.
  The Cinema 4D Windows installer requires Administrator permissions
  that are not available in most conda package build environments. Each
  recipe README includes step-by-step instructions for installing Cinema 4D
  on a fresh EC2 Windows Server instance and creating a redistributable
  archive. Upload the archive to your private Amazon S3 bucket, then download it
  to the `conda_recipes/archive_files` directory of your samples
  repository clone.

The Cinema 4D 2025 package includes the standalone Redshift command
line renderer, which the
[Render Redshift scenes on Deadline Cloud](examples-jb-redshift.md "examples-jb-redshift.md") job bundle uses for GPU
rendering.

Submit the build:

```
./submit-package-job cinema4d-2025
```
