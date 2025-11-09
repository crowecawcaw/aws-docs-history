# Exploring alerting

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Whether you’re starting or expanding your implementation of Grafana Alerting,
learn more about the key concepts and available features that help you create,
manage, and take action on your alerts and improve your team’s ability to resolve
issues quickly.

First of all, let’s look at the different alert rule types that Grafana Alerting
offers.

## Alert rule types

**Grafana-managed rules**

Grafana-managed rules are the most flexible alert rule type. They allow
you to create alerts that can act on data from any of our supported data
sources. In addition to supporting multiple data sources, you can also add
expressions to transform your data and set alert conditions. This is the
only type of rule that allows alerting from multiple data sources in a
single rule definition.

**Mimir and Loki rules**

To create Mimir or Loki alerts you must have a compatible Prometheus or
Loki data source. You can check if your data source supports rule creation
via Grafana by testing the data source and observing if the ruler API is
supported.

**Recording rules**

Recording rules are only available for compatible Prometheus or Loki data
sources. A recording rule allows you to pre-compute frequently needed or
computationally expensive expressions and save their result as a new set of
time series. This is useful if you want to run alerts on aggregated data or
if you have dashboards that query computationally expensive expressions
repeatedly.

## Key concepts and features

The following table includes a list of key concepts, features and their
definitions, designed to help you make the most of Grafana Alerting.

| Key concept or feature    | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Data sources for Alerting | Select data sources you want to query and visualize<br>metrics, logs and traces from.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Provisioning for Alerting | Manage your alerting resources and provision them into<br>your Grafana system using file provisioning or Terraform.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Alertmanager              | Manages the routing and grouping of alert instances.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Alert rule                | A set of evaluation criteria for when an alert rule<br>should fire. An alert rule consists of one or more<br>queries and expressions, a condition, the frequency of<br>evaluation, and the duration over which the condition<br>is met. An alert rule can produce multiple alert<br>instances.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Alert instance            | An alert instance is an instance of an alert rule. A<br>single-dimensional alert rule has one alert instance. A<br>multidimensional alert rule has one or more alert instances. A<br>single alert rule that matches to multiple results, such as CPU<br>against 10 VMs, is counted as multiple (in this case 10) alert<br>instances. This number can vary over time. For example, an alert<br>rule that monitors CPU usage for all VMs in a system has more<br>alert instances as VMs are added. For more information about<br>alert-instance quotas, see [Quota reached errors](v9-alerting-managerules-grafana.md#v9-alerting-rule-quota-reached "v9-alerting-managerules-grafana.md#v9-alerting-rule-quota-reached"). |
| Alert group               | The Alertmanager groups alert instances by default using the<br>labels for the root notification policy. This controls<br>de-duplication and groups of alert instances, which are sent to<br>contact points.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Contact point             | Define how your contacts are notified when an alert rule<br>fires.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Message templating        | Create reusable custom templates and use them in contact<br>points.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Notification policy       | Set of rules for where, when, and how the alerts are<br>grouped and routed to contact points.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Labels and label matchers | Labels uniquely identify alert rules. They link alert<br>rules to notification policies and silences, determining<br>which policy should handle them and which alert rules<br>should be silenced.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Silences                  | Stop notifications from one or more alert instances. The<br>difference between a silence and a mute timing is that a<br>silence only lasts for only a specified window of time<br>whereas a mute timing is meant to be recurring on a<br>schedule. Uses label matchers to silence alert<br>instances.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Mute timings              | Specify a time interval when you don’t want new<br>notifications to be generated or sent. You can also<br>freeze alert notifications for recurring periods of<br>time, such as during a maintenance period. Must be<br>linked to an existing notification policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
