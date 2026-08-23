# Security in Quick

Amazon Quick provides a number of security features to consider as you develop and
implement your own security policies. The following best practices are general guidelines
and don't represent a complete security solution. Because these best practices might not be
appropriate or sufficient for your environment, treat them as helpful considerations rather
than prescriptions.

For more information about how your data is protected, including the statement that
customer data is not used for training or improving underlying LLMs, see
[Data protection in Amazon Quick](sec-data-protection.md "sec-data-protection.md").

For a conceptual explanation of how AI and agent capabilities change the risk analysis
for Quick, including the two-condition model for adversarial content risk,
see [AI and agent security in Amazon Quick](sec-agentic-security.md "sec-agentic-security.md").

**Decide before you deploy**
– The following decisions are irreversible or difficult to change after initial
configuration. Make them deliberately before you create resources or onboard users.

**Register encryption keys before you create
resources** – Quick encrypts all data at rest by
default. For more information, see [Encryption at rest](data-encryption.md#data-encryption-at-rest "data-encryption.md#data-encryption-at-rest"). The following decision is about whether you or
AWS controls the keys. If you require control of the encryption keys that
protect your data, register a customer managed KMS key as the account default
_before_ you create resources. Two key paths matter:

- **Account default key** – Participating
  resource types select the account default key when data is written. Changing the
  default affects future writes but does not re-encrypt existing content.
- **Amazon Q data key** – Set once, the first
  time Amazon Q data is created in the account, from the default key registered at
  that moment. You cannot change this key afterward. For more information, see
  [Amazon Q data key](customer-managed-keys.md#customer-managed-keys-q-data-key "customer-managed-keys.md#customer-managed-keys-q-data-key").
- **Research resources** – A Research resource
  associates a key at creation. A Research resource created without a key association
  cannot be moved to one later.
  Customer managed KMS key support requires an Enterprise subscription. For the full list
  of participating resource types, see [Customer managed KMS key scope](customer-managed-keys.md#customer-managed-keys-scope "customer-managed-keys.md#customer-managed-keys-scope").

**Choose your identity
model** – Choose deliberately among IAM Identity Center,
Active Directory, IAM federation, and Quick local users. Provisioning and
offboarding behavior differ by model. In particular, Quick detects inactive users and populates the
**Inactive users** list. This detection applies only to accounts that
federate through IAM Identity Center or Active Directory. For more information, see
[User lifecycle and data handling in Amazon Quick](user-lifecycle-data-handling.md "user-lifecycle-data-handling.md").

**Select the knowledge base access model at
creation** – For supported integrations, decide at creation
whether a knowledge base is access control list (ACL) aware. Document-level ACL
configuration is
permanent. You cannot turn on ACLs for a knowledge base created without ACL support,
and you cannot turn them off after you turn them on. To change ACL configuration, create a
new knowledge base with your desired setting from the start.

- **Supported integrations** – Amazon S3,
  Google Drive, Microsoft SharePoint, Atlassian Confluence Cloud, and Microsoft
  OneDrive.
- **Sharing and retrieval are separate controls**
  – Knowledge base sharing determines who can use the knowledge base.
  For ACL-aware knowledge bases, source-document ACLs further limit which indexed
  documents each authorized user can retrieve. Review both controls before granting
  access.
- **Fail-closed behavior** – If
  Quick cannot evaluate document permissions for a query, it returns no
  documents rather than unfiltered results.
- **Sync cadence** –
  Quick synchronizes identity and document-permission changes on the
  knowledge base refresh schedule, which is every 24 hours by default. Configure a
  shorter schedule when your access-change requirements demand it.
- **Shared email addresses** – If multiple
  Quick users share the same email address within a namespace, the system
  denies access to everyone using that shared email.
- **ACL resolution scope** –
  Quick resolves all ACLs within the namespace of the knowledge base
  creator.
- **Email recycling** – If your organization
  reassigns an email address before the next ACL refresh and the previous holder never
  used Quick for chat, temporary access leakage is possible. Update ACLs
  and refresh the knowledge base before reassigning the email.
- **Research incompatibility** – Knowledge
  bases with document-level ACLs enabled are not compatible with
  Quick Research.
  For more information, see
  [Best practices for managing ACLs in knowledge bases](acl-best-practices-kb.md "acl-best-practices-kb.md").

**Restrict access**
– After your account is configured, restrict access to the minimum required for each
role.

**Apply least
privilege** – Assign Quick roles that match each
user's responsibilities. Use custom permissions profiles to further scope down the default
capabilities available to a role. Custom permissions can only restrict. They cannot
grant capabilities a user does not already have. When you assign profiles at multiple
levels, the most specific level wins: user-level overrides role-level, which overrides
account-level. Custom permissions require an Enterprise subscription. For more information,
see [Custom permissions](custom-permissions.md "custom-permissions.md").

For BI workloads, supplement permissions with row-level security, column-level security,
and run-as roles to limit data access at query time.

**Deny by default for AI
capabilities** – If your organization has model-risk or
change-approval requirements, restrict the AI capability category so that new AI
capabilities are denied on launch day until you explicitly allow them. Without this
restriction, every new AI capability that Quick ships is automatically
available to all users upon release. For more information, see
[Deny by Default](custom-permissions-governance.md "custom-permissions-governance.md").

**Configure AI
guardrails** – Built-in content safety screening applies
automatically to chat interactions. You can further configure up to 50 blocked words and
phrases that Quick checks against both user requests and generated responses.
For more information, see [AI guardrails in Amazon Quick](guardrails.md "guardrails.md").

**Match oversight to how the action
runs** – Quick supports two invocation models with
different security characteristics. Match your review depth to the autonomy and consequence
of each model.

- **On-demand actions** – User-initiated,
  interactive, and authenticated with the individual user's personal credentials.
  Each action runs as the invoking user and is bounded by that user's connector
  permissions. For more information, see
  [On-demand actions](int-actions-types.md#qbs-actions-types-qbs-actions-on-demand "int-actions-types.md#qbs-actions-types-qbs-actions-on-demand").
- **Automated workflows** – System-level,
  scheduled or event-triggered, non-interactive, and authenticated at service level.
  An automated workflow authenticates at service level. It does not act as an individual
  user, is not bounded by that user's connector permissions, and runs unattended. Give automated workflows closer scrutiny during review. For more
  information, see
  [Automated workflows](int-actions-types.md#qbs-actions-types-qbs-actions-automated-workflows "int-actions-types.md#qbs-actions-types-qbs-actions-automated-workflows").
- **Restricting autonomous execution** – If
  unattended execution is not acceptable for some or all users, use the following
  custom permissions capabilities to restrict it:

  - **Automate** – Prevents restricted users from
    creating, updating, or running automations.
  - **Flows** – Restricts creating, updating,
    sharing, and running flows.
  - **Triggers** – Restricts all trigger
    capabilities, including inbound email triggers and Quick event
    triggers.
    Apply these restrictions in an account-level profile to restrict unattended
    execution across the entire account. For more information, see
    [Custom permissions](custom-permissions.md "custom-permissions.md").

- **Adding a review step** – For workflows
  where a human review step is appropriate, use the human-in-the-loop task center to
  pause execution and collect approval before the workflow continues. For more
  information, see
  [Human-in-the-loop task center](hitl-task-center.md "hitl-task-center.md").
  **Treat retrieved and external content as
  untrusted** – The risk of acting on adversarial content requires
  two conditions: the assistant can read content from outside your trust boundary, and it can
  take a consequential action. Narrowing either side reduces exposure.

- **Read surface** – Content from the following
  sources enters the assistant's context: knowledge base and index retrieval, files
  uploaded to spaces and chat, web search, third-party research providers, and content
  returned by connectors.
- **Action surface** – Limit the connectors,
  actions, and outbound paths available to each role. A narrower action scope reduces
  the consequence of any single compromised input.
- **Built-in screening** – Built-in safety
  checks screen user requests, including requests that contain prompt attacks. Pair
  this screening with narrow action scope rather than relying on screening alone.
  For more information, see
  [AI guardrails in Amazon Quick](guardrails.md "guardrails.md").
  **Restrict network
  access** – Use IP and VPC endpoint rules to control which
  networks can reach Quick through web, embedded, and mobile access. Rule types
  include CIDR blocks (IPv4), VPC IDs, and VPC endpoint IDs. You can add up to 100 IP and
  VPC endpoint rules combined. These rules are global and apply to all AWS Regions.
  Rule changes can take up to 10 minutes to take effect. IP and VPC endpoint rules require an
  Enterprise subscription.

IP and VPC endpoint rules do _not_ restrict access to the public API.
To restrict API access, use IAM policy conditions. For more information, see
[Turning on Internet Protocol (IP) and VPC endpoint restrictions in Amazon Quick](manage-ip-vpc.md#enabling-ip-restrictions "manage-ip-vpc.md#enabling-ip-restrictions").

**Transfer ownership before you
offboard** – Assets left in the account without an owner become
inaccessible to every user. Transfer ownership of connectors, agents, and automations
before you remove a user from the account.

- **Review orphaned assets** – Periodically
  review connectors, agents, and automations whose owners have left your
  organization.
  For more information, see
  [Orphaned assets](user-lifecycle-data-handling.md#user-removal-orphaned-assets "user-lifecycle-data-handling.md#user-removal-orphaned-assets").
- **Review dormant connections** – Managed
  OAuth refresh tokens carry a 90-day lifecycle. Use this cadence as a trigger to
  review whether each connection is still needed, and remove connections that are no
  longer in use.
- **Plan for the full lifecycle** – For
  detailed guidance on user removal and its effects, see
  [User lifecycle and data handling in Amazon Quick](user-lifecycle-data-handling.md "user-lifecycle-data-handling.md").
  **Review what leaves**
  – Each outbound path is customer-enabled, and each connection has its own
  authentication and data-access characteristics. Review each path as a potential egress
  channel before you turn it on.

**Require authentication on every
connection** – The authentication options available depend on the
connector type. Some connector types
allow connecting without authentication, including remote Model Context Protocol (MCP)
servers, agent-to-agent connectors, and generic HTTP connectors. Confirm that every connection requires authentication before you
enable it.

- **User-level OAuth** – Each user authenticates
  individually and acts as themselves. Prefer user-level authentication where the
  connector supports it, because the impact of a misconfigured connection is
  limited to a single user's access scope.
- **Shared client-credentials connection** – A
  single set of credentials is shared across all users of the connector. Every user
  of that connector inherits its reach and access scope. Scope shared credentials
  narrowly and review what they grant.
- **Per-connector restriction** – You can
  restrict individual action connectors for Create and Update, Share, and Use
  through custom permissions, so a connector can be enabled for a narrow set of
  users rather than everyone. For more information, see
  [Custom permissions](custom-permissions.md "custom-permissions.md").
  For more information about the available authentication methods, see
  [Authentication methods](quick-action-auth.md "quick-action-auth.md").

**Review each outbound path before enabling
it** – Before you enable an outbound capability, verify that the
destination and the data that can flow to it meet your organization's requirements.
Outbound paths include action connectors, remote MCP servers, web search, third-party
research providers, public apps, embedding, and export destinations. For per-path detail
on what data can leave, what triggers it, who controls it, and what to verify, see
[Outbound connections and data egress in Amazon Quick](outbound-connections.md "outbound-connections.md").

**Configure
observability** – Configure monitoring and logging before you
onboard users at scale. Use the following signals together when you design monitoring and
incident-response procedures. Before you rely on a signal for compliance, detection, or
investigation, confirm that it covers the event you intend to track.

- **CloudTrail** – Records supported API operations
  and a documented set of non-API events such as dashboard views and user-management
  actions. CloudTrail does not capture chat conversation content or user feedback. For
  those signals, use CloudWatch vended logs. For more information, see
  [Monitoring Amazon Quick using CloudTrail](monitoring-cloudtrail.md "monitoring-cloudtrail.md").
- **CloudWatch vended logs** – Five log types
  deliver conversational and operational data to destinations you control (Amazon CloudWatch
  Logs, Amazon S3, or Firehose):

  - Chat conversations (`CHAT_LOGS`)
  - User feedback (`FEEDBACK_LOGS`)
  - Agent and research hours (`AGENT_HOURS_LOGS`)
  - Index storage usage (`INDEX_USAGE_LOGS`)
  - Knowledge base file sync (`KB_FILE_SYNC_LOGS`)
    Vended logs do not flow by default. Configure delivery shortly after you enable
    Quick AI features so that you do not lose early interaction data. For
    more information, see
    [Monitoring Amazon Quick using CloudWatch Logs](monitoring-cloudwatch-logs.md "monitoring-cloudwatch-logs.md").

- **CloudWatch metrics and alarms** – Near-real-time
  operational metrics cover dashboards, visuals, dataset ingestions, unstructured
  datasets, action connectors, and SPICE capacity. You can create CloudWatch alarms that
  send notifications when a metric reaches a threshold that you specify. For more
  information, see
  [Monitoring Amazon Quick using CloudWatch metrics](monitoring-cloudwatch-metrics.md "monitoring-cloudwatch-metrics.md").
- **Analytics dashboard** – Provides usage,
  adoption, and feedback insights for IAM administrators. Access requires the
  `quicksight:QuickSuiteUsageMetrics` permission. The analytics dashboard
  can expose detailed query text, failed-query content, and the full conversation
  context associated with negative feedback. Grant analytics access only to authorized
  administrators. For more information, see
  [Using the Amazon Quick analytics dashboard](incident-response-logging-and-monitoring-quick-suite.md "incident-response-logging-and-monitoring-quick-suite.md").
- **Feature-specific reports** – Some features
  produce their own operational reports, such as knowledge base sync reports that
  document per-file sync status.
  You control retention for all externalized signals. Set destination retention
  policies to match your compliance requirements. CloudTrail event history retains 90 days of
  management events by default. CloudWatch Logs, Amazon S3, and Firehose destination retention follows
  the policies you configure at each destination. For more information, see
  [Incident response, logging, and monitoring in Amazon Quick](incident-response-logging-and-monitoring.md "incident-response-logging-and-monitoring.md").

CloudTrail records metadata (who, when, what operation) but not the message body or response
content. CloudWatch vended chat logs capture user messages and system responses but not source
document content. The analytics dashboard exposes conversation context only in the scope of
negative feedback review. If your compliance model requires a signal not listed here,
verify coverage before assuming it exists.

**Data source connectivity**
– The following practices help you connect securely to data sources.

**Use VPC connections for private
sources** – Use a virtual private cloud (VPC) connection for
data in AWS data sources and for data in on-premises servers without public
connectivity. For AWS sources, Quick uses an elastic network interface for
secure, private communication with data sources in a VPC. For on-premises sources, use
Direct Connect or AWS Site-to-Site VPN to create a secure, private link. VPC connections
require an Enterprise subscription. For more information, see
[Managing VPC connection in Amazon Quick](vpc-creating-a-connection-in-quicksight.md "vpc-creating-a-connection-in-quicksight.md").

**Encrypt database connections with
SSL** – Use SSL to connect to your databases, especially if you
are using public networks. Using SSL with Quick requires certificates signed
by a publicly recognized certificate authority (CA).

**Configure firewall rules for user and data
access** – To allow users to access Quick, allow
access to HTTPS and WebSockets Secure (wss://) protocol. To allow Quick to
reach a database on a non-AWS server, change that server's firewall configuration to
accept traffic from the applicable Quick IP address range. For more
information, see [Network and database configuration requirements](configure-access.md "configure-access.md").
