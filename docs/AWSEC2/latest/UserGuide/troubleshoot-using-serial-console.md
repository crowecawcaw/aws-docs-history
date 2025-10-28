# Troubleshoot your Amazon EC2 instance using the

EC2 Serial Console

By using EC2 Serial Console, you can troubleshoot boot, network configuration, and other
issues by connecting to your instance's serial port.

Use the instructions for your instance's operating system and for the tool you've
configured on your instance.

###### Tools

- [GRUB (Linux)](#grub "#grub")
- [SysRq (Linux)](#SysRq "#SysRq")
- [SAC (Windows)](#troubleshooting-sac "#troubleshooting-sac")

###### Prerequisites

Before you begin, make sure you have completed the [prerequisites](ec2-serial-console-prerequisites.md "ec2-serial-console-prerequisites.md"), including configuring
your chosen troubleshooting tool.

## (Linux instances) Use GRUB to troubleshoot your instance

GNU GRUB (short for GNU GRand Unified Bootloader, commonly referred to as GRUB) is the
default boot loader for most Linux operating systems. From the GRUB menu, you can select
which kernel to boot into, or modify menu entries to change how the kernel will boot. This
can be useful when troubleshooting a failing instance.

The GRUB menu is displayed during the boot process. The menu is not accessible via
normal SSH, but you can access it using the EC2 Serial Console.

You can boot into single user mode or emergency mode. Single user mode will boot the
kernel at a lower runlevel. For example, it might mount the filesystem but not activate the
network, giving you the opportunity to perform the maintenance necessary to fix the
instance. Emergency mode is similar to single user mode except that the kernel runs at the
lowest runlevel possible.

###### To boot into single user mode

1. [Connect](connect-to-serial-console.md "connect-to-serial-console.md") to the instance's serial
   console.
2. Reboot the instance using the following command.

```
`[ec2-user ~]$` sudo reboot
```

3. During reboot, when the GRUB menu appears, press any key to stop the boot
   process.
4. In the GRUB menu, use the arrow keys to select the kernel to boot into, and press
   `e` on your keyboard.
5. Use the arrow keys to locate your cursor on the line containing the kernel. The line
   begins with either `linux` or `linux16` depending on the AMI that
   was used to launch the instance. For Ubuntu, two lines begin with `linux`,
   which must both be modified in the next step.
6. At the end of the line, add the word `single`.

The following is an example for Amazon Linux 2.

```
linux /boot/vmlinuz-4.14.193-149.317.amzn2.aarch64 root=UUID=d33f9c9a-\
dadd-4499-938d-ebbf42c3e499 ro  console=tty0 console=ttyS0,115200n8 net.ifname\
s=0 biosdevname=0 nvme_core.io_timeout=4294967295 rd.emergency=poweroff rd.she\
ll=0 single
```

7. Press **Ctrl+X** to boot into single user mode.
8. At the `login` prompt, enter the username of the password-based user that
   you [set up previously](configure-access-to-serial-console.md#set-user-password "configure-access-to-serial-console.md#set-user-password"), and then press **Enter**.
9. At the `Password` prompt, enter the password, and then press **Enter**.

 

###### To boot into emergency mode

Follow the same steps as single user mode, but at step 6, add the word
`emergency` instead of `single`.

## (Linux instances) Use SysRq to troubleshoot your instance

The System Request (SysRq) key, which is sometimes referred to as "magic SysRq", can be
used to directly send the kernel a command, outside of a shell, and the kernel will respond,
regardless of what the kernel is doing. For example, if the instance has stopped responding,
you can use the SysRq key to tell the kernel to crash or reboot. For more information, see
[Magic SysRq key](https://en.wikipedia.org/wiki/Magic_SysRq_key "https://en.wikipedia.org/wiki/Magic_SysRq_key") in
Wikipedia.

You can use SysRq commands in the EC2 Serial Console browser-based client or in an SSH
client. The command to send a break request is different for each client.

To use SysRq, choose one of the following procedures based on the client that you are
using.

Browser-based client

###### To use SysRq in the serial console browser-based client

1. [Connect](connect-to-serial-console.md "connect-to-serial-console.md") to the instance's
   serial console.
2. To send a break request, press `CTRL+0` (zero). If your keyboard
   supports it, you can also send a break request using the Pause or Break
   key.

```
`[ec2-user ~]$` CTRL+0
```

3. To issue a SysRq command, press the key on your keyboard that corresponds to
   the required command. For example, to display a list of SysRq commands, press
   `h`.

```
`[ec2-user ~]$` h
```

The `h` command outputs something similar to the following.

```
[ 1169.389495] sysrq: HELP : loglevel(0-9) reboot(b) crash(c) terminate-all-tasks(e) memory-full-oom-kill(f) kill-all-tasks(i) thaw-filesystems
(j) sak(k) show-backtrace-all-active-cpus(l) show-memory-usage(m) nice-all-RT-tasks(n) poweroff(o) show-registers(p) show-all-timers(q) unraw(r
) sync(s) show-task-states(t) unmount(u) show-blocked-tasks(w) dump-ftrace-buffer(z)
```

SSH client

###### To use SysRq in an SSH client

1. [Connect](connect-to-serial-console.md "connect-to-serial-console.md") to the instance's
   serial console.
2. To send a break request, press `~B` (tilde, followed by uppercase
   `B`).

```
`[ec2-user ~]$` ~B
```

3. To issue a SysRq command, press the key on your keyboard that corresponds to
   the required command. For example, to display a list of SysRq commands, press
   `h`.

```
`[ec2-user ~]$` h
```

The `h` command outputs something similar to the following.

```
[ 1169.389495] sysrq: HELP : loglevel(0-9) reboot(b) crash(c) terminate-all-tasks(e) memory-full-oom-kill(f) kill-all-tasks(i) thaw-filesystems
(j) sak(k) show-backtrace-all-active-cpus(l) show-memory-usage(m) nice-all-RT-tasks(n) poweroff(o) show-registers(p) show-all-timers(q) unraw(r
) sync(s) show-task-states(t) unmount(u) show-blocked-tasks(w) dump-ftrace-buffer(z)
```

###### Note

The command that you use for sending a break request might be different
depending on the SSH client that you're using.

## (Windows instances) Use SAC to troubleshoot your

instance

The Special Admin Console (SAC) capability of Windows provides a way to troubleshoot a
Windows instance. By connecting to the instance's serial console and using SAC, you can
interrupt the boot process and boot Windows in safe mode.

###### Note

If you enable SAC on an instance, the EC2 services that rely on password retrieval
will not work from the Amazon EC2 console. Windows on Amazon EC2 launch agents (EC2Config, EC2Launch
v1, and EC2Launch v2) rely on the serial console to execute various tasks. These tasks do
not perform successfully when you enable SAC on an instance. For more information about
Windows on Amazon EC2 launch agents, see [Configure your Amazon EC2 Windows instance](ec2-windows-instances.md "ec2-windows-instances.md"). If you enable
SAC, you can disable it later. For more information, see [Disable SAC and the boot menu](#disable-sac-bootmenu "#disable-sac-bootmenu").

###### Tasks

- [Use SAC](#use-sac "#use-sac")
- [Use the boot menu](#use-boot-menu "#use-boot-menu")
- [Disable SAC and the boot menu](#disable-sac-bootmenu "#disable-sac-bootmenu")

### Use SAC

###### To use SAC

1. [Connect to the serial
   console.](connect-to-serial-console.md "connect-to-serial-console.md")

If SAC is enabled on the instance, the serial console displays the
`SAC>` prompt.

![SAC prompt displayed in the serial console.](images/win-boot-3.png) 2. To display the SAC commands, enter ?, and then press **Enter**.

Expected output

![Enter a question mark to display the SAC commands.](images/win-boot-4.png) 3. To create a command prompt channel (such as `cmd0001` or
`cmd0002`), enter cmd, and then press **Enter**. 4. To view the command prompt channel, press **ESC**,
and then press **TAB**.

Expected output

![The command prompt channel.](images/win-boot-5.png) 5. To switch channels, press **ESC+TAB+channel number**
together. For example, to switch to the `cmd0002` channel (if it has been
created), press **ESC+TAB+2**. 6. Enter the credentials required by the command prompt channel.

![The command prompt requiring credentials.](images/win-boot-6.png)

The command prompt is the same full-featured command shell that you get on a
desktop, but with the exception that it does not allow the reading of characters that
were already output.

![A full-featured command shell.](images/win-boot-7.png)

**PowerShell can also be used from the command
prompt.**

Note that you might need to set the progress preference to silent mode.

![PowerShell within the command prompt.](images/win-boot-8.png)

### Use the boot menu

If the instance has the boot menu enabled and is restarted after connecting through SSH,
you should see the boot menu, as follows.

![Boot menu in the command prompt.](images/win-boot-1.png)

**Boot menu commands**

ENTER

Starts the selected entry of the operating system.

TAB

Switches to the Tools menu.

ESC

Cancels and restarts the instance.

ESC followed by 8

Equivalent to pressing **F8**. Shows advanced
options for the selected item.

ESC key + left arrow

Goes back to the initial boot menu.

The ESC key alone does not take you back to the main menu because Windows is
waiting to see if an escape sequence is in progress.

![Advanced boot options.](images/win-boot-2.png)

### Disable SAC and the boot menu

If you enable SAC and the boot menu, you can disable these features later.

Use one of the following methods to disable SAC and the boot menu on an
instance.

PowerShell

###### To disable SAC and the boot menu on a Windows instance

1. [Connect](connecting_to_windows_instance.md "connecting_to_windows_instance.md") to your
   instance and perform the following steps from an elevated PowerShell command
   line.
2. First disable the boot menu by changing the value to `no`.

```
bcdedit /set '{bootmgr}' displaybootmenu no
```

3. Then disable SAC by changing the value to `off`.

```
bcdedit /ems '{current}' off
```

4. Apply the updated configuration by rebooting the instance.

```
shutdown -r -t 0
```

Command prompt

###### To disable SAC and the boot menu on a Windows instance

1. [Connect](connecting_to_windows_instance.md "connecting_to_windows_instance.md") to your
   instance and perform the following steps from the command prompt.
2. First disable the boot menu by changing the value to `no`.

```
bcdedit /set {bootmgr} displaybootmenu no
```

3. Then disable SAC by changing the value to `off`.

```
bcdedit /ems {current} off
```

4. Apply the updated configuration by rebooting the instance.

```
shutdown -r -t 0
```
