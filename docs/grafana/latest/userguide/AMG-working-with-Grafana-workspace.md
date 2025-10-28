# Use your Grafana

workspace

Your Grafana workspace is where you work on projects to create visualizations and explore
your metrics. Set up and query
data sources for your metrics. Create panels inside dashboards to view your metrics. Explore
your data. Create alarms on your metrics.

The topics in this section explain how to use your Amazon Managed Grafana workspace.

###### Note

Some topics vary based on the version of Grafana that you have in your workspace.
For documentation specific to each version, see [Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md"), [Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md"), and [Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md"). For information about upgrading your workspace
from one version to another, see [Update your workspace version](AMG-workspace-version-update.md "AMG-workspace-version-update.md").

###### Topics

- [What is Grafana?](#what-is-grafana "#what-is-grafana")
- [Connect to your workspace](connect-to-workspace.md "connect-to-workspace.md")
- [Users, teams, and permissions](Grafana-administration-authorization.md "Grafana-administration-authorization.md")
- [Create your first dashboard](getting-started-grafanaui.md "getting-started-grafanaui.md")
- [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md")
- [Connect to data sources](AMG-data-sources.md "AMG-data-sources.md")
- [Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md")
- [Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md")
- [Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md")
- [Change your preferences](change-your-grafana-preferences.md "change-your-grafana-preferences.md")
- [Gather information for support](support-bundles.md "support-bundles.md")
- [Classic dashboard alerts](old-alerts-overview.md "old-alerts-overview.md")

## What is Grafana?

Grafana is open source visualization and analytics software. You can use it to query,
visualize, alert on, and explore your metrics no matter where they are stored.

For example, if you want to view the metric, log, and trace data for your
application, you might create a dashboard. If you are the administrator for a
corporation and you manage Grafana for multiple teams, you might need to set up
provisioning and authentication.

The following sections provide an overview of things you can do with your Grafana
database and links so that you can learn more.

### Explore metrics and logs

Explore your data through one-time, or ad hoc, queries and dynamically drilling down.
You can split the view and compare different time ranges, queries, and data sources side
by side.

For more information, see [Explore in Grafana version 10](v10-explore.md "v10-explore.md").

### Alerts

If you’re using Grafana alerting, alerts can be sent through different alert
notifiers, including the following:

- Amazon SNS
- PagerDuty
- VictorOps
- OpsGenie
- Slack

For more information, see [Alerts in Grafana version 10](v10-alerts.md "v10-alerts.md").

### Annotations

Annotate graphs with rich events from different data sources. Pause on events to see
the full event metadata and tags.

This feature, which shows up as a graph marker in Grafana, is useful for correlating
data in case something goes wrong. You can create the annotations manually by pressing
**Ctrl** while you choose a graph and then entering
some text. Or you can fetch data from any data source.

For more information, see [Annotate visualizations](v10-dash-annotations.md "v10-dash-annotations.md").

### Dashboard variables

Use template variables to create dashboards that can be reused for many different use
cases. With these templates, values aren’t hardcoded. This means that you can use a
dashboard for multiple servers. For example, if you have a production server and a test
server, you can use the same dashboard for both.

Templating helps you drill down into your data. For example, you can drill down from
all data to North America data, down to Texas data, and beyond. You can also share these
dashboards across teams within your organization. If you create a great dashboard
template for a popular data source, you can also contribute it to the whole community to
customize and use.

For more information, see [Variables](v10-dash-variables.md "v10-dash-variables.md").
