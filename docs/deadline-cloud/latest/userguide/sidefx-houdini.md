

# SideFX Houdini
<a name="sidefx-houdini"></a>

SideFX Houdini is a 3D procedural software for modeling, rigging, animation, VFX, look development, lighting, and rendering in film, TV, advertising, and video game pipelines. Houdini is fully supported by Deadline Cloud with comprehensive integration including submitters, conda packages, and an adaptor for increased rendering performance. This guide provides step-by-step instructions for using AWS Deadline Cloud with Houdini to render your projects faster by distributing rendering tasks across multiple machines.

## Support overview
<a name="houdini-support-overview"></a>

Houdini is supported by the following components:
+ **Submitter**: Integrated render output node (ROP) for direct job submission from Houdini with automatic scene and asset detection.
+ **Conda packages**: Deadline Cloud for automatic installation on service-managed fleets.
+ **Adaptor**: A program on worker hosts that keeps the application loaded between tasks for faster rendering and reports render progress.
+ **Cross-platform compatibility**: Submitter support for Windows, macOS, and Linux with worker support for Windows and Linux with automatic path mapping.

## Houdini version compatibility
<a name="houdini-version-compatibility"></a>

The following table shows current support levels for Houdini versions:


| Major Version | Submitter Support | Conda Support | Render Engines | Usage-Based Licensing | 
| --- | --- | --- | --- | --- | 
| 19.5 | Windows, macOS, Linux | Linux | Mantra, Karma CPU, Karma XPU | Usage-based licensing available | 
| 20.0 | Windows, macOS, Linux | Linux | Mantra, Karma CPU, Karma XPU | Usage-based licensing available | 
| 20.5 | Windows, macOS, Linux | Linux | Mantra, Karma CPU, Karma XPU | Usage-based licensing available | 
| 21.0 | Windows, macOS, Linux | Linux | Mantra, Karma CPU, Karma XPU | Usage-based licensing available | 
| 22.0 | Windows, macOS, Linux | Linux | Mantra, Karma CPU, Karma XPU | Usage-based licensing available | 

## Deadline Cloud Conda Channel
<a name="houdini-conda-channel"></a>

The following table lists all conda packages applicable to Houdini available to Service-managed fleets in the deadline-cloud conda channel:


| OS | Package | Version | Notes | 
| --- | --- | --- | --- | 
| Linux | houdini | 19.5 | Includes Mantra and Karma renderers | 
| Linux | houdini | 20.0 | Includes Mantra and Karma renderers | 
| Linux | houdini | 20.5 | Includes Mantra and Karma renderers | 
| Linux | houdini | 21.0 | Includes Mantra and Karma renderers | 
| Linux | houdini | 22.0 | Includes Mantra and Karma renderers | 
| Linux | houdini-openjd |  | Includes the Houdini Adaptor | 

## Getting started
<a name="houdini-getting-started"></a>

To use Houdini with Deadline Cloud:

1. Create a service-managed fleet and associate it with a queue. Your queue must be set up with a queue environment that supports the deadline-cloud conda channel. For more information, see [Creating a queue environment](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/create-queue-environment.html).

1. Install the Deadline Cloud monitor and Houdini submitter on your artist workstation using the Deadline Cloud Submitter and monitor installers. For more information, see [Set up your workstation](submitter.md).

1. Submit your job directly from Houdini using the integrated submitter to the queue.

1. Monitor the job and download the output using the Deadline Cloud monitor.

## Installation
<a name="houdini-installation"></a>

To install the Deadline Cloud for Houdini submitter, you need:
+ A Windows, macOS (arm64), or Linux workstation.
+ A supported version of Houdini.

### Installing the submitter
<a name="houdini-installing-submitter"></a>

**To install the submitter**

1. Download the [Deadline Cloud submitter installer](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/submitter.html).

1. Run the installer.
   + When prompted, select each version of Houdini you want to use the submitter with.

1. Launch Houdini.

The Deadline Cloud submitter is automatically available as a render output (ROP) node.

**Note**  
The submitter installer is available for Windows, macOS, and Linux. For manual installation, see the [manual installation instructions](https://github.com/aws-deadline/deadline-cloud-for-houdini/blob/mainline/README.md) on the GitHub website.

### Verifying the submitter is installed correctly
<a name="houdini-verify-installation"></a>

1. Open Houdini.

1. In the **Network Editor**, choose the `/out` network.

1. Open the context menu (right-click or press **Tab**) and search for `deadline`.

1. Choose **Deadline Cloud** to create a new node.

## Using the Houdini submitter
<a name="houdini-using-submitter"></a>

The Deadline Cloud for Houdini submitter is a node that accepts a render output (ROP) node as input. You can configure and submit your job through this node. When you submit a job, it includes steps for each ROP in the graph.

### Submitting a job from Houdini
<a name="houdini-submit-job"></a>

To use the Deadline Cloud for Houdini submitter, you need:
+ A profile to submit to Deadline Cloud with.
+ An Deadline Cloud farm and queue to submit to.

**To submit a job from Houdini to Deadline Cloud**

1. In the Network Editor, choose the **/out** network.

1. Open the context menu (right-click or press **Tab**) and search for `deadline` to create an Deadline Cloud node.

1. Connect the output of a ROP to the input of the Deadline Cloud node.
   + When you connect a node to the Deadline Cloud node, the submitted job renders the input ROP and all ROPs in its graph.

1. Select the Deadline Cloud node.

1. Use the options in the node editor to configure your job. See [Houdini-specific settings](#houdini-specific-settings) for information about what each option does.

1. (Optional) To export a job's associated files to your job history directory without submitting it, choose **Export Bundle**.

1. Choose **Submit** to send your job to Deadline Cloud.

### Houdini-specific settings
<a name="houdini-specific-settings"></a>

The **Job-specific settings** tab of the Deadline Cloud node provides options specific to Houdini jobs.
+ *Submit Dependencies as Separate Steps* - Split the ROP graph into separate rendering steps for easier monitoring and debugging. When enabled, each connected render node becomes its own step in the job.
+ *Include Adaptor Wheels* - Enable custom builds of the adaptor (called *wheels*) that change rendering behavior. When enabled, you can specify a directory containing adaptor wheels. You can build adaptor wheels by running the [build\_wheels.sh script](https://github.com/aws-deadline/deadline-cloud-for-houdini/blob/mainline/scripts/build_wheels.sh) on the GitHub website.
+ *Adaptor Wheels* - Specify the directory path containing custom adaptor wheels (only available when **Include Adaptor Wheels** is enabled).
+ *Automatically unlock ROPs* - Automatically unlock dependency ROPs during submission. Locked ROPs use existing outputs and won't re-render, which can block dependencies from re-rendering.
+ *Automatically parse scene (.hip) references* - Automatically discover and attach the job's input and output file names and directories based on the ROP graph during job submission.
+ *Automatically save scene (.hip) file* - Automatically save the scene (`.hip`) file to `$HIP` when submitting a job.

For information about the other submitter options, see the [Deadline Cloud guide for using a submitter](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/jobs-using-submitter.html).

### Overriding the render strategy for Deadline Cloud jobs
<a name="houdini-render-strategy"></a>

For many types of nodes, frames can be rendered independently and in any order. For others like simulations, each frame depends on the result of the previous frame and must be rendered sequentially. The submitter chooses a rendering strategy for each node based on its type, but also allows you to override the default.

#### Parallel vs. sequential rendering
<a name="houdini-parallel-vs-sequential"></a>

For parallel rendering, each frame has its own task, and the tasks are distributed across available workers. For sequential rendering, all frames for a node are rendered in a single task running on a single worker.

By default, if a node is a geometry node with **Initialize Simulation OPs** enabled, it renders sequentially. Otherwise the node renders in parallel.

#### Adding a render strategy parameter
<a name="houdini-override-strategy"></a>

You can override the render strategy by creating a `deadline_cloud_render_strategy` parameter on your render node (for example, Mantra or Karma) with a value of either `SEQUENTIAL` or `PARALLEL`.

**To override render strategy by adding a parameter**

1. Open the context menu for a node in the **/out** network (right-click).

1. Choose **Parameters and Channels**, **Edit Parameter Interface**.

1. Under **Create Parameters**, **By Type**, choose **Ordered Menu**.

1. Add an ordered menu to **Existing parameters** by selecting the right arrow next to the **Create Parameters** column.

1. Select the new parameter under **Existing Parameters**, then edit its configuration under **Parameter Description**:
   + In the **Parameter** tab:
     + For **Name**, enter `deadline_cloud_render_strategy`.
     + For **Label**, enter `Deadline Cloud Render Strategy`.
   + In the **Menu** tab, add menu items for:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/sidefx-houdini.html)

1. Choose **Accept**.

Now in the parameter editor for your node, you can use the **Deadline Cloud Render Strategy** menu to specify submitter behavior.

### Husk rendering and USD workflows
<a name="houdini-husk-rendering"></a>

The following sections describe current limitations of USD export workflows in the Houdini submitter and an alternative example job bundle for rendering exported USD scenes with Husk.

#### USD export workflow support
<a name="houdini-usd-export-support"></a>

**The Deadline Cloud submitter for Houdini does not currently have built-in support for USD export workflows.**

You cannot use the submitter node to create a single job that will export a USD scene from Houdini and then call Husk standalone to render without consuming a Houdini Engine license.

#### Alternative: example Husk job bundle
<a name="houdini-husk-bundle"></a>

Deadline Cloud provides an [example Husk job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/houdini_husk_usd_render) on the GitHub website that enables USD export rendering workflows outside of the Houdini submitter. You will need to export the USD scene yourself separately from Houdini before using the example job bundle.

The Husk example job bundle:
+ Allows direct submission of USD scenes for rendering using Husk and a chosen Hydra render delegate without launching Houdini and consuming a Houdini engine license during the render.
+ Automatically introspects USD files to find any file dependencies within to attach using job attachments.
+ Provides a simple GUI for configuration of common Husk settings and submission.

##### Prerequisites
<a name="houdini-husk-prerequisites"></a>

Before using the Husk example job bundle, you need:
+ A scene exported to USD format.
  + See the [USD output documentation](https://www.sidefx.com/docs/houdini/solaris/output.html) on the SideFX website for information on writing out USD files in Houdini.
+ The Deadline Cloud CLI installed and configured.
  + The CLI can be installed from either the submitter installer or directly following the [getting started guide](https://github.com/aws-deadline/deadline-cloud/blob/mainline/docs/index.md#getting-started) on the GitHub website.
+ A git clone of the [deadline-cloud-samples repository](https://github.com/aws-deadline/deadline-cloud-samples) on the GitHub website.
+ The Hydra render delegate available on the worker nodes.
  + Karma is included with Houdini. If you want to use other Hydra render delegates, you must provide them on the worker. See the conda recipes for [V-Ray](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-vray-7) and [Redshift](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-redshift-2026) on the GitHub website as one option to make them available on the worker nodes.

##### Using the Husk example job bundle
<a name="houdini-husk-use"></a>

**To use the Husk example job bundle**

1. Submit the bundle using the Deadline Cloud CLI:

   ```
   deadline bundle gui-submit ./deadline-cloud-samples/job_bundles/houdini_husk_usd_render
   ```

1. Configure your USD file, output settings, frame range, and any other applicable settings to submit.

![Husk example job bundle GUI interface.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/houdini-husk-example-interface.png)


##### Additional resources
<a name="houdini-husk-resources"></a>

The following resources are available on the GitHub website and the SideFX website:
+ [deadline-cloud-samples repository](https://github.com/aws-deadline/deadline-cloud-samples)
+ [SideFX Husk documentation](https://www.sidefx.com/docs/houdini/ref/utils/husk.html)

## Troubleshooting
<a name="houdini-troubleshooting"></a>

The following sections describe common errors and questions you might encounter when using the Deadline Cloud submitter for Houdini, and how to resolve them.

### Why do I get "incomplete asset definitions" errors while rendering?
<a name="houdini-troubleshooting-incomplete-asset"></a>

Jobs from this submitter that run in your farm may produce errors in the logs that look like:

```
The following node types are using incomplete asset definitions:
  Driver/deadline_cloud
```

These errors are safe to ignore. The Deadline Cloud submitter exists as a node in your Houdini scene. When a worker in your farm loads the scene, the scene still contains the Deadline Cloud node, but the worker may not have the submitter installed. Because the worker does not have the files needed to run the Deadline Cloud node, it logs "incomplete asset definition" errors. The Deadline Cloud node itself is not rendered as part of the job, so these errors can be ignored.

### Does the Deadline Cloud submitter support USD export render workflows using Husk?
<a name="houdini-troubleshooting-husk-export"></a>

The Houdini submitter does not directly support export workflows using Husk at this time. Jobs created through the submitter always run the adaptor which uses `hython` and therefore a Houdini engine license for the duration of the render. If you want to render an exported USD scene using just Husk and a Hydra render delegate, you can use an [example job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/houdini_husk_usd_render) on the GitHub website. This approach is useful to render USD scenes with only a render license (for example, Karma) without needing a Houdini engine license for the entire render. For more information on rendering USD scenes with Husk on Deadline Cloud, see [Husk rendering and USD workflows](#houdini-husk-rendering).

## Advanced configurations
<a name="houdini-advanced-configurations"></a>

### Using unsupported versions
<a name="houdini-unsupported-versions"></a>

Deadline Cloud only supports and tests the workstation and worker software versions in the table above. When using the submitter, the worker will attempt to install the same version as used on the workstation. This installation might fail if the workstation version of Houdini does not appear in the version table above.

If you require an unsupported version of Houdini, you have the following options:
+ When submitting the job from Houdini, you can override the CondaPackages queue parameter to specify a supported version to use on the worker (for example, `houdini=21.0, houdini-openjd=*`). This override might or might not work, depending on the features used by your scene and how Houdini works with scenes from your workstation version.
+ you can build a custom conda recipe and channel for your desired version to be installed on the worker. Use the conda recipe for a supported version linked below as a starting point, and package your desired version in a custom conda channel. For more information about creating custom conda channels, see [Creating custom conda channels](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/configure-jobs-s3-channel.html).

## Houdini render engines
<a name="houdini-render-engines"></a>

Houdini supports multiple render engines that are compatible with Deadline Cloud:


| Render Engine | Description | GPU Support | 
| --- | --- | --- | 
| Karma CPU | Modern USD-based renderer (CPU variant) | CPU-based | 
| Karma XPU | Modern USD-based renderer (GPU variant) | GPU accelerated | 
| Mantra | Traditional Houdini renderer | CPU-based | 
| Arnold | Third-party Monte Carlo ray tracer | GPU/CPU hybrid | 
| V-Ray | Third-party photorealistic renderer | GPU/CPU hybrid | 
| Redshift | GPU-accelerated renderer | GPU optimized | 

These render engines are automatically detected and configured by the Houdini integrated submitter and usage is automatically licensed. The submitter maintains dependency trees between connected render output nodes (ROPs).

## Open source resources
<a name="houdini-open-source"></a>

The submitter, adaptor, sample scenes and workflows, and conda recipes for supported versions are open source and available on the GitHub website:
+ [Houdini submitter source code](https://github.com/aws-deadline/deadline-cloud-for-houdini)
+ [Sample scenes and workflows](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/houdini_husk_usd_render)
+ [Conda recipes for supported versions](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/houdini-21.0)