

# Managed deployment configuration
<a name="desktop-enterprise-managed-deployment"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators  | 

Administrators can configure and deploy Amazon Quick on desktop across an enterprise fleet using the following options.

## Managed policies
<a name="desktop-enterprise-mdm-policies"></a>

Amazon Quick reads policies from vendor-neutral OS-managed locations. Any mobile device management (MDM) tool that can deliver a configuration profile (macOS) or registry policy (Windows) works without vendor-specific integration.


**Managed policies for Amazon Quick on desktop**  

| Policy | macOS location | Windows location | Effect | 
| --- | --- | --- | --- | 
| DisableSocialLogin | Preference domain com.aws.QuickWork.mac | HKLM\\SOFTWARE\\Policies\\Amazon\\Quick (REG\_DWORD) | Hides social sign-in, blocks it server-side, and hides "Sign up for free." This policy enforces enterprise SSO as the only authentication path. | 
| DisableAutoUpdates | Preference domain com.aws.QuickWork.mac | HKLM\\SOFTWARE\\Policies\\Amazon\\Quick (REG\_SZ) | Stops the application from updating itself, so that your organization controls when new versions reach the fleet. Accepts patch, minor, or major. The value is the smallest update size that the policy disables. patch disables all automatic updates, including patch, minor, and major updates. minor disables minor and major updates. major disables major updates only. | 

Amazon Quick reads policy values at application startup.

Deploy a configuration profile with preference domain `com.aws.QuickWork.mac`. The profile supports device scope (`/Library/Managed Preferences/com.aws.QuickWork.mac.plist`) or user scope.

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>DisableSocialLogin</key>
    <true/>
    <key>DisableAutoUpdates</key>
    <string>major</string>
</dict>
</plist>
```

Set the registry values at `HKLM\SOFTWARE\Policies\Amazon\Quick`. The Policies hive is not user-editable and survives application updates.

The following example shows both policies configured in the registry:

```
HKLM\SOFTWARE\Policies\Amazon\Quick
  DisableSocialLogin  (REG_DWORD)  =  1
  DisableAutoUpdates  (REG_SZ)     =  major
```

For MDM-specific deployment steps, see your provider's documentation:
+ [macOS preference file profiles](https://learn.microsoft.com/en-us/mem/intune/configuration/preference-file-settings-macos) on the Microsoft Intune website
+ [Application & Custom Settings](https://developer.jamf.com/jamf-pro/docs/application-custom-settings) on the Jamf Pro website

## Proxy support
<a name="desktop-enterprise-proxy-support"></a>

Amazon Quick respects the operating system's proxy configuration (system proxy on Windows, Proxy Auto-Configuration on macOS). All application network traffic, including child processes, routes through the configured enterprise proxy automatically. You don't need to configure the proxy separately.

## Application data paths
<a name="desktop-enterprise-data-paths"></a>

The following table lists the application data paths for each operating system.


**Application data paths by operating system**  

| OS | Path | 
| --- | --- | 
| macOS | \~/.quickwork/ | 
| Windows | %USERPROFILE%\\.quickwork\\ | 

This directory contains local user-specific settings and configurations.

## Silent installation and fleet deployment
<a name="desktop-enterprise-silent-install"></a>

To distribute the application silently to a managed fleet with a mobile device management (MDM) solution – including per-machine packaging for Microsoft Intune and other MDM tools, certificate authority trust, and troubleshooting – see [Deploying Amazon Quick on desktop to a managed fleet with MDM](desktop-enterprise-mdm.md).

For a single-user silent installation on Windows, the installer also supports silent mode. This installs Amazon Quick for the current user in `%LOCALAPPDATA%` and creates desktop and Start menu shortcuts.

```
.\Amazon-Quick-Setup.exe /S
```

## Application updates
<a name="desktop-enterprise-updates"></a>

By default, Amazon Quick delivers updates automatically over HTTPS. Updates are code-signed and apply for each user on the next restart. On macOS, updates use Apple notarization. On Windows, updates use Authenticode signing.

To take control of update delivery, set the `DisableAutoUpdates` policy described in [Managed policies](#desktop-enterprise-mdm-policies). When you block updates, you become responsible for delivering new versions to the fleet, using the same tools you use to deploy other managed applications.

Even when you block updates, Amazon Quick can still notify your users of a required update and restrict functionality remotely if a critical issue is found.

**Important**  
We strongly recommend that you continue to allow patch updates. Patch updates deliver security fixes, performance improvements, and bug fixes. To control larger updates while your fleet still receives patches, set `DisableAutoUpdates` to `minor` or `major` instead of `patch`.