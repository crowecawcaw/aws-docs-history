

# Managed memories

AWS DevOps Agent creates and maintains managed memories as it learns from activity in your Agent Space. A background learning agent runs a set of scheduled tasks that analyze your Agent Space and your recent investigations. You don't maintain managed memories yourself. You can read, search, and deactivate them, and you can update them through Chat, but you can't delete a managed store. For more information about how agents read memories, see [DevOps Agent Memories](about-aws-devops-agent-devops-agent-memories-index.md).

AWS DevOps Agent previously presented some of this knowledge as *learned skills*. It now keeps the same knowledge as memories, in the stores on this page.

## Learning tasks
<a name="learning-tasks"></a>

Each task appears on the learning agent's **Triggers** tab with the last time it ran. For more information, see [Managed agents](working-with-devops-agent-managed-agents.html#triggers-tab).

The learning agent writes every managed store except `directives`, which you write through Chat. For more information, see [Directives](#directives).

### Build agent space understanding
<a name="build-agent-space-understanding"></a>

This task builds the system architecture of your Agent Space from your cloud resources, application code, observability integrations, and custom MCP servers. It runs after initial resource discovery and refreshes at most every 3 days. It writes the `understanding-agent-space` store, which holds a map of the resources in your Agent Space and how they connect. The map includes:
+ An overview of your system and its key domain concepts.
+ Your deployment environments, such as AWS account and Region pairs or Azure subscriptions and regions.
+ A container-level architecture that shows how your logical services connect.
+ The request paths that matter most to your application, and the components each path passes through.
+ A mapping of code repositories to containers.

The store keeps a memory for each logical container. Each container memory lists the container's components, such as compute, data, messaging, and network resources. For each component, it gives the resource types and identifiers, such as ARNs, table names, and queue URLs. It also lists the component's alarms, dashboards, and monitors, and maps the component to its code repositories, packages, and infrastructure-as-code definitions. With this map, the agent can trace a deployed resource back to the code that defines it.

The store also keeps a memory for each critical request path. A path memory describes each step of the request, from its entry point through each intermediate service, data store, and external dependency. It also records how each component calls the next. The memory also lists the signals to check along the path: the log groups for each step, the key metrics such as latency, error rates, throttling, and token quotas with their alarm names and dimensions, and the trace spans to correlate across services and accounts.

### Learn monitor root causes
<a name="learn-monitor-root-causes"></a>

This task learns the recurring root causes of each monitor and alarm from recent investigations, so the agent recognizes them when they fire again. It writes the `monitors` store. Each memory covers one monitor, such as an alarm or a metric, and lists the causes that produced incidents for it, with evidence from each investigation. When an alarm fires, agents read its memory before triage to check whether the incident matches a known cause.

The task runs daily. A monitor memory expires 14 days after its last update, and the task drops a root cause once all of its evidence is older than 14 days.

Each root cause has two possible sources: the investigation and your operators. When your Agent Space is connected to a ticketing integration such as PagerDuty or ServiceNow, the task also reads the comments on the ticket that raised each investigation. From those comments, it takes the root cause that the operator recorded when they resolved the ticket. It records whether that cause matches the cause the investigation found. When operators disagreed with an investigation, the memory records that, so later investigations see the operator's cause next to the agent's.

### Run memory dreaming
<a name="run-memory-dreaming"></a>

This task keeps your managed memories accurate as they go out of date, stop applying, or mislead investigations. For example, a root cause can stop holding after a redesign, two monitor memories can record the same cause, or a reflection can contradict a monitor memory. The task runs once a week and learns from how agents actually used each memory. It works on *claims*, the individual facts inside a memory, such as one root cause of an alarm with the investigations that established it.

The learning agent reviews your recent investigations and custom agent runs. For each claim that a run read, it records three verdicts:
+ **Outdatedness:** whether the claim still held, given what the run observed.
+ **Applicability:** whether the claim was about the problem the run worked on.
+ **Impact:** whether the claim steered the run, didn't help, or misled it away from the root cause that your operators recorded on the resolved ticket.

From these verdicts and the investigations behind each claim, the task deletes claims that no longer hold or that keep misleading investigations, merges duplicate claims, and resolves contradictions between memories. It also rewrites each claim's conditions so they name the evidence to collect. It decides each change from the raw records of those investigations, and a directive in your [`directives` store](#directives) can protect a claim or forbid a merge. The task records every change with its reason, its evidence, and the text before and after, and each change creates a new version of the memory. To see what changed, open the memory and choose an earlier version from the version selector.

### Build knowledge graph
<a name="build-knowledge-graph"></a>

This task links your topology, monitor, reflection, and tool-use memories into the knowledge graph, so agents can move from one memory to related ones. It runs every 3 days. For example, an alarm's monitor memory, a reflection on a past mistake with that alarm, the topology of the component that owns it, and the tool-use guidance for the query that checks it all describe one problem. The task finds pairs of memories that are likely related, judges each pair, and keeps a relationship only when a quote from each memory supports it. Each relationship has one of these types:
+ **Same incident:** Both memories describe the same real event, such as the same ticket, change, or dated incident.
+ **Correlated alarm:** Both memories are alarm monitors that fire together, cause each other's symptoms, or give different causes for the same symptom.
+ **Upstream component:** A topology memory names the component that owns an alarm, or a component earlier in the request path that might cause the alarm's symptom.
+ **Past mistake:** A past investigation reached a cause that a monitor memory records, and later found that the cause was wrong.
+ **Condition definition:** One memory checks a metric, alarm, or log field, and the other defines it.
+ **Runnable check:** One memory calls for a check, and the other holds the exact way to run it.

When an agent reads a memory, it can follow these relationships to the connected memories. For example, from an alarm's monitor memory, the agent can go straight to a reflection on an earlier wrong conclusion, the topology of the component that owns the alarm, and the query to run. For more information about browsing the graph, see [Viewing memories and the knowledge graph](about-aws-devops-agent-devops-agent-memories-index.html#viewing-memories-and-the-knowledge-graph).

### Learn tool-use best practices
<a name="learn-tool-use-best-practices"></a>

This task learns from your recent investigations how the agent can use its tools better, so it avoids known errors and wastes fewer steps. It runs after 10 new investigations complete, at most every 3 days. It writes the `tool-use-best-practices` store. The store keeps a routing memory that lists each tool with the investigation scenarios it supports, and a memory for each category of tools. The guidance for a tool can include three sections:
+ **Best Practices:** Techniques from successful investigations, such as CloudWatch Logs Insights query templates, the metric namespaces and dimensions in your environment, and CloudTrail event source filters. Each entry covers one investigation scenario, with the parameter values and examples from past investigations.
+ **Common Errors:** Errors that recur, with their fixes. Each entry describes one error, such as querying an account the agent can't access or writing an aggregation query that doesn't parse, and the action that avoids or fixes it.
+ **Output Management:** Guidance for tool calls that return large responses. Each entry describes a parameter change or a processing step that makes the output smaller and keeps the details that matter for diagnosis.

When the agent can access your infrastructure, AWS DevOps Agent checks each pattern against your environment before adding it. The memory states confirmed patterns directly, marks unconfirmed patterns as unconfirmed, and leaves out patterns that the check disproved.

### Learn chat tool-use best practices
<a name="learn-chat-tool-use-best-practices"></a>

This task learns from your recent chat sessions how the agent can use its tools better in Chat. It runs after 10 new chat sessions, at most every 3 days. It writes the `chat-tool-use-best-practices` store, which holds the same kind of guidance as the `tool-use-best-practices` store.

### Reflect on investigation feedback
<a name="reflect-on-investigation-feedback"></a>

This task learns from your feedback on recent investigations. It runs at most once a day, after you mark an investigation incorrect and enter its actual root cause. It writes the `reflections` store, which holds lessons about what past investigations missed. When you submit feedback on an investigation, AWS DevOps Agent creates a memory that explains why the actual root cause differs from what the investigation found. Later investigations of the same alarm read the memory so they don't repeat the mistake.

For more information, see [Provide feedback on investigations](production-operations-autonomous-incident-response.html#provide-feedback-on-investigations).

### Map pipeline topology
<a name="map-pipeline-topology"></a>

This task maps your deployment pipelines, so the agent knows how changes reach production. It writes the `understanding-pipeline-topology` store, which maps each of your pipelines from start to finish, including its steps, environment promotions, and deployments. With this map, the agent can tell production from pre-production environments and see where a change is in the release process.

### Map service dependencies
<a name="map-service-dependencies"></a>

This task maps how your services and components depend on one another. It writes the `understanding-dependencies` store: which services call which, which events flow between them, which packages they share, and where infrastructure boundaries are. The agent uses this map to assess the blast radius of a change, find upstream and downstream impact, and work out the order of deployments.

## Directives
<a name="directives"></a>

The `directives` store is the one managed store that no learning task writes. It holds standing instructions that you give the agent, such as infrastructure conventions or naming preferences, and you add them through Chat.

Examples:
+ "Lambdas are no longer used. The service uses Fargate."
+ "The storage service is called Orders Storage Service."