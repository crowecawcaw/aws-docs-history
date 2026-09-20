

# Troubleshoot your Windows instance using SAC
<a name="troubleshoot-windows-sac"></a>

The Special Administration Console (SAC) capability of Windows provides a way to troubleshoot a Windows instance through the instance serial port. By connecting using the EC2 Serial Console, you can troubleshoot boot, network configuration, and other issues through SAC. You can interrupt the boot process or boot Windows in safe mode. With SAC, you can enter commands to an instance as if your keyboard and monitor are directly attached to the instance's serial port. The serial console does not require your instance to have any networking capabilities.

For the equivalent Linux troubleshooting tools (GRUB and SysRq), see [Troubleshoot your Amazon EC2 instance using the EC2 Serial Console](troubleshoot-using-serial-console.md).

**Topics**
+ [Prerequisites](#sac-prerequisites)
+ [Enable SAC and the boot menu](#enable-sac-bootmenu)
+ [Use SAC](#use-sac)
+ [Built-in SAC commands](#sac-builtin-commands)
+ [Use the boot menu](#use-boot-menu)
+ [Known behaviors](#sac-known-behaviors)
+ [Disable SAC and the boot menu](#disable-sac-bootmenu)
+ [See also](#sac-see-also)

## Prerequisites
<a name="sac-prerequisites"></a>

Using SAC requires access to the EC2 Serial Console. Before you begin, complete the steps in [Prerequisites for the EC2 Serial Console](ec2-serial-console-prerequisites.md) and [Configure access to the EC2 Serial Console](configure-access-to-serial-console.md). SAC must also be enabled on the instance. To enable SAC, see [Enable SAC and the boot menu](#enable-sac-bootmenu).

SAC requires at least the [EC2Launch v2.5.0](ec2launch-v2.md) agent and [EC2WinUtil driver v3.2.0](ec2winutil-driver-version-history.md). EC2Launch v2 relies on the serial port to perform several initialization tasks during boot, such as emitting the instance password and RDP thumbprint. Wait until the instance fully initializes before you connect to the serial console. If you connect before EC2Launch v2 emits its output, or if the minimum required versions are not installed, you might not be able to retrieve the instance password or other console output.

For more information about EC2Launch v2, see [Use the EC2Launch v2 agent to perform tasks during EC2 Windows instance launch](ec2launch-v2.md).

## Enable SAC and the boot menu
<a name="enable-sac-bootmenu"></a>

Before you can use SAC to troubleshoot an instance, you must enable SAC on the instance. You can optionally enable the boot menu so that you can interrupt the boot process.

**Note**  
Starting with version 2026.09.09, SAC is enabled by default on the following AWS AMIs:  
`EC2LaunchV2-Windows_Server-2019-English-Core-Base-*`
`EC2LaunchV2-Windows_Server-2019-English-Full-Base-*`
If you launch these AMIs on bare metal instances, you must manually re-enable SAC using the following steps.

Use one of the following methods to enable SAC and the boot menu on an instance.

------
#### [ PowerShell ]

**To enable SAC and the boot menu on a Windows instance**

1. [Connect](connecting_to_windows_instance.md) to your instance and perform the following steps from an elevated PowerShell command line.

1. Enable SAC.

   ```
   bcdedit /ems '{current}' on
   bcdedit /emssettings EMSPORT:1 EMSBAUDRATE:115200
   ```

   On bare metal instances, use the following instead. This directs Windows to use the EMS serial port defined by the instance firmware.

   ```
   bcdedit /ems '{current}' on
   bcdedit /emssettings BIOS
   ```

1. (Optional) Enable the boot menu.

   ```
   bcdedit /set '{bootmgr}' displaybootmenu yes
   bcdedit /set '{bootmgr}' timeout 15
   bcdedit /set '{bootmgr}' bootems yes
   ```

1. Apply the updated configuration by rebooting the instance.

   ```
   shutdown -r -t 0
   ```

------
#### [ Command prompt ]

**To enable SAC and the boot menu on a Windows instance**

1. [Connect](connecting_to_windows_instance.md) to your instance and perform the following steps from the command prompt.

1. Enable SAC.

   ```
   bcdedit /ems {current} on
   bcdedit /emssettings EMSPORT:1 EMSBAUDRATE:115200
   ```

   On bare metal instances, use the following instead. This directs Windows to use the EMS serial port defined by the instance firmware.

   ```
   bcdedit /ems {current} on
   bcdedit /emssettings BIOS
   ```

1. (Optional) Enable the boot menu.

   ```
   bcdedit /set {bootmgr} displaybootmenu yes
   bcdedit /set {bootmgr} timeout 15
   bcdedit /set {bootmgr} bootems yes
   ```

1. Apply the updated configuration by rebooting the instance.

   ```
   shutdown -r -t 0
   ```

------

## Use SAC
<a name="use-sac"></a>

You can use SAC to open a shell channel for instance troubleshooting. Use one of the following methods to open a command prompt or PowerShell channel from the `SAC>` prompt.

------
#### [ PowerShell ]

**To use PowerShell from SAC**

1. [Connect to the serial console.](connect-to-serial-console.md)

   If SAC is enabled on the instance, the serial console displays the `SAC>` prompt. You might see a blank screen instead of the `SAC>` prompt. Press **Enter** to display the `SAC>` prompt.  
![SAC prompt displayed in the serial console.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/win-boot-3.png)

1. To list available commands, enter `?`, and then press **Enter**.  
![SAC command prompt displaying available commands.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/win-boot-4.png)

1. To create a command prompt channel (such as `cmd0001` or `cmd0002`), enter `cmd`, and then press **Enter**.

1. To view the command prompt channel, press **ESC**, and then press **TAB**.

1. To switch channels, press **ESC\+TAB\+channel number** together. For example, to switch to the `cmd0002` channel (if it has been created), press **ESC\+TAB\+2**.

1. Enter the credentials required by the command prompt channel.

1. Start PowerShell from the command prompt channel.

   ```
   powershell
   ```

   To prevent progress output from interfering with the serial console, set the progress preference to silent mode.

   ```
   $ProgressPreference = "SilentlyContinue"
   ```  
![PowerShell within the command prompt.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/win-boot-8.png)

------
#### [ Command prompt ]

**To use the command prompt from SAC**

1. [Connect to the serial console.](connect-to-serial-console.md)

   If SAC is enabled on the instance, the serial console displays the `SAC>` prompt. You might see a blank screen instead of the `SAC>` prompt. Press **Enter** to display the `SAC>` prompt.  
![SAC prompt displayed in the serial console.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/win-boot-3.png)

1. To list available commands, enter `?`, and then press **Enter**.  
![SAC command prompt displaying available commands.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/win-boot-4.png)

1. To create a command prompt channel (such as `cmd0001` or `cmd0002`), enter `cmd`, and then press **Enter**.

1. To view the command prompt channel, press **ESC**, and then press **TAB**.  
![The command prompt channel.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/win-boot-5.png)

1. To switch channels, press **ESC\+TAB\+channel number** together. For example, to switch to the `cmd0002` channel (if it has been created), press **ESC\+TAB\+2**.

1. Enter the credentials required by the command prompt channel.  
![The command prompt requiring credentials.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/win-boot-6.png)

   The command prompt is the same full-featured command shell that you get on a desktop, but with the exception that it does not allow the reading of characters that were already output.  
![A full-featured command shell.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/win-boot-7.png)

------

## Built-in SAC commands
<a name="sac-builtin-commands"></a>

Beyond opening a command prompt channel, SAC provides built-in commands that you can run directly at the `SAC>` prompt for out-of-band administration. These commands do not require you to sign in. The following table lists the built-in commands available at the `SAC>` prompt. To display this list from within SAC, enter `?` or `help`. SAC commands are not case-sensitive.


| Command | Description | 
| --- | --- | 
| ch | Lists all available channels. Enter ch -? for channel management help. | 
| cmd | Creates a Windows command prompt channel. You must provide administrative credentials to use the channel. | 
| d | Displays the current kernel log. | 
| f | Toggles the t (tlist) output between showing processes only and showing both processes and threads. | 
| ? or help | Lists the available SAC commands. | 
| i | Lists all network interfaces with their IP addresses. | 
| i <\#> <ip> <subnet> <gateway> | Sets the IP address, subnet mask, and gateway for the specified network interface number. Useful for restoring connectivity after a network misconfiguration locks you out of the instance. | 
| id | Displays the instance identification information. | 
| k <pid> | Ends the process with the specified process ID. Useful for stopping an unresponsive process. | 
| l <pid> | Lowers the priority of the specified process to the lowest possible value. | 
| lock | Locks access to command prompt channels. | 
| m <pid> <MB-allow> | Limits the memory usage of the specified process to the specified number of megabytes. | 
| p | Pauses the t (tlist) output after each screen of information. | 
| r <pid> | Raises the priority of the specified process by one level. | 
| s | Displays the current date and time. To set them, use s mm/dd/yyyy hh:mm. | 
| t | Lists the running processes and threads (tlist). | 
| restart | Restarts the instance immediately. | 
| shutdown | Shuts down the instance immediately. | 
| crashdump | Forces a stop error (crash) so the instance generates a memory dump for analysis. The instance must have crash dump enabled. | 

## Use the boot menu
<a name="use-boot-menu"></a>

If the boot menu is enabled and you restart the instance after connecting through the serial console, the boot menu should appear as follows.

![Boot menu in the command prompt.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/win-boot-1.png)


**Boot menu commands**

**ENTER**  
Starts the selected entry of the operating system.

**TAB**  
Switches to the Tools menu.

**ESC**  
Cancels and restarts the instance.

**ESC** followed by **8**  
Equivalent to pressing **F8**. Shows advanced options for the selected item.

**ESC** key \+ **left arrow**  
Goes back to the initial boot menu.  
The ESC key alone does not take you back to the main menu because Windows is waiting to see if an escape sequence is in progress.

![Advanced boot options.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/win-boot-2.png)


## Known behaviors
<a name="sac-known-behaviors"></a>
+ **SAC not appearing on bare metal instances** – If the SAC console does not appear when you connect to the serial console, SAC might be using the wrong serial port device. To re-enable SAC on a bare metal instance, see the bare metal instructions in [Enable SAC and the boot menu](#enable-sac-bootmenu).
+ **Blank screen on connect** – When you connect to the serial console on a Windows instance with SAC enabled, you might see a blank screen instead of the `SAC>` prompt. Press **Enter** to display the `SAC>` prompt.
+ **Unexpected output in system log** – If you enable SAC or the boot menu, the Amazon EC2 system log (available from the Amazon EC2 console or the `get-console-output` AWS Command Line Interface (AWS CLI) command) might contain output from SAC or the boot menu. You might see output from SAC such as `SAC> EVENT: The CMD command is now available.` or ANSI escape sequences such as `[2J[1;1H[0m[37;40m` from the boot menu. This output is expected behavior.

## Disable SAC and the boot menu
<a name="disable-sac-bootmenu"></a>

If you enable SAC and the boot menu, you can disable these features later.

Use one of the following methods to disable SAC and the boot menu on an instance.

------
#### [ PowerShell ]

**To disable SAC and the boot menu on a Windows instance**

1. [Connect](connecting_to_windows_instance.md) to your instance and perform the following steps from an elevated PowerShell command line.

1. First disable the boot menu by changing the value to `no`.

   ```
   bcdedit /set '{bootmgr}' displaybootmenu no
   ```

1. Then disable SAC by changing the value to `off`.

   ```
   bcdedit /ems '{current}' off
   ```

1. Apply the updated configuration by rebooting the instance.

   ```
   shutdown -r -t 0
   ```

------
#### [ Command prompt ]

**To disable SAC and the boot menu on a Windows instance**

1. [Connect](connecting_to_windows_instance.md) to your instance and perform the following steps from the command prompt.

1. First disable the boot menu by changing the value to `no`.

   ```
   bcdedit /set {bootmgr} displaybootmenu no
   ```

1. Then disable SAC by changing the value to `off`.

   ```
   bcdedit /ems {current} off
   ```

1. Apply the updated configuration by rebooting the instance.

   ```
   shutdown -r -t 0
   ```

------

## See also
<a name="sac-see-also"></a>
+ [Troubleshoot your Amazon EC2 instance using the EC2 Serial Console](troubleshoot-using-serial-console.md) – GRUB and SysRq troubleshooting tools for Linux instances.
+ [Connect to the EC2 Serial Console](connect-to-serial-console.md)
+ [Prerequisites for the EC2 Serial Console](ec2-serial-console-prerequisites.md)
+ [Configure access to the EC2 Serial Console](configure-access-to-serial-console.md)