# Create an AMI using Windows Sysprep with EC2Launch v2

When you create an image from an instance with the EC2Launch v2 agent installed, EC2Launch v2
performs specific tasks as the image is prepared. This includes working with Windows Sysprep.
For more information, see [Windows Sysprep phases](ami-create-win-sysprep.md#sysprep-phases "ami-create-win-sysprep.md#sysprep-phases").

###### Contents

- [Windows Sysprep actions](#sysprep-actions-ec2launchv2 "#sysprep-actions-ec2launchv2")
- [Post Sysprep](#sysprep-post-ec2launchv2 "#sysprep-post-ec2launchv2")
- [Run Windows Sysprep with
  EC2Launch v2](#sysprep-gui-procedure-ec2launchv2 "#sysprep-gui-procedure-ec2launchv2")

## Windows Sysprep actions

Windows Sysprep and EC2Launch v2 perform the following actions when preparing an
image.

1. When you choose **Shutdown with Sysprep** in
   the **EC2Launch settings** dialog box, the
   system runs the `ec2launch sysprep` command.
2. EC2Launch v2 edits the content of the `unattend.xml`
   file by reading the registry value at `HKEY_USERS\.DEFAULT\Control
Panel\International\LocaleName`. This file is located in the
   following directory:
   `C:\ProgramData\Amazon\EC2Launch\sysprep`.
3. The system run the `BeforeSysprep.cmd`. This
   command creates a registry key as follows:

**reg add
"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v
fDenyTSConnections /t REG_DWORD /d 1 /f**

The registry key disables RDP connections until they are re-enabled.
Disabling RDP connections is a necessary security measure because, during
the first boot session after Windows Sysprep has run, there is a short period of
time where RDP allows connections and the Administrator password is
blank. 4. The EC2Launch v2 service calls Windows Sysprep by running the following
command:

**sysprep.exe /oobe /generalize /shutdown /unattend:
"C:\ProgramData\Amazon\EC2Launch\sysprep\unattend.xml"**

### Generalize phase

- EC2Launch v2 removes image-specific information and configurations,
  such as the computer name and the SID. If the instance is a member of a
  domain, it is removed from the domain. The
  `unattend.xml` answer file includes the following
  settings that affect this phase:
  - **PersistAllDeviceInstalls**:
    This setting prevents Windows Setup from removing and
    reconfiguring devices, which speeds up the image preparation
    process because Amazon AMIs require certain drivers to run and
    re-detection of those drivers would take time.
  - **DoNotCleanUpNonPresentDevices**: This setting retains
    Plug and Play information for devices that are not currently
    present.

- Windows Sysprep shuts down the OS as it prepares to create the AMI. The system
  either launches a new instance or starts the original instance.

### Specialize phase

The system generates OS-specific requirements, such as a computer name and an
SID. The system also performs the following actions based on configurations that
you specify in the `unattend.xml` answer file.

- **CopyProfile**: Windows Sysprep can be
  configured to delete all user profiles, including the built-in
  Administrator profile. This setting retains the built-in Administrator
  account so that any customizations you make to that account are carried
  over to the new image. The default value is `True`.

**CopyProfile** replaces the default
profile with the existing local administrator profile. All accounts that
you log in to after running Windows Sysprep receive a copy of that profile and
its contents at first login.

If you don’t have specific user-profile customizations that you want
to carry over to the new image, then change this setting to
`False`. Windows Sysprep will remove all user profiles (this
saves time and disk space).

- **TimeZone**: The time zone is set to
  Coordinate Universal Time (UTC) by default.
- **Synchronous command with order 1**: The
  system runs the following command, which enables the administrator
  account and specifies the password requirement:

```
`net user Administrator /ACTIVE:YES /LOGONPASSWORDCHG:NO /EXPIRES:NEVER /PASSWORDREQ:YES`
```

- **Synchronous command with order 2**: The
  system scrambles the administrator password. This security measure is
  designed to prevent the instance from being accessible after Windows Sysprep
  completes if you did not configure the `setAdminAccount` task.

The system runs the following command from your local launch agent directory
(`C:\Program Files\Amazon\EC2Launch\`).

```
`EC2Launch.exe internal randomize-password --username Administrator`
```

- To enable remote desktop connections, the system sets the Terminal Server
  `fDenyTSConnections` registry key to false.

### OOBE phase

1. The system specifies the following configurations using the
   EC2Launch v2 answer file:
   - `<InputLocale>en-US</InputLocale>`
   - `<SystemLocale>en-US</SystemLocale>`
   - `<UILanguage>en-US</UILanguage>`
   - `<UserLocale>en-US</UserLocale>`
   - `<HideEULAPage>true</HideEULAPage>`
   - `<HideWirelessSetupInOOBE>true</HideWirelessSetupInOOBE>`
   - `<ProtectYourPC>3</ProtectYourPC>`
   - `<BluetoothTaskbarIconEnabled>false</BluetoothTaskbarIconEnabled>`
   - `<TimeZone>UTC</TimeZone>`
   - `<RegisteredOrganization>Amazon.com</RegisteredOrganization>`
   - `<RegisteredOwner>EC2</RegisteredOwner>`

###### Note

During the generalize and specialize phases, EC2Launch v2 monitors
the status of the OS. If EC2Launch v2 detects that the OS is in a
Sysprep phase, then it publishes the following message to the system
log:

**`Windows is being configured.
 SysprepState=IMAGE_STATE_UNDEPLOYABLE`** 2. The system runs EC2Launch v2.

## Post Sysprep

After Windows Sysprep completes, EC2Launch v2 sends the following message to the console
output:

```
Windows sysprep configuration complete.
```

EC2Launch v2 then performs the following actions:

1. Reads the content of the `agent-config.yml` file and
   runs configured tasks.
2. Executes all tasks in the `preReady` stage.
3. After it is finished, sends a `Windows is ready` message to the
   instance system logs.
4. Executes all tasks in the `PostReady` stage.

For more information about EC2Launch v2 , see [Use the EC2Launch v2 agent to perform tasks during EC2 Windows
instance launch](ec2launch-v2.md "ec2launch-v2.md").

## Run Windows Sysprep with

EC2Launch v2

Use the following procedure to create a standardized AMI using Windows Sysprep with
EC2Launch v2.

1. In the Amazon EC2 console, locate an AMI that you want to duplicate.
2. Launch and connect to your Windows instance.
3. Customize settings
   1. From the Windows **Start** menu, search for and choose
      **Amazon EC2Launch settings**. For more information
      about the options and settings in the Amazon **EC2Launch
      settings** dialog box, see [Configure EC2Launch v2 settings for Windows
      instances](ec2launch-v2-settings.md "ec2launch-v2-settings.md").
   2. If you've made changes, choose **Save** before you
      shut down.

4. Choose **Shutdown with Sysprep** or **Shutdown without
   Sysprep**.

When you are asked to confirm that you want to run Windows Sysprep and shut down the
instance, click **Yes**. EC2Launch v2 runs Windows Sysprep. Next, you are
logged off the instance, and the instance shuts down. If you check the
**Instances** page in the Amazon EC2 console, the instance state
changes from `Running` to `Stopping` to `Stopped`.
At this point, it's safe to create an AMI from this instance.

You can manually invoke the Windows Sysprep tool from the command line using the following
command:

```
"%programfiles%\amazon\ec2launch\ec2launch.exe" sysprep --shutdown=true
```
