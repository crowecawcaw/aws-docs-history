

# Resources in Security Hub
<a name="resources-adv"></a>

Security Hub assigns a **criticality** level to each resource in your environment. Criticality indicates how important a resource is to your business, and it helps you prioritize security work. Criticality is one of `Very High`, `High`, `Medium`, `Low`, or `Unknown`.

## How Security Hub infers criticality
<a name="resource-criticality-inference"></a>

By default, Security Hub **infers** criticality from signals on the resource:
+ **Resource name** – Security Hub matches patterns in the resource name. For example, a resource with `pci` or `prod` in its name is treated as more critical than a resource named `sandbox`.
+ **Tags** – Security Hub matches patterns in resource tags. For example, a resource tagged with `environment=production` is treated as more critical than one tagged `environment=dev`.

## Overriding criticality with an automation rule
<a name="resource-criticality-override"></a>

You can override the inferred criticality by creating an automation rule that sets criticality explicitly on resources that match the rule's criteria. An automation rule always takes precedence over inferred criticality. For more information, see [Resource rule actions and criteria](securityhub-v2-automation-rules.md#resource-rules).

## How criticality affects exposure finding severity
<a name="resource-criticality-exposure-impact"></a>

Security Hub uses resource criticality as an input when it calculates the impact and severity of an exposure finding. Resources with a criticality of `Unknown` do not influence exposure finding severity. For more information, see [Impact](exposure-findings-severity.md#exposure-findings-severity-impact).