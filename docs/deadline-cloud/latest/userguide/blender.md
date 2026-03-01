# Blender

###### Note

For more information about installing, configuring, and using this integration on your workstation, see the [Blender integration user guide on GitHub](https://aws-deadline.github.io/blender/ "https://aws-deadline.github.io/blender/").

Blender is a free and open-source 3D computer graphics software toolset used for creating animated films, visual effects, art, 3D printed models, motion graphics, interactive 3D applications, virtual reality, and computer games. Blender is supported by Deadline Cloud with comprehensive integration including submitters, conda packages, and an adaptor for increased rendering performance.

## Support overview

Blender is supported by the following components:

- **Submitter**: Integrated submitter for direct job submission from Blender with automatic scene and asset detection.
- **Conda packages**: Deadline Cloud for automatic installation on service-managed fleets.
- **Adaptor**: Middleware for efficient rendering with sticky sessions and additional monitoring.
- **Cross-platform compatibility**: Submitter support for Windows, macOS, and Linux with worker support for Windows and Linux with automatic path mapping.

## Blender version compatibility

The following table shows current support levels for Blender versions:

| Major Version | Submitter Support     | Conda Support | Render Engines           |
| ------------- | --------------------- | ------------- | ------------------------ |
| 3.6           | Windows, macOS, Linux | Linux         | Cycles, Eevee, Workbench |
| 4.2           | Windows, macOS, Linux | Linux         | Cycles, Eevee, Workbench |
| 4.5           | Windows, macOS, Linux | Linux         | Cycles, Eevee, Workbench |

## Getting started

To use Blender with Deadline Cloud:

1. Create a service-managed fleet and associate it with a queue. Your queue must be set up with a queue environment that supports the deadline-cloud conda channel. For more information, see [Creating a queue environment](create-queue-environment.md "create-queue-environment.md").
2. Install the Deadline Cloud monitor and Blender submitter on your artist workstation using the Deadline Cloud monitor and submitter installers. For more information, see [Set up your workstation](submitter.md "submitter.md").
3. Submit your job directly from Blender using the integrated submitter to the queue.
4. Monitor the job and download the output using the Deadline Cloud monitor.

For more information about using the Blender integrated submitter, see the [Blender integration user guide on GitHub](https://aws-deadline.github.io/blender/ "https://aws-deadline.github.io/blender/").

## Using the Blender submitter

To submit a render job from Blender:

1. Open Blender and load your scene file.
2. Configure your render settings including output path, frame range, and render engine (Cycles, Eevee, or Workbench).
3. From the top menu, select **Render** > **Deadline Cloud**.
4. In the Deadline Cloud submission dialog:
   - Enter a job name and description.
   - Select your target farm and queue.
   - Configure job attachments to include your scene file and any external assets.
   - Review render settings and frame range.

5. Choose **Submit** to send your job to the queue.

The Deadline Cloud submission will automatically detect your scene dependencies, configure the appropriate render engine, and submit the job with the correct conda packages for your Blender version.

## Advanced configurations

### Using unsupported versions

Deadline Cloud only supports and tests the workstation and worker software versions in the table above. When using the submitter, the worker will attempt to install the same version as used on the workstation. This will fail if the workstation version of Blender does not appear in the version table above.

If you require an unsupported version of Blender, you have the following options:

- When submitting the job from Blender, you may override the CondaPackages queue parameter to specify a supported version to use on the worker (for example, `blender=4.5, blender-openjd=*`). This may or may not work, depending on the features used by your scene and how Blender works with scenes from your workstation version.
- You may build a custom conda recipe and channel for your desired version to be installed on the worker. Use the conda recipe for a supported version linked below as a starting point, and package your desired version in a custom conda channel. For more information about creating custom conda channels, see [Creating custom conda channels](../developerguide/configure-jobs-s3-channel.md "../developerguide/configure-jobs-s3-channel.md").

## Blender render engines

Blender includes several built-in render engines that are supported:

| Render Engine | Description                  | GPU Support    | Notes                                              |
| ------------- | ---------------------------- | -------------- | -------------------------------------------------- |
| Cycles        | Physically-based path tracer | GPU/CPU hybrid | Production quality rendering with GPU acceleration |
| Eevee         | Real-time render engine      | GPU optimized  | Fast viewport and final rendering                  |
| Workbench     | Solid shading engine         | GPU optimized  | For modeling and sculpting workflows               |

All render engines are automatically detected and configured by the Blender integrated submitter. GPU acceleration is available when using service-managed fleets with GPU-enabled instances.

## Deadline Cloud Conda Channel

The following table lists all conda packages applicable to Blender available to Service-managed fleets in the deadline-cloud conda channel:

| OS    | Package        | Version | Notes                                |
| ----- | -------------- | ------- | ------------------------------------ |
| Linux | blender        | 3.6     | Includes all built-in render engines |
| Linux | blender        | 4.2     | Includes all built-in render engines |
| Linux | blender        | 4.5     | Includes all built-in render engines |
| Linux | blender-openjd |         | Includes the Blender Adaptor         |

## Open source resources

The submitter and adaptor are open source and available on GitHub:

- [Deadline Cloud for Blender](https://github.com/aws-deadline/deadline-cloud-for-blender "https://github.com/aws-deadline/deadline-cloud-for-blender")
- [Blender Conda recipes](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.5 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.5") are available on GitHub for supported versions.
