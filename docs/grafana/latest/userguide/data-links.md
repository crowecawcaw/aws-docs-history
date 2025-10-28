# Data links

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

Data links provide more granular context to your links. You can create links that
include the series name or even the value. For example, if your visualization shows four
servers, you can add a data link to one or two of them.

The link itself is accessible in different ways, depending on the visualization. For
the graph panel, you need to choose a data point or line. For a panel such as stat,
gauge, or bar gauge, you can choose anywhere on the visualization to open the context
menu.

You can use variables in data links to send people to a detailed dashboard with
preserved data filters. For example, you can use variables to specify a time range,
series, and variable selection. For more information, see [Data link variables](linking-in-Amazon-Managed-Service-for-Grafana.md#data-link-variables "linking-in-Amazon-Managed-Service-for-Grafana.md#data-link-variables").

## Typeahead suggestions

When you create or update a data link, press **Ctrl+Space** or **Cmd+Space**Cmd+Space on
your keyboard to open the typeahead suggestions to more easily add variables to your
URL.

## Adding a data link

1. Pause on the panel that you want to add a link to, and then press
   **e**. Or choose the dropdown arrow next to the panel
   title, and then choose **Edit**.
2. On the **Field** tab, scroll down to the **Data
   links** section.
3. Expand **Data links**, and then choose **Add
   link**.
4. Enter a **Title** for the link. The title will be
   displayed in the UI.
5. Enter the **URL** that you want to link to.

You can add one of the template variables that are defined in the
dashboard. Choose the **URL** field, and then type
**$**, or press Ctrl+Space or **Cmd+Space** to see a list of
available variables. When you add template variables to your panel link, the
link sends the user to the right context, with the relevant variables
already set. For more information, see [Data link variables](linking-in-Amazon-Managed-Service-for-Grafana.md#data-link-variables "linking-in-Amazon-Managed-Service-for-Grafana.md#data-link-variables"). 6. To open in a new tab, select **Open in a new tab**. 7. Choose **Save** to save changes and close the window. 8. Choose **Save** in the upper right to save your changes
to the dashboard.

## Updating a data link

1. On the **Field** tab, find the link that you want to
   make changes to.
2. Choose the **Edit** (pencil) icon to open the
   **Edit link** window.
3. Make any necessary changes.
4. Choose **Save** to save changes and close the window.
5. Choose **Save** in the upper right to save your changes
   to the dashboard.

## Deleting a data link

1. On the **Field** tab, find the link that you want to
   delete.
2. Choose the **X** icon next to the link that you want to
   delete.
3. Choose **Save** in the upper right to save your changes
   to the dashboard.
