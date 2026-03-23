# Build and test packages locally

Before publishing packages to Amazon S3 or setting up CI/CD automation on your Deadline Cloud farm,
you can build and test conda packages on your workstation using a local filesystem channel.
This approach lets you rapidly iterate locally on recipes and verify packages.

The `rattler-build publish` command builds a recipe, copies the resulting
package to a channel, and indexes the channel in one step. When you target a local filesystem
directory, `rattler-build` creates and initializes the channel automatically if the
directory does not exist.

The following instructions use the Blender 4.5 sample recipe from the
[Deadline Cloud samples](https://github.com/aws-deadline/deadline-cloud-samples "https://github.com/aws-deadline/deadline-cloud-samples")
repository on GitHub. You can substitute a different recipe from the samples
repository or use your own recipe.

## Prerequisites

Before you begin, install the following tools on your workstation:

- **pixi** – A package manager that you use to
  install `rattler-build` and to test packages. Install pixi from
  [pixi.sh](https://pixi.sh "https://pixi.sh").
- **rattler-build** – The package build tool used
  by Deadline Cloud conda recipes. After you install pixi, run the following command to install
  `rattler-build`.

```
pixi global install rattler-build
```

- **git** – Required to clone the samples
  repository. On Windows, [git for
  Windows](https://gitforwindows.org/ "https://gitforwindows.org/") also provides a `bash` shell, which some of the Windows sample recipes require.

## Building and publishing a package to a local channel

In this procedure, you clone the Deadline Cloud samples repository and use
`rattler-build publish` to build and publish the package to a local filesystem
channel.

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
    --to file://$HOME/my-conda-channel
```

On Windows (cmd), run the following command.

```
rattler-build publish blender-4.5/recipe/recipe.yaml ^
    --to file://%USERPROFILE%/my-conda-channel
```

The `rattler-build publish` command performs the following actions:

    * Builds the package from the recipe.
    * Creates the channel directory if the directory does not exist.
    * Copies the package file to the channel.
    * Indexes the channel so that package managers can find the package.

If your package recipe depends on packages from a particular channel, such as
[conda-forge](https://conda-forge.org/ "https://conda-forge.org/"), add `-c
 conda-forge` to the command.

To rebuild the package after making changes to the recipe, add
`--build-number=+1` to automatically increment the build number.

```
rattler-build publish blender-4.5/recipe/recipe.yaml \
    --to file://$HOME/my-conda-channel \
    --build-number=+1
```

For more information about `rattler-build publish`, see the
[rattler-build publish
documentation](https://rattler-build.prefix.dev/latest/publish/ "https://rattler-build.prefix.dev/latest/publish/").

## Debugging builds

If a build fails, `rattler-build` preserves the build directory so you can
investigate. Run the following command to open an interactive shell in the build environment
with all environment variables set up as they were during the build.

```
rattler-build debug shell
```

From the debug shell, you can modify files, run individual build commands, and add
dependencies to isolate the issue. For more information, see [Debugging builds](https://rattler-build.prefix.dev/latest/debugging_builds/ "https://rattler-build.prefix.dev/latest/debugging_builds/") in
the rattler-build documentation.

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

When you are satisfied with the package, you can publish the package to an Amazon S3 conda
channel so that Deadline Cloud workers can install the package. See [Publish packages to an S3 conda
channel](publish-packages-s3-channel.md "publish-packages-s3-channel.md").

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
