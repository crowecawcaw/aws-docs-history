

# KeyShot Studio
<a name="keyshot"></a>

KeyShot Studio is a real-time ray tracing and global illumination program developed by Luxion for rendering 3D models and animations. This guide provides step-by-step instructions for using AWS Deadline Cloud (Deadline Cloud) with KeyShot Studio to render your projects faster by distributing rendering tasks across multiple machines.

## Support overview
<a name="keyshot-support-overview"></a>

KeyShot Studio is supported by the following components:
+ **Submitter**: Integrated submitter extension for direct job submission from KeyShot with automatic scene and asset detection.
+ **Cross-platform compatibility**: Submitter support for Windows and macOS with worker support for Windows.
+ **Licensing (BYOL)**: Bring Your Own License for KeyShot rendering on your farm.

## KeyShot version compatibility
<a name="keyshot-version-compatibility"></a>

The following table shows current support levels for Keyshot versions:


| Major Version | Submitter Support | Render Engines | Licensing | 
| --- | --- | --- | --- | 
| 2024 | Windows, macOS | Built-in ray tracer | BYOL required | 
| 2025 | Windows, macOS | Built-in ray tracer | BYOL required | 

## Prerequisites
<a name="keyshot-prerequisites"></a>

KeyShot requires **Bring Your Own License (BYOL)**. You must have valid KeyShot licenses available for your render farm fleet. Configure your license server to be accessible from worker nodes. For more information, see [Connect service-managed fleets to a custom license server](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/smf-byol.html).

To use KeyShot on service-managed fleets, you must create a conda package and host it in a custom conda channel. A [sample conda recipe for KeyShot](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/keyshot-2025) is available on the GitHub website. For more information about creating custom conda channels, see [Creating custom conda channels](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/configure-jobs-s3-channel.html).

Before you begin, make sure that you have:
+ A Windows or macOS workstation.
+ KeyShot Studio 2023 - 2025.
+ [Deadline Cloud monitor](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/monitor-onboarding.html) installed.
+ Access to an Deadline Cloud farm with a fleet that has KeyShot Studio installed and licensed.

## Getting started
<a name="keyshot-getting-started"></a>

To use KeyShot with Deadline Cloud:

1. Create a service-managed fleet and associate it with a queue. Your queue must be set up with a queue environment that includes your custom conda channel that contains the KeyShot package. For more information, see [Creating a queue environment](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/create-queue-environment.html).

1. Install the Deadline Cloud monitor and KeyShot submitter on your artist workstation using the Deadline Cloud Submitter and monitor installers. For more information, see [Set up your workstation](submitter.md).

## Installation
<a name="keyshot-installation"></a>

The KeyShot submitter extension allows you to submit jobs to Deadline Cloud directly from within KeyShot.

### Installing the submitter
<a name="keyshot-installing-submitter"></a>

To install the submitter:

1. Download the [Deadline Cloud submitter installer](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/submitter.html).

1. Run the installer and follow the on-screen instructions.

1. Launch KeyShot after installation.

### Updating the submitter
<a name="keyshot-updating-submitter"></a>

To update the submitter to the latest version, download and run the latest submitter installer.

## Using the KeyShot submitter
<a name="keyshot-using-submitter"></a>

### Preparing your scene
<a name="keyshot-preparing-scene"></a>

Before submitting a job:

1. Make sure that your scene is saved.

1. Set up your camera angles, materials, and lighting as desired.

1. Configure animation frames if rendering an animation.

### Submitting a job
<a name="keyshot-submitting-job"></a>

1. In KeyShot, on the top toolbar, choose **Scripting Console**.

1. In the Scripting Console, navigate to **Scripts** > **Submit to Deadline Cloud**.

1. Choose **Run**.

### Submission options
<a name="keyshot-submission-options"></a>

When you run the submitter, a dialog asks how you want to handle file attachments.

![Deadline Cloud Submission Options dialog prompting the user to choose which files to attach to the job.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/keyshot-bundling.png)


Choose one of the following options:
+ **The scene BIP file and all external file references** (Recommended)
  + Automatically packages your scene file and all referenced files. Internally, the submitter creates a KeyShot Package (KSP) which bundles all linked files and uses relative paths.
  + Best for scenes with textures, models, and other external assets.
  + Ensures workers have all necessary files to render your scene.
+ **Only the scene BIP file**
  + Only submits the KeyShot scene file.
  + Use this option if your workers already have access to all referenced files.
  + Requires shared network storage or another method to access external files.

### Render settings
<a name="keyshot-render-settings"></a>

After selecting your submission option, the Deadline Cloud submitter interface appears. Configure your render settings:

1. **Shared job settings**.  
![Submit to Deadline Cloud submitter window on the Shared job settings tab, showing job properties and farm and queue selection.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/keyshot-shared-job-settings.png)
   + **Job Name**: Give your job a descriptive name.
   + If you are using the submitter for the first time, you might need to set your farm and queue. To set them, choose the **Settings** button.

1. **Job-specific settings**.  
![Submit to Deadline Cloud submitter window on the Job-specific settings tab, showing KeyShot frame range, output file path, and output format fields.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/keyshot-job-specific-settings.png)
   + **Frames**: Specify which frames to render (for example, `1-30` for frames 1 through 30).
   + **Output File Path**: Set the location and naming pattern for rendered images. The path must include the file's extension, and the extension must match the output format. Use `%d` as a placeholder for the frame number.
   + **Output Format**: Choose the image format (PNG, JPEG, EXR, TIFF, PSD).

1. **Job attachments** (optional). Select which files are uploaded and attached to the job. The submitter automatically detects and attaches files by default.

1. **Host requirements** (optional). Specify which types of hosts are eligible to pick up tasks for this job.

1. Choose **Submit** to send your job to Deadline Cloud.

## Advanced configurations
<a name="keyshot-advanced-configurations"></a>

### Using unsupported versions
<a name="keyshot-unsupported-versions"></a>

Deadline Cloud only supports and tests the workstation and worker software versions in the table above. When using the submitter, the worker uses the KeyShot version from your custom conda package. Ensure that your custom conda channel contains packages for all KeyShot versions that you intend to use.

If you require an unsupported version of KeyShot, you can build a custom conda recipe and channel for your desired version to be installed on the worker. Use the [sample conda recipe for KeyShot](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/keyshot-2025) on the GitHub website as a starting point. For more information about creating custom conda channels, see [Creating custom conda channels](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/configure-jobs-s3-channel.html).

## Open source resources
<a name="keyshot-open-source"></a>

The submitter is open source and available on the GitHub website:
+ [Deadline Cloud for KeyShot](https://github.com/aws-deadline/deadline-cloud-for-keyshot).
+ [KeyShot conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/keyshot-2025).
+ [Standalone KeyShot job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/keyshot_standalone).