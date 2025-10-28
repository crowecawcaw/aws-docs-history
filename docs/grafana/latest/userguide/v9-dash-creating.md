# Creating dashboards

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

**Creating a dashboard**

Dashboards and panels allow you to show your data in visual form using Grafana.
Each panel needs at least one query to display a visualization. Before you get
started, complete the following prerequisites.

- Ensure that you have the proper permissions. For more information about
  permissions, see [Users, teams, and permissions](Grafana-administration-authorization.md "Grafana-administration-authorization.md").
- Identify the dashboard to which you want to add the panel.
- Understand the query language of the target data source.
- Ensure that data source for which you are writing a query has been added.
  To create a dashboard:

1. Sign into Grafana, hover your cursor over **Dashboard**, and click **+ New
   Dashboard**.
2. Click **Add a new panel**.
3. In the first line of the **Query** tab, click
   the dropdown list and select a data source.
4. Write or construct a query in the query language of your data source.
5. In the **Visualization** list, select a
   visualization type. Grafana displays a preview of your query results with
   the visualization applied. For more information, see [Visualizations options](v9-panels-viz.md "v9-panels-viz.md").
6. Adjust panel settings in the following ways.
   - [Configure
     value mappings](v9-panels-configure-value-mappings.md "v9-panels-configure-value-mappings.md")
   - [Visualization-specific
     options](v9-panels-viz.md "v9-panels-viz.md")
   - [Override
     field values](v9-panels-configure-overrides.md "v9-panels-configure-overrides.md")
   - [Configure
     thresholds](v9-panels-configure-thresholds.md "v9-panels-configure-thresholds.md")
   - [Configure
     standard options](v9-panels-configure-standard-options.md "v9-panels-configure-standard-options.md")

   ###### Note

   Most visualizations need some adjustment before they properly
   display the information you need.

7. Add a note to describe the visualization (or describe your changes) and
   then click **Save** in the upper-right corner
   of the page.

###### Note

Notes are helpful if you need to revert the dashboard to a previous
version.
**Configuring repeating rows**

You can configure Grafana to dynamically add panels or rows to a dashboard based
on the value of a variable. Variables dynamically change your queries across all
rows in a dashboard. For more information about repeating panels, see Configure
repeating panels.

You can also repeat rows if you have variables set with `Multi-value`
or `Include all values` selected.

Before you get started, ensure that the query includes a multi-value variable,
then you should complete the following steps.

1. On the dashboard home page, click **Add
   panel**.
2. On the **Add a panel** dialog box, click
   **Add a new row**.
3. Hover over the row title and click the cog icon.
4. On the **Row Options** dialog box, add a
   title and select the variable for which you want to add repeating
   rows.

###### Note

To provide context to dashboard users, add the variable to the row
title.
**To move a panel**

1. Open the dashboard.

1. Click the panel title and drag the panel to the new location. You can
   place a panel on a dashboard in any location.
   **To resize a panel**

1. Open the dashboard.
1. To adjust the size of the panel, click and drag the lower-right corner of
   the panel. You can size a dashboard panel to suits your needs.
