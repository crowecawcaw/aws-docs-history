# Update the WorkSpaces Applications Enterprise Deployment Tool, Client, and USB Driver Manually

By default, the WorkSpaces Applications client and USB driver are updated automatically when a new client version is released. However, if you used the Enterprise Deployment Tool to install the WorkSpaces Applications client for your users and you disabled automatic updates, you must update the WorkSpaces Applications Enterprise Deployment Tool, client, and USB driver manually. To do so, perform the following steps to run the required PowerShell commands on users’ computers.

###### Note

To run these commands, you must either be logged in to the applicable computer as
Administrator, or you can run the script remotely under the SYSTEM account on
startup.

Using the Enterprise Deployment Tool to the manage the WorkSpaces Applications macOS client is
not supported.

1. Uninstall the WorkSpaces Applications Enterprise Deployment Tool silently:

```
Start-Process msiexec.exe -Wait -ArgumentList '/x AmazonAppStreamClientSetup_<existing_version>.msi /quiet'
```

2. Uninstall the WorkSpaces Applications USB driver silently:

```
Start-Process -Wait AmazonAppStreamUsbDriverSetup_<existing_version>.exe -ArgumentList '/uninstall /quiet /norestart'
```

3. Uninstall the WorkSpaces Applications client silently:

```
Start-Process "$env:LocalAppData\AppStreamClient\Update.exe" -ArgumentList '--uninstall'
```

###### Note

This process also removes the registry keys that are used to configure the WorkSpaces Applications client. After you reinstall the WorkSpaces Applications client, you must recreate these keys. 4. Clean the application installation directory:

```
Remove-Item -Path $env:LocalAppData\AppStreamClient -Recurse -Confirm:$false –Force
```

5. Restart the computer:

```
Restart-computer
```

6. Install the latest version of the WorkSpaces Applications Enterprise Deployment Tool silently:

```
Start-Process msiexec.exe -Wait -ArgumentList '/i AmazonAppStreamClientSetup_<new_version>.msi /quiet'
```

7. Install the latest version of the WorkSpaces Applications USB driver silently:

```
Start-Process AmazonAppStreamUsbDriverSetup_<new_version>.exe -Wait -ArgumentList '/quiet'
```
