# Create a conda build recipe for the Maya adaptor

The `maya-openjd` package provides the adaptor that integrates
Maya with AWS Deadline Cloud (Deadline Cloud) job submissions. When you submit a
Maya render job using a Deadline Cloud submitter GUI, the
`CondaPackages` parameter includes `maya-openjd` alongside the
`maya` package. The adaptor handles launching Maya,
communicating render parameters, and managing the application lifecycle during a job
session. For more information about adaptors, see [Adaptor packages](conda-package.md#conda-package-adaptors "conda-package.md#conda-package-adaptors").

## Understanding the recipe

The [maya-openjd sample recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-openjd "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-openjd") on the GitHub website builds the adaptor from the [deadline-cloud-for-maya
source package](https://github.com/aws-deadline/deadline-cloud-for-maya "https://github.com/aws-deadline/deadline-cloud-for-maya") published to PyPI. The [recipe.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-openjd/recipe/recipe.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-openjd/recipe/recipe.yaml") on the GitHub website installs the package using `pip`
into the conda environment.

The recipe depends on Python and two other packages from the Deadline Cloud samples
repository that you need to build first. These packages are available on the GitHub website:

- [deadline](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/deadline "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/deadline") – The Deadline Cloud client library.
- [openjd-adaptor-runtime](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/openjd-adaptor-runtime "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/openjd-adaptor-runtime") – The Open Job Description adaptor
  runtime.

Python and other dependencies are available from [conda-forge](https://conda-forge.org/ "https://conda-forge.org/") on the conda-forge website, so add `-c
 conda-forge` to the `rattler-build publish` command when you build
the adaptor package.

## Building the adaptor package

The `maya-openjd` package depends on two other packages from the Deadline Cloud
samples repository. Build all three packages in order from the
`conda_recipes` directory. The `-c conda-forge` option on each
command is to satisfy recipe dependencies for Python and Python libraries.

Build the `deadline` package.

```
rattler-build publish deadline/recipe/recipe.yaml \
    --to file://$HOME/my-conda-channel \
    --build-number=+1 \
    -c conda-forge
```

Build the `openjd-adaptor-runtime` package.

```
rattler-build publish openjd-adaptor-runtime/recipe/recipe.yaml \
    --to file://$HOME/my-conda-channel \
    --build-number=+1 \
    -c conda-forge
```

Build the `maya-openjd` package.

```
rattler-build publish maya-openjd/recipe/recipe.yaml \
    --to file://$HOME/my-conda-channel \
    --build-number=+1 \
    -c conda-forge
```

For other publishing options:

- To publish to an Amazon S3 channel, see [Publish packages to an S3 conda
  channel](publish-packages-s3-channel.md "publish-packages-s3-channel.md").
- To automate builds using a Deadline Cloud package building queue, see [Automate package builds with Deadline
  Cloud](automate-package-builds.md "automate-package-builds.md").
