

# Managing playlists
<a name="v13-dash-managing-playlists"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 13.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).

A *playlist* is a list of dashboards that are displayed in a sequence. You might use a playlist to build situational awareness or to present your metrics to your team or visitors. Grafana automatically scales dashboards to any resolution, which makes them perfect for large screens. You can access the playlist feature from Grafana's side menu in the **Dashboards** submenu.

## Accessing, sharing, and controlling a playlist
<a name="v13-dash-access-share-control-playlist"></a>

Use the information in this section to access existing playlists. Start and control the display of a playlist by choosing a display mode and options.

**To access a playlist**

1. Select **Playlists** from the left menu.

1. Choose a playlist from the list of existing playlists.

**Starting a playlist**

When you start a playlist, the **Start playlist** dialog box lets you choose how the dashboards are displayed. You select a **Mode** and can turn additional display options on or off. Your selections determine how the menus, navigation bar, and dashboard controls appear while the playlist runs.

By default, each dashboard is displayed for the amount of time entered in the **Interval** field, which you set when you create or edit a playlist. After you start a playlist, you can control it with the navigation bar at the top of the page.

**To start a playlist**

1. Access the playlist page to see a list of existing playlists.

1. Find the playlist that you want to start, then click **Start playlist**.

   The **Start playlist** dialog box opens.

1. Select a **Mode** and set any display options, based on the information in the following table.

1. Click **Start <playlist name>**.

The playlist displays each dashboard for the time specified in the `Interval` field, set when creating or editing a playlist. After a playlist starts, you can control it using the navigation bar at the top of your screen.

The **Start playlist** dialog box provides the following options.


| Option | Description | 
| --- | --- | 
| **Mode** |  +  **Normal** – The side menu and the dashboard navigation bar and controls remain visible. <br />+  **Kiosk** – The side menu, navigation bar, and dashboard controls are hidden for a distraction-free display, such as on a wall-mounted screen or a shared monitor.   | 
| **Autofit** | Adjusts panel heights to fit the screen size. Available in both modes. | 
| **Hide logo** | Available in **Kiosk** mode only. Hides the branding footer from the dashboard. | 
| **Navigation buttons** | Shows the previous and next buttons so that you can manually navigate between the dashboards in the playlist. | 
| **Display dashboard controls** | Controls which dashboard elements remain visible. Each option is enabled by default; clear an option to hide that element.+  **Time and refresh** – The time picker and refresh control. <br />+  **Variables** – The dashboard variable dropdown lists. <br />+  **Dashboard links** – The dashboard links.  | 

**Controlling a playlist**

After a playlist starts, you can control it using the navigation controls at the top of your screen. Press the `Esc` key to stop the playlist.


| Control | Action | 
| --- | --- | 
| Next (forward arrow) | Advances to the next dashboard. | 
| Previous (back arrow) | Returns to the previous dashboard. | 
| Stop playlist | Ends the playlist and returns to the current dashboard. | 
| Time range | The standard dashboard time picker, shown when **Time and refresh** is enabled. Displays data within a selected relative or custom time range. | 
| Refresh | The standard dashboard refresh control, shown when **Time and refresh** is enabled. Reloads the dashboard to display current data, with an optional auto-refresh interval. | 

## Creating a playlist
<a name="v13-dash-create-playlist"></a>

You can create a playlist to present dashboards in a sequence with a set order and time interval between dashboards.

**To create a playlist**

1. Select **Dashboards** from the left menu.

1. Select **Playlists** on the playlist page.

1. Select **New playlist**.

1. Enter a descriptive name in the **Name** text box.

1. Enter a time interval in the **Interval** text box. The dashboards you add are listed in a sequential order.

1. In **Dashboards**, add existing dashboards to the playlist using the **Add by title** and **Add by tag** dropdown options.

1. Optionally:
   + Search for a dashboard by its name, a regular expression, or a tag.
   + Filter your results by starred status or tags.
   + Rearrange the order of the dashboards you have added using the up and down arrow icon.
   + Remove a dashboard from the playlist by clicking the **x** icon beside the dashboard.

1. Select **Save** to save your changes.

## Saving a playlist
<a name="v13-dash-save-playlist"></a>

You can save a playlist and add it to your **Playlists** page, where you can start it.

**Important**  
Ensure all the dashboards that you want to appear in your playlist are added when creating or editing the playlist before saving it.

**To save a playlist**

1. Select **Dashboards** in the left menu.

1. Select **Playlists** to view the playlists available to you.

1. Choose the playlist of your choice.

1. Edit the playlist.

1. Check that the playlist has a **Name**, **Interval**, and at least one **Dashboard** added to it.

1. Select **Save** to save your changes.

## Editing or deleting a playlist
<a name="v13-dash-edit-delete-playlist"></a>

You can edit a playlist by updating its name, interval time, and by adding, removing, and rearranging the order of dashboards, or you can delete the playlist.

**To edit a playlist**

1. Select **Edit playlist** on the playlist page.

1. Update the name and time interval, then add or remove dashboards from the playlist using instructions in Create a playlist, above.

1. Select **Save** to save your changes.

**To delete a playlist**

1. Select **Playlists**.

1. Select **Remove** next to the playlist you want to delete.

**To rearrange dashboard order in a playlist**

1. Next to the dashboard you want to move, click the up or down arrow.

1. Select **Save** to save your changes.

**To remove a dashboard**

1. Select **Remove** to remove a dashboard from the playlist.

1. Select **Save** to save your changes.

## Sharing a playlist in view mode
<a name="v13-dash-share-playlist-view-mode"></a>

You can share a playlist by copying the link address on the view mode you prefer, and pasting the URL to your destination.

**To share a playlist in view mode**

1. From the **Dashboards** left side menu, choose **Playlists**.

1. Select **Start playlist** next to the playlist you want to share.

1. In the dropdown, right click the view mode you prefer.

1. Select **Copy Link Address** to copy the URL to your clipboard.

1. Paste the URL to your destination.