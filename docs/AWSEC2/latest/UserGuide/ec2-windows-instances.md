# Configure your Amazon EC2 Windows instance

After you've launched a Windows instance, you can log in as an administrator
to perform additional configuration for Windows features and system settings.
[EC2 Windows troubleshooting utilities](windows-troubleshooting-utils.md "windows-troubleshooting-utils.md") can help you troubleshoot
issues on your instance.

You can configure Windows launch agents and other Windows-specific features
as follows.

**[Windows launch agents](configure-launch-agents.md "configure-launch-agents.md")**

Each AWS Windows AMI (and many other AMIs that are available on the AWS Marketplace) includes
a Windows launch agent that's pre-configured with default settings. Launch agents perform
tasks during instance startup and run if an instance is stopped and later started, or
restarted.

**[EC2 Fast Launch for Windows](win-ami-config-fast-launch.md "win-ami-config-fast-launch.md")**

Every Amazon EC2 Windows instance must go through the standard Windows operating system (OS)
launch steps, which include several reboots, and often take 15 minutes or longer to
complete. Amazon EC2 Windows Server AMIs that have the EC2 Fast Launch feature enabled
complete some of those steps and reboots in advance to reduce the time it takes to launch
an instance.

## Windows-specific system settings

The following list includes some system settings that apply only for Windows operating systems:

**[Change the Windows Administrator password](ec2-windows-passwords.md "ec2-windows-passwords.md")**

When you connect to a Windows instance, you must specify a user account and password that
has permission to access the instance. The first time that you connect to an instance, you
must use the Administrator account and provide the default password. When you connect to an
instance the first time, we recommend that you change the Administrator password from
its default value.

**[Add Windows System components](windows-optional-components.md "windows-optional-components.md")**

Windows Server operating systems include many optional components. Including all optional
components in each AWS Windows Server AMI is not practical. Instead, we provide
installation media EBS snapshots that have the necessary files to configure or install
components on your Windows instance.

**[Install WSL on Windows](install-wsl-on-ec2-windows-instance.md "install-wsl-on-ec2-windows-instance.md")**

Windows Subsystem for Linux (WSL) is a free download that you can install on your Windows
instance. By installing WSL, you can run native Linux command line tools directly on your
Windows instance and use the Linux tools for scripting, alongside your traditional Windows
desktop. You can easily swap between Linux and Windows on a single Windows instance, which
you might find useful in a development environment.

## AWS device drivers for Windows instances

You can update the AWS device drivers for your Windows instances. For more information,
see [Manage device drivers for your EC2 instance](manage-device-drivers.md "manage-device-drivers.md").

The following table summarizes the supported drivers for [Nitro-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type") by Windows version.

| Version                | Storage driver          | Enhanced networking driver |
| ---------------------- | ----------------------- | -------------------------- |
| Windows Server 2025    | AWS NVMe latest version | ENA latest version         |
| Windows Server 2022    | AWS NVMe latest version | ENA latest version         |
| Windows Server 2019    | AWS NVMe latest version | ENA latest version         |
| Windows Server 2016    | AWS NVMe latest version | ENA latest version         |
| Windows Server 2012 R2 | AWS NVMe version 1.5.1  | ENA version 2.6.0          |
| Windows Server 2008 R2 | AWS NVMe version 1.3.2  | ENA version 2.2.3          |

The following table summarizes the supported drivers for [Xen-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type") by Windows version.

| Version                | Storage driver        | Enhanced networking driver                                          |
| ---------------------- | --------------------- | ------------------------------------------------------------------- |
| Windows Server 2022    | AWS PV latest version | • ENA latest version 1<br>• Intel VF 2<br>• AWS PV latest version 3 |
| Windows Server 2019    | AWS PV latest version | • ENA latest version 1<br>• Intel VF 2<br>• AWS PV latest version 3 |
| Windows Server 2016    | AWS PV latest version | • ENA latest version 1<br>• Intel VF 2<br>• AWS PV latest version 3 |
| Windows Server 2012 R2 | AWS PV version 8.4.3  | • ENA version 2.6.0 1<br>• Intel VF 2<br>• AWS PV version 8.4.3 3   |
| Windows Server 2008 R2 | AWS PV version 8.3.5  | • ENA version 2.2.3 1<br>• Intel VF 2<br>• AWS PV version 8.3.5 3   |

1 For instance types G3, H1, I3, `m4.16xlarge`, P2, P3, P3dn, and R4.

2 For instance types C3, C4, D2, I2, M4 (excluding `m4.16xlarge`), and R3.

3 For instance types C1, M1, M2, M3, T1, T2, X1, and X1e.
