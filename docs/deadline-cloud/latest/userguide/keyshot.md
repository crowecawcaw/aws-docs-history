

# KeyShot Studio
<a name="keyshot"></a>

KeyShot Studio is a real-time ray tracing and global illumination program developed by Luxion for rendering 3D models and animations. This guide provides step-by-step instructions for using AWS Deadline Cloud (Deadline Cloud) with KeyShot Studio to render your projects faster by distributing rendering tasks across multiple machines.

## Support overview
<a name="keyshot-support-overview"></a>

KeyShot Studio is supported by the following components:
+ **Submitter**: A sample KeyShot script that submits the open scene to Deadline Cloud and attaches the scene's external file references.
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
+ A Windows or macOS workstation with a version of KeyShot Studio that's listed in the preceding table.
+ Python 3.11 or later on the workstation, to build the submitter script.
+ The Deadline Cloud CLI with GUI support, installed so that the `deadline` command is on your `PATH`. The Deadline Cloud monitor installer includes the CLI. For more information, see [Set up your workstation](submitter.md).
+ Access to an Deadline Cloud queue with Windows workers that can run KeyShot. For more information, see [Setting up workers](#keyshot-worker-setup).

## Getting started
<a name="keyshot-getting-started"></a>

To use KeyShot with Deadline Cloud:

1. Set up Windows workers that can run KeyShot. For more information, see [Setting up workers](#keyshot-worker-setup).

1. Install the Deadline Cloud monitor and CLI on your artist workstation. For more information, see [Set up your workstation](submitter.md).

1. Install the KeyShot submitter on your artist workstation. For more information, see [Installing the submitter](#keyshot-installing-submitter).

## Installation
<a name="keyshot-installation"></a>

The KeyShot submitter is a script that you run from inside KeyShot to submit jobs to Deadline Cloud.

### Installing the submitter
<a name="keyshot-installing-submitter"></a>

The Deadline Cloud submitter installer doesn't include the KeyShot submitter. The submitter is a single script, `Submit to AWS Deadline Cloud.py`, that you build from the [KeyShot submitter sample](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/custom_submitters/keyshot) on the GitHub website. The build uses only the Python standard library. After you build the script, copy it into your KeyShot scripts folder. KeyShot picks up the new script without a restart.

In KeyShot Studio preferences, under **General**, clear **Use local Python paths**. This setting prevents the submitter from importing Python libraries that KeyShot doesn't include.

For the build command and the scripts folder location on Windows and macOS, see the [KeyShot submitter README](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/job_bundles/custom_submitters/keyshot/README.md) on the GitHub website.

The KeyShot submitter was previously in the deadline-cloud-for-keyshot repository, which is no longer updated. Use the sample for the latest code.

### Updating the submitter
<a name="keyshot-updating-submitter"></a>

To update the submitter, build the script again from the latest version of the sample and replace the copy in your KeyShot scripts folder.

## Setting up workers
<a name="keyshot-worker-setup"></a>

KeyShot jobs run on Windows workers that have KeyShot Studio installed and licensed. The job doesn't use an application adaptor. It looks for the KeyShot executable in the following order:

1. The `KEYSHOT_EXECUTABLE` environment variable.

1. `%KEYSHOT_LOCATION%\bin\keyshot_headless.exe`

1. `keyshot_headless.exe` or `keyshot` on the `PATH`.

Set up workers in one of the following ways:
+ **Service-managed fleets, or any queue with a conda queue environment**: Build a KeyShot conda package with the sample conda recipe that's described in [Prerequisites](#keyshot-prerequisites), and host it in your own conda channel. Set the `CondaChannels` default in the queue environment to that channel, or enter the channel in the submitter's job settings. The submitter requests the KeyShot conda package that matches the major version of KeyShot that submits the job. For more information, see [Creating a queue environment](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/create-queue-environment.html).
+ **Customer-managed fleets with KeyShot installed on the host**: Set `KEYSHOT_EXECUTABLE` on the worker, or add the KeyShot installation directory to the `PATH`. Then clear the `CondaPackages` value in the job settings.

The job uses TCP ports 9000-9099 on the loopback interface (127.0.0.1) to communicate between its scripts and the KeyShot process. These ports don't need network access.

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

1. Open your scene in KeyShot Studio.

1. Choose **Window** > **Scripting Console**.

1. In the Scripting Console, choose **Scripts** > **Submit to AWS Deadline Cloud**.

1. Choose **Run**.

### Submission options
<a name="keyshot-submission-options"></a>

When you run the submitter, a dialog asks how you want to handle file attachments.

![Deadline Cloud Submission Options dialog prompting the user to choose which files to attach to the job.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/keyshot-bundling.png)


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
![Submit to Deadline Cloud submitter window on the Shared job settings tab, showing job properties and farm and queue selection.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/keyshot-shared-job-settings.png)
   + **Job Name**: Give your job a descriptive name.
   + If you are using the submitter for the first time, you might need to set your farm and queue. To set them, choose the **Settings** button.

1. **Job-specific settings**.  
![Submit to Deadline Cloud submitter window on the Job-specific settings tab, showing KeyShot frame range, output file path, and output format fields.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/keyshot-job-specific-settings.png)
   + **Frames**: Specify which frames to render (for example, `1-30` for frames 1 through 30).
   + **Output File Path**: Set the location and naming pattern for rendered images. The path must include the file's extension, and the extension must match the output format. Use `%d` as a placeholder for the frame number.
   + **Output Format**: Choose the image format (PNG, JPEG, EXR, TIFF, PSD).
   + **Override KeyShot render device** and **Render Device**: Choose CPU or GPU rendering instead of the device set in the scene. To render on GPU, set the minimum GPUs host requirement to 1.

1. **Job attachments** (optional). Select which files are uploaded and attached to the job. The submitter automatically detects and attaches files by default.

1. **Host requirements** (optional). Specify which types of hosts are eligible to pick up tasks for this job.

1. Choose **Submit** to send your job to Deadline Cloud.

## Advanced configurations
<a name="keyshot-advanced-configurations"></a>

### Using unsupported versions
<a name="keyshot-unsupported-versions"></a>

Deadline Cloud only supports and tests the workstation and worker software versions in the preceding table. When using the submitter, the worker uses the KeyShot version from your custom conda package. Ensure that your custom conda channel contains packages for all KeyShot versions that you intend to use.

If you require an unsupported version of KeyShot, you can build a custom conda recipe and channel for your desired version to be installed on the worker. Use the [sample conda recipe for KeyShot](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/keyshot-2025) on the GitHub website as a starting point. For more information about creating custom conda channels, see [Creating custom conda channels](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/configure-jobs-s3-channel.html).

## Open source resources
<a name="keyshot-open-source"></a>

The following KeyShot samples are open source and available in the deadline-cloud-samples repository on the GitHub website:
+ [KeyShot submitter](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/custom_submitters/keyshot).
+ [KeyShot conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/keyshot-2025).
+ [Standalone KeyShot job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/keyshot_standalone).