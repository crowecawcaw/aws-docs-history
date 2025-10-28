# Explore in Grafana version 9

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Grafana’s dashboard UI provides functionality to build dashboards for visualization.
_Explore_ strips away the dashboard and panel options so that you
can focus on the query. It helps you iterate until you have a working query and then
you can build a dashboard from the query.

###### Note

If you just want to explore your data and do not want to create a dashboard, then
Explore makes this much easier. If your data source supports graph and table data, then
Explore shows the results both as a graph and a table. This allows you to see trends in
the data and more details at the same time.

## Start exploring

###### Note

In order to access Explore, you must have an editor or an administrator
role.

###### To access Explore

1. In your Grafana workspace, choose the Explore menu item from the left
   menu bar.

An empty Explore tab opens.

Alternately, to start with an existing query in a panel, choose the
Explore option from the Panel menu. This opens an Explore tab with the
query from the panel and allows you to tweak or iterate in the query
outside of your dashboard. 2. Choose your data source from the dropdown in the top left. [Prometheus](prometheus-data-source.md "prometheus-data-source.md") has a
custom Explore implementation, the other data sources use their standard
query editor. 3. In the query field, write your query to explore your data. There are
three buttons beside the query field, a clear button (X), an add query
button (+) and the remove query button (-). Just like the normal query
editor, you can add and remove multiple queries.

For more details about queries, see [Query and transform data](v9-panels-query-xform.md "v9-panels-query-xform.md").

## Split and compare

The split view provides an easy way to compare graphs and tables side-by-side or
to look at related data together on one page.

###### Top open a split view

1. In the Explore view, choose the **Split** button to
   duplicate the current query and split the page into two side-by-side
   queries.

###### Note

It is possible to select another data source for the new query which for
example, allows you to compare the same query for two different servers or
to compare the staging environment to the production environment.

In split view, timepickers for both panels can be linked (if you change one, the
other gets changed as well) by selecting a time-sync button attached to one of
the timepickers. Linking timepickers keeps the start and the end times of the
split view queries in sync. It ensures that you’re looking at the same time
interval in both split panels. 2. To close the newly created query, click on the Close Split button.

## Share shortened link

The Share shortened link capability allows you to create smaller and simpler URLs
of the format /goto/:uid instead of using longer URLs with query parameters. To
create a shortened link to the query results, select the **Share** option in the Explore toolbar. A shortened link that is never
used will automatically get deleted after seven (7) days.
