# Sharing dashboards and panels

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Grafana enables you to share dashboards and panels with other users within an
organization and in certain situations, publicly on the Web. You can share using:

- A direct link
- A snapshot
- An export link (for dashboards only)
  You must have an authorized viewer permission to see an image rendered by a direct
  link.

The same permission is also required to view embedded links unless you have anonymous
access permission enabled for your Grafana instance.

When you share a panel or dashboard as a snapshot, a snapshot (which is a panel or
dashboard at the moment you take the snapshot) is publicly available on the web. Anyone
with a link to it can access it. Because snapshots do not require any authorization to
view, Grafana removes information related to the account it came from, as well as any
sensitive data from the snapshot.

## Sharing a dashboard

You can share a dashboard as a direct link or as a snapshot. You can also
export a dashboard.

###### Note

If you change a dashboard, ensure that you save the changes before
sharing.

1. Navigate to the home page of your Grafana instance.
2. Click on the share icon in the top navigation.

The share dialog box will open and show the **Link** tab.

**Sharing a direct link**

The **Link** tab shows the current time range,
template variables, and the default theme. You can also share a shortened
URL.

1. Click **Copy**. This action copies the
   default or the shortened URL to the clipboard.
2. Send the copied URL to a Grafana user with authorization to view the
   link.

**Publishing a snapshot**

A dashboard snapshot shares an interactive dashboard publicly. Grafana strips
sensitive data such as queries (metric, template, and annotation) and panel links,
leaving only the visible metric data and series names embedded in the dashboard.
Dashboard snapshots can be accessed by anyone with the link.

You can publish snapshots to your local instance.

1. Click **Local Snapshot**.
2. Grafana generates a link of the snapshot. Copy the snapshot link, and
   share it either within your organization or publicly on the web.

**Exporting a dashboard**

Grafana dashboards can easily be exported and imported. For more information, see
[Export and import
dashboards](v9-dash-managing-dashboards.md#v9-dash-export-import-dashboards "v9-dash-managing-dashboards.md#v9-dash-export-import-dashboards").

## Sharing a panel

You can share a panel as a direct link, or as a snapshot. You
can also create library panels using the **Share**
option on any panel.

1. Click a panel title to open the panel menu.
2. Click **Share**. The share dialog box will open
   and show the **Link** tab.

**Using a direct link**

The **Link** tab shows the current time range,
template variables, and the default theme. You can optionally enable a shortened URL
to share.

1. Click **Copy** to copy the default or the
   shortened URL to the clipboard.
2. Send the copied URL to a Grafana user with authorization to view the
   link.
3. You also optionally click **Direct link rendered
   image** to share an image of the panel.

**Querying string parameters for server-side rendered
images**

- **width**: Width in pixels. The default is

800.

- **height**: Height in pixels. The default is

400.

- **tz**: Timezone in the format
  `UTC%2BHH%3AMM` where HH and MM are offset in hours and
  minutes after UTC.
- **timeout**: Number of seconds. The timeout
  can be increased if the query for the panel needs more than the default 30
  seconds.
- **scale**: Numeric value to configure device
  scale factor. Default is 1. Use a higher value to produce more detailed
  images (higher DPI). Supported in Grafana v7.0+.

**Publishing a snapshot**

A panel snapshot shares an interactive panel publicly. Grafana strips sensitive
data leaving only the visible metric data and series names embedded in the
dashboard. Panel snapshots can be accessed by anyone with the link

You can publish snapshots to your local instance.

1. In the **Share Panel** dialog box, click
   **Snapshot** to open the tab.
2. Click **Local Snapshot**. Grafana
   generates the link of the snapshot.
3. Copy the snapshot link, and share it either within your organization or
   publicly on the web.

If you created a snapshot by mistake, click **Delete
snapshot** to remove the snapshot from your Grafana instance.

**Creating a library panel**

To create a library panel from the **Share Panel** dialog box.

1. Click **Library panel**.
2. In **Library panel name**, enter the
   name.
3. In **Save in folder**, select the folder in
   which to save the library panel. By default, the **General** folder is selected.
4. Click **Create library** panel to save your
   changes.
5. Click **Save** to save the dashboard.
