# Viewing existing alert rules

This documentation topic discusses
legacy alerting in Grafana. This will not be supported in future versions
of Amazon Managed Grafana. You can migrate to Grafana alerting to use the latest
alerting features. For more information, see one of the following
topics.

For Grafana workspaces that support Grafana version 10.x, see
[Alerts in Grafana version 10](v10-alerts.md "v10-alerts.md").

For Grafana workspaces that support Grafana version 9.x, see
[Alerts in Grafana version 9](v9-alerts.md "v9-alerts.md").

For Grafana workspaces that support Grafana version 8.x, see
[Grafana alerting](alerts-overview.md "alerts-overview.md").

Amazon Managed Grafana stores individual alert rules in the panels where they are defined, but you
can also view a list of all existing alert rules and their current state.

In the Grafana side bar, pause on the **Alerting** (bell) icon, and
then choose **Alert Rules**. All configured alert rules are
listed, along with their current state.

While viewing alerts, you can do the following:

- **Filter alerts by name** – Type an alert
  name in the **Search alerts** field.
- **Filter alerts by state** – In **States**, select which alert states you want to see.
  All others will be hidden.
- **Pause or resume an alert** – choose the
  **Pause** or **Play** icon next to the alert to pause or resume evaluation.
- **Access alert rule settings** – Choose the
  alert name or the **Edit alert rule** (gear) icon.
  Amazon Managed Grafana opens the **Alert** tab of the panel where the alert
  rule is defined. This is helpful when an alert is firing, but you don’t know
  which panel it is defined in.
