

# Client management reference (Windows)
<a name="client-management-reference-windows"></a>

This topic provides reference information for administrators who manage WorkSpaces client application settings on Windows devices. Use these settings to control client behavior across your organization through the Windows registry or Group Policy.

All registry settings described on this page are under the following path unless otherwise noted:

`HKEY_LOCAL_MACHINE\SOFTWARE\Amazon\Amazon WorkSpaces Client`

**Topics**
+ [Managing client automatic updates](#managing-client-automatic-updates)
+ [Proxy server configuration](#proxy-server-configuration)
+ [IPv6 network settings](#ipv6-network-settings-admin)
+ [Hardware acceleration](#hardware-acceleration-admin)
+ [Related topics](#client-management-reference-related-topics)

## Managing client automatic updates
<a name="managing-client-automatic-updates"></a>

The WorkSpaces client application on Windows automatically checks for available updates, and when new versions become available, installs them in the background when the user is not using the client. Once the installation is complete, the user opens the client to begin using the latest version. This provides users with access to the latest features, enhancements, and bug fixes without interrupting their productivity.

Client updates maintain the same installation context as the original installation. If the client was originally installed for all users on the local device, future updates apply to all users. Similarly, if the client was installed for a single user, future updates apply only to that specific user.

### AWS Regions that support client automatic updates
<a name="regions-support-client-automatic-updates"></a>

Client automatic updates are only applied when the WorkSpaces client for Windows is used to connect to WorkSpaces in the following AWS Regions.


| AWS Region | Region code | 
| --- | --- | 
| US East (N. Virginia) | us-east-1 | 
| US West (Oregon) | us-west-2 | 
| Africa (Cape Town) | af-south-1 | 
| Asia Pacific (Mumbai) | ap-south-1 | 
| Asia Pacific (Seoul) | ap-northeast-2 | 
| Asia Pacific (Singapore) | ap-southeast-1 | 
| Asia Pacific (Sydney) | ap-southeast-2 | 
| Asia Pacific (Tokyo) | ap-northeast-1 | 
| Canada (Central) | ca-central-1 | 
| Europe (Frankfurt) | eu-central-1 | 
| Europe (Ireland) | eu-west-1 | 
| Europe (London) | eu-west-2 | 
| Europe (Paris) | eu-west-3 | 
| Israel (Tel Aviv) | il-central-1 | 
| South America (São Paulo) | sa-east-1 | 

In Regions not listed above, the WorkSpaces client for Windows does not update automatically. Users instead see a message when a new version is available and have the option to install it manually.

### Disabling automatic updates
<a name="disabling-automatic-updates"></a>

We encourage you to keep automatic updates enabled so your users always have access to the latest features, security patches, and bug fixes. However, if you need to manage client updates manually, you can disable client automatic updates by using the following registry setting.

Administrator privileges are required on the local device.

Registry path: `HKEY_LOCAL_MACHINE\SOFTWARE\Amazon\Amazon WorkSpaces Client`

Value name: `clientUpgradeDisabled`

Type: REG\_SZ

Value: 1 (disabled) \| 0 or not present (enabled)

**To disable automatic updates using the Registry Editor**

1. On the Windows client device, type **registry editor** in the Windows search box.

1. Right-click on **Registry Editor** and select **Run as administrator**.

1. If prompted for permission, choose **Yes**.

1. Navigate to: `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Amazon\`

1. If it does not already exist, create a new Key called "Amazon WorkSpaces Client".

1. Within this key, create a new String Value named "clientUpgradeDisabled" and set its value to 1.

1. Either restart your computer or do the following to apply the changes:

   1. Open **Task Manager** and go to the **Processes** tab.

   1. Search for one of the following:
      + For an "all users" installation, search for `WorkSpacesService.exe`.
      + For a "single user" installation, search for `WorkSpacesHelper.exe`.

   1. Right-click and select **End process**.

### Deploy via Group Policy
<a name="deploy-disable-updates-group-policy"></a>

For organizations managing multiple Windows devices, this registry setting can be deployed using Group Policy:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Amazon\Amazon WorkSpaces Client\clientUpgradeDisabled
Type: REG_SZ
Value: 1
```

## Proxy server configuration
<a name="proxy-server-configuration"></a>

If your network requires users to use a proxy server to access the internet, you can configure the WorkSpaces client for Windows to use a proxy for HTTPS (port 443) traffic. The WorkSpaces client uses the HTTPS port for updates, registration, and authentication.

### Port requirements and limitations
<a name="proxy-port-requirements"></a>

**Important**  
The desktop streaming connections to the WorkSpace require ports 4172 and 4195 to be enabled, and do not go through the proxy server.
Proxy servers that require authentication with sign-in credentials are not supported.

### Default proxy behavior
<a name="default-proxy-behavior"></a>

By default, the WorkSpaces client for Windows uses the proxy server that's specified in the local device operating system settings. If the user selects another option for the proxy server in the WorkSpaces client, that setting is used for subsequent launches of the client. If a proxy server is specified at both the operating system level and in the WorkSpaces client, the client setting is used.

## IPv6 network settings
<a name="ipv6-network-settings-admin"></a>

The WorkSpaces client for Windows supports connecting to WorkSpaces using IPv4, IPv6, or dual-stack (both IPv4 and IPv6) addresses. By default, IPv4 connections are used for streaming. Administrators can enable IPv6 connections through the Windows registry.

**Note**  
IPv6 connections are supported on the WorkSpaces client for Windows version 5.30.1 or later.

### Enabling IPv6 connections via registry
<a name="enabling-ipv6-via-registry"></a>

Registry path: `HKEY_LOCAL_MACHINE\SOFTWARE\Amazon\Amazon WorkSpaces Client`

Value name: `WSUseDualStackIPv6`

Type: DWORD (32-bit)

Value: 1 (IPv6 preferred) \| 0 (IPv4 only, default)

**To enable IPv6 using the Registry Editor**

1. On the Windows client device, type **registry editor** in the Windows search box.

1. Right-click on **Registry Editor** and select **Run as administrator**.

1. If prompted for permission, choose **Yes**.

1. Navigate to: `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Amazon\Amazon WorkSpaces Client\`

1. Within this key, create a new DWORD (32-bit) Value named `WSUseDualStackIPv6`.
   + Set its value to 1 to enable IPv6 preferred connections.
   + Set its value to 0 to disable IPv6 preferred connections and use IPv4 exclusively.

1. Changes take effect the next time the WorkSpaces client for Windows is launched. Users can modify this setting in the client UI, but it will revert to the registry key value when the client is relaunched.

## Hardware acceleration
<a name="hardware-acceleration-admin"></a>

Hardware acceleration is enabled by default in the WorkSpaces client for Windows.

### Enabling or disabling hardware acceleration
<a name="enabling-disabling-hardware-acceleration"></a>

Administrators can enable or disable hardware acceleration using the following registry key:

Registry path: `HKEY_CURRENT_USER\SOFTWARE\Amazon Web Services. LLC\Amazon WorkSpaces`

Value name: `EnableHwAcc`

Type: REG\_SZ (String Value)

Value: Present = enabled \| Not present = default behavior

To check for the registry key:

```
reg query "HKCU\SOFTWARE\Amazon Web Services. LLC\Amazon WorkSpaces" /v EnableHwAcc
```

To enable hardware acceleration (add the key):

```
reg add "HKCU\SOFTWARE\Amazon Web Services. LLC\Amazon WorkSpaces" /v EnableHwAcc
```

To disable hardware acceleration (delete the key):

```
reg delete "HKCU\SOFTWARE\Amazon Web Services. LLC\Amazon WorkSpaces" /v EnableHwAcc /f
```

This registry setting takes effect after the WorkSpaces client for Windows is closed and restarted.

### Known issues with hardware acceleration
<a name="hardware-acceleration-known-issues"></a>

If hardware acceleration is enabled, the following issues may occur with certain video driver versions:
+ The screen may have flickering black boxes in some places.
+ The screen may not properly update on the WorkSpaces login page, or after logging in. Artifacts may appear on the screen.
+ Mouse clicks might not be lined up with the cursor position on the screen.

If these issues occur, disable hardware acceleration by deleting the `EnableHwAcc` registry key and restarting the client application.

## Related topics
<a name="client-management-reference-related-topics"></a>
+ [How the Client Experience Policy works](control-client-experience.md#client-experience-policy-how)
+ [Connect to WorkSpaces using a client application](connect-client.md)
+ [WorkSpaces Windows client application](https://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-windows-client.html)
+ [End of life policy for WorkSpaces client applications](workspaces-eol.md)