# Autodesk VRED

###### Note

For more information about installing, configuring, and using this integration on your workstation, see the [VRED integration user guide on GitHub](https://aws-deadline.github.io/vred/ "https://aws-deadline.github.io/vred/").

Autodesk VRED is a professional 3D visualization and virtual prototyping software that brings complex 3D data to life in a realistic virtual environment. This software is widely used by designers and engineers to create product presentations, design reviews, and virtual prototypes, particularly in the automotive industry.

## Support overview

VRED is partially supported by Deadline Cloud with the following components:

- **Submitters**: Integrated submitters for direct job submission from VRED Pro with automatic scene and asset detection.
- **Conda packages**: Automatic installation on service-managed fleets for Linux workers using the vredcore package.
- **Cross-platform compatibility**: Submitter support for Windows with worker support for Linux with automatic path mapping. (VRED Conda packages are available for Linux only; Windows workers require manual installation.)
- **BYOL Licensing**: VRED requires Bring Your Own License (BYOL). Unlike some other DCC applications in Deadline Cloud, usage-based licensing is not available for VRED. You must have valid VRED licenses available for your render farm fleet and configure your license server to be accessible from your workers.

## VRED version compatibility

The following table shows current support levels for VRED versions:

| Major Version | Submitter Support | Conda Support | Usage-Based Licensing |
| ------------- | ----------------- | ------------- | --------------------- |
| 2026          | Windows           | Linux         | BYOL required         |
| 2025          | Windows           | Linux         | BYOL required         |

## Deadline Cloud Conda Channel

The following table lists all conda packages applicable to VRED available to Service-managed fleets in the deadline-cloud conda channel:

| OS    | Package  | Version | Notes               |
| ----- | -------- | ------- | ------------------- |
| Linux | vredcore | 2025    | VRED Core for Linux |
| Linux | vredcore | 2026    | VRED Core for Linux |

## Requirements

To use VRED with Deadline Cloud, you need:

- VRED Pro or VRED Core 2025/2026 with valid licensing
- Python 3.11 or higher
- NVIDIA GPU driver 553.xx (recommended for optimal performance)
- Valid VRED licenses accessible from your render farm fleet
- Optionally: ImageMagick static binary for tile assembly when using region rendering with raytracing

###### Important

VRED integration requires **bring your own licensing (BYOL)**. You must have valid VRED licenses available for your render farm fleet and configure your license server to be accessible from worker nodes. For more information, see [Connect service-managed fleets to a custom license server](../developerguide/smf-byol.md "../developerguide/smf-byol.md").

## Getting started

To use VRED with Deadline Cloud:

1. Create a service-managed fleet and associate it with a queue. Ensure your fleet has access to your VRED license server.
2. Install the Deadline Cloud monitor and VRED submitter on your artist workstation using the Deadline Cloud Submitter and monitor installers. For more information, see [Set up your workstation](submitter.md "submitter.md").
3. Open VRED and load your scene file.
4. Submit your job directly from VRED using the integrated submitter by selecting **Deadline Cloud** > **Submit to Deadline Cloud** from the menu.
5. Monitor the job and download the output using the Deadline Cloud monitor.

## Advanced configuration

### Using unsupported versions

Deadline Cloud only supports and tests the workstation and worker software versions in the table above. When using the submitter, the worker will attempt to install the same version as used on the workstation. This will fail if the workstation version of VRED does not appear in the version table above.

If you require an unsupported version of VRED, you may build a custom Conda recipe and channel for your desired version to be installed on the worker. Use the Conda recipe for a supported version linked below as a starting point and package your desired version in a custom conda channel. For more information about creating custom Conda channels, see [Creating custom conda channels](../developerguide/configure-jobs-s3-channel.md "../developerguide/configure-jobs-s3-channel.md").

## Open source resources

The submitter and adaptor are open source and available on GitHub:

- [VRED Submitter and Adaptor](https://github.com/aws-deadline/deadline-cloud-for-vred "https://github.com/aws-deadline/deadline-cloud-for-vred")
- [VRED Conda recipes](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/vredcore-2026 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/vredcore-2026") are available on GitHub for supported versions.
