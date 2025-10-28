# Panel links

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

Each panel can have its own set of links that are shown in the upper-left corner of
the panel. You can link to any available URLs, including dashboards, panels, or external
sites. You can even control the time range to ensure the user sees the specific data in
the Grafana workspace.

Choose the icon in the top-left corner of a panel to see available panel links.

## Adding a panel link

1. Pause on the panel that you want to add a link to, and then press
   **e**. Or choose the dropdown arrow next to
   the panel title, and then choose **Edit**.
2. On the **Panel** tab, scroll down to the
   **Links** section.
3. Expand **Links**, and then choose **Add
   link**.
4. Enter a **Title** for the link. The title will be
   displayed in the UI.
5. Enter the **URL** that you want to link to. You can
   include one of the template variables that are defined in the dashboard.
   Press **Ctrl+Space** or **Cmd+Space**, and then choose the **URL**
   field to see the available variables. When you add template variables to
   your panel link, the link sends the user to the right context, with the
   relevant variables already set. You can also use time variables
   - `from` defines the lower limit of the time range,
     specified in ms epoch.
   - `to` defines the upper limit of the time range, specified
     in ms epoch.
   - `time` and `time.window` define a time range
     from `time-time.window/2` to
     `time+time.window/2`. Both parameters should be
     specified in milliseconds. For example,
     `?time=1500000000000&time.window=10000` results
     in a 10-second time range from 1499999995000 to 1500000005000.

6. To open in a new tab, select **Open in a new tab**.
7. Choose **Save** to save changes and close the window.
8. Choose **Save** in the upper right to save your changes
   to the dashboard.

## Updating a panel link

1. On the **Panel** tab, find the link that you want to
   make changes to.
2. Choose the **Edit** (pencil) icon to open the
   **Edit link** window.
3. Make any necessary changes.
4. Choose **Save** to save changes and close the window.
5. Choose **Save** in the upper right to save your changes
   to the dashboard.

## Deleting a panel link

1. On the **Panel** tab, find the link that you want to
   delete.
2. Choose the **X** icon next to the link that you want to
   delete.
3. Choose **Save** in the upper right to save your changes
   to the dashboard.
