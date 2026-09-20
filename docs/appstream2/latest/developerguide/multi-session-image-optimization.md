

# Multi-session image optimization
<a name="multi-session-image-optimization"></a>

This section describes Windows image optimizations that reduce CPU and memory usage on WorkSpaces Applications multi-session fleets. These optimizations let you support more concurrent sessions per instance at the same performance level.

## Before you begin
<a name="multi-session-image-optimization-before-you-begin"></a>
+ *If you are using Image Builder*: Launch an Image Builder session from the WorkSpaces Applications console and connect to it. All steps in Part 1 are performed inside this session.
+ *If you are importing an existing image*: Launch a new Image Builder session based on your imported image first, then follow the steps in Part 1. Do not apply optimizations directly to a fleet instance.

## Part 1: Image-level optimizations
<a name="multi-session-image-optimization-part1"></a>

These steps are performed once inside an Image Builder session and baked into your image.

1. *Step 1: Download the Windows Desktop Optimization Tool (WDOT)*. Inside the Image Builder session, open a browser and see the [Windows Desktop Optimization Tool](https://github.com/The-Virtual-Desktop-Team/Windows-Desktop-Optimization-Tool) repository on the GitHub website. Choose **Code**, choose **Download ZIP**, and extract it to a local folder, for example `C:\WDOT`. Alternatively, if Git is available, run the following command.

   ```
   git clone https://github.com/The-Virtual-Desktop-Team/Windows-Desktop-Optimization-Tool.git C:\WDOT\Windows-Desktop-Optimization-Tool-main
   ```

1. *Step 2: Open an elevated PowerShell session*. Choose **Start**, search for **PowerShell**, right-click **Windows PowerShell**, and then choose **Run as administrator**. Navigate to the WDOT folder and allow the scripts to run for the current session.

   ```
   cd C:\WDOT\Windows-Desktop-Optimization-Tool-main
   Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
   ```

1. *Step 3: Create and customize a configuration profile*.

   ```
   # Create a configuration profile
   .\New-WVDConfigurationFiles.ps1 -FolderName "WorkSpaces-Production"
   
   # Apply all recommended settings for each optimization category
   .\Set-WVDConfigurations.ps1 -ConfigurationFile "Services" -ConfigFolderName "WorkSpaces-Production" -ApplyAll
   .\Set-WVDConfigurations.ps1 -ConfigurationFile "ScheduledTasks" -ConfigFolderName "WorkSpaces-Production" -ApplyAll
   .\Set-WVDConfigurations.ps1 -ConfigurationFile "AppxPackages" -ConfigFolderName "WorkSpaces-Production" -ApplyAll
   ```
**Note**  
Review the generated JSON files under `C:\WDOT\Configurations\WorkSpaces-Production\` before proceeding. Set any item to `Skip` if it conflicts with your applications.

1. *Step 4: Apply optimizations*.

   ```
   .\Windows_Optimization.ps1 -ConfigProfile "WorkSpaces-Production" -Optimizations @("Services", "ScheduledTasks", "AppxPackages") -AcceptEULA
   ```

   This does the following:
   + Disables unnecessary Windows services.
   + Disables scheduled tasks that run in the background.
   + Removes unused AppX packages.
**Important**  
If you are optimizing AppX packages, ensure the AppX service is not in a STOPPED state before creating your image. Always test in a non-production environment first to verify application compatibility.

1. *Step 5: Create your image*. Once optimizations are applied, proceed with your normal image creation process from the WorkSpaces Applications console.

## Part 2: User session optimizations
<a name="multi-session-image-optimization-part2"></a>

These optimizations apply per-user registry settings (HKCU). They must run after a user logs on, and they cannot be baked into the image directly. There are two ways to apply them.

### Option A: Session scripts (recommended)
<a name="multi-session-image-optimization-part2-session-scripts"></a>

WorkSpaces Applications session scripts allow you to automatically run a script in the user's context at session start. This is the recommended approach because it requires no user action.

1. *Step 1: Save the optimization script to your image*. Inside your Image Builder session, create the folder and save the script.

   ```
   New-Item -ItemType Directory -Path "C:\Scripts" -Force
   ```

   Save the PowerShell script shown in Step 3 as `C:\Scripts\UserOptimizations.ps1`.

1. *Step 2: Configure the session scripts configuration file*. The session scripts configuration file is located at `C:\AppStream\SessionScripts\config.json` and is present by default on the image. Update it with the following content.

   ```
   {
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
           "arguments": "-ExecutionPolicy Bypass -File C:\\Scripts\\UserOptimizations.ps1",
           "s3LogEnabled": true
         }
       ],
       "waitingTime": 30
     },
     "SessionTermination": {
       "executables": [
         {
           "context": "system",
           "filename": "",
           "arguments": "",
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
     }
   }
   ```

   For full session scripts documentation, see [Use Session Scripts on Multi-Session Fleets](session-scripts-multi-session-fleets.md).

1. *Step 3: Review the optimization script*, saved as `C:\Scripts\UserOptimizations.ps1`.

   ```
   # -----------------------------------------------
   # WorkSpaces Application User Session Optimization Script
   # Run as: User context, at session start
   # -----------------------------------------------
   
   # 1. Disable DWM visual effects
   # Disabling transparency, animations, and blur reduces DWM compositing work —
   # the single largest CPU and memory optimization in multi-session environments.
   $visualFxPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects"
   If (!(Test-Path $visualFxPath)) { New-Item -Path $visualFxPath -Force | Out-Null }
   Set-ItemProperty -Path $visualFxPath -Name VisualFXSetting -Value 2 -Type DWord
   
   $desktopPath = "HKCU:\Control Panel\Desktop"
   Set-ItemProperty -Path $desktopPath -Name UserPreferencesMask -Value ([byte[]](0x90,0x12,0x03,0x80,0x10,0x00,0x00,0x00)) -Type Binary
   
   # Apply visual effects changes immediately without disrupting the session
   rundll32.exe user32.dll, UpdatePerUserSystemParameters
   
   # 2. Disable Search UI web background extensions
   $searchGlobal = "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Search"
   If (!(Test-Path $searchGlobal)) { New-Item -Path $searchGlobal -Force | Out-Null }
   Set-ItemProperty -Path $searchGlobal -Name BingSearchEnabled -Value 0 -Type DWord
   Set-ItemProperty -Path $searchGlobal -Name CortanaConsent -Value 0 -Type DWord
   
   # 3. Restrict background apps
   $backgroundPath = "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications"
   If (!(Test-Path $backgroundPath)) { New-Item -Path $backgroundPath -Force | Out-Null }
   Set-ItemProperty -Path $backgroundPath -Name GlobalUserDisabled -Value 1 -Type DWord
   
   $privacyPath = "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Privacy"
   If (!(Test-Path $privacyPath)) { New-Item -Path $privacyPath -Force | Out-Null }
   Set-ItemProperty -Path $privacyPath -Name LetAppsRunInBackground -Value 2 -Type DWord
   
   # 4. Disable News & Interests (Taskbar widgets)
   $feedPath = "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Feeds"
   If (!(Test-Path $feedPath)) { New-Item -Path $feedPath -Force | Out-Null }
   Set-ItemProperty -Path $feedPath -Name ShellFeedsTaskbarViewMode -Value 2 -Type DWord
   
   # 5. Disable Tips & Suggestions
   $contentPath = "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager"
   If (!(Test-Path $contentPath)) { New-Item -Path $contentPath -Force | Out-Null }
   Set-ItemProperty -Path $contentPath -Name "SubscribedContent-338389Enabled" -Value 0 -Type DWord
   Set-ItemProperty -Path $contentPath -Name SoftLandingEnabled -Value 0 -Type DWord
   ```

### Option B: Default user profile (no session scripts required)
<a name="multi-session-image-optimization-part2-default-profile"></a>

If you prefer not to use session scripts, you can apply these settings to the Windows default user profile during image creation. Any new user logging in to the instance inherits these settings automatically. In your elevated PowerShell session on the Image Builder, run the following commands.

```
# Load the default user hive
reg load "HKU\DefaultUser" "C:\Users\Default\NTUSER.DAT"

# DWM visual effects
reg add "HKU\DefaultUser\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects" /v VisualFXSetting /t REG_DWORD /d 2 /f
reg add "HKU\DefaultUser\Control Panel\Desktop" /v UserPreferencesMask /t REG_BINARY /d 9012038010000000 /f

# Search UI web background extensions
reg add "HKU\DefaultUser\SOFTWARE\Microsoft\Windows\CurrentVersion\Search" /v BingSearchEnabled /t REG_DWORD /d 0 /f
reg add "HKU\DefaultUser\SOFTWARE\Microsoft\Windows\CurrentVersion\Search" /v CortanaConsent /t REG_DWORD /d 0 /f

# Background apps
reg add "HKU\DefaultUser\SOFTWARE\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications" /v GlobalUserDisabled /t REG_DWORD /d 1 /f
reg add "HKU\DefaultUser\SOFTWARE\Microsoft\Windows\CurrentVersion\Privacy" /v LetAppsRunInBackground /t REG_DWORD /d 2 /f

# News & Interests
reg add "HKU\DefaultUser\SOFTWARE\Microsoft\Windows\CurrentVersion\Feeds" /v ShellFeedsTaskbarViewMode /t REG_DWORD /d 2 /f

# Tips & Suggestions
reg add "HKU\DefaultUser\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v "SubscribedContent-338389Enabled" /t REG_DWORD /d 0 /f
reg add "HKU\DefaultUser\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v SoftLandingEnabled /t REG_DWORD /d 0 /f

# Unload the hive
reg unload "HKU\DefaultUser"
```

**Note**  
Always unload the hive with `reg unload` before creating your image. Leaving it loaded will cause issues with the image.

## Part 3: Antivirus configuration
<a name="multi-session-image-optimization-part3"></a>

If you run antivirus software on your fleet instances, improper configuration can significantly reduce multi-session performance. Antivirus scans running concurrently across many sessions compound CPU and I/O overhead rapidly.

Follow the guidance in [Antivirus Software](windows-update-antivirus-software.md#windows-update-antivirus-software-av) to ensure your antivirus is correctly configured for multi-session environments. Key practices include the following:
+ Exclude WorkSpaces Applications process paths and user session directories from real-time scanning.
+ Schedule full scans outside of active session hours.
+ Use a VDI-optimized antivirus agent where available.