# Tutorial: Install the Amazon WorkSpaces Applications Client And Customize the Client Experience for Your Users

The following sections describe how to install the WorkSpaces Applications client and customize the client experience for your users. If you plan to download and install the client for your users, first download the Enterprise
Deployment Tool. You can then run PowerShell scripts to install the WorkSpaces Applications client and configure client settings remotely.

###### Note

Using the Enterprise Deployment Tool with the WorkSpaces Applications macOS client is not
supported.

###### Contents

- [Download the Enterprise Deployment Tool](#install-client-use-remote-deployment-tool "#install-client-use-remote-deployment-tool")
- [Install the
  WorkSpaces Applications Client and USB Driver](#run-powershell-script-install-client-usb-driver-silently "#run-powershell-script-install-client-usb-driver-silently")
- [Accessing WorkSpaces Applications with the WorkSpaces Applications Client](#access-appstream-with-client "#access-appstream-with-client")
- [Set the StartURL Registry Value for WorkSpaces Applications Client Users](#set-start-url-registry-value "#set-start-url-registry-value")
- [Set the TrustedDomains Registry Value to Enable Other Domains for the WorkSpaces Applications Client](#set-trusted-domains-registry-value "#set-trusted-domains-registry-value")
- [Create the AS2TrustedDomains DNS TXT Record to Enable Your Domain for the WorkSpaces Applications Client Without Registry Changes](#create-AS2TrustedDomains-DNS-TXT-record-client "#create-AS2TrustedDomains-DNS-TXT-record-client")
- [Disable DNS TXT Record Lookup for Trusted Domains](#disable-DNS-TXT-record-lookup-client "#disable-DNS-TXT-record-lookup-client")
- [Choose Whether to Disable Automatic Client Updates](#disable-automatic-updates-client "#disable-automatic-updates-client")
- [Choose Whether to Disable On-Demand Diagnostic Log Uploads](#disable-on-demand-diagnostic-log-uploads "#disable-on-demand-diagnostic-log-uploads")
- [Choose Whether to Disable Native Application Mode](#disable-native-application-mode-client "#disable-native-application-mode-client")
- [Choose Whether to Disable Local Printer Redirection](#disable-local-printer-redirection-client "#disable-local-printer-redirection-client")
- [Choose Whether to Disable Smart Card Redirection](#disable-local-smart-card-support-client "#disable-local-smart-card-support-client")
- [Configure Additional WorkSpaces Applications Client Settings for Your Users](#configure-client "#configure-client")
- [Using Group Policy to Customize WorkSpaces Applications Client Experience](#configure-client-with-adm-template-group-policy "#configure-client-with-adm-template-group-policy")

## Download the Enterprise Deployment Tool

The Enterprise Deployment Tool includes the WorkSpaces Applications client
installation files and a Group Policy administrative template.

1. To download the Enterprise Deployment Tool, on the bottom right of the [WorkSpaces Applications supported clients](https://clients.amazonappstream.com "https://clients.amazonappstream.com") page, select the
   **Enterprise Deployment Tool** link. This link
   opens a .zip file that contains the required files for the latest
   version of the tool.
2. To extract the required files, navigate to the location where you downloaded the tool, right-click the
   **AmazonAppStreamClient_EnterpriseSetup\_<version>**
   folder, and choose **Extract All**. The folder contains
   two installation programs and a Group Policy administrative
   template:
   - WorkSpaces Applications client installer (AmazonAppStreamClientSetup\_<version>.msi) — Installs the
     WorkSpaces Applications client.
   - WorkSpaces Applications USB driver installer (AmazonAppStreamUsbDriverSetup\_<version>.exe) — Installs the WorkSpaces Applications USB driver that is required to use USB devices with applications streamed through WorkSpaces Applications.
   - WorkSpaces Applications client Group Policy administrative template (as2_client_config.adm) — Lets you configure the WorkSpaces Applications client through Group Policy.

## Install the

WorkSpaces Applications Client and USB Driver

After you download the WorkSpaces Applications client installation files, run the following
PowerShell script on users' computers to install the WorkSpaces Applications client installation file, AppStreamClient.exe, and the USB
driver silently.

###### Note

To run this script, you must be logged in to the applicable computer with Administrator
permissions. You can also run the script remotely under the System account
on startup.

```
Start-Process msiexec.exe -Wait -ArgumentList  '/i AmazonAppStreamClientSetup_<version>.msi /quiet'

Start-Process AmazonAppStreamUsbDriverSetup_<version>.exe -Wait -ArgumentList  '/quiet'
```

After you install the Enterprise Deployment Tool on a user's computer, the WorkSpaces Applications client is installed as follows:

1. The WorkSpaces Applications client installation file is copied to the following path on the user's computer: C:\Program Files (x86)\Amazon WorkSpaces Applications Client Installer\AppStreamClient.exe.
2. The first time the user logs on to their computer after the Enterprise Deployment Tool is installed, the WorkSpaces Applications client is installed.

###### Note

If the Enterprise Deployment Tool detects that the WorkSpaces Applications Client folder, **AppStreamClient**, already exists in **%localappdata%**, the tool does not install the client.

If a user uninstalls the WorkSpaces Applications client, the client isn’t installed again until you
update the WorkSpaces Applications Enterprise Deployment Tool.

## Accessing WorkSpaces Applications with the WorkSpaces Applications Client

By default, when users launch the WorkSpaces Applications client, they can connect only to URLs that
include the WorkSpaces Applications domain or domains that include a DNS TXT record that enables the
connection. You can let client users access domains other than the WorkSpaces Applications domain by doing any of the following:

- Set the `StartURL` registry value to specify a custom URL that users can access, such as the URL for your organization's login portal.
- Set the `TrustedDomains` registry value to specify trusted domains that users can access.
- Create the `AS2TrustedDomains` DNS TXT record to specify trusted domains that users can access. This method lets you avoid registry changes.

###### Note

The WorkSpaces Applications client and DNS TXT record configuration do not prevent users from using other connection methods to access the domains or URLs
that you specify. For example, users can access specified
domains or URLs by using a web browser, if they have
network access to the domains or URLs.

## Set the StartURL Registry Value for WorkSpaces Applications Client Users

You can use the `StartUrl` registry value to set a custom
URL that is populated in the WorkSpaces Applications client when a user launches the client. You
can create this HKLM registry key while installing the client so that your users
don’t need to specify a URL when they launch the client.

After the WorkSpaces Applications client is installed, you can run the following PowerShell script
to create this registry key, or you can use the administrative template that is
included in the WorkSpaces Applications client Enterprise Deployment Tool to configure the client
through Group Policy.

Replace the `StartUrl` value with a URL for your
identity provider (IdP). The URL must use a certificate that is trusted by the
device. This means that the certificate that is used by the
`StartUrl` webpage must contain a Subject Alternative
Name (SAN) that includes the URL's domain name. For example, if your
`StartUrl` is set to https://appstream.example.com, the
SSL certificate must have a SAN that includes appstream.example.com.

###### Note

To run this script, you must be logged in to the applicable computer with Administrator
permissions. You can also run the script remotely under the System account
on startup.

```
$registryPath="HKLM:\Software\Amazon\AppStream Client"
New-Item -Path "HKLM:\Software\Amazon" -Name "AppStream Client" -Force

New-ItemProperty -Path $registryPath -Name "StartUrl" -Value "https://www.example.com" -PropertyType String -Force | Out-Null
```

## Set the TrustedDomains Registry Value to Enable Other Domains for the WorkSpaces Applications Client

You can configure the WorkSpaces Applications client to connect to URLs in trusted domains that you
specify. For example, you might want to let users connect to any URL in your
organizational domain or to any URL in one or more of your IdP domains. When you
specify the URL, use the following format:
\*.`example`-`idp`.`com`.

You can specify a list of trusted domains in a
comma-separated format. Add this list as a registry value to the
WorkSpaces Applications `TrustedDomains` HKLM registry key. We recommend that you create this registry key and specify the list of trusted domains when you install the WorkSpaces Applications client or, if you are using Microsoft Active Directory, through Group Policy. That way, your users can connect
to a URL in any trusted domain immediately after the client is installed.

After the WorkSpaces Applications client is installed, you can run the following PowerShell script
to create this registry key. Or, you can use the administrative template that is
included in the WorkSpaces Applications client Enterprise Deployment Tool to configure the client
through Group Policy.

Replace the `TrustedDomains` value with a
comma-separated list for one or more of your organizational or IdP domains. The
certificate used by the trusted domain webpage must contain a SAN that includes
the URL's domain. For example, if your trusted domain includes \*.example.com,
and users specify https://appstream.example.com, the SSL certificate must have a
SAN that includes appstream.example.com.

###### Note

To run this script, you must be logged in to the applicable computer with Administrator
permissions. You can also run the script remotely under the System account
on startup.

```
$registryPath="HKLM:\Software\Amazon\AppStream Client"
New-Item -Path "HKLM:\Software\Amazon" -Name "AppStream Client" -Force

New-ItemProperty -Path $registryPath -Name "TrustedDomains" -Value "*.example1.com, *.example2.com, aws.amazon.com" -PropertyType String -Force | Out-Null
```

The following are requirements and considerations for formatting trusted domain names.

- The following characters are supported: a-z, 0-9, -, \*
- DNS treats the \* character either as a wildcard or as an asterisk character (ASCII 42), depending on where it appears in the domain name. Following are restrictions when using \* as a wildcard in the name of a DNS record:
  - The \* must replace the leftmost label in a domain name. For example, \*.example.com or \*.prod.example.com. If you include \* in any other position, such as prod.\*.example.com, DNS treats it as an asterisk character (ASCII 42), not as a wildcard.
  - The \* must replace the entire label. For example, you can't specify \*prod.example.com or prod\*.example.com.
  - The \* applies to the subdomain level that includes the \*, and to all the subdomains of that subdomain. For example, if an entry is named \*.example.com, the WorkSpaces Applications client allows zenith.example.com, acme.zenith.example.com, and pinnacle.acme.zenith.example.com.

## Create the AS2TrustedDomains DNS TXT Record to Enable Your Domain for the WorkSpaces Applications Client Without Registry Changes

You can enable users to connect to any URL in your organizational domain (for
example, \*.example.com) or to any URL in your IdP domains (for example,
\*.example-idp.com) by creating a DNS TXT record in that domain. When you create
the DNS TXT record, the `StartURL` or
`TrustedDomains` registry values are not required to
allow a user to connect to a URL.

You can specify a list of trusted subdomains
in a comma-separated format, prefixed with
`AS2TrustedDomains=`. Then, create a DNS TXT record for
the appropriate domain. The `AS2TrustedDomains` DNS TXT
record can only enable the same domain, or subdomains, of the domain in which the
DNS TXT record is created. You cannot use the DNS TXT record to enable other domains.

For more information about setting up the DNS record, see [Enable your organizational domain for the AppStream 2.0 client with a Route
53 DNS TXT record](https://aws.amazon.com/blogs/desktop-and-application-streaming/enable-your-organizational-domain-for-the-appstream-2-0-client-with-a-route-53-dns-txt-record/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/enable-your-organizational-domain-for-the-appstream-2-0-client-with-a-route-53-dns-txt-record/") and [Creating an AS2TrustedDomains DNS TXT record to redirect the AppStream 2.0
native client to a third-party identity provider](https://aws.amazon.com/blogs/desktop-and-application-streaming/creating-an-as2trusteddomains-dns-txt-record-to-redirect-the-appstream-2-0-native-client-to-a-third-party-identity-provider/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/creating-an-as2trusteddomains-dns-txt-record-to-redirect-the-appstream-2-0-native-client-to-a-third-party-identity-provider/").

###### Note

When you create DNS TXT records, any users can stream from enabled domains that are not
included in the `StartURL` or
`TrustedDomains` registry values. The WorkSpaces Applications client
and DNS TXT record configuration do not prevent users from using other
connection methods to access the domains or URLs that you specify. For
example, users can access specified domains or URLs by using a web browser,
if they have network access to the domains or URLs.

### DNS TXT Record Configuration Example

The following is an example of a DNS TXT record configuration. With the configuration for this example, users can launch the WorkSpaces Applications client and connect to appstream.example.com or appstream-dev.example.com. However, they cannot connect to example.com.

- `Domains to enable` — appstream.example.com, appstream-dev.example.com
- `DNS TXT record location` — example.com
- `DNS TXT record value` — AS2TrustedDomains=appstream.example.com,appstream-dev.example.com

### Requirements and Considerations

Keep in mind the following requirements and considerations for creating a DNS TXT record:

- You must create the TXT record at the second-level domain. For example, if your domain is prod.appstream.example.com, you must create the DNS TXT record at example.com.
- The TXT record value must start with `AS2TrustedDomains=`
- The following characters are supported: a-z, 0-9, -, \*
- DNS treats the \* character either as a wildcard or as an asterisk character (ASCII 42), depending on where it appears in the domain name. Following are restrictions when using \* as a wildcard in the name of a DNS record:
  - The \* must replace the leftmost label in a domain name. For example, \*.example.com or \*.prod.example.com. If you include \* in any other position, such as prod.\*.example.com, DNS treats it as an asterisk character (ASCII 42), not as a wildcard.
  - The \* must replace the entire label. For example, you can't specify \*prod.example.com or prod\*.example.com.
  - The \* applies to the subdomain level that includes the \*, and to all the subdomains of that subdomain. For example, if an entry is named \*.example.com, the WorkSpaces Applications client allows connections to the following domains: zenith.example.com, acme.zenith.example.com, and pinnacle.acme.zenith.example.com.

## Disable DNS TXT Record Lookup for Trusted Domains

By default, when users launch the WorkSpaces Applications and specify a URL that is not an WorkSpaces Applications domain, the client performs a DNS TXT record lookup. The lookup is performed on the second-level domain of the URL so that the client can determine whether the domain is included in the `AS2TrustedDomains` list. This behavior lets users connect to domains that are not specified in the `StartURL` or `TrustedDomains` registry keys, or WorkSpaces Applications domains.

You can disable this behavior by setting the value for the
`DnsTxtRecordQueryDisabled` registry key to `true`.
You can create this registry key when you install the WorkSpaces Applications client. That way,
the client connects only to URLs that are specified by the `StartURL`
or `TrustedDomains` registry keys.

After the WorkSpaces Applications client is installed, you can run the following PowerShell
script to create this registry key. Or, you can use the administrative template
that is included in the WorkSpaces Applications client Enterprise Deployment Tool to configure
the client through Group Policy.

###### Note

To run this script, you must be logged in to the applicable computer with Administrator
permissions. You can also run the script remotely under the System account
on startup.

```
$registryPath="HKLM:\Software\Amazon\AppStream Client"
New-Item -Path "HKLM:\Software\Amazon" -Name "AppStream Client" -Force

New-ItemProperty -Path $registryPath -Name "DnsTxtRecordQueryDisabled" -Value "true" -PropertyType String -Force | Out-Null
```

## Choose Whether to Disable Automatic Client Updates

By default, when a new version of the WorkSpaces Applications client is available, the client
updates automatically to the latest version. You can disable automatic
updates by setting the value for the `AutoUpdateDisabled`
registry key to `true`. You can create this
registry key when you install the WorkSpaces Applications client. That way, the client is not
updated automatically whenever a new version is available.

After the WorkSpaces Applications client is installed, you can run the following PowerShell script
to create this registry key. Or, you can use the administrative template that is
included in the WorkSpaces Applications client Enterprise Deployment Tool to configure the client
through Group Policy.

###### Note

To run this script, you must be logged in to the applicable computer with Administrator
permissions. You can also run the script remotely under the System account
on startup.

```
$registryPath="HKLM:\Software\Amazon\AppStream Client"
New-Item -Path "HKLM:\Software\Amazon" -Name "AppStream Client" -Force

New-ItemProperty -Path $registryPath -Name "AutoUpdateDisabled" -Value "True" -PropertyType String -Force | Out-Null
```

## Choose Whether to Disable On-Demand Diagnostic Log Uploads

By default, the WorkSpaces Applications client allows users to upload diagnostic logs and minidumps on demand to WorkSpaces Applications (AWS). In addition, if an exception
occurs or the WorkSpaces Applications client stops responding, users are prompted to choose
whether they want to upload the minidump and associated logs. For more
information about on-demand diagnostic logging, see [Automatic and On-Demand Diagnostic Log
Uploads](feature-support-diagnostic-log-upload.md "feature-support-diagnostic-log-upload.md").

You can disable these behaviors by setting the value for the `UserUploadOfClientLogsAllowed`
registry key to `false`. You can create this HKLM registry key when you
install the WorkSpaces Applications client.

After the WorkSpaces Applications client is installed, you can run the following PowerShell script
to create this registry key. Or, you can use the administrative template that is
included in the WorkSpaces Applications client Enterprise Deployment Tool to configure the client
through Group Policy.

###### Note

To run this script, you must be logged in to the applicable computer with Administrator
permissions. You can also run the script remotely under the System account
on startup.

```
$registryPath="HKLM:\Software\Amazon\AppStream Client"
New-Item -Path "HKLM:\Software\Amazon" -Name "AppStream Client" -Force

New-ItemProperty -Path $registryPath -Name "UserUploadOfClientLogsAllowed" -Value "false" -PropertyType String -Force | Out-Null

```

## Choose Whether to Disable Native Application Mode

By default, the WorkSpaces Applications client can run in either classic mode or native application
mode. You can disable native application mode by setting the value for the `NativeAppModeDisabled`
registry key to `true`. You can create this HKLM registry key when you
install the WorkSpaces Applications client. If the value is set to `true`, the client runs
in classic mode only. For information about native application mode, see [Native Application
Mode](feature-support-native-application-mode.md "feature-support-native-application-mode.md").

After the WorkSpaces Applications client is installed, you can run the following PowerShell
script to create this registry key. Or, you can use the administrative template
that is included in the WorkSpaces Applications client Enterprise Deployment Tool to configure
the client through Group Policy.

###### Note

To run this script, you must be logged in to the applicable computer with Administrator
permissions. You can also run the script remotely under the System account
on startup.

```
$registryPath="HKLM:\Software\Amazon\AppStream Client"
New-Item -Path "HKLM:\Software\Amazon" -Name "AppStream Client" -Force

New-ItemProperty -Path $registryPath -Name "NativeAppModeDisabled" -Value "True" -PropertyType String -Force | Out-Null
```

## Choose Whether to Disable Local Printer Redirection

By default, the WorkSpaces Applications client enables users to redirect print jobs from their
streaming applications to a printer that is connected to their local computer.
You can disable local printer redirection by setting the value for the
`PrinterRedirectionDisabled` registry key to `true`.
You can create this HKLM registry key when you install the WorkSpaces Applications client. If the
value is set to `true`, the client does not redirect print jobs from
users’ streaming applications to a printer that is connected to their local
computer.

After
you install the WorkSpaces Applications client, you can run the following
PowerShell script to create this registry key. Or, you can use the administrative template that is included in the WorkSpaces Applications client Enterprise Deployment Tool to configure the client through Group Policy.

###### Note

To run this script, you must be logged in to the applicable computer with Administrator
permissions. You can also run the script remotely under the System account
on startup.

```
$registryPath="HKLM:\Software\Amazon\AppStream Client"
New-Item -Path "HKLM:\Software\Amazon" -Name "AppStream Client" -Force

New-ItemProperty -Path $registryPath -Name "PrinterRedirectionDisabled" -Value "True" -PropertyType String -Force | Out-Null
```

## Choose Whether to Disable Smart Card Redirection

By default, smart card redirection is enabled for the WorkSpaces Applications client. When this feature is enabled, users can use smart card readers that are connected to their local computers and their smart cards during WorkSpaces Applications streaming sessions without USB redirection. During WorkSpaces Applications streaming sessions, users' smart card readers and smart cards remain accessible for use with local applications. The client redirects the smart card API calls from users’ streaming applications to their local smart card. You can disable smart card redirection by setting the value for the `SmartCardRedirectionDisabled` registry key to `true`. You can create this HKLM registry key when you install the WorkSpaces Applications client.

If the value is set to `true`, your users can't use their smart
card readers and smart cards during an WorkSpaces Applications streaming session without USB
redirection. In this case, users can't sign in to their streaming applications
by using a smart card that is connected to their local computer unless you [qualify the device](qualify-usb-devices.md "qualify-usb-devices.md"). After you qualify
the device, users must [share the
device with WorkSpaces Applications](client-application-windows-how-to-share-usb-devices-user.md "client-application-windows-how-to-share-usb-devices-user.md"). When smart card redirection is disabled, during
users' WorkSpaces Applications streaming sessions, their smart card readers and smart cards are
not accessible for use with local applications.

After
you install the WorkSpaces Applications client, you can run the following
PowerShell script to create this registry key. Or, you can use the administrative template that is included in the WorkSpaces Applications client Enterprise Deployment Tool to configure the client through Group Policy.

###### Note

To run this script, you must be logged in to the applicable computer with Administrator
permissions. You can also run the script remotely under the System account
on startup.

```
$registryPath="HKLM:\Software\Amazon\AppStream Client"
New-Item -Path "HKLM:\Software\Amazon" -Name "AppStream Client" -Force

New-ItemProperty -Path $registryPath -Name "SmartCardRedirectionDisabled" -Value "True" -PropertyType String -Force | Out-Null
```

## Configure Additional WorkSpaces Applications Client Settings for Your Users

The WorkSpaces Applications client uses registry keys to configure the following additional client settings:

- WorkSpaces Applications client End-User License Agreement (EULA) acceptance
- WorkSpaces Applications client EULA version accepted
- Automatic diagnostic log uploads for the WorkSpaces Applications client
- Automatic updates for the USB driver that is used to pass USB drivers to WorkSpaces Applications
- Enabling hardware rendering in the WorkSpaces Applications client
- Setting custom folder paths for file system redirection in the WorkSpaces Applications client
- Opening URL for your identity provider (IdP) in system default
  browser

The following table summarizes the registry values for additional client settings that you can use to customize the WorkSpaces Applications client experience for your users.

###### Note

These values are case sensitive.

| Value                                 | Registry path                           | Type   | Description                                                                                                                                                                                                                                | Data                                                                                 |
| ------------------------------------- | --------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ----------------------- | ----------------------- | ------------------- |
| `EULAAccepted`                        | `HKCU\Software\Amazon\Appstream Client` | String | Set this value to `true` to accept the WorkSpaces Applications client EULA on behalf of your users.                                                                                                                                        | `true`/`false`                                                                       |
| `AcceptedEULAVersion`                 | `HKCU\Software\Amazon\Appstream Client` | String | The version of EULA that is accepted. If the current version of<br>the WorkSpaces Applications client EULA is different from the version of the EULA<br>that is accepted, users are prompted to accept the current<br>version of the EULA. | `1.0`                                                                                |
| `DiagnosticInfoCollectionAllowed`     | `HKCU\Software\Amazon\Appstream Client` | String | Set this value to `true` to enable WorkSpaces Applications to<br>automatically send diagnostic logs from the WorkSpaces Applications client to<br>WorkSpaces Applications (AWS).                                                           | `true`/`false`                                                                       |
| `USBDriverOptIn`                      | `HKCU\Software\Amazon\Appstream Client` | String | Set this value to `true` to enable WorkSpaces Applications to automatically update the USB driver that is used to pass USB drivers to WorkSpaces Applications.                                                                             | `true`/`false`                                                                       |
| `HardwareRenderingEnabled`            | `HKCU\Software\Amazon\Appstream Client` | String | Set this value to `true` to enable hardware<br>rendering in the WorkSpaces Applications client.                                                                                                                                            | `true`/`false`                                                                       |
| `FileRedirectionCustomDefaultFolders` | `HKCU\Software\Amazon\Appstream Client` | String | Set this value to include at least one folder path for file<br>system redirection. Separate multiple folder paths by using '                                                                                                               | '.<br>By default, the following folder paths are specified:<br>%USERPROFILE%\Desktop | %USERPROFILE%\Documents | %USERPROFILE%\Downloads | `Valid folder path` |
| `OpenIdpUrlInSystemBrowser`           | `HKCU\Software\Amazon\Appstream Client` | String | Set this value to `true` to enable the WorkSpaces Applications<br>client to open the IdP URL in a system default browser. This<br>feature is supported on client version 1.1.1360 and<br>later.                                            | `true`/`false`                                                                       |

After the WorkSpaces Applications client is installed, you can run the following PowerShell script to
create these registry keys. If you don’t want to create all of the registry keys,
modify the script as needed to create only the registry keys that you want. Or, you
can use the administrative template that is provided in the WorkSpaces Applications client Enterprise
Deployment Tool to configure the client through Group Policy.

###### Note

You must set the following entries for each user.

```
$registryPath="HKCU:\Software\Amazon\AppStream Client"
New-Item -Path "HKCU:\Software\Amazon" -Name "AppStream Client" -Force
New-ItemProperty -Path $registryPath -Name "EULAAccepted" -Value "true" -PropertyType String -Force | Out-Null
New-ItemProperty -Path $registryPath -Name "AcceptedEULAVersion" -Value "1.0" -PropertyType String -Force | Out-Null
New-ItemProperty -Path $registryPath -Name "DiagnosticInfoCollectionAllowed" -Value "true" -PropertyType String -Force | Out-Null
New-ItemProperty -Path $registryPath -Name "USBDriverOptIn" -Value "true" -PropertyType String -Force | Out-Null
New-ItemProperty -Path $registryPath -Name "HardwareRenderingEnabled" -Value "true" -PropertyType String -Force | Out-Null
New-ItemProperty -Path $registryPath -Name "FileRedirectionCustomDefaultFolders" -Value "%USERPROFILE%\Desktop|%USERPROFILE%\Documents|%USERPROFILE%\Downloads" -PropertyType String -Force | Out-Null
New-ItemProperty -Path $registryPath -Name "OpenIdpUrlInSystemBrowser" -Value "true" -PropertyType String -Force | Out-Null
```

## Using Group Policy to Customize WorkSpaces Applications Client Experience

You can use the administrative template that is provided in the WorkSpaces Applications client
Enterprise Deployment Tool to configure the client through Group Policy. To
learn how to load administrative templates into the Group Policy Management Console,
see [Recommendations for managing Group Policy administrative template
(.adm) files](https://support.microsoft.com/en-us/help/816662/recommendations-for-managing-group-policy-administrative-template-adm "https://support.microsoft.com/en-us/help/816662/recommendations-for-managing-group-policy-administrative-template-adm") in the Microsoft Support documentation.
