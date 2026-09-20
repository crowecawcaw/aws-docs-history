

# Getting started
<a name="getting-started-desktop"></a>

This section walks you through downloading, installing, and signing in to the Amazon Quick desktop application for macOS and Windows.

## Prerequisites
<a name="desktop-prerequisites"></a>

Verify that your system meets the following requirements.

### macOS
<a name="desktop-prerequisites-macos"></a>


| Requirement | Minimum | 
| --- | --- | 
| Operating system | macOS 12 (Monterey) or later | 
| Processor | Apple Silicon (M1 or later) | 
| Memory | 8 GB RAM | 
| Disk space | 2 GB available for installation. 10 GB or more recommended for search indexing and knowledge graph features. | 
| Internet | Required for sign-in, AI model access, and connected services | 

### Windows
<a name="desktop-prerequisites-windows"></a>


| Requirement | Minimum | 
| --- | --- | 
| Operating system | Windows 10 (64-bit) or later | 
| Processor | x86\_64 compatible | 
| Memory | 8 GB RAM | 
| Disk space | 2 GB available for installation. 10 GB or more recommended for search indexing and knowledge graph features. | 
| Internet | Required for sign-in, AI model access, and connected services | 

## Downloading and installing
<a name="desktop-download-install"></a>

**Important**  
If your organization uses an Enterprise account, complete the steps in [Setting up Amazon Quick on desktop for enterprise deployments](desktop-enterprise-setup.md) before downloading or distributing the application. Enterprise sign-in becomes available after an administrator configures it.

You can download the Amazon Quick desktop application from the following locations:
+ **Amazon Quick web application** – Sign in to Amazon Quick on the web. In the left navigation, choose **Extensions**, find the desktop extension card, and choose the download for your platform.
+ **Direct download** – Use the following links:


<table>
<thead>
  <tr><th>Platform</th><th>Download</th></tr>
</thead>
<tbody>
  <tr><td>macOS (Apple Silicon)</td><td><a href="https://desktop.downloads.quick.aws.com/mac/arm64/Amazon-Quick.dmg">Amazon-Quick.dmg</a></td></tr>
  <tr><td>Windows (x64)</td><td><a href="https://desktop.downloads.quick.aws.com/windows/x64/Amazon-Quick.exe">Amazon-Quick.exe</a></td></tr>
</tbody>
</table>


**To install on macOS**

1. Download the `.dmg` installer file.

1. Open the `.dmg` file.

1. Drag **Amazon Quick** to the **Applications** folder.

1. Open **Amazon Quick** from the Applications folder or Launchpad.

**Note**  
On first launch, macOS might report that the application is from an unidentified developer or was downloaded from the internet. Choose **Open** to continue. If macOS blocks the application, open **System Settings**, choose **Privacy & Security**, scroll to **Security**, and choose **Open Anyway**.

**To install on Windows**

1. Download the `.exe` installer file.

1. Run the installer and follow the on-screen prompts.

1. After installation, launch **Amazon Quick** from the Start menu or desktop shortcut.

**Note**  
On first launch, Windows might display a SmartScreen prompt. Choose **More info**, then **Run anyway**, to continue.

## Signing in
<a name="desktop-sign-in"></a>

When you open the application, the sign-in screen shows the available options.

**To sign in with a personal account**

1. Open the application.

1. On the sign-in screen, choose **Continue with**, and select your provider (for example, email, Amazon, Apple, Google, or GitHub).

1. Enter your credentials on the provider's sign-in page.

1. Complete any multi-factor authentication prompts.

1. After authentication succeeds, the application loads the Home screen.

Enterprise sign-in becomes available after your organization's administrator configures it.

**To sign in with an enterprise account**

1. Open the application.

1. On the sign-in screen, choose **Continue with single sign-on (SSO)**.

1. (Optional) Select your AWS Region, or choose **Dynamic** to detect it automatically.

1. Enter your corporate credentials on your organization's identity provider page.

1. After authentication succeeds, the application loads the Home screen.

## First-run setup
<a name="desktop-first-run-setup"></a>

After you sign in for the first time, Quick guides you through connecting your data sources. The onboarding flow presents categories of connections:


| Category | What it connects | Examples | 
| --- | --- | --- | 
| Email | Calendar and email, for meeting prep and action items | A calendar or email connector | 
| Messaging | Threads, direct messages, and channels | A messaging connector | 
| Local files | Folders on your computer | Any folder on your machine | 

For each category, choose **Connect** to set it up, or **Dismiss** to skip it. You can connect data sources later from **Customize**, on the **Connectors** tab. For more information, see [Connectors](connections-desktop.md).