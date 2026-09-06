

# Deploying Amazon Quick on desktop to a managed fleet with MDM
<a name="desktop-enterprise-mdm"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators  | 

As an administrator, you can distribute the Amazon Quick desktop application to a managed fleet with mobile device management (MDM), without any per-machine interaction. This page describes the deployment using Microsoft Intune for both macOS and Windows. The artifacts it describes – a signed macOS `.pkg` and a per-machine Windows `.exe` – also work with other MDM solutions, such as Jamf, Kandji, and VMware Workspace ONE. Only the upload mechanics differ between solutions.

This page describes how to complete the following tasks:

1. Get the per-machine installer artifacts from the download service.

1. Deploy the macOS application with Microsoft Intune.

1. Deploy the Windows application with Microsoft Intune.

1. (Optional) Trust a corporate certificate authority for networks that inspect encrypted traffic.

**Note**  
This page covers distributing the application binary. To let users sign in with their corporate credentials, you must also configure enterprise single sign-on. For more information, see [Setting up Amazon Quick on desktop for enterprise deployments](desktop-enterprise-setup.md). To enforce enterprise SSO as the only sign-in method by disabling consumer social login across your fleet, see [Managed policies](desktop-enterprise-setup.md#desktop-enterprise-mdm-policies).

## Prerequisites
<a name="desktop-mdm-prerequisites"></a>

Before you begin, verify that you have the following:
+ Administrator access to your MDM solution, and a fleet of devices that are enrolled in it.
+ Devices that meet the Amazon Quick desktop application system requirements. For the macOS and Windows requirements, see [Prerequisites](getting-started-desktop.md#desktop-prerequisites).
+ For Windows, devices that run Windows Pro, Enterprise, or Education. The application deployment method for Windows uses the Win32 app type, which Microsoft Intune does not support on Windows Home. MDM enrollment also requires a Windows client edition (Windows Server is not supported for MDM enrollment).
+ For Windows, the Microsoft Win32 Content Prep Tool (`IntuneWinAppUtil.exe`), which packages the installer into the `.intunewin` format that the Win32 app type requires. For more information, see [Microsoft Win32 Content Prep Tool](https://github.com/microsoft/Microsoft-Win32-Content-Prep-Tool) on GitHub.

**Use per-machine installers only**  
Use the per-machine installer variants described in this page, not the per-user installers that your users download individually. An MDM solution runs as the system account with no signed-in user, so a per-user installer does not deploy correctly in that context.

## Get the installer artifacts
<a name="desktop-mdm-artifacts"></a>

The Amazon Quick download service at `desktop.downloads.quick.aws.com` provides the desktop installers. For MDM deployment, use the per-machine installer for each platform. The per-machine installer differs from the per-user installer that individual users download from the standard download page:
+ **macOS** – a signed, notarized component `.pkg`, named `Amazon Quick-{{version}}-arm64.pkg`, that installs `Amazon Quick.app` to the `/Applications` folder as the root user.
+ **Windows** – a per-machine `.exe`, named `Amazon Quick-Admin Setup {{version}}.exe`, that installs the application for all users into `C:\Program Files\Amazon Quick\`.

Each platform publishes a channel manifest that lists the current version and a SHA-512 checksum. Fetch the manifest to find the version to deploy and the checksum to verify your download against.

```
# macOS manifest
curl -fsSL https://desktop.downloads.quick.aws.com/darwin/arm64/quick-latest-mac.yml

# Windows per-machine manifest
curl -fsSL https://desktop.downloads.quick.aws.com/win32/x64/quick-prod-admin.yml
```

Download the per-machine artifact for each platform. In the following URL patterns, replace {{version}} with the version from the manifest.

```
# macOS .pkg (per-machine, installs to /Applications)
https://desktop.downloads.quick.aws.com/darwin/arm64/quick-prod/Amazon Quick-{{version}}-arm64.pkg

# Windows per-machine .exe (installs for all users into Program Files)
https://desktop.downloads.quick.aws.com/win32/x64/quick-prod-admin/Amazon Quick-Admin Setup {{version}}.exe
```

A pre-production beta channel also exists for internal testing. It updates itself automatically and does not publish a public first-time installer, so it is not used for MDM deployment. For the standard download page that individual users use, see [Downloading and installing](getting-started-desktop.md#desktop-download-install).

### Static and version-specific download URLs
<a name="desktop-mdm-download-urls"></a>

The Windows per-machine `.exe` also has a static download link that always resolves to the current version, so you do not need to fetch the manifest first:

```
https://desktop.downloads.quick.aws.com/windows/x64/Amazon-Quick-Admin.exe
```

To pin a specific version, fetch the manifest first to get the exact version string, and then use the version-specific channel URL.

For macOS, download the `.pkg` in two steps, because the `.pkg` is published only under its version-specific channel path. Fetch the manifest to get the current version, and then substitute that version into the URL.

## Deploying the macOS application with Microsoft Intune
<a name="desktop-mdm-macos"></a>

The macOS installer is a signed, notarized component `.pkg` that installs `Amazon Quick.app` to the `/Applications` folder.

**To add and assign the macOS application**

1. In the Microsoft Intune admin center, go to **Apps → All apps → Add**, and then select the **macOS app (PKG)** app type.
**Note**  
Use the **macOS app (PKG)** type, not the line-of-business app type.

1. Choose **Select app package file**, and then upload the `.pkg` that you downloaded.

1. In the **Included apps** detection list, keep only the main application bundle and remove the helper bundles.
**Keep only the main application bundle**  
The macOS installer includes the main application plus four nested helper components inside `Contents/Frameworks/`. When you upload the `.pkg`, Microsoft Intune automatically populates the **Included apps** list with all five bundles. Delete the four helper rows (the ones whose IDs end in `.e0` through `.e3`, such as **Amazon Quick Helper (GPU)**) so that exactly one entry remains, with the following values.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/quick/latest/userguide/desktop-enterprise-mdm.html)
If you leave the helper rows in place, macOS might report installation failure code `0x87D13BA2` even when the application files are present.  
The app bundle ID (`com.aws.QuickWork.mac`) is the application's `CFBundleIdentifier`, which Microsoft Intune uses for detection. It is intentionally different from the installer's package receipt identifier (`com.amazon.QuickWork.mac`), which you use with `pkgutil --forget` when you clean a test device.

1. Set **Ignore app version** to **Yes**. The application includes a built-in updater that keeps it current from the channel manifest, so let the application manage its own version. With this setting, Microsoft Intune installs the application once if the bundle ID is absent, and then does not reinstall it when the version changes. Without it, Microsoft Intune repeatedly attempts to reinstall when it detects version drift between what it deployed and what the auto-updater has since applied.

1. On the **Assignments** tab, add a device or user group with the **Required** intent.

On each assigned device, the installation runs silently and the application is installed at `/Applications/Amazon Quick.app`. To verify the installation on a device, run the following command and confirm that it returns `com.aws.QuickWork.mac`.

```
defaults read "/Applications/Amazon Quick.app/Contents/Info" CFBundleIdentifier
```

Device-side deployment logs are in the `/Library/Logs/Microsoft/Intune/` directory.

## Deploying the Windows application with Microsoft Intune
<a name="desktop-mdm-windows"></a>

The Windows installer is an NSIS `.exe`. The Microsoft Intune Win32 app type does not accept a raw `.exe`, so you first wrap the installer into a `.intunewin` package. Use the **Windows app (Win32)** app type. The line-of-business app type accepts only `.msi`, `.appx`, and `.msix` files, so it does not apply.

The following table lists the key facts for the per-machine Windows installer.


| Item | Value | 
| --- | --- | 
| Silent install flag | /S (a capital S, not /silent) | 
| Silent uninstall flag | /S | 
| Install path | C:\\Program Files\\Amazon Quick\\ | 
| Binary name | Amazon Quick.exe | 
| Uninstaller name | Uninstall Amazon Quick.exe | 
| Required edition | Windows Pro, Enterprise, or Education (not Home) | 

**To wrap the installer into a .intunewin package**

1. Place the `.exe` installer by itself in a source folder.

1. Run the Win32 Content Prep Tool, replacing {{version}} with the version you downloaded.

   ```
   IntuneWinAppUtil.exe -c C:\IntuneSource -s "Amazon Quick-Admin Setup {{version}}.exe" -o C:\IntuneOutput -q
   ```

   The tool creates `C:\IntuneOutput\Amazon Quick-Admin Setup {{version}}.intunewin`.

**To create and assign the Win32 application**

1. In the Microsoft Intune admin center, go to **Apps → All apps → Add**, select the **Windows app (Win32)** app type, and then upload the `.intunewin` package.

1. On the **Program** tab, configure the following settings. Replace {{version}} with the version you downloaded.
   + **Install command** – `"Amazon Quick-Admin Setup {{version}}.exe" /S`
   + **Uninstall command** – `"C:\Program Files\Amazon Quick\Uninstall Amazon Quick.exe" /S`
   + **Install behavior** – **System**

1. On the **Requirements** tab, set the operating system architecture to **x64** and set the minimum operating system to a supported Windows client version.

1. On the **Detection rules** tab, add a manually configured rule with the following settings.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/quick/latest/userguide/desktop-enterprise-mdm.html)

1. On the **Assignments** tab, add a device group with the **Required** intent.

The Intune Management Extension installs on a device the first time you assign a Win32 application, which can take a few minutes and two device check-ins. To trigger a check-in on a device, go to **Settings → Accounts → Access work or school**, select your account, and choose **Sync**. To watch the installation on a device, tail the log with the following PowerShell command.

```
Get-Content "C:\ProgramData\Microsoft\IntuneManagementExtension\Logs\AppWorkload.log" -Wait -Tail 50
```

## Trusting a corporate certificate authority
<a name="desktop-mdm-tls"></a>

If your network inspects encrypted traffic or uses a custom corporate certificate authority (CA), the Amazon Quick desktop application must trust that CA. Otherwise, sign-in and responses can fail on the corporate network. Examples of traffic-inspection proxies include Zscaler and Netskope.

Deploy the CA into the operating system trust store with an MDM certificate profile. The application reads the operating system trust store when it starts, so a CA that you install there is trusted for all of the application's outbound connections. This approach works on both platforms and requires no environment variables, scripts, or certificate file placement.

macOS  
Deploy a configuration profile with a **Trusted certificate** payload that targets the **System keychain**.

Windows  
Deploy a **Trusted certificate** configuration profile to the computer store under **Trusted Root**.

**Note**  
The certificate profile is the reliable path for the application itself. Deploy environment variables such as `REQUESTS_CA_BUNDLE`, `SSL_CERT_FILE`, or `NODE_EXTRA_CA_CERTS` only if other, non-Amazon Quick tools on the device require the CA through those variables.

### Advanced: environment variables for mixed toolchains on Windows
<a name="desktop-mdm-tls-envvars"></a>

**Do not use per-user path variables in scripts that run under Intune**  
Do not use `%HOMEDRIVE%%HOMEPATH%` in scripts that run under Intune. Intune runs scripts as the system account, where those variables resolve to a service profile path (for example, `C:\Windows\system32\config\systemprofile`), not the user's home directory. Place certificate files and environment-variable scripts at a machine-wide path such as `C:\ProgramData\Amazon Quick\certs\` instead. Use `SETX /M` to write machine-scoped environment variables. New processes inherit these variables after the next sign-in or restart.

The following example install script places the CA bundle at a machine-wide path and sets the environment variables.

```
@echo off
mkdir "C:\ProgramData\Amazon Quick\certs" 2>nul
copy /Y "%~dp0tls-ca-bundle.pem" "C:\ProgramData\Amazon Quick\certs\tls-ca-bundle.pem"
SETX /M REQUESTS_CA_BUNDLE "C:\ProgramData\Amazon Quick\certs\tls-ca-bundle.pem"
SETX /M SSL_CERT_FILE "C:\ProgramData\Amazon Quick\certs\tls-ca-bundle.pem"
exit /b 0
```

The `NODE_EXTRA_CA_CERTS` variable is not consumed by the Amazon Quick agent, so the certificate profile remains the reliable path for the application itself. Use the environment-variable script only if other tooling on the device requires the CA through those variables.

## Troubleshooting MDM deployment
<a name="desktop-mdm-troubleshooting"></a>

The following table describes common issues you might encounter when you deploy the application with an MDM solution, and how to resolve them.

The Windows silent installation does nothing  
Confirm that the install command uses the `/S` flag (a capital `S`), not `/silent`.

A device reports that the Win32 app is not supported  
The device runs Windows Home, which does not support Win32 app deployment. Use a device that runs Windows Pro, Enterprise, or Education.

The IntuneManagementExtension folder or logs are missing  
The Intune Management Extension bootstraps only after you assign a Win32 application and the device checks in. Assign the application, sync the device, and then wait a few minutes.

macOS reports a failure although the files installed  
If macOS reports installation failure code `0x87D13BA2`, the nested helper bundles were left in the **Included apps** list. Delete every helper row so that only the main application bundle (`com.aws.QuickWork.mac`) remains, and then reassign the application.

Microsoft Intune reports the macOS app as installed but the app is missing  
A prior installation left an application bundle or a package receipt on the device. With version-independent detection, this reads as installed and the deployment is skipped. Test on a clean device. To fully clean a test device, remove the application bundle and forget the package receipt, and then test the deployment again.  

```
sudo rm -rf "/Applications/Amazon Quick.app"
sudo pkgutil --forget com.amazon.QuickWork.mac
```

Application binaries are removed after a restart, but profile data survives  
This is caused by a version conflict between the MDM-deployed build and the built-in auto-updater, which happens when the software catalog pins an older version while the auto-updater has already applied a newer one. The installer reads the version mismatch as a broken installation and removes the binaries. To resolve it, set **Ignore app version** to **Yes** in the Intune application configuration, and do not pin a specific version while the auto-updater is active. Admin-controlled version pinning is not available at general availability.

A Windows Server or pooled virtual machine does not enroll  
MDM enrollment requires a persistent Windows client edition (Windows 10 or 11). Windows Server is not supported for MDM enrollment.