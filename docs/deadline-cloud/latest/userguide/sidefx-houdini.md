# SideFX Houdini

###### Note

For more information about installing, configuring, and using this integration on your workstation, see the [Houdini integration user guide on GitHub](https://aws-deadline.github.io/houdini/ "https://aws-deadline.github.io/houdini/").

SideFX Houdini is a 3D procedural software for modeling, rigging, animation, VFX, look development, lighting and rendering in film, TV, advertising and video game pipelines. Houdini is fully supported by Deadline Cloud with comprehensive integration including submitters, conda packages, and an adaptor for increased rendering performance.

## Support overview

Houdini is supported by the following components:

- **Submitter**: Integrated render output node (ROP) for direct job submission from Houdini with automatic scene and asset detection.
- **Conda packages**: Deadline Cloud for automatic installation on service-managed fleets.
- **Adaptor**: Middleware for efficient rendering with sticky sessions and additional monitoring.
- **Cross-platform compatibility**: Submitter support for Windows, macOS, and Linux with worker support for Windows and Linux with automatic path mapping.

## Houdini version compatibility

The following table shows current support levels for Houdini versions:

| Major Version | Submitter Support     | Conda Support | Render Engines               | Usage-Based Licensing           |
| ------------- | --------------------- | ------------- | ---------------------------- | ------------------------------- |
| 19.0          | Windows, macOS, Linux | Linux         | Mantra, Karma CPU, Karma XPU | Usage-based licensing available |
| 19.5          | Windows, macOS, Linux | Linux         | Mantra, Karma CPU, Karma XPU | Usage-based licensing available |
| 20.0          | Windows, macOS, Linux | Linux         | Mantra, Karma CPU, Karma XPU | Usage-based licensing available |
| 20.5          | Windows, macOS, Linux | Linux         | Mantra, Karma CPU, Karma XPU | Usage-based licensing available |
| 21.0          | Windows, macOS, Linux | Linux         | Mantra, Karma CPU, Karma XPU | Usage-based licensing available |

## Deadline Cloud Conda Channel

The following table lists all conda packages applicable to Houdini available to Service-managed fleets in the deadline-cloud conda channel:

| OS    | Package        | Version | Notes                               |
| ----- | -------------- | ------- | ----------------------------------- |
| Linux | houdini        | 19.0    | Includes Mantra and Karma renderers |
| Linux | houdini        | 19.5    | Includes Mantra and Karma renderers |
| Linux | houdini        | 20.0    | Includes Mantra and Karma renderers |
| Linux | houdini        | 20.5    | Includes Mantra and Karma renderers |
| Linux | houdini        | 21.0    | Includes Mantra and Karma renderers |
| Linux | houdini-openjd |         | Includes the Houdini Adaptor        |

## Getting started

To use Houdini with Deadline Cloud:

1. Create a service-managed fleet and associate it with a queue. Your queue must be set up with a queue environment that supports the deadline-cloud conda channel. For more information, see [Creating a queue environment](create-queue-environment.md "create-queue-environment.md").
2. Install the Deadline Cloud monitor and Houdini submitter on your artist workstation using the Deadline Cloud Submitter and monitor installers. For more information, see [Set up your workstation](submitter.md "submitter.md").
3. Submit your job directly from Houdini using the integrated submitter to the queue.
4. Monitor the job and download the output using the Deadline Cloud monitor.

## Using the Houdini submitter

To use the Houdini submitter:

1. Open Houdini.
2. In the Network Editor, usually in the lower right side of Houdini, select the `/out` network.
3. Press **Tab**, and enter `deadline`.
4. Select the **Deadline Cloud** option and place it within the `/out` network to create the node.
5. Connect the output of the last render output node (ROP) (for example, Karma, Mantra, or compositing) in your existing `/out` network to the input of the Deadline Cloud node.
6. Choose the Deadline Cloud node.
7. Enter any job settings in the node editor, usually in the upper right side of Houdini.
8. In the bottom right of the node editor, choose **Submit**.

The Deadline Cloud submission will automatically parse the connected `/out` network tree and submit each node as a step in the job maintaining the dependency tree. Using non-default render networks other than `/out` is also supported.

## Advanced configurations

### Using unsupported versions

Deadline Cloud only supports and tests the workstation and worker software versions in the table above. When using the submitter, the worker will attempt to install the same version as used on the workstation. This may fail if the workstation version of Houdini does not appear in the version table above.

If you require an unsupported version of Houdini, you have the following options:

- When submitting the job from Houdini, you may override the CondaPackages queue parameter to specify a supported version to use on the worker (for example, `houdini=21.0, houdini-openjd=*`). This may or may not work, depending on the features used by your scene and how Houdini works with scenes from your workstation version.
- You may build a custom conda recipe and channel for your desired version to be installed on the worker. Use the conda recipe for a supported version linked below as a starting point, and package your desired version in a custom conda channel. For more information about creating custom conda channels, see [Creating custom conda channels](../developerguide/configure-jobs-s3-channel.md "../developerguide/configure-jobs-s3-channel.md").

## Houdini render engines

Houdini supports multiple render engines that are compatible with Deadline Cloud:

| Render Engine | Description                             | GPU Support     |
| ------------- | --------------------------------------- | --------------- |
| Karma CPU     | Modern USD-based renderer (CPU variant) | CPU-based       |
| Karma XPU     | Modern USD-based renderer (GPU variant) | GPU accelerated |
| Mantra        | Traditional Houdini renderer            | CPU-based       |
| Arnold        | Third-party Monte Carlo ray tracer      | GPU/CPU hybrid  |
| V-Ray         | Third-party photorealistic renderer     | GPU/CPU hybrid  |
| Redshift      | GPU-accelerated renderer                | GPU optimized   |

These render engines are automatically detected and configured by the Houdini integrated submitter and usage is automatically licensed. The submitter maintains dependency trees between connected render output nodes (ROPs).

## Open source resources

The submitter and adaptor are open source and available on GitHub. Houdini Conda recipes are available on GitHub for supported versions.

- [Houdini submitter source code on GitHub](https://github.com/aws-deadline/deadline-cloud-for-houdini "https://github.com/aws-deadline/deadline-cloud-for-houdini")
- [Sample scenes and workflows on GitHub](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/houdini_husk_usd_render "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/houdini_husk_usd_render")
- [Conda recipes for supported versions on GitHub](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-21.0 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-21.0")
