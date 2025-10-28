# List of SysPrep error messages and error fixes

Modern AppX Packages might still be installed for your users. Remove the AppX package by running the
Powershell `cmdlet`, `Remove-AppxPackage`.

###### Note

During the BYOL import process, offending AppX packages will be cleaned up and Sysprep
will be retried. If the image import process continues to fail, it means AppX packages will
need to be manually cleaned up.

###### To disable reserved storage

1. Open the Registry Editor but entering `regedit.exe`.
2. Navigate to the registry key: `HKLM\Software\Microsoft\Windows\CurrentVersion\ReserveManager`.
3. Change the value of the `ShippedWithReserves` parameter from `1` to `0`.
4. Change the value of `ActiveScenario` to `0`.
5. Disable Reserved Storage in Windows using the following command:

```
DISM.exe /Online /Set-ReservedStorageState /State:Disabled
```

You must uninstall your antivirus software. Run the Image Compatibility Checker to get details for the antivirus software to uninstall.
For more information, see [(Optional) Validate your image before importing](byol-windows-images.md#windows_images_run_byol_checker_script "byol-windows-images.md#windows_images_run_byol_checker_script").

SysPrep failure reason couldn't be determined. Contact AWS support at [https://aws.amazon.com/support](https://aws.amazon.com/support "https://aws.amazon.com/support").
