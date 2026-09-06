

# Dashboards in Grafana version 12
<a name="v12-dashboards"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 12.x**.  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

 A dashboard is a set of one or more [panels](v12-panels.md) organized and arranged into one or more rows. Grafana ships with a variety of panels making it easy to construct the right queries, and customize the visualization so that you can create the perfect dashboard for your need. Each panel can interact with data from any configured [Connect to data sources](AMG-data-sources.md). 

The dashboard rendering engine is built on the Scenes framework, providing improved performance, better template variable support, and more flexible layouts.

 Dashboard snapshots are static. Queries and expressions cannot be re-executed from snapshots. As a result, if you update any variables in your query or expression, it will not change your dashboard data. 

**Topics**
+ [Using dashboards](v12-dash-using-dashboards.md)
+ [Building dashboards](v12-dash-building-dashboards.md)
+ [Managing dashboards](v12-dash-managing-dashboards.md)
+ [Managing playlists](v12-dash-managing-playlists.md)
+ [Sharing dashboards and panels](v12-dash-sharing.md)
+ [Variables](v12-dash-variables.md)
+ [Assessing dashboard usage](v12-dash-assess-dashboard-usage.md)
+ [Troubleshoot dashboards](v12-dash-troubleshoot.md)
+ [Searching Dashboards in Grafana version 12](v12-search.md)