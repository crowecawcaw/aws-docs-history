# Creating dashboards

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

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
- Ensure that data source for which you are writing a query has been
  added. For more information, see [Connect to data sources](AMG-data-sources.md "AMG-data-sources.md").
  To create a dashboard:

1. Sign into Grafana, and select **Dashboards**
   from the left menu.
2. Select **New**, then **New
   dashboard**.
3. On the empty dashboard, select **+ Add visualization**.
   This opens the new visualization dialog box.
4. Select a data source. You can choose an existing data source, one of
   Grafana's built in data sources for testing, or choose
   **Configure a new data source** to set up a new one
   (only users with Admin permissions can configure new data sources).

The **Edit panel** view opens, with your data source
selected. You can change the data source for the panel later, using the
**Query** tab of the panel editor, if needed. 5. Write or construct a query in the query language of your data
source. Choose the refresh dashboard icon to perform a query on the data
source, seeing the results as you go. 6. In the **Visualization** list, select a
visualization type. Grafana displays a preview of your query results with
the visualization applied. For more information, see [Visualizations options](v10-panels-viz.md "v10-panels-viz.md"). 7. Under **Panel options**, you can enter a title and
description for your panel. 8. Most visualizations need some adjustment before they display the exact
information that you need. You can adjust panel settings in the following
ways.

    * [Configure
     value mappings](v10-panels-configure-value-mappings.md "v10-panels-configure-value-mappings.md")
    * [Visualization-specific
     options](v10-panels-viz.md "v10-panels-viz.md")
    * [Override field
     values](v10-panels-configure-overrides.md "v10-panels-configure-overrides.md")
    * [Configure
     thresholds](v10-panels-configure-thresholds.md "v10-panels-configure-thresholds.md")
    * [Configure
     standard options](v10-panels-configure-standard-options.md "v10-panels-configure-standard-options.md")

9. When you've finished configuring your panel, choose
   **Save** to save the dashboard.

Alternatively, select **Apply** to see changes
without leaving the panel editor. 10. Add a note to describe the visualization (or describe your changes) and
then click **Save** in the upper-right corner
of the page.

###### Note

Notes are helpful if you need to revert the dashboard to a previous
version. 11. Choose **Save**. 12. Optionally, you can add more panels to the dashboard by choosing
**Add** in the dashboard header, and selecting
**Visualization** from the drop-down.
**Copying an existing dashboard**

You can quickly copy an existing dashboard, to jumpstart creating a new one.

###### To copy an existing dashboard

1. Select **Dashboards** from the left menu.
2. Choose the dashboard you want to copy, to open it.
3. Select **Settings** (gear icon) in the top right of
   the dashboard.
4. Select **Save as**in the top right corner of the
   dashboard.
5. (Optional) Specify the name, folder, description, and whether or not to
   copy the original dashboard tags for the copied dashboard.
6. Select **Save**.
   **Configuring repeating rows**

You can configure Grafana to dynamically add panels or rows to a dashboard based
on the value of a variable. Variables dynamically change your queries across all
rows in a dashboard. For more information about repeating panels, see Configure repeating
panels.

You can also repeat rows if you have variables set with `Multi-value`
or `Include all values` selected.

Before you get started, ensure that the query includes a multi-value variable,
then you should complete the following steps.

###### To configure repeating rows

1. Select **Dashboards** from the left menu, then
   choose the dashboard you want to modify.
2. At the top of the dashboard, select **Add**, and then
   select **Row** from the drop down.

If the dashboard is empty, you can alternately select the
**+ Add row** button in the middle of the
dashboard. 3. Hover over the row title and select the **Settings**
(gear) icon that appears. 4. On the **Row Options** dialog box, add a
title and select the variable for which you want to add repeating
rows.

###### Note

To provide context to dashboard users, add the variable to the row
title. 5. Select **Update**.
**Repeating rows and the Dashboard special data
source**

If a row includes panels using the special [Dashboard](AMG-data-sources.md#AMG-data-sources-special "AMG-data-sources.md#AMG-data-sources-special") data source—the data source that uses a result set from
another panel in the smae dashboard—then corresponding panels in repeated
rows will reference the panel in the original row, not the ones in the repeated
rows.

For example, in a dashboard:

- `Row 1` includes `Panel 1A` and `Panel 
1B`.
- `Panel 1B` uses the results from `Panel 1A` by
  using the `Dashboard` data source.
- Repeating `Row 2` includes `Panel 2A` and `Panel 
2B`.
- `Panel 2B` references `Panel 1A`, not `Panel 
 2A`.
  **To move a panel**

1. Open the dashboard.
2. Select the panel title and drag the panel to the new location. You can
   place a panel on a dashboard in any location.
   **To resize a panel**

3. Open the dashboard.
4. To adjust the size of the panel, drag the lower-right corner of
   the panel. You can size a dashboard panel to suits your needs.
