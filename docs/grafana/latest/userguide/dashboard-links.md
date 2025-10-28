# Dashboard links

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

When you create a dashboard link, you can include the time range and current template
variables to directly jump to the same context in another dashboard. This helps to
ensure that the person you send the link to is looking at the right data. For other
types of links, see [Data link variables](linking-in-Amazon-Managed-Service-for-Grafana.md#data-link-variables "linking-in-Amazon-Managed-Service-for-Grafana.md#data-link-variables").

After you add a dashboard link, it appears in the upper-right corner of your
dashboard.

## Adding links to dashboards

Add links to other dashboards at the top of your current dashboard.

1. While viewing the dashboard that you want to add a link to, choose the
   gear icon at the top of the screen to open **Dashboard
   settings**.
2. Choose **Links**, and then choose **Add
   Dashboard Link** or **New**.
3. In **Type**, select **dashboards**.
4. Select link options:
   - With tags – Enter tags to limit
     the linked dashboards to only the ones with the tags you enter.
     Otherwise, the Grafana workspace includes links to all other
     dashboards.
   - As dropdown – Select this
     option if you are linking to many dashboards, and add an optional
     title to the dropdown list. If this option is not selected, the
     Grafana workspace displays the dashboard links side by side across
     the top of your dashboard.
   - Time range – Select this option
     to include the dashboard time range in the link. When the user
     chooses the link, the linked dashboard opens with the indicated time
     range already set.
   - Variable values – Select this
     option to include the template variables that are currently used as
     query parameters in the link. When the user chooses the link, any
     matching templates in the linked dashboard are set to the values
     from the link.
   - Open in new tab – Select this
     option to open the dashboard link in a new tab or window.

5. Choose **Add**.

## Adding a URL link to a

dashboard

Add a link to a URL at the top of your current dashboard. You can link to any
available URL, including dashboards, panels, or external sites. You can even control
the time range to ensure that the user sees the specific data in the Grafana
workspace.

1. While viewing the dashboard that you want to link to, choose the gear
   icon at the top of the screen to open **Dashboard
   settings**.
2. Choose **Links**, and then choose **Add
   Dashboard Link** or **New**.
3. In **Type**, select **link**.
4. Select link options:
   - Url – Enter the URL that you
     want to link to. Depending on the target, you might want to include
     field values.
   - Title – Enter the title that
     you want the link to display.
   - Tooltip – Enter the tooltip
     that you want the link to display when the user pauses over it.
   - Icon – Choose the icon that you
     want to display with the link.
   - Time range – Select this option
     to include the dashboard time range in the link. When the user
     chooses the link, the linked dashboard opens with the indicated time
     range already set.
     - `from` defines the lower limit of the time range,
       specified in ms epoch.
     - `to` defines the upper limit of the time range,
       specified in ms epoch.
     - `time` and `time.window` define a time
       range from `time-time.window/2` to
       `time+time.window/2`. Both parameters should
       be specified in milliseconds. For example,
       `?time=1500000000000&time.window=10000`
       results in a 10-second time range from 1499999995000 to
     1500000005000.

   - Variable values – Select this
     option to include the template variables that are currently used as
     query parameters in the link. When the user chooses the link, any
     matching templates in the linked dashboard are set to the values
     from the link; for example,
     https://play.grafana.org/d/000000074/alerting?var-app=backend&var-server=backend\_01&var-server=backend\_03&var-interval=1h
   - Open in new tab – Select this
     option to open the dashboard link in a new tab or window.

5. Choose **Add**.

## Updating a dashboard link

To change or update an existing dashboard link, use the following procedure.

1. In **Dashboard Settings**, on the
   **Links** tab, choose the existing link that you want
   to edit.
2. Change the settings, and then choose **Update**.

## Duplicating a dashboard link

To duplicate an existing dashboard link, choose the duplicate icon next to the
existing link that you want to duplicate.

## Deleting a dashboard link

To delete an existing dashboard link, choose the trash can icon for the link that
you want to delete.
