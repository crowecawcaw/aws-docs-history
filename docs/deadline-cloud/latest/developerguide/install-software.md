

# Install and configure software required for jobs
<a name="install-software"></a>

After you set up the Deadline Cloud worker agent, you can prepare the worker host with any software that is required to run jobs.

When you submit a job to a queue with an associated `jobRunAsUser`, the job runs as that user. When a job is submitted with commands that are not an absolute path, that command must be found in the `PATH` of that user.

On Linux, you might specify the `PATH` for a user in one of the following:
+ their `~/.bashrc` or `~/.bash_profile`
+ system configuration files such as `/etc/profile.d/*` and `/etc/profile`
+ shell startup scripts: `/etc/bashrc`.

On Windows, you might specify the `PATH` for a user in one of the following:
+ their user-specific environment variables
+ the system-wide environment variables

## Install digital content creation tool adaptors
<a name="install-adaptors"></a>

Deadline Cloud provides Open Job Description (OpenJD) adaptors for using popular digital content creation (DCC) applications. An adaptor is a command-line program that runs the DCC application on the worker host, keeps the application loaded between tasks, reports render progress to the job's logs, and applies path mapping. For more information, see [Adaptor packages](conda-package.md#conda-package-adaptors).

To use these adaptors in a customer-managed fleet, you must install the DCC software and the application adaptors. Then, ensure the software's executable programs are available on the system search path (for example, in the `PATH` environment variable).

To install a digital content creation (DCC) adaptor on a customer-managed fleet

1. Open a terminal:

   1. On Linux, open a terminal as the `root` user (or use `sudo` or `su`).

   1. On Windows, open an administrator command prompt or PowerShell terminal.

1. Install the adaptor package for your DCC application. The following example installs the Maya adaptor:

   ```
   pip install deadline-cloud-for-maya
   ```

   The following table lists the adaptor package name and documentation link for each supported DCC application. All adaptor packages are available on the GitHub website:


<table>
<thead>
  <tr><th>DCC application</th><th>Adaptor package</th></tr>
</thead>
<tbody>
  <tr><td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/userguide/adobe-after-effects.html">Adobe After Effects</a></td><td><a href="https://github.com/aws-deadline/deadline-cloud-for-after-effects">deadline-cloud-for-after-effects</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/userguide/autodesk-3ds-max.html">Autodesk 3ds Max</a></td><td><a href="https://github.com/aws-deadline/deadline-cloud-for-3ds-max">deadline-cloud-for-3ds-max</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/userguide/autodesk-maya.html">Autodesk Maya</a></td><td><a href="https://github.com/aws-deadline/deadline-cloud-for-maya">deadline-cloud-for-maya</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/userguide/autodesk-vred.html">Autodesk VRED</a></td><td><a href="https://github.com/aws-deadline/deadline-cloud-for-vred">deadline-cloud-for-vred</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/userguide/blender.html">Blender</a></td><td><a href="https://github.com/aws-deadline/deadline-cloud-for-blender">deadline-cloud-for-blender</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/userguide/autodesk-maya.html">Chaos V-Ray for Maya</a></td><td><a href="https://github.com/aws-deadline/deadline-cloud-for-maya">deadline-cloud-for-maya</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/userguide/foundry-nuke.html">Foundry Nuke</a></td><td><a href="https://github.com/aws-deadline/deadline-cloud-for-nuke">deadline-cloud-for-nuke</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/userguide/keyshot.html">KeyShot Studio</a></td><td><a href="https://github.com/aws-deadline/deadline-cloud-for-keyshot">deadline-cloud-for-keyshot</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/userguide/maxon-cinema-4d.html">Maxon Cinema 4D</a></td><td><a href="https://github.com/aws-deadline/deadline-cloud-for-cinema-4d">deadline-cloud-for-cinema-4d</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/userguide/autodesk-maya.html">Maxon Redshift for Maya</a></td><td><a href="https://github.com/aws-deadline/deadline-cloud-for-maya">deadline-cloud-for-maya</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/userguide/sidefx-houdini.html">SideFX Houdini</a></td><td><a href="https://github.com/aws-deadline/deadline-cloud-for-houdini">deadline-cloud-for-houdini</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/deadline-cloud/latest/userguide/epic-unreal-engine.html">Unreal Engine</a></td><td><a href="https://github.com/aws-deadline/deadline-cloud-for-unreal-engine">deadline-cloud-for-unreal-engine</a></td></tr>
</tbody>
</table>


**Installing multiple adaptors on the same worker**  
If you install more than one DCC adaptor on the same worker, install each adaptor into its own Python virtual environment. Adaptors can pin different version ranges for shared Python packages (for example, `deadline` or `openjd-adaptor-runtime`). An environment with multiple adaptors might fail with a `ResolutionImpossible` error. It might also silently downgrade a shared package and break the adaptors that need the newer version.