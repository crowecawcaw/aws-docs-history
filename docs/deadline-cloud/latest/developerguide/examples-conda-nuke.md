# Build a Foundry Nuke conda package for Deadline Cloud

The samples repository includes the following Nuke conda recipes:

- [nuke-16.0](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nuke-16.0 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nuke-16.0")
  — Foundry Nuke 16.0 for Linux 64-bit. The recipe README includes a
  version update checklist for adapting the recipe to Nuke 15.x or
  17.x.
- [nuke-denoise](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nuke-denoise "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nuke-denoise")
  — Nuke De:Noise OFX plugin. The recipe demonstrates how to package OFX
  plugins for Nuke. Place `.bundle` files in a known
  directory in `$PREFIX` and set the
  `OFX_PLUGIN_PATH` environment variable.
  To build the recipe, download `Nuke16.0v1-linux-x86_64.tgz`
  from the Foundry website and place it in the
  `conda_recipes/archive_files` directory of your samples
  repository clone. A Foundry account is required to access the
  download.

Submit the build:

```
./submit-package-job nuke-16.0
```
