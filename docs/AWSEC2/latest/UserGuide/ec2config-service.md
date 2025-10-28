# Use the EC2Config service to perform tasks during EC2 legacy Windows

operating system instance launch

###### Note

EC2Config has reached the end of support. The operating system versions that it runs on
are no longer supported by Microsoft. We strongly recommend that you upgrade to the latest
launch agent.

The latest launch agent for Windows Server 2022 and later operating system versions is
[EC2Launch v2](ec2launch-v2.md "ec2launch-v2.md"), which replaces both EC2Config and EC2Launch,
and comes pre-installed on AWS Windows Server 2022 and 2025 AMIs. You can also manually install
and configure the agent on Windows Server 2016 and 2019. For more information, see
[Install EC2Launch v2](ec2launch-v2-install.md "ec2launch-v2-install.md").

Windows AMIs for Windows Server versions prior to Windows Server 2016 include an optional
service, the EC2Config service (`EC2Config.exe`). EC2Config starts when
the instance boots and performs tasks during startup and each time you stop or start the
instance. EC2Config can also perform tasks on demand. Some of these tasks are automatically
enabled, while others must be enabled manually. Although optional, this service provides
access to advanced features that aren't otherwise available. This service runs in the
LocalSystem account.

The EC2Config service runs Sysprep, a Microsoft tool that enables you to create a customized
Windows AMI that can be reused. When EC2Config calls Sysprep, it uses the files in
`%ProgramFiles%\Amazon\EC2ConfigService\Settings` to determine
which operations to perform. You can edit these files indirectly using the **EC2
Service Properties** system dialog, or directly using an XML editor or a text
editor. However, there are some advanced settings that aren't available in the
**Ec2 Service Properties** system dialog, so you must edit those
entries directly.

If you create an AMI from an instance after updating its settings, the new settings
are applied to any instance that's launched from the new AMI. For information about
creating an AMI, see [Create an Amazon EBS-backed AMI](creating-an-ami-ebs.md "creating-an-ami-ebs.md").

EC2Config uses settings files to control its operation. You can update these settings
files using either a graphical tool or by directly editing XML files. The service binaries
and additional files are contained in the
`%ProgramFiles%\Amazon\EC2ConfigService` directory.

###### Contents

- [EC2Config and AWS Systems Manager](#ec2config-ssm "#ec2config-ssm")
- [EC2Config tasks](#UsingConfig_Ovw "#UsingConfig_Ovw")
- [EC2Config settings files](#UsingConfigXML_WinAMI "#UsingConfigXML_WinAMI")
- [Install the latest version of EC2Config](UsingConfig_Install.md "UsingConfig_Install.md")
- [Configure .NET proxy settings for the EC2Config service](ec2config-proxy.md "ec2config-proxy.md")
- [Set EC2Config service properties from the system dialog on your EC2 Windows instance](set-ec2config-service-properties.md "set-ec2config-service-properties.md")
- [Troubleshoot issues with the EC2Config launch agent](repair-ec2config.md "repair-ec2config.md")
- [EC2Config version history](ec2config-version-details.md "ec2config-version-details.md")

## EC2Config and AWS Systems Manager

The EC2Config service processes Systems Manager requests on instances created from AMIs for versions
of Windows Server prior to Windows Server 2016 that were published before November 2016.

Instances created from AMIs for versions of Windows Server prior to Windows Server 2016 that
were published after November 2016 include the EC2Config service _and_ SSM Agent.
EC2Config performs all of the tasks described earlier, and SSM Agent processes requests
for Systems Manager capabilities like Run Command and State Manager.

You can use Run Command to upgrade your existing instances to use to the latest
version of the EC2Config service and SSM Agent. For more information, see [Update SSM Agent using
Run Command](../../../systems-manager/latest/userguide/run-command-tutorial-update-software.md "../../../systems-manager/latest/userguide/run-command-tutorial-update-software.md") in the _AWS Systems Manager User Guide_.

## EC2Config tasks

EC2Config runs initial startup tasks when the instance is first started and then
disables them. To run these tasks again, you must explicitly enable them prior to
shutting down the instance, or by running Sysprep manually. These tasks are as
follows:

- Set a random, encrypted password for the administrator account.
- Generate and install the host certificate used for Remote Desktop
  Connection.
- Dynamically extend the operating system partition to include any unpartitioned
  space.
- Execute the specified user data (and Cloud-Init, if it's installed). For more information
  about specifying user data, see [Run commands when you launch an EC2 instance with user data input](user-data.md "user-data.md").

EC2Config performs the following tasks every time the instance starts:

- Change the host name to match the private IP address in Hex notation (this
  task is disabled by default and must be enabled in order to run at instance
  start).
- Configure the key management server (AWS KMS), check for Windows activation status, and
  activate Windows as necessary.
- Mount all Amazon EBS volumes and instance store volumes, and map volume names to
  drive letters.
- Write event log entries to the console to help with troubleshooting (this task
  is disabled by default and must be enabled in order to run at instance
  start).
- Write to the console that Windows is ready.
- Add a custom route to the primary network adapter to enable the following IP addresses
  when a single NIC or multiple NICs are attached: `169.254.169.250`,
  `169.254.169.251`, and `169.254.169.254`. These addresses are used by Windows
  Activation and when you access instance metadata.

###### Note

If the Windows OS is configured to use IPv4, these IPv4 link-local addresses can be used. If
the Windows OS has the IPv4 network protocol stack disabled and uses IPv6
instead, add `[fd00:ec2::250]` in place of
`169.254.169.250` and `169.254.169.251`. Then add
`[fd00:ec2::254]` in place of
`169.254.169.254`.

EC2Config performs the following task every time a user logs in:

- Display wallpaper information to the desktop background.

While the instance is running, you can request that EC2Config perform the following
task on demand:

- Run Sysprep and shut down the instance so that you can create an AMI from it.
  For more information, see [Create an Amazon EC2 AMI using Windows Sysprep](ami-create-win-sysprep.md "ami-create-win-sysprep.md").

## EC2Config settings files

The settings files control the operation of the EC2Config service. These files are
located in the `C:\Program Files\Amazon\Ec2ConfigService\Settings`
directory:

- `ActivationSettings.xml`—Controls product activation
  using a key management server (AWS KMS).
- `AWS.EC2.Windows.CloudWatch.json`—Controls which
  performance counters to send to CloudWatch and which logs to send to CloudWatch Logs.
- `BundleConfig.xml`—Controls how EC2Config prepares an instance
  store-backed instance for AMI creation.
- `Config.xml`—Controls the primary settings.
- `DriveLetterConfig.xml`—Controls drive letter
  mappings.
- `EventLogConfig.xml`—Controls the event log
  information that's displayed on the console while the instance is
  booting.
- `WallpaperSettings.xml`—Controls the information
  that's displayed on the desktop background.

###### ActivationSettings.xml

This file contains settings that control product activation. When Windows boots,
the EC2Config service checks whether Windows is already activated. If Windows is not
already activated, it attempts to activate Windows by searching for the specified
AWS KMS server.

- `SetAutodiscover`—Indicates whether to detect a AWS KMS
  automatically.
- `TargetKMSServer`—Stores the private IP address of a AWS KMS. The AWS KMS
  must be in the same Region as your instance.
- `DiscoverFromZone`—Discovers the AWS KMS server from the specified DNS
  zone.
- `ReadFromUserData`—Gets the AWS KMS server from UserData.
- `LegacySearchZones`—Discovers the AWS KMS server from the specified DNS
  zone.
- `DoActivate`—Attempts activation using the specified settings
  in the section. This value can be `true` or
  `false`.
- `LogResultToConsole`—Displays the result to the
  console.

###### BundleConfig.xml

This file contains settings that control how EC2Config prepares an instance for
AMI creation.

- `AutoSysprep`—Indicates whether to use Sysprep automatically.
  Change the value to `Yes` to use Sysprep.
- `SetRDPCertificate`—Sets a self-signed certificate to the Remote Desktop
  server. This enables you to securely RDP into the instances. Change the value to
  `Yes` if the new instances should have the certificate.

This setting is not used for instances with operating system versions prior
to Windows Server 2016, because they can generate their own certificates.

- `SetPasswordAfterSysprep`—Sets a random password on a newly
  launched instance, encrypts it with the user launch key, and outputs the
  encrypted password to the console. Change the value of this setting to
  `No` if the new instances should not be set to a random encrypted
  password.

###### Config.xml

_Plug-ins_

- `Ec2SetPassword`—Generates a random encrypted password each
  time you launch an instance. This feature is disabled by default after the first
  launch so that reboots of this instance don't change a password set by the user.
  Change this setting to `Enabled` to continue to generate passwords
  each time you launch an instance.

This setting is important if you are planning to create an AMI from your
instance.

- `Ec2SetComputerName`—Sets the host name of the instance to a
  unique name based on the IP address of the instance and reboots the instance. To
  set your own host name, or prevent your existing host name from being modified,
  you must disable this setting.
- `Ec2InitializeDrives`—Initializes and formats all volumes
  during startup. This feature is enabled by default.
- `Ec2EventLog`—Displays event log entries in the console. By
  default, the three most recent error entries from the system event log are
  displayed. To specify the event log entries to display, edit the
  `EventLogConfig.xml` file located in the
  `EC2ConfigService\Settings` directory. For information
  about the settings in this file, see [Eventlog Key](https://learn.microsoft.com/en-us/windows/win32/eventlog/eventlog-key "https://learn.microsoft.com/en-us/windows/win32/eventlog/eventlog-key").
- `Ec2ConfigureRDP`—Sets up a self-signed certificate on the
  instance, so users can securely access the instance using Remote Desktop. This
  setting is not used for instances with operating system versions prior
  to Windows Server 2016, because they can generate their own certificates.
- `Ec2OutputRDPCert`—Displays the Remote Desktop certificate
  information to the console so that the user can verify it against the
  thumbprint.
- `Ec2SetDriveLetter`—Sets the drive letters of the mounted
  volumes based on user-defined settings. By default, when an Amazon EBS volume is
  attached to an instance, it can be mounted using the drive letter on the
  instance. To specify your drive letter mappings, edit the
  `DriveLetterConfig.xml` file located in the
  `EC2ConfigService\Settings` directory.
- `Ec2WindowsActivate`—The plug-in handles Windows activation.
  It checks to see if Windows is activated. If not, it updates the AWS KMS client
  settings, and then activates Windows.

To modify the AWS KMS settings, edit the
`ActivationSettings.xml` file located in the
`EC2ConfigService\Settings` directory.

- `Ec2DynamicBootVolumeSize`—Extends Disk 0/Volume 0 to include
  any unpartitioned space.
- `Ec2HandleUserData`—Creates and runs scripts created by the user on
  the first launch of an instance after Sysprep is run. Commands wrapped in script
  tags are saved to a batch file, and commands wrapped in PowerShell tags are
  saved to a .ps1 file (corresponds to the User Data checkbox on the Ec2 Service
  Properties system dialog).
- `Ec2ElasticGpuSetup`—Installs the Elastic GPU software package if the
  instance is associated with an elastic GPU.
- `Ec2FeatureLogging`—Sends Windows feature installation and corresponding service status
  to the console. Supported only for the Microsoft Hyper-V feature and corresponding vmms service.

_Global Settings_

- `ManageShutdown`—Ensures that instances launched from Amazon S3-backed AMIs do
  not terminate while running Sysprep.
- `SetDnsSuffixList`—Sets the DNS suffix of the network adapter
  for Amazon EC2. This allows DNS resolution of servers running in Amazon EC2 without
  providing the fully qualified domain name.

###### Note

This adds a DNS suffix lookup for the following domain and configures other
standard suffixes. For more information about how launch
agents set DNS suffixes, see [Configure DNS Suffix for EC2 Windows launch agents](launch-agents-set-dns.md "launch-agents-set-dns.md").

```
`region`.ec2-utilities.amazonaws.com
```

- `WaitForMetaDataAvailable`—Ensures that the EC2Config service
  will wait for metadata to be accessible and the network available before
  continuing with the boot. This check ensures that EC2Config can obtain
  information from metadata for activation and other plug-ins.
- `ShouldAddRoutes`—Adds a custom route to the primary network
  adapter to enable the following IP addresses when multiple NICs are attached:
  169.254.169.250, 169.254.169.251, and 169.254.169.254. These addresses are used
  by Windows Activation and when you access instance metadata.
- `RemoveCredentialsfromSyspreponStartup`—Removes the
  administrator password from `Sysprep.xml` the next time the
  service starts. To ensure that this password persists, edit this setting.

###### DriveLetterConfig.xml

This file contains settings that control drive letter mappings. By default, a
volume can be mapped to any available drive letter. You can mount a volume to a
particular drive letter as follows.

```
<?xml version="1.0" standalone="yes"?>
<DriveLetterMapping>
  <Mapping>
    <VolumeName></VolumeName>
    <DriveLetter></DriveLetter>
  </Mapping>
  . . .
  <Mapping>
    <VolumeName></VolumeName>
    <DriveLetter></DriveLetter>
  </Mapping>
</DriveLetterMapping>
```

- `VolumeName`—The volume label. For example,
  `My Volume`. To specify a mapping
  for an instance storage volume, use the label `Temporary
Storage X`, where `X` is a number from 0 to

25.

- `DriveLetter`—The drive letter. For example,
  `M:`. The mapping fails if the
  drive letter is already in use.

###### EventLogConfig.xml

This file contains settings that control the event log information that's
displayed on the console while the instance is booting. By default, we display the
three most recent error entries from the System event log.

- `Category`—The event log key to monitor.
- `ErrorType`—The event type (for example, `Error`,
  `Warning`, `Information`.)
- `NumEntries`—The number of events stored for this
  category.
- `LastMessageTime`—To prevent the same message from being
  pushed repeatedly, the service updates this value every time it pushes a
  message.
- `AppName`—The event source or application that logged the
  event.

###### WallpaperSettings.xml

This file contains settings that control the information that's displayed on the
desktop background. The following information is displayed by default.

- `Hostname`—Displays the computer name.
- `Instance ID`—Displays the ID of the instance.
- `Public IP Address`—Displays the public IP address of the
  instance.
- `Private IP Address`—Displays the private IP address of the
  instance.
- `Availability Zone`—Displays the Availability Zone in which
  the instance is running.
- `Instance Size`—Displays the type of instance.
- `Architecture`—Displays the setting of the `PROCESSOR_ARCHITECTURE` environment variable.

You can remove any of the information that's displayed by default by deleting its
entry. You can add additional instance metadata to display as follows.

```
<WallpaperInformation>
  <name>`display_name`</name>
  <source>metadata</source>
  <identifier>meta-data/`path`</identifier>
</WallpaperInformation>
```

You can add additional System environment variables to display as follows.

```
<WallpaperInformation>
  <name>`display_name`</name>
  <source>EnvironmentVariable</source>
  <identifier>`variable-name`</identifier>
</WallpaperInformation>
```

###### InitializeDrivesSettings.xml

This file contains settings that control how EC2Config initializes drives.

By default, EC2Config initialize drives that were not brought online with the
operating system. You can customize the plugin as follows.

```
<InitializeDrivesSettings>
    <SettingsGroup>`setting`</SettingsGroup>
</InitializeDrivesSettings>
```

Use a settings group to specify how you want to initialize drives:

_FormatWithTRIM_

Enables the TRIM command when formatting drives. After a drive has been
formatted and initialized, the system restores TRIM configuration.

Starting with EC2Config version 3.18, the TRIM command is disabled during
the disk format operation by default. This improves formatting times. Use
this setting to enable TRIM during the disk format operation for EC2Config
version 3.18 and later.

_FormatWithoutTRIM_

Disables the TRIM command when formatting drives and improves formatting
times in Windows. After a drive has been formatted and initialized, the
system restores TRIM configuration.

_DisableInitializeDrives_

Disables formatting for new drives. Use this setting to initialize drives
manually.
