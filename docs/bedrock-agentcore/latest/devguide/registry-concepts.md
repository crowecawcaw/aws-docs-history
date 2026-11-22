

# Concepts and terminology

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on October 30, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

## Registry
<a name="registry-concept-registry"></a>

A registry is a centralized catalog that you create in your AWS account to organize and manage resources. Each registry has a name, a description, an authorization configuration that controls how consumers access the discoverable data-plane APIs and the MCP endpoint, and an approval configuration that determines whether records require manual review before becoming discoverable.

How you organize your registries depends on your needs — for example, dedicated registries for different resource types (an agent registry, an MCP server registry, a skill registry), registries for different stages of development (production, QA, development), independent registries for different teams or business units, or a single registry for your entire organization.

## Registry record
<a name="registry-concept-record"></a>

A registry record represents the metadata for an individual resource published into a registry. Each record captures key metadata that describes the underlying resource — providing information about what it is, what it does, and how it can be found. Records have a `name`, an optional human-readable `displayName`, an optional description, a `recordVersion`, a `recordType` (`AGENT`, `MCP`, `SKILL`, `CUSTOM`, or `WEB_BOT`), and resource-type-specific descriptors that carry the actual content. The combination of `name` and `recordVersion` must be unique within the registry (used as a dedup key), so the same `name` can be reused across different versions of the same resource.

## Publisher
<a name="registry-concept-publisher"></a>

A *Publisher* is a verified public identifier under which your organization publishes records to the public discovery plane. A Publisher’s identifier is a domain with at least two dot-separated levels, such as `example.com`. Your organization proves that it controls the identifier through domain verification before the Publisher can be used. After a record is approved and associated with a verified Publisher, it becomes discoverable across organizational boundaries through AWS-authenticated public search. For more information, see [Publishers](registry-publishers.md).

**Note**  
In AWS Agent Registry, you encounter the word *Publisher* in two ways.  
The **Publisher persona** is a builder who creates records and submits them for approval (see [Key Personas](#registry-concept-personas)).
The **Publisher construct** — the subject of this section — is a verified public identifier (a domain) used for public discovery.
The two are related but distinct: a builder publishes records, and a verified identifier is what those records are published under.

## Resource types
<a name="registry-concept-resource-types"></a>

 **MCP servers** — Model Context Protocol (MCP) servers provide tools that AI agents can discover and invoke. An MCP server record contains a server definition describing the server’s configuration and tool definitions for all the tools the server provides, including their input parameters and output formats. AWS Agent Registry validates MCP server records against the [MCP protocol schema](https://modelcontextprotocol.io/docs/getting-started/intro) to ensure correctness.

 **Agents** — Agents are autonomous programs that can reason, plan, and take actions to accomplish tasks. An agent record contains an agent card that describes the agent’s capabilities, skills, and communication interface per the A2A [(Agent-to-Agent)](https://a2a-protocol.org/latest/) protocol specification. AWS Agent Registry validates agent records against the A2A protocol schema to ensure correctness.

 **Skills** — Skills are reusable capabilities that can be shared across agents. A skill record contains basic descriptor metadata like Name, Description, optional access information like Package or Repository details, and optional markdown documentation (SKILL.md) describing what the skill does and how to use it. A skill record can also carry a full skill package: a ZIP archive that contains SKILL.md and the files that the skill uses. You can upload the package, or synchronize it from Amazon S3 or a GitHub folder. AWS Agent Registry validates skill content against the [Agent Skills specification](https://agentskills.io/specification) on the Agent Skills website, and consumers can download the approved package.

 **Custom resources** — For resources that don’t fit the standard types above you can define your own metadata schema using any valid JSON structure.

 **Web bot** — A Web bot record represents a signed-request bot identity that AWS WAF can recognize when evaluating web requests. For more information, see [Web bot records](registry-web-bot.md).

## Credential provider
<a name="registry-concept-credential-provider"></a>

When you configure a registry record to synchronize metadata from an external source (outbound authorization) AWS Agent Registry needs credentials to access that source. A credential provider stores the authorization details — either OAuth credentials or an IAM role — that AWS Agent Registry uses to invoke the external resource’s endpoint during synchronization. You reference a credential provider by its ARN when configuring synchronization on a record. For more information, see [Manage credential providers](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-outbound-credential-provider.html).

Registry authorization has two types:

1.  **Inbound authorization**: Use this configuration to control how your consumers search, browse, and invoke the registry’s discoverable data-plane APIs and MCP endpoint (via the AWS CLI, AWS SDK, or an MCP-compatible client). The registry supports IAM-based and JWT-based inbound authorization. You specify inbound authorization as part of the workflow for creating a registry.

1.  **Outbound authorization**: When you configure a record for synchronization with a remote MCP or A2A endpoint, the registry needs outbound credentials to invoke the remote resource at the specified endpoint and retrieve metadata. You provide these credentials as part of setting up the synchronization job for a particular registry record.

## Tags
<a name="registry-concept-tags"></a>

You can attach tags to registries and registry records for cost allocation, access control, and organizational tracking. Each tag is a key-value pair, and both keys and values are strings you define. Tags do not affect the runtime behavior of a registry or a record — they exist as metadata that you and your organization can use to categorize resources across an AWS account.

## Key Personas
<a name="registry-concept-personas"></a>

Personas that use the Registry can vary from organization to organization. However, we have seen the following general personas that interact with the Registry, found commonly across organizations.

 **Administrator**   
As an administrator, you own the registry infrastructure. You create and configure registries within the AWS account, decide how each registry is organized (by team, environment, or resource type), and choose the authorization method (IAM or JWT) that determines how consumers access the registry. You set up the approval workflow — deciding whether records require manual review or are auto-approved — and configure Amazon EventBridge integrations to connect the registry to your organization’s existing notification and review systems. You manage IAM permissions to control which publishers, curators, and consumers can access each registry. As the admin, you also have full access to create, update, and delete records, and can approve, reject, or deprecate records when needed.  
For public discovery, you also create and verify [Publishers](#registry-concept-publisher): you own the domains and DNS zones that back your organization’s public identifiers, prove ownership of the domain by adding the DNS challenge record that AWS Agent Registry returns, and manage that verification over its lifetime. A builder later associates approved records with a verified Publisher.

 **Publisher**   
As a publisher, you are a builder within the organization who has created a resource — an MCP server, an agent, a skill, or some other tool — and wants to make it discoverable to others. You create registry records that describe your resources, providing the metadata, definitions, and version information that helps others find and understand what the resource does. You iterate on records in Draft status, refining descriptions and schemas until the record is ready, then submit it for approval. If a record is rejected, you review the curator’s feedback, make the necessary changes, and resubmit. You can also configure URL-based synchronization so that your records stay in sync with live MCP servers without manual updates.

 **Curator / Approver**   
As a curator, you are the quality gatekeeper of the registry, and can often also be the administrator of the registry. You review records that publishers have submitted for approval, evaluating each record against your organization’s standards for security, compliance, metadata completeness, and any other criteria your organization defines. You approve records that meet these standards — making them visible via the discoverable data-plane APIs (search, list, batch-get) and through the MCP endpoint — and reject records that don’t, providing clear feedback on what needs to be fixed. When a resource is decommissioned, has known issues, or is superseded by a newer version, you deprecate the record to remove it from discovery. As a curator, you help keep the registry a trusted, high-quality catalog that builders across the organization can rely on.

 **Consumer**   
As a consumer, you are a human or agent that needs to find and use resources. You can discover approved records in three ways:  
+  **Search** with natural language queries or keyword lookups to find records that match a topic, capability, or use case (`SearchDiscoverableRegistryRecords`).
+  **Browse** the catalog of approved records with a paginated list, optionally filtered by record type, and retrieve details for one or many records at a time (`ListDiscoverableRegistryRecords` and `GetDiscoverableRegistryRecord` / `BatchGetDiscoverableRegistryRecord`).
+  **Connect** to the registry’s MCP endpoint from any MCP-compatible client to discover available tools programmatically (`InvokeRegistryMcp`).

  As a consumer, you only see approved records, so you can trust that everything you find in the registry has been reviewed and meets the organization’s quality standards. You can authorize via IAM credentials or JWT tokens from a corporate identity provider, depending on how the registry is configured.

 **Client**   
As a client, you are a human or agent in any organization who searches for publicly discoverable agents and resources. Using AWS-authenticated public search, you find records that other organizations have promoted to the public discovery plane under a verified Publisher. Unlike a consumer, who discovers records within a single organization’s registry, a client discovers records across organizational boundaries. For more information, see [Search publicly discoverable records](registry-public-search.md).