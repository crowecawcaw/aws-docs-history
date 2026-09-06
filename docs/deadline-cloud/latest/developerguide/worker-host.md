

# Worker host setup and configuration
<a name="worker-host"></a>

A worker host refers to a host machine that runs a Deadline Cloud worker. This section explains how to set up the worker host and configure it for your specific needs. Each worker host runs a program called a *worker agent*. The worker agent is responsible for:
+ Managing the worker life cycle.
+ Synchronizing assigned work, its progress and results.
+ Monitoring running work.
+ Forwarding logs to configured destinations.

We recommend that you use the provided Deadline Cloud worker agent. The worker agent is open source and we encourage feature requests, but you can also develop and customize to fit your needs.

To complete the tasks in the following sections, you need the following:

------
#### [ Linux ]
+ A Linux-based Amazon Elastic Compute Cloud (Amazon EC2) instance. We recommend Amazon Linux 2023.
+ `sudo` privileges
+ Python 3.9 or above

------
#### [ Windows ]
+ A Windows-based Amazon Elastic Compute Cloud (Amazon EC2) instance. We recommend Windows Server 2022.
+ Administrator access to the worker host
+ Python 3.9 or above installed for all users

------

## Create and configure a Python virtual environment
<a name="python-virtual-env"></a>

You can create a Python virtual environment on Linux if you have installed Python 3.9 or greater and placed it in your `PATH`.

**Note**  
On Windows, agent files must be installed into Python's global site-packages directory. Python virtual environments are not currently supported.

**To create and activate a Python virtual environment**

1. Open a terminal as the `root` user (or use `sudo` / `su`).

1. Create and activate a Python virtual environment.

   ```
   python3 -m venv /opt/deadline/worker
   source /opt/deadline/worker/bin/activate
   pip install --upgrade pip
   ```

## Install Deadline Cloud worker agent
<a name="install-worker-agent"></a>

After you've set up your Python and created a virtual environment on Linux, install the Deadline Cloud worker agent Python packages.

### To install the worker agent Python packages
<a name="w2aac38c18c19b5"></a>

------
#### [ Linux ]

1. Open a terminal as the `root` user (or use `sudo` / `su`).

1. Download and install the Deadline Cloud worker agent packages from PyPI:

   ```
   /opt/deadline/worker/bin/python -m pip install deadline-cloud-worker-agent
   ```

------
#### [ Windows ]

1. Open an administrator command prompt or PowerShell terminal.

1. Download and install the Deadline Cloud worker agent packages from PyPI:

   ```
   python -m pip install deadline-cloud-worker-agent
   ```

------

When your Windows worker host requires long path names (greater than 250 characters), you must enable long path names as follows:

#### To enable long paths for Windows worker hosts
<a name="long-path"></a>

1. Make sure that the long path registry key is enabled. For more information, see [Registry setting to enable long paths](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry#registry-setting-to-enable-long-paths) on the Microsoft website.

1. Install the Windows SDK for Desktop C\+\+ x86 Apps. For more information, see [Windows SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/) on the Microsoft website.

1. Open the Python installation location in your environment where the worker agent is installed. The default is `C:\Program Files\Python311`. There is an executable file named `pythonservice.exe`.

1. Create a new file called `pythonservice.exe.manifest` in the same location. Add the following: 

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

1. Open a command prompt and run the following command in the location of the manifest file that you created:

   ```
   "C:\Program Files (x86)\Windows Kits\10\bin\10.0.26100.0\x86\mt.exe" -manifest pythonservice.exe.manifest -outputresource:pythonservice.exe;#1
   ```

   You should see output similar to the following:

   ```
   Microsoft (R) Manifest Tool
   Copyright (c) Microsoft Corporation.
   All rights reserved.
   ```

The worker is now able to access long paths. To clean up, remove the `pythonservice.exe.manifest` file and uninstall the SDK.

If jobs still fail with missing-file errors after you complete this procedure, the limit is being applied by the rendering application rather than by the worker agent. For more information, see [Why does my job fail on Windows when my file paths are long?](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/troubleshooting.html#troubleshooting-windows-long-paths) in the *AWS Deadline Cloud User Guide*.

## Configure the Deadline Cloud worker agent
<a name="worker-agent-config"></a>

You can configure the Deadline Cloud worker agent settings in three ways. We recommend you use the operating system setup by running the `install-deadline-worker` tool.

**Command line arguments** — You can specify arguments when you run the Deadline Cloud worker agent from the command line. Some configuration settings are not available through command line arguments. To see all the available command line arguments, enter `deadline-worker-agent --help`. 

**Environment variables** — You can configure the Deadline Cloud worker agent by setting environment variable beginning with `DEADLINE_WORKER_`. For example, to see all the available command line arguments you can use `export DEADLINE_WORKER_VERBOSE=true` to set the worker agent's output to verbose. For more examples and information, see `/etc/amazon/deadline/worker.toml.example` on Linux or `C:\ProgramData\Amazon\Deadline\Config\worker.toml.example` on Windows.

**Configuration file** — When you install the worker agent, it creates a configuration file located at `/etc/amazon/deadline/worker.toml` on Linux or `C:\ProgramData\Amazon\Deadline\Config\worker.toml` on Windows. The worker agent loads this configuration file when it starts. You can use the example configuration file (`/etc/amazon/deadline/worker.toml.example` on Linux or `C:\ProgramData\Amazon\Deadline\Config\worker.toml.example` on Windows) to tailor the default worker agent configuration file for your specific needs. 

Finally, we recommend you enable auto shutdown for the worker agent *after* your software is deployed and working as expected. This allows the worker fleet to scale up when needed and to shut down when a job finishes. Auto scaling helps ensure you're only using the resources needed. To enable an instance started by the auto scaling group to shut down, you must add `shutdown_on_stop=true` to the `worker.toml` configuration file.

**To enable auto shutdown**

As a **root** user:
+ Install the worker agent with parameters **--allow-shutdown**.

------
#### [ Linux ]

  Enter:

  ```
  /opt/deadline/worker/bin/install-deadline-worker \
    --farm-id {{FARM_ID}} \
    --fleet-id {{FLEET_ID}} \
    --region {{REGION}} \
    --allow-shutdown
  ```

------
#### [ Windows ]

  Enter:

  ```
  install-deadline-worker ^
    --farm-id {{FARM_ID}} ^
    --fleet-id {{FLEET_ID}} ^
    --region {{REGION}} ^
    --allow-shutdown
  ```

------

## Create job users and groups
<a name="create-job-user-and-group"></a>

This section describes the required user and group relationship between the agent user and the `jobRunAsUser` defined on your queues.

The Deadline Cloud worker agent should run as a dedicated agent-specific user on the host. You should configure the `jobRunAsUser` property of Deadline Cloud queues so that workers will run the queue jobs as a specific operating system user and group. This configuration means you can control the shared filesystem permissions that your jobs have. It also provides as an important security boundary between your jobs and the worker agent user.

**Linux job users and groups**

To set up a local worker agent user and `jobRunAsUser`, ensure you meet the following requirements. If you are using a Linux Pluggable Authentication Module (PAM) such as Active Directory or LDAP, your procedure may be different.

The worker agent user and the shared `jobRunAsUser` group are set when you install the worker agent. The defaults are `deadline-worker-agent` and `deadline-job-users`, but you can change those when you install the worker agent.

```
install-deadline-worker \
    --user {{AGENT_USER_NAME}} \
    --group {{JOB_USERS_GROUP}}
```

Commands should be run as the root user. 
+ Each `jobRunAsUser` should have a matching primary group. Creating a user with the `adduser` command usually creates a matching primary group.

  ```
  adduser -r -m {{jobRunAsUser}}
  ```
+ The primary group of the `jobRunAsUser` is a secondary group for the worker agent user. The shared group allows the worker agent to make files available to the job as it is running. 

  ```
  usermod -a -G {{jobRunAsUser}} {{deadline-worker-agent}}
  ```
+ The `jobRunAsUser` must be a member of the shared job group.

  ```
  usermod -a -G {{deadline-job-users}} {{jobRunAsUser}}
  ```
+ The `jobRunAsUser` must not belong to the worker agent user's primary group. Sensitive files written by the worker agent are owned by the agent's primary group. If a `jobRunAsUser` is part of this group, worker agent files may be accessible to jobs running on the worker.
+ The default AWS Region must match the Region of the farm that the worker belongs to. Apply this setting to all `jobRunAsUser` accounts on the worker.

  ```
  sudo -u {{jobRunAsUser}} aws configure set default.region {{aws-region}}
  ```
+ The worker agent user must be able to run `sudo` commands as the `jobRunAsUser`. Run the following command to open an editor to create a new sudoers rule:

  ```
  visudo -f /etc/sudoers.d/deadline-worker-job-user
  ```

  Add the following to the file:

  ```
  # Allows the Deadline Cloud worker agent OS user to run commands
   # as the queue OS user without requiring a password.
  deadline-worker-agent ALL=(jobRunAsUser) NOPASSWD:ALL
  ```

The following diagram illustrates the relationship between the agent user and the `jobRunAsUser` users and groups for queues associated with the fleet.

![An illustration of the relationship between agent-users and the jobRunAsUser on queues.](http://docs.aws.amazon.com/deadline-cloud/latest/developerguide/images/worker_users_and_groups.png)


**Windows users**

To use a Windows user as the `jobRunAsUser`, it must meet the following requirements:
+ All queue `jobRunAsUser` users must exist.
+ Their passwords must match the value of the secret specified in their queue's `JobRunAsUser` field. For instructions, see step 7 in [Deadline Cloud queues](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/queues.html) in the *AWS Deadline Cloud User Guide*.
+  The agent-user must be able to log on as those users.

## Securing your worker host
<a name="securing-worker-host"></a>

When setting up your worker host, follow security best practices to protect sensitive information and maintain proper access controls.

### Configuring log folder permissions
<a name="configuring-log-folder-permissions"></a>

The worker agent writes log files that may contain sensitive information from host configuration scripts and job execution. The `install-deadline-worker` command creates the log directory with secure permissions. If you need to create the directory manually before installation, use the following procedures to match the permissions used by service-managed fleets:

------
#### [ Linux ]

**To configure log directory permissions on Linux**

1. Create the log directory:

   ```
   sudo mkdir -p /var/log/amazon/deadline
   ```

1. Set the owner and group to the worker agent user:

   ```
   sudo chown -R deadline-worker-agent:deadline-worker-agent /var/log/amazon/deadline
   ```

1. Set permissions to 750:

   ```
   sudo chmod -R 750 /var/log/amazon/deadline
   ```

   These permissions ensure that only the worker agent user and group can access the log files, preventing job users and other unauthorized users from reading potentially sensitive information.

------
#### [ Windows ]

**To configure log directory permissions on Windows**

1. Open an administrator PowerShell terminal.

1. Create the log directory:

   ```
   New-Item -ItemType Directory -Force -Path "$env:PROGRAMDATA\Amazon\Deadline\Logs"
   ```

1. Configure restricted ACLs to allow only the worker agent user and Administrators:

   ```
   $acl = Get-Acl "$env:PROGRAMDATA\Amazon\Deadline\Logs"
   $acl.SetAccessRuleProtection($true, $false)
   $acl.Access | ForEach-Object { $acl.RemoveAccessRule($_) }
   $agentRule = New-Object System.Security.AccessControl.FileSystemAccessRule("deadline-worker", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
   $adminRule = New-Object System.Security.AccessControl.FileSystemAccessRule("Administrators", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
   $acl.AddAccessRule($agentRule)
   $acl.AddAccessRule($adminRule)
   Set-Acl "$env:PROGRAMDATA\Amazon\Deadline\Logs" $acl
   ```

   These commands restrict access to the log directory to only the worker agent user and Administrators group, preventing job users and other unauthorized users from reading potentially sensitive information.

------