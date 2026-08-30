# Build a SideFX Houdini conda package for Deadline Cloud

The samples repository on the GitHub website includes the following
Houdini conda recipes:

- [houdini-20.5](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-20.5 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-20.5")
- [houdini-21.0](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-21.0 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-21.0")
- [houdini-22.0](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-22.0 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-22.0"):
  Houdini 22.0 builds are compiled with GCC 14.2, so download the
  `gcc14.2` source archive from SideFX rather than the
  archive that earlier versions use.
- [houdini-redshift-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-redshift-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-redshift-2025")
  and
  [houdini-redshift-2026](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-redshift-2026 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-redshift-2026"): Redshift renderer for Houdini.
- [houdini-vray-7](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-vray-7 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-vray-7"): V-Ray 7 renderer for Houdini.
  The
  [Render USD scenes with Houdini Husk on Deadline Cloud](examples-jb-houdini-husk-usd.md "examples-jb-houdini-husk-usd.md") job bundle uses these
  recipes to render USD scenes with Karma, V-Ray, and Redshift Hydra render
  delegates.

Submit the build:

```
./submit-package-job houdini-21.0
```
