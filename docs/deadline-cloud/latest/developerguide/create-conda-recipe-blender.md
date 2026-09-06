# Create a conda build recipe for Blender

Blender is free to use and simple to package with conda, which makes it
a good starting point for learning how to create conda packages for AWS Deadline Cloud (Deadline Cloud). The
Blender Foundation provides [application archives](https://download.blender.org/release/Blender4.5/ "https://download.blender.org/release/Blender4.5/") on the Blender website for
multiple operating systems. The [Blender 4.5 sample recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.5 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.5") in the Deadline Cloud samples repository on
the GitHub website packages these archives into a conda package.

## Understanding the recipe

The [recipe.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/blender-4.5/recipe/recipe.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/blender-4.5/recipe/recipe.yaml") file on the GitHub website defines the package metadata, source URLs, and build
options in [rattler-build template syntax](https://rattler-build.prefix.dev/latest/reference/recipe_file/#spec-reference "https://rattler-build.prefix.dev/latest/reference/recipe_file/#spec-reference") on the prefix.dev website. The recipe specifies the version number once
and provides different source URLs based on the operating system.

The `build` section in `recipe.yaml` turns off binary relocation
and dynamic shared object (DSO) linking checks. These options control how the package works
when installed into a conda virtual environment at any directory prefix. The default values
used in the `build` section are designed for packaging each dependency library separately, but when binary repackaging
an application, you need to change them. Blender does not require any RPATH
adjustment because the application archives are built with relocatability in mind. See
[Create a conda recipe for Maya](create-conda-recipe-maya.md "create-conda-recipe-maya.md") for an
example of adding relocatability.

During the package build, the [build.sh](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/blender-4.5/recipe/build.sh "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/blender-4.5/recipe/build.sh") or [build\_win.sh](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/blender-4.5/recipe/build_win.sh "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/blender-4.5/recipe/build_win.sh") script on the GitHub website runs to install files into the environment. These scripts
copy the installation files into `$PREFIX/opt/blender`, create symlinks from
`$PREFIX/bin` (on Linux), and set up activation scripts that configure
environment variables such as `BLENDER_LOCATION`. On Windows, the activation
script adds the Blender directory to the PATH instead of creating
symlinks.

The Windows build script uses `bash` instead of a `cmd.exe`
.bat file for consistency across platforms. You can install [git for Windows](https://gitforwindows.org/ "https://gitforwindows.org/") on the Git for Windows website to provide
`bash` for package building.

The recipe also includes a `deadline-cloud.yaml` file that specifies the
conda platforms and metadata for submitting automated package build jobs to Deadline Cloud. For
more information, see [Submit a package build
job](automate-package-builds.md#automate-submit-package-job "automate-package-builds.md#automate-submit-package-job").

## Building the Blender package

Use `rattler-build publish` to build the Blender 4.5 recipe
and publish the package to a channel. You can publish to a local filesystem channel for
testing or directly to an Amazon S3 channel for production use. If you completed the setup
in [Build and test packages locally](build-test-packages-locally.md "build-test-packages-locally.md"),
run the following command from the `conda_recipes` directory.

```
rattler-build publish blender-4.5/recipe/recipe.yaml \
    --to file://$HOME/my-conda-channel \
    --build-number=+1
```

For other publishing options:

- To publish to an Amazon S3 channel, see [Publish packages to an S3 conda
  channel](publish-packages-s3-channel.md "publish-packages-s3-channel.md").
- To automate builds using a Deadline Cloud package building queue, see [Automate package builds with Deadline
  Cloud](automate-package-builds.md "automate-package-builds.md").
