# Install and configure software required for jobs

After you set up the Deadline Cloud worker agent, you can prepare the worker host with any software
 that is required to run jobs.

When you submit a job to a queue with an associated `jobRunAsUser`, the job runs
 as that user. When a job is submitted with commands that are not an absolute path, that command 
 must be found in the `PATH` of that user.

On Linux, you might specify the `PATH` for a user in one of the following:


* their `~/.bashrc` or `~/.bash_profile`
* system configuration files such as `/etc/profile.d/*` 
 and `/etc/profile`
* shell startup scripts: `/etc/bashrc`.
On Windows, you might specify the `PATH` for a user in one of the following:


* their user-specific environment variables
* the system-wide environment variables

## Install digital content creation tool adaptors


Deadline Cloud provides OpenJobDescription adaptors for using popular digital content creation (DCC) 
 applications. To use these adaptors in a customer-managed fleet, you must install the DCC software 
 and the application adaptors. Then, ensure the software's executable programs are available on 
 the system search path (for example, in the `PATH` environment variable).


To install DCC adaptors on a customer-managed fleet

1. Open the a terminal.


	1. On Linux, open a terminal as the `root` user (or use 
	 `sudo` / `su`)
	2. On Windows, open an administrator command prompt or PowerShell terminal.
2. Install the Deadline Cloud adaptor packages.



```
pip install deadline deadline-cloud-for-maya deadline-cloud-for-nuke deadline-cloud-for-blender deadline-cloud-for-3ds-max
```
