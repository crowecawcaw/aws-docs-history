

# Getting started
<a name="getting-started-desktop"></a>

This section walks you through downloading, installing, and signing in to the Amazon Quick desktop application for macOS and Windows.

## Prerequisites
<a name="desktop-prerequisites"></a>

Before you install the Amazon Quick desktop application, verify that your system meets the following requirements.

### macOS
<a name="desktop-prerequisites-macos"></a>


| Requirement | Minimum | 
| --- | --- | 
| Operating system | macOS 12 (Monterey) or later | 
| Processor | Apple Silicon (M1 or later) | 
| Memory | 8 GB RAM | 
| Disk space | 500 MB available (installation only). 10 GB or more recommended for search indexing and knowledge graph features. | 
| Internet | Required for sign-in, AI model access, and connected services | 

### Windows
<a name="desktop-prerequisites-windows"></a>


| Requirement | Minimum | 
| --- | --- | 
| Operating system | Windows 10 (64-bit) or later | 
| Processor | x86\_64 compatible | 
| Memory | 8 GB RAM | 
| Disk space | 500 MB available (installation only). 10 GB or more recommended for search indexing and knowledge graph features. | 
| Internet | Required for sign-in, AI model access, and connected services | 

## Downloading and installing
<a name="desktop-download-install"></a>

**Important**  
If your organization uses an Enterprise account, complete the steps in [Setting up Amazon Quick on desktop for enterprise deployments](desktop-enterprise-setup.md) before downloading or distributing the application. Enterprise sign-in is not available until an administrator configures the extension access.

You can download the Amazon Quick desktop application from the following locations:
+ **Amazon Quick web application** – Sign in to Amazon Quick on the web. In the left navigation, choose **Extensions**. On the **QuickDesktop-extension** card, choose the menu, and then choose **Download for Windows** or **Download for Mac**.
+ **Direct download** – Use the following links:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/quick/latest/userguide/getting-started-desktop.html)

**To install on macOS**

1. Download the `.dmg` installer file.

1. Open the `.dmg` file.

1. Drag **Amazon Quick** to the **Applications** folder.

1. Open **Amazon Quick** from the Applications folder or Launchpad.

**Note**  
On first launch, macOS might display a security prompt stating that the application is from an unidentified developer or was downloaded from the internet. Choose **Open** to continue. If macOS blocks the application, open **System Settings → Privacy & Security**, scroll to the **Security** section, and choose **Open Anyway** next to the message about Amazon Quick.

**To install on Windows**

1. Download the `.exe` installer file.

1. Run the installer and follow the on-screen prompts.

1. After installation completes, launch **Amazon Quick** from the Start menu or desktop shortcut.

**Note**  
On first launch, Windows might display a SmartScreen prompt. Choose **More info** and then **Run anyway** to continue.

## Signing in
<a name="desktop-sign-in"></a>

The sign-in process depends on your account type. Amazon Quick on desktop is available for Plus and Enterprise accounts. Free accounts can try Amazon Quick on desktop during the first 30 days. When you open the application, you see the **Sign in to your Quick account** screen with two sign-in options.

**To sign in with a Plus account or Free trial**

1. Open the Amazon Quick desktop application.

1. On the sign-in screen, choose **Continue with** and select your preferred sign-in provider. Available providers include email, Amazon, Apple, Google, and GitHub.

1. You are redirected to the sign-in page. Enter your account credentials for the provider you selected.

1. Complete any multi-factor authentication prompts.

1. After authentication succeeds, the application loads the Home screen.

**Note**  
Enterprise sign-in must be configured by your organization's administrator before you can use it. If your administrator has not yet completed the setup, see [Setting up Amazon Quick on desktop for enterprise deployments](desktop-enterprise-setup.md).

**To sign in with an Enterprise account**

1. Open the Amazon Quick desktop application.

1. On the sign-in screen, choose **Continue with SSO**.

1. (Optional) Select your AWS Region from the list, or choose **Dynamic** to have the application detect your Region automatically.

1. You are redirected to your organization's identity provider. Enter your corporate credentials.

1. After authentication succeeds, the application loads the Home screen.

After you sign in, you can verify your authentication status in **Settings → Capabilities → Connectors**. The **Authentication** section displays your signed-in account and a green checkmark with the text "Signed in as {{your-email}} (Social)" or your organization's identity type.

## Onboarding and setup
<a name="desktop-onboarding"></a>

After you sign in for the first time, Amazon Quick guides you through an onboarding flow to connect your data sources. Connecting your data sources allows Quick to monitor what matters, prepare for meetings, and provide more relevant responses.

The onboarding flow presents the following categories of connections:


| Category | Description | Examples | 
| --- | --- | --- | 
| Email | Calendar and email for meeting prep and action items | Microsoft Outlook, Gmail, Google Calendar | 
| Messaging | Threads, DMs, and channels — triage what matters | Slack, Microsoft Teams | 
| Local files | Grant access to folders on your computer | Any folder on your machine | 

For each category, you can choose **Connect** to set up the connection immediately, or choose **Dismiss** to skip it. Each connection opens a sign-in page where you authenticate with the third-party service and grant Quick the required permissions.

**Tip**  
You can skip the onboarding flow entirely and connect your data sources later. To connect data sources at any time, open **Settings** in the sidebar, choose **Capabilities**, and select the **Connectors** tab. Amazon Quick supports connections including Slack, Microsoft Outlook, Microsoft Teams, Gmail, Google Calendar, Google Drive, and more. For a complete list of available connections, see [Connectors](connections-desktop.md).

## After setup
<a name="desktop-after-setup"></a>

After you complete the onboarding flow (or skip it), the Amazon Quick Home screen displays:
+ A **personalized greeting** based on the time of day.
+ The **chat input area** where you can start asking questions or requesting tasks.
+ **Connection setup cards** for any data sources you haven't connected yet. You can connect them at any time or dismiss them.
+ A **priority feed widget** showing the most important items from your connected services, with suggested actions you can take directly.

You're now ready to start using Amazon Quick on desktop. For an overview of the interface, see [Understanding the desktop interface](desktop-interface.md). To connect additional data sources, see [Connectors](connections-desktop.md).