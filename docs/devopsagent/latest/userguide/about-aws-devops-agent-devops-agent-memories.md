

# DevOps Agent Memories
<a name="about-aws-devops-agent-devops-agent-memories"></a>

Memories are informational knowledge items that AWS DevOps Agent builds and maintains to supplement its capabilities with synthesized, high-signal context specific to your Agent Space. Unlike [DevOps Agent Skills](about-aws-devops-agent-devops-agent-skills.md), which encode procedural knowledge and extend agent capabilities, memories encode informational knowledge that helps agents make faster and more accurate decisions during investigations.

## What are memories
<a name="what-are-memories"></a>

A *memory* is a single markdown file that captures synthesized information relevant to your Agent Space. Examples include recurring root causes for a specific alarm, known environmental quirks, or user-specific preferences. Memories do not extend agent capabilities; they provide context the agent uses to make better decisions.

A *memory store* is a collection of related memory files. Each memory store has a name and description that agents use to decide whether to browse its contents. Memory stores are the organizational containers that group memories by topic.

Memory stores come from two places. AWS DevOps Agent creates and maintains *managed* stores as it learns from activity in your Agent Space. You create *custom* stores yourself to group the operational knowledge that matters to a team, a service, or a recurring problem. The agent treats both the same way: it reads each store's name and description to decide whether to open it.

Memories differ from other knowledge item types in key ways:


| Aspect | Skill | Agent instructions | Memory | 
| --- | --- | --- | --- | 
| Knowledge type | Procedural (instructions) | Procedural (always-on instructions) | Informational (synthesized context) | 
| Content format | Markdown or ZIP bundle | Markdown only | Markdown only | 
| Context injection | On demand (agent decides via description matching) | Always (every session) | On demand (agent decides via description matching) | 
| Created by | User (UI, CLI), AWS DevOps Agent | User (UI, CLI) | User (UI, CLI, via Chat), AWS DevOps Agent (Learning agent) | 

## Why use memories
<a name="why-use-memories"></a>

Memories give agents access to historical patterns and environmental knowledge that would otherwise be lost between sessions.

**Key benefits:**
+ **Faster investigations** - Agents recall recent root causes for specific monitors, avoiding redundant diagnostic steps when a recurring issue fires again.
+ **Environmental awareness** - Memories capture environment-specific details such as known noisy alarms, infrastructure quirks, or component relationships that are difficult to re-discover each session.
+ **Continuous improvement** - As the DevOps Agent resolves more incidents, it automatically builds a richer knowledge base of patterns and root causes specific to your infrastructure.
+ **User preferences** - Memories record communication preferences and directives so the agent consistently behaves according to your expectations.

## How memories work
<a name="how-memories-work"></a>

When an agent session starts, the agent receives a list of memory stores with their names and descriptions—not their contents. During an investigation, the agent matches the current task against each store's description to decide whether the store is relevant. If it is, the agent lists the memories inside, and each memory carries its own description that the agent uses the same way—it reads a memory's full content only after that description looks relevant. Because a name and description are all the agent sees before it opens a store or a memory, the description is the signal the agent matches against; the contents stay hidden until the agent decides to read them. This progressive-disclosure pattern keeps context consumption low while making all relevant knowledge accessible.

Each memory is versioned. Every update creates a new immutable version, so you can view previous versions and keep an audit trail of how a memory changed over time.

## Organizing memories into folders
<a name="organizing-memories-into-folders"></a>

A memory's name is its path within the store, so you can group related memories into folders instead of keeping a single flat list. Use `/` in a name to nest memories—for example, `alarms/checkout-latency` or `services/checkout/overview`. Because a memory's location signals what it holds, the agent reads an index first and opens only the few files relevant to the task, the same progressive-disclosure pattern described above.

For example, the agent's map of your environment is a set of files—an overview, a file for each service, and a file for each critical request path—with an index that the agent reads first. The operator app displays memories in this folder structure, so you can browse a store the way the agent navigates it.

## Managed memory stores
<a name="managed-memory-stores"></a>

AWS DevOps Agent creates and maintains a set of managed memory stores automatically as it learns from activity in your Agent Space. These include the built-in `monitors` and `directives` stores, and a store for each area of your environment that AWS DevOps Agent learns about—your topology, code dependencies, pipeline structure, and tool-use patterns. AWS DevOps Agent previously presented this knowledge as *learned skills*; today it maintains the same knowledge as memory, in the stores described here. For how these stores are built and refreshed, see [How memory is built and refreshed](#how-memory-is-built-and-refreshed).

### monitors
<a name="monitors"></a>

Per-monitor recurring root cause history. Each memory file corresponds to a specific monitor (alarm or metric) and lists the cause categories that have produced incidents for that alarm, with per-investigation evidence. Agents read the entry matching the firing alarm before triaging to quickly identify whether the current incident matches a known pattern.

When there are investigations in the past 2 weeks in the Agent Space, a Learning agent runs once per day to analyze recent investigations, then extract and store memories in this store. Memory items in this store are deleted when they have no updates for 2 weeks. If the store becomes full, the oldest memory item is deleted to make room.

### directives
<a name="directives"></a>

User-authored directives that steer agent behavior. Use this store to record standing instructions the agent should follow, such as infrastructure conventions or naming preferences.

Examples:
+ "Lambdas are no longer used. The service uses Fargate."
+ "The storage service is called Orders Storage Service."

### Agent Space Understanding
<a name="agent-space-understanding"></a>

The `understanding-agent-space` store holds a map of the resources and relationships in your Agent Space. It includes a plain-language system overview with key domain concepts, the deployment environments (AWS account and Region pairs, Azure subscriptions and regions, and so on), a container-level architecture that shows how logical services connect, the request paths that are central to your application with the components they traverse, and a mapping of code repositories to containers.

The store keeps a memory for each logical container that describes its internal components (compute, data, messaging, network, and others) with resource types and physical identifiers such as ARNs, table names, and queue URLs. Each container memory also captures observability coverage—the alarms, dashboards, and monitors linked to each component—and maps each component to its associated code repositories, packages, and infrastructure-as-code definitions, giving a complete traceability chain from source code to deployed resources.

It also keeps a memory for each critical request path that describes the full end-to-end request flow at component granularity, from the entry point through each intermediate service, data store, and external dependency. Each path memory includes a sequenced flow of operations and interaction mechanisms between components, and it catalogs the observability signals relevant to the path: log group patterns for each hop, key metrics (latency, error rates, throttling, token quotas) with their alarm names and dimensions, and distributed trace spans that can be correlated across services and accounts.

### Understanding Code Dependencies
<a name="understanding-code-dependencies"></a>

The `understanding-dependencies` store holds a complete service-to-service and package dependency map. Use it to understand how repositories connect: which services call which, what events flow between them, which packages are shared, and where infrastructure boundaries lie. This store is essential for assessing the blast radius of a change, identifying upstream and downstream impact, and understanding deployment ordering.

### Understanding Pipeline Topology
<a name="understanding-pipeline-topology"></a>

The `understanding-pipeline-topology` store maps your project pipelines from start to finish, including steps, environment promotions, and deployments along the way to release. This helps the agent distinguish production from pre-production environments and understand where a change is in the release process.

### Tool Use Best Practices
<a name="tool-use-best-practices"></a>

The `tool-use-best-practices` store holds effective tool-use patterns, common failure modes, and parameter guidance that the agent distilled from past investigations, so it avoids known pitfalls and runs investigations with fewer wasted steps. It keeps a routing memory that lists each tool with the investigation scenarios it supports, plus a memory for each category of tools. The guidance for a tool can include up to three sections:
+ **Best Practices** — Investigation-driven techniques extracted from successful tool usage, such as CloudWatch Logs Insights query templates, environment-specific metric namespaces and dimensions, and CloudTrail event source filters. Each entry is organized around an investigation scenario and includes concrete parameter values and examples observed in past investigations.
+ **Common Errors** — Recurring failure modes and their fixes. Each entry describes a specific error condition, such as querying an inaccessible account or constructing a malformed aggregation query, and provides a corrective action so the agent can avoid or recover from the error without wasting investigation steps.
+ **Output Management** — Guidance for tool calls that tend to return large responses. Each entry describes a parameter change or processing strategy that reduces output size while preserving diagnostic value.

When live infrastructure access is available, AWS DevOps Agent validates these patterns against your environment before including them. Confirmed patterns are stated with confidence, unconfirmed patterns use cautious language, and disproved patterns are excluded.

## How memory is built and refreshed
<a name="how-memory-is-built-and-refreshed"></a>

AWS DevOps Agent builds and updates its managed memory automatically as it works—you don't maintain it by hand. A background learning agent analyzes your Agent Space and your recent investigations, then writes and refreshes the memories in the managed stores.
+ The **Agent Space Understanding** store is first generated when an Agent Space finishes its initial resource discovery, and is regenerated when your connected code repositories, deployment pipelines, or observability integrations change. Changes to connected AWS, Azure, or Dynatrace accounts are reflected on the next scheduled refresh rather than immediately. For active Agent Spaces, the store is also refreshed on a recurring schedule, at most once every 3 days. An Agent Space is active if it has completed at least one investigation in the last 6 days; if it has none for 6 days, the scheduled refresh pauses automatically and resumes after a new investigation completes.
+ The **Tool Use Best Practices** store is refreshed after at least 10 new completed investigations have accumulated since its last refresh, and no more than once every 3 days.
+ The **monitors** store is refreshed once per day when the Agent Space has had investigations in the past two weeks.

To regenerate this memory manually, choose **Regenerate** on the Topology page in the operator app, or ask AWS DevOps Agent in chat to update it.

The summary report is built from the Agent Space Understanding memory. It's a versioned, read-only view of what AWS DevOps Agent knows about your environment, available on the **Summary report** tab of the Agent Space details page in the AWS DevOps Agent admin console, and in the **Artifacts** section of the web app. The Topology page visualizes your environment as logical containers and components; the topology graph it draws from is also what feeds the Agent Space Understanding memory. For more information, see [What is a DevOps Agent Topology?](about-aws-devops-agent-what-is-a-devops-agent-topology.md).

## Creating your own memory stores
<a name="creating-your-own-memory-stores"></a>

You can create your own memory stores to hold operational knowledge for a team, a service, or a recurring problem—for example, the standard procedures your team follows for a routine task, or the standing context behind an operational report you produce on a schedule. Give a store a name and a clear description. The agent uses the description to decide when the store is relevant, so a specific, accurate description is the most important thing you provide.

You can create a memory store from the console or by chatting with AWS DevOps Agent.

**To create a memory store (console):**

1. Navigate to the **Knowledge** page in your Agent Space Operator Web App.

1. Choose the **Memories** tab.

1. Choose **Create memory store**.

1. Enter a name and a description, and then choose **Create**.

**To create a memory store (chat):**

Ask AWS DevOps Agent. For example:
+ "Create a memory store named payments-runbook that holds standing guidance for investigating the payments service." - Creates a store.
+ "In the payments-runbook store, remember that the checkout latency alarm is expected to spike during nightly batch jobs." - Adds a memory to the store.
+ "Create a memory store named operational-procedures that holds the standard runbooks for our routine maintenance tasks." - Creates a store for standard operating procedures.
+ "Create a memory store named weekly-report-context with the sections, sources, and format our weekly operations report should follow." - Creates a store for a recurring operational report.

The agent uses a custom store the same way it uses a managed store: it reads the store's description during a task, and if the store is relevant, it opens the memories it needs. Custom stores count toward the same limits as managed stores. See [Memory limits](#memory-limits).

**Writing effective descriptions**

A store's description is the most important thing you write, because it's how the agent decides whether the store is relevant—before it reads anything inside. When the agent works on a task, it sees each store's name and description, not its memories, and opens the store only when the description signals that its contents apply. The same holds one level down: each memory has its own description, and the agent reads a memory's full content only after that description looks relevant. A precise description gets the store opened at the right moment; a vague label such as `notes` or `misc` gives the agent nothing to match against, so it skips the store even when the answer is inside.

Write a description that states two things: what the store holds, and when the agent should use it. A reliable pattern is to end with the situations it applies to—for example, "Read when investigating checkout or billing latency." Keep it specific and concrete, and phrase it as a plain statement about the store's subject rather than an instruction addressed to a person. For example:
+ **Too vague:** "Payments notes."
+ **Effective:** "Standing runbooks, known issues, and escalation contacts for the payments service. Read when investigating checkout, billing, or refund incidents."

A description can be up to 1,024 characters. You can refine it later, and doing so is the usual fix when the agent isn't drawing on a store you expected it to use.

**What to put in a memory store**

A memory store holds durable, synthesized knowledge—facts about your environment, recurring root causes, standing conventions and directives, and the findings and summaries you distill from past work. Store the conclusion worth recalling later, not raw data.

A memory store is not a scratchpad for a single investigation, and it isn't a key-value cache for a tool's output. You can't stash a tool call's raw result in a store and fetch it back later in the same investigation—during an investigation, the agent already keeps tool outputs in its working context. Instead, record the fact or finding the result established (for example, "the checkout service calls the payments API synchronously"), which the agent can reuse in future sessions.

For the best results:
+ Keep each memory focused on a single fact or lesson rather than a large dump, so the agent can retrieve exactly what it needs.
+ Store what stays true across investigations, and let one-off working data stay in the investigation that produced it.

## Viewing memories
<a name="viewing-memories"></a>

You can view all memory stores and their contents from the **Knowledge** page in your Agent Space Operator Web App.

**To view memory stores:**

1. Navigate to the **Knowledge** page in your Agent Space Operator Web App.

1. Choose the **Memories** tab.

1. Browse the list of memory stores, each showing its name, description, and agent type scope.

**To view memories within a store:**

1. On the **Memories** tab, choose **View** next to the memory store you want to explore.

1. The store detail page lists all memories with their name, description, version number, and last modified date, sorted alphabetically by name.

**To view a specific memory:**

1. From the store detail page, choose **View** next to the memory you want to read.

1. The memory detail page displays the rendered markdown content along with creation date, last modified date, and a version selector.

**To view a previous version:**

1. On the memory detail page, use the version selector dropdown to choose an older version.

1. The content updates to display the selected version.

## Activating and deactivating memories
<a name="activating-and-deactivating-memories"></a>

You can toggle individual memory stores or individual memories active or inactive without deleting them.

**To toggle a memory store:**

1. On the **Memories** tab, use the toggle switch next to the memory store.

1. When inactive, agents do not access any memories within that store.

**To toggle an individual memory:**

1. Navigate into a memory store to see its list of memories.

1. Use the toggle switch next to the memory you want to activate or deactivate.

1. When inactive, agents skip that specific memory during investigations.

## Editing memories with Chat
<a name="editing-memories-with-chat"></a>

You can create, update, or delete memories by chatting with the DevOps Agent in the Chat interface. The Chat agent can write directly to memory stores.

**Examples of Chat commands:**
+ "Remember that the storage service is called Orders Storage Service" - Creates or updates a memory in the directives store.
+ "Update the memory for the canary alarm to note that it is flaky during deployments" - Updates a specific memory in the monitors store.
+ "Delete the memory about the old database connection string" - Removes a memory that is no longer relevant.
+ "Create a memory store called network-quirks and add a note that the eu-west-1 NAT gateway drops idle connections after 350 seconds" - Creates a store and its first memory.

The Chat agent writes directly to memory stores on your behalf.

## Deleting a memory store
<a name="deleting-a-memory-store"></a>

You can delete a custom memory store you no longer need. Managed stores (such as `monitors`, `directives`, and the learned-skill stores) can't be deleted.
+ **In chat**, the agent won't delete a store that still contains memories—it asks you to delete the memories first. Delete the memories, and then delete the store.
+ **In the console**, deleting a store also deletes the memories it contains. This can't be undone, so make sure it's the store you mean to remove.

To delete a store in chat, ask the agent. For example:

```
Delete the network-quirks memory store.
```

## Memory limits
<a name="memory-limits"></a>

The following limits apply to memories:


| Resource | Limit | 
| --- | --- | 
| Memory stores per Agent Space | 50 | 
| Memories per memory store | 200 | 
| Individual memory content size | 100 KB | 