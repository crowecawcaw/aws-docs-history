# Adding an external Alertmanager

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Set up Grafana to use an external Alertmanager as a single Alertmanager to receive
all of your alerts. This external Alertmanager can then be configured and
administered from within Grafana itself.

###### Note

You can't use Amazon Managed Service for Prometheus as an external Alertmanager.

Once you have added the alertmanager, you can use the Grafana Alerting UI to
manage silences, contact points, and notification policies. A dropdown option in
these pages allows you to switch between alertmanagers.

External alertmanagers are configured as data sources using Grafana
Configuration from the main Grafana navigation menu. This enables you to manage the
contact points and notification policies of external alertmanagers from within
Grafana and also encrypts HTTP basic authentication credentials that were previously
visible when configuring external alertmanagers by URL.

###### Note

Starting with Grafana 9.2, the URL configuration of external alertmanagers
from the Admin tab on the Alerting page is deprecated. It will be removed in a
future release.

###### To add an external Alertmanager

1. Choose **Connections** from the main left menu.
2. Search for `Alertmanager`.
3. Choose the **Create a new data source** button.
4. Fill out the fields on the page, as required.

If you are provisioning your data source, set the flag
`handleGrafanaManagedAlerts` in the `jsonData`
field to `true` to send Grafana-managed alerts to this
Alertmanager.

###### Note

Prometheus, Grafana Mimir, and Cortex implementations of
Alertmanager are supported. For Prometheus, contact points and
notification policies are read-only in the Grafana Alerting
UI. 5. Choose **Save & test**.
