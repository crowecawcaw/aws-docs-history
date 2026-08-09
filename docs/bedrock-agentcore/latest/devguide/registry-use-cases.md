# Sample use cases

###### Migration Now Open

AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md "registry-faq.md").

Below you will find some examples use cases where registry can be used.

## Discover Agents or Tools for building an internal workflow

A builder is creating an internal HR workflow that generates a report of employee time-off balances. The workflow needs access to an employee information service, a PTO tracking service, and a document generation service like SharePoint. Rather than asking around or searching through internal wikis, the builder searches the AWS Agent Registry for services matching their needs. They find all three services registered with their connection details and tool schemas, and use this information to construct the workflow — reducing what would have been days of discovery into minutes.

## Add a new capability to a customer-facing agent

A builder maintains an external customer service agent that handles order inquiries. They need to add a new use case: helping customers track delayed package deliveries. The agent already has access to customer information and order history services, but needs a delivery tracking service. The builder searches the registry, finds a registered delivery tracking service with the right capabilities, attaches it to their Gateway, and updates the agent’s policy to allow calls to this new service — all without needing to know which team built the delivery service or how to contact them.

## Manage agent sprawl across teams

An administrator reviewing the registry notices that a new team is building a travel booking agent with capabilities very similar to an existing travel planning agent registered by another team. By discovering this overlap through the registry, the administrator connects the two teams. Instead of duplicating effort, the existing agent is updated with the additional capabilities, and the organization avoids maintaining two agents that do essentially the same thing.

## Share reusable skills across agents

A team has developed a skill for extracting structured data from PDF documents. They received positive feedback about the effectiveness of this skill, and were asked to broadly share this skill across the organization to boost collective productivity. Instead of reaching out to each team independently, they publish the skill to the registry with detailed markdown documentation and a structured definition. Other agent builders discover the skill through search or by browsing the approved-record catalog, and integrate it into their own agents, accelerating development across the organization.

## Explore the registry catalog before committing to a search

A builder who is new to the registry doesn’t yet know what’s available and can’t craft a specific search query. They browse the approved-record catalog through the console or `ListDiscoverableRegistryRecords`, filter by record type (say, MCP servers), and page through results to get a sense of what tools exist in the organization. When they find several records that look promising, they fetch full details in a single call with `BatchGetDiscoverableRegistryRecord` and pick the ones that fit their workflow.

## Enforce quality standards through curation

A builder submits a new MCP server record to the registry. The submission triggers an Amazon EventBridge notification that kicks off the organization’s standard review pipeline. The automated pipeline checks that the server definition includes complete tool descriptions, that input schemas are properly defined, and that the server meets the organization’s security requirements. The review finds that several tool descriptions are missing required fields. The curator rejects the record with a detailed reason, and the builder receives feedback on what to fix before resubmitting.

## Keep registry records synchronized with live servers

A team deploys MCP servers on AgentCore Runtime whose tool definitions evolve as new features are added. Rather than manually updating registry records every time a tool changes, they configure URL-based synchronization on each record and simply come to the registry periodically to trigger synchronization. When they do so, AWS Agent Registry fetches the latest server and tool metadata from the MCP server’s endpoint, keeping the registry accurate.
