# Prerequisites for the EC2 Serial

Console

###### To connect to the EC2 Serial Console and use your chosen tool for

troubleshooting, the following prerequisites must be met:

- [AWS Regions](#sc-prereqs-regions "#sc-prereqs-regions")
- [Wavelength Zones and AWS
  Outposts](#sc-prereqs-wavelength-zones-outposts "#sc-prereqs-wavelength-zones-outposts")
- [Local Zones](#sc-prereqs-local-zones "#sc-prereqs-local-zones")
- [Instance types](#sc-prereqs-instance-types "#sc-prereqs-instance-types")
- [Grant access](#sc-prereqs-configure-ec2-serial-console "#sc-prereqs-configure-ec2-serial-console")
- [Support for browser-based
  client](#sc-prereqs-for-browser-based-connection "#sc-prereqs-for-browser-based-connection")
- [Instance state](#sc-prereqs-instance-state "#sc-prereqs-instance-state")
- [Amazon EC2 Systems Manager](#sc-prereqs-ssm "#sc-prereqs-ssm")
- [Configure your chosen
  troubleshooting tool](#sc-prereqs-configure-troubleshooting-tool "#sc-prereqs-configure-troubleshooting-tool")

## AWS Regions

Supported in all AWS Regions except Asia Pacific (Taipei).

## Wavelength Zones and AWS

Outposts

Not supported.

## Local Zones

Supported in all Local Zones.

## Instance types

Supported instance types:

- **Linux**
  - All virtualized instances built on the Nitro System.
  - All bare metal instances except:
    - General purpose: `a1.metal`, `mac1.metal`,
      `mac2.metal`
    - Accelerated computing: `g5g.metal`
    - Memory optimized: `u-6tb1.metal`, `u-9tb1.metal`,
      `u-12tb1.metal`, `u-18tb1.metal`,
      `u-24tb1.metal`

- **Windows**

All virtualized instances built on the Nitro System. Not supported on bare metal
instances.

## Grant access

You must complete the configuration tasks to grant access to the EC2 Serial Console. For
more information, see [Configure access to the EC2 Serial Console](configure-access-to-serial-console.md "configure-access-to-serial-console.md").

## Support for browser-based

client

To connect to the serial console [using
the browser-based client](connect-to-serial-console.md#sc-connect-browser-based-client "connect-to-serial-console.md#sc-connect-browser-based-client"), your browser must support WebSocket. If your browser does
not support WebSocket, connect to the serial console [using
your own key and an SSH client.](connect-to-serial-console.md#sc-connect-SSH "connect-to-serial-console.md#sc-connect-SSH")

## Instance state

Must be `running`.

You can't connect to the serial console if the instance is in the `pending`,
`stopping`, `stopped`, `shutting-down`, or
`terminated` state.

For more information about the instance states, see [Amazon EC2 instance state changes](ec2-instance-lifecycle.md "ec2-instance-lifecycle.md").

## Amazon EC2 Systems Manager

If the instance uses Amazon EC2 Systems Manager, then SSM Agent version 3.0.854.0 or later must be
installed on the instance. For information about SSM Agent, see [Working with SSM Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md") in
the _AWS Systems Manager User Guide_.

## Configure your chosen

troubleshooting tool

To troubleshoot your instance using the serial console, you can use GRUB or SysRq on Linux
instances, and Special Admin Console (SAC) on Windows instances. Before you can use these
tools, you must first perform configuration steps on every instance on which you'll use
them.

Use the instructions for your instance's operating system to configure your chosen
troubleshooting tool.

To configure GRUB, choose one of the following procedures based on the AMI that was
used to launch the instance.

Amazon Linux 2

###### To configure GRUB on an Amazon Linux 2 instance

1.  [Connect to your Linux instance using SSH](connect-to-linux-instance.md "connect-to-linux-instance.md")
2.  Add or change the following options in
    `/etc/default/grub`:

        * Set `GRUB_TIMEOUT=1`.
        * Add `GRUB_TERMINAL="console serial"`.
        * Add `GRUB_SERIAL_COMMAND="serial --speed=115200"`.

    The following is an example of `/etc/default/grub`. You might
    need to change the configuration based on your system setup.

```
GRUB_CMDLINE_LINUX_DEFAULT="console=tty0 console=ttyS0,115200n8 net.ifnames=0 biosdevname=0 nvme_core.io_timeout=4294967295 rd.emergency=poweroff rd.shell=0"
GRUB_TIMEOUT=1
GRUB_DISABLE_RECOVERY="true"
GRUB_TERMINAL="console serial"
GRUB_SERIAL_COMMAND="serial --speed=115200"
```

3. Apply the updated configuration by running the following command.

```
`[ec2-user ~]$` sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

Ubuntu

###### To configure GRUB on an Ubuntu instance

1.  [Connect](connect-to-linux-instance.md "connect-to-linux-instance.md") to your
    instance.
2.  Add or change the following options in
    `/etc/default/grub.d/50-cloudimg-settings.cfg`:

        * Set `GRUB_TIMEOUT=1`.
        * Add `GRUB_TIMEOUT_STYLE=menu`.
        * Add `GRUB_TERMINAL="console serial"`.
        * Remove `GRUB_HIDDEN_TIMEOUT`.
        * Add `GRUB_SERIAL_COMMAND="serial --speed=115200"`.

    The following is an example of
    `/etc/default/grub.d/50-cloudimg-settings.cfg`. You might need to
    change the configuration based on your system setup.

```
# Cloud Image specific Grub settings for Generic Cloud Images
# CLOUD_IMG: This file was created/modified by the Cloud Image build process

# Set the recordfail timeout
GRUB_RECORDFAIL_TIMEOUT=0

# Do not wait on grub prompt
GRUB_TIMEOUT=1
GRUB_TIMEOUT_STYLE=menu

# Set the default commandline
GRUB_CMDLINE_LINUX_DEFAULT="console=tty1 console=ttyS0 nvme_core.io_timeout=4294967295"

# Set the grub console type
GRUB_TERMINAL="console serial"
GRUB_SERIAL_COMMAND="serial --speed 115200"
```

3. Apply the updated configuration by running the following command.

```
`[ec2-user ~]$` sudo update-grub
```

RHEL

###### To configure GRUB on a RHEL instance

1.  [Connect](connect-to-linux-instance.md "connect-to-linux-instance.md") to your
    instance.
2.  Add or change the following options in
    `/etc/default/grub`:

        * Remove `GRUB_TERMINAL_OUTPUT`.
        * Add `GRUB_TERMINAL="console serial"`.
        * Add `GRUB_SERIAL_COMMAND="serial --speed=115200"`.

    The following is an example of `/etc/default/grub`. You might
    need to change the configuration based on your system setup.

```
GRUB_TIMEOUT=1
GRUB_DISTRIBUTOR="$(sed 's, release .*$,,g' /etc/system-release)"
GRUB_DEFAULT=saved
GRUB_DISABLE_SUBMENU=true
GRUB_CMDLINE_LINUX="console=tty0 console=ttyS0,115200n8 net.ifnames=0 rd.blacklist=nouveau nvme_core.io_timeout=4294967295 crashkernel=auto"
GRUB_DISABLE_RECOVERY="true"
GRUB_ENABLE_BLSCFG=true
GRUB_TERMINAL="console serial"
GRUB_SERIAL_COMMAND="serial --speed=115200"
```

3. Apply the updated configuration by running the following command.

```
`[ec2-user ~]$` sudo grub2-mkconfig -o /boot/grub2/grub.cfg --update-bls-cmdline
```

For RHEL 9.2 and earlier, use the following command.

```
`[ec2-user ~]$` sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

CentOS
For instances that are launched using a CentOS AMI, GRUB is configured for the
serial console by default.

The following is an example of `/etc/default/grub`. Your
configuration might be different based on your system setup.

```
GRUB_TIMEOUT=1
GRUB_DISTRIBUTOR="$(sed 's, release .*$,,g' /etc/system-release)"
GRUB_DEFAULT=saved
GRUB_DISABLE_SUBMENU=true
GRUB_TERMINAL="serial console"
GRUB_SERIAL_COMMAND="serial --speed=115200"
GRUB_CMDLINE_LINUX="console=tty0 crashkernel=auto console=ttyS0,115200"
GRUB_DISABLE_RECOVERY="true"
```

To configure SysRq, you enable the SysRq commands for the current boot cycle. To
make the configuration persistent, you can also enable the SysRq commands for subsequent
boots.

###### To enable all SysRq commands for the current boot cycle

1. [Connect](connect-to-linux-instance.md "connect-to-linux-instance.md") to your
   instance.
2. Run the following command.

```
`[ec2-user ~]$` sudo sysctl -w kernel.sysrq=1
```

This setting will clear on the next reboot.

###### To enable all SysRq commands for subsequent boots

1. Create the file `/etc/sysctl.d/99-sysrq.conf` and open it in your
   favorite editor.

```
`[ec2-user ~]$` sudo vi /etc/sysctl.d/99-sysrq.conf
```

2. Add the following line.

```
kernel.sysrq=1
```

3. Reboot the instance to apply the changes.

```
`[ec2-user ~]$` sudo reboot
```

4. At the `login` prompt, enter the username of the password-based user
   that you [set up previously](configure-access-to-serial-console.md#set-user-password "configure-access-to-serial-console.md#set-user-password"), and then press
   **Enter**.
5. At the `Password` prompt, enter the password, and then press
   **Enter**.

###### Note

If you enable SAC on an instance, the EC2 services that rely on password retrieval
will not work from the Amazon EC2 console. Windows on Amazon EC2 launch agents (EC2Config,
EC2Launch v1, and EC2Launch v2) rely on the serial console to execute various tasks.
These tasks do not perform successfully when you enable SAC on an instance. For more
information about Windows on Amazon EC2 launch agents, see [Configure your Amazon EC2 Windows instance](ec2-windows-instances.md "ec2-windows-instances.md"). If you enable SAC, you can disable it later. For
more information, see [Disable SAC and the boot menu](troubleshoot-using-serial-console.md#disable-sac-bootmenu "troubleshoot-using-serial-console.md#disable-sac-bootmenu").

Use one of the following methods to enable SAC and the boot menu on an
instance.

PowerShell

###### To enable SAC and the boot menu on a Windows instance

1. [Connect](connecting_to_windows_instance.md "connecting_to_windows_instance.md") to your
   instance and perform the following steps from an elevated PowerShell command
   line.
2. Enable SAC.

```
bcdedit /ems '{current}' on
bcdedit /emssettings EMSPORT:1 EMSBAUDRATE:115200
```

3. Enable the boot menu.

```
bcdedit /set '{bootmgr}' displaybootmenu yes
bcdedit /set '{bootmgr}' timeout 15
bcdedit /set '{bootmgr}' bootems yes
```

4. Apply the updated configuration by rebooting the instance.

```
shutdown -r -t 0
```

Command prompt

###### To enable SAC and the boot menu on a Windows instance

1. [Connect](connecting_to_windows_instance.md "connecting_to_windows_instance.md") to your
   instance and perform the following steps from the command prompt.
2. Enable SAC.

```
bcdedit /ems {current} on
bcdedit /emssettings EMSPORT:1 EMSBAUDRATE:115200
```

3. Enable the boot menu.

```
bcdedit /set {bootmgr} displaybootmenu yes
bcdedit /set {bootmgr} timeout 15
bcdedit /set {bootmgr} bootems yes

```

4. Apply the updated configuration by rebooting the instance.

```
shutdown -r -t 0
```
