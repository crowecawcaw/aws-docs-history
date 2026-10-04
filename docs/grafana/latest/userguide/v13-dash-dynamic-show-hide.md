

# Showing and hiding content dynamically
<a name="v13-dash-dynamic-show-hide"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 13.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).

*Show/hide rules* let you show or hide panels, rows, or tabs based on variable values or data query results, so that a single dashboard can adapt to different contexts. For example, you can create a rule to show the Kubernetes section of a dashboard only when the `$datasource` variable is Prometheus, or to hide an empty row when a query returns no data. This replaces the need to maintain multiple near-identical dashboards for different environments.