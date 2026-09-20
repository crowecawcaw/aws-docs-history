

# Troubleshoot your Amazon EC2 instance using the EC2 Serial Console
<a name="troubleshoot-using-serial-console"></a>

By using EC2 Serial Console, you can troubleshoot boot, network configuration, and other issues by connecting to your instance's serial port.

Use the instructions for your instance's operating system and for the tool you've configured on your instance.

**Topics**
+ [GRUB (Linux)](#grub)
+ [SysRq (Linux)](#SysRq)
+ [SAC (Windows)](#troubleshooting-sac)

**Prerequisites**  
Before you begin, make sure you have completed the [ prerequisites](ec2-serial-console-prerequisites.md), including configuring your chosen troubleshooting tool.

## (Linux instances) Use GRUB to troubleshoot your instance
<a name="grub"></a>

GNU GRUB (short for GNU GRand Unified Bootloader, commonly referred to as GRUB) is the default boot loader for most Linux operating systems. From the GRUB menu, you can select which kernel to boot into, or modify menu entries to change how the kernel will boot. This can be useful when troubleshooting a failing instance.

The GRUB menu is displayed during the boot process. The menu is not accessible through normal SSH, but you can access it using the EC2 Serial Console.

You can boot into single user mode or emergency mode. Single user mode will boot the kernel at a lower runlevel. For example, it might mount the filesystem but not activate the network, giving you the opportunity to perform the maintenance necessary to fix the instance. Emergency mode is similar to single user mode except that the kernel runs at the lowest runlevel possible.

**To boot into single user mode**

1. [Connect](connect-to-serial-console.md) to the instance's serial console.

1. Reboot the instance using the following command.

   ```
   [ec2-user ~]$ sudo reboot
   ```

1. During reboot, when the GRUB menu appears, press any key to stop the boot process.

1. In the GRUB menu, use the arrow keys to select the kernel to boot into, and press `e` on your keyboard. 

1. Use the arrow keys to locate your cursor on the line containing the kernel. The line begins with either `linux` or `linux16` depending on the AMI that was used to launch the instance. For Ubuntu, two lines begin with `linux`, which must both be modified in the next step.

1. At the end of the line, add the word `single`.

   The following is an example for Amazon Linux 2.

   ```
   linux /boot/vmlinuz-4.14.193-149.317.amzn2.aarch64 root=UUID=d33f9c9a-\
   dadd-4499-938d-ebbf42c3e499 ro  console=tty0 console=ttyS0,115200n8 net.ifname\
   s=0 biosdevname=0 nvme_core.io_timeout=4294967295 rd.emergency=poweroff rd.she\
   ll=0 single
   ```

1. Press **Ctrl\+X** to boot into single user mode.

1. At the `login` prompt, enter the username of the password-based user that you [set up previously](configure-access-to-serial-console.md#set-user-password), and then press **Enter**.

1. At the `Password` prompt, enter the password, and then press **Enter**.

 

**To boot into emergency mode**  
Follow the same steps as single user mode, but at step 6, add the word `emergency` instead of `single`.

## (Linux instances) Use SysRq to troubleshoot your instance
<a name="SysRq"></a>

The System Request (SysRq) key, which is sometimes referred to as "magic SysRq", can be used to directly send the kernel a command, outside of a shell, and the kernel will respond, regardless of what the kernel is doing. For example, if the instance has stopped responding, you can use the SysRq key to tell the kernel to crash or reboot. For more information, see [Magic SysRq key](https://en.wikipedia.org/wiki/Magic_SysRq_key) in Wikipedia.

You can use SysRq commands in the EC2 Serial Console browser-based client or in an SSH client. The command to send a break request is different for each client.

To use SysRq, choose one of the following procedures based on the client that you are using.

------
#### [ Browser-based client ]

**To use SysRq in the serial console browser-based client**

1. [Connect](connect-to-serial-console.md) to the instance's serial console.

1. To send a break request, press `CTRL+0` (zero). If your keyboard supports it, you can also send a break request using the Pause or Break key.

   ```
   [ec2-user ~]$ CTRL+0
   ```

1. To issue a SysRq command, press the key on your keyboard that corresponds to the required command. For example, to display a list of SysRq commands, press `h`.

   ```
   [ec2-user ~]$ h
   ```

   The `h` command outputs something similar to the following.

   ```
   [ 1169.389495] sysrq: HELP : loglevel(0-9) reboot(b) crash(c) terminate-all-tasks(e) memory-full-oom-kill(f) kill-all-tasks(i) thaw-filesystems
   (j) sak(k) show-backtrace-all-active-cpus(l) show-memory-usage(m) nice-all-RT-tasks(n) poweroff(o) show-registers(p) show-all-timers(q) unraw(r
   ) sync(s) show-task-states(t) unmount(u) show-blocked-tasks(w) dump-ftrace-buffer(z)
   ```

------
#### [ SSH client ]

**To use SysRq in an SSH client**

1. [Connect](connect-to-serial-console.md) to the instance's serial console.

1. To send a break request, press `~B` (tilde, followed by uppercase `B`).

   ```
   [ec2-user ~]$ ~B
   ```

1. To issue a SysRq command, press the key on your keyboard that corresponds to the required command. For example, to display a list of SysRq commands, press `h`.

   ```
   [ec2-user ~]$ h
   ```

   The `h` command outputs something similar to the following.

   ```
   [ 1169.389495] sysrq: HELP : loglevel(0-9) reboot(b) crash(c) terminate-all-tasks(e) memory-full-oom-kill(f) kill-all-tasks(i) thaw-filesystems
   (j) sak(k) show-backtrace-all-active-cpus(l) show-memory-usage(m) nice-all-RT-tasks(n) poweroff(o) show-registers(p) show-all-timers(q) unraw(r
   ) sync(s) show-task-states(t) unmount(u) show-blocked-tasks(w) dump-ftrace-buffer(z)
   ```
**Note**  
The command that you use for sending a break request might be different depending on the SSH client that you're using.

------

## (Windows instances) Use SAC to troubleshoot your instance
<a name="troubleshooting-sac"></a>

The Special Administration Console (SAC) capability of Windows provides a way to troubleshoot a Windows instance. By connecting to the instance's serial console and using SAC, you can interrupt the boot process and boot Windows in safe mode. For information about enabling, using, and disabling SAC and the boot menu, see [Troubleshoot your Windows instance using SAC](troubleshoot-windows-sac.md).