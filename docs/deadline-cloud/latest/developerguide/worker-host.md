# Worker host setup and configuration

A worker host refers to a host machine that runs a Deadline Cloud worker. This section explains how
 to set up the worker host and configure it for your specific needs. Each worker host runs a
 program called a *worker agent*. The worker agent is responsible
 for:


* Managing the worker life cycle.
* Synchronizing assigned work, its progress and results.
* Monitoring running work.
* Forwarding logs to configured destinations.
We recommend that you use the provided Deadline Cloud worker agent. The worker agent is open source
 and we encourage feature requests, but you can also develop and customize to fit your
 needs.

To complete the tasks in the following sections, you need the following:


Linux

* A Linux-based Amazon Elastic Compute Cloud (Amazon EC2) instance. We recommend Amazon Linux
 2023.
* `sudo` privileges
* Python 3.9 or above


Windows

* A Windows-based Amazon Elastic Compute Cloud (Amazon EC2) instance. We recommend
 Windows Server 2022.


* Administrator access to the worker host


* Python 3.9 or above installed for all users



## Create and configure a Python virtual
 environment


You can create a Python virtual environment on Linux if you have installed Python
 3.9 or greater and placed it in your `PATH`.


###### Note

On Windows, agent files must be installed into Python’s global site-packages
 directory. Python virtual environments are not currently supported.


###### To create and activate a Python virtual environment

1. Open a terminal as the `root` user (or use `sudo`
 / `su`).
2. Create and activate a Python virtual environment.



```
`python3 -m venv /opt/deadline/worker`
`source /opt/deadline/worker/bin/activate`
`pip install --upgrade pip`
```

## Install Deadline Cloud worker agent


After you've set up your Python and created a virtual environment on Linux, install
 the Deadline Cloud worker agent Python packages.


### To install the worker agent Python packages



Linux

1. Open a terminal as the `root` user (or use
 `sudo` / `su`).
2. Download and install the Deadline Cloud worker agent packages from
 PyPI:



```
`/opt/deadline/worker/bin/python -m pip install deadline-cloud-worker-agent`
```


Windows

1. Open an administrator command prompt or PowerShell
 terminal.
2. Download and install the Deadline Cloud worker agent packages from
 PyPI:



```
`python -m pip install deadline-cloud-worker-agent`
```



When your Windows worker host requires long path names (greater than 250
 characters), you must enable long path names as follows:


1. Make sure that the long path registry key is enabled. For more
 information, see [Registry setting to enable log paths](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry#registry-setting-to-enable-long-paths "https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry#registry-setting-to-enable-long-paths") on the Microsoft
 website.
2. Install the Windows SDK for Desktop C++ x86 Apps. For more
 information, see [Windows SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/ "https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/") in the Windows Dev Center.
3. Open the Python installation location in your environment where
 the worker agent is installed. The default is `C:\Program
 Files\Python311`. There is an executable file named
 `pythonservice.exe`.
4. Create a new file called `pythonservice.exe.manifest`
 in the same location. Add the following: 



```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <assemblyIdentity type="win32" name="pythonservice" processorArchitecture="x86" version="1.0.0.0"/>
  <application xmlns="urn:schemas-microsoft-com:asm.v3">
    <windowsSettings>
      <longPathAware xmlns="http://schemas.microsoft.com/SMI/2016/WindowsSettings">true</longPathAware>
    </windowsSettings>
  </application>
</assembly>
```
5. Open a command prompt and run the following command in the
 location of the manifest file that you created:



```
"C:\Program Files (x86)\Windows Kits\10\bin\10.0.26100.0\x86\mt.exe" -manifest pythonservice.exe.manifest -outputresource:pythonservice.exe;#1
```

You should see output similar to the following:



```
Microsoft (R) Manifest Tool
Copyright (c) Microsoft Corporation.
All rights reserved.
```
The worker is now able to access long paths. To clean up, remove the
 `pythonservice.exe.manifest` file and uninstall the
 SDK.


## Configure the Deadline Cloud worker agent


You can configure the Deadline Cloud worker agent settings in three ways. We recommend you use
 the operating system setup by running the `install-deadline-worker`
 tool.


The worker agent does not support running as a domain user on Windows. To run a job as
 a domain user, you can specify a domain user account when you configure a queue user for
 running jobs. For more information, see step 7 in [Deadline Cloud queues](../userguide/queues.md "../userguide/queues.md") in the
 *AWS Deadline Cloud User Guide*.


**Command line arguments** — You can specify
 arguments when you run the Deadline Cloud worker agent from the command line. Some configuration
 settings are not available through command line arguments. To see all the available
 command line arguments, enter `deadline-worker-agent --help`. 


**Environment variables** — You can configure the
 Deadline Cloud worker agent by setting environment variable beginning with
 `DEADLINE_WORKER_`. For example, to see all the available command line
 arguments you can use `export DEADLINE_WORKER_VERBOSE=true` to set the worker
 agent's output to verbose. For more examples and information, see
 `/etc/amazon/deadline/worker.toml.example` on Linux or
 `C:\ProgramData\Amazon\Deadline\Config\worker.toml.example` on
 Windows.


**Configuration file** — When you install the
 worker agent, it creates a configuration file located at
 `/etc/amazon/deadline/worker.toml` on Linux or
 `C:\ProgramData\Amazon\Deadline\Config\worker.toml` on Windows. The
 worker agent loads this configuration file when it starts. You can use the example
 configuration file (`/etc/amazon/deadline/worker.toml.example` on Linux or
 `C:\ProgramData\Amazon\Deadline\Config\worker.toml.example` on Windows)
 to tailor the default worker agent configuration file for your specific needs. 


Finally, we recommend you enable auto shutdown for the worker agent
 *after* your software is deployed and working as expected. This
 allows the worker fleet to scale up when needed and to shut down when a job finishes.
 Auto scaling helps ensure you're only using the resources needed. To enable an instance
 started by the auto scaling group to shut down, you must add
 `shutdown_on_stop=true` to the `worker.toml` configuration
 file.


###### To enable auto shutdown

As a `root` user:

* Install the worker agent with parameters
 `--allow-shutdown`.



Linux
Enter:



```
`/opt/deadline/worker/bin/install-deadline-worker \
 --farm-id `FARM_ID` \
 --fleet-id `FLEET_ID` \
 --region `REGION` \
 --allow-shutdown`
```


Windows
Enter:



```
`install-deadline-worker ^
 --farm-id `FARM_ID` ^
 --fleet-id `FLEET_ID` ^
 --region `REGION` ^
 --allow-shutdown`
```

## Create job users and groups


This section describes the required user and group relationship between the agent user
 and the `jobRunAsUser` defined on your queues.


The Deadline Cloud worker agent should run as a dedicated agent-specific user on the host. You
 should configure the `jobRunAsUser` property of Deadline Cloud queues so that workers
 will run the queue jobs as a specific operating system user and group. This means you
 can control the shared filesystem permissions that your jobs have. It also provides as
 an important security boundary between your jobs and the worker agent user.


**Linux job users and groups**


To set up a local worker agent user and `jobRunAsUser`, ensure you meet the
 following requirements. If you are using a Linux Pluggable Authentication Module (PAM)
 such as Active Directory or LDAP, your procedure may be different.


The worker agent user and the shared `jobRunAsUser` group are set when you
 install the worker agent. The defaults are `deadline-worker-agent` and
 `deadline-job-users`, but you can change those when you install the
 worker agent.



```
install-deadline-worker \
    --user `AGENT_USER_NAME` \
    --group `JOB_USERS_GROUP`
```

Commands should be run as the root user. 



* Each `jobRunAsUser` should have a matching primary group. Creating
 a user with the `adduser` command usually creates a matching primary
 group.



```
adduser -r -m `jobRunAsUser`
```
* The primary group of the `jobRunAsUser` is a secondary group for
 the worker agent user. The shared group allows the worker agent to make files
 available to the job as it is running. 



```
usermod -a -G `jobRunAsUser` `deadline-worker-agent`
```
* The `jobRunAsUser` must be a member of the shared job group.



```
usermod -a -G `deadline-job-users` `jobRunAsUser`
```
* The `jobRunAsUser` must not belong to the worker agent user's
 primary group. Sensitive files written by the worker agent are owned by the
 agent's primary group. If a `jobRunAsUser` is part of this group,
 worker agent files may be accessible to jobs running on the worker.
* The default AWS Region must match the Region of the farm that the worker
 belongs to. This should be applied to all `jobRunAsUser` accounts on
 the worker.



```
sudo -u `jobRunAsUser` aws configure set default.region `aws-region`
```
* The worker agent user must be able to run `sudo` commands as the
 `jobRunAsUser`. Run the following command to open an editor to
 create a new sudoers rule:



```
visudo -f /etc/sudoers.d/deadline-worker-job-user
```

Add the following to the file:



```
# Allows the Deadline Cloud worker agent OS user to run commands
 # as the queue OS user without requiring a password.
deadline-worker-agent ALL=(jobRunAsUser) NOPASSWD:ALL
```

The following diagram illustrates the relationship between the agent user and the
 `jobRunAsUser` users and groups for queues associated with the
 fleet.



![An illustration of the relationship between agent-users and the jobRunAsUser on queues.](/images/deadline-cloud/latest/developerguide/images/worker_users_and_groups.png)

**Windows users**


To use a Windows user as the `jobRunAsUser`, it must meet the following
 requirements:



* All queue `jobRunAsUser` users must exist.
* Their passwords must match the value of the secret specified in their queue’s
 `JobRunAsUser` field. For instructions, see step 7 in [Deadline Cloud
 queues](../userguide/queues.md "../userguide/queues.md") in the *AWS Deadline Cloud User Guide*.
* The agent-user must be able to log on as those users.
