# Adding a panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

You can use panels to show your data in visual form. This topic walks you through the
basic steps to build a panel.

###### To add a panel to a dashboard

1. Choose the dashboard that you want to add a panel to.
2. Choose the **Add panel** icon.
3. Choose **Add new panel**.

The Grafana workspace creates an empty graph panel with your default data
source selected. 4. While not required, we recommend that you add a helpful title and description
to your panel. You can optionally use variables that you have defined in either
field, but not global variables. For more information, see [Templates and variables](templates-and-variables.md "templates-and-variables.md").

    * Panel title – Text entered in
     this field is displayed at the top of your panel in the panel editor and
     in the dashboard.
    * Description – Text entered in
     this field is displayed in a tooltip in the upper-left corner of the
     panel. Write a description of the panel and the data that you are
     displaying.

5. Write a query for the panel. To display a visualization, each panel needs at
   least one query. You write queries on the **Query** tab of the
   panel editor. For more information, see [Queries](panel-queries.md "panel-queries.md").
   1. Choose a data source. In the first line of the
      **Query** tab, choose the dropdown list to see all
      available data sources. This list includes all data sources that you
      added. For more information about data sources, see [Connect to data sources](AMG-data-sources.md "AMG-data-sources.md").
   2. Write or construct a query in the query language of your data source.
      Options will vary. See your specific data source documentation for
      specific guidelines.

6. In the **Visualization** section of the
   **Panel** tab, choose a visualization type. The Grafana
   workspace displays a preview of your query results with that visualization
   applied.
7. We recommend that you add a note to describe your changes before you choose
   **Save**. Notes are helpful if you need to
   revert the dashboard to a previous version.
8. To save the dashboard, choose **Save** in the upper-right
   corner of the screen.
