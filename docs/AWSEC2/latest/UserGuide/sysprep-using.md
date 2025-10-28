# Create an AMI using Windows Sysprep with EC2Config

When you create an image from an instance with the EC2Config service installed, EC2Config
performs specific tasks as the image is prepared. This includes working with Windows Sysprep.
For more information, see [Windows Sysprep phases](ami-create-win-sysprep.md#sysprep-phases "ami-create-win-sysprep.md#sysprep-phases").

###### Contents

- [Windows Sysprep actions](#sysprep-actions "#sysprep-actions")
- [Post Sysprep](#sysprep-post "#sysprep-post")
- [Run Windows Sysprep with the EC2Config
  service](#sysprep-gui-procedure "#sysprep-gui-procedure")

## Windows Sysprep actions

Windows Sysprep and the EC2Config service perform the following actions when preparing an
image.

1. When you choose **Shutdown with Sysprep** in
   the **EC2 Service Properties** dialog box, the
   system runs the **ec2config.exe -sysprep**
   command.
2. The EC2Config service reads the content of the
   `BundleConfig.xml` file. This file is located in the
   following directory, by default: `C:\Program
Files\Amazon\Ec2ConfigService\Settings`.

The `BundleConfig.xml` file includes the following
settings. You can change these settings:

    * **AutoSysprep**: Indicates whether to
     use Windows Sysprep automatically. You do not need to change this value if
     you are running Windows Sysprep from the EC2 Service Properties dialog box.
     The default value is `No`.
    * **SetRDPCertificate**: Sets a
     self-signed certificate for the Remote Desktop server. This enables
     you to securely use the Remote Desktop Protocol (RDP) to connect to
     the instance. Change the value to `Yes` if new instances
     should use a certificate. This setting is not used with Windows
     Server 2012 instances because these operating
     systems can generate their own certificates. The default value is
     `No`.
    * **SetPasswordAfterSysprep**: Sets a
     random password on a newly launched instance, encrypts it with the
     user launch key, and outputs the encrypted password to the console.
     Change the value to `No` if new instances should not be
     set to a random encrypted password. The default value is
     `Yes`.
    * **PreSysprepRunCmd**: The location of
     the command to run. The command is located in the following
     directory, by default: `C:\Program
     Files\Amazon\Ec2ConfigService\Scripts\BeforeSysprep.cmd`

3. The system runs `BeforeSysprep.cmd`. This command
   creates a registry key as follows:

```
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 1 /f
```

The registry key disables RDP connections until they are re-enabled.
Disabling RDP connections is a necessary security measure because, during
the first boot session after Windows Sysprep has run, there is a short period of
time where RDP allows connections and the Administrator password is
blank. 4. The EC2Config service calls Windows Sysprep by running the following
command:

```
sysprep.exe /unattend: "C:\Program Files\Amazon\Ec2ConfigService\sysprep2008.xml" /oobe /generalize /shutdown
```

### Generalize phase

- The tool removes image-specific information and configurations such as
  the computer name and the SID. If the instance is a member of a domain,
  it is removed from the domain. The `sysprep2008.xml`
  answer file includes the following settings that affect this phase:
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

The system generates OS specific requirements such as a computer name and a
SID. The system also performs the following actions based on configurations that
you specify in the sysprep2008.xml answer file.

- **CopyProfile**: Windows Sysprep can be
  configured to delete all user profiles, including the built-in
  Administrator profile. This setting retains the built-in Administrator
  account so that any customizations you made to that account are carried
  over to the new image. The default value is True.

**CopyProfile** replaces the default
profile with the existing local administrator profile. All accounts
logged into after running Windows Sysprep will receive a copy of that profile
and its contents at first login.

If you don’t have specific user-profile customizations that you want
to carry over to the new image then change this setting to False.
Windows Sysprep will remove all user profiles; this saves time and disk space.

- **TimeZone**: The time zone is set to
  Coordinate Universal Time (UTC) by default.
- **Synchronous command with order 1**: The
  system runs the following command that enables the administrator
  account and specifies the password requirement.

**net user Administrator /ACTIVE:YES /LOGONPASSWORDCHG:NO
/EXPIRES:NEVER /PASSWORDREQ:YES**

- **Synchronous command with order 2**: The
  system scrambles the administrator password. This security measure is
  designed to prevent the instance from being accessible after Windows Sysprep
  completes if you did not enable the ec2setpassword setting.

C:\Program Files\Amazon\Ec2ConfigService\ScramblePassword.exe" -u
Administrator

- **Synchronous command with order 3**: The
  system runs the following command:

C:\Program
Files\Amazon\Ec2ConfigService\Scripts\SysprepSpecializePhase.cmd

This command adds the following registry key, which re-enables
RDP:

reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal
Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f

### OOBE phase

1. Using the EC2Config service answer file, the system specifies the
   following configurations:
   - <InputLocale>en-US</InputLocale>
   - <SystemLocale>en-US</SystemLocale>
   - <UILanguage>en-US</UILanguage>
   - <UserLocale>en-US</UserLocale>
   - <HideEULAPage>true</HideEULAPage>
   - <HideWirelessSetupInOOBE>true</HideWirelessSetupInOOBE>
   - <NetworkLocation>Other</NetworkLocation>
   - <ProtectYourPC>3</ProtectYourPC>
   - <BluetoothTaskbarIconEnabled>false</BluetoothTaskbarIconEnabled>
   - <TimeZone>UTC</TimeZone>
   - <RegisteredOrganization>Amazon.com</RegisteredOrganization>
   - <RegisteredOwner>Amazon</RegisteredOwner>

###### Note

During the generalize and specialize phases the EC2Config service
monitors the status of the OS. If EC2Config detects that the OS is
in a Sysprep phase, then it publishes the following message to the
system log:

**`EC2ConfigMonitorState: 0 Windows is being configured.
 SysprepState=IMAGE_STATE_UNDEPLOYABLE`** 2. After the OOBE phase completes, the system runs
`SetupComplete.cmd` from the following location:
`C:\Windows\Setup\Scripts\SetupComplete.cmd`.
In Amazon public AMIs before April 2015 this file was empty and ran
nothing on the image. In
public AMIs dated after April 2015, the file includes the following
value: **call "C:\Program Files\Amazon\Ec2ConfigService\Scripts\PostSysprep.cmd"**. 3. The system runs `PostSysprep.cmd`, which performs the following
operations:

    * Sets the local Administrator password to not expire. If the
     password expired, Administrators might not be able to log
     on.
    * Sets the MSSQLServer machine name (if installed) so that the
     name will be in sync with the AMI.

## Post Sysprep

After Windows Sysprep completes, the EC2Config services sends the following message to the
console output:

```
Windows sysprep configuration complete.
			Message: Sysprep Start
			Message: Sysprep End
```

EC2Config then performs the following actions:

1. Reads the content of the config.xml file and lists all enabled plug-ins.
2. Executes all “Before Windows is ready” plug-ins at the same time.
   - Ec2SetPassword
   - Ec2SetComputerName
   - Ec2InitializeDrives
   - Ec2EventLog
   - Ec2ConfigureRDP
   - Ec2OutputRDPCert
   - Ec2SetDriveLetter
   - Ec2WindowsActivate
   - Ec2DynamicBootVolumeSize

3. After it is finished, sends a “Windows is ready” message to the instance
   system logs.
4. Runs all “After Windows is ready” plug-ins at the same time.
   - Amazon CloudWatch Logs
   - UserData
   - AWS Systems Manager (Systems Manager)

For more information about Windows plug-ins, see [Use the EC2Config service to perform tasks during EC2 legacy Windows
operating system instance launch](ec2config-service.md "ec2config-service.md").

## Run Windows Sysprep with the EC2Config

service

Use the following procedure to create a standardized AMI using Windows Sysprep and the
EC2Config service.

1. In the Amazon EC2 console, locate or [create](creating-an-ami-ebs.md "creating-an-ami-ebs.md") an AMI that you want to duplicate.
2. Launch and connect to your Windows instance.
3. Customize it.
4. Specify configuration settings in the EC2Config service answer
   file:

`C:\Program
 Files\Amazon\Ec2ConfigService\sysprep2008.xml` 5. From the Windows **Start** menu, choose **All
Programs**, and then choose **EC2ConfigService
Settings**. 6. Choose the **Image** tab in the **Ec2 Service
Properties** dialog box. For more information about the options
and settings in the Ec2 Service Properties dialog box, see [Ec2 Service Properties](ec2config-service.md "ec2config-service.md"). 7. Select an option for the Administrator password, and then select
**Shutdown with Sysprep** or **Shutdown without
Sysprep**. EC2Config edits the settings files based on the
password option that you selected.

    * **Random**: EC2Config generates a password,
     encrypts it with user's key, and displays the encrypted password to
     the console. We disable this setting after the first launch so that
     this password persists if the instance is rebooted or stopped and
     started.
    * **Specify**: The password is stored in the
     Windows Sysprep answer file in unencrypted form (clear text). When Windows Sysprep
     runs next, it sets the Administrator password. If you shut down now,
     the password is set immediately. When the service starts again, the
     Administrator password is removed. It's important to remember this
     password, as you can't retrieve it later.
    * **Keep Existing**: The existing password for the
     Administrator account doesn't change when Windows Sysprep is run or
     EC2Config is restarted. It's important to remember this password, as
     you can't retrieve it later.

8. Choose **OK**.

When you are asked to confirm that you want to run Windows Sysprep and shut down the
instance, click **Yes**. You'll notice that EC2Config runs Windows Sysprep.
Next, you are logged off the instance, and the instance is shut down. If you check
the **Instances** page in the Amazon EC2 console, the instance state
changes from `Running` to `Stopping`, and then finally to
`Stopped`. At this point, it's safe to create an AMI from this
instance.

You can manually invoke the Windows Sysprep tool from the command line using the following
command:

```
"%programfiles%\amazon\ec2configservice\"ec2config.exe -sysprep""
```

###### Note

The double quotation marks in the command are not required if your CMD shell
is already in the C:\Program Files\Amazon\EC2ConfigService\ directory.

However, you must be very careful that the XML file options specified in the
`Ec2ConfigService\Settings` folder are correct; otherwise,
you might not be able to connect to the instance. For more information about the
settings files, see [EC2Config settings files](ec2config-service.md#UsingConfigXML_WinAMI "ec2config-service.md#UsingConfigXML_WinAMI"). For an example of configuring and then
running Windows Sysprep from the command line, see
`Ec2ConfigService\Scripts\InstallUpdates.ps1`.
