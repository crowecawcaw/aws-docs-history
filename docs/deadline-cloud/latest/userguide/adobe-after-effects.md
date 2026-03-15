# Adobe After Effects

###### Note

For more information about installing, configuring, and using this integration on your
workstation, see the [After
Effects integration user guide on GitHub](https://aws-deadline.github.io/after-effects/ "https://aws-deadline.github.io/after-effects/").

Adobe After Effects is a professional digital visual effects, motion graphics, and
compositing application. After Effects is fully supported by Deadline Cloud with comprehensive
integration including submitters and conda packages for increased rendering performance.

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
     - macOS: `/Users/<user>/DeadlineCloudSubmitter/Submitters/AfterEffects/AE<version>`

   - **System Install** (Windows only):
     Installs to Adobe After Effects installation directory as a dockable
     panel.
     - Windows: `C:\Program Files\Adobe\Adobe After Effects
<version>\Support Files\Scripts\Script UI Panels`

## Using the After Effects submitter

### Launching the submitter

###### To launch the After Effects submitter

1. Launch Adobe After Effects.
2. Update the following settings within After Effects to allow scripts to
   write files and send communication over a network:
   - For Windows, choose **Edit** > **Preferences** > **Scripting & Expressions**,
     and then choose **Allow scripts to write files and access
     networks**.
   - For macOS, choose **After Effects** > **Settings** > **Scripting & Expressions**,
     and then choose **Allow scripts to write files and access
     networks**.

3. Restart After Effects.
4. Open the Deadline Cloud submitter based on your install type:
   - For a system install, select **Window**, then
     choose **DeadlineCloudSubmitter.jsx**.
   - For a user install, choose **File** > **Scripts** > **Run Script File**, and
     then locate and select **DeadlineCloudSubmitter.jsx**
     .

5. (Optional) If the submitter is closed and you used a user install, reopen
   it by choosing **File** > **Scripts**
   > **Recent Script Files** and selecting **DeadlineCloudSubmitter.jsx**.

### Submitting a render job

###### To submit a render job from After Effects

1. Choose **Open Render Queue** on the submitter.
2. Add a composition to your render queue and set up your render settings,
   output module, and output path.
3. Choose **Refresh** on the submitter to see your
   composition in the composition list.
4. Select the composition to render and choose **Submit** to
   submit a render job.
5. If you see a warning about running a script file, suppress the warning
   messages by following the instructions in the popup.
6. Install any Python libraries if prompted.
7. Choose **Submit** to send your job to Deadline Cloud.
8. Monitor the job and download the output using the Deadline Cloud monitor.

## Advanced configurations

### Using unsupported versions

Deadline Cloud only supports and tests the workstation and worker software versions in the
table above. When using the submitter, the worker will attempt to install the same
version as used on the workstation. This will fail if the workstation version of
After Effects does not appear in the version table above.

If you require an unsupported version of After Effects, you have the following
options:

- When submitting the job from After Effects, you may override the
  CondaPackages queue parameter to specify a supported version to use on the
  worker (for example, `aftereffects=2025`). This may or may not
  work, depending on the features used by your scene and how After Effects
  works with scenes from your workstation version.
- You may build a custom conda recipe and channel for your desired version
  to be installed on the worker. Use the conda recipe for a supported version
  linked below as a starting point, and package your desired version in a
  custom conda channel. For more information about creating custom conda
  channels, see [Creating
  custom conda channels](../developerguide/configure-jobs-s3-channel.md "../developerguide/configure-jobs-s3-channel.md").

## Open source resources

The submitter is open source and available on GitHub:

- [Deadline Cloud
  for After Effects](https://github.com/aws-deadline/deadline-cloud-for-after-effects "https://github.com/aws-deadline/deadline-cloud-for-after-effects")
- [Standalone
  After Effects job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/afterfx_render_one_task "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/afterfx_render_one_task") is available on GitHub.
- [Comprehensive user
  guide](https://aws-deadline.github.io/after-effects/ "https://aws-deadline.github.io/after-effects/") is available.
