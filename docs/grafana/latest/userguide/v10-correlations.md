# Correlations in Grafana version 10

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

You can create interactive links for Explore visualizations to run queries related to
presented data by setting up Correlations.

A correlation defines how data in one data source is used to query data in another data
source. Some examples:

- An application name returned in a logs data source can be used to query
  metrics related to that application in a metrics data source.
- A user name returned by an SQL data source can be used to query logs related
  to that particular user in a logs data source.
  Explore takes user-defined correlations to display links inside the visualizations. You
  can click on a link to run the related query and see results in Explore Split View.

Explore visualizations that currently support showing links based on correlations:

- [Logs](v10-panels-logs.md "v10-panels-logs.md")
- [Table](v10-panels-table.md "v10-panels-table.md")
  You can configure correlations using the **Administration > Plugins and data >
  Correlations** page in Grafana or directly in [Explore](v10-explore-correlations.md "v10-explore-correlations.md").

###### Topics

- [Correlation configuration](v10-correlations-config.md "v10-correlations-config.md")
- [Create a new correlation](v10-correlations-create.md "v10-correlations-create.md")
