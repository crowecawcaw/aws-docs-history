# Task definitions for EC2Launch v2 startup tasks

Each task that EC2Launch v2 runs during launch or startup has its own set of properties
and requirements. Task details include settings for how often a task runs – once, or
always, what stage of the agent boot process it runs in, syntax, and YAML document examples.
For more information, review the task details shown in this reference.

###### EC2Launch v2 Tasks

- [activateWindows](#ec2launch-v2-activatewindows "#ec2launch-v2-activatewindows")
- [enableJumboFrames](#ec2launch-v2-enablejumboframes "#ec2launch-v2-enablejumboframes")
- [enableOpenSsh](#ec2launch-v2-enableopenssh "#ec2launch-v2-enableopenssh")
- [executeProgram](#ec2launch-v2-executeprogram "#ec2launch-v2-executeprogram")
- [executeScript](#ec2launch-v2-executescript "#ec2launch-v2-executescript")
- [extendRootPartition](#ec2launch-v2-extendrootpartition "#ec2launch-v2-extendrootpartition")
- [initializeVolume](#ec2launch-v2-initializevolume "#ec2launch-v2-initializevolume")
- [optimizeEna](#ec2launch-v2-optimizeena "#ec2launch-v2-optimizeena")
- [setAdminAccount](#ec2launch-v2-setadminaccount "#ec2launch-v2-setadminaccount")
- [setDnsSuffix](#ec2launch-v2-setdnssuffix "#ec2launch-v2-setdnssuffix")
- [setHostName](#ec2launch-v2-sethostname "#ec2launch-v2-sethostname")
- [setWallpaper](#ec2launch-v2-setwallpaper "#ec2launch-v2-setwallpaper")
- [startSsm](#ec2launch-v2-startssm "#ec2launch-v2-startssm")
- [sysprep](#ec2launch-v2-task-sysprep "#ec2launch-v2-task-sysprep")
- [writeFile](#ec2-launch-v2-writefile "#ec2-launch-v2-writefile")

## activateWindows

Activates Windows against a set of AWS KMS servers. Activation is skipped if the
instance is detected as Bring-Your-Own-License (BYOL).

_Frequency_ — once

_AllowedStages_ — `[PreReady]`

_Inputs_ —

`activation`: (map)

`type`: (string) activation type to use, set to
`amazon`

_Example_

```
task: activateWindows
  inputs:
    activation:
    type: amazon
```

## enableJumboFrames

Enables Jumbo Frames, which increase the maximum transmission unit (MTU) of
the network adapter. For more information, see [Jumbo frames (9001 MTU)](network_mtu.md#jumbo_frame_instances "network_mtu.md#jumbo_frame_instances").

_Frequency_ — always

_AllowedStages_ — `[PostReady, UserData]`

_Inputs_ — none

_Example_

```
task: enableJumboFrames
```

## enableOpenSsh

Enables Windows OpenSSH and adds the public key for the instance to the
authorized keys folder.

_Frequency_ — once

_AllowedStages_ — `[PreReady, UserData]`

_Inputs_ — none

_Example_

The following example shows how to enable OpenSSH on an instance, and to add
the public key for the instance to the authorized keys folder. This
configuration works only on instances running Windows Server 2019 and later
versions.

```
task: enableOpenSsh
```

## executeProgram

Runs a program with optional arguments and a specified frequency.

**Stages:** You can run the `executeProgram`
task during the `PreReady`, `PostReady`, and `UserData` stages.

**Frequency:** configurable, see _Inputs_.

**Inputs**

This section contains one or more programs for the **executeProgram**
task to run (inputs). Each input can include the following configurable settings:

**frequency (string)**

(Required) Specify exactly one of the following values:

- `once`
- `always`

**path (string)**

(Required) The file path for the executable to run.

**arguments (list of strings)**

(Optional) A comma separated list of arguments to provide to
the program as input.

**runAs (string)**

(Required) Must be set to `localSystem`

**Output**

All of the tasks write logfile entries to the `agent.log`
file. Additional output from the `executeProgram` task is stored
separately in a dynamically named folder, as follows:

`%LocalAppData%\Temp\`EC2Launch#########`\`outputfilename.tmp``

The exact path to the output files is included in the `agent.log` file, for example:

```
`Program file is created at: C:\Windows\system32\config\systemprofile\AppData\Local\Temp\EC2Launch123456789\ExecuteProgramInputs.tmp
Output file is created at: C:\Windows\system32\config\systemprofile\AppData\Local\Temp\EC2Launch123456789\Output.tmp
Error file is created at: C:\Windows\system32\config\systemprofile\AppData\Local\Temp\EC2Launch123456789\Err.tmp`
```

###### Output files for the `executeProgram` task

`ExecuteProgramInputs.tmp`

Contains the path for the executable, and all of the
input parameters that the `executeProgram`
task passes to it when it runs.

`Output.tmp`

Contains runtime output from the program that the
`executeProgram` task runs.

`Err.tmp`

Contains runtime error messages from the program that the
`executeProgram` task runs.

**Examples**

The following examples show how to run an executable file from a
local directory on an instance with the `executeProgram` task.

###### Example 1: Setup executable with one argument

This example shows an `executeProgram` task
that runs a setup executable in quiet mode.

```
task: executeProgram
  inputs:
    - frequency: always
      path: C:\Users\Administrator\Desktop\setup.exe
      arguments: ['-quiet']
```

###### Example 2: VLC executable with two arguments

This example shows an `executeProgram` task
that runs a VLC executable file with two arguments passed as
input parameters.

```
task: executeProgram
  inputs:
    - frequency: always
      path: C:\vlc-3.0.11-win64.exe
      arguments: ['/L=1033','/S']
      runAs: localSystem
```

## executeScript

Runs a script with optional arguments and a specified frequency.
Script behavior depends on what mode the agent runs the scripts in – inline,
or detached.

Inline (default)

The EC2Launch v2 agent runs scripts one at a time (`detach: false`).
This is the default setting.

###### Note

When your inline script issues a **reset** or
**sysprep** command, it runs immediately and resets the
agent. The current task finishes, then the agent shuts down without
running any further tasks.

For example, if the task that issues the command would have been followed
by a `startSsm` task (included by default after user data runs), the
task doesn't run and the Systems Manager service never starts.

Detached

The EC2Launch v2 agent runs scripts concurrently with other tasks
(`detach: true`).

###### Note

When your detached script issues a **reset** or
**sysprep** command, those commands wait for the agent
to finish before they run. Tasks after the executeScript will still run.

**Stages:** You can run the `executeScript`
task during the `PreReady`, `PostReady`, and `UserData` stages.

**Frequency:** configurable, see _Inputs_.

**Inputs**

This section contains one or more scripts for the **executeScript**
task to run (inputs). Each input can include the following configurable settings:

**frequency (string)**

(Required) Specify exactly one of the following values:

- `once`
- `always`

**type (string)**

(Required) Specify exactly one of the following values:

- `batch`
- `powershell`

**arguments (list of strings)**

(Optional) A list of string arguments to pass to the shell (not to the
PowerShell script). This parameter isn't supported for
`type: batch`. If no arguments are passed, EC2Launch v2 adds the
following argument by default: `-ExecutionPolicy Unrestricted`.

**content (string)**

(Required) Script content.

**runAs (string)**

(Required) Specify exactly one of the following values:

- `admin`
- `localSystem`

**detach (Boolean)**

(Optional) The EC2Launch v2 agent defaults to run scripts one at
a time (`detach: false`). To run the script concurrently
with other tasks, set the value to `true`
(`detach: true`).

###### Note

Script exit codes (including `3010`) have no effect
when `detach` is set to `true`.

**Output**

All of the tasks write logfile entries to the `agent.log`
file. Additional output from script that the `executeScript` task runs
is stored separately in a dynamically named folder, as follows:

`%LocalAppData%\Temp\`EC2Launch#########`\`outputfilename.ext``

The exact path to the output files is included in the `agent.log` file, for example:

```
`Program file is created at: C:\Windows\system32\config\systemprofile\AppData\Local\Temp\EC2Launch123456789\UserScript.ps1
Output file is created at: C:\Windows\system32\config\systemprofile\AppData\Local\Temp\EC2Launch123456789\Output.tmp
Error file is created at: C:\Windows\system32\config\systemprofile\AppData\Local\Temp\EC2Launch123456789\Err.tmp`
```

###### Output files for the `executeScript` task

`UserScript.`ext``

Contains the script that the `executeScript` task ran. The file
extension depends on the type of script you
specified in the `type` parameter for the
`executeScript` task, as
follows:

- If the type is `batch`, then the file extension
  is `.bat`.
- If the type is `powershell`, then the file extension
  is `.ps1`.

`Output.tmp`

Contains runtime output from the script that the
`executeScript` task runs.

`Err.tmp`

Contains runtime error messages from the script that the
`executeScript` task runs.

**Examples**

The following examples show how to run an inline script with
the `executeScript` task.

###### Example 1: Hello world output text file

This example shows an `executeScript` task
that runs a PowerShell script to create a "Hello world"
text file on the `C:` drive.

```
task: executeScript
  inputs:
    - frequency: always
      type: powershell
      runAs: admin
      content: |-
        New-Item -Path 'C:\PowerShellTest.txt' -ItemType File
        Set-Content 'C:\PowerShellTest.txt' "Hello world"
```

###### Example 2: Run two scripts

This example shows that the `executeScript` task
can run more than one script, and the script type doesn't
necessarily need to match.

The first script (`type: powershell`)
writes a summary of the processes that are currently running on
the instance to a text file located on the `C:` drive.

The second script (`batch`) writes the system
information to the `Output.tmp` file.

```
task: executeScript
  inputs:
    - frequency: always
      type: powershell
      runAs: localSystem
      content: |
        Get-Process | Out-File -FilePath C:\Process.txt
    - frequency: always
      type: batch
      runAs: localSystem
      content: |
        systeminfo
```

###### Example 3: Idempotent system configuration with reboots

This example shows an `executeScript` task that runs an
idempotent script to perform the following system configuration with
a reboot between each step:

- Rename the computer.
- Join the computer to the domain.
- Enable Telnet.

The script ensures that each operation runs one time only.
This prevents a reboot loop and makes the script idempotent.

```
task: executeScript
  inputs:
    - frequency: always
      type: powershell
      runAs: localSystem
      content: |-
        $name = $env:ComputerName
        if ($name -ne $desiredName) {
          Rename-Computer -NewName $desiredName
          exit 3010
        }
        $domain = Get-ADDomain
        if ($domain -ne $desiredDomain)
        {
          Add-Computer -DomainName $desiredDomain
          exit 3010
        }
        $telnet = Get-WindowsFeature -Name Telnet-Client
        if (-not $telnet.Installed)
        {
          Install-WindowsFeature -Name "Telnet-Client"
          exit 3010
        }
```

## extendRootPartition

Extends the root volume to use all of the available space on the disk.

_Frequency_ — once

_AllowedStages_ — `[Boot]`

_Inputs_ — none

_Example_

```
task: extendRootPartition
```

## initializeVolume

Initializes empty volumes that are attached to the instance so that they're
activated and partitioned. The launch agent skips initialization if it detects
that the volume is not empty. A volume is considered empty if the first
4 KiB of the volume are empty, or if the volume doesn't have a [Windows-recognizable drive layout](https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-drive_layout_information_ex "https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-drive_layout_information_ex").

The `letter` input parameter is always applied when this task runs,
regardless of whether the drive is already initialized.

The `initializeVolume` task performs the following actions.

- Set disk attributes `offline` and `readonly` to false.
- Create a partition. If no partition type is specified in the `partition`
  input parameter, the following defaults apply:
  - If the disk size is smaller than 2 TB, set the partition type to `mbr`.
  - If the disk size is 2 TB or larger, set the partition type to `gpt`.

- Format the volume as NTFS.
- Set the volume label as follows:
  - Use the value of the `name` input parameter, if specified.
  - If the volume is ephemeral, and no name was specified, set the volume label to
    `Temporary Storage Z`.

- If the volume is ephemeral (SSD or HDD – not Amazon EBS), create an
  `Important.txt` file at the root of the volume with the
  following content:

```
`This is an 'Instance Store' disk and is provided at no additional charge.

*This disk offers increased performance since it is local to the host
*The number of Instance Store disks available to an instance vary by instance type
*DATA ON THIS DRIVE WILL BE LOST IN CASES OF IMPAIRMENT OR STOPPING THE INSTANCE. PLEASE ENSURE THAT ANY IMPORTANT DATA IS BACKED UP FREQUENTLY

For more information, please refer to: Instance store temporary block storage for EC2 instances.`
```

- Set the drive letter to the value specified in the `letter`
  input parameter.

**Stages:** You can run the `initializeVolume`
task during the `PostReady` and `UserData` stages.

**Frequency:** always.

**Inputs**

You can configure runtime parameters as follows:

**devices (list of maps)**

(Conditional) Configuration for each device that the launch agent initializes.
This is required if the `initialize` input parameter is set to
`devices`.

- **device (string, required)** –
  Identifies the device during instance creation. For example,
  `xvdb`, `xvdf`, or `\dev\nvme0n1`.
- **letter (string, optional)** –
  One character. The drive letter to assign.
- **name (string, optional)** –
  The volume name to assign.
- **partition (string, optional)** –
  Specify one of the following values for the type of partition
  to create, or let the launch agent default based on volume size:
  - mbr
  - gpt

**initialize (string)**

(Required) Specify exactly one of the following values:

- `all`
- `devices`

**Examples**

The following examples show sample input configurations for the
`initializeVolume` task.

###### Example 1: Initialize two volumes on an instance

This example shows an `initializeVolume` task
that initializes two secondary volumes on an instance. The
device named `DataVolume2` in the example is ephemeral.

```
task: initializeVolume
inputs:
  initialize: devices
  devices:
  - device: xvdb
    name: DataVolume1
    letter: D
    partition: mbr
  - device: /dev/nvme0n1
    name: DataVolume2
    letter: E
    partition: gpt
```

###### Example 2: Initialize EBS volumes attached to an instance

This example shows an `initializeVolume` task
that initializes all empty EBS volumes that are attached to
the instance.

```
task: initializeVolume
inputs:
  initialize: all
```

## optimizeEna

Optimizes ENA settings based on the current instance type; might reboot the
instance.

_Frequency_ — always

_AllowedStages_ — `[PostReady, UserData]`

_Inputs_ — none

_Example_

```
task: optimizeEna
```

## setAdminAccount

Sets attributes for the default administrator account that is created on the
local machine.

_Frequency_ — once

_AllowedStages_ — `[PreReady]`

_Inputs_ —

`name`: (string) name of the administrator account

`password`: (map)

`type`: (string) strategy to set the password, either as
`static`, `random`, or `doNothing`

`data`: (string) stores data if the `type` field is
static

_Example_

```
task: setAdminAccount
inputs:
  name: Administrator
  password:
  type: random
```

## setDnsSuffix

Adds DNS suffixes to the list of search suffixes. Only suffixes that do not
already exist are added to the list. For more information about how launch
agents set DNS suffixes, see [Configure DNS Suffix for EC2 Windows launch agents](launch-agents-set-dns.md "launch-agents-set-dns.md").

_Frequency_ — always

_AllowedStages_ — `[PreReady]`

_Inputs_ —

`suffixes`: (list of strings) list of one or more valid DNS
suffixes; valid substitution variables are `$REGION` and
`$AZ`

_Example_

```
task: setDnsSuffix
inputs:
  suffixes:
  - $REGION.ec2-utilities.amazonaws.com
```

## setHostName

Sets the hostname of the computer to a custom string or, if
`hostName` is not specified, the private IPv4 address.

_Frequency_ — always

_AllowedStages_ — `[PostReady, UserData]`

_Inputs_ —

`hostName`: (string) optional host name, which must be formatted as
follows.

- Must be 15 characters or less
- Must contain only alphanumeric (a-z, A-Z, 0-9) and hyphen (-)
  characters.
- Must not consist entirely of numerical characters.

`reboot`: (boolean) denotes whether a reboot is permitted when the
hostname is changed

_Example_

```
task: setHostName
inputs:
  reboot: true
```

## setWallpaper

Creates the `setwallpaper.lnk` shortcut file in the startup folder
of each existing user except for `Default User`. This shortcut file
runs when the user logs in for the first time after instance boot. It sets up
the instance with a custom wallpaper that displays the instance attributes.

The shortcut file path is:

```
$env:SystemDrive/Users/<user>/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/setwallpaper.lnk
```

###### Note

When you remove the `setWallpaper` task, it does not delete this
shortcut file. For more information, see [setWallpaper task is not enabled but the wallpaper resets
at reboot](ec2launchv2-troubleshooting.md#ec2launchv2-troubleshooting-wallpaper-resets "ec2launchv2-troubleshooting.md#ec2launchv2-troubleshooting-wallpaper-resets").

**Stages:** You can configure wallpaper during the
`PreReady` and `UserData` stages.

**Frequency:** `always`

###### Wallpaper configuration

You can use the following settings to configure your wallpaper.

**Inputs**

Input parameters that you provide, and attributes that you can set
to configure your wallpaper:

**attributes (list of strings)**

(Optional) You can add one or more of the following attributes to your wallpaper:

- `architecture`
- `availabilityZone`
- `hostName`
- `instanceId`
- `instanceSize`
- `memory`
- `network`
- `privateIpAddress`
- `publicIpAddress`

**instanceTags**

(Optional) You can use exactly one of the following options for this setting.

- AllTags (string) – Add
  all instance tags to your wallpaper.

```
instanceTags: AllTags
```

- instanceTags (list of strings)
  – Specify a list of instance tag names to add to your
  wallpaper. For example:

```
instanceTags:
  - Tag 1
  - Tag 2
```

**path (string)**

(Required) The filename path of the local .jpg format image file to use for
your wallpaper image.

###### Example

The following example shows wallpaper configuration inputs that set the
file path for the wallpaper background image, along with instance tags named
`Tag 1` and `Tag 2`, and attributes that
include the host name, instance ID, and private and public IP addresses for
the instance.

```
task: setWallpaper
inputs:
  path: C:\ProgramData\Amazon\EC2Launch\wallpaper\Ec2Wallpaper.jpg
  attributes:
  - hostName
  - instanceId
  - privateIpAddress
  - publicIpAddress
instanceTags:
  - Tag 1
  - Tag 2
```

###### Note

You must enable tags in metadata to show tags on the wallpaper. For more
information about instance tags and metadata, see
[View tags for your EC2 instances using instance metadata](work-with-tags-in-IMDS.md "work-with-tags-in-IMDS.md").

## startSsm

Starts the Systems Manager (SSM) service following Sysprep.

_Frequency_ — always

_AllowedStages_ — `[PostReady, UserData]`

_Inputs_ — none

_Example_

```
task: startSsm
```

## sysprep

Resets the service state, updates `unattend.xml`, disables RDP, and
runs Sysprep. This task runs only after all other tasks are completed.

_Frequency_ — once

_AllowedStages_ — `[UserData]`

_Inputs_ —

`clean`: (boolean) cleans instance logs before running
Sysprep

`shutdown`: (boolean) shuts down the instance after running
Sysprep

_Example_

```
task: sysprep
inputs:
clean: true
shutdown: true
```

## writeFile

Writes a file to a destination.

_Frequency_ — see _Inputs_

_AllowedStages_ — `[PostReady, UserData]`

_Inputs_ —

`frequency`: (string) one of `once` or
`always`

`destination`: (string) path to which to write the content

`content`: (string) text to write to the destination

_Example_

```
task: writeFile
inputs:
  - frequency: once
  destination: C:\Users\Administrator\Desktop\booted.txt
  content: Windows Has Booted
```
