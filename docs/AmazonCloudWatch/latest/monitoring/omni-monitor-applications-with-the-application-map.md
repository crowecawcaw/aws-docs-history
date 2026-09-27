

# Monitor applications with the application map
<a name="omni-monitor-applications-with-the-application-map"></a>

Use the application map to understand how your applications and services interact with each other and to identify what needs the most attention. The application map shows your application services, their dependencies, and related cloud resources. You can also organize your application map by other dimensions such as environment, resource type, or related services.

Omni builds the application map from your telemetry for the time range you select. It then adds the infrastructure resources that it finds in your account. Omni observes service calls and resource access. It draws each one as an arrow between two nodes. When the map is grouped by application, Omni groups services by the OpenTelemetry `service.namespace` attribute. The `service.name` attribute names each service in that application. Services that do not set the `service.namespace` attribute are grouped under **None**. Services running in other clouds appear alongside your AWS services when their telemetry carries the standard OpenTelemetry resource attributes, and calls between them are drawn like any other.

You can access the application map from the Quick Launch menu in the Omni web UI. You can also access the underlying Context Graph programmatically. See [Using Context Graph](omni-using-context-graph.md).

**Find which services need your attention**

Start with the application map to find which applications have problems, and which service or dependency is responsible.

1. Select the time range that contains the behavior you want to investigate.

1. Find the application you want to review.

1. Use the **Health** filter to focus on services or dependencies that need attention. Health status for an application is "critical" if the percentage of errors is greater than 5%, and "warning" if it is greater than 1%.

1. Select a service to review its activity and relationships.

1. Open the service or its telemetry when you need more detailed evidence.

For detailed service monitoring, see [Monitor a service](omni-monitor-a-service.md). To investigate individual requests and operations, see [Application traces](omni-application-traces.md).

**Understand what appears on the map**

![Application map showing the two kinds of node and the three kinds of relationship between them.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/omni-application-map.png)


The map is your application's observed topology, drawn from two kinds of nodes and three kinds of relationship between them.


| Node | What it is | 
| --- | --- | 
| Service | An instrumented application that sends its own telemetry. | 
| Resource | A resource that a service uses or runs on, including managed and customer-deployed resources such as a database, queue, bucket, function, or compute. | 

Nodes also carry a category, which determines the icon shown on the map: compute, storage, database, messaging/queue, Gen AI model, network, or uncategorized.


| Relationship | What it means | 
| --- | --- | 
| Calls | One service calls another service. | 
| Accesses | A service reads from or writes to a resource. | 
| Runs on | A service is hosted on a piece of infrastructure, such as a cluster. | 

A relationship can also contain operations observed between its nodes. For example, you can see which operations one service called on another service or resource. Node health reflects the error rate observed over the selected time range. A node is reported as one of the following:
+ **Healthy** — the observed error rate is within normal range.
+ **Warning** — the error rate is elevated.
+ **Critical** — the error rate is high.
+ **Unknown** — the node has too little traffic to classify. A low-traffic node is reported as unknown rather than as healthy.

**Investigate an application or a service from the map**

Select an application or a service to review information for the selected time range. The service view can include request activity, latency, errors, and its relationships with other services and resources. Review the services that call the selected service, the services it calls, and the resources it accesses. This helps you determine whether the problem is isolated to the service or involves a dependency. From the service, continue to the telemetry:

1. Open traces to investigate individual requests.

1. Open logs to inspect application messages, exceptions, or events.

1. Open metrics to investigate service or infrastructure signals.

**Narrow and organize the map**

The map opens grouped by **Application**, so it shows your applications rather than every individual service. Use the **Analysis** rail when a large map contains more nodes than you need for the current investigation. Use **Group by** in the analysis rail to change the grouping dimension. For example, if your services run in multiple environments, group by **Environment** to focus on all services in a given environment.

Use **Filter** to narrow the map without changing its grouping. You can filter by node properties such as Health, Type, and Instrumentation, or by attributes such as **Application**, **Service Name**, **Environment**, **Platform**, and **Resource type**.

Use **Show all infrastructure** to include resources discovered in your account even when Omni has not observed them through telemetry. Use **Node style** to switch the node view between cards and circles.

**What to watch out for**

1. **Most relationships on the map come from your telemetry.** A service that is not instrumented appears as a single node with no related telemetry if Omni discovers it in your account. It can also appear as a node named from a caller's span, because the caller's telemetry names the far end of the call. The map draws a call between two of your services when you trace it. Omni also builds relationships from network and access logs, from CloudTrail, and from the resources it discovers in your account. To close a gap, instrument the service that is missing. See [Send telemetry to CloudWatch Omni](omni-send-telemetry.md).

1. **Individual hosts, tasks, and identities are left out on purpose.** The map does not create nodes for EC2 instances, ECS tasks and containers, or IAM roles and users. Leaving these out keeps the map focused on your services and their dependencies.

1. **Two nodes can carry the same service name.** Omni creates a separate node for each combination of AWS account, AWS Region, cloud provider, and deployment environment. Each combination is a separate deployment of the service. The service details page shows a node's account, Region, and cloud provider as node attributes, so you can tell two deployments apart there. Set those attributes consistently. If some replicas of one service set `deployment.environment` and others leave it unset, Omni splits that service into more than one node and divides its traffic and dependencies between them. See [Using Context Graph](omni-using-context-graph.md).

1. **Resources that Omni finds by inspecting your account appear on a delay, and the time range does not filter them.** Telemetry updates the map continuously, and telemetry-derived nodes are the ones observed inside the range you select. A resource that Omni learns about by discovering what is deployed in your account appears after the next scheduled refresh. It then reflects the most recent discovery rather than the selected range, so narrowing the range does not remove it. Such a resource can appear with its name before anything has called it, and it shows no metrics or traces because Omni has not observed any. For which discovery sources contribute what, see [Using Context Graph](omni-using-context-graph.md).

**Where to go next**


| To do this | See | 
| --- | --- | 
| Open a single service, its dependencies, and its health | [Monitor a service](omni-monitor-a-service.md) | 
| Follow one request through your services | [Application traces](omni-application-traces.md) | 
| Query the logs, metrics, and traces behind a node | [Explore and query your telemetry](omni-explore-and-query-your-telemetry.md) | 
| Understand spaces and where this telemetry is stored | [CloudWatch Omni](cloudwatch-omni.md) | 

**Cross-account and cross-Region topology**

The map shows the services and resources in the space's own account and Region. To add more accounts and Regions, centralize their telemetry into the space's account. Their services and dependencies then appear on the same map. To set this up, see [Set up Omni for your organization](omni-set-up-omni-for-your-organization.md).