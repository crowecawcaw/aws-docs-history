

# Supported Software
<a name="supported-software"></a>

Deadline Cloud supports many digital content creation (DCC) applications for 3D rendering, animation, visual effects, and compositing. The applications in the following table are preconfigured to work out of the box with some or all of the following:
+ **Submitter** – An integrated plug-in for submitting jobs directly from the application. For more information, see [Set up your workstation](submitter.md).
+ **Service-managed fleet conda packages** – Prebuilt packages in the `deadline-cloud` conda channel that install the application on workers automatically, with no image to build or maintain. For more information, see [Creating a queue environment](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/create-queue-environment.html).
+ **Usage-based licensing (UBL)** – Pay-as-you-go licensing on service-managed fleets, so you don't need to bring your own license server. Applications that don't require a license to render are marked as *Not needed*. For more information, see [Software licensing for service-managed fleets](smf-licensing.md).

You aren't limited to the applications in the table. You can run almost any application or plugin on Deadline Cloud by packaging it yourself. For more information, see [Software that isn't listed](#software-not-listed).

## Software support summary
<a name="software-support-summary"></a>

The following table summarizes support for each application. Select an application for versions, submitter installation steps, renderers, plugins, and conda package details.


| Software | Supported versions | Submitter | Service-managed fleet conda packages | Usage-based licensing | 
| --- | --- | --- | --- | --- | 
| [Adobe After Effects](adobe-after-effects.md) | 2024 - 2026 | Windows, macOS | Windows | No | 
| [Autodesk 3ds Max](autodesk-3ds-max.md) | 2024 - 2027 | Windows | No | Yes | 
| [Autodesk Arnold for Cinema 4D](maxon-cinema-4d.md) | 4.8.4.1 | Windows, macOS | Windows, Linux | Yes | 
| [Autodesk Arnold for Maya](autodesk-maya.md) | 7.1 - 7.5 | Windows, macOS, Linux | Linux | Yes | 
| [Autodesk Maya](autodesk-maya.md) | 2023 - 2027 | Windows, macOS, Linux | Linux | Yes | 
| [Autodesk VRED](autodesk-vred.md) | 2025 - 2026 | Windows | Linux | No | 
| [Blender](blender.md) | 3.6 - 5.1 | Windows, macOS, Linux | Linux | Not needed | 
| [Chaos V-Ray for Maya](autodesk-maya.md) | 6 - 7 | Windows, macOS, Linux | Linux | Yes | 
| [Foundry Nuke](foundry-nuke.md) | 15 - 17 | Windows, macOS, Linux | Linux | Yes | 
| [KeyShot Studio](keyshot.md) | 2023 - 2025 | Windows, macOS | No | No | 
| [Maxon Cinema 4D](maxon-cinema-4d.md) | 2024 - 2026 | Windows, macOS | Windows, Linux | Yes | 
| [Maxon Redshift for Maya](autodesk-maya.md) | 2025-2026 | Windows, macOS, Linux | Linux | Yes | 
| [SideFX Houdini](sidefx-houdini.md) | 19.5 - 22.0 | Windows, macOS, Linux | Linux | Yes | 
| [Unreal Engine](epic-unreal-engine.md) | 5.4 - 5.8 | Windows | Windows | Not needed | 

## Software that isn't listed
<a name="software-not-listed"></a>

If an application, plugin, or version that you need isn't in the table, you can still run it on Deadline Cloud. Service-managed fleets install software from any conda channel that you configure, so a customer-managed fleet isn't required. You have the following options:
+ Build a conda package for the application or plugin and host it in your own channel. Workers on service-managed and customer-managed fleets install it the same way as packages from the `deadline-cloud` channel. Examples of software you can add as packages include plugins such as MayaUSD, custom shaders, and OCIO configurations. For more information, see [Create a conda package for an application or plugin](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/conda-package.html) in the *Deadline Cloud Developer Guide*.
+ Install the software directly on the worker hosts of a customer-managed fleet, for example through a custom Amazon Machine Image (AMI). For more information, see [Install and configure software required for jobs](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/cmf-software.html) in the *Deadline Cloud Developer Guide*.

For an overview of all the ways to provide software to your jobs, see [Provide applications for your jobs](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/provide-applications.html) in the *Deadline Cloud Developer Guide*.

## Beyond digital content creation
<a name="supported-software-other-workloads"></a>

Deadline Cloud also supports general-purpose compute-intensive workloads including scientific simulations, financial modeling, machine learning model training and evaluation, autonomous driving simulation, and data processing. You can run any workload that benefits from distributed parallel processing by creating custom job bundles. For examples that span these domains, see [Code examples](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/code-examples.html) in the *Deadline Cloud Developer Guide*.