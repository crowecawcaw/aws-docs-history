

# Correlations in Grafana version 13
<a name="v13-correlations"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 13.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).

You can create interactive links for Explore visualizations to run queries related to presented data by setting up Correlations.

A correlation defines how data in one data source is used to query data in another data source. Some examples:
+ An application name returned in a logs data source can be used to query metrics related to that application in a metrics data source.
+ A user name returned by an SQL data source can be used to query logs related to that particular user in a logs data source.

Explore takes user-defined correlations to display links inside the visualizations. You can click on a link to run the related query and see results in Explore Split View.

Explore visualizations that currently support showing links based on correlations:
+ [Logs](v13-panels-logs.md)
+ [Table](v13-panels-table.md)

You can configure correlations using the **Administration > Plugins and data > Correlations** page in Grafana or directly in [Explore](v13-explore-correlations.md). You can also add correlations to external URLs directly from Explore, enabling seamless navigation between data sources and external systems.

**Topics**
+ [Correlation configuration](v13-correlations-config.md)
+ [Create a new correlation](v13-correlations-create.md)