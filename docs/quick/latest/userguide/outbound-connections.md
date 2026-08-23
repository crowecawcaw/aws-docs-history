# Outbound connections and data egress in Amazon Quick

Stored customer data in Amazon Quick does not leave its AWS Region. The
documented exceptions are AI inference processed within a defined geography (cross-Region
inference) and the outbound paths that you or your administrator enables. Every path
described on this page is either off by default or requires explicit configuration before
data can leave the service boundary.

For related guidance on evaluating these paths before you enable them, see
[Security in Quick](best-practices-security.md "best-practices-security.md").

Code execution is not an outbound path in the web experience. Python code that the AI
assistant writes and runs in web chat executes in an isolated sandbox with no internet
access. Automation code actions run in a restricted Python environment. External API calls belong to REST API integrations, which are connectors described on this page. For more information, see
[Code execution isolation](sec-agentic-security.md#sec-agentic-security-code-execution "sec-agentic-security.md#sec-agentic-security-code-execution").

The following table summarizes each outbound path, the data that can leave, and the
control that enables it.

| Outbound path                  | Data that can leave                                                                                                  | What enables it                                                                                                                                                                                                    |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Action connectors              | Conversational context, user requests, and structured parameters sent to the<br>connected third-party or AWS service | Administrator creates and configures the connector, selects authentication<br>method and scopes; individual connectors can be restricted through custom<br>permissions                                             |
| Remote MCP servers             | Tool invocation parameters derived from conversational context                                                       | Administrator creates the MCP integration (Enterprise subscription<br>required)                                                                                                                                    |
| Web search                     | Queries derived from user requests sent to external web search<br>providers                                          | Administrator enables web search for the organization                                                                                                                                                              |
| Third-party research providers | Research queries derived from the research objective                                                                 | Administrator sets up each integration individually and shares it with<br>authorized users; premium providers require a provisioned license; the Research<br>custom permission removes all providers for a profile |
| Quick Apps (public access)     | App content rendered to anonymous internet viewers                                                                   | App owner enables public sharing (Free and Plus accounts only)                                                                                                                                                     |
| Embedding                      | Dashboard visuals, analytics, and generative BI content rendered in an<br>external web application                   | Administrator or developer configures embedding with IAM API calls and domain<br>allowlisting (Enterprise required)                                                                                                |
| Exports and downloads          | Dashboard data (PDF, CSV), research reports, analysis data                                                           | User-initiated; administrator can restrict through custom permissions                                                                                                                                              |
| Log and metric delivery        | Chat conversations, user feedback, agent hours, index storage usage, knowledge<br>base file sync results             | Administrator configures delivery destinations (CloudWatch Logs, Amazon S3,<br>Firehose)                                                                                                                           |
| Cross-Region inference         | Inference inputs and outputs move between Regions within a defined<br>geography                                      | Automatic platform behavior; no outbound destination for you to review or<br>restrict                                                                                                                              |

## Action connectors

Action connectors create secure connections between Amazon Quick and third-party or AWS
services. After an administrator configures a connector, it sends conversational context, user
requests, and structured parameters to the target service.

- **What triggers it** – On-demand connectors
  execute when a user initiates them. Automated workflow connectors execute on a schedule
  or in response to an event, without user interaction.
- **Who controls it** – An administrator creates
  and configures each connector, choosing the authentication method (managed OAuth, custom
  user OAuth, API key, or service-to-service) and the scopes granted. A user can invoke
  only the connectors that an administrator shares with that user. Administrators can additionally
  restrict individual action connectors through custom permissions. Each connector
  supports three permissions: **Create and Update action**,
  **Share action**, and **Use action**.
  Custom permissions profiles apply at the user, role, or account level. The most specific
  level takes precedence. For more information, see
  [Custom permissions](custom-permissions.md "custom-permissions.md").
- **What to verify** – Before enabling a
  connector, verify the authentication method and OAuth scopes granted, whether the
  connector is shared broadly or narrowly, whether it is on-demand or automated, and what
  the service-level authorization permits. The credential you configure defines the
  connector's reach into the connected system. The connector can act on whatever
  the granted scopes and the service-level authorization permit, and nothing
  more.

For more information about action types, see
[On-demand actions](int-actions-types.md#qbs-actions-types-qbs-actions-on-demand "int-actions-types.md#qbs-actions-types-qbs-actions-on-demand") and
[Automated workflows](int-actions-types.md#qbs-actions-types-qbs-actions-automated-workflows "int-actions-types.md#qbs-actions-types-qbs-actions-automated-workflows"). For details on
authentication methods, see
[Authentication methods](quick-action-auth.md "quick-action-auth.md").

## Remote MCP servers

With remote Model Context Protocol (MCP) server integrations, the AI assistant can
invoke tools that those servers provide. When the assistant invokes a tool, it sends tool
invocation parameters derived from conversational context to the MCP server
endpoint.

- **What triggers it** – The AI assistant selects
  a tool during a user-initiated or automated conversation. During connection,
  Amazon Quick discovers and registers the tools that the MCP server provides. After
  discovery completes, each tool is listed as an action that you can review and turn
  on.
- **Who controls it** – An administrator creates
  the MCP integration in the console. The integration specifies the endpoint URL, the
  connection type (public internet or private VPC), and the authentication method. You need an Enterprise subscription. Administrators can restrict individual MCP connectors
  through custom permissions. Each connector supports three permissions:
  **Create and Update action**, **Share action**, and
  **Use action**. For more information, see
  [Custom permissions](custom-permissions.md "custom-permissions.md").
- **Transport restriction** – MCP integration
  supports remote servers only. Local stdio connections are not supported. An MCP
  integration cannot invoke a process running on a local machine.
- **What to verify** – Before enabling an MCP
  integration, verify whether authentication is enabled (unauthenticated access is a
  selectable option), the OAuth scope if user authentication is selected, the network path
  (public internet or private VPC), and what tools the server exposes. Confirm that only
  the tools required for the intended use case are turned on.

For more information, see
[Model Context Protocol (MCP) integration](mcp-integration.md "mcp-integration.md").

## Web search

When web search is enabled, Amazon Quick sends queries derived from user requests to
external web search providers. The assistant uses web search automatically in chat and
research sessions to gather information from publicly available online sources.

- **What triggers it** – The assistant selects web
  search during a user-initiated chat or research session. You can turn off web search
  for individual queries.
- **Who controls it** – An administrator enables
  or disables web search for the organization. When web search is enabled, you can
  turn it off for each query. Web search queries route through designated AWS
  Regions based on the account's primary Region.
- **What to verify** – Before enabling web search,
  determine whether your use case requires external web data and understand how queries
  route across Regions.

For more information, see
[Admin controls](admin-controls.md "admin-controls.md").

For more information about cross-Region routing for web search, see
[Cross-Region calls for web search](regions.md#web-search-cross-region "regions.md#web-search-cross-region").

## Third-party research providers

Amazon Quick Research integrates with third-party data providers such as FactSet, IDC, and
S&P Global. When a user runs a research session, the agent determines which providers to
use based on relevance to the research objective and sends queries to those
providers.

- **What triggers it** – The research agent
  selects providers automatically based on relevance. Users choose which provider
  categories to include for each research session.
- **Who controls it** – Access to third-party
  research providers is layered across multiple controls. An administrator sets up each
  integration individually and shares it only with the users who need access. Unshared
  integrations are unavailable. Premium providers (FactSet, IDC, S&P Global
  Energy, S&P Global Market Intelligence) additionally require an
  administrator-provisioned license. If you don't provision a license, those
  providers stay unavailable. The Research capability in custom permissions removes access to
  Research – and therefore all third-party providers – for a given
  profile. Restricting the "Use internet to enhance results" capability separately
  removes web-based search in chat agents and Research.
- **What to verify** – Verify that each
  third-party data integration is shared only with authorized users. For premium
  providers, verify that licenses are provisioned only where needed. For public
  providers, verify that your acceptable-use policies permit sending research queries to
  external sources. Use the Research capability in custom permissions to remove Research
  entirely for profiles that must not reach any external provider. For more information
  about custom permissions, see
  [Custom permissions](custom-permissions.md "custom-permissions.md").

For more information, see
[Using third party data in Amazon Quick Research](third-party-data.md "third-party-data.md") and
[Select research materials](select-research-materials.md "select-research-materials.md").

## Quick Apps and public access

Quick Apps run inside a security sandbox that blocks direct external network access. All
communication with external systems goes through the secure bridge API or a registered
action connector. When an app owner enables public sharing, app content renders to anonymous
internet viewers who have no identity, no integrations, and are rate-limited.

- **What triggers it** – The app owner creates and
  publishes an app. Anonymous viewers access it through a public URL.
- **Who controls it** – The app owner controls
  sharing and public access settings. Public access is available only to Free and Plus
  accounts. The sandbox is platform-enforced and blocks app code from making direct HTTP
  requests to external servers or loading external resources.
- **What to verify** – Before making an app
  public, verify that public viewers have no access to integrations, that usage counts
  against the owner's quota, and that the sandbox restrictions meet your security
  requirements.

For more information, see
[Security and sandbox in apps in Quick](security-sandbox-apps.md "security-sandbox-apps.md").

## Embedding

Embedding renders Amazon Quick dashboard visuals, analytics, and generative BI content in
an external web application. Domain allowlisting controls where embedded content can
render. Row-level security (RLS) and column-level security (CLS) are enforced for embedded
viewers.

- **What triggers it** – An administrator or
  developer configures embedding through IAM API calls. End users then access the
  embedded content in the host application.
- **Who controls it** – An Enterprise subscription
  is required. The administrator or developer configures the
  `AllowedDomains` parameter to limit which domains can host embedded content.
  The IAM policy condition `AllowedEmbeddingDomains` provides additional
  restriction.
- **What to verify** – Before enabling embedding,
  verify that every domain in the allowlist is controlled by your organization, that RLS
  and CLS are configured for the underlying datasets, and that you have an Enterprise
  subscription.

For more information, see
[Embedding Amazon Quick Sight analytics into your applications](embedding-overview.md "embedding-overview.md").

## Exports and downloads

Users can export dashboard data as PDF or CSV files, download research reports, and
export analysis data. Exported data goes to the user's local device or, for scheduled email
reports, to the configured email delivery destination.

- **What triggers it** – A user initiates an
  export or download action in the console.
- **Who controls it** – An administrator can
  restrict export capabilities through custom permissions. For example, you can disable
  access to the export-to-PDF option on analyses and dashboards. An Enterprise
  subscription is required for custom permissions.
- **What to verify** – No single consolidated
  export-security configuration exists. Verify whether export capabilities are restricted
  through custom permissions for the relevant roles, whether scheduled email reports are
  limited to intended recipients, and whether your compliance requirements impose
  constraints on where exported data can be stored.

For more information about restricting capabilities, see
[Custom permissions](custom-permissions.md "custom-permissions.md").

## Log and metric delivery

Use log and metric delivery to send data from Amazon Quick to destinations that you
control. Unlike the
other paths on this page, data goes to your own AWS infrastructure rather than to a third
party. Log types include chat conversations, user feedback, agent and research hours, index
storage usage, and knowledge base file sync results.

###### Sensitive data in chat logs

Chat logs can contain sensitive or personally identifiable data.

- **What triggers it** – An administrator
  configures delivery. After configuration, delivery is continuous or scheduled.
- **Who controls it** – An administrator
  configures the delivery destination (CloudWatch Logs, Amazon S3, or Firehose). IAM permissions are
  required to set up delivery. When a destination uses a customer managed KMS key, the key
  policy must allow the delivery service principal.
- **What to verify** – Before configuring log
  delivery, verify the encryption and access policies at the destination, the retention
  policies at the destination, and that personnel with access to the destination
  understand that chat logs can contain sensitive data.

For more information, see
[Monitoring Amazon Quick using CloudWatch Logs](monitoring-cloudwatch-logs.md "monitoring-cloudwatch-logs.md").

## Cross-Region inference

Cross-Region inference is processing within a defined geography, not customer-enabled
egress. It is included on this page to prevent confusion, because it involves data moving
between Regions. However, it differs from every other path described on this page. There is no
customer-chosen destination. No data reaches a third party. Data stays on the AWS network,
and stored data remains in the primary Region.

- **What moves** – Inference inputs (prompts) and
  outputs (results) can move outside of the primary Region during processing. All data is
  transmitted encrypted across the AWS secure network.
- **What triggers it** – Amazon Quick automatically
  selects the optimal Region within a defined geography to process inference requests. You
  do not initiate or schedule this routing.
- **Who controls it** – Cross-Region inference is
  not a customer-configurable outbound path. Inference is processed within the Regions
  that make up your geography, no data reaches a third party, and stored data remains in
  your primary Region. Because there is no outbound destination, there is no destination for you to approve or
  restrict. You cannot disable cross-Region inference. Instead, verify which geography your
  Region belongs to. Confirm that the geography boundary satisfies your data residency
  requirements.
- **Boundaries** – Cross-Region inference
  requests stay within the AWS Regions that are part of the geography where the data
  originally resides. Stored data remains only in the primary Region.

For more information, see
[Cross-Region inference for Australia, Japan, Europe, and the United States](regions.md#cross-region-inference "regions.md#cross-region-inference").
