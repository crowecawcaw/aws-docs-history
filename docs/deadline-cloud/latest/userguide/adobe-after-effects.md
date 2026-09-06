# Adobe After Effects

Adobe After Effects is a professional digital visual effects, motion graphics, and
compositing application. After Effects is fully supported by Deadline Cloud with comprehensive
integration including submitters and conda packages for increased rendering performance.
This guide provides step-by-step instructions for using AWS Deadline Cloud with After Effects to
render your projects faster by distributing rendering tasks across multiple machines.

## Support overview

After Effects is supported by the following components:

- **Submitter**: Integrated submitter for direct
  job submission from After Effects with automatic scene and asset detection.
- **Conda packages**: Deadline Cloud for automatic
  installation on service-managed fleets.
- **Cross-platform compatibility**: Submitter
  support for Windows and macOS with worker support for Windows.

## After Effects version compatibility

The following table shows current support
levels
for After Effects versions:

| Major Version | Submitter Support | Conda Support |
| ------------- | ----------------- | ------------- |
| 2024          | Windows, macOS    | Windows       |
| 2025          | Windows, macOS    | Windows       |
| 2026          | Windows, macOS    | Windows       |

## Deadline Cloud Conda Channel

The
following table lists all conda packages applicable to After Effects available to
Service-managed fleets in the deadline-cloud conda channel:

| OS      | Package      | Version |
| ------- | ------------ | ------- |
| Windows | aftereffects | 24.6    |
| Windows | aftereffects | 25.1    |
| Windows | aftereffects | 25.2    |
| Windows | aftereffects | 25.6    |
| Windows | aftereffects | 26.0    |

## Getting started

Complete the following steps to set up After Effects with Deadline Cloud. You will install the
required submitter and monitor on your workstation and begin submitting render jobs to
your queue.

1. Create a service-managed fleet and associate it with a queue. Your queue must
   be set up with a queue environment that supports the deadline-cloud conda
   channel. For more information, see [Creating
   a queue environment](create-queue-environment.md "create-queue-environment.md").
2. Install the Deadline Cloud monitor on your artist workstation using the Deadline Cloud monitor
   Installers. For more information, see [Set up your workstation](submitter.md "submitter.md").
3. Install the Deadline Cloud After Effects submitter on your artist workstation using the
   Deadline Cloud Submitter Installers. When you install the submitter, you can choose
   between User Install (no admin required) or System Install (Windows only,
   requires admin). macOS users must use User Install.

   - **User Install**: Installs to user
     directory without admin privileges. The submitter will be a standalone
     window rather than a dockable panel.

     - Windows: `C:\Users\<user>\DeadlineCloudSubmitter\Submitters\AfterEffects\AE<version>`
     - macOS: `/Users/<user>/Library/Preferences/Adobe/After Effects/<version>/Scripts/ScriptUI Panels`

   - **System Install** (Windows only):
     Installs to Adobe After Effects installation directory as a dockable
     panel.

     - Windows: `C:\Program Files\Adobe\Adobe After Effects
   <version>\Support Files\Scripts\Script UI Panels`

## Installation

To install the Deadline Cloud submitter for After Effects, prepare the following environment:

- Windows or macOS workstation.
- Adobe After Effects 24, 25, or 26 installation.
- Python 3.9 or higher.
- Access to an Deadline Cloud farm with either:

  - A service-managed fleet with After Effects available (via custom conda package).
  - A customer-managed fleet with After Effects and licensing set up.

### Prerequisites

Before installing the submitter, complete the following steps:

1. Install the Deadline Cloud CLI and Deadline Cloud monitor by running the Deadline Cloud submitter and monitor installers from the downloads section of the Deadline Cloud service in your AWS console.
2. Enable script permissions in After Effects. The submitter requires the ability to write files and send communication over the network to function properly. By default, After Effects scripts are not allowed to perform these actions. For more information, see [Adobe's scripts reference](https://helpx.adobe.com/after-effects/using/scripts.html "https://helpx.adobe.com/after-effects/using/scripts.html") on the Adobe website.

To allow scripts to write files or send communication over a network, complete the steps for your operating system:

    * **Windows**: Choose **Edit** > **Preferences** > **Scripting & Expressions** > select **Allow Scripts To Write Files And Access Network**.
    * **macOS**: Choose **After Effects** > **Settings** > **Scripting & Expressions** > select **Allow Scripts To Write Files And Access Network**.

### Installing the submitter

The After Effects submitter extension allows you to submit jobs to Deadline Cloud directly from within After Effects.

###### Note

During the installer process, you choose between User Install or System Install. macOS users default to User Install, because automatic System Install is currently not supported on macOS (manual System Install is still possible for admin users). Read only the section below that matches your selection.

#### User install

1. Download the Deadline Cloud submitter installer by following [Step 1: Install the Deadline Cloud Submitter](submitter.md#submitter-installation "submitter.md#submitter-installation").
2. Run the installer (no admin required).
3. Follow the prompts and select the After Effects submitter and choose the major version (for example, 24, 25, or 26).
4. The submitter is installed based on your operating system:

   - **macOS**: The installer automatically places `DeadlineCloudSubmitter(User).jsx` and `DeadlineCloudSubmitter_Assets` into your After Effects user preferences directory for all minor versions of the selected major version:

   ```
   /Users/<user>/Library/Preferences/Adobe/After Effects/<version>/Scripts/ScriptUI Panels
   ```

   The submitter appears in the **Window** menu in After Effects.
   - **Windows**: The submitter is installed to a standalone location by default:

   ```
   C:\Users\<user>\DeadlineCloudSubmitter\Submitters\AfterEffects\AE<version>
   ```

   You will need to run the script manually using **File** > **Scripts** > **Run Script File**.

#### System install

###### Note

Automatic macOS system install is not yet supported by the submitter installer. macOS admin users can perform a manual system install by copying files to the application directory (see [Manual installation (alternative)](#after-effects-manual-install "#after-effects-manual-install")).

1. Download the Deadline Cloud submitter installer by following [Step 1: Install the Deadline Cloud Submitter](submitter.md#submitter-installation "submitter.md#submitter-installation").
2. **Windows only**: Right-click the installer and choose **Run as Admin**.
3. Follow the prompts and select the After Effects submitter. It is installed to:

   - **Windows**: `C:\Program Files\Adobe\Adobe After Effects <version>\Support Files\Scripts\Script UI Panels`
   - **macOS** (manual): `/Applications/Adobe After Effects <version>/Scripts/ScriptUI Panels`

#### Final setup steps

1. After installing using the submitter installer, ensure you log into your Deadline Cloud user profile by running `deadline auth login` in the Terminal/PowerShell or logging in using Deadline Cloud monitor.
2. To install the necessary dependencies used by the After Effects submitter, run the following in your local Terminal or Command Prompt:

```
pip install fonttools
```

3. Restart After Effects if it was open.

#### Manual installation (alternative)

If you prefer to install manually, you can copy the submitter files directly:

1. Locate the `DeadlineCloudSubmitter.jsx` file and the `DeadlineCloudSubmitter_Assets` folder in the `dist` folder of the [deadline-cloud-for-after-effects repository](https://github.com/aws-deadline/deadline-cloud-for-after-effects "https://github.com/aws-deadline/deadline-cloud-for-after-effects") on the GitHub website.
2. Copy both to the **ScriptUI Panels** folder within your After Effects installation:

   - **Windows**: `Program Files\Adobe\Adobe After Effects <version>\Support Files\Scripts\Script UI Panels`
   - **macOS**: `Applications/Adobe After Effects <version>/Scripts/Script UI Panels`

3. Restart After Effects if it was open.

#### Setting up After Effects with your Deadline Cloud farm

After Effects conda packages are available in Deadline Cloud service-managed fleets. For the list of supported versions, see the [Deadline Cloud user guide](create-queue-environment.md "create-queue-environment.md"). If you want to build a conda channel that contains a different After Effects conda package, follow the [instructions for creating custom conda channels](../developerguide/configure-jobs-s3-channel.md "../developerguide/configure-jobs-s3-channel.md").

You can also use the After Effects conda recipe in the [deadline-cloud-samples package](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/aftereffects-25.1 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/aftereffects-25.1") on the GitHub website as a reference when building the package.

Jobs created by this submitter require the `aerender` executable to be available on the PATH of the user that runs your jobs. Alternatively, you can set the `AERENDER_EXECUTABLE` environment variable to point to the aerender executable.

#### Updating the submitter

To update the submitter to the latest version, download and run the latest submitter installer.

## Using the After Effects submitter

To use the Deadline Cloud submitter for After Effects, ensure your farm is configured with an After Effects-capable fleet (see [Setting up After Effects with your Deadline Cloud farm](#after-effects-setup-farm "#after-effects-setup-farm")) and have the submitter installed. Log into Deadline Cloud monitor or provide AWS credentials using a configuration profile for Deadline Cloud access.

### Submit a job

###### Note

Follow the instructions below that match the install type you selected during installation.

#### User install - macOS

1. Launch Adobe After Effects.
2. Open the submitter by choosing **Window** > **DeadlineCloudSubmitter(User).jsx**.
3. Follow the steps in [Submitting your job](#after-effects-submitting-your-job "#after-effects-submitting-your-job") below.

#### User install - Windows

1. Launch Adobe After Effects.
2. Open the submitter by choosing **File** > **Scripts** > **Run Script File**. Navigate to the `DeadlineCloudSubmitter.jsx` file and select it to run the submitter. If you recently closed the submitter, you can reopen it by choosing **File** > **Scripts** > **Recent Script Files** and selecting the `DeadlineCloudSubmitter.jsx` file.
3. Follow the steps in [Submitting your job](#after-effects-submitting-your-job "#after-effects-submitting-your-job") below.

#### System install

1. Launch After Effects as Admin (Windows) or with appropriate permissions (macOS).
2. Open the submitter by choosing **Window** > **DeadlineCloudSubmitter.jsx**.
3. Follow the steps in [Submitting your job](#after-effects-submitting-your-job "#after-effects-submitting-your-job") below.

#### Submitting your job

1. Choose **Open Render Queue** on the submitter. Add any composition to your render queue and set up your render settings, output module, and output path.
2. Choose **Refresh** on the submitter to see your composition in the composition list.
3. Select your composition you want to render and choose **Submit** to submit a render job. For details on available settings, see [After Effects-specific settings](#after-effects-specific-settings "#after-effects-specific-settings") below.
4. If you see a warning popup window with "You are about to run the script contained in file", you can suppress the warning by following the instruction in the popup.
5. Install any Python libraries if prompted and choose the **Login** button in the bottom left if you are not logged in.
6. Set the farm and queue you are submitting to using the **Settings** button, and choose **Submit**.

###### Note

The After Effects submitter calls the Deadline Cloud GUI submitter to complete job submission. If you encounter any issues on the GUI submitter, see the [deadline-cloud library](https://github.com/aws-deadline/deadline-cloud "https://github.com/aws-deadline/deadline-cloud") on the GitHub website for help.

### Shared job settings

The following settings apply to the entire job:

- **Farm Selection** - Choose which farm your job will render on.
- **Queue Selection** - Select the specific queue within your chosen farm.
- **Job Name** - Give your render job a descriptive name.
- **Job Description** - Add optional details about your render job.
- **Priority** - Set job priority for queue management.
- **Initial State** - Control whether the job starts immediately or remains paused.
- **Max Failed Tasks Count** - Set the maximum number of tasks that can fail before the job is marked as failed.
- **Max Retries Per Task** - Set the number of times a failed task is retried.
- **Max Worker Count** - Set the maximum number of workers that can work on this job simultaneously.

### After Effects-specific settings

The following settings are specific to After Effects rendering:

- **Composition Selection** - Select which composition from your render queue to submit.
- **Frames Per Task** - (For image sequences) Specify how many frames each task should render. By default, Deadline Cloud creates one task for every frame. Increasing this value can speed up rendering in jobs where each frame renders quickly.
- **Multi-Frame Rendering** - Enable After Effects multi-frame rendering. You can also specify the max percentage of CPU usage to allocate towards rendering. For more information, see [Adobe's multi-frame rendering documentation](https://helpx.adobe.com/after-effects/using/multi-frame-rendering.html "https://helpx.adobe.com/after-effects/using/multi-frame-rendering.html") on the Adobe website.
- **Timeout** - (Optional) Configure timeout settings (days, hours, and minutes) to handle unexpected cases where a task may become unresponsive. The default timeout is 2 days.
- **Output Type** - Automatically detected based on your render queue settings (image sequence or video).
- **Output Path** - Directory where rendered files will be saved (from your render queue settings).

For information about the other submitter tabs, see the [Deadline Cloud guide for using a submitter](jobs-using-submitter.md "jobs-using-submitter.md").

### Font attachment system

Fonts used in the submitted composition are detected by the submitter and are automatically added as job attachments on submission. Fonts are installed on the worker before the render starts and are removed when the job ends.

**Supported font types**:

- OpenType (`.otf`).
- TrueType (`.ttf`).
- TrueType Collection (`.ttc`) - majority supported.
- [Adobe Fonts](https://fonts.adobe.com/ "https://fonts.adobe.com/") on the Adobe website.
- Windows bitmap fonts (`.fon`) - only supported on Windows machines.

**Troubleshooting fonts**:

If fonts are missing at render time:

1. Check that fonts are installed on your system:

   - **Windows**: Open **Settings** > **Personalization** > **Fonts** to view installed fonts.
   - **macOS**: Open Font Book application to view installed fonts.

2. Verify fonts are included in job attachments: After choosing **Submit** in the submitter, check the **Job Attachments** tab in the submission dialog to confirm your fonts are listed.

**Adobe Creative Cloud Fonts**:

For Deadline Cloud to use fonts distributed through Adobe Creative Cloud, they must be made available for all non-Adobe apps on your workstation.

To install fonts for non-Adobe apps in Creative Cloud:

1. Open Adobe Creative Cloud Desktop.
2. Choose **Adobe Fonts** on the account sidebar under **Your plan** to show the Adobe Fonts panel.
3. Choose **Added fonts** on the **Adobe Fonts** sidebar to show your added fonts.
4. Choose **Install family** next to the fonts you would like to make available for non-Adobe apps.

### Viewing the job bundle

To submit a job, the submitter first generates a [job bundle](../developerguide/build-job-bundle.md "../developerguide/build-job-bundle.md"), and then uses functionality from the deadline-cloud package to submit the job bundle to your render farm to run.

If you want to see the job that will be submitted to your farm:

1. Use the **Export Bundle** button in the submitter to export the job bundle in the job history directory (default: `~/.deadline/job_history`).
2. If you want to submit the job from the export, rather than through the submitter, you can use the Deadline Cloud application to submit that bundle to your farm.

## Troubleshooting

The following sections address common issues and questions about using the After Effects submitter with Deadline Cloud.

### Rendering questions

**Q: Can I run custom ExtendScript (.jsx) scripts on Deadline Cloud workers?**

A: Yes, with limitations. The After Effects conda package on service-managed fleets packages the renderer and its dependencies, not a full After Effects installation. You can run custom `.jsx` scripts on workers using host configurations. However, scripts that make networking calls will not work on workers, because the "Allow Scripts To Write Files And Access Network" preference is a local user setting that cannot be configured without a full installation.

### Troubleshooting questions

**Q: My After Effects job is timing out or I'm seeing PermissionDenied errors during session cleanup. What's going on?**

A: This issue is typically caused by After Effects hanging due to a UI dialog (for example, `alert()`, `confirm()`) that cannot be dismissed in headless mode. The symptoms are:

- **Timeout errors**: The process hangs waiting for user interaction that will never come, resulting in a `subprocess.TimeoutExpired` error.
- **PermissionDenied errors during session cleanup**: The hung After Effects process holds locks on Adobe DLLs (`AdobeXMP.dll`, `dvacore.dll`, `dynamiclink.dll`, etc.). When the worker attempts session cleanup, it produces `Access to the path '<file>' is denied` errors.

Fixing the root cause (the hung process) resolves both the timeout and the cleanup errors. Remove all UI calls from scripts intended for farm execution.

**Troubleshooting tip**: Try running the same workflow on a Windows workstation with the After Effects UI to eliminate any non-Deadline Cloud-specific issues.

**Q: I'm getting "aerender Error: Could not read from source" when my job runs. What's wrong?**

A: This error typically means the output path was not set in your composition's render queue before submitting the job. The After Effects submitter requires that you add your composition to the render queue and set up your render settings, output module, and output path before submission. See [Using the After Effects submitter](#after-effects-use-submitter "#after-effects-use-submitter") for the full submission workflow.

**Q: My job fails at "Install Fonts to Worker" with `AddFontResource failed to load`. What do I do?**

A: Some fonts are not installable on certain operating systems due to OS-specific limitations. When the font manager attempts to install an unsupported font on a worker, it fails with an error like:

```
OSError: AddFontResource failed to load "...\tempFonts\HelveticaNeue-CondensedBlack.ttc"
```

To resolve this issue, try the following steps:

1. Check whether the font is actually used in your composition - it may have been uploaded by mistake.
2. If the font is not needed, remove it from the job attachments in the submitter before resubmitting.
3. If the font is needed, try substituting a different font that is compatible with Windows (Deadline Cloud only runs After Effects on Windows workers).
4. As a workaround, you can convert text layers to shapes in After Effects. For more information, see [Creating shapes from text](https://helpx.adobe.com/after-effects/using/creating-shapes-masks.html "https://helpx.adobe.com/after-effects/using/creating-shapes-masks.html") on the Adobe website. Note that conversion removes the font dependency entirely and is one-way. You will no longer be able to edit the text or use text-specific features.
5. If none of the preceding options work, [create an issue in the repository](https://github.com/aws-deadline/deadline-cloud-for-after-effects/issues "https://github.com/aws-deadline/deadline-cloud-for-after-effects/issues") on the GitHub website for further investigation.

**Tip**: You can check if a font is installable on Windows by double-clicking the font file on a Windows machine. If it opens and shows an "Install" option, the font is supported.

### Error: Couldn't find Python 3 or higher on your PATH

**For macOS**:

1. Open Terminal and run the following commands: `where python` and `where python3`. If you're not getting any results, you need to install Python for your workstation.
2. If you do not have `python3` CLI installed but you have `python`, run `python --version` to check if you have Python 3.9 or higher. If not, install Python 3.9 or higher first and add it to your path.
3. After you get results from the version check and where check, then check which Python executable is actively being used. Run `which python` and `which python3`. If you're not getting any results, you need to add your Python CLI to your zsh `$PATH`.
4. You must also ensure you're adding the Python that was used to install the Deadline Cloud CLI. Run `python -m pip list` and/or `python3 -m pip list` to verify, and add to `$PATH` whichever Python applies.
5. Add the `bin` folder containing the Python CLI to your path by editing `~/.zshrc` (and `~/.bashrc` if applicable) and updating the `$PATH`. For example, if your Python and Deadline Cloud CLI are under `/Library/Frameworks/Python.framework/Versions/3.13/bin`, add the following line to your `~/.zshrc` file at the end of the file so it gets final priority when the `$PATH` is evaluated:

```
export PATH=$PATH:/Library/Frameworks/Python.framework/Versions/3.13/bin
```

6. Save and exit, then run `source ~/.zshrc`.
7. Now if you run `python --version` and `deadline --version`, you have access to both executables and After Effects does too. Retry job submission. Your output should follow a pattern similar to:

```
user@7cf34df03377 ~ % which python3
/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
user@7cf34df03377 ~ % where deadline
/Library/Frameworks/Python.framework/Versions/3.13/bin/deadline
```

**For Windows**:

1. Open Command Prompt (or PowerShell).
2. Run `where python`, `where python3`, `where py`, and `where deadline` to locate the executables. In PowerShell, use `Get-Command python` instead of `where python`.
3. Press Windows + S and search for "Edit the system environment variables". This step requires admin access. Choose **Environment Variables...**.
4. Depending on whether the Deadline Cloud CLI was a user installation or system installation, select the **Path** variable under either **User variables** or **System variables**, then choose **Edit**.
5. In the Edit window, choose **New** and paste the path to the folder containing your Python and Deadline Cloud executables.
6. Ensure that the binary folders containing deadline and your Python CLI have been added. Deadline will be located in the DeadlineCloudSubmitter folder when installed from the submitter installer or under a Python folder if managed by pip. If you're managing the Deadline Cloud CLI with pip, run `python -m pip list` and/or `python3 -m pip list` to ensure you add the Python containing the Deadline Cloud CLI to your path.

### Error: Deadline Not Found

1. Open your Terminal or Command Prompt and run `deadline --version` to verify installation.
2. Then follow the troubleshooting steps above for Python for your operating system and verify that deadline is on your `$PATH`.
3. If you have multiple Python installations and manage the Deadline Cloud CLI using pip, verify that the Python on your `$PATH` is the Python that managed your Deadline Cloud CLI installation. Run `python -m pip list` and `python3 -m pip list` to verify.

### Error: Missing job template

Example error: `Missing job template at /Applications/Adobe After Effects 2025/Scripts/ScriptUI Panels/DeadlineCloudSubmitter_Assets/JobTemplate`.

This error occurs when the `DeadlineCloudSubmitter_Assets` folder is missing or not located next to the `DeadlineCloudSubmitter.jsx` script file.

1. Locate where your `DeadlineCloudSubmitter.jsx` script is installed or moved to.
2. Ensure the `DeadlineCloudSubmitter_Assets` folder is in the same directory as the script.
3. If the assets folder is missing, copy it from your original installation source to the same location as the JSX script.
4. Restart After Effects and try running the submitter again.

### Warning: Unsupported After Effects version detected

This warning means you are using an After Effects version that is not available in the deadline-cloud conda channel. For example, if you're using After Effects 24.3, but the channel supports only 24.6.

If you continue, the default major version in use locally is filled in the CondaPackages field, but your job submission may fail unless you have created a custom conda channel with your specific After Effects version and included this channel in the CondaChannels parameter.

To resolve this, you can either:

1. Switch to a supported After Effects version.
2. Acknowledge the warning and proceed (at your own risk).
3. Create a custom conda channel with your desired After Effects version.

### Command prompt flashes on Windows after submission

Go to the Windows Start menu and search for "Manage app execution aliases". Then disable the `python3.exe` and `python.exe` aliases manually and retry submission.

### Font with an unsupported extension was found

See [Font attachment system](#after-effects-font-attachment "#after-effects-font-attachment") for supported font types.

## After Effects plugins

You can make After Effects plugins available on service-managed fleet workers by
using either a conda package or a host configuration script. Plugins that are packaged
as a conda package install into the After Effects `Plug-ins` directory when
the conda environment activates. Plugins that require a full installer instead use a
host configuration script that runs when each worker launches. To package several
`.aex` plugins together, use the [aftereffects-plugin-bundle
conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/aftereffects-plugin-bundle "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/aftereffects-plugin-bundle") on the GitHub website.

### Saber

Saber is a visual effects plugin for After Effects. You can build a conda package
that installs the `Saber.aex` plugin on Windows workers with the
aftereffects-saber conda recipe, and then add it to a custom conda channel. You can
also use the recipe as a template for packaging other `.aex` plugins.

Conda recipe: [aftereffects-saber
conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/aftereffects-saber "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/aftereffects-saber") on the GitHub website.

### Red Giant

You can install Maxon Red Giant on your workers with a host configuration script
that fetches and silently installs the Red Giant installer when each worker
launches. The script has been tested and verified on Windows GPU service-managed
fleets. If a persistent volume is attached to the fleet, the script installs the
software once and restores it on later boots to reduce worker startup time.

Host configuration script: [aftereffects\_redgiant](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/aftereffects/aftereffects_redgiant "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/aftereffects/aftereffects_redgiant") on the GitHub website.

## Advanced configurations

### Using unsupported versions

Deadline Cloud only supports and tests the workstation and worker software versions in the
table above. When using the submitter, the worker will attempt to install the same
version as used on the workstation. This installation fails if the workstation version of
After Effects does not appear in the version table above.

If you require an unsupported version of After Effects, you have the following
options:

- When submitting the job from After Effects, you may override the
  CondaPackages queue parameter to specify a supported version to use on the
  worker (for example, `aftereffects=2025`). This override might or might not
  work, depending on the features used by your scene and how After Effects
  works with scenes from your workstation version.
- You may build a custom conda recipe and channel for your desired version
  to be installed on the worker. Use the conda recipe for a supported version
  linked below as a starting point, and package your desired version in a
  custom conda channel. For more information about creating custom conda
  channels, see [Creating
  custom conda channels](../developerguide/configure-jobs-s3-channel.md "../developerguide/configure-jobs-s3-channel.md").

## Open source resources

The submitter and standalone job bundle are open source and available on the GitHub website:

- [Deadline Cloud
  for After Effects](https://github.com/aws-deadline/deadline-cloud-for-after-effects "https://github.com/aws-deadline/deadline-cloud-for-after-effects")
- [Standalone
  After Effects job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/afterfx_render_one_task "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/afterfx_render_one_task")
