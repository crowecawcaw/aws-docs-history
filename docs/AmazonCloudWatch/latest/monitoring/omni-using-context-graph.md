

# Using Context Graph
<a name="omni-using-context-graph"></a>

Use the Context Graph to understand the services, resources, and relationships that Omni has identified in your environment. Omni builds the graph from your telemetry and from resources it discovers in your account. A dependency is one kind of relationship: evidence that one component called another. The application map is a visual view of this graph. For the node and relationship types shown on the map, see [Monitor applications with the application map](omni-monitor-applications-with-the-application-map.md).

**Note**  
Omni builds the graph from telemetry you are already sending and from the resources it finds in your account. You do not need to create or maintain the graph. The telemetry and resource attributes you send determine how completely and accurately Omni represents your environment.

**Understand what contributes to the graph**

Different telemetry signals contribute different information.


| What you send | What it contributes | 
| --- | --- | 
| Traces | The caller, the callee, and the dependency between them. Traces establish service-to-service call relationships. | 
| Metrics | A node for the component that emitted the metrics. Metrics alone do not establish a dependency. | 
| Logs | A node for the component that emitted the logs. When a log identifies its compute, Omni can also associate the service with that compute. | 
| Network and access logs | Communication observed between endpoints. Omni can resolve those endpoints to known resources when enough resource information is available. | 

A dependency appears when Omni has evidence that one component called another. A trace is the most direct evidence. Network logs, access logs, and CloudTrail also carry that evidence for some call paths. Metrics do not, so two services that only emit metrics can both appear with no dependency between them. To capture service-to-service dependencies reliably, instrument the caller and send traces. See [Send telemetry to CloudWatch Omni](omni-send-telemetry.md).

**Understand discovered resources**

Omni can also add resources that it discovers in your account. A discovered resource can appear in the graph before Omni observes telemetry from that resource. In that case, the resource exists in the graph but has no telemetry attached to it. This is expected and does not necessarily indicate an instrumentation problem.

Telemetry and discovery use different time semantics. Discovered resources reflect the most recent inventory available to Omni. Changing the telemetry time range does not remove a discovered resource that had no activity during that period. A resource can therefore exist in the graph without any observations in the selected time range.


| Discovery source | What it adds | 
| --- | --- | 
| AWS Config | Resources that AWS Config records in your account. This source adds resource nodes. It also adds some relationships, such as the compute a service runs on. | 
| Resource discovery | Services and resources found by inspecting your account, and the relationships between them: which compute a service runs on, and which resources it accesses. | 

Omni creates a service-linked configuration recorder when you create a space. AWS Config then records a fixed set of resource types. Omni adds those resources to the Context Graph. You do not create the recorder. You do not configure it. You pay no AWS Config fee for the records that Omni uses.

Omni adds a graph node for only some of the types. It uses the other records to add detail to nodes that exist. For the full list, see [Using AWS Config for resource discovery](omni-using-aws-config-for-resource-discovery.md).

**Important**  
**Discovery reports current state rather than a time window.** Telemetry-derived elements are the ones observed inside the time range you request. Discovery-derived elements reflect the most recent discovery of your account, so narrowing the time range does not narrow them. A graph made only of discovered resources reports no observations in the range at all.

**Make services appear correctly**

Use consistent OpenTelemetry resource attributes so Omni can identify services and deployments correctly.

**Identify each service**: Set `service.name` on every service. If a service is missing from the graph, verify this attribute first.

**Group services into an application**: Set `service.namespace` on related services so they are grouped into the same application.

**Distinguish deployments**: Use `deployment.environment` to distinguish deployments such as production and staging.

**Important**  
Set identity attributes consistently across every replica of a service. Two replicas that declare **different** values become separate nodes and split their telemetry. A replica that leaves an attribute unset folds onto the replica that declares it.

**Identify managed dependencies**: Add the attributes that name the destination to the calling span. Omni then resolves the dependency to a known resource. OpenTelemetry semantic conventions define these attributes. Supported AWS SDK instrumentation can set many of them for you.


| When the call is to | The span needs | 
| --- | --- | 
| A queue or topic | messaging.destination.name | 
| A database or table | db.namespace (or db.name). Add db.collection.name for the table or collection. | 
| An object store bucket | aws.s3.bucket | 
| A function | faas.invoked\_name | 
| A model | gen\_ai.request.model | 

If a span contains only a hostname, Omni can represent the dependency by that hostname rather than by the underlying resource. For a call between two services, the span must also represent the outbound call: a span that records only work received does not establish an outgoing dependency to another service. Messaging is the exception. A consumer that polls a queue or a topic gets a relationship to that queue or topic.

**Retrieve the graph programmatically**

Use the `GetContextGraph` operation to retrieve the Context Graph through the API. Authenticate the request the same way as other Omni API operations.

Each request includes a time range. Nodes and relationships from telemetry show the activity in that range. Discovered resources show the latest inventory instead. The time range does not limit them. Results can span several pages.

**Important**  
Relationships are returned with their source nodes rather than as one top-level edge list. When you process a response, iterate through the nodes and read the relationships attached to each node.

Omni attaches each relationship to the node it starts from. A node carries all of its outbound relationships on the page that carries the node. They are never split across pages. To find what points at a node, you must read the nodes at the far end, and those nodes can be on a later page. Read all pages before you decide what depends on a node.

Node and relationship kinds in the response use the same model the application map presents. Each node also reports which signals it was seen in and which sources contributed it. The graph carries no evidence that a dependency does *not* exist.

**Pivot from the graph to your telemetry**

Each node carries the attribute values that identify its own telemetry, so you can move from a dependency on the graph to the metrics, logs, and traces behind it. Use those attribute values as the selectors in your query. For the query languages, see [Explore and query your telemetry](omni-explore-and-query-your-telemetry.md).

This applies to nodes that telemetry contributed. A resource that Omni discovered in your account and never saw in telemetry carries no signals, no operations, and no metrics, so check `signalTypes` before you query a node's telemetry. An empty `signalTypes` means Omni observed no telemetry for that node inside the range you requested. It does not mean the resource was never used.

A node reports its attributes in several forms, and the difference matters when you query.


| On the node | What it is, and when to use it | 
| --- | --- | 
| Normalized identity properties | The resolved identity Omni settled on after merging what it observed across sources. Use these to identify and display a node. | 
| Telemetry attributes | The OpenTelemetry attributes as your telemetry emitted them. Use these to query, because they are the values the stored telemetry carries. | 
| Operation details | For each operation observed on the node, the attribute sets that identify that operation's metric series. Use these attribute sets to chart one operation rather than the whole service. | 
| Per-metric metadata | For each metric on the node: its name, its meaning, its unit, the statistic to chart, and the attributes to query it with. Request this explicitly. See the following note. | 

**Note**  
Omni returns per-metric metadata only when you ask for it, because it costs an extra lookup for every node in the response. Operation details are returned either way.

**Important**  
**Query a metric using the attributes reported for that metric rather than the node's identity.** A node that Omni merged from several sources can carry different attribute values for different metrics. The per-metric attributes match the emitted series. The node's resolved identity might not match, and a query built from it can return nothing even though the metric exists.

A node that telemetry contributed also reports when Omni first and most recently observed it. Compare those timestamps, or run the same request over two ranges, to see whether something appeared, disappeared, or stopped being exercised. A resource known only from discovery might report neither, because Omni has not observed it in use.

**Name your operations**

Omni names an operation from the semantic-convention attributes on the span, and it prefers the most specific set of attributes. Omni also records the span name as an operation. When the two names match, they merge into one operation. When they differ, you see both. If a span records the route it served, Omni names the operation for that route rather than for the method alone.


| Record this | And an operation is named | 
| --- | --- | 
| http.request.method and http.route | By method and route together, such as a GET on a specific path, rather than by method alone | 
| db.operation.name with db.namespace or the table | By the database operation and what it acted on | 
| messaging.destination.name and messaging.operation.type | By the destination and the kind of messaging operation | 

Record the route. Without it, Omni names one operation for each HTTP method, and every request the service handles is grouped into that operation.

**Use the graph with an AI agent**

An AI agent can use the Context Graph to retrieve topology while answering a question or investigating a problem. The agent can verify relationships between services and resources before using those relationships as evidence in its analysis.

For how to connect an agent to Omni, see [Use Omni skills](omni-use-omni-skills.md).

**Troubleshoot an incomplete graph**

Check the following when the graph does not show what you expect:

1. **Relationships come from your telemetry.** A service-to-service dependency requires trace evidence of the call, so a call that is never traced is not a relationship. Other signals identify a component without establishing the dependency. A service that sends no telemetry appears only if Omni discovers it in your account, and it then appears with no telemetry attached.

1. **A single page is not the whole graph.** One response page can contain only part of the graph, or only some of a node's relationships.

1. **Omni identifies a resource from its resource identifier.** Where Omni can resolve a managed resource to a resource identifier, it represents the resource. Where it cannot, the same dependency can appear as a host, an endpoint, or an address instead.

1. **The time range changes what telemetry contributes.** Telemetry-derived nodes and relationships appear only when Omni observed them during the range you request, so a dependency exercised once a day is absent from a one-hour window. That absence is not evidence that the dependency does not exist.

1. **Discovered resources report current inventory.** Resource discovery is not constrained by the telemetry time range, so discovered resources reflect the latest inventory regardless of the range you choose.

**Where to go next**


| To do this | See | 
| --- | --- | 
| Read the map, group it, and open a service from it | [Monitor applications with the application map](omni-monitor-applications-with-the-application-map.md) | 
| Instrument a service so it appears in the graph | [Send telemetry to CloudWatch Omni](omni-send-telemetry.md) | 
| Query the telemetry behind a node | [Explore and query your telemetry](omni-explore-and-query-your-telemetry.md) | 