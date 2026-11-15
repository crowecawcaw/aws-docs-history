

# Managed deployment configuration
<a name="desktop-enterprise-managed-deployment"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators  | 

Administrators can configure and deploy AWS Quick on desktop across an enterprise fleet using the following options.

## Managed policies
<a name="desktop-enterprise-mdm-policies"></a>

AWS Quick reads policies from vendor-neutral OS-managed locations. Any mobile device management (MDM) tool that can deliver a configuration profile (macOS) or registry policy (Windows) works without vendor-specific integration.


**Managed policies for AWS Quick on desktop**  

| Policy | macOS location | Windows location | Effect | 
| --- | --- | --- | --- | 
| DisableSocialLogin | Preference domain com.aws.QuickWork.mac | HKLM\\SOFTWARE\\Policies\\Amazon\\Quick (REG\_DWORD) | Hides social sign-in, blocks it server-side, and hides "Sign up for free." This policy enforces enterprise SSO as the only authentication path. | 
| DisableAutoUpdates | Preference domain com.aws.QuickWork.mac | HKLM\\SOFTWARE\\Policies\\Amazon\\Quick (REG\_SZ) | Stops the application from updating itself, so that your organization controls when new versions reach the fleet. Accepts patch, minor, or major. The value is the smallest update size that the policy disables. patch disables all automatic updates, including patch, minor, and major updates. minor disables minor and major updates. major disables major updates only. | 

AWS Quick reads policy values at application startup.

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

AWS Quick uses the operating system's proxy configuration (system proxy on Windows, Proxy Auto-Configuration (PAC) on macOS) for the connections that the application opens on the device. Some components don't use this routing. Local MCP servers and coding agents use their own network settings, and local browser automation uses the browser or operating system proxy configuration.

If the application can't retrieve or evaluate a PAC file, or proxy routing fails to start, the application connects directly. To require that all device traffic passes through your proxy, enforce it at the network layer, for example with outbound firewall rules that allow traffic only through the proxy.

Requests that run in the AWS Quick agent runtime, such as web search (including fetch URL), file download, remote managed browser automation, and cloud connector calls, don't originate from the device and don't pass through your proxy. For more information, see [Network connections](desktop-security.md#desktop-architecture-network).

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

To distribute the application silently to a managed fleet with a mobile device management (MDM) solution – including per-machine packaging for Microsoft Intune and other MDM tools, certificate authority trust, and troubleshooting – see [Deploying AWS Quick on desktop to a managed fleet with MDM](desktop-enterprise-mdm.md).

For a single-user silent installation on Windows, the installer also supports silent mode. This installs AWS Quick for the current user in `%LOCALAPPDATA%` and creates desktop and Start menu shortcuts.

```
.\Amazon-Quick-Setup.exe /S
```

## Application updates
<a name="desktop-enterprise-updates"></a>

By default, AWS Quick delivers updates automatically over HTTPS. Updates are code-signed and apply for each user on the next restart. On macOS, updates use Apple notarization. On Windows, updates use Authenticode signing.

To take control of update delivery, set the `DisableAutoUpdates` policy described in [Managed policies](#desktop-enterprise-mdm-policies). When you block updates, you become responsible for delivering new versions to the fleet, using the same tools you use to deploy other managed applications.

Even when you block updates, AWS Quick can still notify your users of a required update and restrict functionality remotely if a critical issue is found.

**Important**  
We strongly recommend that you continue to allow patch updates. Patch updates deliver security fixes, performance improvements, and bug fixes. To control larger updates while your fleet still receives patches, set `DisableAutoUpdates` to `minor` or `major` instead of `patch`.