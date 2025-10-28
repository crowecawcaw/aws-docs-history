# Common error messages and their solutions

Microsoft Office must be uninstalled before import. For more information, see
[Uninstall Office from a PC](https://support.microsoft.com/en-au/office/uninstall-office-from-a-pc-9dd49b83-264a-477a-8fcc-2fdf5dbf61d8 "https://support.microsoft.com/en-au/office/uninstall-office-from-a-pc-9dd49b83-264a-477a-8fcc-2fdf5dbf61d8").

Uninstall the PCoIP Agent. For information about uninstalling the PCoIP agent, see
[Uninstalling the Teradici PCoIP Software Client for Mac](https://www.teradici.com/web-help/ter1307002/1.10/Content/Topics/03_Installing.htm "https://www.teradici.com/web-help/ter1307002/1.10/Content/Topics/03_Installing.htm")

Disable Windows updates by following the following steps:

1. Press **Windows key** + **R**.
   Type `services.msc`, then press **Enter**.
2. Right-click on **Windows Update**, then choose **Properties**.
3. Under the **General** tab, set the **Startup type** to **Disabled**.
4. Choose **Stop**.
5. Click **Apply**, and then choose **OK**.
6. Restart your computer.
   You must enable Automount. Run the following command in powershell as an
   administrator.

```
C:\> diskpart
DISKPART> automount enable
```

Automatic mounting of new volumes enabled.

WorkSpaces_BYOL account must be enabled. For more information, see
[Enable BYOL for your account for BYOL using the Amazon WorkSpaces console](byol-windows-images.md#windows_images_enable_byol "byol-windows-images.md#windows_images_enable_byol").

Network interface must be changed to use DHCP. For more information, see
[Change TCP/IP settings](https://support.microsoft.com/en-us/windows/change-tcp-ip-settings-bd0a07af-15f5-cd6a-363f-ca2b6f391ace "https://support.microsoft.com/en-us/windows/change-tcp-ip-settings-bd0a07af-15f5-cd6a-363f-ca2b6f391ace").

Local disk must have enough space and requires you to free up 20 GB or more.

Only the C drive can be present on an Amazon Machine Image that is being used for importing BYOL WorkSpace Image. Remove all other drives, including virtual drives.

Use a Windows 10 or Windows 11 operating system.

System must be unjoined from AD domain. For more information, see
[Azure Active Directory device management FAQ](https://learn.microsoft.com/en-us/azure/active-directory/devices/faq#how-do-i-unjoin-an-azure-ad-joined-device-locally-on-the-device "https://learn.microsoft.com/en-us/azure/active-directory/devices/faq#how-do-i-unjoin-an-azure-ad-joined-device-locally-on-the-device").

System must be unjoined from Azure domain. For more information, see
[Azure Active Directory device management FAQ](https://learn.microsoft.com/en-us/azure/active-directory/devices/faq#how-do-i-unjoin-an-azure-ad-joined-device-locally-on-the-device "https://learn.microsoft.com/en-us/azure/active-directory/devices/faq#how-do-i-unjoin-an-azure-ad-joined-device-locally-on-the-device").

Public firewall profile must be disabled. For more information, see
[Turn Microsoft Defender Firewall on or off](https://support.microsoft.com/en-us/windows/turn-microsoft-defender-firewall-on-or-off-ec0844f7-aebd-0583-67fe-601ecf5d774f "https://support.microsoft.com/en-us/windows/turn-microsoft-defender-firewall-on-or-off-ec0844f7-aebd-0583-67fe-601ecf5d774f").

VMWare tools must be uninstalled. For more information, see [Uninstalling and manually installing VMware Tools in VMware Fusion (1014522)](https://kb.vmware.com/s/article/1014522#:~:text=reinstall%20VMware%20Tools.-,Uninstalling%20VMware%20Tools,-To%20uninstall%20VMware "https://kb.vmware.com/s/article/1014522#:~:text=reinstall%20VMware%20Tools.-,Uninstalling%20VMware%20Tools,-To%20uninstall%20VMware").

The disk must be smaller than 80 GB. Reduce the disk size.

Volumes must be MBR partitioned for Windows 10 and GPT partitioned for Windows 11. For more information, see
[Manage disks](https://learn.microsoft.com/en-us/windows-server/storage/disk-management/manage-disks "https://learn.microsoft.com/en-us/windows-server/storage/disk-management/manage-disks").

Install all updates and reboot the operating system.

###### To disable the AutoLogon registry:

1. Press **Windows key** + **R** and type `Regedit.exe` in the command prompt.
2. Scroll down to `HKEY_LOCAL_Machine\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\Winlogon`
3. Add a value for `DontDisplayLastUserName`.
4. For **Type**, enter `REG_SZ`.
5. For **Value**, enter `0`.

###### Note

- The value `DontDisplayLastUserName` determines whether the logon dialog box displays the
  username of the last user that logged onto the PC.
- The value does not exist by default. If it exists, you must set it to `0` or the value of `DefaultUser`
  will be wiped and AutoLogon will fail.
  RealTimeUniversal Registry Key must be enabled. For more information, see
  [Configure time settings for Windows Server 2008 and later](../../../AWSEC2/latest/WindowsGuide/windows-set-time.md#windows-persisting-time-changes-w2k8 "../../../AWSEC2/latest/WindowsGuide/windows-set-time.md#windows-persisting-time-changes-w2k8").

Number of bootable partitions must not exceed one.

###### To remove additional partitions

1. Press the **Windows logo** + **R** keys to open **Run** box. Enter `msconfig` and press the
   **Enter** key on the keyboard to open the System Configuration window.
2. Choose the **Boot** tab from the window and check if the OS you want to use is set to **Current OS; Default OS**.
   If it isn't set, choose your desired OS from the window and choose **Set as default** on the same window.
3. To delete another partition, choose that partition, then select **Delete**, **Apply**, **OK**.

###### If the error still shows up, boot your computer from the installation or repair disc, and follow these steps.

1. Skip the initial languages screen, and then choose **Repair your computer** on the main install screen.
2. On the **Choose an option** screen, choose **Troubleshoot**.
3. On the **Advanced options** screen, choose **Command Prompts**.
4. In the command prompt, enter `bootrec.exe /fixmbr`, then press **Enter**.
   A 64 bit OS image must be used. For more information, see [Windows versions supported for BYOL](byol-windows-images.md#windows_images_supported_versions "byol-windows-images.md#windows_images_supported_versions").

Windows must not have been upgraded from a previous version.

You must uninstall your antivirus software. Run Image Compatibility Checker to get details for the antivirus software to uninstall.

The Legacy BIOS BootMode must be used for Windows 10.For more information, see
[Boot modes](../../../vm-import/latest/userguide/prerequisites.md#vmimport-boot-modes "../../../vm-import/latest/userguide/prerequisites.md#vmimport-boot-modes").

###### To disable the Reserved Storage State

1. Install all Windows updates and reboot the operating system.
2. Make sure there are no new updates.
3. Run either of the following command in Powershell as an administrator.
   - ```
     Set-WindowsReservedStorageState -State Disabled
     ```

   ````
   * ```
   DISM.exe /Online /Set-ReservedStorageState /State:Disabled
   ````

4. Reboot the System.

###### Note

If reserved storage is in use, it might not be disabled, and the following error message is returned:
`This operation is not supported when reserved storage is in use. Please wait for any servicing 
 operations to complete and then try again later.`

The `D:` Drive is a restricted drive letter for WorkSpaces. Please ensure
that `D:` is not being used or will not be mapped to during launch of an instance
from the image.

The image being imported is not supported by the streaming protocol chosen, see
[Create a BYOL image using the WorkSpaces console](windows_images_create_byol_image_console.md "windows_images_create_byol_image_console.md").

Memory Integrity is not supported when Credential Guard is enabled on the Windows operating system of a WorkSpace.
Memory Integrity was detected with UEFILock which cannot be disabled during image import. Please import an image with UEFILock disabled, see
[Disable Credential Guard](https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/configure?tabs=intune#disable-credential-guard "https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/configure?tabs=intune#disable-credential-guard").

To Disable Bitlocker:

1. Open Powershell as an administrator.
2. Run the following command:

```
manage-bde -off  `DriveLetter`:
```

3. Check the status of BitLocker by running the below command:

```
manage-bde -Status  `DriveLetter`:
```

4.  Ensure the values shown match these:

        * **BitLocker Version** – None
        * **Conversion Status** – Fully Decrypted
        * **Percentage Encrypted** – 0.0%
        * **Encryption Method** – None
        * **Protection Status** – Protection Off
        * **Lock Status** – Unlocked

    By default, custom images reach out to "time.windows.com" as the default NTP server. If the NTP server is not reachable, time synchronization issues can occur, causing RDP/Skylight certificate validation failures and SSL connection problems that prevent WorkSpaces creation.

If you encounter time synchronization issues, update the NTP server to use the Amazon Time Sync Service at 169.254.169.123. For more information, see [Configure the time for your Windows instance](../../../AWSEC2/latest/UserGuide/configure-ec2-ntp.md "../../../AWSEC2/latest/UserGuide/configure-ec2-ntp.md").
