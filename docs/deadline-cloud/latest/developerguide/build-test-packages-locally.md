# Build and test packages locally

Before publishing packages to Amazon S3 or setting up CI/CD automation on your Deadline Cloud farm,
you can build and test conda packages on your workstation using a local filesystem channel.
This approach lets you rapidly iterate locally on recipes and verify packages.

The `rattler-build publish` command builds a recipe, copies the resulting
package to a channel, and indexes the channel in one step. When you target a local filesystem
directory, `rattler-build` creates and initializes the channel automatically if the
directory does not exist.

The following instructions use the Blender 4.5 sample recipe from the
[Deadline Cloud samples
repository](https://github.com/aws-deadline/deadline-cloud-samples "https://github.com/aws-deadline/deadline-cloud-samples") on the GitHub website. You can substitute a different recipe from the
samples repository or use your own recipe.

## Prerequisites

Before you begin, install the following tools on your workstation:

- **pixi** – A package manager that you use to
  install `rattler-build` and to test packages. For installation instructions,
  see [pixi.sh](https://pixi.sh "https://pixi.sh") on the Pixi website.
- **rattler-build** – The package build tool used
  by Deadline Cloud conda recipes. After you install pixi, run the following command to install
  `rattler-build`.

```
pixi global install rattler-build
```

- **git** – Required to clone the samples
  repository. On Windows, [Git for
  Windows](https://gitforwindows.org/ "https://gitforwindows.org/") on the Git for Windows website also provides a
  `bash` shell, which some of the Windows sample recipes
  require.

## Building and publishing a package to a local channel

In this procedure, you clone the Deadline Cloud samples repository and use
`rattler-build publish` to build and publish the package to a local filesystem
channel.

###### Note

Large applications can require tens of GB of free disk space for the source archive,
extracted files, and build output. Make sure that you use a disk with enough available
space for the package build output.

###### To build and publish a package to a local channel

1. Clone the Deadline Cloud samples repository.

```
git clone https://github.com/aws-deadline/deadline-cloud-samples.git
```

2. Change to the `conda_recipes` directory.

```
cd deadline-cloud-samples/conda_recipes
```

3. Run the following command to build the Blender 4.5 recipe and publish
   the package to a local channel directory.

On Linux and macOS, run the following command.

```
rattler-build publish blender-4.5/recipe/recipe.yaml \
    --to file://$HOME/my-conda-channel \
    --build-number=+1
```

On Windows (cmd), run the following command.

```
rattler-build publish blender-4.5/recipe/recipe.yaml ^
    --to file://%USERPROFILE%/my-conda-channel ^
    --build-number=+1
```

The `rattler-build publish` command performs the following actions:

    * Builds the package from the recipe.
    * Creates the channel directory if the directory does not exist.
    * Copies the package file to the channel.
    * Indexes the channel so that package managers can find the package.

If your package recipe depends on packages from a particular channel, such as
[conda-forge](https://conda-forge.org/ "https://conda-forge.org/") on the conda-forge website,
add `-c conda-forge` to the command.

###### About build numbers

The `--build-number=+1` option automatically picks the next build number
based on what already exists in the destination channel. The best practice is to never
overwrite a package in a channel. Always build to a new build number if the package would
otherwise have the same filename. Using `--build-number=+1` achieves this when
you build to a production channel or a staging channel that mirrors production.

If you want to control the build number directly, you can set it with a specific value
such as `--build-number=7`. If you omit the option, `rattler-build`
uses the build number defined in the `recipe.yaml` file.

For more information about `rattler-build publish`, see the
[rattler-build publish
documentation](https://rattler-build.prefix.dev/latest/publish/ "https://rattler-build.prefix.dev/latest/publish/") on the prefix.dev website.

## Debugging builds

If a build fails, `rattler-build` preserves the build directory so you can
investigate. Run the following command to open an interactive shell in the build environment
with all environment variables set up as they were during the build.

```
rattler-build debug shell
```

From the debug shell, you can modify files, run individual build commands, and add
dependencies to isolate the issue. For more information, see [Debugging builds](https://rattler-build.prefix.dev/latest/debugging_builds/ "https://rattler-build.prefix.dev/latest/debugging_builds/")
on the prefix.dev website.

## Testing the package

After you build and publish the package, create a temporary pixi project. Use the
project to install the package from the local channel and verify that it works
correctly.

###### To test the package

1. Create a temporary test directory and initialize a pixi project with the local
   channel.

On Linux and macOS, run the following commands.

```
mkdir package-test-env
cd package-test-env
pixi init --channel file://$HOME/my-conda-channel
```

On Windows (cmd), run the following commands.

```
mkdir package-test-env
cd package-test-env
pixi init --channel file://%USERPROFILE%/my-conda-channel
```

2. Add the package to the project.

```
pixi add blender=4.5
```

3. Verify that the package works correctly.

```
pixi run blender --version
```

The `pixi run` command activates the conda environment for the
project directory and runs the specified command within it. The environment persists in
the project directory, so you can use the same `pixi run` command from other
terminals. For more information, see the [`pixi run`
command](https://pixi.sh/latest/reference/cli/pixi/run/ "https://pixi.sh/latest/reference/cli/pixi/run/") on the Pixi website.

When you are satisfied with the package, you can publish the package to an Amazon S3 conda
channel so that Deadline Cloud workers can install the package. See [Publish packages to an S3 conda
channel](publish-packages-s3-channel.md "publish-packages-s3-channel.md").

## Removing packages from the channel

Avoid removing packages from channels that you use for production, because lockfiles
reference specific packages by hash. Removing a package prevents re-creating environments
from those lockfiles. For development and testing channels, you can remove a specific
package by deleting the `.conda` file from the channel directory and then
re-indexing the channel. First, install `rattler-index`.

```
pixi global install rattler-index
```

Then delete the package file and re-index the channel.

On Linux and macOS, run the following commands.

```
rm $HOME/my-conda-channel/linux-64/blender-4.5.0-hb0f4dca_1.conda
rattler-index fs $HOME/my-conda-channel
```

On Windows (cmd), run the following commands.

```
del %USERPROFILE%\my-conda-channel\win-64\blender-4.5.0-hb0f4dca_1.conda
rattler-index fs %USERPROFILE%\my-conda-channel
```

Package files are stored in platform-specific subdirectories such as
`linux-64`, `win-64`, or `osx-arm64`. List the contents
of these subdirectories to find the exact filename of the package you want to remove.

## Cleaning up

After testing, you can remove the test project and the local channel.

###### To clean up test resources

1. Remove the test project directory.

On Linux and macOS, run the following command.

```
rm -rf package-test-env
```

On Windows (cmd), run the following command.

```
rmdir /s /q package-test-env
```

2. Remove the local conda channel directory.

On Linux and macOS, run the following command.

```
rm -rf $HOME/my-conda-channel
```

On Windows (cmd), run the following command.

```
rmdir /s /q %USERPROFILE%\my-conda-channel
```

3. (Optional) Remove the `rattler-build` output directory that contains the
   built package file.

On Linux and macOS, run the following command.

```
rm -rf deadline-cloud-samples/conda_recipes/output
```

On Windows (cmd), run the following command.

```
rmdir /s /q deadline-cloud-samples\conda_recipes\output
```

For supported plugins with plugin sync examples, see [Sync plugins to Deadline Cloud workers](plugin-sync.md "plugin-sync.md").
