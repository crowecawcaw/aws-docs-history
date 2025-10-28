# Share query results with another

panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Grafana lets you use the query result from one panel for any other panel in the
dashboard. Sharing query results across panels reduces the number of queries made to
your data source, which can improve the performance of your dashboard.

The _Dashboard_ data source lets you select a panel in your
dashboard that contains the queries you want to share the results for. Instead of
sending a separate query for each panel, Grafana sends one query and other panels
use the query results to construct visualizations.

This strategy can drastically reduce the number of queries being made when you for
example have several panels visualizing the same data.

###### To share query results

1. [Create a dashboard](v10-dash-creating.md "v10-dash-creating.md").
2. Change the title to `Source panel`. You'll use this panel as a
   source for the other panels.
3. Define the query or queries that you want to share.

If you don't have a data source available, use the
**Grafana** data source, which returns a random time
series that you can use for testing. 4. Add a second panel and select the **Dashboard** data
source in the query editor. 5. In the **Use results from panel list**, select the first
panel you created.
All queries defined in the source panel are now available to the new panel.
Queries made in the source panel can be shared with multiple panels.

You can click on any of the queries to go to the panel where they are
defined.
