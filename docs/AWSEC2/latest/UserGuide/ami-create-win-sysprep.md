# Create an Amazon EC2 AMI using Windows Sysprep

The Microsoft System Preparation (Windows Sysprep) tool creates a generalized version of
the operating system, with instance-specific system configuration removed before it captures
a new image.

We recommend that you use [EC2 Image Builder](../../../imagebuilder/latest/userguide/what-is-image-builder.md "../../../imagebuilder/latest/userguide/what-is-image-builder.md") to
automate the creation, management, and deployment of customized, secure, and up-to-date
"golden" server images that are pre-installed and preconfigured with software and
settings.

You can also use Windows Sysprep to create a standardized AMI using the Windows
launch agents: EC2Launch v2, EC2Launch, and EC2Config.

###### Important

Do not use Windows Sysprep to create an instance backup. Windows Sysprep removes system-specific
information; removing this information might have unintended consequences for an
instance backup.

To troubleshoot Windows Sysprep, see [Troubleshoot Sysprep issues with Amazon EC2 Windows instances](sysprep-troubleshoot.md "sysprep-troubleshoot.md").

###### Contents

- [Windows Sysprep phases](#sysprep-phases "#sysprep-phases")
- [Before you begin](#sysprep-begin "#sysprep-begin")
- [Use Windows Sysprep with EC2Launch v2](sysprep-using-ec2launchv2.md "sysprep-using-ec2launchv2.md")
- [Use Windows Sysprep with EC2Launch](ec2launch-sysprep.md "ec2launch-sysprep.md")
- [Use Windows Sysprep with EC2Config](sysprep-using.md "sysprep-using.md")

## Windows Sysprep phases

Windows Sysprep runs through the following phases:

- **Generalize**: The Sysprep tool removes
  image-specific information and configurations. For example, Windows Sysprep removes
  the security identifier (SID), the computer name, the event logs, and
  specific drivers, to name a few. After this phase is completed, the
  operating system (OS) is ready to create an AMI.

###### Note

When you run Windows Sysprep with the Windows launch agents, the
system prevents drivers from being removed because
`PersistAllDeviceInstalls` is set to true by
default.

- **Specialize**: Plug and Play scans the
  computer and installs drivers for any detected devices. The Sysprep tool generates
  OS requirements, like the computer name and SID. Optionally, you can run
  commands in this phase.
- **Out-of-Box Experience (OOBE)**: The system
  runs an abbreviated version of Windows Setup and asks you to enter
  information such as system language, time zone, and registered organization.
  When you run Windows Sysprep with Windows launch agents, the answer file automates
  this phase.

## Before you begin

- Before performing Windows Sysprep, we recommend that you remove all local user
  accounts and all account profiles other than a single administrator account
  under which Windows Sysprep will be run. If you perform Windows Sysprep with additional
  accounts and profiles, unexpected behavior could result, including loss of
  profile data or failure to complete Windows Sysprep.
- Learn more about [Sysprep Overview](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--system-preparation--overview "https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--system-preparation--overview").
- Learn which [Sysprep Support for Server Roles](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep-support-for-server-roles "https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep-support-for-server-roles").
