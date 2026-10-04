

# Alert rule types
<a name="v13-alerting-explore-rules-types"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 13.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).

Grafana supports several alert rule types. Learn more about each of the alert rule types, how they work, and decide which one is best for your use case.

## Grafana managed rules
<a name="v13-alerting-explore-rule-types-grafana"></a>

Grafana managed rules are the most flexible alert rule type. They allow you to create alerts that can act on data from any of your existing data sources.

In addition to supporting multiple data sources, you can add [expressions](v13-panels-query-xform-expressions.md) to transform your data and express alert conditions.

In Grafana managed alerting:
+ Alert rules are created within Grafana, based on one or more data sources.
+ Alert rules are evaluated by the alert rule evaluation engine from within Grafana.
+ Alerts are delivered using the internal Grafana Alertmanager.

**Note**  
You can also configure alerts to be delivered using an external Alertmanager, or use both internal and external Alertmanagers. For more information, see [Add an external alertmanager](v13-alerting-setup-alertmanager.md).

## Data source managed rules
<a name="v13-alerting-explore-rule-types-datasource"></a>

To create data source managed alert rules you must have a compatible Prometheus or Loki data source. You can check if your data source supports rule creation via Grafana by testing the data source and observing if the Ruler API is supported.

In data source managed alerting:
+ Alert rules are created and stored within the data source itself.
+ Alert rules can only be created based on Prometheus data.
+ Alert rule evaluation and delivery is distributed across multiple nodes for high-availability and fault tolerance.