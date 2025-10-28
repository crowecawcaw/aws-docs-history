# Explore related telemetry

Computer systems can generate a large amount of telemetry, including both metrics and
logs, and complex systems even more so. When looking at a specific set of telemetry, it
can be a challenge to find other telemetry related to your initial set. It can take
advanced training to gain the skills needed to find issues and troubleshoot them. Because
systems are complex, understanding what is going on can involve viewing metrics and logs
from many different services and resources, requiring context switching and navigating
between systems.

The Amazon CloudWatch **Explore related** feature offers access to AWS
resource relationships, related metrics, and logs across service consoles, enhancing
observability and efficiency for operators of all skill levels. When viewing alarms
or anomalies in CloudWatch dashboards, or metrics in AWS, users can quickly find and view
metrics and logs for related resources in your system.

CloudWatch provides visibility into metrics and logs tied to specific resources, and the
**Explore related** pane extends that by allowing you to correlate
your infrastructure resources to your workloads with all of their associated
telemetry. This gives you quick access to the information you need to
troubleshoot infrastructure-related issues. You view the relationship between
resources, and their related telemetry in the **Explore related** pane.
The **Explore related** pane is accessed from CloudWatch or from other AWS
consoles showing resources or telemetry.

###### Note

**Explore related** is currently limited in accounts set up as monitoring accounts in CloudWatch cross-account observability.
You should access **Explore related** from the source accounts where the resources are originally created and managed.
In source accounts, you can navigate between connected resources, and view related logs and metrics.

The following topics discuss the details of exploring related telemetry.

###### Topics

- [What is related telemetry?](#what-is-related-telemetry "#what-is-related-telemetry")
- [How to access the Explore related pane](#access-related-telemetry "#access-related-telemetry")
- [Navigating related telemetry](#using-related-telemetry "#using-related-telemetry")
- [Using the topology map](#using-related-telemetry-map "#using-related-telemetry-map")
- [Finding a specific resource](#using-related-telemetry-find "#using-related-telemetry-find")
- [Permissions and prerequisites needed
  to view and explore related telemetry](#related-telemetry-permissions "#related-telemetry-permissions")
- [How does CloudWatch find related
  telemetry?](how-does-related-telemetry-work.md "how-does-related-telemetry-work.md")
- [AWS services that support related
  telemetry](services-with-related-telemetry.md "services-with-related-telemetry.md")
- [How to add related information to
  custom telemetry sent to CloudWatch](adding-your-own-related-telemetry.md "adding-your-own-related-telemetry.md")

## What is related telemetry?

Related telemetry is metrics and log data from resources that are
related to the current resource or service. Traditionally, you might look at the
metrics and logs that are related to a single load balancer, or all telemetry related
to Amazon EC2. The **Explore related** feature in Amazon CloudWatch adds an
interactive _topology map_. The map is a resource-centric view
where you can find metrics and logs for a specific resource, but you can also see how
that resource is connected to other resources.

For example, if you are looking at the telemetry for a load balancer in the
**Explore related** pane, besides the metrics and logs associated with
that load balancer, the maps shows you the
target groups for that load balancer. Selecting one of the target groups will then
show you the Amazon EC2 instances associated with that target group. At each step in this
process, the telemetry, including metrics and logs, for the selected resources are
shown, making it easy to quickly find the telemetry you are looking for, or to explore
the telemetry, looking for the cause of a specific issue.

## How to access the Explore related pane

Within the CloudWatch console, there are multiple ways to access telemetry related to your
current view. For example, if you are looking at a graph on a dashboard, and you want
to view telemetry related to that graph or an aspect of the graph, you can choose to
explore related data directly from that graph. From many places in the console, you can
choose an **Explore related** menu item, or select a compass
icon (
![Compass icon representing navigation or direction in a user interface.](images/compass-icon.png)
) to show the **Explore related**
pane.

You can access the exploring experience from entry points throughout the CloudWatch
console (and other AWS consoles), including:

- **Metrics navigation** – When you choose
  **Metrics** then **All metrics** from the CloudWatch
  console left hand menu, the tile for any supported service or metric source will
  show the compass icon that brings up related telemetry in the bottom right
  corner.
- **Metric legend** – When viewing any
  metric graph (in CloudWatch or other AWS consoles), hovering over the legend of
  the graph shows information about the data, as well as an **Explore
  related** button that brings up the related telemetry.
- **Metric datapoints** – When viewing any
  metric graph, hovering over a datapoint in the graph shows information about
  the metric, as well as a compass icon, to bring up the related telemetry.
- **Metric search** – When searching for
  metrics in CloudWatch, if you choose a found metric name, you can select
  **Explore related** from the menu that pops up, which will
  bring up the related telemetry.
- **Console toolbar** – In many AWS
  console pages, the console toolbar (usually in the upper right of the console)
  includes a CloudWatch service icon, which will bring up CloudWatch tools, including the
  **Explore related** pane.

Depending on where you access the pane from, the default context of the pane will
show an appropriate filter, if possible.

## Navigating related telemetry

When you select any of the entry points to the **Explore related**
pane, it appears on the right side of the CloudWatch console. This pane gives you access to
view and find telemetry related to _entities_, in your system. An
entity is a resource, such as an Amazon EC2 instance, or a service, such as an
application that you have built. You can work within this pane without interrupting
your current workflow, because it opens to the side of your initial page.

The following image shows the **Explore related** pane focused on a
single Amazon EC2 instance, and the associated entities.

![The Explore related pane, with a single Amazon EC2 instance in focus, and its associated entities.](images/compass-explore-main.png)

The top of the **Explore related** pane is a visual
_topology map_ (map) of the current entity and other related
entities. The currently selected entity sets the focus for the pane. There are two ways
to select an entity.

- [Topology map](#using-related-telemetry-map "#using-related-telemetry-map") – The
  _map_ is a visual display of the current entity with
  focus. It also displays any related entities, allowing you to navigate around the set of resources
  and services that are related to each other.
- [Find other resources](#using-related-telemetry-find "#using-related-telemetry-find")
  – You can use the **Find other resources** button to
  filter and search for entities to use as the focus.

The bottom part of the pane shows you an automated search of metrics and logs for
the current focal entity.

By default, the focus is set to an entity matching the location from which
you accessed the **Explore related** pane. For example, if you
accessed it by clicking the compass icon associated with a metric from a specific
Amazon EC2 instance, then the focus will be set to that Amazon EC2 instance.

When you select an AWS resource for the focus in the **Explore
related** pane, you can navigate to the resource-specific console for the
selected resource. For example, if you have selected an Amazon EC2 instance, you can select
the **View in EC2 console** link to open the Amazon EC2 console with that
instance selected.

When you set a focus, the metrics and logs are automatically filtered to show the
telemetry related to your focus.

- **Metrics** – Each metric is shown as a
  graph for the time period that you have chosen.

Much like any dashboard graph in CloudWatch, you can hover over or select a graph
to get more information about the metric graph, and to see options including
viewing in CloudWatch metrics. Choosing to view in CloudWatch will open the metrics view
with the same viewing context as the **Explore related** pane,
including resource and time range.

- **Log patterns** – CloudWatch analyzes the log
  groups associated with the focal resource and shows common patterns in those
  logs. For more information about log patterns, see
  [Pattern analysis](../logs/CWL_AnalyzeLogData_Patterns.md "../logs/CWL_AnalyzeLogData_Patterns.md") in the _Amazon CloudWatch Logs
  User Guide_.

You can select **Compare timerange** to choose another time
range and compare logs across the two time ranges.

You can select **View in Logs Insights** to analyze the logs
in CloudWatch Logs Insights with the same options as your current view, including resource,
log group, and time range. For more information, see [Analyzing log data
with CloudWatch Logs Insights](../logs/AnalyzingLogData.md "../logs/AnalyzingLogData.md") in the _Amazon CloudWatch Logs User
Guide_.

- **Log groups** – The [log groups](../logs/Working-with-log-groups-and-streams.md "../logs/Working-with-log-groups-and-streams.md") that contain the logs are shown.

You can select the log groups and then perform one of the following
actions:

    + Choose **Start tailing in Live Tail** to view a
     streaming list of new log events as they are ingested for the selected
     log groups. The Live Tail session is started in the CloudWatch console. For
     more information on Live Tail, see [Troubleshoot with CloudWatch Logs LiveTail](../logs/CloudWatchLogs_LiveTail.md "../logs/CloudWatchLogs_LiveTail.md") in the *Amazon CloudWatch Logs
     User Guide*.
    + Choose **Query in Logs Insights** to open Logs
     Insights with a query scoped to just those log groups, applying your
     current context, including resources and time range.

## Using the topology map

The _topology map_ (map) is a visual display of the current
focal entity and its related resources or services. You can use this interactive
visualization to see the connections between different resources and services,
and explore the relationships between components in your system. For example,
if you are viewing _load balancer_ resource, the map will show
connected _target group_ resources. Selecting a target group
will display the associated instances. The visualization of connectivity helps
operators understand and explore the relationships between different resources
and services in your system.

You can drag the map, and zoom in and out, to see more of the associated
entities, or to focus on fewer entities.

When you select an associated entity, like a target group, the pane's focus shifts
to show telemetry for that entity. The map updates to center on the selected target
group, displaying its connections to other entities, such as the load balancer and
and any Amazon EC2 instances that are specified in that target group. As you navigate
through different entities in the map, the metrics and logs at the bottom of the pane
dynamically update, providing you with relevant telemetry for the newly selected
resources.

## Finding a specific resource

If a resource doesn't appear on the topology map, you can use the **Find
other resources** feature to locate it. You can filter resources by tag or
type, then select the ones you are looking for. After you have found resources to
focus on, you are returned to the topology map, with those resources selected, to
browse associated entities and telemetry.

###### Note

There are many reasons why you might not see your resources on the topology map.
For example:

- It's not related to the current focal entity.
- You don't have [permissions](#related-telemetry-permissions "#related-telemetry-permissions") to access associated entities or
  telemetry.
- The [resource or
  service](services-with-related-telemetry.md "services-with-related-telemetry.md") may not support telemetry or associated
  entities.

By using **Find other resources**, you can discover and visualize
resources that may not be directly connected or visible in the current map. This
ensures that you can access and analyze all relevant components of your
infrastructure.

###### Select a resource with Find resources.

1. Open the **Explore related** pane from any of the
   [entry points](#access-related-telemetry "#access-related-telemetry") in the
   CloudWatch console.
2. Choose **Find resources**.
3. Choose the time frame for which you want to view logs or metrics.
4. Choose **Resource
   types**, then select the type of the resource you want to focus on
   from the drop down list, for example, **EC2 instances**.
5. Optionally, filter the set of resources by providing a tag to filter on. You
   can do this by selecting the **Filter resources by tags**
   filter, or by choosing the label that says **5 tags found**
   (the number will depend on the tags in your system). This gives you a list of
   tags to choose from.

After you have selected the tags, the list of resources is automatically
filtered to only those that are associated with those tags. 6. Optionally, choose one or more specific resources from the ones found that
match your filters. 7. Choose **Show on map** to return to the **Topology
map** with your resources selected.

Your list of **Metrics** and **Logs**
is now filtered to just logs and metrics that are associated with that
resource type. You can choose the **Metrics** or
**Logs** tab to view the kind of telemetry that you want to
view.

## Permissions and prerequisites needed

to view and explore related telemetry

To explore related telemetry, you must be getting entity information with the
telemetry from your workloads, and you must have the proper permissions to view
that data.

Many services send entity information automatically. For workloads that use the CloudWatch
agent, you must have at least version `1.300049.1` of the agent, and you must
configure it correctly. For information about configuring the agent, see
[How to add related information to
custom telemetry sent to CloudWatch](adding-your-own-related-telemetry.md "adding-your-own-related-telemetry.md"). For workloads running on Amazon EKS, you
must have at least version `v2.3.1-eksbuild.1` of the Amazon CloudWatch
Observability EKS add-on. For more information about this add-on, see
[Quick start with the Amazon CloudWatch
Observability EKS add-on](Container-Insights-setup-EKS-addon.md "Container-Insights-setup-EKS-addon.md").

To explore related telemetry you must be signed in with certain permissions.
Exploring related telemetry is a read-only activity, and requires at least read-only
access to CloudWatch.

The permissions needed for viewing associations between telemetry and entities
are: `logs:ListLogGroupsForEntity`,
`logs:ListEntitiesForLogGroup`,
`cloudwatch:ListEntitiesForMetric`, and
`application-signals:ListObservedEntities`.

Each of the following AWS managed policies will provide the CloudWatch permissions
needed to access related telemetry in the CloudWatch console:

- [CloudWatchFullAccessV2](../../../aws-managed-policy/latest/reference/CloudWatchFullAccessV2.md "../../../aws-managed-policy/latest/reference/CloudWatchFullAccessV2.md") – Provides full access to CloudWatch.
- [CloudWatchReadOnlyAccess](../../../aws-managed-policy/latest/reference/CloudWatchReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/CloudWatchReadOnlyAccess.md") – Provides read-only access to
  CloudWatch.
- [ReadOnlyAccess](../../../aws-managed-policy/latest/reference/ReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/ReadOnlyAccess.md") – Provides read-only access to AWS
  services and resources.

Additionally, you must have at least read-only access (`Describe*`
and `Get*`) to any resources in the topology map, in order for CloudWatch to
discover and display relationships.

For more details about using policies to control access, see [Managing access using policies](auth-and-access-control-cw.md#security_iam_access-manage "auth-and-access-control-cw.md#security_iam_access-manage").
