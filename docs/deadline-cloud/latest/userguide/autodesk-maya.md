# Autodesk Maya

###### Note

For more information about installing, configuring, and using this integration on your workstation, see the [Maya integration user guide on GitHub](https://aws-deadline.github.io/maya/ "https://aws-deadline.github.io/maya/").

Autodesk Maya is a 3D computer animation, modeling, simulation, and rendering software used for creating interactive 3D applications, including video games, animated films, TV series, and visual effects. Maya is fully supported by Deadline Cloud with comprehensive integration including submitters, conda packages, usage-based licensing, and an adaptor for increased rendering performance.

## Support overview

Maya is supported by the following components:

- **Submitter**: Integrated plug-in for direct job submission from Maya.
- **Conda packages**: Automatic installation on service-managed fleets when using the submitter.
- **Adaptor**: Middleware for efficient rendering with sticky sessions and additional monitoring.
- **Cross-platform compatibility**: Submitter support for Windows, macOS, and Linux with worker support for Windows and Linux.
- **Usage-based Licensing**: Pay-as-you-go for Maya and renderer licensing.

## Maya version compatibility

The following table shows current support levels for Maya versions:

| Major Version | Submitter Support     | Conda Support | Render Engines                                | Usage-Based Licensing           |
| ------------- | --------------------- | ------------- | --------------------------------------------- | ------------------------------- |
| 2024          | Windows, macOS, Linux | Linux         | Maya Software, Arnold (MtoA)                  | Usage-based licensing available |
| 2025          | Windows, macOS, Linux | Linux         | Maya Software, Arnold (MtoA), V-Ray, Redshift | Usage-based licensing available |
| 2026          | Windows, macOS, Linux | Linux         | Maya Software, Arnold (MtoA), V-Ray, Redshift | Usage-based licensing available |

## Getting started

To use Maya with Deadline Cloud:

1. Create a service-managed fleet and associate it with a queue. Your queue must be set up with a queue environment that supports the deadline-cloud conda channel. For more information, see [Creating a queue environment](create-queue-environment.md "create-queue-environment.md").
2. Install the Deadline Cloud monitor and Maya submitter on your artist workstation using the Deadline Cloud Submitter and monitor Installers. For more information, see [Set up your workstation](submitter.md "submitter.md").
3. Submit your job directly from Maya using the integrated submitter to the queue.
4. Monitor the job and download the output using the Deadline Cloud monitor.

## Advanced configurations

### Using unsupported versions

Deadline Cloud only supports and tests the workstation and worker software versions in the table above. When using the submitter, the worker will attempt to install the same version as used on the workstation. This will fail if the workstation version of Maya does not appear in the version table above.

If you require an unsupported version of Maya, you have the following options:

- When submitting the job from Maya, you may override the CondaPackages queue parameter to specify a supported version to use on the worker (for example, `maya=2026, maya-openjd=*`). This may or may not work, depending on the features used by your scene and how Maya works with scenes from your workstation version.
- You may build a custom conda recipe and channel for your desired version to be installed on the worker. Use the conda recipes for supported versions as a starting point:

      + [Maya conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2026 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2026")
      + [Maya OpenJD adaptor conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-openjd "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-openjd")

  For more information about creating custom conda channels, see [Creating custom conda channels](../developerguide/configure-jobs-s3-channel.md "../developerguide/configure-jobs-s3-channel.md").

## Maya render engines

Maya supports multiple render engines that are fully compatible with Deadline Cloud:

| Render Engine | Description                         | GPU Support    | Notes                                              | Usage-Based Licensing   |
| ------------- | ----------------------------------- | -------------- | -------------------------------------------------- | ----------------------- |
| Maya Software | Built-in CPU renderer               | CPU-based      | Legacy renderer with basic features                | Included with Maya      |
| Arnold (MtoA) | Monte Carlo ray tracer              | GPU/CPU hybrid | Production quality rendering, MtoA 5.3.5+ required | Available for 2024-2026 |
| V-Ray         | Third-party photorealistic renderer | GPU/CPU hybrid | Requires separate licensing                        | Available for 2025-2026 |
| Redshift      | GPU-accelerated renderer            | GPU optimized  | Requires separate licensing                        | Available for 2025-2026 |

All render engines are automatically detected and configured by the Maya integrated submitter. The submitter maintains proper dependency handling and scene file management.

## Maya plugins

| Plugin        | Plugin Versions              | Conda Recipe Provided | SMF Conda Package Provided | Usage-based Licensing Support |
| ------------- | ---------------------------- | --------------------- | -------------------------- | ----------------------------- |
| Arnold (MtoA) | 2024.5.3, 2025.5.4, 2026.5.5 | Yes                   | Yes                        | Yes                           |
| V-Ray         | 2025.7, 2026.7               | Yes                   | Yes                        | Yes                           |
| Redshift      | 2025.4, 2026.2.1             | Yes                   | Yes                        | Yes                           |

### Arnold for Maya (MtoA)

Arnold is supported using the maya-mtoa conda package and is automatically installed when using the Maya integrated submitter. An additional licensing cost applies when using Arnold for rendering.

Conda recipe: [maya-mtoa conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-mtoa "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-mtoa")

### V-Ray Plugin

V-Ray is supported using the maya-vray conda package and is automatically installed when using the Maya integrated submitter. An additional licensing cost applies when using V-Ray for rendering.

Conda recipe: [maya-vray conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-vray "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-vray")

### Redshift Plugin

Redshift is supported using the maya-redshift conda package and is automatically installed using the Maya integrated submitter. An additional licensing cost applies when using Redshift for rendering.

Conda recipe: [maya-redshift conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-redshift "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-redshift")

## Deadline Cloud Conda Channel

The following table lists all conda packages applicable to Maya available to Service-managed fleets in the deadline-cloud conda channel:

| OS    | Package       | Version  | Notes                           |
| ----- | ------------- | -------- | ------------------------------- |
| Linux | maya          | 2024     | Includes Maya Software renderer |
| Linux | maya          | 2025     | Includes Maya Software renderer |
| Linux | maya          | 2026     | Includes Maya Software renderer |
| Linux | maya-mtoa     | 2024.5.3 | Arnold for Maya 2024            |
| Linux | maya-mtoa     | 2025.5.4 | Arnold for Maya 2025            |
| Linux | maya-mtoa     | 2026.5.5 | Arnold for Maya 2026            |
| Linux | maya-openjd   |          | Includes the Maya Adaptor       |
| Linux | maya-redshift | 2025.4   | Redshift for Maya 2025          |
| Linux | maya-redshift | 2026.2.1 | Redshift for Maya 2026          |
| Linux | maya-vray     | 2025.7   | V-Ray for Maya 2025             |
| Linux | maya-vray     | 2026.7   | V-Ray for Maya 2026             |

## Open source resources

The submitter and adaptor are open source and available on GitHub:

- [Maya submitter source code](https://github.com/aws-deadline/deadline-cloud-for-maya "https://github.com/aws-deadline/deadline-cloud-for-maya")
- [Maya conda recipes](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2026 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2026")
