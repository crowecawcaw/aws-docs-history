# Maxon Cinema 4D

Cinema 4D is a professional 3D animation, modeling, simulation, and rendering software solution from Maxon. Cinema 4D is supported by AWS Deadline Cloud (Deadline Cloud) including a submitter, conda packages, usage-based licensing, and an adaptor for improved performance. This guide walks you through using Deadline Cloud with Cinema 4D - from installation to your first successful render.

The following are reasons to use Deadline Cloud for Cinema 4D:

- **Scale your renders** - Render complex scenes faster by distributing frames across multiple instances, reducing render times from hours to minutes.
- **Free up your workstation** - Submit renders to Deadline Cloud and continue working on your next project while your scenes render in the background.
- **Pay only for what you use** - No upfront costs or long-term commitments. Pay only for the compute time you actually use.
- **Redshift-ready** - Full support for Maxon Cinema 4D and Maxon Redshift.

## Support overview

Cinema 4D is supported by the following components:

- **Submitter**: Integrated submitter for direct job submission from Cinema 4D with automatic scene and asset detection.
- **Conda packages**: Automatic installation on service-managed fleets when using the submitter.
- **Adaptor**: A program on worker hosts that keeps the application loaded between tasks for faster rendering and reports render progress.
- **Cross-platform compatibility**: Submitter support for Windows and macOS with worker support for Windows and Linux with automatic path mapping.
- **Usage-based Licensing**: Pay-as-you-go licensing for Cinema 4D, Redshift, and Red Giant licensing.

## Cinema 4D version compatibility

The following table shows current support levels for Cinema 4D versions:

| Major Version | Submitter Support | Conda Support  | Usage-Based Licensing           |
| ------------- | ----------------- | -------------- | ------------------------------- |
| 2024          | Windows, macOS    | Windows        | Usage-based licensing available |
| 2025          | Windows, macOS    | Windows, Linux | Usage-based licensing available |
| 2026          | Windows, macOS    | Windows, Linux | Usage-based licensing available |

## Deadline Cloud Conda Channel

The following table lists all conda packages applicable to Cinema 4D available to Service-managed fleets in the deadline-cloud conda channel:

| OS             | Package         | Version | Notes                                              |
| -------------- | --------------- | ------- | -------------------------------------------------- |
| Windows        | cinema4d        | 2024    | Includes Standard, Physical and Redshift renderers |
| Windows, Linux | cinema4d        | 2025    | Includes Standard, Physical and Redshift renderers |
| Windows, Linux | cinema4d        | 2026    | Includes Standard, Physical and Redshift renderers |
| Windows, Linux | cinema4d-c4dtoa | 2025    | Cinema4D to Arnold                                 |
| Windows        | cinema4d-c4dtoa | 2026    | Cinema4D to Arnold                                 |
| Windows, Linux | cinema4d-openjd |         | Includes the Cinema 4D Adaptor                     |

###### Note

For **Cinema 4D**, the Linux conda package does not
support substance 3D materials. Jobs with this material fail with one of the following errors:

```
Commandline: ./modules/io_substance/source/substance_framework/src/details/detailsengine.cpp:794: SubstanceAir::Details::Engine::Context::Context(SubstanceAir::Details::Engine&, SubstanceAir::RenderCallbacks*): Assertion `res==0' failed.
```

```
/home/job-user/.conda/envs/<hash>/Lib/deadline/cinema4d_adaptor/Cinema4DAdaptor/adaptor.sh: line 44: 10832 Segmentation fault      (core dumped) $C4DEXE ${ARGS[*]}
```

We recommend that you submit jobs with substance materials to Windows instead.

In Cinema 4D 2025.3.3 on Linux, globalized asset paths can cause segmentation faults.
Therefore, the Linux conda package contains Cinema 4D 2025.3.1 with Redshift 2025.6.0 instead.
If you need features or bug fixes from Cinema 4D 2025.3.3, we recommend two options: upgrade
to Cinema 4D 2026 or submit those jobs to Windows instead.

For **Cinema 4D OpenJD,** to prevent any timeout issues,
we recommend you set task run timeouts to double their expected render time,
instead of using the default 2 day timeout.

## Getting started

To use Cinema 4D fully-managed on Deadline Cloud:

1. Create a service-managed fleet and associate it with a queue. Configure the fleet with GPU support if you intend to use Redshift or Red Giant features that require a GPU. Your queue should be set up with a queue environment that supports the deadline-cloud conda channel. For more information, see [Creating a queue environment](create-queue-environment.md "create-queue-environment.md").
2. Install the Deadline Cloud monitor and Cinema 4D submitter on your artist workstation using the Deadline Cloud Submitter and monitor Installers. For more information, see [Set up your workstation](submitter.md "submitter.md").
3. Submit your job directly from Cinema 4D using the integrated submitter to the queue.
4. Monitor the job and download the output using the Deadline Cloud monitor.

## Quick start

Set up Cinema 4D and Deadline Cloud in just a few steps.

### What you need

- **Cinema 4D 2024 - 2026** installed on your workstation.

  - Redshift, Arnold, and Cargo are supported natively.

- **Windows or macOS** workstation for job submission.
- [Deadline Cloud monitor](monitor-onboarding.md "monitor-onboarding.md") installed.
- **Access to an Deadline Cloud farm** with either:

  - A Windows service-managed fleet, or
  - A customer-managed fleet with Cinema 4D, the Cinema 4D adaptor, and licensing set up.

### Step 1: Install the submitter

The submitter adds Deadline Cloud functionality to Cinema 4D's Extensions menu, allowing you to submit your scene directly to Deadline Cloud to manage the rendering.

Download the [official installer](submitter.md "submitter.md") (recommended).

1. Run the installer and follow the on-screen instructions.
2. Launch Cinema 4D after installation.
3. Verify the submitter appears in **Extensions** > **Deadline Cloud Submitter**.

#### Updating the submitter

To update the submitter to the latest version, download and run the latest [submitter installer](submitter.md "submitter.md").

#### System-wide installation for multiple users (Windows)

For shared workstations or enterprise environments where multiple users need access to the Cinema 4D submitter, you can perform a system-wide installation.

Make sure that you have the following prerequisites:

- Administrator account access.
- Cinema 4D installed on the system.

**Installation steps**:

1. Install the submitter as Administrator:

   - Run the [Deadline Cloud submitter installer](submitter.md "submitter.md") as Administrator.
   - Select "system installation" option during installation.

2. Initial dependency setup:

   - Open Cinema 4D as Administrator (right-click → "Run as administrator").
   - Choose **Extensions**, **Deadline Cloud Submitter**.
   - Choose "Yes" when prompted to install GUI dependencies.
   - This step configures permissions so all users can access the installed packages.

3. Regular usage:

   - After initial setup, any user can open Cinema 4D normally (without Administrator privileges).
   - The Deadline Cloud submitter is available to all users.

For troubleshooting permission issues, see [Troubleshooting](#cinema-4d-troubleshooting "#cinema-4d-troubleshooting").

### Step 2: Submit your first render

1. Open Cinema 4D and load a scene.
2. Make sure your scene is saved.
3. Set up your camera angles, materials, and lighting as desired.
4. Choose **Extensions**, **Deadline Cloud Submitter**.

5. Review your render settings.
6. Choose **Submit**.

### Step 3: Monitor your renders

If you haven't already, install Deadline Cloud monitor from the requirements above.

After submitting a job, open Deadline Cloud monitor to view the job's progress. The submitter creates a job with a single step and one task per frame.

![Deadline Cloud monitor showing a submitted job.](images/cinema-4d-DCM.png)

To view rendering logs, open the context (right-click) menu for a task, and then choose **View logs**. Viewing logs is especially useful for troubleshooting failed jobs.

![Deadline Cloud monitor task logs view.](images/cinema-4d-DCM-logs.png)

### Step 4: Download your results

Once your render job completes successfully, you can download the rendered frames.

1. In Deadline Cloud monitor, locate your completed job.
2. Open the context (right-click) menu for the job.
3. Choose **Download output**.
4. Choose where to save your rendered files.
5. The download begins automatically.

![Download output process in Deadline Cloud monitor.](images/cinema-4d-DCM-download-output.png)

Your rendered frames are organized in the same structure as specified in your output settings.

## Submitter features

The Cinema 4D submitter provides automation and configuration options for your rendering workflow.

### Key benefits

- **Smart asset detection** - Automatically finds and includes all textures, models, and other files your scene needs. No more missing asset errors or manual file hunting.
- **Advanced settings** - Provides additional configuration options beyond basic settings, allowing you to customize output paths, frame ranges, takes, and error checking to fit your workflow.

### Shared job settings

Settings that apply to the entire job:

- **Farm Selection** - Choose which farm your job will render on.
- **Queue Selection** - Select the specific queue within your chosen farm.
- **Job Name** - Give your render job a descriptive name.
- **Job Description** - Add optional details about your render job.
- **Priority** - Set job priority for queue management.
- **Initial State** - Control whether the job starts immediately or remains paused.
- **Max Failed Tasks Count** - Maximum number of tasks that can fail before the job is marked as failed.
- **Max Retries Per Task** - Number of times a failed task will be retried.
- **Max Worker Count** - Maximum number of workers that can work on this job simultaneously.
- **Conda Packages** - Specify additional conda packages required for your render.
- **Conda Channels** - Define custom conda channels for package installation.

![Shared job settings in the Cinema 4D submitter.](images/cinema-4d-shared-job-settings.png)

### Job-specific settings

Settings specific to your Cinema 4D render:

- **Override Output Path** - Override the main render output path from your scene settings.
- **Override Multipass Path** - Override the multipass output path for additional render passes.
- **Takes** - Select which Cinema 4D takes to render.
- **Override Frame Range** - Override the frame range from your scene settings.
- **Automatic Error Checking** - Optional checkbox to activate or deactivate error checking during rendering.
- **Activate detailed logging** - Enable detailed logging to capture detailed logs for debugging rendering issues. When enabled, debug logs are automatically captured and printed to the job output for easy review.
- **Task Run Timeout** - Maximum time allowed for each task to complete.
- **Cinema 4D Launch Timeout** - Maximum time allowed for Cinema 4D to start up.
- **Cinema 4D Shutdown Timeout** - Maximum time allowed for Cinema 4D to shut down cleanly.
- **Save Cinema 4D Project with Assets** - Prevents missing file errors during rendering by creating a temporary copy of your project with all assets and fixing file paths before submission. Uses more disk space and submission time.
- **Use cached text during render** - Prevents incorrect or missing text by re-animating the text on the worker using the cached fonts for each frame. Will increase rendering time.
- **Tile Rendering** - Split each frame into a grid of tiles that render in parallel across multiple workers, then automatically assemble into the final image. Configure the number of columns and rows (1-99 each, default 2x2). See [Tile rendering](#cinema-4d-tile-rendering "#cinema-4d-tile-rendering") below for details.
- **Frames per chunk** – Number of frames to group into each chunk (1-150). Use 1 for one frame per task (default). Higher values reduce per-task overhead. When you set Target chunk duration, this value serves only as the initial chunk size. For more information, see [Task chunking for job templates](../developerguide/build-job-bundle-chunking.md "../developerguide/build-job-bundle-chunking.md").
- **Target chunk duration** – Target render time per chunk in seconds. Deadline Cloud automatically adjusts how many frames to group together to reach this target. To always use the fixed frames-per-chunk value, set this to 0.

![Job-specific settings in the Cinema 4D submitter.](images/cinema-4d-job-specific-settings.png)

### Optional tabs

- **Job Attachments** (optional) - Select which files will be uploaded and attached to the job. Files are automatically detected and attached by default.
- **Host Requirements** (optional) - Allows you to specify which types of hosts will be eligible for picking up tasks for this job.

The submitter handles the technical details so you can focus on your creative work.

### Tile rendering

Tile rendering splits each frame into a grid of smaller tiles that render independently across multiple workers, then automatically assembles them into the final full-resolution image. Tile rendering is useful for large or complex single-frame scenes where a single frame takes a long time to render.

#### How to enable

1. In the **Job-Specific Settings** tab, find the **Tile Rendering** group.
2. Select **Enable Tile Rendering**.
3. Set the number of **Columns** and **Rows** for the tile grid (default: 2x2).

#### How it works

When enabled, the submitter creates a two-step job for each take:

1. **Render step** - Each tile is a separate task. A 3x3 grid produces 9 tile tasks per frame, each rendering only its assigned tile.
2. **Assembly step** - After all tiles for a frame finish, an assembly task automatically stitches them into the final full-resolution image. Both beauty and multi-pass outputs are assembled.

No manual stitching or external tools required.

#### Downloading outputs

The Render step produces intermediary tile image files (for example, `image_0_tile_0_0.png`, `image_0_tile_1_0.png`) that are used as input for assembly. If you only need the final composited images, download the output from the **Assemble Tiles** step rather than the Render step. The Assemble Tiles step contains only the final full-resolution images with all tiles stitched together.

### Detailed logging for debugging

The **Activate detailed logging** feature helps you troubleshoot rendering issues by capturing detailed logs.

#### When to use detailed logging

Enable detailed logging when you need to:

- Debug Redshift rendering issues or unexpected behavior.
- Investigate rendering artifacts or errors.
- Analyze renderer performance and behavior.
- Capture detailed information for technical support.

#### How it works

When you enable the "Activate detailed logging" checkbox in the Job-Specific Settings:

1. **Log capture** - The system automatically enables Redshift debug logging by setting the `REDSHIFT_DEBUGCAPTURE` environment variable.
2. **Log output** - After rendering completes, all Redshift logs are automatically printed to the job output for easy review.

#### Viewing the logs

To view the detailed logs:

1. Open Deadline Cloud monitor.
2. Navigate to your completed job.
3. Open the context (right-click) menu for a task, and then choose **View logs**.
4. Enable the **View logs for all tasks** button.
5. Scroll through the task run logs to find the "Shut down DetailedLogging" section for detailed logs.

The Redshift logs are output in HTML format and include timestamps at the start of each line. If you want to save and view the logs in a web browser without timestamps, you can use the provided cleanup utility:

1. Download the detailed log file from Deadline Cloud monitor. Open the context (right-click) menu for the task, and then choose **Download logs**.
2. Run the cleanup script with the log file path:

```
cd deadline-cloud-for-cinema-4d/scripts
python clean_redshift_detailed_logs.py /path/to/detailed_logs.log
```

Or run it without arguments and enter the path when prompted:

```
python clean_redshift_detailed_logs.py
```

3. Open the generated `redshift_log_cleaned.html` file in your web browser.

The cleanup script automatically extracts the Redshift HTML logs from the detailed log file and removes timestamp prefixes (for example, `2024/11/17 14:23:45-08:00`) from each line, making the logs easier to read and compare.

#### Important notes

- Detailed logging is **disabled by default** to minimize overhead.
- Only enable it when you need to debug specific issues.
- Logs are captured on a per-job basis - each job has its own log output.
- The feature works across Windows and Linux worker nodes.

## Troubleshooting

The following sections describe common issues you might encounter when using Cinema 4D with Deadline Cloud and how to resolve them.

### Rendering questions

**Q: How many tiles should I use?**

A: It depends on your scene. A 3x3 or 4x4 grid is a good starting point. More tiles means more parallelism but also more tasks and overhead. The total tasks per frame is (columns x rows) + 1 for assembly. Deadline Cloud has a maximum of 10,000 tasks per step. Exceeding this limit will cause the job to fail with a `CREATE_FAILED` status. For example, a 99x99 grid on a single frame would produce 9,801 render tasks, which is close to the limit.

**Q: Why don't fonts work while submitting with macOS?**

A: Font functionality is currently only supported on Windows due to technical limitations. This limitation is a known behavior in mixed macOS/Windows environments, as confirmed by Maxon's official documentation. For more information, see [Maxon's official FAQ on resolving missing fonts in Team Render](https://support.maxon.net/hc/en-us/articles/1500006439721-How-to-resolve-missing-fonts-in-Team-Render-for-Cinema-4D-install-fonts-or-make-Text-editable "https://support.maxon.net/hc/en-us/articles/1500006439721-How-to-resolve-missing-fonts-in-Team-Render-for-Cinema-4D-install-fonts-or-make-Text-editable").

### Common issues

**Q: My submitter button doesn't appear in Cinema 4D.**

A: Make sure you've installed the extension correctly and restarted Cinema 4D. Check the Console (**Extensions** > **Console**) for any error messages. Consider re-installing the submitter if the issue persists.

**Q: My job completed successfully but I get "no outputs found" when trying to download outputs. Why?**

A: The cause is most likely a version mismatch between the Cinema 4D submitter and Deadline Cloud monitor. Jobs submitted with `deadline-cloud-for-cinema-4d` 0.11.1 (or newer) are incompatible with Deadline Cloud monitor 1.1.7 and earlier, which causes output downloads to fail even though the render itself succeeded.

**How to verify you're affected**:

1. Check your submitter version. The version is displayed in the submitter window title. If the version is `0.11.1` or later, you have the new submitter.
2. Check your Deadline Cloud monitor version. Open Deadline Cloud monitor and view the **About** dialog (on macOS, **Deadline Cloud monitor** menu > **About Deadline Cloud monitor**; on Windows, **Help** menu > **About Deadline Cloud monitor**). If the version is `1.1.7` or earlier, you have the old Deadline Cloud monitor.

If both conditions are true, you are hitting this issue.

**Fix**: Update Deadline Cloud monitor to **1.1.8 or later**. You can download the latest version from the [Deadline Cloud monitor downloads page](working-with-deadline-monitor.md "working-with-deadline-monitor.md"). After updating, re-open the job in Deadline Cloud monitor and the outputs will download as expected. No re-submission is required.

**Q: Why are some of my textures or assets missing in the rendered output?**

A: The cause is typically a path mapping issue. Cinema 4D sometimes stores deep links (absolute paths) to assets in the scene file that cannot be edited. When the scene is submitted and rendered on the farm, it might still reference the original workstation paths even though the assets were uploaded.

**Workaround**: Enable "Save Cinema 4D Project with Assets" in the Job-Specific Settings tab of the submitter. This setting consolidates all assets into the project folder and fixes the paths before submission, ensuring they render correctly on the farm.

**Q: Are nested Redshift proxy files detected when submitting Cinema 4D jobs to Deadline Cloud?**

A: No, Redshift proxy files are not detected when submitting Cinema 4D jobs to Deadline Cloud. This behavior is a limitation of the Redshift `*.rs` file format. When you export a Cinema 4D scene containing RS Proxy objects to `*.rs`, all referenced proxy data is flattened or inlined into a single file - no external references are preserved. The Cinema 4D SDK cannot read `*.rs` files to discover nested dependencies, and the Redshift Core doesn't expose this functionality either. For more information, see the [Maxon developer forum post](https://developers.maxon.net/forum/topic/16370/cinema-4d-redshift-nested-redshift-proxy-files-not-detected-by-project-asset-inspector/2 "https://developers.maxon.net/forum/topic/16370/cinema-4d-redshift-nested-redshift-proxy-files-not-detected-by-project-asset-inspector/2").

**Q: I'm getting permission errors with a system-wide installation on Windows. How do I fix this?**

A: If users encounter permission errors when accessing the submitter after a system-wide installation:

1. Verify initial setup was completed:

   - Ensure Cinema 4D was opened as Administrator at least once.
   - Ensure the dependency installation prompt was accepted.
   - Check that the installation completed without errors.

2. Check file permissions:

   - Navigate to the installation directory (for example, `C:\Program Files\DeadlineCloudSubmitter\`).
   - Right-click → Properties → Security tab.
   - Verify that "Users" group has "Read & execute" permissions.
   - Permissions should be inherited by all subdirectories and files.

3. Manual permission fix (if needed):

   - Open Command Prompt as Administrator.
   - Run: `icacls "C:\Program Files\DeadlineCloudSubmitter" /grant *S-1-5-32-545:(OI)(CI)(RX) /T`.
   - This grants read and execute permissions to all users.

4. Verify Cinema 4D Python environment:

   - Open Cinema 4D as the affected user.
   - Choose **Extensions**, **Console**.
   - Try importing: `import deadline`.
   - If this fails, the permissions may not be correctly applied.

## Getting support

This section guides you through troubleshooting steps and how to get support when you need it.

### Before you contact support

Before reaching out for help, try these troubleshooting steps. They often resolve common issues and will help you provide better information if you do need to contact support.

**Troubleshooting checklist**:

- **Render one frame locally** - Before submitting to the cloud, render at least one frame locally in Cinema 4D to verify your scene renders correctly. This step helps identify scene-specific issues vs. cloud rendering issues.
- **Update to the latest submitter** - We release updates frequently with bug fixes and improvements. Your issue may already be fixed in a newer version. To check if you're running the latest version:

  - Find your current version: The version is displayed in the submitter window title.
  - Compare with the latest release: Visit the [releases page](https://github.com/aws-deadline/deadline-cloud-for-cinema-4d/releases "https://github.com/aws-deadline/deadline-cloud-for-cinema-4d/releases") to see the most recent version.
  - If your version is older, update the submitter and test again before reporting the issue.

- **Check your Job-Specific Settings** - Review the Job-Specific Settings tab in the submitter. In particular, enable the **Save Cinema 4D Project with Assets** checkbox. This setting creates a temporary copy of your project with all assets and fixes file paths, helping identify missing files and organizing assets for render farms. See [Job-specific settings](#cinema-4d-job-specific-settings "#cinema-4d-job-specific-settings") for more information.
- **Try different Cinema 4D versions** - If you're experiencing issues, test with Cinema 4D 2024, 2025, or 2026 to see if the problem is version-specific.
- **Check existing GitHub issues** - Search the [GitHub issues page](https://github.com/aws-deadline/deadline-cloud-for-cinema-4d/issues?q=is%3Aissue "https://github.com/aws-deadline/deadline-cloud-for-cinema-4d/issues?q=is%3Aissue") to see if someone else has already reported your problem and found a solution.
- **Try a different fleet operating system** - Submit your job to both Windows and Linux fleets if available. Windows generally has better support and compatibility for Cinema 4D features.
- **Review session logs** - Download and review the session logs from Deadline Cloud monitor. These logs often contain error messages that generally pinpoint the issue.
- **Create a scene project file** - Use Cinema 4D's **File** > **Save Project with Assets** to create a self-contained project that includes all dependencies. Zip this file for easy sharing with support.

### When to contact support

Different types of issues should be directed to different support channels.

#### AWS general support

Contact AWS Support for:

- AWS account issues.
- Billing questions.
- General AWS service questions.
- Deadline Cloud internal server errors in Deadline Cloud monitor or while using the CLI.

You can also report Cinema 4D submitter or adaptor issues through AWS Support, but note that these requests might take longer because they need to be routed to the maintainers of the integration repository. For faster response on Cinema 4D-specific issues, we recommend using GitHub issues.

[Contact AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

#### Cinema 4D submitter or adaptor support

Use GitHub issues as your primary channel for Cinema 4D-specific problems:

- Submitter bugs or crashes.
- Adaptor issues.
- Rendering failures specific to Cinema 4D.
- Feature requests.
- Integration problems.

[Open a GitHub issue](https://github.com/aws-deadline/deadline-cloud-for-cinema-4d/issues "https://github.com/aws-deadline/deadline-cloud-for-cinema-4d/issues").

### How to report issues on GitHub

#### Bug reports

**Before creating a new bug report**:

1. [Search existing bugs](https://github.com/aws-deadline/deadline-cloud-for-cinema-4d/issues?q=label%3Abug "https://github.com/aws-deadline/deadline-cloud-for-cinema-4d/issues?q=label%3Abug") to see if your problem has already been reported or fixed in latest versions.
2. If you find an existing issue that matches your problem:

   - Add a thumbs-up reaction to help us prioritize.
   - Comment with any additional details or reproduction steps you can provide.
   - This information helps us understand how many users are affected.

If no existing issue matches, [create a new bug report](https://github.com/aws-deadline/deadline-cloud-for-cinema-4d/issues/new?template=bug.yml "https://github.com/aws-deadline/deadline-cloud-for-cinema-4d/issues/new?template=bug.yml") using the bug report template. The template will guide you through providing all the necessary information.

#### Feature requests

**Before creating a new feature request**:

1. [Search existing feature requests](https://github.com/aws-deadline/deadline-cloud-for-cinema-4d/issues?q=is%3Aopen+label%3Aenhancement "https://github.com/aws-deadline/deadline-cloud-for-cinema-4d/issues?q=is%3Aopen+label%3Aenhancement") to see if someone has already suggested your idea.
2. If you find an existing request that matches:

   - Add a thumbs-up reaction to show your support.
   - Comment with your specific use case - this strengthens the request and helps us understand different needs.
   - The more users who express interest, the higher priority it receives.

If no existing request matches, [create a new feature request](https://github.com/aws-deadline/deadline-cloud-for-cinema-4d/issues/new?template=feature_request.yml "https://github.com/aws-deadline/deadline-cloud-for-cinema-4d/issues/new?template=feature_request.yml") using the feature request template. The template will guide you through providing all the necessary information.

###### Note

Feature requests help us prioritize development, but there's no guarantee of implementation timeline.

### What to include in your support request

**Required information checklist**:

When contacting support or creating a GitHub issue, always include:

- **Cinema 4D version** - for example, Cinema 4D 2025.1.0.
- **Operating system** - for example, Windows 11, macOS 14.2.
- **Submitter version** - Copy the entire contents of the About panel (**Extensions** > **Deadline Cloud Submitter** > **About**).
- **Renderer** - Standard, Redshift, Arnold, etc.
- **Fleet configuration** - Worker OS (Windows or Linux), memory requirements, disk space, GPU type if using Redshift.
- **Error messages** - Complete error text, not paraphrased.

#### How to gather log files

Logs are essential for diagnosing issues. To enable detailed logging:

1. In the Cinema 4D submitter, select **Activate detailed logging** in Job-Specific Settings.
2. Submit your job.
3. After the job completes (or fails), retrieve the logs:

   - Open Deadline Cloud monitor.
   - Navigate to your job.
   - Choose **Download logs** and select **Entire session** to download the full session logs for sharing with support.

#### How to create scene project files

A scene project file packages your Cinema 4D scene with all its assets:

1. First, remove any confidential assets or data from your scene before saving.
2. In Cinema 4D, go to **File** > **Save Project with Assets**.
3. Choose a destination folder.
4. Cinema 4D will copy your scene and all referenced assets to this folder.
5. Zip the entire project folder.
6. Share the zip file with support.

###### Important

Remove confidential assets _before_ using "Save Project with Assets" - not after. Removing assets after saving can cause missing file errors that make it harder to diagnose your original issue.

**Tip**: The best way to share a reproducible test case is with a publicly available scene or a simplified scene that demonstrates the issue without confidential material. If you can recreate the problem with non-proprietary assets, that makes it much easier for support to investigate.

## Advanced configurations

### Using unsupported versions

Deadline Cloud only supports and tests the workstation and worker software versions in the table above. When using the submitter, the worker will attempt to install the same version as used on the workstation. This installation fails if the workstation version of Cinema 4D does not appear in the version table above.

If you require an unsupported version of Cinema 4D, you can build a custom conda recipe and channel for your desired version to be installed on the worker. Use the conda recipe for a supported version linked in the Open Source Resources section below as a starting point, and package your desired version in a custom conda channel. For more information about creating custom conda channels, see [Creating custom conda channels](../developerguide/configure-jobs-s3-channel.md "../developerguide/configure-jobs-s3-channel.md").

If you create a conda package for a different version of Cinema 4D, you should ensure it will acquire a license correctly. If the version is compatible with licensing for a supported version in the table above, then usage-based licensing will work automatically. You may also bring your own license to a service-managed fleet by following [Connect service-managed fleets to a custom license server](../developerguide/smf-byol.md "../developerguide/smf-byol.md").

## Cinema 4D plugins

| Plugin               | Plugin Version | Conda Recipe Provided | SMF Conda Package Provided | Usage-based Licensing Support |
| -------------------- | -------------- | --------------------- | -------------------------- | ----------------------------- |
| Redshift             | 2026.3.0       | Bundled\*             | Yes                        | Yes                           |
| Redshift             | 2025.6.0       | Bundled\*             | Yes                        | Yes                           |
| Red Giant            | 2025.x         | No                    | No                         | Yes                           |
| V-Ray                | 7.x            | Yes                   | No                         | Yes                           |
| Insydium X-Particles | 2024.x         | Yes                   | No                         | N/A                           |
| C4DtoArnold          | 4.8.4.1        | Yes                   | Yes                        | Yes                           |

\*Included in the base Cinema 4D package recipe

### Maxon Redshift

The Redshift renderer is included with all Cinema 4D conda packages and is automatically used when appropriate when using the Cinema 4D integrated submitter. An additional licensing cost applies when using Redshift for rendering. For more information about Deadline Cloud pricing, see [Deadline Cloud pricing](https://aws.amazon.com/deadline-cloud/pricing/ "https://aws.amazon.com/deadline-cloud/pricing/").

### Maxon Red Giant

Red Giant is a comprehensive toolkit designed for video post-production, motion graphics, and visual effects. It offers rich color grading, smooth transitions, realistic visual effects, motion design templates and tools to create and edit your visuals. For more information, see [Red Giant](https://www.maxon.net/en/red-giant "https://www.maxon.net/en/red-giant").

Red Giant requires custom setup on service-managed fleets. A host configuration script is provided which you can use in your Deadline Cloud fleet. Once configured, Red Giant is supported by Deadline Cloud Usage-based Licensing and requires no further configuration to operate.

### V-Ray Plugin

V-Ray is a 3D photorealistic ray-traced rendering plug-in. V-Ray for Cinema 4D is not currently fully supported in Service-managed fleets. We provide a conda recipe that you can use to create your own conda channel for use in your Deadline Cloud farm. For more information about creating custom conda channels, see [Creating custom conda channels](../developerguide/configure-jobs-s3-channel.md "../developerguide/configure-jobs-s3-channel.md"). After installation, V-Ray is supported by Deadline Cloud Usage-based Licensing and requires no further configuration to operate.

### C4DToArnold

Autodesk Arnold software is an advanced Monte Carlo ray tracing renderer. For more information, see [Arnold](https://www.autodesk.com/in/products/arnold/overview "https://www.autodesk.com/in/products/arnold/overview"). C4DToArnold is fully supported in Service-managed fleets.

### Insydium X-Particles

X-Particles is a fully-featured advanced particle and VFX system for Maxon's Cinema 4D. For more information, see [X-Particles](https://insydium.ltd/products/x-particles/ "https://insydium.ltd/products/x-particles/"). Insydium X-Particles is not currently fully supported in Service-managed fleets. We provide a conda recipe that you can use to create your own conda channel for use in your Deadline Cloud farm. For more information about creating custom conda channels, see [Creating custom conda channels](../developerguide/configure-jobs-s3-channel.md "../developerguide/configure-jobs-s3-channel.md"). When you create the conda package from your X-Particles package, it will include your purchased license. No additional configuration is necessary to operate on service-managed fleets.

## Open source resources

The submitter and adaptor are open source and available on GitHub:

- [Deadline Cloud for Cinema 4D](https://github.com/aws-deadline/deadline-cloud-for-cinema-4d "https://github.com/aws-deadline/deadline-cloud-for-cinema-4d")
- [Cinema 4D Conda recipes](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes") are available on GitHub for C4D 2024, C4D 2025, the INSYDIUM X-PARTICLES plugin, the C4DtoA plugin, and the V-Ray Plugin.
- [Host Configuration script](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/cinema4d/cinema4d_redgiant "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/cinema4d/cinema4d_redgiant") is included to support Red Giant plugins.
