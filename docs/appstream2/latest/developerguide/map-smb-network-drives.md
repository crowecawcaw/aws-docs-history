# Map Server Message Block (SMB) Network Drives

You can use any machine that is under the targeted network of the SMBs. If
you prefer to configure the setup through session scripts, you need to first
create a script that gets invoked when user is logged on, as session script is
configured per image.

To map Server Message Block (SMB) network drives, do the following steps.

## Step 1: Ensure services are running

From the Start Menu, open **services.msc** and
make sure the following services are all running:

- DNS Client
- Function Discovery Resource Publication
- SSDP Discovery
- UPnP Device Host

## Step 2: Create a SMB folder

You can create an SMB with File Explorer.

###### To use File Explorer to configure your SMB shared folders

1. Right-click the SMB folder and choose **Properties**,
   **Sharing**.
2. Choose **Advanced Sharing**.
3. For **Advanced Sharing**, check **Share
   this folder**, and then choose **Permissions**.
4. If you want to provide permissions for all your users, leave it as the default setting.

If you want to add specific users, under **Share Permissions**,
choose **Everyone**, **Remove**. Then choose
**Add** and enter the users or groups you want to access the file share.

For each user or group you add, choose **Allow** to assign
**Full Control**, **Change**, or
**Read permissions**. 5. Choose **Apply**, **OK**, **OK**,
**Close**.

## Step 3: Verify that the SMB is accessible in the domain

Open the file explorer from another server that uses the same security group and joins to
the same domain. Access the network share through the provided network path by navigating to
the network path folder. Choose **Properties**, **Sharing**,
**Network Path**.

## Step 4: Enable users to create symbolic links from local/domain Group Policy

Enable creating symbolic links from local/domain Group Policy for your users to ensure the
session script or logon script defined in group policy. This allows you to create a script in Step 5
with user permissions.

###### To enable users to create symbolic links from local/domain Group Policy

1. In the GPO, which will be used to define this policy, choose **Computer Configuration**,
   **Windows Settings**, **Security Settings**,
   **User Rights Assignment**, **Policy**, **Create symbolic links**.
   Then, update the permission for users to include. For more information about creating symbolic links, see
   [Create symbolic links](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/create-symbolic-links "https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/create-symbolic-links").
2. By default, remote-to-remote (for example, a symlink mapping to a network share
   within another similar symlink) and remote-to-local (for example, a symlink mapping to a
   local share within a symlink mapping to a network share) accesses are disabled.
   If symlink mapping is needed, run the commands below:
   - For enabling remote-to-remote access - `fsutil behavior set SymlinkEvaluation R2R:1`
   - For enabling remote-to-local access - `fsutil behavior set SymlinkEvaluation R2L:1`

## Step 5: Create a script that gets invoked when user is logged on

Create a script that gets invoked when user is logged on by either using an WorkSpaces Applications session script or GPO logon script.
If you choose to use the WorkSpaces Applications session script, the session script will only get applied to that specific WorkSpaces Applications image.
If you use the GPO logon script, the GPOs will be applied to the domain / OU, which can be configured to your fleets.
That way you don’t need configure scripts for every image that you own.

###### To use a session script to mount the SMB shared folder under My Files (using Powershell)

1. After you’ve successfully defined user permissions, configure the following example script using user
   context or system context.

The following is the example config.json script that uses user context.

```
"SessionStart": {
    "executables": [
    {
        "context": "system",
        "filename": "",
        "arguments": "",
        "s3LogEnabled": true
    },
    {
        "context": "user",
        "filename": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
        "arguments": "-File \"C:\\AppStream\\SessionScripts\\userStart.ps1\"",
        "s3LogEnabled": true
    }
 ],
"waitingTime": 30
```

The following is the example script that uses system context.

```
"SessionStart": {
    "executables": [
    {
        "context": "system",
        "filename": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
        "arguments": "-File \"C:\\AppStream\\SessionScripts\\systemStart.ps1\"",
        "s3LogEnabled": true
    },
    {
        "context": "user",
        "filename": "",
        "arguments": "",
        "s3LogEnabled": true
    }
 ],
"waitingTime": 30
```

2. If you're using multi-session fleets, you can use the system environment variable
   `$env:AppStream_Session_UserName` to navigate to the your user's My Files
   folder. This allows mapping to `Admin` instead of the user name when using
   the system context `$env:USERNAME`.

```
# Define the target application path
$targetPathes = "<SMB-PATH>"

# Define the shortcut location
$symlinkLocation = "C:\Users\$Env:AppStream_Session_UserName\My Files\Custom Folder"

# Create the junction for Custom Home Folder under MyFiles
New-Item -ItemType SymbolicLink -Path $symlinkLocation -Target $targetPaths
```

1. Mount SMB shared folders by creating a symbolic fink to a file or folder. For more
   information, see [Example 7: Create a symbolic link to a file or folder](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell. management/new-item?view=powershell-7.4#example-7-create-a-symbolic-link-to-a-file-or-folder "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell. management/new-item?view=powershell-7.4#example-7-create-a-symbolic-link-to-a-file-or-folder")
2. [Assign user logon scripts.](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server- 2012-r2-and-2012/dn789196(v=ws.11)#how-to-assign-user-logon-scripts "https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server- 2012-r2-and-2012/dn789196(v=ws.11)#how-to-assign-user-logon-scripts")
3. Add the following script to create a junction for Custom Home Folders, under My Files.

```
# Define the target application path
$targetPathes = "<SMB-PATH>"

# Define the shortcut location
$symlinkLocation = "C:\Users\$env:Username\My Files\Custom Folder"

# Create the junction for Custom Home Folder under MyFiles
New-Item -ItemType SymbolicLink -Path $symlinkLocation -Target $targetPaths
```

If you are using Windows Server 2022 images, you might experience an issue where your
My Files folder doesn't get created until the Logon Script is completed successfully. This might
can cause a timeout when your SMB mounting operation is done through Logon Script. To resolve this
issue, while also mounting your SMB, trigger an independent process (`Start-Process`)
using your Logon Script by doing the following:

    1. Create a Logon Script.



    ```
    # Define the log file path
    $logFilePath = "<This-is-where-your-log-files-are-saved>"

    # Function to write log messages
    function Write-Log {
        param (
            [string]$message
        )
        $timestamp = get-date -format "yyyy-MM-dd HH:mm:ss"
        $logMessage = "$timestamp - $message"
        $logMessage | Out-File -FilePath $logFilePath -Append -Encoding UTF8
    }

    try {
        Write-Log "Setting execution policy..."
        Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
        Write-Log "Unblocking logon script file..."
        $filePath = "<This-is-where-your-actual-logon-script-is-linked>"
        Unblock-File -Path $filePath
        Write-Log "Running actual logon script..."
        Start-Process -FilePath 'Powershell.exe' -ArgumentList "-File `"$filePath`""
    } catch {
        Write-Log "An error occurred: $_" "ERROR"
    }
    ```
    2. Update this Logon Script delay configuration using Group Policy, if needed. For more information,
     see [Configure Logon Script Delay](https://admx.help/?Category=Windows_8.1_2012R2&Policy=Microsoft.Policies.GroupPolicy::LogonScriptDelay "https://admx.help/?Category=Windows_8.1_2012R2&Policy=Microsoft.Policies.GroupPolicy::LogonScriptDelay"). Logon Script delay will be the amount for time it will delay
     before triggering your async Logon Script. The default delay is 5 minutes.
    3. Restart your fleet to apply the Logon Script delay.
