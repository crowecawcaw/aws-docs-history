# Library panels

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

Library panels allow users to create reusable panels where any changes made to one
instance of the library panel are reflected on every dashboard affecting all other
instances where the panel is used. These panels can be saved in folders alongside
Dashboards and streamline reuse of panels across multiple dashboards.

## Create a library panel

###### Note

When you create library panels, the panel on the source dashboard is converted
to a library panel as well. You will need to save the original dashboard once a
panel is converted.

###### To create a library panel

1. Create a panel as you normally would. You can also use an existing
   panel.
2. Choose the title of the panel and choose **Edit**.
3. In the panel display options side pane, choose the down arrow option to
   bring changes to the visualization.
4. Choose **Library panels**, and choose **Create
   new library panel**.
5. Enter a name for the library panel, and select the folder to save it
   in.
6. Choose **Create library panel** and then save the
   dashboard.

You can also create library panels by using the **Share** option
for any panel.

Once created, you can modify the library panel using any dashboard on which it
appears. Once the library panel changes are saved, all instances of the library
panel will reflect these modifications.

## Add a library panel

###### To add a library panel to a dashboard

1. Pause on the + option on the left menu, then choose
   **Create**.
2. Choose **Add a panel from the panel library**.
3. Filter the list of library panels to find the panel that you want.
4. Choose that panel and add it to the dashboard.

## Unlink a library panel

If you have a library panel on your dashboard that you want to modify without
affecting all other instances of the library panel, you can unlink the library
panel.

###### To unlink a library panel from a dashboard

1. Pause on **Dashboard** on the left menu, then choose
   **Library panels**.
2. Select a library panel. You will see a list of all the dashboards where
   the library panel is used.
3. Select the panel that you want to unlink and update.
4. Choose the title of the panel and choose **Edit**.
5. Choose **Unlink**.

## Delete a library panel

Before you delete a library panel, verify that it is no longer in use on any
dashboard.

###### To delete a library panel

1. Pause on **Dashboard** on the left menu, then choose
   **Library panels**.
2. Select a library panel. You will see a list of all the dashboards where
   the library panel is used.
3. Select the panel that you want to delete.
4. Choose the delete icon next to the panel name.

## Parts of the panel editor

This section describes the parts of the panel editor screen, with information
about fields, options, or tasks associated with each part.

### Header

The header section lists the name of the dashboard that the panel is in and
some dashboard commands. You can also choose the **Go back**
arrow to return to the dashboard.

On the right side of the header are the following options:

- Dashboard settings (gear) icon –
  Choose to access the dashboard settings.
- Discard Choose to discard all changes
  that you have made to the panel since you last saved the dashboard.
- Save – Choose to save the dashboard
  including all changes that you have made in the panel editor.
- Apply – Choose to apply changes
  that you made and then close the panel editor, returning to the
  dashboard. Also save the dashboard to persist the applied changes.

### Visualization preview

The visualization preview section contains viewing options, time range
controls, the visualization preview, and (if applicable) the panel title, axes,
and legend.

- Fill – The visualization preview
  fills the available space in the preview part. If you change the width
  of the side pane or height of the bottom pane, the visualization adapts
  to fill whatever space is available.
- Fit – The visualization preview
  fills in the available space, but it preserves the aspect ratio of the
  panel.
- Exact – The visualization preview
  has the exact size as the size on the dashboard. If not enough space is
  available, the visualization scales down, preserving the aspect ratio.
- Time range controls – For more
  information, see [Time range controls](dashboard-time-range-controls.md "dashboard-time-range-controls.md"). .

### Data section (lowest pane)

The data section contains tabs where you enter queries, transform your data,
and create alert rules (if applicable).

- Query tab – Select your data source
  and enter queries here. For more information, see [Queries](panel-queries.md "panel-queries.md").
- Transform tab – Apply data
  transformations. For more information, see [Transformations](panel-transformations.md "panel-transformations.md").
- Alert tab – Write alert rules. For
  more information, see [Grafana alerting](alerts-overview.md "alerts-overview.md").

### Panel and field options

(side pane)

This section contains tabs where you control almost every aspect of how your
data is visualized. Not all tabs are available for each visualization.

Features on these tabs are documented in the following topics:

- [Adding a panel](add-a-panel-to-a-dashboard.md "add-a-panel-to-a-dashboard.md")
- [Visualizations](AMG-visualizations.md "AMG-visualizations.md")
- [Field options and overrides](field-options-overrides.md "field-options-overrides.md")
- [Panel links](panel-links.md "panel-links.md") and [Data links](data-links.md "data-links.md"), which help you
  connect your visualization to other resources
