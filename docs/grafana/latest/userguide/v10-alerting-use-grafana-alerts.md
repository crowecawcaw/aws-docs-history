# Migrating classic dashboard alerts to Grafana

alerting

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Workspaces that choose not to use Grafana alerting use the [Classic dashboard alerts](old-alerts-overview.md "old-alerts-overview.md"). To switch to
the new Grafana alerting, you must opt in to the feature. To see details about the
differences between classic dashboard alerting and Grafana alerting, see [Grafana alerting vs legacy dashboard
alerting](#v10-alerting-diff-old-new "#v10-alerting-diff-old-new"). GrafanaLabs has announced that
classic dashboard alerts will be removed in version 11.

When you are using classic dashboard alerting, Amazon Managed Grafana shows you a preview of
Grafana alerting where you can review and modify your upgraded alerts before
finalizing the upgrade.

## Previewing Grafana

alerts

You can preview your alerts in Grafana alerts before migrating. In the preview,
you can make changes to the alerts that will change the migration.

###### To preview your Grafana alerting migration

1. Sign into your Grafana workspace.
2. From the left menu, choose **Alerting (legacy)** to
   view your current alerts.
3. From the left menu, choose **Alerting upgrade** to
   view your alerts in Grafana alerting.

From this view, you can see what your alerts will look like after
migration.

###### Note

From this view, you can also make changes that will affect your
migration. To undo any changes you make, choose **Reset
upgrade** at the top right of the upgrade page.

When you are ready to upgrade your alerts, see the next section.

## Migrating to Grafana

alerting system

You can configure your Amazon Managed Grafana instance to use Grafana alerting using the AWS Management Console,
the AWS CLI, or the Amazon Managed Grafana API. For details about how to configure Amazon Managed Grafana, including
turning Grafana alerting on or off, see [Configure a Amazon Managed Grafana workspace](AMG-configure-workspace.md "AMG-configure-workspace.md").

When Grafana alerting is turned on, existing classic dashboard alerts migrate in a
format compatible with the Grafana alerting. In the Alerting page of your Grafana
instance, you can view the migrated alerts alongside new alerts. With Grafana alerting, your Grafana-managed alert rules send multiple
notifications rather than a single alert when they are matched.

Read and write access to classic dashboard alerts and Grafana alerts are governed
by the permissions of the folders storing them. During migration, classic dashboard
alert permissions are matched to the new rules permissions as follows:

- If the original alert's dashboard has permissions, migration creates a
  folder named with this format `Migrated {"dashboardUid": "UID",
"panelId": 1, "alertId": 1}` to match permissions of the original
  dashboard (including the inherited permissions from the folder).
- If there are no dashboard permissions and the dashboard is under a folder,
  then the rule is linked to this folder and inherits its permissions.
- If there are no dashboard permissions and the dashboard is under the
  General folder, then the rule is linked to the General Alerting folder, and
  the rule inherits the default permissions.

###### Note

Since there is no `Keep Last State` option for `NoData`
in Grafana alerting, this option becomes `NoData` during the classic
rules migration. Option `Keep Last State` for `Error`
handling is migrated to a new option `Error`. To match the behavior
of the `Keep Last State`, in both cases, during the migration
Amazon Managed Grafana automatically creates a silence for each alert rule with a duration of
one year.

Notification channels are migrated to an Alertmanager configuration with the
appropriate routes and receivers. Default notification channels are added as contact
points to the default route. Notification channels not associated with any Dashboard
alert go to the `autogen-unlinked-channel-recv` route.

### Limitations

- Grafana alerting system can retrieve rules from all available
  Prometheus, Loki, and Alertmanager data sources. It might not be able to
  fetch alerting rules from other supported data sources.
- Migrating back and forth between Grafana alerts and the classic
  dashboard alerting can result in data loss for features supported in one
  system, but not the other.

###### Note

If you migrate back to the classic dashboard alerting, you lose
all changes made to alerting configuration made while you had
Grafana alerting enabled, including any new alert rules that were
created.

## Grafana alerting vs legacy dashboard

alerting

Introduced in Grafana 8, Grafana alerting has several enhancements over
legacy dashboard alerting.

### Multi-dimensional

alerting

You can now create alerts that give you system-wide visibility
with a single alerting rule. Generate multiple alert instances
from a single alert rule. For example, you can create a rule to
monitor the disk usage of multiple mount points on a single
host. The evaluation engine returns multiple time series from a
single query, with each time series identified by its label set.

### Create alerts

outside of Dashboards

Unlike legacy dashboard alerts, Grafana alerts allow you to
create queries and expressions that combine data from multiple
sources in unique ways. You can still link dashboards and panels
to alerting rules using their ID and quickly troubleshoot the
system under observation.

Since unified alerts are no longer directly tied to panel
queries, they do not include images or query values in the
notification email. You can use customized notification
templates to view query values.

### Create Loki and Grafana Mimir alerting rules

In Grafana Alerting, you can manage Loki and Grafana Mimir alerting rules using
the same UI and API as your Grafana managed alerts.

### View and search for alerts from Prometheus compatible data sources

Alerts for Prometheus compatible data sources are now listed
under the Grafana alerts section. You can search for labels
across multiple data sources to quickly find relevant alerts.

### Special alerts for alert state NoData and Error

Grafana Alerting introduced a new concept of the alert states.
When evaluation of an alerting rule produces state NoData or
Error, Grafana Alerting will generate special alerts that will
have the following labels:

- `alertname` with value DatasourceNoData or
  DatasourceError depending on the state.
- `rulename` name of the alert rule the
  special alert belongs to.
- `datasource_uid` will have the UID of the
  data source that caused the state.
- All labels and annotations of the original alert rule

You can handle these alerts the same way as regular alerts by
adding a silence, route to a contact point, and so on.

###### Note

If the rule uses many data sources and one or many returns no data, the
special alert will be created for each data source that caused the alert
state.
