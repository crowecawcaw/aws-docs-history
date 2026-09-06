# Build a Foundry Nuke conda package for Deadline Cloud

The following Nuke conda recipes are available on the GitHub website:

- [nuke-16.0](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nuke-16.0 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nuke-16.0"): Foundry Nuke 16.0 for Linux 64-bit.
- [nuke-17.0](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nuke-17.0 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nuke-17.0"): Foundry Nuke 17.0 for Linux 64-bit.
- [nuke-denoise](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nuke-denoise "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nuke-denoise"): Nuke De:Noise OFX plugin. The recipe demonstrates how to package OFX
  plugins for Nuke. Place `.bundle` files in a known
  directory in `$PREFIX` and set the
  `OFX_PLUGIN_PATH` environment variable.
  Each recipe README includes a version update checklist for adapting
  the recipe to other Nuke versions.

To build a recipe, download the matching Nuke source archive from the
Foundry website (for example,
`Nuke17.0v1-linux-x86_64.tgz`) and place it in the
`conda_recipes/archive_files` directory of your samples
repository clone. A Foundry account is required to access the
download.

Submit the build:

```
./submit-package-job nuke-17.0
```
