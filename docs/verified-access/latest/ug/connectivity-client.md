# Connectivity Client for AWS Verified Access

AWS Verified Access provides the Connectivity Client so that you can enable connectivity
between user devices and non-HTTP applications. The client securely encrypts
user traffic, adds user identity information and device context, and routes
it to Verified Access for policy enforcement. If the access policies allow access, the
user is connected to the application. User access is continuously authorized for
as long as the Connectivity Client is connected.

The client runs as a system service and is resilient against crashes. If the connection
becomes unsteady, the client reestablishes the connection.

The client uses ephemeral OAuth access tokens to establish the secure tunnel. The
tunnel is disconnected when the user signs out of the client.

Access and refresh tokens are stored locally on the user device, in an encrypted
SQLite database.

###### Contents

- [Prerequisites](#connectivity-client-prerequisites "#connectivity-client-prerequisites")
- [Download the Connectivity Client](#connectivity-client-download "#connectivity-client-download")
- [Export the client configuration file](#connectivity-client-export-configuration "#connectivity-client-export-configuration")
- [Connect to the application](#connectivity-client-connect "#connectivity-client-connect")
- [Uninstall the client](#connectivity-client-uninstall "#connectivity-client-uninstall")
- [Best practices](#connectivity-client-best-practices "#connectivity-client-best-practices")
- [Troubleshooting](#connectivity-client-troubleshooting "#connectivity-client-troubleshooting")
- [Version history](#connectivity-client-version-history "#connectivity-client-version-history")

## Prerequisites

Before you begin, complete the following prerequisites:

- Create a Verified Access instance with a trust provider.
- Create a TCP endpoint for your application.
- Disconnect your computer from any VPN clients to avoid routing issues.
- Enable IPv6 on your computer. For instructions, see the documentation for the
  operating system that is running on your computer.
- On a Windows computer, verify that [Trusted Platform Module (TPM)](https://support.microsoft.com/en-us/topic/what-s-a-trusted-platform-module-tpm-705f241d-025d-4470-80c5-4feeb24fa1ee "https://support.microsoft.com/en-us/topic/what-s-a-trusted-platform-module-tpm-705f241d-025d-4470-80c5-4feeb24fa1ee")
  is supported and install the [WebView2](https://developer.microsoft.com/en-us/microsoft-edge/webview2 "https://developer.microsoft.com/en-us/microsoft-edge/webview2") runtime.

## Download the Connectivity Client

Uninstall any previous version of the client. Download the client, verify that
the installer is signed, and run the installer. Do not install the client using an
unsigned installer.

- [Connectivity Client for Mac with Apple Silicon version 1.0.2](https://d1wo6wuaox5vq3.cloudfront.net/mac-arm64/1.0.2/ConnectivityClientInstaller.pkg "https://d1wo6wuaox5vq3.cloudfront.net/mac-arm64/1.0.2/ConnectivityClientInstaller.pkg")
- [Connectivity Client for Mac with Intel version 1.0.2](https://d1wo6wuaox5vq3.cloudfront.net/mac-x86_64/1.0.2/ConnectivityClientInstaller.pkg "https://d1wo6wuaox5vq3.cloudfront.net/mac-x86_64/1.0.2/ConnectivityClientInstaller.pkg")
- [Connectivity Client for Windows with x64 version 1.0.2](https://d1wo6wuaox5vq3.cloudfront.net/windows-x86_64/1.0.2/ConnectivityClientInstaller.msi "https://d1wo6wuaox5vq3.cloudfront.net/windows-x86_64/1.0.2/ConnectivityClientInstaller.msi")

## Export the client configuration file

Use the following procedure to export the configuration information required by the
client from your Verified Access instance.

###### To export the client configuration file using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Verified Access instances**.
3. Select the Verified Access instance.
4. Choose **Actions**, **Export client configuration file**.

###### To export the client configuration file using the AWS CLI

Use the [export-verified-access-instance-client-configuration](../../../cli/latest/reference/ec2/export-verified-access-instance-client-configuration.md "../../../cli/latest/reference/ec2/export-verified-access-instance-client-configuration.md") command. Save the output to a
.json file. The file name must start with the `ClientConfig-` prefix.

## Connect to the application

Use the following procedure to connect to an application using the client.

###### To connect to an application using the client

1. Deploy the client configuration files to the users' devices in the following
   location:
   - Windows – `C:\ProgramData\Connectivity Client`
   - macOS – `/Library/Application\ Support/Connectivity\ Client`

2. Ensure that the client configuration files are owned by root (macOS) or Admin (Windows).
3. Launch the Connectivity Client.
4. After the Connectivity Client is loaded, the user is authenticated by the IdP.
5. After authentication, users can access the application using the DNS name provided by Verified Access,
   using the client of their choice.

## Uninstall the client

When you are finished using the Connectivity Client, you can uninstall it.

macOS

###### Version 1.0.1 and later

Navigate to `/Applications/Connectivity Client` and run
`Connectivity Client Uninstaller.app`.

###### Version 1.0.0

Download the `connectivity_client_cleanup.sh` script for
[Mac with Apple Silicon](https://d1wo6wuaox5vq3.cloudfront.net/mac-arm64/1.0.0/connectivity_client_cleanup.sh "https://d1wo6wuaox5vq3.cloudfront.net/mac-arm64/1.0.0/connectivity_client_cleanup.sh")
or [Mac with Intel](https://d1wo6wuaox5vq3.cloudfront.net/mac-x86_64/1.0.0/connectivity_client_cleanup.sh "https://d1wo6wuaox5vq3.cloudfront.net/mac-x86_64/1.0.0/connectivity_client_cleanup.sh"),
set execution permissions on the script, and run the script as follows.

```
sudo ./connectivity_client_cleanup.sh
```

Windows
To uninstall the client on Windows, run the installer and choose **Remove**.

## Best practices

Consider the following best practices:

- Install the latest version of the client.
- Do not install the client using an unsigned installer.
- Users should not use a configuration unless it is a trusted configuration provided by
  an IT admin. An untrusted configuration could redirect to a phishing page.
- Users should sign out of the client before leaving their workstations idle.
- Add the `offline_access` scope to your OIDC configuration. This allows
  requests for refresh tokens, which are used to obtain more access tokens without
  requiring the user to re-authenticate.

## Troubleshooting

The following information can help you troubleshoot issues with the client.

###### Issues

- [When signing in, the browser doesn't open to complete authentication by the IdP](#issue-signing-in "#issue-signing-in")
- [After authentication, the client status is "not connected"](#issue-not-connected "#issue-not-connected")
- [Can't connect using a Chrome or Edge browser](#issue-chrome-edge "#issue-chrome-edge")

### When signing in, the browser doesn't open to complete authentication by the IdP

Possible cause: The configuration file is missing
or malformed.

Solution: Contact your system administrator and
request an updated configuration file.

### After authentication, the client status is "not connected"

Possible cause: Running other VPN software, such as
AWS Client VPN, Cisco AnyConnect, or OpenVPN Connect.

Solution: Disconnect from any other VPN software.
If you're still unable to connect, generate a diagnostic report and share it with
your system administrator.

Possible cause: On Windows platforms, the client uses HTTP on port 80
for control plane communication. A firewall rule that blocks TCP port 80 prevents control plane communication.

Solution: Check Windows Firewall rules for an explicit outbound
rule blocking TCP on port 80 and disable it.

### Can't connect using a Chrome or Edge browser

Possible cause: When connecting to a web application using
a Chrome or Edge browser, the browser fails to resolve the IPv6 domain name.

Solution: Contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

## Version history

The following table contains the version history of the client.

| Version | Changes                                                                                                                                        | Download                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Date             |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| 1.0.2   | macOS<br>• Bug fixes and stability improvements<br>• UI enhancements<br>Windows<br>• Bug fixes and stability improvements<br>• UI enhancements | • [Mac with Apple Silicon](https://d1wo6wuaox5vq3.cloudfront.net/mac-arm64/1.0.2/ConnectivityClientInstaller.pkg "https://d1wo6wuaox5vq3.cloudfront.net/mac-arm64/1.0.2/ConnectivityClientInstaller.pkg")<br>• [Mac with Intel](https://d1wo6wuaox5vq3.cloudfront.net/mac-x86_64/1.0.2/ConnectivityClientInstaller.pkg "https://d1wo6wuaox5vq3.cloudfront.net/mac-x86_64/1.0.2/ConnectivityClientInstaller.pkg")<br>• [Windows with x64](https://d1wo6wuaox5vq3.cloudfront.net/windows-x86_64/1.0.2/ConnectivityClientInstaller.msi "https://d1wo6wuaox5vq3.cloudfront.net/windows-x86_64/1.0.2/ConnectivityClientInstaller.msi") | June 9, 2025     |
| 1.0.1   | macOS<br>• Stability improvements<br>• Uninstaller application<br>Windows<br>• Stability improvements                                          | • [Mac with Apple Silicon](https://d1wo6wuaox5vq3.cloudfront.net/mac-arm64/1.0.1/ConnectivityClientInstaller.pkg "https://d1wo6wuaox5vq3.cloudfront.net/mac-arm64/1.0.1/ConnectivityClientInstaller.pkg")<br>• [Mac with Intel](https://d1wo6wuaox5vq3.cloudfront.net/mac-x86_64/1.0.1/ConnectivityClientInstaller.pkg "https://d1wo6wuaox5vq3.cloudfront.net/mac-x86_64/1.0.1/ConnectivityClientInstaller.pkg")<br>• [Windows with x64](https://d1wo6wuaox5vq3.cloudfront.net/windows-x86_64/1.0.1/ConnectivityClientInstaller.msi "https://d1wo6wuaox5vq3.cloudfront.net/windows-x86_64/1.0.1/ConnectivityClientInstaller.msi") | February 5, 2025 |
| 1.0.0   | Public preview                                                                                                                                 | • [Mac with Apple Silicon](https://d1wo6wuaox5vq3.cloudfront.net/mac-arm64/1.0.0/ConnectivityClientInstaller.pkg "https://d1wo6wuaox5vq3.cloudfront.net/mac-arm64/1.0.0/ConnectivityClientInstaller.pkg")<br>• [Mac with Intel](https://d1wo6wuaox5vq3.cloudfront.net/mac-x86_64/1.0.0/ConnectivityClientInstaller.pkg "https://d1wo6wuaox5vq3.cloudfront.net/mac-x86_64/1.0.0/ConnectivityClientInstaller.pkg")<br>• [Windows with x64](https://d1wo6wuaox5vq3.cloudfront.net/windows-x86_64/1.0.0/ConnectivityClientInstaller.msi "https://d1wo6wuaox5vq3.cloudfront.net/windows-x86_64/1.0.0/ConnectivityClientInstaller.msi") | December 1, 2024 |
