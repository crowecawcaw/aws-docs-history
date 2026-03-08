# KeyShot Studio

###### Note

For more information about installing, configuring, and using this integration on your workstation, see the [KeyShot integration user guide on GitHub](https://aws-deadline.github.io/keyshot/ "https://aws-deadline.github.io/keyshot/").

KeyShot Studio is a real-time ray tracing and global illumination program developed by Luxion for rendering 3D models and animations.

## Support overview

KeyShot Studio is supported by the following components:

- **Submitter**: Integrated submitter extension for direct job submission from KeyShot with automatic scene and asset detection.
- **Conda package**: Pre-packaged software for automatic installation on service-managed fleets.
- **Cross-platform compatibility**: Submitter support for Windows and macOS with worker support for Windows.
- **Usage-based Licensing**: Pay-as-you-go for KeyShot licensing.

## KeyShot version compatibility

The following table shows current support levels for Keyshot versions:

| Major Version | Submitter Support | Conda Support | Render Engines      | Usage-Based Licensing           |
| ------------- | ----------------- | ------------- | ------------------- | ------------------------------- |
| 2024          | Windows, macOS    | Windows       | Built-in ray tracer | Usage-based licensing available |
| 2025          | Windows, macOS    | Windows       | Built-in ray tracer | Usage-based licensing available |

## Deadline Cloud Conda Channel

The following table lists all conda packages applicable to Keyshot available to Service-managed fleets in the `deadline-cloud` conda channel:

| OS      | Package        | Version | Notes                        |
| ------- | -------------- | ------- | ---------------------------- |
| Windows | keyshot        | 2024    | Includes built-in ray tracer |
| Windows | keyshot        | 2025    | Includes built-in ray tracer |
| Linux   | keyshot-openjd |         | Includes the KeyShot Adaptor |

## Getting started

To use KeyShot with Deadline Cloud:

1. Create a service-managed fleet and associate it with a queue. Your queue must be set up with a queue environment that supports the `deadline-cloud` conda channel. For more information, see [Creating a queue environment](create-queue-environment.md "create-queue-environment.md").
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

Deadline Cloud only supports and tests the workstation and worker software versions in the table above. When using the submitter, the worker will attempt to install the same version as used on the workstation. This will fail if the workstation version of KeyShot does not appear in the version table above.

If you require an unsupported version of KeyShot, you have the following options:

- When submitting the job from KeyShot, you may override the CondaPackages queue parameter to specify a supported version to use on the worker (for example, `keyshot=2024`). The job may run successfully depending on the features used by your scene and how KeyShot works with scenes from the version on your workstation.
- You may build a custom conda recipe and channel for your desired version to be installed on the worker. Use the conda recipe for a supported version linked below as a starting point, and package your desired version in a custom conda channel. For more information about creating custom conda channels, see [Creating custom conda channels](../developerguide/configure-jobs-s3-channel.md "../developerguide/configure-jobs-s3-channel.md").

## Open source resources

The submitter is open source and available on GitHub:

- [Deadline Cloud for KeyShot](https://github.com/aws-deadline/deadline-cloud-for-keyshot "https://github.com/aws-deadline/deadline-cloud-for-keyshot")
- [Standalone KeyShot job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/keyshot_standalone "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/keyshot_standalone") is available on GitHub.
- [Comprehensive user guide](https://aws-deadline.github.io/keyshot/ "https://aws-deadline.github.io/keyshot/") is available.
