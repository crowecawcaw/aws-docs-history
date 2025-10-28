# Panel editor

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

This topic describes the parts of the Amazon Managed Grafana panel editor, and it includes links
to where you can find more information.

## Opening the panel editor

There are several ways to access the panel editor, also called the **Edit
Panel** screen, _edit mode_, or _panel edit
mode_.

- Choose the **Add panel** icon at the top of the screen,
  and then choose **Add new panel**. The new panel opens in
  the panel editor. For more information about how to add a panel, see [Adding a panel](add-a-panel-to-a-dashboard.md "add-a-panel-to-a-dashboard.md").
- Choose the title of an existing panel, and then choose
  **Edit**. The panel opens in edit mode.
- Choose anywhere on an existing panel, and then press **e** on your keyboard. The panel opens in edit mode.

## Resizing panel editor

sections

Drag to resize sections of the panel editor. If the side pane becomes too narrow,
the **Panel**, **Field**, and
**Overrides** tabs change to a dropdown list.

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
- Save – Choose to saves the
  dashboard, including all changes that you have made in the panel editor.
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
