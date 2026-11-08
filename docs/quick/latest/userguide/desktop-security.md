

# Security, privacy, and architecture of Amazon Quick on desktop
<a name="desktop-security"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators  | 

Amazon Quick on desktop is a native application that runs on the user's device and connects to the Amazon Quick service in the cloud. The service processes each request and stores the user's data in your Amazon Quick account. The application gives the service access to the device, such as the folders that the user grants.

AWS doesn't use your conversations, files, or personal context to train or improve AI models.

Responsibility for security follows these trust boundaries:
+ The user's device, which your organization manages.
+ The Amazon Quick service, which AWS manages.
+ Connected services, which your organization or a third party manages.

## Components
<a name="desktop-architecture"></a>

The desktop application and the agent runtime handle each chat request.

### Desktop application
<a name="desktop-architecture-device"></a>

The desktop application runs on the user's device. It connects to the Amazon Quick service and runs local tools when the agent runtime calls them. Local tools include folder access, browser automation, code execution, local connectors, and coding agents, and each one runs with the operating system permissions of the signed-in user.

Code execution runs in an operating system sandbox with no network access, either in the agent runtime or on the user's device. Amazon Quick updates the libraries in the agent runtime. The libraries on the device update with the desktop application.

### Agent runtime
<a name="desktop-architecture-agent-runtime"></a>

The agent runtime is the cloud environment that processes each chat request. It runs on [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) and uses a model hosted on [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html). Each user's agent runtime runs in a dedicated, single-tenant environment. AgentCore isolates each session in its own microVM. For more information, see [AgentCore Runtime session isolation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html).

To complete a request, the agent runtime calls tools, such as [system tools](system-tools-desktop.md) and [cloud connectors](connections-desktop.md). It reads the user's data and the [spaces](spaces-desktop.md), [knowledge bases](knowledge-base-integrations.md), and [datasets](working-with-datasets.md) that the user can access. It enforces resource permissions, plus document access control lists (ACLs) and row- and column-level security where they're configured.

### Example: a chat request
<a name="desktop-architecture-example"></a>

The following steps show how the components work together for one chat request. Administrative requests, such as account and permission changes, follow a different path.

1. The desktop application sends the prompt and any attachments to Amazon Quick with the user's authentication token.

1. The agent runtime processes the prompt with the model.

1. Amazon Quick checks each tool call against the administrator, connector owner, and user permissions before the call runs.

1. The agent runtime saves the conversation, including the prompt, response, tool calls, and citations, encrypted at rest.

1. Amazon Quick returns the response to the desktop application.

## Network connections
<a name="desktop-architecture-network"></a>

The desktop application opens every network connection itself, so the device needs only outbound firewall rules. It connects over HTTPS and WebSocket Secure on port 443 with Transport Layer Security (TLS) 1.2 or later. The agent runtime sends local tool calls over the WebSocket connection that the application opened.

During sign-in, the application opens a local port to receive the identity provider's response from the browser, and it closes the port when sign-in completes. For more information, see [Sign-in and credentials](#desktop-security-sign-in).

Calls to cloud connectors and data sources start in the Amazon Quick service and go over the public internet or a virtual private cloud (VPC) connection. They don't come from the user's device. For information about connecting to data sources in your VPC, see [Configuring VPC connections in Amazon Quick Sight](working-with-aws-vpc.md).

For information about proxies, see [Proxy support](desktop-enterprise-managed-deployment.md#desktop-enterprise-proxy-support). For information about traffic inspection, see [Trusting a corporate certificate authority](desktop-enterprise-mdm.md#desktop-mdm-tls).

### Network access and required domains
<a name="desktop-network-access"></a>

The application connects to Amazon Quick for discovery and data-plane operations, remote configuration, updates, and identity provider sign-in. In restricted networks, add the following domains to your allowlist.


| Category | Domain | Wildcard meaning | Purpose | 
| --- | --- | --- | --- | 
| Amazon Quick console | \*.quicksight.aws.amazon.com | \* = AWS Region (for example, us-east-1) | Web console, resource discovery | 
| Amazon Quick data plane | \*.dp.appintegrations | First \* = per-account cell ID; second \* = AWS Region | Inference, streaming, search | 
| Amazon Quick desktop sign-in | `<tenant-id>.<region>.enterprise.quick.aws.com`<br />`<tenant-id>.*.<region>.enterprise.quick.aws.com` | \* = cell ID, which can change | Desktop sign-in, and token issuance and renewal | 
| Amazon Quick enterprise resource server for Amazon Quick on desktop | `<tenant-id>.<region>.enterprise.quick.aws.com`<br />`<tenant-id>.*.<region>.enterprise.quick.aws.com` | \* = cell ID, which can change | Desktop API access | 
| Remote configuration and updates | \*.cloudfront.net | \* = Amazon CloudFront distribution ID | Feature flags, application updates, Apps in Amazon Quick content | 
| Telemetry | cognito-identity.\*.amazonaws.com | \* = AWS Region | Operational telemetry | 
| Identity provider | Customer-specific (for example, login.microsoftonline.com) | Not applicable | Sign-in through your organization's identity provider | 
+ For strict proxy environments that can't use wildcards, you can determine the account-specific cell hostname after you first sign in. It follows the pattern `<cell-id>.dp.appintegrations.<region>`. In that pattern, `<cell-id>` is a stable identifier for each account, and `<region>` is the account's home Region.
+ If your organization inspects encrypted traffic, add the inspection certificate authority to the operating system trust store, or exclude the Quick domains from inspection. The application doesn't pin certificates, so it trusts any certificate authority in that store.
+ In the desktop sign-in and resource server domains, replace `<tenant-id>` with your tenant ID and `<region>` with your account's home Region. Allow both patterns for each domain. To find your tenant ID, do one of the following:
  + In the Amazon Quick console, go to **Inbound connectors**, choose the **Quick Desktop** tab, and open the desktop connector.
  + Use the Amazon Quick API. Call `DescribeInboundConnector`, `ListInboundConnectors`, `DescribeAccessControlApplication`, or `ListAccessControlApplications`.

## Sign-in and credentials
<a name="desktop-security-sign-in"></a>

The desktop application doesn't store usernames or passwords, and it doesn't receive AWS credentials. It keeps its sign-in tokens in the operating system credential vault, which is the macOS Keychain or Windows Credential Manager. It renews the tokens in the background, and each profile keeps its own token. When a token expires or is revoked, the user signs in again.

During sign-in, the application listens on `http://localhost:18080` for the response from the browser. The port is open only while sign-in is in progress. If your endpoint security software blocks local listeners, allow this port.

Security scanning tools can flag this redirect URI because it uses HTTP. The traffic stays on the device. An application that intercepts the authorization code can't exchange it for tokens without the Proof Key for Code Exchange (PKCE) verifier. Only the desktop application holds that verifier.

## Where data is stored
<a name="desktop-architecture-data"></a>

Amazon Quick stores data in your Amazon Quick account and on the user's device.

### In your Amazon Quick account
<a name="desktop-security-data-handling"></a>

Amazon Quick keeps each user's conversations, memory, knowledge graph, library, skills, and indexed folder content in your Amazon Quick account. Each user's data is separate from other users' data. Amazon Quick encrypts it at rest. You can register an AWS Key Management Service (AWS KMS) [customer managed key](customer-managed-keys.md) for the resource types that page lists.

### On the user's device
<a name="desktop-security-data-storage"></a>

The desktop application stores its configuration in `~/.quickwork/` on macOS or `%USERPROFILE%\.quickwork\` on Windows. This includes settings, folder permissions, local connector and coding agent configuration, and sandbox settings. The application also keeps file-sync metadata, browser session state, logs, and cached content, such as previews of opened files.

Your organization is responsible for protecting this data. The application doesn't encrypt the directory itself, so turn on the operating system's full-disk encryption, such as FileVault on macOS or BitLocker on Windows. Any process that runs as the same operating system user can read the directory. Model Context Protocol (MCP) values that the user marks as secret go to the operating system keychain, and the application stores other values in plaintext.

Signing out or uninstalling the application doesn't remove all local data.

## Administrator and user controls
<a name="desktop-admin-user-controls"></a>

The administrator, the connector owner, and the user each set controls for a tool call. They apply in that order, and each role can only narrow what the role before it allows. The connected service then authorizes the call with the user's identity or the connector's credential.

### Administrator controls
<a name="desktop-admin-controls"></a>

Administrators set controls in the Amazon Quick account, which apply to every surface, and through device management. You can do the following:
+ [Turn on desktop access](desktop-enterprise-setup.md#desktop-enterprise-turn-on) and choose the [sign-in method](desktop-enterprise-advanced-idp.md).
+ Allow or deny desktop capabilities with [custom permissions](custom-permissions.md), and deny new capabilities with [Deny by Default](custom-permissions-governance.md).
+ Set [managed policies](desktop-enterprise-managed-deployment.md#desktop-enterprise-mdm-policies) and control [application updates](desktop-enterprise-managed-deployment.md#desktop-enterprise-updates).
+ Cap usage with [limit profiles](limit-profiles.md).
+ Configure [AI guardrails](guardrails.md).
+ Deliver chat logs with [vended logs](monitoring-cloudwatch-logs.md).
+ Encrypt data with [customer managed keys](customer-managed-keys.md).
+ Block or warn about files based on sensitivity labels with [data loss prevention](data-loss-prevention.md).

To revoke one user's access, remove or delete the user. For more information, see [User lifecycle and data handling in Amazon Quick](user-lifecycle-data-handling.md). To revoke desktop access for a group or for every user, restrict the **Quick desktop** capability with custom permissions.

### Connector owner controls
<a name="desktop-connector-owner-controls"></a>

The owner of a cloud connector decides who can use it. The owner sets each action to **Let Users Choose** or **Always Ask**, or turns the action off. For more information, see [Tool permissions](connector-tool-permissions.md).

#### Connection security
<a name="desktop-security-connection-security"></a>

The agent runtime invokes cloud connectors from your Amazon Quick account, not from the device. Amazon Quick stores each connector's tokens in a token vault in your account. For more information, see [Authentication methods](quick-action-auth.md).

Each connected service has its own connection, so users can disconnect and reconnect one service without affecting the others. Quick requests only the permissions that each service needs.

### User controls
<a name="desktop-user-controls"></a>

Users set the following controls for their own work:
+ Which folders the agent can reach, and whether files are uploaded for [indexing](knowledge-desktop.md#knowledge-indexing-options). Granting a folder doesn't upload its files.
+ Which files to upload to [spaces](spaces-desktop.md) or attach to [chat messages](working-with-chat-desktop.md#desktop-attachments).
+ The [access level](system-tools-desktop.md#desktop-settings-manage-permissions) for each system tool.
+ Whether write actions need approval, when the connector owner sets the action to **Let Users Choose**.
+ Which [MCP servers](connections-desktop.md#desktop-mcp-servers) and [coding agents](connections-desktop.md#desktop-coding-agents) to add.
+ Whether Quick learns from conversations, set in [privacy controls](desktop-settings.md#desktop-privacy-controls) and [incognito mode](working-with-chat-desktop.md#desktop-incognito-mode).

Local connectors belong to the user who adds them, and only that user can use them. Administrators can allow or deny local connectors and coding agents with custom permissions. They can't see which ones a user adds.

## AI usage
<a name="desktop-security-ai-usage"></a>

The desktop application doesn't host or run models. Inference runs in the agent runtime, and Amazon Quick hosts its embedding models on Amazon SageMaker AI. For information about the controls that apply to model use, see [AI guardrails](guardrails.md) and [AI and agent security](sec-agentic-security.md). Inference and web search can run in other AWS Regions. For the current Regions, see [AWS Regions, websites, IP address ranges, and endpoints](regions.md). Use of the service is subject to the [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/).

## Monitoring and auditing
<a name="desktop-monitoring"></a>

You audit Amazon Quick on desktop with the same tools as the rest of Amazon Quick. AWS CloudTrail records API calls, and it records connector actions when you turn on data events. For more information, see [Monitoring Amazon Quick using CloudTrail](monitoring-cloudtrail.md).

Vended logs deliver chat conversations, including incognito conversations, to a destination in your AWS account. For more information, see [Monitoring Amazon Quick using CloudWatch Logs](monitoring-cloudwatch-logs.md). Users can also export diagnostic logs from the device. For more information, see [Exporting diagnostics](desktop-troubleshooting.md#desktop-ts-diagnostics).

## Data retention and deletion
<a name="desktop-data-retention"></a>

Amazon Quick sets the retention periods for data in your Amazon Quick account. For information about the periods, see [Amazon Quick desktop usage limits](usage-limits-desktop.md). You set retention for the logs that you deliver to your own destinations. For more information, see [Security best practices](best-practices-security.md). For information about what happens to a user's data when you remove the user, see [User lifecycle and data handling in Amazon Quick](user-lifecycle-data-handling.md).