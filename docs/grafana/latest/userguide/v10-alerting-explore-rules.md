

# About alert rules
<a name="v10-alerting-explore-rules"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 10.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

An alerting rule is a set of evaluation criteria that determines whether an alert instance will fire. The rule consists of one or more queries and expressions, a condition, the frequency of evaluation, and the duration over which the condition needs to be met to start firing.

While queries and expressions select the data set to evaluate, a *condition* sets the threshold that the data must meet or exceed to create an alert.

An *interval* specifies how frequently an alerting rule is evaluated. *Duration*, when configured, indicates how long a condition must be met. The alert rules can also define alerting behavior in the absence of data.

**Topics**
+ [Alert rule types](v10-alerting-explore-rules-types.md)
+ [Recording rules](v10-alerting-explore-rule-recording.md)
+ [Queries and conditions](v10-alerting-explore-rules-queries.md)
+ [Alert instances](v10-alerting-rules-instances.md)
+ [Namespaces, folders and groups](v10-alerting-rules-grouping.md)
+ [Alert rule evaluation](v10-alerting-rules-evaluation.md)
+ [State and health of alerting rules](v10-alerting-explore-state.md)
+ [Notification templating](v10-alerting-rules-notification-templates.md)