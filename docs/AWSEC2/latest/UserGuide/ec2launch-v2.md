# Use the EC2Launch v2 agent to perform tasks during EC2 Windows

instance launch

All supported instances of Amazon EC2 that are launched from AWS Windows Server 2022 and
Windows Server 2025 AMIs include the EC2Launch v2 launch agent (`EC2Launch.exe`) by
default. We also provide Windows Server 2016 and 2019 AMIs with EC2Launch v2 installed as the
default launch agent. These AMIs are provided in addition to the Windows Server 2016 and
2019 AMIs that include EC2Launch v1. You can search for Windows AMIs that include EC2Launch v2 by
default by entering the following prefix in your search from the **AMIs**
page in the Amazon EC2 console: `EC2LaunchV2-Windows_Server-*`.

To compare launch agent version features, see [Compare Amazon EC2 launch agents](configure-launch-agents.md#ec2launch-agent-compare "configure-launch-agents.md#ec2launch-agent-compare").

EC2Launch v2 performs tasks during instance startup and runs if an instance is stopped and
later started, or restarted. EC2Launch v2 can also perform tasks on demand. Some of these tasks
are automatically enabled, while others must be enabled manually. The EC2Launch v2 service
supports all EC2Config and EC2Launch features.

This service uses a configuration file to control its operation. You can update the
configuration file using either a graphical tool or by directly editing it as a single .yml
file (`agent-config.yml`). For more information about file locations, see [EC2Launch v2 directory structure](#ec2launch-v2-directory "#ec2launch-v2-directory").

EC2Launch v2 publishes Windows event logs to help you troubleshoot errors and set triggers.
For more information, see [Windows event logs](ec2launchv2-troubleshooting.md#ec2launchv2-windows-event-logs "ec2launchv2-troubleshooting.md#ec2launchv2-windows-event-logs").

###### Supported OS versions

The EC2Launch v2 agent supports the following Windows Server operating system (OS)
versions:

- Windows Server 2025
- Windows Server 2022
- Windows Server 2019 (Long-Term Servicing Channel and Semi-Annual Channel)
- Windows Server 2016

###### Tasks that run by default

The EC2Launch v2 agent runs the following tasks one time only by default during the
initial instance launch. Tasks are organized according to the order in which they run
within their launch stage.

`Boot` stage

- extendRootPartition
  `PreReady` stage

- activateWindows
- setDnsSuffix
- setAdminAccount
- setWallpaper
  `PostReady` stage

- startSsm

## EC2Launch v2 concepts

The following concepts are useful to understand when considering EC2Launch v2.

**agent-config**

`agent-config` is a file that is located in the configuration
folder for EC2Launch v2. It includes configuration for the boot, network,
PreReady, and PostReady stages. This file is used to specify the instance
configuration for tasks that should run when the AMI is either booted for
the first time or for subsequent times.

By default, the EC2Launch v2 installation installs an
`agent-config` file that includes recommended configurations
that are used in standard Amazon Windows AMIs. You can update the
configuration file to alter the default boot experience for your AMI that
EC2Launch v2 specifies. For more information about file locations, see [EC2Launch v2 directory structure](#ec2launch-v2-directory "#ec2launch-v2-directory").

**Frequency**

Task frequency determines when tasks should run, depending on the boot
context. Most tasks have only one allowed frequency. You can specify a
frequency for `executeScript` tasks.

You will see the following frequencies in the [EC2Launch v2 task
configuration](ec2launch-v2-settings.md#ec2launch-v2-task-configuration "ec2launch-v2-settings.md#ec2launch-v2-task-configuration").

- Once – The task runs once, when the AMI has booted for the
  first time (finished Sysprep).
- Always – The task runs every time that the launch agent
  runs. The launch agent runs when:
  - an instance starts or restarts
  - the EC2Launch service runs
  - `EC2Launch.exe run` is invoked

**Stage**

A stage is a logical grouping of tasks that the EC2Launch v2 agent runs. Some
tasks can run only in a specific stage. Others can run in multiple stages.
When using `agent-config.yml`, you must specify a list of stages,
and a list of tasks to run within each stage.

The service runs stages in the following order:

Stage 1: Boot

Stage 2: Network

Stage 3: PreReady

Windows is ready

After the PreReady stage completes, the service sends the
`Windows is ready` message to the Amazon EC2
console.

Stage 4: PostReady

User data runs during the _PostReady_
stage. Some script versions run before the
`agent-config.yml` file
_PostReady_ stage, and some run after, as
follows:

Before
`agent-config.yml`

- YAML user data version 1.1
- XML user data

After
`agent-config.yml`

- YAML user data version 1.0 (legacy version
  for backwards compatibility)

For example stages and tasks, see [Example:
agent-config.yml](ec2launch-v2-settings.md#ec2launch-v2-example-agent-config "ec2launch-v2-settings.md#ec2launch-v2-example-agent-config").

When you use user data, you must specify a list of tasks for the launch
agent to run. The stage is implied. For example tasks, see [Example: user data](ec2launch-v2-settings.md#ec2launch-v2-example-user-data "ec2launch-v2-settings.md#ec2launch-v2-example-user-data").

EC2Launch v2 runs the list of tasks in the order that you specify in
`agent-config.yml` and in user data. Stages run sequentially.
The next stage starts after the previous stage completes. Tasks also run
sequentially.

**Task**

You can invoke a task to perform an action on an instance. You can
configure tasks in the `agent-config.yml` file or through
user data. For a list of available tasks for EC2Launch v2, see [EC2Launch v2 tasks](#ec2launch-v2-tasks "#ec2launch-v2-tasks"). For task
configuration schema and details, see [EC2Launch v2 task
configuration](ec2launch-v2-settings.md#ec2launch-v2-task-configuration "ec2launch-v2-settings.md#ec2launch-v2-task-configuration").

**User data**

User data is data that is configurable when you launch an instance. You
can update user data to dynamically change how custom AMIs or quickstart
AMIs are configured. EC2Launch v2 supports 60 kB user data input length. User
data includes only the UserData stage, and therefore runs after the
`agent-config` file. You can enter user data when you launch
an instance using the launch instance wizard, or you can modify user data
from the EC2 console. For more information about working with user data, see
[How Amazon EC2 handles user data for Windows instances](user-data.md#ec2-windows-user-data "user-data.md#ec2-windows-user-data").

## EC2Launch v2 task overview

EC2Launch v2 can perform the following tasks at each boot:

- Set up new and optionally customized wallpaper that renders information about
  the instance.
- Set the attributes for the administrator account that is created on the local
  machine.
- Add DNS suffixes to the list of search suffixes. Only suffixes that do not
  already exist are added to the list.
- Set drive letters for any additional volumes and extend them to use available
  space.
- Write files from the configuration to the disk.
- Run scripts specified in the EC2Launch v2 config file or from
  `user-data`. Scripts from `user-data` can be plain
  text or zipped and provided as a base64 format.
- Run a program with given arguments.
- Set the computer name.
- Send instance information to the Amazon EC2 console.
- Send the RDP certificate thumbprint to the Amazon EC2 console.
- Dynamically extend the operating system partition to include any unpartitioned
  space.
- Run user data. For more information about specifying user data, see [EC2Launch v2 task
  configuration](ec2launch-v2-settings.md#ec2launch-v2-task-configuration "ec2launch-v2-settings.md#ec2launch-v2-task-configuration").
- Set non-persistent static routes to reach the metadata service and AWS KMS
  servers.
- Set non-boot partitions to `mbr` or `gpt`.
- Start the Systems Manager service following Sysprep.
- Optimize ENA settings.
- Enable OpenSSH for later Windows versions.
- Enable Jumbo Frames.
- Set Sysprep to run with EC2Launch v2.
- Publish Windows event logs.

## EC2Launch v2 directory structure

EC2Launch v2 should be installed in the following directories:

- Service binaries: `%ProgramFiles%\Amazon\EC2Launch`
- Service data (settings, log files, and state files):
  `%ProgramData%\Amazon\EC2Launch`

###### Note

By default, Windows hides files and folders under `C:\ProgramData`. To
view EC2Launch v2 directories and files, you must either enter the path in Windows
Explorer or change the folder properties to show hidden files and folders.

The `%ProgramFiles%\Amazon\EC2Launch` directory contains binaries and
supporting libraries. It includes the following subdirectories:

- `settings`
  - `EC2LaunchSettingsUI.exe` – user interface for modifying
    the `agent-config.yml` file
  - `YamlDotNet.dll` – DLL for supporting some operations in
    the user interface

- `tools`
  - `ebsnvme-id.exe` – tool for examining the metadata of the
    EBS volumes on the instance
  - `AWSAcpiSpcrReader.exe` – tool for determining the correct
    COM port to use
  - `EC2LaunchEventMessage.dll` – DLL for supporting the
    Windows event logging for EC2Launch

- `service`
  - `EC2LaunchService.exe` – Windows service executable
    that is launched when the launch agent runs as a service

- `EC2AgentTelemetry.dll` – DLL for supporting EC2 agent telemetry
- `EC2Launch.exe` – main EC2Launch executable
- `EC2LaunchAgentAttribution.txt` – attribution for code used within
  EC2 Launch

The `%ProgramData%\Amazon\EC2Launch` directory contains the following
subdirectories. All of the data produced by the service, including logs, configuration,
and state, is stored in this directory.

- `config` – Configuration

The service configuration file is stored in this directory as
`agent-config.yml`. This file can be updated to modify, add, or
remove default tasks run by the service. Permission to create files in this
directory is restricted to the administrator account to prevent privilege
escalation.

- `log` – Instance logs

Logs for the service (`agent.log`), console
(`console.log`), performance (`bench.log`), errors
(`err.log`), and telemetry (`telemetry.log` are stored
in this directory. Log files are appended to on subsequent executions of the
service.

- `state` – Service state data

The state that the service uses to determine which tasks should run is stored
here. There is a `.run-once` file that indicates whether the service
has already run after Sysprep (so tasks with a frequency of once will be skipped
on the next run). This subdirectory includes a `state.json` and
`previous-state.json` to track the status of each task.

- `sysprep` – Sysprep

This directory contains files that are used to determine which operations to
perform by Sysprep when it creates a customized Windows AMI that can be
reused.

- `wallpaper` – Wallpaper

This wallpaper images is stored in this directory.

## Telemetry

Telemetry is additional information that helps AWS to better understand your
requirements, diagnose issues, and deliver features to improve your experience with
AWS services.

EC2Launch v2 version `2.1.592` and later collect telemetry, such as usage
metrics and errors. This data is collected from the Amazon EC2 instance on which EC2Launch v2
runs. This includes all Windows AMIs owned by AWS.

The following types of telemetry are collected by EC2Launch v2:

- **Usage information** — agent commands,
  install method, and scheduled run frequency.
- **Errors and diagnostic information** —
  agent installation error codes, run error codes, and error call stacks.

Examples of collected data from version 2.0.592 through 2.1.1:

```
`2025/07/18 22:38:52Z: EC2LaunchTelemetry: IsTelemetryEnabled=true
2025/07/18 22:38:52Z: EC2LaunchTelemetry: AgentOsArch=windows_amd64
2025/07/18 22:38:52Z: EC2LaunchTelemetry: IsAgentScheduledPerBoot=true
2025/07/18 22:38:52Z: EC2LaunchTelemetry: AgentCommandErrorCode=0
2025/07/18 22:38:52Z: EC2LaunchTelemetry: AdminPasswordTypeCode=0
2025/07/18 22:38:52Z: EC2LaunchTelemetry: IpConflictDetectionCode=0
2025/07/18 22:38:52Z: EC2LaunchTelemetry: AgentErrorLocation=addroutes.go:49`
```

Starting with version 2.2.63, EC2 Agent telemetry data is formatted as a JSON object:

```
`{"type":"EC2AgentTelemetry","agentId":"WindowsLaunchAgentV2" ... }`
```

Telemetry is enabled by default. You can disable telemetry collection at any time.

###### Disable telemetry on an instance

To disable telemetry for a single instance, you can either set a system
environment variable, or use the MSI to modify the installation.

To disable telemetry by setting a system environment variable, run the following
command as an administrator.

```
setx /M EC2LAUNCH_TELEMETRY 0
```

To disable telemetry using the MSI, run the following command after you [download the MSI](ec2launch-v2-install.md "ec2launch-v2-install.md").

```
msiexec /i ".\AmazonEC2Launch.msi" Remove="Telemetry" /q
```

###### More topics for EC2Launch v2

- [Install the latest version of
  EC2Launch v2](ec2launch-v2-install.md "ec2launch-v2-install.md")
- [Configure EC2Launch v2 settings for Windows
  instances](ec2launch-v2-settings.md "ec2launch-v2-settings.md")
- [Task definitions for EC2Launch v2 startup tasks](ec2launch-v2-task-definitions.md "ec2launch-v2-task-definitions.md")
- [Troubleshoot issues with the EC2Launch v2 agent](ec2launchv2-troubleshooting.md "ec2launchv2-troubleshooting.md")
- [EC2Launch v2 version histories](ec2launchv2-versions.md "ec2launchv2-versions.md")
