# Supported authentication patterns

AgentCore Identity supports two primary authentication patterns that address different agent
use cases. Understanding these patterns will help you choose the right approach for your
specific agent implementation.

For detailed examples of how these patterns apply to specific industries and agent
types, see [Example use cases](identity-use-cases.md "identity-use-cases.md").

###### Topics

- [User-delegated access (OAuth 2.0
  authorization code grant)](#user-delegated-access "#user-delegated-access")
- [Machine-to-machine authentication (OAuth
  2.0 client credentials grant)](#machine-to-machine-auth "#machine-to-machine-auth")
- [Choosing the right authentication
  pattern](#choosing-auth-pattern "#choosing-auth-pattern")

## User-delegated access (OAuth 2.0

authorization code grant)

The OAuth 2.0 authorization code grant flow enables agents to access user-specific
data with explicit user consent. This pattern is essential when agents need to
access personal data or perform actions on behalf of specific users. The flow
includes a user consent step where the resource owner (user) explicitly authorizes
the agent to access their data within specific scopes.

**Key characteristics**

- Requires explicit user consent through an authorization prompt
- Provides access to user-specific data and resources
- Maintains clear separation between agent identity and user
  authorization
- Supports fine-grained scopes that limit what data the agent can
  access

**Example scenario** – A productivity agent
needs to access a user's Google Calendar to schedule meetings, their Gmail to send
emails, and their Google Drive to store documents. The agent uses the OAuth 2.0
authorization code grant to obtain user consent for each service, with specific
scopes that limit access to only the necessary data. The user explicitly authorizes
the agent through Google's consent screen, and AgentCore Identity securely stores the
resulting credentials for future use.

This pattern is ideal for personal assistant agents, customer service agents, and
any scenario where agents need access to user-specific data across multiple
services. For detailed industry-specific examples, see [Personal assistant agents](identity-use-cases.md#personal-assistant-agents "identity-use-cases.md#personal-assistant-agents")
and [Customer service agents](identity-use-cases.md#customer-service-agents "identity-use-cases.md#customer-service-agents").

## Machine-to-machine authentication (OAuth

2.0 client credentials grant)

The OAuth 2.0 client credentials grant flow enables direct authentication between
systems without user interaction. This pattern is appropriate when agents need to
access resources that aren't user-specific or when agents act themselves with
pre-authorized user consent.

**Key characteristics**

- No user interaction or consent required
- Agent authenticates directly with resource servers using its own
  credentials
- Suitable for background processes, scheduled tasks, and system-level
  operations
- Permissions are defined at the agent level rather than per-user

**Example scenario** – An enterprise data
processing agent needs to collect data from multiple internal systems, process it,
and store the results in a data warehouse. The agent uses the OAuth 2.0 client
credentials grant to authenticate directly with each system using its own identity
and pre-configured permissions. No user interaction is required, and the agent can
operate when agents act themselves with pre-authorized user consent on scheduled
intervals.

This pattern is ideal for enterprise automation agents, data processing workflows,
and DevOps automation. For detailed industry-specific examples, see [Enterprise automation agents](identity-use-cases.md#enterprise-automation-agents "identity-use-cases.md#enterprise-automation-agents"), [Data processing and analytics
agents](identity-use-cases.md#data-processing-and-analytics-agents "identity-use-cases.md#data-processing-and-analytics-agents"), and [Development and DevOps agents](identity-use-cases.md#development-and-devops-agents "identity-use-cases.md#development-and-devops-agents").

## Choosing the right authentication

pattern

When designing your agent authentication strategy, consider these factors to
determine which pattern is most appropriate:

Authentication pattern selection guide| Factor | User-delegated access (OAuth 2.0 authorization code
grant) | Machine-to-machine authentication (OAuth 2.0 client credentials
grant) |
| --- | --- | --- |
| Data ownership | User-specific data (emails, documents, personal calendars) | System or organization-owned data (analytics, logs, shared resources) |
| User interaction | User is present and can provide consent | No user interaction required or available |
| Operation timing | Interactive, real-time operations | Background, scheduled, or batch operations |
| Permission scope | Permissions vary by user and their consent choices | Consistent permissions defined at the agent level | Many agent implementations will require both patterns for different aspects of their functionality. For example, a customer service agent might use user-delegated access to retrieve a specific customer's data while using machine-to-machine authentication to access company knowledge bases and internal systems. AgentCore Identity supports both patterns simultaneously, allowing agents to use the most appropriate authentication mechanism for each resource they need to access. Both authentication patterns benefit from AgentCore Identity's core capabilities: <br>• Secure credential storage without exposing secrets to agent code <br>• Consistent authentication interfaces across multiple resource types <br>• Comprehensive audit logging for security and compliance <br>• Fine-grained access controls based on identity and context <br>• Simplified integration through the AgentCore SDK
