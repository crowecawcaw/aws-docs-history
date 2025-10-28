# Migrating classic dashboard alerts to Grafana

alerting

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

Existing workspaces, or workspaces that choose not to use Grafana alerting, use the
classic dashboard alerting. To migrate to the new Grafana alerting, you must opt in to
the feature.

You can configure your Amazon Managed Grafana instance to use Grafana alerting using the AWS Management Console,
the AWS CLI, or the Amazon Managed Grafana API. For details about how to configure Amazon Managed Grafana, including
turning Grafana alerting on or off, see [Configure a Amazon Managed Grafana workspace](AMG-configure-workspace.md "AMG-configure-workspace.md").

###### Note

When using Grafana alerting, alert rules defined in Grafana, rather than in
Prometheus, send multiple notifications to your contact point. If you are using
native Grafana alerts, we recommend that you stay on classic dashboard alerting and
not enable the new Grafana alerting feature. If you would like to view Alerts
defined in your Prometheus data source, then we recommend you enable Grafana
Alerting, which sends only a single notification for alerts created in Prometheus
Alertmanager.

This limitation is removed in Amazon Managed Grafana workspaces that support Grafana v10.4
and later.

## Migrating to Grafana alerting

system

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
