

# Security, privacy, and architecture
<a name="desktop-security"></a>

Amazon Quick on desktop is designed to keep your data private while providing full access to AI capabilities.

Your data is never used for AI model training. AWS does not use your conversations, files, or personal context to train or improve AI models.

## How data is handled
<a name="desktop-security-data-handling"></a>

Amazon Quick runs in the cloud. Your conversations, memory, knowledge graph, agent-produced files (your Library), and the index of content you make searchable are kept per user in your Amazon Quick account, isolated from other users. The desktop application stores only what it needs to operate locally: application configuration (settings, preferences, and connection state), the folders you have granted access to and their local settings, locally configured MCP and coding-agent servers, and your sign-in credentials (authentication tokens, held in your operating system's credential vault).

## Data storage
<a name="desktop-security-data-storage"></a>

Local application data, configuration, folder permissions, locally configured MCP and coding-agent servers, and sandbox settings, is stored in `~/.quickwork/` on macOS or `%USERPROFILE%\.quickwork\` on Windows. Your conversations, memory, and knowledge graph are not stored here; they are kept in your Amazon Quick account.

## Folder permissions
<a name="desktop-security-folder-permissions"></a>

Quick uses operating-system sandboxing to control file access. It accesses only folders you explicitly grant, and you revoke access at any time. Each folder supports independent controls for keyword search, semantic search, and knowledge graph extraction, plus granular per-operation permissions.

Quick also has access to system temporary directories regardless of folder permissions. On Windows these are `C:\TEMP`, `C:\TMP`, `\TEMP`, and `\TMP`. On macOS and Linux these are `/tmp`, `/var/tmp`, and `/usr/tmp`.

## System tool permissions
<a name="desktop-security-tool-permissions"></a>

Amazon Quick on desktop governs three kinds of capabilities with the same permission model: system tools that provide core capabilities, connectors to third-party services such as Slack, Outlook, and Gmail, and local tools that run on your device. You can turn each capability on or off. Each supports a three-tier permission model, Always Allow, Ask Each Time, or Always Deny, with granular per-operation controls (see [System tools](system-tools-desktop.md)).

Quick stores your permission choices and applies them consistently whenever an agent acts on your behalf, including scheduled agents. An agent can only take actions you have authorized, and you can review or change these permissions at any time.

## Connection security
<a name="desktop-security-connection-security"></a>
+ OAuth 2.0: connected services authenticate with OAuth 2.0; Quick never sees or stores your third-party passwords.
+ Independent connections: each service is managed independently; you disconnect and reconnect any service without affecting others.
+ Minimal permissions: Quick requests only the permissions needed for each service.

## Privacy controls
<a name="desktop-privacy-controls"></a>

Quick provides controls for whether it learns from your conversations, searches your conversation history, and extracts entities from connected services. You view, edit, and delete individual memories (see [My context](desktop-settings-my-context.md)).

## Network access and required domains
<a name="desktop-network-access"></a>

The application makes outbound connections for discovery and data-plane operations, remote configuration, application updates, and identity-provider authentication. In restricted networks, add the required Amazon Quick domains to your allow list.


| Category | Domain | Wildcard meaning | Purpose | 
| --- | --- | --- | --- | 
| Amazon Quick console | \*.quicksight.aws.amazon.com | \* = AWS Region (for example, us-east-1) | Web console, resource discovery | 
| Amazon Quick data plane | \*.dp.appintegrations.\*.prod.plato.ai.aws.dev | First \* = per-account cell ID; second \* = AWS Region | Inference, streaming, search | 
| Amazon Quick enterprise gateway | \*.desktop.enterprise.quick.aws.dev | \* = multi-level subdomain (<cell>.<stage>.<region>) | Enterprise account bidirectional communication | 
| Remote configuration and updates | \*.cloudfront.net | \* = CloudFront distribution ID | Feature flags, application updates, Apps in Amazon Quick content | 
| Telemetry | cognito-identity.\*.amazonaws.com | \* = AWS Region | Operational telemetry | 
| Identity provider | Customer-specific (for example, login.microsoftonline.com) | Not applicable | Enterprise SSO authentication | 

For strict proxy environments that cannot use wildcards, you can determine the account-specific cell hostname after you first sign in. It follows the pattern `<cell-id>.dp.appintegrations.<region>.prod.plato.ai.aws.dev`, where `<cell-id>` is a stable per-account identifier and `<region>` is the account's home region. If your organization inspects encrypted traffic, the operating-system trust store must trust the inspection certificate authority, or the Quick domains must be excluded from inspection (see [Setting up Amazon Quick on desktop for enterprise deployments](desktop-enterprise-setup.md)).

## Clearing all data
<a name="desktop-clearing-data"></a>

To completely reset Quick, use Clear all data in Settings, on the Advanced tab. This is irreversible and removes all conversations, knowledge graph data, saved credentials, and preferences.