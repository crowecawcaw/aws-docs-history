# Alert groups

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

Alert groups show grouped alerts from an Alertmanager instance. By default, the alerts
are grouped by the label keys for the root policy in [Working with notification policies](alert-notifications.md "alert-notifications.md"). Grouping common alerts into a single alert
group prevents duplicate alerts from being initiated.

###### To view alert groupings

1. From your Grafana console, in the Grafana menu, choose the
   **Alerting** (bell) icon, then the
   **Alert grouping** item to open the page listing
   existing groups.
2. From the **Alertmanager** drop-down, select an external
   Alertmanager as your data source. By default, the `Grafana`
   Alertmanager is selected.
3. From the **custom group by** drop-down, select a combination
   of labels to view a grouping other than the default. You can use this view to
   debug or verify your grouping of notification policies.
   Alerts without labels specified in the grouping of the root policy or the custom
   grouping, are added to a group with a header of `No grouping`.

**Filter alerts**

You can use the following filters to view alerts that match specific criteria:

- **Search by label** – In
  **Search**, enter an existing label to view alerts matching
  the label. For example, `environment=production`,
  `region=~US|EU`, `severity!=warning`.
- **Filter alerts by state** – In
  **States**, select from `Active`,
  `Suppressed`, or `Unprocessed` states to view alerts
  in that state.
