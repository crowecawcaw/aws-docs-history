# Epic Unreal Engine

###### Note

For more information about installing, configuring, and using this integration on your workstation, see the [Unreal Engine integration user guide on GitHub](https://aws-deadline.github.io/unreal-engine/ "https://aws-deadline.github.io/unreal-engine/").

Unreal Engine is a real-time 3D creation tool for photoreal visuals and immersive experiences. Unreal Engine is supported by Deadline Cloud with submitters, conda packages, and an adaptor for increased rendering performance.

## Support overview

Unreal Engine is supported by the following components:

- **Submitter**: Integrated submitter plugin for direct job submission from Unreal Engine with automatic scene and asset detection.
- **Conda packages**: Deadline Cloud for automatic installation on service-managed fleets.
- **Adaptor**: Middleware for efficient rendering with sticky sessions and additional monitoring.
- **Cross-platform compatibility**: Submitter and worker support for Windows only.
- **Movie Render Queue Integration**: Support for Unreal's Movie Render Queue system.

## Unreal Engine version compatibility

The following table shows current support levels for Unreal Engine versions:

| Major Version | Submitter Support | Conda Support |
| ------------- | ----------------- | ------------- |
| 5.4           | Windows           | Windows       |
| 5.5           | Windows           | Windows       |
| 5.6           | Windows           | Windows       |
| 5.7           | Windows           | Windows       |

## Deadline Cloud Conda Channel

The following table lists all conda packages applicable to Unreal Engine available to Service-managed fleets in the `deadline-cloud` conda channel:

| OS      | Package              | Version |
| ------- | -------------------- | ------- |
| Windows | unreal-engine        | 5.4     |
| Windows | unreal-engine        | 5.5     |
| Windows | unreal-engine        | 5.6     |
| Windows | unreal-engine        | 5.7     |
| Windows | unreal-engine-openjd |         |

## Getting started

### Prerequisites

Before installing the Unreal Engine submitter, ensure you have the following:

- Windows workstation (Windows 10 or later)
- Supported version of Unreal Engine installed
- Deadline Cloud monitor installed ([download here](monitor-onboarding.md "monitor-onboarding.md"))
- Access to an Deadline Cloud farm with either a GPU-enabled Windows service-managed fleet or a customer-managed fleet with Unreal Engine, the Unreal Engine adaptor, and licensing set up

### Installing the Unreal Engine Submitter

The Unreal Engine submitter adds Deadline Cloud functionality as a plugin to Unreal Engine, allowing you to submit your Movie Render Queue jobs directly to Deadline Cloud for rendering.

For detailed installation instructions, see the [Unreal Submitter Setup Guide](https://aws-deadline.github.io/unreal-engine/setup-submitter/ "https://aws-deadline.github.io/unreal-engine/setup-submitter/").

#### Updating the Submitter

Refresh your git repository and re-run the installation script as mentioned in [Unreal Submitter Setup Guide](https://aws-deadline.github.io/unreal-engine/setup-submitter/ "https://aws-deadline.github.io/unreal-engine/setup-submitter/").

## Using the Unreal Engine submitter

To use the Unreal Engine submitter:

1. Open Unreal Engine with your project.
2. Set up your Movie Render Queue with the desired shots and render settings.
3. Access the Deadline Cloud submitter plugin from the Unreal Engine interface.
4. Configure your job settings including:
   - Movie Render Queue configuration
   - Output paths and formats
   - Render parameters

5. Choose **Submit** to send your job to Deadline Cloud.

The submitter automatically detects Movie Render Queue configurations and handles asset dependencies, including project plugins and content files.

## Advanced configurations

### Service-Managed Fleets vs Customer-Managed Fleets

#### Service-Managed Fleets (SMF)

On Service-Managed Fleets, the Unreal Engine and adaptor are automatically available via the `deadline-cloud` Conda channel with the default Queue Environment. This provides the easiest setup experience.

#### Customer-Managed Fleets (CMF)

For Customer-Managed Fleets, Unreal Engine and the adaptor must be manually installed on worker hosts. This setup provides more control and supports additional features like Perforce integration.

For detailed instructions, see the [CMF Worker Setup Guide](https://aws-deadline.github.io/unreal-engine/setup-cmf-worker/ "https://aws-deadline.github.io/unreal-engine/setup-cmf-worker/").

### Perforce integration

Unreal Engine integration includes support for Perforce version control systems. The integration provides utilities for syncing dependent files and managing Perforce workspaces during rendering.

For more information on submitting perforce integrated jobs to deadline-cloud see [Perforce Guide](https://aws-deadline.github.io/unreal-engine/create-perforce-render-job/ "https://aws-deadline.github.io/unreal-engine/create-perforce-render-job/") .

## Unreal Engine rendering features

Unreal Engine's rendering system provides comprehensive support for:

| Feature            | Description                           | Notes                                         |
| ------------------ | ------------------------------------- | --------------------------------------------- |
| Movie Render Queue | High-quality offline rendering        | Integration with job submission               |
| Sequencer          | Timeline-based animation system       | Automatic shot detection and processing       |
| Project Plugins    | Custom plugin support                 | Automatic detection and inclusion             |
| Asset Dependencies | Content file management               | Comprehensive asset tracking                  |
| Sticky Rendering   | Application persistence between shots | Improved performance for multi-shot sequences |

All rendering features are automatically detected and configured by the Unreal Engine integrated submitter. The adaptor maintains proper dependency handling and supports efficient multi-shot rendering without restarting Unreal Engine.

## Open source resources

The submitter and adaptor are open source and available on GitHub:

- [Deadline Cloud for Unreal Engine](https://github.com/aws-deadline/deadline-cloud-for-unreal-engine "https://github.com/aws-deadline/deadline-cloud-for-unreal-engine")
