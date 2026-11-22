

# Resources in Security Hub

Security Hub provides an inventory of the resources in your cloud environment. The **Resources** page lists each resource with its type, account, Region, tags, current configuration, findings, and criticality. The inventory covers your AWS resources and the resources in other cloud providers that you connect to Security Hub. You can filter, sort, and group the inventory, and open a resource to view its details and the findings that affect it. A delegated administrator account can view the resources of all member accounts in its organization. Security Hub records your AWS resources through service-linked configuration recorders and keeps the inventory current as resources are created, changed, and deleted.

Security Hub assigns a **criticality** level to each resource in the inventory. Criticality indicates how important a resource is to your business, and it helps you prioritize security work. Criticality is one of `Very High`, `High`, `Medium`, `Low`, or `Unknown`. Security Hub infers criticality from signals about the resource, such as its name, its tags, the software installed on it, and its usage. You can also set criticality with an automation rule. For each resource, Security Hub records which sources determined the criticality and the reason for each source.

## How Security Hub infers criticality
<a name="resource-criticality-inference"></a>

By default, Security Hub **infers** criticality from the following signals on the resource. Security Hub combines the signals that are available for a resource into one criticality. A signal that isn't available for a resource doesn't lower its criticality.
+ **Resource name** – Security Hub matches patterns in the resource name. For example, a resource with `pci` or `prod` in its name is treated as more critical than a resource named `sandbox`.
+ **Tags** – Security Hub matches patterns in resource tags. For example, a resource tagged with `environment=production` is treated as more critical than one tagged `environment=dev`.
+ **Installed software and packages** – For compute resources that Security Hub monitors, Security Hub analyzes the software bill of materials (SBOM) to identify the software installed on the resource. For example, a resource that runs a database engine, an identity and access service, or a message broker is treated as more critical than a resource that runs only monitoring agents. For more information, see [Software bill of materials](securityhub-v2-sbom.md).
+ **CloudWatch telemetry** – Security Hub reads Amazon CloudWatch metrics that measure resource usage, such as request counts, invocations, messages, consumed capacity, database connections, and network traffic. It compares the resource's usage over the previous 7 days with other resources of the same type in the same account and AWS Region. Security Hub uses the metrics only to infer criticality and doesn't show the metric values.

If Security Hub finds no signals that are specific to a resource, the resource's criticality is `Unknown`. Security Hub doesn't assign a criticality based on the resource type alone.

## Overriding criticality with an automation rule
<a name="resource-criticality-override"></a>

You can override the inferred criticality by creating an automation rule that sets criticality explicitly on resources that match the rule's criteria. An automation rule always takes precedence over inferred criticality. For more information, see [Resource rule actions and criteria](securityhub-v2-automation-rules.md#resource-rules).

## Viewing criticality and its sources
<a name="resource-criticality-view"></a>

The **Resources** page shows the criticality of each resource in the **Criticality** column, and you can sort, filter, and group resources by **Resource criticality**. To see why a resource received its criticality, choose the resource to open its details, and then choose **How this was determined** next to the criticality. The **Resource criticality** panel lists each source and how it was determined. The sources are **Automation rule**, **Tags**, **Resource name**, **Installed software and packages**, and **CloudWatch telemetry**. For example, the CloudWatch telemetry source might read "Usage is at percentile 92 among the 40 Lambda functions in this account and region". The installed software source might read "Runs software that stores data". When an automation rule sets the criticality, the panel shows the rule under **Set by** and lists the inferred signals under **Inferred signals (overridden)**.

Resource criticality also appears on the **Impact assessment** tab of an exposure finding on the resource.

In the API, the [GetResourcesV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetResourcesV2.html) operation returns the criticality in `ResourceCriticality` and lists the sources in `CriticalitySources`. Each source has a `Source`, which is one of `AutomationRule`, `ResourceName`, `TagInference`, `InstalledSoftwareAndPackageInference`, or `CloudWatchTelemetryInference`, and a `Reason`.

## How criticality affects exposure finding severity
<a name="resource-criticality-exposure-impact"></a>

Security Hub uses resource criticality as an input when it calculates the impact and severity of an exposure finding. Resources with a criticality of `Unknown` do not influence exposure finding severity. Because some signals change over time, such as usage and installed software, a resource's criticality can change. Security Hub uses the criticality that was recorded when it evaluated the exposure finding. The severity of an existing finding can therefore differ from what the resource's current criticality implies until Security Hub evaluates the finding again. For more information, see [Impact](exposure-findings-severity.md#exposure-findings-severity-impact).