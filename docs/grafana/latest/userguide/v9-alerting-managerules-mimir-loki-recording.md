# Creating Grafana

Mimir or Loki managed recording rules

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

You can create and manage recording rules for an external Grafana Mimir or Loki
instance. Recording rules calculate frequently needed expressions or
computationally expensive expressions in advance and save the result as a new set
of time series. Querying this new time series is faster, especially for
dashboards since they query the same expression every time the dashboards
refresh.

**Prerequisites**

For Grafana Mimir and Loki data sources, enable the ruler API by configuring their
respective services.

- **Loki** – The `local` rule
  storage type, default for the Loki data source, supports only viewing of
  rules. To edit rules, configure one of the other storage types.
- **Grafana Mimir** – When configuring a
  data source to point to Grafana Mimir, use the legacy
  `/api/prom` prefix, not `/prometheus`. The
  Prometheus data source supports both Grafana Mimir and Prometheus, and Grafana
  expects that both the Query API and Ruler API are under the same URL. You
  cannot provide a separate URL for the Ruler API.

###### Note

If you do not want to manage alerting rules for a particular Loki or
Prometheus data source, go to its settings and clear the **Manage alerts
via Alerting UI** check box.

###### To add a Grafana Mimir or Loki managed recording rule

1. From your Grafana console, in the Grafana menu, choose the
   **Alerting** (bell) icon to open the
   **Alerting** page listing existing alerts.
2. Choose **Create alert rule**.
3. In **Step 1**, add the rule type, rule name, and storage
   location, as follows.
   - Select the **Mimir or Loki recording rule**
     option.
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
greater than 0. An alert is created for each series. 5. In **Step 3**, add additional metadata associated with
the rule.

    * Add a description and summary to customize alert messages. Use the
     guidelines in [Annotations and labels for alerting
     rules](alert-rules.md#alert-rule-labels "alert-rules.md#alert-rule-labels").
    * Add Runbook URL, panel, dashboard, and alert IDs.
    * Add custom labels.

6. Choose **Save** to save the rule or **Save and
   exit** to save the rule and go back to the
   **Alerting** page.
