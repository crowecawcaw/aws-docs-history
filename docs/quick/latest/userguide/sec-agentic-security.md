# AI and agent security in Amazon Quick

Amazon Quick includes AI capabilities that read content, take actions, and run automated
workflows. These capabilities introduce properties that differ from traditional BI features.
Use this page to understand what makes these capabilities different, how to apply the
available controls, and where those controls have limits. For the corresponding security
checklist, see
[Security in Quick](best-practices-security.md "best-practices-security.md").

## What makes these capabilities different

Three properties distinguish the AI and agent capabilities from traditional features
such as dashboards and datasets.

- **The assistant reads content your users did not
  author** – Knowledge bases, web search, third-party research providers,
  and connectors all supply content that originates outside your organization. Any content
  from outside your trust boundary is a potential source of adversarial input. For the
  full list of content sources, see
  [Two-condition model for adversarial content risk](#sec-agentic-security-two-condition-model "#sec-agentic-security-two-condition-model").
- **The assistant can take actions with effects outside the
  service** – Through connectors, Model Context Protocol (MCP) server
  tools, and web search queries, the assistant can cause changes in external systems. For the full inventory of
  outbound paths, see
  [Outbound connections and data egress in Amazon Quick](outbound-connections.md "outbound-connections.md").
- **Some capabilities run without a person
  watching** – Automated workflows execute on a schedule or in response
  to events, without an interactive user session. This changes how you evaluate the risk
  of each action. For more information, see
  [Autonomy and identity](#sec-agentic-security-autonomy-identity "#sec-agentic-security-autonomy-identity").

None of these properties is unique to Amazon Quick. They are common across AI-powered
services. Together, they mean that the same security review you apply to a traditional
dashboard does not fully address the risk profile of an agent or automated workflow.

## Two-condition model for adversarial content risk

The risk of acting on adversarial content requires two conditions to be present at the
same time:

1. The assistant can read content from outside your trust boundary.
2. The assistant can take a consequential action.

Narrowing either condition reduces your exposure. A trust boundary is the set of
content sources that you consider safe and under your control. Any content that enters the
assistant's context from outside that boundary is untrusted by definition.

### Read surface

The following sources can supply content to the assistant's context. Each is a point
where content you did not author can enter.

- Knowledge base and index retrieval (including bring-your-own-index from
  Amazon Q Business)
- Files uploaded to spaces
- Files uploaded in chat
- Web search results
- Third-party research provider data
- Content returned by action connectors
- Content returned by remote MCP server tools

Retained context also contributes to the read surface. Past conversations and, on
Quick Desktop, entities extracted from connected data sources persist across
sessions and can inform later responses. For more information, see
[Memory and retained context](#sec-agentic-security-memory "#sec-agentic-security-memory").

Not all of these sources carry equal risk. Files uploaded by your own users in chat
are within your trust boundary. Content returned by a web search query to the open
internet is not. Evaluate each source against your trust boundary when you review your
configuration.

### Action surface

The following paths allow the assistant to cause effects outside Amazon Quick. Each is
a point where a consequential action can occur.

- On-demand actions through third-party and AWS service connectors
- Automated workflow actions through service-level connectors
- Remote MCP server tool invocations
- Web search queries (send context externally)
- Quick Apps bridge API calls (sandboxed)
- Code execution on Quick Desktop (file effects on the user's machine,
  within configured folder permissions; other code execution surfaces are sandboxed
  without external reach)
- Scheduled agent execution

For the complete inventory of outbound paths, including what data can leave through
each one and who controls it, see
[Outbound connections and data egress in Amazon Quick](outbound-connections.md "outbound-connections.md").

## Autonomy and identity

Amazon Quick supports two invocation models with different security characteristics. The
same connector or action carries different risk depending on which model invokes it.

### On-demand actions

On-demand actions are user-initiated and interactive. They authenticate with the
individual user's personal credentials and act as the invoking user. Each on-demand
action is bounded by that user's connector permissions, and a person is present in the
session when it executes.

### Automated workflows

Automated workflows are scheduled or event-triggered and non-interactive. They
authenticate at service level rather than as an individual user. Because they use
service-level authentication, they are not bounded by an individual user's connector
permissions and they run unattended.

The consequence for your review is that an automated workflow can reach any
resource the service-level credential permits, regardless of which user created the
workflow. No interactive session is present to observe what happens during execution.
An action can carry limited risk when you invoke it on demand. The same action can carry
broader risk when an automated workflow invokes it with service-level reach.

### Adding a review step

To add a review step to an automated workflow, use the human-in-the-loop task
center. For workflows where you want a person to approve an action before it executes,
the task center pauses execution and collects approval before the workflow continues.
For more information, see
[Human-in-the-loop task center](hitl-task-center.md "hitl-task-center.md").

## Human oversight

You can apply human approval gates at five points in the lifecycle of AI and agent
capabilities. Together, they form a layered model for human oversight.

1. **Capability approval (Deny by Default)** –
   New AI capabilities in a restricted category are denied on launch until an
   administrator explicitly allows them. This gate applies before a capability is
   available to any user. For more information, see
   [Deny by Default](custom-permissions-governance.md "custom-permissions-governance.md").
2. **Build-time consent (Apps integration consent)**
   – When the Apps agent adds an integration to an app (action connector, space,
   dashboard visual, or AI inference), it prompts the author for approval. The published
   app never includes unapproved integrations, and app viewers inherit the approved
   integration scope rather than broader access. For more information, see
   [Integration consent model](security-sandbox-apps.md#apps-integration-consent "security-sandbox-apps.md#apps-integration-consent").
3. **Share approval (Flows)** –
   Custom permissions control which users can review and approve flow sharing
   requests, and whether creators can share flows without approval. Administrators
   configure these capabilities through custom permissions profiles. For more
   information, see
   [Custom permissions](custom-permissions.md "custom-permissions.md").
4. **Runtime review (human-in-the-loop task center)**
   – For workflows where you want a person to approve an action before it
   executes, the human-in-the-loop task center pauses execution and collects approval.
   This gate is optional and per-workflow. For more information, see
   [Human-in-the-loop task center](hitl-task-center.md "hitl-task-center.md").
5. **Per-action user control (Desktop, Preview)**
   – On Quick Desktop, each system tool can be enabled or disabled
   individually and supports a three-tier permission model –
   **Full Access**, **Read Only**, and
   **Ask Each Time** – with granularity for each operation.
   **Full Access** runs operations without prompting for confirmation.
   **Ask Each Time** confirms every
   operation. This places an approval decision in your hands at the moment of each
   action, for the tools you have enabled. For more information, see
   [Access levels](system-tools-desktop.md#system-tools-access-levels "system-tools-desktop.md#system-tools-access-levels") and
   [Manage permissions](desktop-settings.md#desktop-settings-manage-permissions "desktop-settings.md#desktop-settings-manage-permissions").

Where a per-action prompt applies, it is a user-configurable choice. On Desktop, you
set a tool to **Ask Each Time** to confirm every operation, or to
**Full Access** to run without
prompting. In the web experience, on-demand actions execute when you trigger them, and
automated workflows are non-interactive by design – the gates at capability,
build, and share time do the work there.

Per-action confirmation is therefore available but not universal. It depends on the
surface and on how you configure each tool.

For an automated workflow running unattended, no interactive session exists to
confirm anything. For those workflows, the review effort belongs at approval time, when
you evaluate what the automation can reach and what it can do.

## Controls and limits for AI and agent capabilities

Amazon Quick provides the following controls relevant to AI and agent capabilities. Each
control is described together with its limits.

### Retrieval permission enforcement

For knowledge bases with document-level access control list (ACL) support
enabled, Amazon Quick enforces
synchronized document permissions on every retrieval. Supported integrations include
Amazon S3, Google Drive, Microsoft SharePoint, Atlassian Confluence Cloud, and Microsoft
OneDrive. If Amazon Quick cannot evaluate document permissions for a query, it returns no
documents rather than unfiltered results.

**Limit** – ACL enforcement applies only to
knowledge bases created with ACL support. Knowledge bases created without ACL support
do not enforce document-level permissions. ACL configuration is permanent and cannot be
changed after creation. For more information, see
[Best practices for managing ACLs in knowledge bases](acl-best-practices-kb.md "acl-best-practices-kb.md").

### Custom permissions and deny by default

Custom permissions restrict the capabilities available to each role. They cannot
grant capabilities that a user does not already have. The most specific level wins:
user-level overrides role-level, which overrides account-level. The deny-by-default
option for the AI capability category restricts all AI capabilities, current and
future, so that new capabilities are denied on launch day until you explicitly allow
them.

**Limit** – Custom permissions require an
Enterprise subscription. They scope down access but cannot extend it. For more
information, see
[Custom permissions](custom-permissions.md "custom-permissions.md") and
[Deny by Default](custom-permissions-governance.md "custom-permissions-governance.md").

### Organization-level controls and their limits

Custom permissions apply at the account level, and an administrator of that account
can change them. If you manage many accounts with AWS Organizations, you can add
organization-level controls that individual account administrators cannot override.
These controls act on AWS API operations and account sign-up. Understand what they
reach and what they do not.

- **Restrict who signs up for Quick**
  – A service control policy (SCP) controls which accounts, editions, and
  identity types can create a Quick subscription, so new accounts cannot
  start a subscription outside your approved set. For more information, see
  [Using service control policies to restrict Amazon Quick sign-up options](security-scp-admin.md "security-scp-admin.md").
- **Restrict the management API operations** –
  An SCP denies the Quick API operations that create and manage agents,
  flows, spaces, and knowledge bases. Where the policy applies, principals cannot create
  those resources through the AWS Command Line Interface, the AWS SDKs, or
  CloudFormation.
- **Restrict AI feature availability with custom permissions,
  not SCPs** – SCPs act on AWS API operations and account
  sign-up. They do not control which AI features a user sees or can use within the
  product. To restrict AI features for your users, use custom permissions with the
  deny-by-default option for the AI capability category. For more information, see
  [Deny by Default](custom-permissions-governance.md "custom-permissions-governance.md").

**Limit** – Each control enforces a different
layer. An SCP controls account sign-up and API-based management across your organization,
and no account administrator can override it. Custom permissions control which AI
features your users can use, and an account administrator can change them. To detect a
custom permissions change, record the Quick management API operations with
AWS CloudTrail and review them. For more information, see
[Incident response, logging, and monitoring in Amazon Quick](incident-response-logging-and-monitoring.md "incident-response-logging-and-monitoring.md").

### Tool and connector supply chain

Tools reach the AI assistant only through integrations that an administrator
creates. MCP integrations require an Enterprise subscription. The integration
model restricts the transport and discovery path for external tools.

- Only remote MCP servers are supported. Local stdio connections are not
  supported.
- During connection, Amazon Quick discovers and registers the tools that the MCP
  server provides. After discovery completes, each tool is listed as an action that
  you can review and turn on. Tools do not become available automatically.
- You can connect to private MCP servers through a VPC connection that has
  network access to the server.
- Administrators can restrict individual connectors through custom permissions.
  Each connector supports three permissions: **Create and Update action**,
  **Share action**, and **Use action**. For more information, see
  [Custom permissions](custom-permissions.md "custom-permissions.md").

For more information about configuring an MCP integration, see
[Model Context Protocol (MCP) integration](mcp-integration.md "mcp-integration.md").

**Limit** – Authentication options vary by
connector type. For remote MCP servers, agent-to-agent connectors, and generic HTTP
connectors, connecting without authentication is a selectable option. The integrity of
a connection depends on how it is configured. The service does not evaluate the
trustworthiness of a third-party MCP server or the behavior of the tools it
exposes. That assessment is yours to make.

### Guardrail screening and blocked words

Built-in content safety screening checks user requests for harmful content,
including hate speech, insults, sexual content, violence, and misconduct. These checks
also assess user requests for prompt attacks. You can configure up to 50 blocked words
and phrases that Amazon Quick checks against both user requests and generated
responses.

**Limit** – These controls help reduce risk.
However, they do not replace your responsibility to configure access, permissions,
agents, flows, and data sources for your use case. Blocked-word checks use exact-match
string comparison, not semantic analysis, and are limited to 50 entries of up to 36
characters each. Blocked-word checks apply only to chat agents and flows in the
Amazon Quick web experience. For more information, see
[AI guardrails in Amazon Quick](guardrails.md "guardrails.md").

### Code execution isolation

The AI assistant can write and run Python code on four surfaces. Each surface runs
code in a sandboxed environment designed to contain the code's effects. The surfaces
differ in where code runs and what it can reach.

- **Quick Desktop** – Code runs
  in an OS-level sandbox (macOS Seatbelt or Windows AppContainer) on the user's
  machine. File access inside the sandbox follows the folder permissions the user
  configures, and a persistent namespace carries variables across code runs within a
  conversation. Pre-installed Python packages only; package installation
  (`pip install`) is not supported. For more information, see
  [Code Execution](system-tools-desktop.md#system-tool-code-execution "system-tools-desktop.md#system-tool-code-execution").
- **Web experience chat** – Code runs in an
  isolated, service-managed sandbox with no internet access. Outbound network
  requests from the sandbox fail. The sandbox does not persist beyond the
  conversation.
- **Automated workflows (Quick Automate)**
  – Code actions and custom agent code run within a restricted Python
  environment. Code actions are not the path for reaching external systems: external
  API calls belong to REST API integrations, and file system or database access
  belongs to the appropriate integrations. For more information, see
  [Code](actions-code.md "actions-code.md").
- **Office extensions** – The assistant
  creates and executes code within the Office application sandbox (Outlook, Excel,
  Word, and PowerPoint). For more information, see
  [Connect Amazon Quick to your existing tools with extensions](working-with-extensions-detail.md "working-with-extensions-detail.md").

The Execute code locally capability in custom permissions restricts code
execution in Quick Desktop for the users a profile applies to. Extension
capabilities, including code execution within Office applications,
can be restricted through extension access controls. For more information, see
[Custom permissions](custom-permissions.md "custom-permissions.md") and
[Extension access](extension-access.md "extension-access.md").

**Limit** – On Desktop, the sandbox always has
access to the system temporary directories regardless of the configured folder
permissions. On Desktop, the persistent namespace means data loaded by an earlier code
run remains available to later code runs in the same conversation. Sandboxing contains
what code can reach; it does not evaluate what the code does with content already in
the conversation context. Review generated code output like any other assistant
output.

### Logging and audit coverage

AWS CloudTrail records API-level activity (who did what). Vended logs record
conversational content (what was said and what was responded). Together, they provide
after-the-fact visibility into AI and agent activity.

**Limit** – Logging does not prevent any
action. It provides visibility after the fact. The service does not include real-time
alerting; you must configure CloudWatch alarms separately if you need near-real-time
notification. Vended
chat logs do not capture the content of source documents that retrieval returns. For
more information, see
[Incident response, logging, and monitoring in Amazon Quick](incident-response-logging-and-monitoring.md "incident-response-logging-and-monitoring.md").

### Limits stated plainly

The following limitations apply to the AI and agent capabilities in
Amazon Quick:

- **Screening reduces risk but does not replace
  configuration** – Built-in screening and guardrails help reduce
  risk. They do not replace your responsibility to configure access, permissions,
  agents, flows, and data sources for your use case.
- **No universal human review requirement**
  – Human review is not a system-wide requirement for actions. Per-action
  confirmation is available where a tool is configured for it (on Desktop, through the
  **Ask Each Time** access level), and the human-in-the-loop task
  center is available for
  workflows where you choose to add a review step. However, on-demand actions in the
  web experience execute immediately, and automated workflows execute without user
  intervention.
- **Authentication options vary by connector
  type** – The authentication methods available depend on the
  connector type. For remote MCP servers, agent-to-agent connectors, and generic HTTP
  connectors, connecting without authentication is a selectable option.

## Memory and retained context

Chat memory personalizes responses by remembering your preferences, context, and past
interactions. Chat agents reference stored information to provide more relevant responses
without you repeating information in every conversation. For more information, see
[Memory and response personalization](using-quick-chat.md#chat-memory "using-quick-chat.md#chat-memory").

On Quick Desktop, a My Context surface provides a Knowledge graph tab
that shows entities and relationships extracted from connected data sources, and a Memory
tab that shows facts, procedures, and patterns learned from conversations. For more
information, see
[My Context](desktop-settings.md#desktop-settings-my-context "desktop-settings.md#desktop-settings-my-context").

### Why retained context matters for security

Retained context is part of the read surface described in
[Two-condition model for adversarial content risk](#sec-agentic-security-two-condition-model "#sec-agentic-security-two-condition-model"). Unlike a single
conversation, retained context persists across sessions. Information that the assistant
remembers from a past interaction can influence responses and actions in a future
session.

### Controls

- **Isolation** – Memories are specific to
  the individual user and are not shared with other users.
- **User control** – You can review your
  chat memory through **Conversation History**. On Desktop, you can additionally manage
  whether Quick learns from your conversations, searches your
  conversation history, and extracts entities from connected services. You can also
  view, edit, and delete individual memories. For more information, see
  [Privacy controls](desktop-security.md#desktop-privacy-controls "desktop-security.md#desktop-privacy-controls").
- **Full reset (Desktop)** – The
  **Clear all data** option irreversibly removes all conversations,
  knowledge graph data, saved
  credentials, and user preferences. For more information, see
  [Clearing all data](desktop-security.md#desktop-clearing-data "desktop-security.md#desktop-clearing-data").
- **Administrator control** – Custom
  permissions include capabilities that restrict building and managing engrams
  (profiles of a user's writing style and patterns) and creating and accessing
  knowledge memory in Quick Desktop. For more
  information, see
  [Custom permissions](custom-permissions.md "custom-permissions.md").
- **No training** – Quick does
  not use your conversations, files, or personal context to train or improve AI
  models.

### Limitations

- Chat memory is not supported for accounts configured with AWS KMS customer
  managed keys. An organization that requires customer managed keys does not get chat
  memory. For more information, see
  [Memory and response personalization](using-quick-chat.md#chat-memory "using-quick-chat.md#chat-memory").
- Quick Desktop is in Preview. The My Context surface, the
  Knowledge graph tab, the ability to view, edit, and delete individual memories, and
  the **Clear all data** option are Desktop features. In the web
  experience, you review
  chat memory through **Conversation History**. Confirm which
  controls are available on the surface you deploy rather than assuming parity between
  Desktop and web.

## Where to go next

- [Security in Quick](best-practices-security.md "best-practices-security.md") – The security checklist with
  actionable practices for configuring Amazon Quick.
- [Outbound connections and data egress in Amazon Quick](outbound-connections.md "outbound-connections.md") – The complete inventory of outbound
  paths, what data can leave through each, and who controls it.
- [AI guardrails in Amazon Quick](guardrails.md "guardrails.md") – Built-in
  content safety screening and administrator-configured blocked words.
- [Custom permissions](custom-permissions.md "custom-permissions.md") – Role-based capability restriction
  and deny-by-default governance.
- [Best practices for managing ACLs in knowledge bases](acl-best-practices-kb.md "acl-best-practices-kb.md") – Document-level access control
  for knowledge bases, including fail-closed retrieval behavior.
