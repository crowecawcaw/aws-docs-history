# Foundry Nuke

###### Note

For more information about installing, configuring, and using this integration on your workstation, see the [Nuke integration user guide on GitHub](https://aws-deadline.github.io/nuke/ "https://aws-deadline.github.io/nuke/").

Foundry Nuke is a node-based digital compositing and visual effects application used for television and film post-production. Nuke is supported by Deadline Cloud with submitters, conda packages, and an adaptor for increased rendering performance.

## Support overview

Nuke is supported by the following components:

- **Submitter**: Integrated submitter plugin for direct job submission from Nuke with automatic scene and asset detection.
- **Conda packages**: Packages to install nuke versions 15, 16, and 17 are available on the Deadline Cloud conda channel for service-managed fleets.
- **Adaptor**: Middleware for efficient rendering with sticky sessions and additional monitoring.
- **Cross-platform compatibility**: Submitter support for Windows, macOS, and Linux with worker support for Linux only with automatic path mapping.

## Nuke version compatibility

The following table shows current support levels for Nuke versions:

| Major Version | Submitter Support     | Conda Support |
| ------------- | --------------------- | ------------- |
| 15            | Windows, macOS, Linux | Linux         |
| 16            | Windows, macOS, Linux | Linux         |
| 17            | Windows, macOS, Linux | Linux         |

## Deadline Cloud Conda Channel

The following table lists conda packages applicable to Nuke available to Service-managed fleets in the deadline-cloud conda channel:

| OS    | Package     | Version | Notes                                |
| ----- | ----------- | ------- | ------------------------------------ |
| Linux | nuke        | 15      | Includes built-in compositing engine |
| Linux | nuke        | 16      | Includes built-in compositing engine |
| Linux | nuke        | 17      | Includes built-in compositing engine |
| Linux | nuke-openjd |         | Includes the Nuke Adaptor            |

## Getting started

To use Nuke with Deadline Cloud:

1. Create a service-managed fleet and associate it with a queue. Your queue must be set up with a queue environment that supports the deadline-cloud conda channel. For more information, see [Creating a queue environment](create-queue-environment.md "create-queue-environment.md").
2. Install the Deadline Cloud monitor and Nuke submitter on your artist workstation using the Deadline Cloud Submitter and monitor Installers. For more information, see [Set up your workstation](submitter.md "submitter.md").
3. Submit your job directly from Nuke using the integrated submitter to the queue.
4. Monitor the job and download the output using the Deadline Cloud monitor.

### Launch the submitter

###### To launch the Deadline Cloud submitter in Nuke

###### Note

Support for Nuke is provided using the Conda environment for service-managed fleets. For more information, see [Default conda queue environment](create-queue-environment.md#conda-queue-environment "create-queue-environment.md#conda-queue-environment").

1. Install the Deadline Cloud monitor and Nuke submitter on your artist workstation using the Deadline Cloud Submitter and monitor Installers. For more information, see [Set up your workstation](submitter.md "submitter.md").
2. Open **Nuke**.
3. Open a Nuke script with dependencies that exist within the asset root directory.
4. Choose **AWS Deadline**, and then choose **Submit to Deadline Cloud** to launch the submitter.
   1. If you are not already authenticated in the Deadline Cloud submitter, the **Credentials Status** shows as **NEEDS_LOGIN**.
   2. Choose **Login**.
   3. In the login browser window, log in with your user credentials.
   4. Choose **Allow**. You are now logged in and the **Credentials Status** shows as **AUTHENTICATED**.

5. Choose **Submit**.

## Using the Nuke submitter

To use the Nuke submitter:

1. Open Nuke.
2. Load your composition with the required Write nodes configured.
3. From the menu, choose **Deadline Cloud** to launch the submitter.
4. If you are not already authenticated, choose **Login** and authenticate with your credentials.
5. Configure your job settings in the submitter interface, including:
   - Frame range settings
   - Write node selection
   - Output paths and formats

6. Choose **Submit** to send your job to Deadline Cloud.

The submitter automatically detects Write nodes in your composition and allows you to select which ones to render. It also handles automatic input/output path detection and supports multiple views rendering.

## Advanced configurations

### Using unsupported versions

Deadline Cloud only supports and tests the workstation and worker software versions in the table above. When using the submitter, the worker will attempt to install the same version as used on the workstation. This will fail if the workstation version of Nuke does not appear in the version table above.

If you require an unsupported version of Nuke, you have the following options:

- When submitting the job from Nuke, you can override the CondaPackages queue parameter to specify a supported version to use on the worker (for example, `nuke=17, nuke-openjd=*`). This might or might not work, depending on the features used by your composition and how Nuke works with compositions from your workstation version.
- You can build a custom conda recipe and channel for your desired version to be installed on the worker. Use the conda recipe for a supported version linked below as a starting point, and package your desired version in a custom conda channel. For more information about creating custom conda channels, see [Creating custom conda channels](../developerguide/configure-jobs-s3-channel.md "../developerguide/configure-jobs-s3-channel.md").

### Custom Nuke executable

You can set the `NUKE_EXECUTABLE` environment variable to point to a specific Nuke executable if it's not available on the PATH.

### OpenColorIO support

The Nuke integration includes full support for OpenColorIO (OCIO) color management workflows. Color configurations are automatically detected and included with job submissions to ensure consistent color handling across the render farm.

## Nuke compositing features

Nuke's compositing engine provides comprehensive support for:

| Feature          | Description                        | Notes                                    |
| ---------------- | ---------------------------------- | ---------------------------------------- |
| Write Nodes      | Multiple output formats and codecs | Automatically detected by submitter      |
| Frame Ranges     | Custom frame range specification   | Supports override and default ranges     |
| Multiple Views   | Stereo and multi-view rendering    | Proper handling of view-specific outputs |
| Color Management | OpenColorIO integration            | Automatic OCIO configuration detection   |
| Path Mapping     | Cross-platform path translation    | Seamless Windows/Linux compatibility     |
| CopyCat          | ML-based paint and rotoscoping     | Requires Nuke 14.0 or later              |

Compositing features are automatically detected and configured by the Nuke integrated submitter. The submitter maintains proper dependency handling and asset management for complex compositions.

## Open source resources

The submitter and adaptor are open source and available on GitHub:

- [Deadline Cloud for Nuke](https://github.com/aws-deadline/deadline-cloud-for-nuke "https://github.com/aws-deadline/deadline-cloud-for-nuke")
- [Nuke Conda recipes](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes") are available on GitHub for supported versions.
