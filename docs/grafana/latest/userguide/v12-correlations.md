

# Correlations in Grafana version 12
<a name="v12-correlations"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 12.x**.  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

You can create interactive links for Explore visualizations to run queries related to presented data by setting up Correlations.

A correlation defines how data in one data source is used to query data in another data source. Some examples:
+ An application name returned in a logs data source can be used to query metrics related to that application in a metrics data source.
+ A user name returned by an SQL data source can be used to query logs related to that particular user in a logs data source.

Explore takes user-defined correlations to display links inside the visualizations. You can click on a link to run the related query and see results in Explore Split View.

Explore visualizations that currently support showing links based on correlations:
+ [Logs](v12-panels-logs.md)
+ [Table](v12-panels-table.md)

You can configure correlations using the **Administration > Plugins and data > Correlations** page in Grafana or directly in [Explore](v12-explore-correlations.md). You can also add correlations to external URLs directly from Explore, enabling seamless navigation between data sources and external systems.

**Topics**
+ [Correlation configuration](v12-correlations-config.md)
+ [Create a new correlation](v12-correlations-create.md)