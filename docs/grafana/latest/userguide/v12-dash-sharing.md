

# Sharing dashboards and panels
<a name="v12-dash-sharing"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 12.x**.  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

Grafana enables you to share dashboards and panels with other users within an organization and in certain situations, publicly on the Web. You can share using:
+ A direct link
+ A snapshot
+ An export link (for dashboards only)

You must have an authorized viewer permission to see an image rendered by a direct link.

When you share a panel or dashboard as a snapshot, a snapshot (which is a panel or dashboard at the moment you take the snapshot) is publicly available on the web. Anyone with a link to it can access it. Because snapshots do not require any authorization to view, Grafana removes information related to the account it came from, as well as any sensitive data from the snapshot.

## Sharing a dashboard
<a name="v12-dash-share-dashboard"></a>

You can share a dashboard as a direct link or as a snapshot. You can also export a dashboard. The sharing workflow includes customizable shareable panel images and a streamlined interface.

**Note**  
If you change a dashboard, ensure that you save the changes before sharing.

**To Share a dashboard**

1. Select **Dashboards** from the left menu in your workspace.

1. Choose the dashboard you want to share.

1. Select the share icon at the top of the screen.

   The share dialog box opens and shows the **Link** tab.

**Sharing a direct link**

The **Link** tab shows the current time range, template variables, and the default theme. You can also share a shortened URL.

**To share a directly link**

1. Select **Copy**. This action copies the default or the shortened URL to the clipboard.

1. Send the copied URL to a Grafana user with authorization to view the link.

**Publishing a snapshot**

A dashboard snapshot shares an interactive dashboard publicly. Grafana strips sensitive data such as queries (metric, template, and annotation) and panel links, leaving only the visible metric data and series names embedded in the dashboard. Dashboard snapshots can be accessed by anyone with the link.

You can publish snapshots to your local instance.

**To publish a snapshot**

1. Select the **Snapshot** tab.

1. Select the **Local Snapshot**.

1. Grafana generates a link of the snapshot. Copy the snapshot link, and share it either within your organization or publicly on the web.

**Exporting a dashboard**

Grafana dashboards can easily be exported and imported. For more information, see the import and export sections in [Building dashboards](v12-dash-building-dashboards.md).

## Sharing a panel
<a name="v12-dash-share-panel"></a>

You can share a panel as a direct link, or as a snapshot. You can also create library panels using the **Share** option on any panel.

**To share a panel**

1. Select the panel title of the panel you want to share. The panel menu opens.

1. Select **Share**. The share dialog box will open and show the **Link** tab.

**Using a direct link**

The **Link** tab shows the current time range, template variables, and the default theme. You can optionally enable a shortened URL to share.

**To use a direct link**

1. Select **Copy** to copy the default or the shortened URL to the clipboard. 

1. Send the copied URL to a Grafana user with authorization to view the link.

**Publishing a snapshot of a panel**

A panel snapshot is a share of an interactive panel publicly. Grafana strips sensitive data leaving only the visible metric data and series names embedded in the dashboard. Panel snapshots can be accessed by anyone with the link.

You can publish snapshots to your local instance.

**To publish a snapshot of a panel**

1. In the **Share Panel** dialog box, select the **Snapshot** tab.

1. Select **Local Snapshot**. Grafana generates the link of the snapshot.

1. Copy the snapshot link, and share it either within your organization or publicly on the web.

If you created a snapshot by mistake, click **Delete snapshot** to remove the snapshot from your Grafana instance.

**Creating a library panel**

To create a library panel from the **Share Panel** dialog box.

**To create a library panel**

1. Select **Library panel**.

1. In **Library panel name**, enter the name.

1. In **Save in folder**, select the folder in which to save the library panel. By default, the root folder is selected.

1. Select **Create library panel** to save your changes.

1. Save the dashboard.