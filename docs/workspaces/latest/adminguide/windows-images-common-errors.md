

# Common error messages and their solutions
<a name="windows-images-common-errors"></a><a name="windows-images-errors"></a><a name="OfficeInstalled"></a>

## BYOL import does not support systems with active Standalone Microsoft Office installed. BYOL import only supports Microsoft Office 365 applications to be present on the source before starting the import process.
<a name="OfficeInstalled-collapsed"></a>

Standalone Microsoft Office (Non Microsoft Office 365) must be uninstalled before import. For more information, see [ Uninstall Office from a PC](https://support.microsoft.com/en-au/office/uninstall-office-from-a-pc-9dd49b83-264a-477a-8fcc-2fdf5dbf61d8).<a name="PCoIPAgentInstalled"></a>

## BYOL import requires a system without a PCoIP Agent.
<a name="PCoIPAgentInstalled-collapsed"></a>

Uninstall the PCoIP Agent. For information about uninstalling the PCoIP agent, see [ Uninstalling the Teradici PCoIP Software Client for Mac](https://www.teradici.com/web-help/ter1307002/1.10/Content/Topics/03_Installing.htm)<a name="WindowsUpdatesEnabled"></a>

## BYOL import requires that Windows updates are disabled.
<a name="WindowsUpdatesEnabled-collapsed"></a>

Disable Windows updates by following the following steps:

1. Press **Windows key** \+ **R**. Type `services.msc`, then press **Enter**.

1. Right-click on **Windows Update**, then choose **Properties**.

1. Under the **General** tab, set the **Startup type** to **Disabled**.

1. Choose **Stop**.

1. Click **Apply**, and then choose **OK**.

1. Restart your computer.<a name="AutoMountDisabled"></a>

## BYOL import requires that Automount is enabled.
<a name="AutoMountDisabled-collapsed"></a>

You must enable Automount. Run the following command in powershell as an administrator.

```
C:\> diskpart
DISKPART> automount enable
```

Automatic mounting of new volumes enabled.<a name="WorkspacesBYOLAccountDisabled"></a>

## BYOL import requires the WorkSpaces\_BYOL account to be enabled
<a name="WorkspacesBYOLAccountDisabled-collapsed"></a>

WorkSpaces\_BYOL account must be enabled. For more information, see [ Enable BYOL for your account for BYOL using the Amazon WorkSpaces console](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html#windows_images_enable_byol).<a name="DHCPDisabled"></a>

## BYOL import requires the network interface to use DHCP to automatically assign an IP address. The network interface is currently using a static IP address.
<a name="DHCPDisabled-collapsed"></a>

Network interface must be changed to use DHCP. For more information, see [ Change TCP/IP settings](https://support.microsoft.com/en-us/windows/change-tcp-ip-settings-bd0a07af-15f5-cd6a-363f-ca2b6f391ace).<a name="DiskFreeSpace"></a>

## BYOL import requires more than 20 GB of space on the local disk.
<a name="DiskFreeSpace-collapsed"></a>

Local disk must have enough space and requires you to free up 20 GB or more.<a name="AdditionalDrivesAttache"></a>

## BYOL import requires systems with 1 local drive. There are additional Local, Removable or Network drives.
<a name="AdditionalDrivesAttached-collapsed"></a>

Only the C drive can be present on an Amazon Machine Image that is being used for importing BYOL WorkSpace Image. Remove all other drives, including virtual drives.<a name="OSNotSupported"></a>

## BYOL import requires Windows 10 or Windows 11.
<a name="OSNotSupported-collapsed"></a>

Use a Windows 10 or Windows 11 operating system.<a name="DomainJoined"></a>

## BYOL import requires systems that are not AD domain joined.
<a name="DomainJoined-collapsed"></a>

System must be unjoined from AD domain. For more information, see [ Azure Active Directory device management FAQ](https://learn.microsoft.com/en-us/azure/active-directory/devices/faq#how-do-i-unjoin-an-azure-ad-joined-device-locally-on-the-device).<a name="AzureDomainJoined"></a>

## BYOL import requires systems that are not Azure domain joined.
<a name="AzureDomainJoined-collapsed"></a>

System must be unjoined from Azure domain. For more information, see [ Azure Active Directory device management FAQ](https://learn.microsoft.com/en-us/azure/active-directory/devices/faq#how-do-i-unjoin-an-azure-ad-joined-device-locally-on-the-device).<a name="FirewallEnabled"></a>

## BYOL import requires Windows Public Firewall disabled.
<a name="FirewallEnabled-collapsed"></a>

Public firewall profile must be disabled. For more information, see [ Turn Microsoft Defender Firewall on or off](https://support.microsoft.com/en-us/windows/turn-microsoft-defender-firewall-on-or-off-ec0844f7-aebd-0583-67fe-601ecf5d774f).<a name="VMWareToolsInstalled"></a>

## BYOL import requires a system without VMware tools.
<a name="VMWareToolsInstalled-collapsed"></a>

VMWare tools must be uninstalled. For more information, see [ Uninstalling and manually installing VMware Tools in VMware Fusion (1014522)](https://kb.vmware.com/s/article/1014522#:~:text=reinstall%20VMware%20Tools.-,Uninstalling%20VMware%20Tools,-To%20uninstall%20VMware).<a name="DiskSizeExceeded"></a>

## BYOL import requires the local disk to be less than 80 GB.
<a name="DiskSizeExceeded-collapsed"></a>

The disk must be smaller than 80 GB. Reduce the disk size.<a name="IncompatiblePartitioning"></a>

## BYOL import requires less than 2 partitions on the local drive. In addition, all Windows 10 partitions must be MBR partitioned and all Windows 11 partitions must be GPT partitioned.
<a name="IncompatiblePartitioning-collapsed"></a>

Volumes must be MBR partitioned for Windows 10 and GPT partitioned for Windows 11. For more information, see [Manage disks](https://learn.microsoft.com/en-us/windows-server/storage/disk-management/manage-disks).<a name="PendingReboot"></a>

## BYOL import requires all pending updates that require reboots are complete.
<a name="PendingReboot-collapsed"></a>

Install all updates and reboot the operating system.<a name="AutoLogonEnabled"></a>

## BYOL import requires that AutoLogon is disabled.
<a name="AutoLogonEnabled-collapsed"></a>

**To disable the AutoLogon registry:**

1. Press **Windows key** \+ **R** and type `Regedit.exe` in the command prompt.

1. Scroll down to `HKEY_LOCAL_Machine\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\Winlogon`

1. Add a value for `DontDisplayLastUserName`.

1. For **Type**, enter `REG_SZ`.

1. For **Value**, enter `0`.

**Note**  
The value `DontDisplayLastUserName` determines whether the logon dialog box displays the username of the last user that logged onto the PC.
The value does not exist by default. If it exists, you must set it to `0` or the value of `DefaultUser` will be wiped and AutoLogon will fail.<a name="RealTimeUniversalDisabled"></a>

## BYOL import requires `RealTimeIsUniversal` to be enabled.
<a name="RealTimeUniversalDisabled-collapsed"></a>

RealTimeUniversal Registry Key must be enabled. For more information, see [ Configure time settings for Windows Server 2008 and later](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/windows-set-time.html#windows-persisting-time-changes-w2k8).<a name="MultipleBootPartition"></a>

## BYOL import requires a system with one bootable partition.
<a name="MultipleBootPartition-collapsed"></a>

Number of bootable partitions must not exceed one.

**To remove additional partitions**

1. Press the **Windows logo** \+ **R** keys to open **Run** box. Enter `msconfig` and press the **Enter** key on the keyboard to open the System Configuration window.

1. Choose the **Boot** tab from the window and check if the OS you want to use is set to **Current OS; Default OS**. If it isn't set, choose your desired OS from the window and choose **Set as default** on the same window.

1. To delete another partition, choose that partition, then select **Delete**, **Apply**, **OK**.

**If the error still shows up, boot your computer from the installation or repair disc, and follow these steps.**

1. Skip the initial languages screen, and then choose **Repair your computer** on the main install screen.

1. On the **Choose an option** screen, choose **Troubleshoot**.

1. On the **Advanced options** screen, choose **Command Prompts**.

1. In the command prompt, enter `bootrec.exe /fixmbr`, then press **Enter**.<a name="Requires64BitOS"></a>

## BYOL import requires a 64 bit system.
<a name="Requires64BitOS-collapsed"></a>

A 64 bit OS image must be used. For more information, see [ Windows versions supported for BYOL](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html#windows_images_supported_versions).<a name="InPlaceUpgrade"></a>

## BYOL import requires a system that has not been upgraded in-place. This system has been upgraded in-place.
<a name="InPlaceUpgrade-collapsed"></a>

Windows must not have been upgraded from a previous version.<a name="AntiVirusInstalled"></a>

## BYOL import requires that no antivirus is installed on the system.
<a name="AntiVirusInstalled-collapsed"></a>

You must uninstall your antivirus software. Run Image Compatibility Checker to get details for the antivirus software to uninstall.<a name="UEFINotSupported"></a>

## BYOL import requires Windows 10 systems to have a legacy Boot mode.
<a name="UEFINotSupported-collapsed"></a>

The Legacy BIOS BootMode must be used for Windows 10.For more information, see [Boot modes](https://docs.aws.amazon.com/vm-import/latest/userguide/prerequisites.html#vmimport-boot-modes).

## BYOL Import requires Windows Reserved Storage state to be disabled
<a name="WindowsReservedStorage-collapsed"></a>

**To disable the Reserved Storage State**

1. Install all Windows updates and reboot the operating system.

1. Make sure there are no new updates.

1. Run either of the following command in Powershell as an administrator.
   + 

     ```
     Set-WindowsReservedStorageState -State Disabled
     ```
   + 

     ```
     DISM.exe /Online /Set-ReservedStorageState /State:Disabled
     ```

1. Reboot the System.

**Note**  
If reserved storage is in use, it might not be disabled, and the following error message is returned: `This operation is not supported when reserved storage is in use. Please wait for any servicing operations to complete and then try again later.`

## BYOL import has a restricted drive letter in use.
<a name="RestrictedDriveLetterInUse-collapsed"></a>

The `D:` Drive is a restricted drive letter for WorkSpaces. Please ensure that `D:` is not being used or will not be mapped to during launch of an instance from the image.

## BYOL import has an OS image that is incompatible with the streaming protocol selected.
<a name="ProtocolOSIncompatibility-collapsed"></a>

 The image being imported is not supported by the streaming protocol chosen, see [ Create a BYOL image using the WorkSpaces console](https://docs.aws.amazon.com/workspaces/latest/adminguide/windows_images_create_byol_image_console.html).

## BYOL import is incompatible with memory integrity.
<a name="MemoryIntegrityIncompatibility-collapsed"></a>

Memory Integrity is not supported when Credential Guard is enabled on the Windows operating system of a WorkSpace. Memory Integrity was detected with UEFILock which cannot be disabled during image import. Please import an image with UEFILock disabled, see [Disable Credential Guard](https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/configure?tabs=intune#disable-credential-guard).

## BYOL Import requires Bitlocker state to be disabled.
<a name="DisableBitlocker-collapsed"></a>

To Disable Bitlocker:

1. Open Powershell as an administrator.

1. Run the following command:

   ```
   manage-bde -off  {{DriveLetter}}:
   ```

1. Check the status of BitLocker by running the below command:

   ```
   manage-bde -Status  {{DriveLetter}}:
   ```

1. Ensure the values shown match these:
   + **BitLocker Version** – None
   + **Conversion Status** – Fully Decrypted
   + **Percentage Encrypted** – 0.0%
   + **Encryption Method** – None
   + **Protection Status** – Protection Off
   + **Lock Status** – Unlocked<a name="NTPConfigurationError"></a>

## WorkSpaces creation fails due to time synchronization issues with custom images
<a name="NTPConfigurationError-collapsed"></a>

By default, custom images reach out to "time.windows.com" as the default NTP server. If the NTP server is not reachable, time synchronization issues can occur, causing RDP/Skylight certificate validation failures and SSL connection problems that prevent WorkSpaces creation.

If you encounter time synchronization issues, update the NTP server to use the Amazon Time Sync Service at 169.254.169.123. For more information, see [Configure the time for your Windows instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-ec2-ntp.html).