# KeyShot Studio

###### Note

For more information about installing, configuring, and using this integration on your workstation, see the [KeyShot integration user guide on GitHub](https://aws-deadline.github.io/keyshot/ "https://aws-deadline.github.io/keyshot/").

KeyShot Studio is a real-time ray tracing and global illumination program developed by Luxion for rendering 3D models and animations.

## Support overview

KeyShot Studio is supported by the following components:

- **Submitter**: Integrated submitter extension for direct job submission from KeyShot with automatic scene and asset detection.
- **Cross-platform compatibility**: Submitter support for Windows and macOS with worker support for Windows.
- **Licensing (BYOL)**: Bring Your Own License for KeyShot rendering on your farm.

## KeyShot version compatibility

The following table shows current support levels for Keyshot versions:

| Major Version | Submitter Support | Render Engines      | Licensing     |
| ------------- | ----------------- | ------------------- | ------------- |
| 2024          | Windows, macOS    | Built-in ray tracer | BYOL required |
| 2025          | Windows, macOS    | Built-in ray tracer | BYOL required |

## Prerequisites

KeyShot requires **Bring Your Own License (BYOL)**. You must have valid KeyShot licenses available for your render farm fleet. Configure your license server to be accessible from worker nodes. For more information, see [Connect service-managed fleets to a custom license server](../developerguide/smf-byol.md "../developerguide/smf-byol.md").

To use KeyShot on service-managed fleets, you must create a conda package and host it in a custom conda channel. A [sample conda recipe for KeyShot](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/keyshot-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/keyshot-2025") is available on GitHub. For more information about creating custom conda channels, see [Creating custom conda channels](../developerguide/configure-jobs-s3-channel.md "../developerguide/configure-jobs-s3-channel.md").

## Getting started

To use KeyShot with Deadline Cloud:

1. Create a service-managed fleet and associate it with a queue. Your queue must be set up with a queue environment that includes your custom conda channel that contains the KeyShot package. For more information, see [Creating a queue environment](create-queue-environment.md "create-queue-environment.md").
2. Install the Deadline Cloud monitor and KeyShot submitter on your artist workstation using the Deadline Cloud Submitter and monitor installers. For more information, see [Set up your workstation](submitter.md "submitter.md").

## Using the KeyShot submitter

To use the KeyShot submitter:

1. Open KeyShot.
2. Choose **Windows** > **Scripting console** > **Submit to Deadline Cloud** and **Run**.
3. Select your preferred submission mode from the dialog that appears.
4. Configure your job settings in the submitter interface.
5. Choose **Submit** to send your job to Deadline Cloud.
6. Monitor the job and download the output using the Deadline Cloud monitor.

For more information about using the KeyShot submitter for Deadline Cloud, see [KeyShot submitter guide](https://aws-deadline.github.io/keyshot/ "https://aws-deadline.github.io/keyshot/").

## Advanced configurations

### Using unsupported versions

Deadline Cloud only supports and tests the workstation and worker software versions in the table above. When using the submitter, the worker uses the KeyShot version from your custom conda package. Ensure that your custom conda channel contains packages for all KeyShot versions that you intend to use.

If you require an unsupported version of KeyShot, you can build a custom conda recipe and channel for your desired version to be installed on the worker. Use the [sample conda recipe for KeyShot](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/keyshot-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/keyshot-2025") as a starting point. For more information about creating custom conda channels, see [Creating custom conda channels](../developerguide/configure-jobs-s3-channel.md "../developerguide/configure-jobs-s3-channel.md").

## Open source resources

The submitter is open source and available on GitHub:

- [Deadline Cloud for KeyShot](https://github.com/aws-deadline/deadline-cloud-for-keyshot "https://github.com/aws-deadline/deadline-cloud-for-keyshot").
- [KeyShot conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/keyshot-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/keyshot-2025").
- [Standalone KeyShot job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/keyshot_standalone "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/keyshot_standalone").
- [Comprehensive user guide](https://aws-deadline.github.io/keyshot/ "https://aws-deadline.github.io/keyshot/").
