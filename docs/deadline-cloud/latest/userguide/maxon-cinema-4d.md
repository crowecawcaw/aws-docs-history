# Maxon Cinema 4D

###### Note

For more information about installing, configuring, and using this integration on your workstation, see the [Cinema 4D integration user guide on GitHub](https://aws-deadline.github.io/cinema-4d/ "https://aws-deadline.github.io/cinema-4d/").

Cinema 4D is a professional 3D animation, modeling, simulation and rendering software solution from Maxon. Cinema 4D is supported by Deadline Cloud including a submitter, conda packages, usage-based licensing and an adaptor for improved performance.

## Support overview

Cinema 4D is supported by the following components:

- **Submitter**: Integrated submitter for direct job submission from Cinema 4D with automatic scene and asset detection.
- **Conda packages**: Automatic installation on service-managed fleets when using the submitter.
- **Adaptor**: Middleware for more efficient rendering with sticky sessions and additional monitoring.
- **Cross-platform compatibility**: Submitter support for Windows and macOS with worker support for Windows and Linux with automatic path mapping.
- **Usage-based Licensing**: Pay-as-you-go licensing for Cinema 4D, Redshift, and Red Giant licensing.

## Cinema 4D version compatibility

The following table shows current support levels for Cinema 4D versions:

| Major Version | Submitter Support | Conda Support  | Usage-Based Licensing           |
| ------------- | ----------------- | -------------- | ------------------------------- |
| 2024          | Windows, macOS    | Windows        | Usage-based licensing available |
| 2025          | Windows, macOS    | Windows, Linux | Usage-based licensing available |
| 2026          | Windows, macOS    | Windows, Linux | Usage-based licensing available |

## Deadline Cloud Conda Channel

The following table lists all conda packages applicable to Cinema 4D available to Service-managed fleets in the deadline-cloud conda channel:

| OS             | Package         | Version | Notes                                              |
| -------------- | --------------- | ------- | -------------------------------------------------- |
| Windows        | cinema4d        | 2024    | Includes Standard, Physical and Redshift renderers |
| Windows, Linux | cinema4d        | 2025    | Includes Standard, Physical and Redshift renderers |
| Windows, Linux | cinema4d        | 2026    | Includes Standard, Physical and Redshift renderers |
| Windows, Linux | cinema4d-c4dtoa | 2025    | Cinema4D to Arnold                                 |
| Windows        | cinema4d-c4dtoa | 2026    | Cinema4D to Arnold                                 |
| Windows, Linux | cinema4d-openjd |         | Includes the Cinema 4D Adaptor                     |

###### Note

For **Cinema 4D**, the Linux conda package does not
support substance 3D materials. Jobs with this material fail with one of the following errors:

```
Commandline: ./modules/io_substance/source/substance_framework/src/details/detailsengine.cpp:794: SubstanceAir::Details::Engine::Context::Context(SubstanceAir::Details::Engine&, SubstanceAir::RenderCallbacks*): Assertion `res==0' failed.
```

```
/home/job-user/.conda/envs/<hash>/Lib/deadline/cinema4d_adaptor/Cinema4DAdaptor/adaptor.sh: line 44: 10832 Segmentation fault      (core dumped) $C4DEXE ${ARGS[*]}
```

We recommend that you submit jobs with substance materials to Windows instead.

In Cinema 4D 2025.3.3 on Linux, globalized asset paths can cause segmentation faults.
Therefore, the Linux conda package contains Cinema 4D 2025.3.1 with Redshift 2025.6.0 instead.
If you need features or bug fixes from Cinema 4D 2025.3.3, we recommend two options: upgrade
to Cinema 4D 2026 or submit those jobs to Windows instead.

For **Cinema 4D OpenJD,** to prevent any timeout issues,
we recommend you set task run timeouts to double their expected render time,
instead of using the default 2 day timeout.

## Getting started

To use Cinema 4D fully-managed on Deadline Cloud:

1. Create a service-managed fleet and associate it with a queue. Configure the fleet with GPU support if you intend to use Redshift or Red Giant features that require a GPU. Your queue should be set up with a queue environment that supports the deadline-cloud conda channel. For more information, see [Creating a queue environment](create-queue-environment.md "create-queue-environment.md").
2. Install the Deadline Cloud monitor and Cinema 4D submitter on your artist workstation using the Deadline Cloud Submitter and monitor Installers. For more information, see [Set up your workstation](submitter.md "submitter.md").
3. Submit your job directly from Cinema 4D using the integrated submitter to the queue.
4. Monitor the job and download the output using the Deadline Cloud monitor.

For more information about using the Cinema 4D integrated submitter, see the [Cinema 4D integration user guide on GitHub](https://aws-deadline.github.io/cinema-4d/ "https://aws-deadline.github.io/cinema-4d/").

## Advanced configurations

### Using unsupported versions

Deadline Cloud only supports and tests the workstation and worker software versions in the table above. When using the submitter, the worker will attempt to install the same version as used on the workstation. This will fail if the workstation version of Cinema 4D does not appear in the version table above.

If you require an unsupported version of Cinema 4D, you may build a custom conda recipe and channel for your desired version to be installed on the worker. Use the conda recipe for a supported version linked in the Open Source Resources section below as a starting point, and package your desired version in a custom conda channel. For more information about creating custom conda channels, see [Creating custom conda channels](../developerguide/configure-jobs-s3-channel.md "../developerguide/configure-jobs-s3-channel.md").

If you create a conda package for a different version of Cinema 4D, you should ensure it will acquire a license correctly. If the version is compatible with licensing for a supported version in the table above, then usage-based licensing will work automatically. You may also bring your own license to a service-managed fleet by following [Connect service-managed fleets to a custom license server](../developerguide/smf-byol.md "../developerguide/smf-byol.md").

## Cinema 4D plugins

| Plugin               | Plugin Version | Conda Recipe Provided | SMF Conda Package Provided | Usage-based Licensing Support |
| -------------------- | -------------- | --------------------- | -------------------------- | ----------------------------- |
| Redshift             | 2026.3.0       | Bundled\*             | Yes                        | Yes                           |
| Redshift             | 2025.6.0       | Bundled\*             | Yes                        | Yes                           |
| Red Giant            | 2025.x         | No                    | No                         | Yes                           |
| V-Ray                | 7.x            | Yes                   | No                         | Yes                           |
| Insydium X-Particles | 2024.x         | Yes                   | No                         | N/A                           |
| C4DtoArnold          | 4.8.4.1        | Yes                   | Yes                        | Yes                           |

\*Included in the base Cinema 4D package recipe

### Maxon Redshift

The Redshift renderer is included with all Cinema 4D conda packages and is automatically used when appropriate when using the Cinema 4D integrated submitter. An additional licensing cost applies when using Redshift for rendering. For more information about Deadline Cloud pricing, see [Deadline Cloud pricing](https://aws.amazon.com/deadline-cloud/pricing/ "https://aws.amazon.com/deadline-cloud/pricing/").

### Maxon Red Giant

Red Giant is a comprehensive toolkit designed for video post-production, motion graphics, and visual effects. It offers rich color grading, smooth transitions, realistic visual effects, motion design templates and tools to create and edit your visuals. For more information, see [Red Giant](https://www.maxon.net/en/red-giant "https://www.maxon.net/en/red-giant").

Red Giant requires custom setup on service-managed fleets. A host configuration script is provided which you can use in your Deadline Cloud fleet. Once configured, Red Giant is supported by Deadline Cloud Usage-based Licensing and requires no further configuration to operate.

### V-Ray Plugin

V-Ray is a 3D photorealistic ray-traced rendering plug-in. V-Ray for Cinema 4D is not currently fully supported in Service-managed fleets. A conda recipe is provided which you can use to create your own Conda channel for use in your Deadline Cloud farm. For more information about creating custom conda channels, see [Creating custom conda channels](../developerguide/configure-jobs-s3-channel.md "../developerguide/configure-jobs-s3-channel.md"). Once installed, V-Ray is supported by Deadline Cloud Usage-based Licensing and requires no further configuration to operate.

### C4DToArnold

Autodesk Arnold software is an advanced Monte Carlo ray tracing renderer. For more information, see [Arnold](https://www.autodesk.com/in/products/arnold/overview "https://www.autodesk.com/in/products/arnold/overview"). C4DToArnold is fully supported in Service-managed fleets.

### Insydium X-Particles

X-Particles is a fully-featured advanced particle and VFX system for Maxon's Cinema 4D. For more information, see [X-Particles](https://insydium.ltd/products/x-particles/ "https://insydium.ltd/products/x-particles/"). Insydium X-Particles is not currently fully supported in Service-managed fleets. A conda recipe is provided which you can use to create your own Conda channel for use in your Deadline Cloud farm. For more information about creating custom conda channels, see [Creating custom conda channels](../developerguide/configure-jobs-s3-channel.md "../developerguide/configure-jobs-s3-channel.md"). When you create the conda package from your X-Particles package, it will include your purchased license. No additional configuration is necessary to operate on service-managed fleets.

## Open source resources

The submitter and adaptor are open source and available on GitHub:

- [Deadline Cloud for Cinema 4D](https://github.com/aws-deadline/deadline-cloud-for-cinema-4d "https://github.com/aws-deadline/deadline-cloud-for-cinema-4d")
- [Cinema 4D Conda recipes](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes") are available on GitHub for C4D 2024, C4D 2025, the INSYDIUM X-PARTICLES plugin, the C4DtoA plugin, and the V-Ray Plugin.
- [Host Configuration script](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/cinema4d/cinema4d_redgiant "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/cinema4d/cinema4d_redgiant") is included to support Red Giant plugins.
