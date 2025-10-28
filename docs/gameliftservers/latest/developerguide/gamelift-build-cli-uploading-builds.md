# Create a Amazon GameLift Servers build resource for

managed hosting

When creating a build and uploading your files, you have a couple of options:

- [Create a build from a
  file directory](gamelift-build-cli-uploading-upload-build.md "gamelift-build-cli-uploading-upload-build.md"). This is the
  simplest and most commonly used option.
- [Create a build with
  files in Amazon Simple Storage Service (Amazon S3)](gamelift-build-cli-uploading-create-build.md "gamelift-build-cli-uploading-create-build.md"). With this option, you can manage your build
  versions in Amazon S3.
  With both methods, Amazon GameLift Servers creates a new build resource with a unique build ID and other
  metadata. The build starts in the **Initialized** status. After Amazon GameLift Servers
  acquires the game server files, the build moves to **Ready** status.

When the build is ready, you can deploy it to a new Amazon GameLift Servers fleet. For more information,
see [Create an Amazon GameLift Servers managed EC2 fleet](fleets-creating.md "fleets-creating.md").When Amazon GameLift Servers sets up
the new fleet, it downloads the build files to each fleet instance and installs the
build files.
