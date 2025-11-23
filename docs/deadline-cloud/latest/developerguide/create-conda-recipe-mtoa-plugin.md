# Create a conda build recipe for Autodesk Maya to Arnold (MtoA) plugin

You can package plugins for commercial applications as conda packages. Plugins are dynamically loaded libraries
that use an application binary interface (ABI) provided by an application to extend the functionality of that application.
The Maya to Arnold (MtoA) plugin adds the Arnold renderer as an option within Maya.

- The MtoA sample build recipe depends on the **Maya** package
  and uses an `==` constraint for the version.
- The Maya package configures a Maya module path in the virtual environment,
  `$PREFIX/usr/autodesk/maya$MAYA_VERSION/modules`, for the plugin to place a `.mod` file in.
  The MtoA sample build recipe creates a file `mtoa.mod` in this directory.

###### Write the recipe metadata

1. Open the GitHub [deadline-cloud-samples/conda_recipes/maya-mtoa-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-mtoa-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-mtoa-2025") directory in your browser or in a text editor in your
   local clone of the repository.

The recipe follows the same patterns as the Maya conda build recipe, and uses the same source
archives to install the plugin. 2. Open the [recipe/recipe.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-mtoa-2025/recipe/recipe.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-mtoa-2025/recipe/recipe.yaml") and [recipe/meta.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-mtoa-2025/recipe/meta.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-mtoa-2025/recipe/meta.yaml") files to review or edit the settings for rattler-build and for conda-build. These files
specify a dependency on `maya` during package build and when creating a virtual environment to run the plugin.

###### Write the package build script

- The package build scripts in the MtoA sample conda build recipe include comments explaining the steps
  the scripts perform. Read through the comments and commands to learn how the recipe installs MtoA
  and creates a file `mtoa.mod` in the directory specified by the Maya package.

Arnold and Maya use the same licensing technology, so the Maya
conda build recipe already includes the information needed by Arnold.

The differences between the Linux and Windows build scripts are similar to the differences for
the Maya conda build recipe.

###### Submit a job that builds the Maya MtoA plugin packages

1. Enter the `conda_recipes` directory in your clone of the GitHub [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples "https://github.com/aws-deadline/deadline-cloud-samples") repository.
2. Ensure that you have built packages for the Maya host application from the previous section.
3. Make sure that your Deadline Cloud farm is configured for your Deadline Cloud CLI. If you followed the steps to
   [Create a conda channel using Amazon S3](configure-jobs-s3-channel.md "configure-jobs-s3-channel.md") then your farm should be configured for your CLI.
4. Run the following command to submit a job that builds both Linux and Windows packages.

`./submit-package-job maya-mtoa-2025 --all-platforms`
