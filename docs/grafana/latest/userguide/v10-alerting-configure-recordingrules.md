# Configure recording

rules

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

You can create and manage recording rules for an external Grafana Mimir or Loki
instance. Recording rules calculate frequently needed expressions or
computationally expensive expressions in advance and save the result as a new set
of time series. Querying this new time series is faster, especially for
dashboards since they query the same expression every time the dashboards
refresh.

###### Note

Recording rules are run as instance rules, and run every 10 seconds.

**Prerequisites**

- Verify that you have write permissions to the Prometheus or Loki data
  source. You will be creating or updating alerting rules in your data
  source.
- For Grafana Mimir and Loki data sources, enable the ruler API by
  configuring their respective services.
  - **Loki** – The `local` rule
    storage type, default for the Loki data source, supports only viewing of
    rules. To edit rules, configure one of the other storage types.
  - **Grafana Mimir** – Use the
    `/prometheus` prefix. The Prometheus data source supports both
    Grafana Mimir and Prometheus, and Grafana
    expects that both the Query API and Ruler API are under the same URL. You
    cannot provide a separate URL for the Ruler API.

###### Note

If you do not want to manage alerting rules for a particular Loki or
Prometheus data source, go to its settings and clear the **Manage alerts
via Alerting UI** check box.

###### To create recording rules

1. From your Grafana console, in the Grafana menu, choose
   **Alerting**,
   **Alert rules**.
2. Choose **New recording rule**.
3. Set rule name.

The recording rule name must be a Prometheus metric name and contain no
whitespace. 4. Define query

    * Select your Loki or Prometheus data source.
    * Enter a query.

5. Add namespace and group.
   - From the **Namespace** dropdown, select an
     existing rule namespace or add a new one. Namespaces can
     contain one or more rule groups and only have an organizational
     purpose.
   - From the **Group** dropdown, select an existing
     group within the selected namespace or add a new one. Newly created
     rules are appended to the end of the group. Rules within a group
     are run sequentially at a regular interval, with the same
     evaluation time.

6. Add labels.
   - Add custom labels selecting existing key-value pairs from the
     dropdown, or add new labels by entering the new key or value.

7. Choose **Save rule** to save the rule, or **Save
   rule and exit** to save the rule and go back to the Alerting
   page.
