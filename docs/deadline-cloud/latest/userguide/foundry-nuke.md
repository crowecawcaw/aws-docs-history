

# Foundry Nuke
<a name="foundry-nuke"></a>

Foundry Nuke is a node-based digital compositing and visual effects application used for television and film post-production. Nuke is supported by AWS Deadline Cloud (Deadline Cloud) with submitters, conda packages, and an adaptor for increased rendering performance. This guide provides step-by-step instructions for using Deadline Cloud with Nuke to render your projects faster by distributing rendering tasks across multiple machines.

## Support overview
<a name="nuke-support-overview"></a>

Nuke is supported by the following components:
+ **Submitter**: Integrated submitter plugin for direct job submission from Nuke with automatic scene and asset detection.
+ **Conda packages**: Packages to install nuke versions 15, 16, and 17 are available on the Deadline Cloud conda channel for service-managed fleets.
+ **Adaptor**: A program on worker hosts that keeps the application loaded between tasks for faster rendering and reports render progress.
+ **Cross-platform compatibility**: Submitter support for Windows, macOS, and Linux with worker support for Linux only with automatic path mapping.

## Nuke version compatibility
<a name="nuke-version-compatibility"></a>

The following table shows current support levels for Nuke versions:


| Major Version | Submitter Support | Conda Support | 
| --- | --- | --- | 
| 15 | Windows, macOS, Linux | Linux | 
| 16 | Windows, macOS, Linux | Linux | 
| 17 | Windows, macOS, Linux | Linux | 

## Deadline Cloud Conda Channel
<a name="nuke-conda-channel"></a>

The following table lists conda packages applicable to Nuke available to Service-managed fleets in the deadline-cloud conda channel:


| OS | Package | Version | Notes | 
| --- | --- | --- | --- | 
| Linux | nuke | 15 | Includes built-in compositing engine | 
| Linux | nuke | 16 | Includes built-in compositing engine | 
| Linux | nuke | 17 | Includes built-in compositing engine | 
| Linux | nuke-openjd |  | Includes the Nuke Adaptor | 

## Getting started
<a name="nuke-getting-started"></a>

To use Nuke with Deadline Cloud:

1. Create a service-managed fleet and associate it with a queue. Your queue must be set up with a queue environment that supports the deadline-cloud conda channel. For more information, see [Creating a queue environment](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/create-queue-environment.html).

1. Install the Deadline Cloud monitor and Nuke submitter on your artist workstation using the Deadline Cloud Submitter and monitor Installers. For more information, see [Set up your workstation](submitter.md).

1. Submit your job directly from Nuke using the integrated submitter to the queue.

1. Monitor the job and download the output using the Deadline Cloud monitor.

### Launch the submitter
<a name="nuke-launch-submitter"></a>

**To launch the Deadline Cloud submitter in Nuke**
**Note**  
Support for Nuke is provided using the conda environment for service-managed fleets. For more information, see [Default conda queue environment](create-queue-environment.md#conda-queue-environment).

1. Install the Deadline Cloud monitor and Nuke submitter on your artist workstation using the Deadline Cloud Submitter and monitor Installers. For more information, see [Set up your workstation](submitter.md).

1. Open **Nuke**.

1. Open a Nuke script with dependencies that exist within the asset root directory.

1. Choose **AWS Deadline**, and then choose **Submit to Deadline Cloud** to launch the submitter.

1. If you are not already authenticated, choose **Login** and log in with your user credentials in the browser window.

1. Choose **Submit**.

## Installation
<a name="nuke-installation"></a>

To install the Deadline Cloud for Nuke submitter, you need:
+ A Windows, macOS, or Linux workstation.
+ Nuke 14, 15, 16, or 17. We recommend Nuke 15 or later over Nuke 14, because these versions are supported by the [default conda queue environment](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/create-queue-environment.html#conda-queue-environment) on service-managed fleets. To use Nuke 14 with a service-managed fleet, you need to make Nuke 14 available to the worker. The recommended way is to create your own conda package by following [Create a conda package for an application or plugin](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/conda-package.html).

There are two ways to install the Deadline Cloud for Nuke submitter:
+ Using the Deadline Cloud submitter installer (recommended).
+ Manually installing the submitter from source. For instructions, see [Manual installation](https://github.com/aws-deadline/deadline-cloud-for-nuke/blob/mainline/DEVELOPMENT.md#manual-installation) on the GitHub website.

### Using the Deadline Cloud submitter installer
<a name="nuke-install-installer"></a>

You can install the Deadline Cloud for Nuke submitter using the Deadline Cloud submitter installer.

**To install the submitter**:

1. Download the [Deadline Cloud submitter installer](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/submitter.html).

1. Run the installer.

1. When prompted to select components, find and mark the checkbox for Nuke.  
![Deadline Cloud submitter installer with Nuke component selected.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/nuke-submitter_installer.png)

1. Finish running the installer.

1. Launch Nuke.

1. Verify the installation by checking if **Deadline Cloud** has been added to the top navigation bar.

## Using the Nuke submitter
<a name="nuke-using-submitter"></a>

The Deadline Cloud for Nuke submitter supports two types of jobs:
+ Render jobs - Render the output files created by one or more of the Write nodes in your Nuke script. For more information, see [Write nodes](https://learn.foundry.com/nuke/content/comp_environment/rendering/output_write_nodes.html) on the Foundry website.
+ CopyCat training jobs - Perform training for a CopyCat node in your Nuke script. For more information, see [CopyCat](https://learn.foundry.com/nuke/content/reference_guide/air_nodes/copycat.html) on the Foundry website.

### Render jobs
<a name="nuke-render-jobs"></a>

To use the Deadline Cloud for Nuke submitter, you need:
+ A profile to submit to Deadline Cloud with.
+ An Deadline Cloud farm and queue to submit to.

**To submit a render job from Nuke to Deadline Cloud**:

1. Save your Nuke file.

1. From the top navigation bar, choose **Deadline Cloud**. From the drop-down menu, choose **Submit to Deadline Cloud**.

1. Use the tabs in the dialog to customize your job.

1. (Optional) To export a job's associated files to your job history directory without submitting it, choose **Export bundle**.

1. Choose **Submit** and follow the prompts to send your job to Deadline Cloud.

#### Nuke render-specific settings
<a name="nuke-render-settings"></a>

The **Job-specific settings** tab has options specific to jobs created in Nuke:

![Submitter interface showing Nuke render-specific job settings.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/nuke-render_job_settings.png)

+ *Write nodes* - Which write nodes to render outputs for. You can either select to render all write nodes, or select a specific node. For more information, see [Write nodes](https://learn.foundry.com/nuke/content/comp_environment/rendering/output_write_nodes.html) on the Foundry website.
+ *Views* - Which views should be rendered. For more information, see [Setting up stereo views](https://learn.foundry.com/nuke/content/comp_environment/stereoscopic_films/setting_up_stereo_views.html) on the Foundry website.
+ *Override frame range* - Select this option to render a different frame or frame range than is set in Nuke. Frame ranges follow the [Open Job Description specification](https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#34111-intrangeexpr) on the GitHub website.
+ *Use proxy mode* - Manages whether to use proxy mode in the submitted job. For more information, see [Proxy mode](https://learn.foundry.com/nuke/9.0/content/getting_started/managing_scripts/proxy_mode.html) on the Foundry website.
+ *Continue on error* - If selected, Nuke tries to continue rendering when it encounters an error. If cleared, Nuke fails the task when it encounters an error.
+ *Chunk size* - Number of frames to group into each chunk (1-150). Use 1 for one frame per task (default). Higher values group frames into contiguous chunks to reduce per-task overhead. For more information, see [Task chunking for job templates](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-job-bundle-chunking.html).
+ *Target chunk duration (seconds)* - When you specify a value, the scheduler dynamically adjusts chunk sizes based on observed runtimes of completed chunks, aiming for this duration for each chunk. Leave at 0 to use a fixed chunk size for all chunks.
+ *Use timeouts* - Whether to use user-configured timeouts.
+ *Render task timeout* - Maximum duration of each action which performs a render. Default is 6 days.
+ *Setup timeout* - Maximum duration of each action which sets up the job for rendering, such as scene load. Default is 1 day.
+ *Teardown timeout* - Maximum duration of action which tears down the setup required for rendering. Default is 1 hour.
+ *Include gizmos in job bundle* - Whether to include gizmos in the job bundle. For more information, see [Creating and sourcing gizmos](https://learn.foundry.com/nuke/content/comp_environment/configuring_nuke/creating_sourcing_gizmos.html) on the Foundry website.

For information about the other submitter tabs, see the [Deadline Cloud guide for using a submitter](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/jobs-using-submitter.html).

### CopyCat training jobs
<a name="nuke-copycat-jobs"></a>

To use the Deadline Cloud for Nuke submitter to train CopyCat nodes, you need:
+ A profile to submit to Deadline Cloud with.
+ An Deadline Cloud farm and queue to submit to.
+ An Deadline Cloud fleet with GPU-enabled workers associated with the queue you will be submitting to. For instructions on creating a service-managed fleet with GPU access, see [Managing service-managed fleets](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/smf-manage.html).

**To submit a CopyCat training job from Nuke to Deadline Cloud**:

1. Create or open a Nuke script containing a CopyCat node.

1. Attach ground-truth and input nodes to the CopyCat node, and configure knobs on the node to desired values. For details on using CopyCat, see [CopyCat](https://learn.foundry.com/nuke/content/reference_guide/air_nodes/copycat.html) on the Foundry website.

1. Save your Nuke file.

1. From the top navigation bar, choose **Deadline Cloud**. From the drop-down menu, choose **Submit CopyCat Training to Deadline Cloud**.

1. Use the tabs in the dialog to customize your job.

1. (Optional) To export a job's associated files to your job history directory without submitting it, choose **Export bundle**.

1. Choose **Submit** and follow the prompts to send your job to Deadline Cloud.

#### Nuke CopyCat training-specific settings
<a name="nuke-copycat-settings"></a>

The **Job-specific settings** tab has options specific to CopyCat training jobs created in Nuke.

![Submitter interface showing Nuke CopyCat training-specific job settings.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/nuke-copycat_job_settings.png)

+ *CopyCat Node* - Select which CopyCat node to train by node name.
+ *Use timeouts* - Whether to use user-configured timeouts.
+ *Render task timeout* - Maximum duration of each action. In the case of CopyCat, the training is a single action. Default is 6 days.
+ *Setup timeout* - Maximum duration of each action which sets up the job, such as scene load. Default is 1 day.
+ *Teardown timeout* - Maximum duration of action which tears down the setup. Default is 1 hour.
+ *Include gizmos in job bundle* - Whether to include gizmos in the job bundle. For more information, see [Creating and sourcing gizmos](https://learn.foundry.com/nuke/content/comp_environment/configuring_nuke/creating_sourcing_gizmos.html) on the Foundry website.

For information about the other submitter tabs, see the [Deadline Cloud guide for using a submitter](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/jobs-using-submitter.html).

## Advanced configurations
<a name="nuke-advanced-configurations"></a>

### Using unsupported versions
<a name="nuke-unsupported-versions"></a>

Deadline Cloud only supports and tests the workstation and worker software versions in the table above. When using the submitter, the worker attempts to install the same version as used on the workstation. This fails if the workstation version of Nuke does not appear in the version table above.

If you require an unsupported version of Nuke, you have the following options:
+ When submitting the job from Nuke, you can override the CondaPackages queue parameter to specify a supported version to use on the worker (for example, `nuke=17, nuke-openjd=*`). This override might or might not work, depending on the features used by your composition and how Nuke works with compositions from your workstation version.
+ You can build a custom conda recipe and channel for your desired version to be installed on the worker. Use the conda recipe for a supported version linked below as a starting point, and package your desired version in a custom conda channel. For more information about creating custom conda channels, see [Creating custom conda channels](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/configure-jobs-s3-channel.html).

### Custom Nuke executable
<a name="nuke-custom-executable"></a>

You can set the `NUKE_EXECUTABLE` environment variable to point to a specific Nuke executable if it's not available on the PATH.

### OpenColorIO support
<a name="nuke-ocio-support"></a>

The Nuke integration includes full support for OpenColorIO (OCIO) color management workflows. Color configurations are automatically detected and included with job submissions to ensure consistent color handling across the render farm.

## Nuke plugins
<a name="nuke-plugins"></a>

You can add third-party Nuke plugins to a service-managed fleet by building a conda package from a conda recipe and adding it to a custom conda channel. For more information, see [Create a conda package for an application or plugin](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/conda-package.html). To include Nuke gizmos with a job instead, use the **Include gizmos in job bundle** option in the submitter.

### RevisionFX DENoise
<a name="nuke-denoise"></a>

RevisionFX DENoise is a noise-reduction plugin for Nuke compositing jobs. You can build a conda package for DENoise 3.6.9 on Linux workers with the nuke-denoise conda recipe, and then add it to a custom conda channel. A commercial DENoise license is required.

For the recipe, see [nuke-denoise conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nuke-denoise) on the GitHub website.

## Nuke compositing features
<a name="nuke-compositing-features"></a>

Nuke's compositing engine provides comprehensive support for:


| Feature | Description | Notes | 
| --- | --- | --- | 
| Write Nodes | Multiple output formats and codecs | Automatically detected by submitter | 
| Frame Ranges | Custom frame range specification | Supports override and default ranges | 
| Multiple Views | Stereo and multi-view rendering | Proper handling of view-specific outputs | 
| Color Management | OpenColorIO integration | Automatic OCIO configuration detection | 
| Path Mapping | Cross-platform path translation | Windows/Linux compatibility | 
| CopyCat | ML-based paint and rotoscoping | Requires Nuke 14.0 or later | 

Compositing features are automatically detected and configured by the Nuke integrated submitter. The submitter maintains proper dependency handling and asset management for complex compositions.

## Open source resources
<a name="nuke-open-source"></a>

The submitter and adaptor are open source and available on the GitHub website:
+ [Deadline Cloud for Nuke](https://github.com/aws-deadline/deadline-cloud-for-nuke)
+ [Nuke conda recipes](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes) for supported versions.