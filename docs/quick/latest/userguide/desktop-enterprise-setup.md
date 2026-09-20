

# Setting up Amazon Quick on desktop for enterprise deployments
<a name="desktop-enterprise-setup"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators  | 

To use Amazon Quick on desktop for enterprise deployments, administrators must configure enterprise single sign-on (SSO) so that users in the organization can sign in with their corporate credentials. This setup connects your organization's OpenID Connect (OIDC) compatible identity provider (IdP) to Amazon Quick.

**Note**  
If you are using a Free or Plus account, this section does not apply to you. Continue to [Getting started](getting-started-desktop.md).

## How enterprise sign-in works
<a name="desktop-enterprise-how-it-works"></a>

The Amazon Quick desktop application uses the OIDC protocol to authenticate users. When you choose **Continue with SSO**, a browser window opens to Amazon Quick. Amazon Quick identifies your configured identity provider and redirects to your IdP's authorization endpoint. The application then exchanges the resulting authorization code for tokens using Proof Key for Code Exchange (PKCE).

To identify the configured identity provider, your browser must have an active Amazon Quick web session. If no session exists, the browser prompts you to sign in to Amazon Quick before the application redirects to your IdP.

Amazon Quick validates the token and maps the user to an identity in your account. The email address in your IdP must exactly match the email address of the user in Amazon Quick.

**Note**  
If you sign in for the first time, the browser checks for an active Amazon Quick web session. If no session exists, the browser opens the Amazon Quick sign-in page instead of redirecting to your IdP. Sign in to Amazon Quick in the browser to continue. The desktop application then completes sign-in through your configured identity provider.

## Supported token signing algorithms
<a name="desktop-enterprise-token-signing"></a>

Amazon Quick verifies the signature on each ID token against the public keys published at your identity provider's JWKS URI. Your IdP must sign ID tokens with one of the following asymmetric algorithms.


| Key type | Supported `alg` values | 
| --- | --- | 
| RSA | RS256, RS384, RS512, PS256, PS384, PS512 | 
| ECDSA | ES256, ES384, ES512 | 

**Symmetric signing is not supported**  
Amazon Quick does not accept ID tokens signed with HMAC (`HS256`, `HS384`, or `HS512`). These algorithms sign the token with the client secret rather than with a key that can be published in a JWKS, so the signature cannot be verified against your IdP's JWKS URI. Unsecured tokens (an `alg` value of `none`) are also rejected. If your IdP is configured to use one of these, sign-in fails with a token validation error.

You do not select the algorithm in Amazon Quick. Your IdP chooses it when it issues the token, and Amazon Quick accepts any of the algorithms in the preceding table. Most identity providers use `RS256` by default.

## Prerequisites
<a name="desktop-enterprise-prerequisites"></a>

Before you begin, verify that you have the following:
+ An AWS account with an active Amazon Quick subscription. The Amazon Quick account's home region (identity region) must be in a supported AWS Region. For a list of supported Regions, see [Supported AWS Regions for Amazon Quick](regions.md#regions-qs). All identity types are supported, including IAM Identity Center, IAM federation, and native Amazon Quick (username/password) users.
+ Administrator access to your Amazon Quick account.
+ Access to your IdP with permissions to create OIDC application registrations.
+ In restricted network environments, the ability to reach the required Amazon Quick and identity provider domains. For the list of domains to add to your allow list, see [Network access and required domains](desktop-security.md#desktop-network-access).

**Important**  
Amazon Quick on desktop is available for Enterprise accounts in AWS Regions that support the full Amazon Quick feature set. Regions that support Amazon Quick Sight capabilities only do not include desktop. For the full list, see [Supported AWS Regions for Amazon Quick](regions.md#regions-qs).

## Setup process
<a name="desktop-enterprise-process"></a>

Setting up enterprise sign-in involves the same four steps regardless of which identity provider you use:

1. **Create an OIDC application in your identity provider.** Register a public OIDC client and record its Client ID and OIDC endpoints. The steps and endpoint formats are specific to your identity provider.

1. **Add the extension access in the Amazon Quick administration console.** In the Amazon Quick administration console, add an extension access using the Client ID and OIDC endpoints from Step 1.

1. **Create the extension in the Amazon Quick console.** On the **Extensions** page in the Amazon Quick console, create the extension from the extension access you added in Step 2.

1. **Download, verify, and distribute the desktop application.** Download and install the application, choose **Continue with SSO** to confirm that authentication succeeds, and then direct your users to download and sign in.

The complete procedure for each of these steps is documented on the page for your identity provider. Choose your identity provider to get started:
+ [Microsoft Entra ID](desktop-enterprise-entra-id.md) – Microsoft Entra ID
+ [Google Workspace](desktop-enterprise-google-workspace.md) – Google Workspace
+ [Okta](desktop-enterprise-okta.md) – Okta
+ [Ping Identity](desktop-enterprise-ping-identity.md) – Ping Identity (PingFederate and PingOne)

If you encounter problems during setup or sign-in, see [Troubleshooting enterprise sign-in for Amazon Quick on desktop](desktop-enterprise-setup-troubleshooting.md).

## Managed deployment configuration
<a name="desktop-enterprise-managed-deployment"></a>

Administrators can configure and deploy Amazon Quick on desktop across an enterprise fleet using the following options.

### Managed policies
<a name="desktop-enterprise-mdm-policies"></a>

Amazon Quick reads policies from vendor-neutral OS-managed locations. Any mobile device management (MDM) tool that can deliver a configuration profile (macOS) or registry policy (Windows) works without vendor-specific integration.


| Policy | macOS location | Windows location | Effect | 
| --- | --- | --- | --- | 
| DisableSocialLogin | Preference domain com.aws.QuickWork.mac | HKLM\\SOFTWARE\\Policies\\Amazon\\Quick (REG\_DWORD) | Hides social sign-in, blocks it server-side, and hides "Sign up for free." This policy enforces enterprise SSO as the only authentication path. | 
| DisableAutoUpdates | Preference domain com.aws.QuickWork.mac | HKLM\\SOFTWARE\\Policies\\Amazon\\Quick (REG\_SZ) | Stops the application from updating itself, so that your organization controls when new versions reach the fleet. Accepts patch, minor, or major. The value is the smallest update size that the policy blocks. patch blocks all automatic updates. minor allows patch updates only. major allows patch and minor updates. | 

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

### Proxy support
<a name="desktop-enterprise-proxy-support"></a>

Amazon Quick respects the operating system's proxy configuration (system proxy on Windows, Proxy Auto-Configuration on macOS). All application network traffic, including child processes, routes through the configured enterprise proxy automatically. You don't need to configure the proxy separately.

### Application data paths
<a name="desktop-enterprise-data-paths"></a>

The following table lists the application data paths for each operating system.


| OS | Path | 
| --- | --- | 
| macOS | \~/.quickwork/ | 
| Windows | %USERPROFILE%\\.quickwork\\ | 

This directory contains local user-specific settings and configurations.

### Silent installation and fleet deployment
<a name="desktop-enterprise-silent-install"></a>

To distribute the application silently to a managed fleet with a mobile device management (MDM) solution – including per-machine packaging for Microsoft Intune and other MDM tools, certificate authority trust, and troubleshooting – see [Deploying Amazon Quick on desktop to a managed fleet with MDM](desktop-enterprise-mdm.md).

For a single-user silent installation on Windows, the installer also supports silent mode. This installs Amazon Quick for the current user in `%LOCALAPPDATA%` and creates desktop and Start menu shortcuts.

```
.\Amazon-Quick-Setup.exe /S
```

### Application updates
<a name="desktop-enterprise-updates"></a>

By default, Amazon Quick delivers updates automatically over HTTPS. Updates are code-signed and apply for each user on the next restart. On macOS, updates use Apple notarization. On Windows, updates use Authenticode signing.

To take control of update delivery, set the `DisableAutoUpdates` policy described in [Managed policies](#desktop-enterprise-mdm-policies). When you block updates, you become responsible for delivering new versions to the fleet, using the same tools you use to deploy other managed applications.

Even when you block updates, Amazon Quick can still notify your users of a required update and restrict functionality remotely if a critical issue is found.

**Important**  
We strongly recommend that you continue to allow patch updates. Patch updates deliver security fixes, performance improvements, and bug fixes. To control larger updates while your fleet still receives patches, set `DisableAutoUpdates` to `minor` or `major` instead of `patch`.

**Topics**
+ [How enterprise sign-in works](#desktop-enterprise-how-it-works)
+ [Supported token signing algorithms](#desktop-enterprise-token-signing)
+ [Prerequisites](#desktop-enterprise-prerequisites)
+ [Setup process](#desktop-enterprise-process)
+ [Managed deployment configuration](#desktop-enterprise-managed-deployment)
+ [Set up enterprise sign-in with Microsoft Entra ID for Amazon Quick on desktop](desktop-enterprise-entra-id.md)
+ [Set up enterprise sign-in with Google Workspace for Amazon Quick on desktop](desktop-enterprise-google-workspace.md)
+ [Set up enterprise sign-in with Okta for Amazon Quick on desktop](desktop-enterprise-okta.md)
+ [Set up enterprise sign-in with Ping Identity for Amazon Quick on desktop](desktop-enterprise-ping-identity.md)
+ [Troubleshooting enterprise sign-in for Amazon Quick on desktop](desktop-enterprise-setup-troubleshooting.md)
+ [Deploying Amazon Quick on desktop to a managed fleet with MDM](desktop-enterprise-mdm.md)