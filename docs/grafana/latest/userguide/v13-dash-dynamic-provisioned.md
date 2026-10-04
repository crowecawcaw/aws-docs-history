

# Provisioned dashboards and the version 2 schema
<a name="v13-dash-dynamic-provisioned"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 13.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).

Dynamic dashboards use a new dashboard schema (version 2). Dashboards that are provisioned as code (using the API, Terraform, or Git Sync) continue to work. Version 1 dashboards are migrated to version 2 automatically when they are loaded. For more information about the dashboard JSON model, see [Dashboard JSON model](v13-dash-dashboard-json-model.md).