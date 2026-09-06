

# Security, privacy, and architecture
<a name="desktop-security"></a>

The Amazon Quick desktop application is designed to keep your data private while providing full access to AI capabilities. The following sections describe how Amazon Quick on desktop handles security, privacy, and data storage.

**Important**  
Your data is never used for AI model training. AWS does not use your conversations, files, or personal context to train or improve AI models.

**Note**  
To control which Amazon Quick features your users can access after they sign in, configure custom permissions. For more information, see [Custom permissions](custom-permissions.md).

## How data is handled
<a name="desktop-local-architecture"></a>

The Amazon Quick desktop application processes your requests using AI models through API Gateway. The network calls Quick makes are to AI models and to your connected services (such as Slack, Outlook, or Gmail). Quick requires the following to be stored on your machine for the application to operate:
+ **Application configuration** – Settings, preferences, and connection state needed to run the desktop application.
+ **Cached content** – Temporary data for performance, including file indexes for your granted local folders.
+ **Credentials** – Authentication tokens for your connected third-party services.

## Data storage
<a name="desktop-data-storage"></a>

Application data is stored in the `~/.quickwork/` directory on macOS or `%USERPROFILE%\.quickwork\` on Windows.

## Folder permissions
<a name="desktop-folder-permissions"></a>

Amazon Quick on desktop uses OS-level sandboxing to control file access. Quick can only access folders that you explicitly grant permission to, and you can revoke access at any time. Each folder supports independent controls for keyword search indexing, semantic search indexing, and knowledge graph extraction. You can also set granular per-operation permissions for read and write operations.

**Note**  
Quick also has access to system temporary directories regardless of your folder permission settings. On Windows, these are `C:\TEMP`, `C:\TMP`, `\TEMP`, and `\TMP`. On macOS and Linux, these are `/tmp`, `/var/tmp`, and `/usr/tmp`.

To manage folder access and permissions, see [My Computer](desktop-settings.md#desktop-settings-my-computer).

## System tool permissions
<a name="desktop-system-tool-permissions"></a>

Amazon Quick on desktop includes system tools that provide core capabilities. Each tool can be individually toggled on or off and supports a three-tier permission model (Full Access, Read Only, or Ask Each Time) with granular per-operation controls. For a complete list of system tools and their permissions, see [System tools](system-tools-desktop.md).

## Connection security
<a name="desktop-connection-security"></a>

Amazon Quick on desktop uses industry-standard security practices for third-party service connections.
+ **OAuth 2.0** – Services such as Slack, Google, and Microsoft use OAuth 2.0 for authentication. Quick redirects you to the service's sign-in page, and the service returns an authorization token. Quick never sees or stores your third-party passwords.
+ **Independent connections** – Each connected service is managed independently. You can disconnect and reconnect any service at any time from **Settings** > **Capabilities** > **Connectors** without affecting other connections.
+ **Minimal permissions** – Quick requests only the permissions needed to provide its features for each connected service.

## Network access and required domains
<a name="desktop-network-access"></a>

The Amazon Quick desktop application makes outbound connections for discovery and data plane operations, remote configuration, application updates, and identity provider authentication. In restricted network environments, add the following domains to your allow list so that the application can operate.


| Category | Domains | Wildcard meaning | Purpose | 
| --- | --- | --- | --- | 
| Amazon Quick console | \*.quicksight.aws.amazon.com | \* = AWS Region (for example, us-east-1) | Web console, resource discovery | 
| Amazon Quick data plane | \*.dp.appintegrations.\*.prod.plato.ai.aws.dev | First \* = per-account cell ID. Second \* = AWS Region. | Inference, streaming, search | 
| Amazon Quick enterprise gateway | \*.desktop.enterprise.quick.aws.dev | \* = multi-level subdomain (<cell>.<stage>.<region>) | Enterprise account bidirectional streaming | 
| Remote configuration and updates | \*.cloudfront.net | \* = CloudFront distribution ID | Feature flags, application updates, Quick Apps content | 
| Telemetry | cognito-identity.\*.amazonaws.com | \* = AWS Region | Operational telemetry | 
| Identity provider | Customer-specific (for example, login.microsoftonline.com) | Not applicable | Enterprise SSO authentication | 

For strict proxy environments that can't use wildcards, you can determine the account-specific cell hostname after you first sign in. It follows the pattern `<cell-id>.dp.appintegrations.<region>.prod.plato.ai.aws.dev`, where `<cell-id>` is a stable per-account identifier and `<region>` is the account's home region.

If the application cannot sign in, load content, or update in a restricted environment, verify that these domains are reachable, and check your firewall and VPN settings.

## Privacy controls
<a name="desktop-privacy-controls"></a>

Amazon Quick on desktop provides privacy controls that let you manage whether Quick learns from your conversations, searches your conversation history, and extracts entities from connected services. You can also view, edit, and delete individual memories. To configure privacy settings, see [My Context](desktop-settings.md#desktop-settings-my-context).

## Clearing all data
<a name="desktop-clearing-data"></a>

If you need to completely reset Amazon Quick on desktop, you can use the **Clear all data** option in **Settings** > **Customization** > **Danger zone**. This action is irreversible and removes all conversations, knowledge graph data, saved credentials, and user preferences. For more information, see [Danger zone](desktop-settings.md#desktop-settings-danger-zone).