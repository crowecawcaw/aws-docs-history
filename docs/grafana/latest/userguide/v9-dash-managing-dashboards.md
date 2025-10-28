# Managing dashboards

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

A dashboard is a set of one or more [panels](v9-panels.md "v9-panels.md")
that visually presents your data in one or more rows.

For more information about creating dashboards, see Add and
organize panels.

## Creating dashboard folders

Folders help you organize and group dashboards, which is useful when you have many
dashboards or multiple teams using the same Grafana instance.

**Prerequisites**

Ensure that you have Grafana Admin permissions. For more
information about dashboard permissions, see [Dashboard permissions](Grafana-administration-authorization.md "Grafana-administration-authorization.md").

**To create a dashboard folder**

1. Sign in to Grafana and on the side menu, click **Dashboards > New folder**
2. Enter a unique name and click **Create**.

###### Note

When you save a dashboard, you can either select a folder for the dashboard to
be saved in or create a new folder.

## Managing dashboards and

folders

On the **Manage dashboards and folders** page, you
can:

- Create a folder
- Create a dashboard
- Move dashboards into folders
- Delete multiple dashboards
- Navigate to a folder page where you can assign folder and dashboard
  permissions

**Dashboard folder page**

You can complete the following tasks on the **Dashboard
Folder** page:

- Move or delete dashboards in a folder.
- Rename a folder (available under the **Settings** tab).
- Assign permissions to folders (which are inherited by the dashboards in
  the folder).

To navigate to the dashboard folder page, click the cog appears when you hover
over a folder in the dashboard search result list or the **Manage dashboards and folders** page.

**Dashboard permissions**

You can assign permissions to a folder. Any permissions you assign are inherited
by the dashboards in the folder. An Access Control List (ACL) is used where
**Organization Role**, **Team**, and a **User** can be assigned
permissions.

See [permissions](Grafana-permissions.md "Grafana-permissions.md") for more information.

## Exporting and importing

dashboards

You can use the Grafana UI or the HTTP API to export and import dashboards.

**Exporting a dashboard**

The dashboard export action creates a Grafana JSON file that contains everything
you need, including layout, variables, styles, data sources, queries, and so on, so
that you can later import the dashboard.

###### Note

Grafana downloads a JSON file to your local machine.

1. Open the dashboard that you want to export.
2. Select the share icon.
3. Choose **Export**.
4. Choose **Save to file.**

**Making a dashboard portable**

If you want to export a dashboard for others to use, you can add template
variables for things like a metric prefix (use a constant variable) and server
name.

A template variable of the type `Constant` will automatically be hidden
in the dashboard, and will also be added as a required input when the dashboard is
imported.

**Importing a dashboard**

1.  Choose **Dashboards** in the side
    menu.
2.  Choose **New**, then select **Import** from the dropdown menu.
3.  Perform one of the following steps.

        * Upload a dashboard JSON file.
        * Paste a [Grafana.com](https://grafana.com/ "https://grafana.com/")
         dashboard URL.
        * Paste dashboard JSON text directly into the text area.

    The import process enables you to change the name of the dashboard, pick
    the data source you want the dashboard to use, and specify any metric
    prefixes (if the dashboard uses any).

## Troubleshooting dashboards

This section provides information to help you solve common dashboard problems.

**Dashboard is slow**

If your dashboard is slow, consider the following:

- Are you trying to render dozens (or hundreds or thousands) of time-series
  on a graph? This can cause the browser to lag. Try using functions like
  highestMax (in Graphite) to reduce the returned series.

- Sometimes the series names can be very large. This causes larger response
  sizes. Try using alias to reduce the size of the returned series
  names.
- Are you querying many time-series or for a long range of time? Both of
  these conditions can cause Grafana or your data source to pull in a lot of
  data, which can slow it down.
- It could be high load on your network infrastructure. If the slowness
  isn’t consistent, this might be the problem.

**Dashboard refresh rate issues**

By default, Grafana queries your data source every 30 seconds. Setting a low
refresh rate on your dashboards puts unnecessary stress on the backend. In many
cases, querying this frequently isn’t necessary because the data isn’t being sent to
the system such that changes would be seen.

If you have this issue, the following solutions are recommended.

- Do not enable auto-refreshing on dashboards, panels, or variables unless
  you need it. Users can refresh their browser manually, or you can set the
  refresh rate for a time period that makes sense (such as very ten minutes or
  every hour).
- If it is required, then set the refresh rate to once a minute. Users can
  always refresh the dashboard manually.
- If your dashboard has a longer time period (such as one week), then
  automated refreshing might not be necessary.

**Handling or rendering null data is wrong or
confusing**

Some applications publish data intermittently. For example, they only post a
metric when an event occurs. By default, Grafana graphs connect lines between the
data points.
