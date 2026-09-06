

# Kernel debugging for Windows instances over the network
<a name="troubleshoot-windows-with-kdnet"></a>

The KDNET Extensibility Module for Elastic Network Adapter (ENA) is a hardware driver support layer that enables Windows kernel debugging over the network through ENA on Amazon Elastic Compute Cloud instances. You can use the extensibility module with the Windows Debugger (WinDbg) to perform kernel-level debugging on EC2 instances running Windows.

Kernel debugging helps you diagnose and troubleshoot low-level operating system issues such as blue screen errors (BSODs), driver failures, and boot problems on your EC2 Windows instances.

**Topics**
+ [Prerequisites](#kdnet-prerequisites)
+ [Step 1: Install Windows Debugging Tools on the debug host](#kdnet-step1-install-debugging-tools)
+ [Step 2: Set up the debug target](#kdnet-step2-setup-debug-target)
+ [Step 3: Start the debugging session on the debug host](#kdnet-step3-start-debugging-session)
+ [Step 4: Reboot the debug target](#kdnet-step4-reboot-debug-target)
+ [Clean up debug settings after debugging](#kdnet-clean-up)
+ [Limitations](#kdnet-limitations)
+ [Additional notes](#kdnet-additional-notes)

## Prerequisites
<a name="kdnet-prerequisites"></a>

Before you begin, make sure you have the following:

Two EC2 Windows instances, in the same subnet:
+ A **debug host** instance — runs the Windows Debugger (WinDbg).
+ A **debug target** instance — the instance you want to debug.

For more information about launching instances, see [Get started with Amazon EC2](EC2_GetStarted.md).

Security groups for the host and target instances must allow inbound and outbound UDP traffic on the port used for KDNET debugging (recommended range: 50000–50039). The simplest way to set this up is to create a security group with an inbound rule that allows UDP traffic from itself as the source, and then attach that security group to both instances. For more information, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html) in the *Amazon VPC User Guide*.

The debug target instance must run one of these Windows versions (or later):
+ Windows Server 2025 with build number 26100.7462 (December 2025 patch)
+ Windows 11 24H2 with build number 26100.7309
+ Windows 11 25H2 with build number 26200.7309

**Note**  
The KDNET extensibility module for ENA is distributed as part of Windows and can only be updated through Windows monthly cumulative updates. We recommend keeping the latest Windows KB installed on the debug target to ensure you have the most recent version of it.  
To verify that the module is present on the debug target, run the following command in an elevated PowerShell session:  

```
Test-Path C:\Windows\system32\kd_02_1d0f.dll
```
If the command returns `True`, the module is available.

## Step 1: Install Windows Debugging Tools on the debug host
<a name="kdnet-step1-install-debugging-tools"></a>

Install the Windows Debugging Tools on the debug host instance by running the following command in a PowerShell session:

```
winget install microsoft.windbg
```

For detailed installation instructions, see [Install the Windows Debugger](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) in the Microsoft documentation.

After installation, verify that the debugger is working by running the following command in a PowerShell session:

```
windbgx
```

The WinDbg window should open. If it does, the installation was successful and you can close the window.

## Step 2: Set up the debug target
<a name="kdnet-step2-setup-debug-target"></a>

**Note**  
When kernel debugging is active, the ENA device used for the debugging session is dedicated to debugger traffic only. If you need to maintain internet access on the debug target instance during debugging, attach a second ENA to the instance before you begin.

On the debug target, open an elevated PowerShell session and configure kernel debugging using the following steps.

Run the following command to list the bus, device, and function number of the ENA adapter attached to the instance:

```
Get-NetAdapter -Physical |
    Where-Object -Property PnPDeviceID -Match -Value '^PCI\\VEN_1D0F&DEV_EC2[01]&' |
    Get-NetAdapterHardwareInfo |
    Select-Object InterfaceDescription, BusNumber, DeviceNumber, FunctionNumber |
    Format-List
```

### If multiple ENA adapters are attached to the instance
<a name="kdnet-multiple-ena-adapters"></a>

If multiple ENA adapters are attached to the instance, use the following command to map each physical adapter to its private IP address. You can cross-reference these details in the AWS Management Console under **EC2 → Instances → [Instance ID] → Networking → Network interfaces**. This helps you correlate specific Network Interface IDs, private IPs, and security groups with the OS-level adapter for targeted debugging.

```
Get-NetAdapter -Physical |
    Where-Object PnPDeviceID -Match '^PCI\\VEN_1D0F&DEV_EC2[01]&' |
    ForEach-Object {
        $adapter = $_
        $hwInfo = $adapter | Get-NetAdapterHardwareInfo
        $ipInfo = Get-NetIPAddress -InterfaceIndex $adapter.InterfaceIndex -AddressFamily IPv4
        [PSCustomObject]@{
            InterfaceDescription = $adapter.InterfaceDescription
            IPAddress            = $ipInfo.IPAddress
            BusNumber            = $hwInfo.BusNumber
            DeviceNumber         = $hwInfo.DeviceNumber
            FunctionNumber       = $hwInfo.FunctionNumber
        }
    } | Format-List
```

Note the `BusNumber`, `DeviceNumber`, and `FunctionNumber` values of the ENA adapter to be used for debugging from the output.

Run the following commands to configure kernel debugging. Replace the placeholder values with your specific configuration:

```
bcdedit /debug on
bcdedit /set loadoptions FORCEHVTONOTSHAREDEBUGDEVICE
bcdedit /dbgsettings net hostip:{{host-private-ip}} port:{{port-number}} key:{{encryption-key}} busparams:{{b.d.f}}
```

**Note**  
Check for existing `loadoptions` by running the following command. If a value is returned, copy that string and append `;FORCEHVTONOTSHAREDEBUGDEVICE` to it.  

```
(bcdedit /enum) -match "loadoptions"
```

Where:
+ {{host-private-ip}} — The private IPv4 address of the debug host instance. If your instances are launched in an IPv6-only subnet, see [Setting up KDNET with IPv6](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/setting-up-a-network-debugging-connection#ipv6) in the Microsoft documentation to learn more about using IPv6 with KDNET.
+ {{port-number}} — The port to use for the debugging session. The recommended range is 50000–50039 (for example, `50000`).
+ {{encryption-key}} — A 256-bit key used to encrypt the debugging connection, specified as four 64-bit values separated by periods. Each 64-bit value can be up to 13 characters long using only lowercase letters a–z and digits 0–9. Special characters are not allowed. Example encryption key: `1kdnet2keys3.4kdnet5keys6.7kdnet8keys9.10kdnet11ke`.
+ {{b.d.f}} — The bus, device, and function numbers for the ENA device, formatted as `bus.device.function` (for example, `0.3.0`), used for debugging.

**Tip**  
To debug the Windows boot process, also run the following command:  

```
bcdedit /bootdebug on
```

## Step 3: Start the debugging session on the debug host
<a name="kdnet-step3-start-debugging-session"></a>

To allow debugging traffic on the host, you can create a firewall rule for either the WinDbg application or a specific UDP port.

**Option 1: Allow the WinDbg application**  
Run the following commands to authorize the WinDbg executable:

```
$WinDbgxPath = "$env:LocalAppData\Microsoft\WindowsApps\WinDbgX.exe"
New-NetFirewallRule -DisplayName "Allow Inbound KDNET Connection" -Action Allow -Program $WinDbgxPath
```

**Option 2: Allow a specific UDP port**  
Alternatively, you can allow inbound UDP traffic to the port configured for kernel debugging. Replace {{port-number}} with your chosen KDNET port:

```
$DebugPort = {{port-number}}
New-NetFirewallRule -DisplayName "Allow Inbound KDNET Connection" -Direction Inbound -LocalPort $DebugPort -Protocol UDP -Action Allow
```

**Note**  
Firewall configurations may be restricted by Domain Group Policy (GPO) or require elevated Administrator permissions. If the command fails, contact your network administrator.

Start WinDbg with the port and key that match the debug target configuration. You can specify additional kernel debugging options documented in the [Microsoft WinDbg command line reference](https://learn.microsoft.com/en-us/windows-hardware/drivers/debuggercmds/windbg-command-line-preview#kernel-options) to suit your use case.

```
windbgx -k net:port={{port-number}},key={{encryption-key}}
```

WinDbg opens and waits for the debug target to connect.

## Step 4: Reboot the debug target
<a name="kdnet-step4-reboot-debug-target"></a>

On the debug target, restart the instance to initiate the debugging connection:

```
shutdown -r -t 0
```

After the debug target restarts, WinDbg on the debug host connects to the target automatically. You can now use WinDbg to inspect the kernel state, set breakpoints, and diagnose issues.

## Clean up debug settings after debugging
<a name="kdnet-clean-up"></a>

**On the debug target**  
After you finish debugging, remove the kernel debugging configuration from the debug target to restore normal boot behavior. On the debug target, open an elevated PowerShell session and run the following commands:

```
bcdedit /debug off
bcdedit /dbgsettings LOCAL
bcdedit /deletevalue loadoptions
```

If you have existing `loadoptions` other than `FORCEHVTONOTSHAREDEBUGDEVICE`, you should restore the setting by running `bcdedit /set loadoptions` with the original `loadoptions`.

If you enabled boot debugging, also run:

```
bcdedit /bootdebug off
```

Restart the instance for the changes to take effect.

**On the debug host**  
Remove the firewall rule by running:

```
Remove-NetFirewallRule -DisplayName "Allow Inbound KDNET Connection"
```

## Limitations
<a name="kdnet-limitations"></a>

The KDNET extensibility module for ENA does not currently support:
+ 8th generation non-metal x86\_64 instance types (for example, `m8a.xlarge`)
+ 7th generation 48xlarge non-metal x86\_64 instance types (for example, `m7a.48xlarge`)
+ u7i instance types

The module does not currently support instances with Secure Boot enabled. You can verify the status by running `Confirm-SecureBootUEFI` in an elevated PowerShell session. If the output is `True`, Secure Boot is active. Note that all Amazon-provided images with a 'TPM' prefix have Secure Boot enabled by default.

## Additional notes
<a name="kdnet-additional-notes"></a>

If you encounter issues connecting the debugger to the target instance, verify the following:
+ All prerequisites listed in this guide are met, including the required Windows Server build version and the presence of the extensibility module.
+ The security groups attached to both instances are configured correctly to allow traffic between them on the configured debugging port.
+ Windows Firewall rules on the host instances do not block network traffic between the two instances on the configured port.

For additional guidance, see [Set up KDNET network kernel debugging manually](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/setting-up-a-network-debugging-connection) in the Microsoft documentation.