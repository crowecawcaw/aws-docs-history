# Creating Grafana Mimir

or Loki managed alert rules

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Using Grafana, you can create alerting rules for an external Grafana Mimir or Loki
instance.

###### Note

Grafana Mimir can connect to Amazon Managed Service for Prometheus and Prometheus data
sources.

**Prerequisites**

- Verify that you have write permissions to the Prometheus data source.
  Otherwise, you are not able to create or update Cortex managed alerting
  rules.
- For Grafana Mimir and Loki data sources, enable the ruler API by configuring
  their respective services.
  - **Loki** – The
    `local` rule storage type, default for the Loki data
    source, supports only viewing of rules. To edit rules, configure one
    of the other storage types.
  - **Grafana Mimir** – Use the
    legacy `/api/prom` prefix, not
    `/prometheus`. The Prometheus data source supports
    both Grafana Mimir and Prometheus, and Grafana expects that both
    the Query API and Ruler API are under the same URL. You cannot
    provide a separate URL for the Ruler API.

###### Note

If you do not want to manage alerting rules for a particular Loki or
Prometheus data source, go to its settings and clear the **Manage
alerts via Alerting UI** checkbox.

###### To add a Grafana Mimir or Loki managed alerting rule

1. From your Grafana console, in the Grafana menu, choose the
   **Alerting** (bell) icon to open the
   **Alerting** page listing existing alerts.
2. Choose **Create alert rule**.
3. In **Step 1**, choose the rule type, and details,
   as follows:
   - Choose **Mimir or Loki alert**.
   - In **Rule name**, add a descriptive name. This
     name is displayed in the alert rules list. It is also the
     `alertname` label for every alert instance that is
     created from this rule.
   - From the **Select data source** dropdown, select
     a Prometheus, or Loki data source.
   - From the **Namespace** dropdown, select an
     existing rule namespace. Otherwise, choose **Add
     new** and enter a name to create one. Namespaces can
     contain one or more rule groups and only have an organizational
     purpose. For more information, see [Cortex or Loki rule groups and
     namespaces](alert-rules.md#alert-rule-groups "alert-rules.md#alert-rule-groups").
   - From the **Group** dropdown, select an existing
     group within the selected namespace. Otherwise, choose **Add
     new** and enter a name to create one. Newly created
     rules are appended to the end of the group. Rules within a group run
     sequentially at a regular interval, with the same evaluation
     time.

4. In **Step 2**, add the query to evaluate.

The value can be a PromQL or LogQL expression. The rule initiates an alert
if the evaluation result has at least one series with a value that is
greater than 0. An alert is created for each series. 5. In **Step 3**, specify the alert evaluation interval.

In the **For** text box of the condition, specify the duration for which the
condition must be true before the alert is initiated. If you specify
`5m`, the conditions must be true for five minutes before the
alert is initiated.

###### Note

After a condition is met, the alert goes into `Pending`
state. If the condition remains active for the duration specified, the
alert transitions to the `Firing` state. If it is no longer
met, it reverts to the `Normal` state. 6. In **Step 4**, add additional metadata associated with
the rule.

    * Add a description and summary to customize alert messages. Use the
     guidelines in [Labels and annotations](v9-alerting-explore-labels.md "v9-alerting-explore-labels.md").
    * Add Runbook URL, panel, dashboard, and alert IDs.
    * Add custom labels.

7. Choose **Preview alerts** to evaluate the rule and see
   what alerts it would produce. It displays a list of alerts with state and
   value of each one.
8. Choose **Save** to save the rule or **Save and
   exit** to save the rule and go back to the
   **Alerting** page.
   After you have created your rule, you can create a notification for your rule.
   For more information about notifications, see [Manage your alert
   notifications](v9-alerting-managenotifications.md "v9-alerting-managenotifications.md").
