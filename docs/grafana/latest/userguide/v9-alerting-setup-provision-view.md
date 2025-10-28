# Viewing provisioned

alerting resources in Grafana

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

You can verify that your alerting resources were created in
Grafana.

###### To view your provisioned resources in Grafana

1. Open your Grafana instance.
2. Navigate to Alerting.
3. Click an alerting resource folder, for example, Alert
   rules.

Provisioned resources are labeled **Provisioned**,
so that it is clear that they were not created manually.

###### Note

You cannot edit provisioned resources from Grafana. You can only change
the resource properties by changing the provisioning file and restarting
Grafana or carrying out a hot reload. This prevents changes being made
to the resource that would be overwritten if a file is provisioned again
or a hot reload is carried out.
