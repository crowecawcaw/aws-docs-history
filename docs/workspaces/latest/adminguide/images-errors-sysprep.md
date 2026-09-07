

# List of SysPrep error messages and error fixes
<a name="images-errors-sysprep"></a><a name="windows-images-errors-sysprep"></a><a name="AppXInstalled"></a>

## The AMI you are importing has AppX packages installed. Remove them and re-import the image.
<a name="AppXInstalled-collapsed"></a>

Modern AppX Packages might still be installed for your users. Remove the AppX package by running the Powershell `cmdlet`, `Remove-AppxPackage`.

**Note**  
During the BYOL import process, offending AppX packages will be cleaned up and Sysprep will be retried. If the image import process continues to fail, it means AppX packages will need to be manually cleaned up.<a name="ReserveStorageInUse"></a>

## The AMI you are importing has reserved storage enabled. Disable it after Windows updates and re-import the image.
<a name="ReserveStorageInUse-collapsed"></a>

**To disable reserved storage**

1. Open the Registry Editor but entering `regedit.exe`.

1. Navigate to the registry key: `HKLM\Software\Microsoft\Windows\CurrentVersion\ReserveManager`.

1. Change the value of the `ShippedWithReserves` parameter from `1` to `0`.

1. Change the value of `ActiveScenario` to `0`.

1. Disable Reserved Storage in Windows using the following command:

   ```
   DISM.exe /Online /Set-ReservedStorageState /State:Disabled
   ```<a name="SysprepAntiVirusInstalled"></a>

## The AMI you are importing has anti-virus or anti-spyware software installed. Remove it and re-import the image.
<a name="SysprepAntiVirusInstalled-collapsed"></a>

You must uninstall your antivirus software. Run the Image Compatibility Checker to get details for the antivirus software to uninstall. For more information, see [(Optional) Validate your image before importing](byol-windows-images.md#windows_images_run_byol_checker_script).<a name="SysprepImportError"></a>

## An unknown error has occurred to the AMI you are importing during AMI SysPrep.
<a name="SysprepImportErrorcollapsed"></a>

SysPrep failure reason couldn't be determined. Contact AWS support at [ https://aws.amazon.com/support](https://aws.amazon.com/support).