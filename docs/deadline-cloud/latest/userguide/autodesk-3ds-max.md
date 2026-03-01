# Autodesk 3ds Max

###### Note

For more information about installing, configuring, and using this integration on your
workstation, see the [Autodesk 3ds Max
integration user guide on GitHub](https://aws-deadline.github.io/3ds-max/ "https://aws-deadline.github.io/3ds-max/").

###### Note

When using Autodesk 3ds Max with AWS Deadline Cloud, you can use Autodesk cloud rights included with your subscription. For more information about cloud rights and subscription benefits, see [Subscription Benefits FAQ: Cloud Rights](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Subscription-Benefits-FAQ-Cloud-Rights.html "https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Subscription-Benefits-FAQ-Cloud-Rights.html") on the Autodesk website.

Autodesk 3ds Max is a professional 3D computer graphics program for creating 3D animations, models, games, and images. Deadline Cloud provides comprehensive support for 3ds Max with integrated submitters, host configuration scripts, usage-based licensing, and adaptors for increased rendering performance.

## Support overview

3ds Max is supported by the following components:

- **Submitter**: Integrated submitter for direct job submission from 3ds Max with automatic scene and asset detection.
- **Host Configuration Script**: Example host configuration script to install 3ds Max.
- **Adaptor**: Middleware for efficient rendering with sticky sessions and additional monitoring.
- **Cross-platform compatibility**: Submitter support for Windows with worker support for Windows and automatic path mapping.
- **Usage-based Licensing**: Pay-as-you-go licensing for 3ds Max and Corona.

## 3ds Max version compatibility

The following table shows current support levels for 3ds Max versions:

| Major Version | Submitter Support | Host Configuration Support |
| ------------- | ----------------- | -------------------------- |
| 2024          | Windows           | Windows                    |
| 2025          | Windows           | Windows                    |
| 2026          | Windows           | Windows                    |

## 3ds Max differences from other digital content creation tools

In Deadline Cloud, 3ds Max is installed using host configuration scripts instead of conda packages. This differs from most other DCCs in Deadline Cloud due to unique requirements of the 3ds Max installation process, as the application must be installed by a system administrator.

## Getting started

To use 3ds Max with Deadline Cloud:

1. Create a service-managed fleet and associate it with a queue. Configure the fleet with GPU support if you intend to use GPU-accelerated rendering features. The fleet must be configured with a host configuration script that installs 3ds Max. For more information, see [3ds Max Host Configuration script setup](https://aws.amazon.com/blogs/media/how-to-use-3ds-max-with-service-managed-fleets-on-aws-deadline-cloud/ "https://aws.amazon.com/blogs/media/how-to-use-3ds-max-with-service-managed-fleets-on-aws-deadline-cloud/") and the [3ds Max Host Config example on GitHub](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/3dsmax "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/3dsmax").
2. Install the Deadline Cloud monitor and 3ds Max submitter on your artist workstation using the Deadline Cloud Submitter and monitor Installers. For more information, see [Set up your workstation](submitter.md "submitter.md").
3. Submit your job directly from 3ds Max using the integrated submitter to the queue.
4. Monitor the job and download the output using the Deadline Cloud monitor.

For more information about using the 3ds Max integrated submitter, see the [3ds Max integration user guide on GitHub](https://aws-deadline.github.io/3ds-max "https://aws-deadline.github.io/3ds-max").

## Advanced configurations

### Using unsupported versions

Deadline Cloud only supports and tests the workstation and worker software versions in the table above. You must ensure the version of 3ds Max used by the artist is compatible with the version of 3ds Max configured in your fleet's host configuration.

Support for older 3ds Max versions is possible via host configuration scripts. However, the integrated submitter may not function due to older Python versions. In such cases, custom job bundles can still be submitted as Deadline Cloud jobs.

## 3ds Max renderers

Deadline Cloud supports rendering 3ds Max jobs using the following renderers when using a host configuration script that includes them:

| Renderer                 | Renderer Version | Host Configuration Script Provided | Usage-based Licensing Support |
| ------------------------ | ---------------- | ---------------------------------- | ----------------------------- |
| Autodesk Scanline        | Built-in         | N/A                                | N/A                           |
| Autodesk Raytracer (ART) | Built-in         | N/A                                | N/A                           |
| Chaos V-Ray 6            | 6.x              | Yes                                | Yes                           |
| Chaos V-Ray 7            | 7.x              | Yes                                | Yes                           |
| Corona                   | Latest           | Yes                                | No                            |

## Open source resources

The submitter and adaptor are open source and available on GitHub:

- [3ds Max Submitter and Adaptor](https://github.com/aws-deadline/deadline-cloud-for-3ds-max "https://github.com/aws-deadline/deadline-cloud-for-3ds-max")
- [Deadline Cloud Samples (for 3ds Max workflow examples)](https://github.com/aws-deadline/deadline-cloud-samples "https://github.com/aws-deadline/deadline-cloud-samples")
- [3ds Max Host Config example](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/3dsmax "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/3dsmax")
