# Configure data source

managed alert rules

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Create alert rules for an external Grafana Mimir or Loki instance that has ruler API
enabled; these are called data source managed alert rules.

###### Note

Alert rules for an external Grafana Mimir or Loki instance can be edited or deleted by
users with Editor or Admin roles.

If you delete an alerting resource created in the UI, you can no longer retrieve it. To
make a backup of your configuration and to be able to restore deleted alerting resources,
create your alerting resources using Terraform, or the Alerting API.

**Prerequisites**

- Verify that you have write permission to the Prometheus or Loki data source.
  Otherwise, you will not be able to create or update Grafana Mimir managed alert
  rules.
- For Grafana Mimir and Loki data sources, enable the Ruler API by configuring
  their respective services.
  - **Loki** - The `local` rule
    storage type, default for the Loki data source, supports only viewing of
    rules. To edit rules, configure one of the other rule storage
    types.
  - **Grafana Mimir** - use the
    `/prometheus` prefix. The Prometheus data source supports
    both Grafana Mimir and Prometheus, and Grafana expects that both the
    [Query API](https://grafana.com/docs/mimir/latest/operators-guide/reference-http-api/#querier--query-frontend "https://grafana.com/docs/mimir/latest/operators-guide/reference-http-api/#querier--query-frontend") and [Ruler API](https://grafana.com/docs/mimir/latest/operators-guide/reference-http-api/#ruler "https://grafana.com/docs/mimir/latest/operators-guide/reference-http-api/#ruler") are under the same URL. You cannot provide a
    separate URL for the Ruler API.

###### Note

If you do not want to manage alert rules for a particular Loki or Prometheus
data source, go to its settings and clear the **Manage alerts via
alerting UI** checkbox.

In the following procedures, we’ll guide you through the process of creating your data
source managed alert rules.

To create a data source-managed alert rule, use the in-workspace alert creation flow and
follow these steps to help you.

###### To set the alert rule name

1. Choose **Alerting** -> **Alert
   rules** -> **+ New alert rule**.
2. Enter a name to identify your alert rule.

This name is displayed in the alert rule list. It is also the
`alertname` label for every alert instance that is created
from this rule.
Define a query to get the data you want to measure and a condition that needs to be
met before an alert rule fires.

###### To define query and condition

1. All alert rules are managed by Grafana by default. To switch to a data
   source managed alert rule, choose **Switch to data source-managed
   alert rule**.
2. Select a data source from the drop-down list.

You can also choose **Open advanced data source picker**
to see more options, including adding a data source (Admins only). 3. Enter a PromQL or LogQL query. 4. Choose **Preview alerts**.
Use alert rule evaluation to determine how frequently an alert rule should be
evaluated and how quickly it should change its state.

###### To set alert evaluation behavior

1. Select a namespace or choose **+ New namespace**.
2. Select an evaluation group or choose **+ New evaluation
   group**.

If you are creating a new evaluation group, specify the interval for the
group.

All rules within the same group are evaluated sequentially over the same
time interval. 3. Enter a pending period.

The pending period is the period in which an alert rule can be in breach
of the condition until it fires.

Once a condition is met, the alert goes into the `Pending`
state. If the condition remains active for the duration specified, the
alert transitions to the `Firing` state, else it reverts to the
`Normal` state.
Add labels to your alert rules to set which notification policy should handle
your firing alert instances.

All alert rules and instances, irrespective of their labels, match the default
notification policy. If there are no nested policies, or no nested policies match
the labels in the alert rule or alert instance, then the default notification
policy is the matching policy.

###### Configure notifications

- Add labels if you want to change the way your notifications are routed.

Add custom labels by selecting existing key-value pairs from the drop down, or
add new labels by entering the new key or value.
Add [annotations](v10-alerting-overview-labels.md#v10-alerting-overview-labels-annotations "v10-alerting-overview-labels.md#v10-alerting-overview-labels-annotations") to
provide more context on the alert in your alert notifications.

Annotations add metadata to provide more information on the alert in your alert
notifications. For example, add a `Summary` annotation to
tell you which value caused the alert to fire or which server it happened on.

###### To add annotations

1. [Optional] Add a summary.

Short summary of what happened and why. 2. [Optional] Add a description.

Description of what the alert rule does. 3. [Optional] Add a Runbook URL.

Webpage where you keep your runbook for the alert 4. [Optional] Add a custom annotation 5. [Optional] Add a dashboard and panel link.

Links alerts to panels in a dashboard. 6. Choose **Save rule**.
