

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
[See the AWS documentation website for more details](http://docs.aws.amazon.com/deadline-cloud/latest/developerguide/install-software.html)

**Installing multiple adaptors on the same worker**  
If you install more than one DCC adaptor on the same worker, install each adaptor into its own Python virtual environment. Adaptors can pin different version ranges for shared Python packages (for example, `deadline` or `openjd-adaptor-runtime`). An environment with multiple adaptors might fail with a `ResolutionImpossible` error. It might also silently downgrade a shared package and break the adaptors that need the newer version.