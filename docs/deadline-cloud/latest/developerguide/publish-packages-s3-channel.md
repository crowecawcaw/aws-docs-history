# Publish packages to an Amazon S3 conda channel

You can publish conda packages to an Amazon Simple Storage Service (Amazon S3) bucket so that AWS Deadline Cloud (Deadline Cloud) workers can
install them for running jobs. The `rattler-build publish` command works with
Amazon S3 the same way as with a local filesystem channel. The command can build a recipe and
publish the result, or publish a package file that you already built. In both cases, the command
uploads the package to the bucket and indexes the channel in one step.

The `rattler-build publish` command authenticates with AWS using the standard
credential chain, so it uses your AWS configuration like any AWS tool. For more
information about configuring credentials, see [Configuration and credential file
settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md") in the _AWS Command Line Interface (AWS CLI) User Guide_.

## Prerequisites

Before you publish packages to Amazon S3, complete the following prerequisites:

- **pixi and rattler-build** – Install pixi from
  [pixi.sh](https://pixi.sh "https://pixi.sh"), then install
  `rattler-build`.

```
pixi global install rattler-build
```

- **git** – Required to clone the samples
  repository. On Windows, [git for
  Windows](https://gitforwindows.org/ "https://gitforwindows.org/") also provides a `bash` shell, which some of the Windows sample recipes require.
- **Amazon S3 bucket** – An Amazon S3 bucket to use as the
  conda channel. You can use the job attachments bucket from your Deadline Cloud farm or create a
  separate bucket.
- **AWS credentials** – Configure credentials
  on your workstation using the `aws configure` command or the `aws
 login` command. For more information, see [Setting up the
  AWS CLI](../../../cli/latest/userguide/getting-started-quickstart.md "../../../cli/latest/userguide/getting-started-quickstart.md") in the _AWS Command Line Interface User Guide_.
- **IAM permissions** – (Optional) To
  reduce the scope of permissions your credentials have, you can use an AWS Identity and Access Management
  (IAM) policy that only grants the following permissions on the Amazon S3 bucket and the
  channel prefix you use (for example, `/Conda/*`):

  - `s3:GetObject`
  - `s3:PutObject`
  - `s3:DeleteObject`
  - `s3:ListBucket`
  - `s3:GetBucketLocation`

## Publishing a package to an Amazon S3 channel

Use `rattler-build publish` with an `s3://` target to publish a
package to your Amazon S3 conda channel. If the channel does not exist in the bucket,
`rattler-build` initializes the channel automatically. Before you begin, make
sure that you have completed the [prerequisites](#publish-s3-prereqs "#publish-s3-prereqs").

The following example publishes the Blender 4.5 sample recipe from the
[Deadline Cloud samples](https://github.com/aws-deadline/deadline-cloud-samples "https://github.com/aws-deadline/deadline-cloud-samples")
repository on GitHub. You can substitute a different recipe from the samples
repository or use your own recipe.

###### Note

Large applications can require tens of GB of free disk space for the source archive,
extracted files, and build output. Make sure that you use a disk with enough available
space for the package build output.

###### To publish a package to an Amazon S3 channel

1. Clone the Deadline Cloud samples repository.

```
git clone https://github.com/aws-deadline/deadline-cloud-samples.git
```

2. Change to the `conda_recipes` directory.

```
cd deadline-cloud-samples/conda_recipes
```

3. Run the following command. Replace `amzn-s3-demo-bucket`
   with your bucket name.

```
rattler-build publish blender-4.5/recipe/recipe.yaml --to s3://amzn-s3-demo-bucket/Conda/Default --build-number=+1
```

The `/Conda/Default` prefix organizes the channel within the bucket. You
can use a different prefix, but the prefix must be consistent across all commands and
queue configurations that reference the channel.

###### About build numbers

The `--build-number=+1` option automatically picks the next build number
based on what already exists in the destination channel. The best practice is to never
overwrite a package in a channel. Always build to a new build number if the package would
otherwise have the same filename. Using `--build-number=+1` achieves this when
you build to a production channel or a staging channel that mirrors production.

If you want to control the build number directly, you can set it with a specific value
such as `--build-number=7`. If you omit the option, `rattler-build`
uses the build number defined in the `recipe.yaml` file.

If your package recipe depends on packages from a particular channel, such as
[conda-forge](https://conda-forge.org/ "https://conda-forge.org/"), add `-c
 conda-forge` to the command.

You can also publish a package file that you already built, for example, a
`.conda` file from a local build. Replace
`amzn-s3-demo-bucket` with your bucket name.

```
rattler-build publish output/linux-64/blender-4.5.0-hb0f4dca_0.conda \
    --to s3://amzn-s3-demo-bucket/Conda/Default
```

## Initializing or reindexing a channel

When you use `rattler-build publish` to publish a package, the command
initializes the channel automatically if the channel does not already exist. In most cases,
you don't need to initialize or reindex the channel manually.

You might need to manually initialize or reindex a channel in the following
situations:

- You want to create an empty channel before publishing any packages, for example,
  to verify that your Deadline Cloud queue environment can connect to the channel.
- You uploaded or deleted `.conda` files directly with Amazon S3 tools
  instead of using `rattler-build publish`, and the channel index is out of
  date.

### Initializing an empty channel

To initialize an empty channel, create a `repodata.json` file and upload
it to the `noarch` subdirectory of the channel prefix. Replace
`amzn-s3-demo-bucket` with your bucket name.

```
echo '{"info":{"subdir":"noarch"},"packages":{},"packages.conda":{},"removed":[],"repodata_version":1}' > empty_channel_repodata.json
aws s3api put-object --body empty_channel_repodata.json --key Conda/Default/noarch/repodata.json --bucket `amzn-s3-demo-bucket`
```

The `/Conda/Default` prefix must match the channel prefix that your queue
environment uses. After you initialize the channel, you can publish packages to the
channel by using `rattler-build publish`.

### Reindexing a channel

If the channel index is out of date, use `rattler-index` to rebuild the
index from the package files in the channel. First, install
`rattler-index`.

```
pixi global install rattler-index
```

Then reindex the channel. Replace `amzn-s3-demo-bucket`
with your bucket name.

```
rattler-index s3 s3://amzn-s3-demo-bucket/Conda/Default
```

## Testing the package

After you publish the package, create a temporary pixi project to verify that the
package works correctly. The project installs the package from the Amazon S3 channel.

###### To test the package

1. Create a temporary test directory and initialize a pixi project with the Amazon S3
   channel. Replace `amzn-s3-demo-bucket` with your bucket
   name.

```
mkdir package-test-env
cd package-test-env
pixi init --channel s3://amzn-s3-demo-bucket/Conda/Default
```

2. Add the package to the project.

```
pixi add blender=4.5
```

3. Verify that the package works correctly.

```
pixi run blender --version
```

The [`pixi
 run`](https://pixi.sh/latest/reference/cli/pixi/run/ "https://pixi.sh/latest/reference/cli/pixi/run/") command activates the conda environment for the project directory
and runs the specified command within it. The environment persists in the project
directory, so you can use the same `pixi run` command from other
terminals.

## Removing packages from the channel

Avoid removing packages from channels that you use for production, because lockfiles
reference specific packages by hash. Removing a package prevents re-creating environments
from those lockfiles. For development and testing channels, you can remove a specific
package by deleting the `.conda` file from the bucket and then reindexing the
channel.

Delete the package file and then reindex the channel. Replace
`amzn-s3-demo-bucket` with your bucket name.

```
aws s3 rm s3://amzn-s3-demo-bucket/Conda/Default/linux-64/blender-4.5.0-hb0f4dca_1.conda
```

After you delete the file, reindex the channel to update the channel metadata. For
instructions, see [Reindexing a channel](#publish-s3-reindex "#publish-s3-reindex").

Package files are stored in platform-specific subdirectories such as
`linux-64`, `win-64`, or `osx-arm64`. To list the
packages in a subdirectory, run the following command.

```
aws s3 ls s3://amzn-s3-demo-bucket/Conda/Default/linux-64/
```

## Cleaning up

After testing, remove the test project directory.

###### To clean up test resources

- Remove the test project directory.

On Linux and macOS, run the following command.

```
rm -rf package-test-env
```

On Windows (cmd), run the following command.

```
rmdir /s /q package-test-env
```

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

## Building packages for other platforms

The `rattler-build publish` command builds packages for the operating system
of the workstation where the command runs. If your Deadline Cloud fleet uses a different operating
system than your workstation, or if your package has other host requirements, you have
the following options:

- Run `rattler-build publish` on a host that matches the target operating
  system. For example, use an Amazon Elastic Compute Cloud (Amazon EC2) instance running Linux to build
  packages for a Linux fleet.
- Use a Deadline Cloud package building queue to automate builds on the target platform. See
  [Create a package building queue](automate-package-builds.md#s3-channel-create-queue "automate-package-builds.md#s3-channel-create-queue").
- (Advanced) Use cross-compilation to build packages for a different platform from your
  workstation. For more information, see [Cross-compilation](https://rattler-build.prefix.dev/latest/compilers/#cross-compilation "https://rattler-build.prefix.dev/latest/compilers/#cross-compilation") in the rattler-build documentation.

## Next steps

After you publish packages to your Amazon S3 conda channel, configure your Deadline Cloud queues to
use the channel:

- [Configure production queue
  permissions for custom conda packages](configure-jobs-s3-channel.md#s3-channel-configure-permissions "configure-jobs-s3-channel.md#s3-channel-configure-permissions") – Grant your production queues
  read-only access to the Amazon S3 conda channel.
- [Add a conda channel to a queue
  environment](configure-jobs-s3-channel.md#s3-channel-add-channel "configure-jobs-s3-channel.md#s3-channel-add-channel") – Configure the queue environment to install packages from
  the Amazon S3 conda channel.
