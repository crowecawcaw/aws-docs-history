# Update the WorkSpaces Applications Enterprise Deployment Tool, Client, and USB Driver Manually

By default, the WorkSpaces Applications client and USB driver update automatically when we release a new client version. If you used the Enterprise Deployment Tool to install the WorkSpaces Applications client and disabled automatic updates, you must update the client and USB driver manually. To do so, run the following PowerShell commands on your users' computers.

###### Note

To run these commands, you must either be logged in to the applicable computer as
Administrator, or you can run the script remotely under the SYSTEM account on
startup.

Using the Enterprise Deployment Tool to manage the WorkSpaces Applications macOS client is
not supported.

1. Install the new version of the WorkSpaces Applications client over the existing version:

```
Start-Process msiexec.exe -Wait -ArgumentList '/i AmazonWorkSpacesApplicationsClientSetup_<new_version>.msi ALLUSERS=1 /quiet'
```

###### Note

You don't need to uninstall the previous version or reboot. The new version automatically replaces the previous version. 2. (Optional) Update the WorkSpaces Applications USB driver:

```
Start-Process AmazonAppStreamUsbDriverSetup_<new_version>.exe -Wait -ArgumentList '/quiet'
```

###### Upgrading from versions 1.2.1830 and earlier

If you previously installed the client using the Enterprise Deployment Tool (versions 1.2.1830 and earlier), the new MSI automatically removes the legacy installation during upgrade. No manual uninstall or reboot is required. The install location changes from `C:\Program Files (x86)\Amazon WorkSpaces Applications Client Installer\` to `C:\Program Files\Amazon Web Services, Inc\Amazon WorkSpaces Applications\`. The MSI requires a 64-bit version of Windows.
